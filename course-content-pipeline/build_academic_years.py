import openpyxl
from openpyxl.styles import PatternFill, Font, Alignment
from openpyxl.formatting.rule import FormulaRule
from openpyxl.utils import get_column_letter
from copy import copy

SRC = "Jadwal_TRA_Sistem.xlsx"

wb = openpyxl.load_workbook(SRC, data_only=False)

# ---- 1. Rename existing schedule sheets into the new academic-year naming ----
RENAME = {
    "Semester 1": "Gasal 26-27 Sem1",
    "Semester 3": "Gasal 26-27 Sem3",
    "Semester 5": "Gasal 27-28 Sem5",
}
for old, new in RENAME.items():
    wb[old].title = new

# Drop Semester 7 (empty template, not part of the requested periods)
if "Semester 7" in wb.sheetnames:
    del wb["Semester 7"]

TEMPLATE_NAME = "Gasal 27-28 Sem5"  # empty template used as base for new empty sheets

# ---- 2. Create new empty schedule sheets by copying the empty template ----
NEW_SHEETS = [
    ("Genap 26-27 Sem2", "2"),
    ("Genap 26-27 Sem4", "4"),
    ("Gasal 27-28 Sem1", "1"),
    ("Gasal 27-28 Sem3", "3"),
]

template_ws = wb[TEMPLATE_NAME]
tmpl_col_widths = {k: v.width for k, v in template_ws.column_dimensions.items()}
tmpl_freeze = template_ws.freeze_panes
tmpl_dvs = list(template_ws.data_validations.dataValidation)
tmpl_max_row = template_ws.max_row

for name, sem_num in NEW_SHEETS:
    ws = wb.copy_worksheet(template_ws)
    ws.title = name
    # restore column widths (copy_worksheet does not carry these over)
    for col, width in tmpl_col_widths.items():
        ws.column_dimensions[col].width = width
    ws.freeze_panes = tmpl_freeze
    # restore data validations (dropdowns for Hari / Dosen Kode)
    for dv in tmpl_dvs:
        new_dv = openpyxl.worksheet.datavalidation.DataValidation(
            type=dv.type, formula1=dv.formula1, allow_blank=dv.allow_blank
        )
        new_dv.sqref = dv.sqref
        ws.add_data_validation(new_dv)
    # fix "Semester" literal column (B) to the correct semester number
    for r in range(2, tmpl_max_row + 1):
        ws.cell(row=r, column=2, value=sem_num)

# ---- 3. Tab colors per Tahun Akademik period ----
PERIOD_SHEETS = {
    "Gasal 26-27": ["Gasal 26-27 Sem1", "Gasal 26-27 Sem3"],
    "Genap 26-27": ["Genap 26-27 Sem2", "Genap 26-27 Sem4"],
    "Gasal 27-28": ["Gasal 27-28 Sem1", "Gasal 27-28 Sem3", "Gasal 27-28 Sem5"],
}
PERIOD_COLOR = {
    "Gasal 26-27": "1F4E78",  # blue
    "Genap 26-27": "375623",  # green
    "Gasal 27-28": "833C00",  # orange
}
SHEET_PERIOD = {}
for period, sheets in PERIOD_SHEETS.items():
    for s in sheets:
        SHEET_PERIOD[s] = period
        wb[s].sheet_properties.tabColor = PERIOD_COLOR[period]

# ---- 4. Per-sheet conflict conditional formatting, scoped to its own period ----
YELLOW = PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid")
for period, sheets in PERIOD_SHEETS.items():
    for s in sheets:
        ws = wb[s]
        # remove any pre-existing CF rules (the copied template carries the old one)
        ws.conditional_formatting._cf_rules.clear()
        max_r = max(ws.max_row, 31)
        terms = []
        for other in sheets:
            terms.append(
                f"COUNTIFS('{other}'!$D$2:$D$500,$D2,'{other}'!$E$2:$E$500,$E2,"
                f"'{other}'!$J$2:$J$500,$J2)"
            )
        formula = f'AND($J2<>"",({"+".join(terms)})>1)'
        ws.conditional_formatting.add(
            f"A2:K{max_r}", FormulaRule(formula=[formula], fill=YELLOW)
        )

# ---- 5. Rename Overview -> Overview Gasal 26-27 (data unchanged, static snapshot) ----
if "Overview" in wb.sheetnames:
    ov = wb["Overview"]
    ov.title = "Overview Gasal 26-27"
    ov.sheet_properties.tabColor = PERIOD_COLOR["Gasal 26-27"]
    for row in ov.iter_rows():
        for c in row:
            if isinstance(c.value, str) and "sheet Semester 1/3/5/7" in c.value:
                c.value = c.value.replace(
                    "sheet Semester 1/3/5/7",
                    "sheet 'Gasal 26-27 Sem1' dan 'Gasal 26-27 Sem3'",
                ).replace(
                    "lintas semua semester",
                    "lintas semester dalam periode Gasal 26-27"
                )

# ---- 6. Update Daftar Dosen Total SKS / Jumlah Sesi formulas to cover all 7 sheets ----
ALL_SHEETS = (
    PERIOD_SHEETS["Gasal 26-27"] + PERIOD_SHEETS["Genap 26-27"] + PERIOD_SHEETS["Gasal 27-28"]
)
dd = wb["Daftar Dosen"]
for r in range(2, dd.max_row + 1):
    sum_terms = "+".join(
        f"SUMIF('{s}'!$J:$J,A{r},'{s}'!$I:$I)" for s in ALL_SHEETS
    )
    cnt_terms = "+".join(f"COUNTIF('{s}'!$J:$J,A{r})" for s in ALL_SHEETS)
    dd.cell(row=r, column=3, value=f'=IF(A{r}="","",{sum_terms})')
    dd.cell(row=r, column=4, value=f'=IF(A{r}="","",{cnt_terms})')

# ---- 7. Build "Daftar Mata Kuliah" master sheet ----
if "Daftar Mata Kuliah" in wb.sheetnames:
    del wb["Daftar Mata Kuliah"]
dmk = wb.create_sheet("Daftar Mata Kuliah")

seen = {}
order = []
for s in ["Gasal 26-27 Sem1", "Gasal 26-27 Sem3"]:
    ws = wb[s]
    for r in range(2, ws.max_row + 1):
        kode = ws.cell(row=r, column=7).value
        mk = ws.cell(row=r, column=8).value
        sks = ws.cell(row=r, column=9).value
        sem = ws.cell(row=r, column=2).value
        if not kode or not mk:
            continue
        if kode not in seen:
            seen[kode] = {"mk": mk, "sks": sks, "sem": sem}
            order.append(kode)

headers = ["Kode MK", "Mata Kuliah", "SKS", "Semester (biasanya)"]
header_fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
header_font = Font(bold=True, color="FFFFFF")
for i, h in enumerate(headers, start=1):
    c = dmk.cell(row=1, column=i, value=h)
    c.fill = header_fill
    c.font = header_font
    c.alignment = Alignment(horizontal="center")

for i, kode in enumerate(order, start=2):
    d = seen[kode]
    dmk.cell(row=i, column=1, value=kode)
    dmk.cell(row=i, column=2, value=d["mk"])
    dmk.cell(row=i, column=3, value=d["sks"])
    dmk.cell(row=i, column=4, value=d["sem"])

dmk.column_dimensions["A"].width = 10
dmk.column_dimensions["B"].width = 60
dmk.column_dimensions["C"].width = 7
dmk.column_dimensions["D"].width = 18
dmk.freeze_panes = "A2"

# ---- 8. Regenerate "Rekap Dosen" grouped by Tahun Akademik, with per-period conflict CF ----
if "Rekap Dosen" in wb.sheetnames:
    del wb["Rekap Dosen"]
rd = wb.create_sheet("Rekap Dosen", 0)

RD_HEADERS = [
    "No", "Tahun Akademik", "Semester", "Kelas", "Dosen (Nama)", "Dosen (Kode)",
    "Hari", "Jam Mulai", "Jam Selesai", "Kode MK", "Mata Kuliah", "SKS",
]
for i, h in enumerate(RD_HEADERS, start=1):
    c = rd.cell(row=1, column=i, value=h)
    c.fill = header_fill
    c.font = header_font
    c.alignment = Alignment(horizontal="center")

widths = {"A": 5, "B": 15, "C": 10, "D": 10, "E": 34, "F": 10, "G": 10,
          "H": 10, "I": 11, "J": 10, "K": 52, "L": 7}
for col, w in widths.items():
    rd.column_dimensions[col].width = w
rd.freeze_panes = "A2"

no = 1
period_row_ranges = {}  # period -> (first_row, last_row)
for period, sheets in PERIOD_SHEETS.items():
    start_row = rd.max_row + 1
    entries = []
    for s in sheets:
        ws = wb[s]
        for r in range(2, ws.max_row + 1):
            kode_dosen = ws.cell(row=r, column=10).value
            if not kode_dosen:
                continue
            entries.append((s, r, ws.cell(row=r, column=11).value or ""))
    entries.sort(key=lambda e: e[2])  # sort by dosen nama (formula string, best effort)

    for s, r, _ in entries:
        row = rd.max_row + 1
        rd.cell(row=row, column=1, value=no)
        rd.cell(row=row, column=2, value=period)
        rd.cell(row=row, column=3, value=f"='{s}'!B{r}")
        rd.cell(row=row, column=4, value=f"='{s}'!C{r}")
        rd.cell(row=row, column=5, value=f"='{s}'!K{r}")
        rd.cell(row=row, column=6, value=f"='{s}'!J{r}")
        rd.cell(row=row, column=7, value=f"='{s}'!D{r}")
        rd.cell(row=row, column=8, value=f"='{s}'!E{r}")
        rd.cell(row=row, column=9, value=f"='{s}'!F{r}")
        rd.cell(row=row, column=10, value=f"='{s}'!G{r}")
        rd.cell(row=row, column=11, value=f"='{s}'!H{r}")
        rd.cell(row=row, column=12, value=f"='{s}'!I{r}")
        no += 1
    end_row = rd.max_row
    if end_row >= start_row:
        period_row_ranges[period] = (start_row, end_row)

# conflict highlight per period block, scoped to that period's own sheets
for period, (start_row, end_row) in period_row_ranges.items():
    sheets = PERIOD_SHEETS[period]
    terms = [
        f"COUNTIFS('{s}'!$D$2:$D$500,$G{start_row},'{s}'!$E$2:$E$500,$H{start_row},"
        f"'{s}'!$J$2:$J$500,$F{start_row})"
        for s in sheets
    ]
    formula = f'AND($F{start_row}<>"",({"+".join(terms)})>1)'
    rd.conditional_formatting.add(
        f"A{start_row}:L{end_row}", FormulaRule(formula=[formula], fill=YELLOW)
    )

# ---- 9. Update Petunjuk sheet ----
pt = wb["Petunjuk"]
pt.delete_rows(1, pt.max_row)
lines = [
    "PETUNJUK PEMAKAIAN — SISTEM JADWAL DOSEN OTOMATIS",
    "",
    "STRUKTUR FILE:",
    "- Sheet jadwal dikelompokkan per Tahun Akademik (warna tab beda per periode):",
    "  * Gasal 26-27 (biru): 'Gasal 26-27 Sem1', 'Gasal 26-27 Sem3'",
    "  * Genap 26-27 (hijau): 'Genap 26-27 Sem2', 'Genap 26-27 Sem4'",
    "  * Gasal 27-28 (oranye): 'Gasal 27-28 Sem1', 'Gasal 27-28 Sem3', 'Gasal 27-28 Sem5'",
    "- 'Daftar Dosen' = master data dosen (kode + nama).",
    "- 'Daftar Mata Kuliah' = master data mata kuliah (kode, nama, SKS, semester biasanya).",
    "",
    "1. Input/edit jadwal HANYA di sheet jadwal per Tahun Akademik & Semester di atas.",
    "   Satu baris = satu sesi kelas (Hari, Jam, Mata Kuliah, Dosen). Kolom 'Dosen (Nama)'",
    "   otomatis terisi dari kode dosen lewat sheet 'Daftar Dosen'.",
    "2. Sheet 'Rekap Dosen' (tab pertama) adalah rekap otomatis semua jadwal, dikelompokkan",
    "   per Tahun Akademik. Sel-selnya berupa formula yang mengambil langsung dari sheet",
    "   jadwal — kalau data di sheet jadwal diubah, rekap ini ikut berubah otomatis.",
    "3. INDIKATOR BENTROK (kuning): baris otomatis berwarna KUNING kalau dosen yang sama",
    "   mengajar di HARI & JAM yang sama lebih dari satu kali — HANYA dicek di dalam",
    "   Tahun Akademik/periode yang sama (karena periode berbeda tidak berjalan bersamaan).",
    "4. Sheet 'Daftar Dosen' adalah master nama dosen. Tambah dosen baru di sini (kode +",
    "   nama lengkap), maka otomatis muncul sebagai pilihan dropdown di kolom 'Dosen (Kode)'",
    "   pada tiap sheet jadwal, dan Total SKS & Jumlah Sesi dosen tsb terhitung otomatis",
    "   lintas semua Tahun Akademik.",
    "5. Sheet 'Daftar Mata Kuliah' adalah master mata kuliah untuk referensi (kode, nama,",
    "   SKS, semester biasanya ditawarkan). Tambah mata kuliah baru di sini kalau perlu.",
    "6. Kolom 'Hari' dan 'Dosen (Kode)' di tiap sheet jadwal punya dropdown supaya",
    "   penulisan konsisten (penting untuk deteksi bentrok).",
    "7. Sheet 'Overview Gasal 26-27' adalah tampilan grid (mirip jadwal cetak) untuk",
    "   periode Gasal 26-27. Untuk periode lain, buat overview serupa setelah datanya",
    "   terisi (jalankan/adaptasi build_overview.py).",
]
for i, line in enumerate(lines, start=1):
    pt.cell(row=i, column=1, value=line)
pt.column_dimensions["A"].width = 110

# ---- 10. Reorder sheets ----
order = [
    "Rekap Dosen", "Overview Gasal 26-27", "Daftar Dosen", "Daftar Mata Kuliah",
    "Gasal 26-27 Sem1", "Gasal 26-27 Sem3",
    "Genap 26-27 Sem2", "Genap 26-27 Sem4",
    "Gasal 27-28 Sem1", "Gasal 27-28 Sem3", "Gasal 27-28 Sem5",
    "Petunjuk",
]
wb._sheets = [wb[name] for name in order]
wb.active = 0

wb.save(SRC)
print("Done. Sheets:", wb.sheetnames)
