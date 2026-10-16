#!/usr/bin/env python3
"""Bilingual practice-exercise PDFs for Digital_Technic_Logic meetings 10-13,
in lectures/meeting<N>/exercise/ (separate from exercises/ assignment PDFs)."""
from build_exercises import build_exercise_tex, compile_exercise

COURSE_NAME = "Digital Technic: Digital Logic Fundamentals"
COURSE_CODE = "AV0301DT"

MEETINGS = {
    10: {
        "topic": "Flip-Flop: Terminologi \\& Jenis (SR, D)",
        "subcpmk": "Sub-CPMK 5",
        "cpmk": "CPMK-3 (CPL-1)",
        "problems": [
            ("Foundational",
             r"Draw the truth table for an SR latch built from cross-coupled NOR gates (inputs $S,R$, output $Q$), and identify which input combination produces the forbidden/invalid state.",
             r"Gambarkan tabel kebenaran SR latch yang dibangun dari gerbang NOR bersilang (input $S,R$, output $Q$), dan identifikasi kombinasi input mana yang menghasilkan kondisi terlarang/tidak valid.",
             r"$S{=}0,R{=}0$: hold (no change). $S{=}1,R{=}0$: set, $Q{=}1$. $S{=}0,R{=}1$: reset, $Q{=}0$. $S{=}1,R{=}1$: \textbf{forbidden state} -- both $Q$ and $\overline{Q}$ are forced to 0, violating $Q\neq\overline{Q}$, and the next state is unpredictable when both inputs release simultaneously.",
             r"$S{=}0,R{=}0$: hold (tidak berubah). $S{=}1,R{=}0$: set, $Q{=}1$. $S{=}0,R{=}1$: reset, $Q{=}0$. $S{=}1,R{=}1$: \textbf{kondisi terlarang} -- $Q$ dan $\overline{Q}$ sama-sama dipaksa 0, melanggar $Q\neq\overline{Q}$, dan kondisi berikutnya tidak dapat diprediksi ketika kedua input dilepas bersamaan."),
            ("Application",
             r"A D flip-flop has $D=1$ held constant while five rising clock edges occur. State the value of $Q$ after each edge, and explain in one sentence why $Q$ never depends on how long $D$ was held between edges.",
             r"Sebuah D flip-flop memiliki $D=1$ konstan selama lima rising edge clock terjadi. Sebutkan nilai $Q$ setelah setiap edge, dan jelaskan dalam satu kalimat mengapa $Q$ tidak pernah bergantung pada berapa lama $D$ ditahan di antara edge.",
             r"\textbf{Answer:} $Q=1$ after every one of the five edges (it was already 1 after the first edge and stays 1). This is because a D flip-flop is edge-triggered: $Q$ only updates to the value of $D$ at the instant of the rising edge, so it is insensitive to $D$'s duration between edges (unlike a level-sensitive D latch).",
             r"\textbf{Jawaban:} $Q=1$ setelah setiap dari kelima edge (sudah 1 sejak edge pertama dan tetap 1). Ini karena D flip-flop bersifat edge-triggered: $Q$ hanya diperbarui ke nilai $D$ pada saat rising edge terjadi, sehingga tidak peka terhadap berapa lama $D$ ditahan di antara edge (berbeda dengan D latch yang level-sensitive)."),
            ("Analytical",
             r"An avionics engineer is designing a data-holding register for a flight-control bus and must choose between raw SR latches and D flip-flops for each storage bit. Explain why the SR latch is unsuitable for this role and how the D flip-flop's structure avoids the problem.",
             r"Seorang insinyur avionik merancang register penyimpan data untuk bus flight-control dan harus memilih antara SR latch mentah atau D flip-flop untuk setiap bit penyimpanan. Jelaskan mengapa SR latch tidak cocok untuk peran ini dan bagaimana struktur D flip-flop menghindari masalah tersebut.",
             r"An SR latch is unsuitable because control logic driving $S$ and $R$ could accidentally assert both simultaneously (glitch, race, or logic-design error), landing the bus register in the forbidden state with unpredictable resolved output -- unacceptable for flight-critical data integrity. A D flip-flop internally derives complementary drive signals from a single $D$ input (often via a master-slave SR pair with inverted internal control), so by construction $S$ and $R$ can never both be asserted at the same time -- the forbidden state is structurally impossible, and the single $D$ input plus clock gives fully deterministic, edge-synchronized storage.",
             r"SR latch tidak cocok karena logika kontrol yang menggerakkan $S$ dan $R$ bisa secara tidak sengaja mengaktifkan keduanya bersamaan (glitch, race, atau kesalahan desain logika), membuat register bus berada pada kondisi terlarang dengan output yang tidak dapat diprediksi -- tidak dapat diterima untuk integritas data flight-critical. D flip-flop secara internal menurunkan sinyal penggerak yang saling komplementer dari satu input $D$ (sering lewat pasangan SR master-slave dengan kontrol internal yang dibalik), sehingga secara konstruksi $S$ dan $R$ internal tidak pernah bisa aktif bersamaan -- kondisi terlarang secara struktural tidak mungkin terjadi, dan satu input $D$ plus clock memberikan penyimpanan yang sepenuhnya deterministik dan tersinkronisasi edge."),
        ],
    },
    11: {
        "topic": "Flip-Flop: Operasi (JK, T) \\& Aplikasi",
        "subcpmk": "Sub-CPMK 5",
        "cpmk": "CPMK-3 (CPL-1)",
        "problems": [
            ("Foundational",
             r"Complete the JK flip-flop's next-state behavior for each input pair: $J{=}0,K{=}0$; $J{=}1,K{=}0$; $J{=}0,K{=}1$; $J{=}1,K{=}1$. State which case resolves the SR flip-flop's forbidden state.",
             r"Lengkapi perilaku next-state JK flip-flop untuk setiap pasangan input: $J{=}0,K{=}0$; $J{=}1,K{=}0$; $J{=}0,K{=}1$; $J{=}1,K{=}1$. Sebutkan kasus mana yang menyelesaikan kondisi terlarang SR flip-flop.",
             r"$J{=}0,K{=}0$: hold. $J{=}1,K{=}0$: set ($Q{=}1$). $J{=}0,K{=}1$: reset ($Q{=}0$). $J{=}1,K{=}1$: \textbf{toggle} ($Q\to\overline{Q}$) -- this is the case that resolves the SR forbidden state, giving a well-defined output instead of an invalid one.",
             r"$J{=}0,K{=}0$: hold. $J{=}1,K{=}0$: set ($Q{=}1$). $J{=}0,K{=}1$: reset ($Q{=}0$). $J{=}1,K{=}1$: \textbf{toggle} ($Q\to\overline{Q}$) -- kasus inilah yang menyelesaikan kondisi terlarang SR, memberikan output yang terdefinisi dengan baik alih-alih tidak valid."),
            ("Application",
             r"A T flip-flop with $T=1$ permanently is driven by a 4\,kHz clock. What is the frequency of the output $Q$, and what circuit function does this single T flip-flop perform?",
             r"Sebuah T flip-flop dengan $T=1$ permanen digerakkan oleh clock 4\,kHz. Berapa frekuensi output $Q$, dan fungsi rangkaian apa yang dijalankan satu T flip-flop ini?",
             r"With $T=1$ held constant, the flip-flop toggles on every clock edge, so $Q$ changes state once per input cycle -- $\boldsymbol{f_Q = 4\text{kHz}/2 = 2\text{kHz}}$. This is a \textbf{divide-by-2 frequency divider} (the basic building block of a binary ripple counter).",
             r"Dengan $T=1$ ditahan konstan, flip-flop toggle pada setiap edge clock, sehingga $Q$ berubah keadaan sekali per siklus input -- $\boldsymbol{f_Q = 4\text{kHz}/2 = 2\text{kHz}}$. Ini adalah \textbf{pembagi frekuensi dibagi-2} (blok dasar pembentuk ripple counter biner)."),
            ("Analytical",
             r"An avionics team needs a low-part-count binary counter to count engine-shaft revolution pulses for RPM display. They choose to cascade four JK flip-flops, each configured with $J{=}K{=}1$ and clocked by the previous flip-flop's $Q$ output. Explain the counting mechanism, and identify one timing risk this ripple (asynchronous) arrangement introduces that a synchronous counter would avoid.",
             r"Tim avionik membutuhkan binary counter berjumlah komponen rendah untuk menghitung pulsa putaran poros mesin untuk tampilan RPM. Mereka memilih mencascade empat JK flip-flop, masing-masing dikonfigurasi $J{=}K{=}1$ dan di-clock oleh output $Q$ flip-flop sebelumnya. Jelaskan mekanisme penghitungan, dan identifikasi satu risiko timing yang ditimbulkan susunan ripple (asinkron) ini yang dapat dihindari oleh synchronous counter.",
             r"With $J{=}K{=}1$ each flip-flop toggles on every rising edge of its clock input; because each stage's clock is driven by the previous stage's $Q$ (which itself toggles at half the rate of the stage before it), the four stages together produce a 4-bit binary count of input pulses (0000 through 1111, wrapping). \textbf{Timing risk:} propagation delay accumulates stage-by-stage (ripple effect) -- after a pulse edge, the count briefly passes through incorrect intermediate binary states before settling, so if the count is sampled/displayed at exactly the wrong instant it can read a transient wrong value; a synchronous counter, where all flip-flops share one common clock, changes all bits simultaneously and avoids this ripple-through glitch.",
             r"Dengan $J{=}K{=}1$ setiap flip-flop toggle pada setiap rising edge clock inputnya; karena clock setiap tahap digerakkan oleh $Q$ tahap sebelumnya (yang sendiri toggle pada setengah laju tahap sebelumnya), keempat tahap bersama-sama menghasilkan hitungan biner 4-bit dari pulsa input (0000 hingga 1111, lalu berulang). \textbf{Risiko timing:} delay propagasi terakumulasi tahap demi tahap (efek ripple) -- setelah satu edge pulsa, hitungan sesaat melewati keadaan biner antara yang salah sebelum stabil, sehingga jika hitungan dibaca/ditampilkan tepat pada saat yang salah bisa terbaca nilai transien yang keliru; synchronous counter, di mana semua flip-flop berbagi satu clock bersama, mengubah semua bit secara serentak dan menghindari glitch ripple-through ini."),
        ],
    },
    12: {
        "topic": "Rangkaian Logika Sekuensial",
        "subcpmk": "Sub-CPMK 5",
        "cpmk": "CPMK-3 (CPL-1)",
        "problems": [
            ("Foundational",
             r"State the single defining difference between a combinational circuit and a sequential circuit, in terms of what determines the output.",
             r"Sebutkan satu perbedaan mendasar antara rangkaian kombinasional dan rangkaian sekuensial, dari segi apa yang menentukan output.",
             r"A combinational circuit's output depends \textbf{only} on the present input values. A sequential circuit's output depends on the present input \textbf{and} on the circuit's stored state (memory, i.e.\ flip-flops), so the same input can produce different outputs depending on history.",
             r"Output rangkaian kombinasional \textbf{hanya} bergantung pada nilai input saat ini. Output rangkaian sekuensial bergantung pada input saat ini \textbf{dan} pada state tersimpan rangkaian (memori, yaitu flip-flop), sehingga input yang sama dapat menghasilkan output berbeda tergantung riwayatnya."),
            ("Application",
             r"A 4-bit serial-in, parallel-out shift register is initially $0000$ and clocked while the serial input feeds the bit sequence $1,0,1,1$ (one bit per clock edge, earliest bit first). Give the register contents after each of the four clock edges.",
             r"Sebuah shift register 4-bit serial-in, parallel-out mulai dari $0000$ dan di-clock sementara input serial memasukkan urutan bit $1,0,1,1$ (satu bit per edge clock, bit paling awal duluan).Sebutkan isi register setelah setiap dari empat edge clock.",
             r"Each edge shifts all bits one position and inserts the new bit at the entry end: after bit 1 $\to 0001$; after bit 0 $\to 0010$; after bit 1 $\to 0101$; after bit 1 $\to 1011$. \textbf{Final contents: $1011$.}",
             r"Setiap edge menggeser semua bit satu posisi dan menyisipkan bit baru di ujung masuk: setelah bit 1 $\to 0001$; setelah bit 0 $\to 0010$; setelah bit 1 $\to 0101$; setelah bit 1 $\to 1011$. \textbf{Isi akhir: $1011$.}"),
            ("Analytical",
             r"A flight-critical timing subsystem must count fast pulse trains reliably. The design team is choosing between a ripple (asynchronous) counter and a synchronous counter built from the same JK flip-flops. Explain, from the sequential-circuit state-transition perspective, why the synchronous design is preferred for this application.",
             r"Subsistem pengaturan waktu flight-critical harus menghitung deretan pulsa cepat secara andal. Tim desain memilih antara ripple counter (asinkron) atau synchronous counter yang dibangun dari JK flip-flop yang sama. Jelaskan, dari perspektif transisi state rangkaian sekuensial, mengapa desain synchronous lebih disukai untuk aplikasi ini.",
             r"In a sequential circuit the \emph{next state} is only valid once every flip-flop has actually latched using the same reference clock edge. In a ripple counter, each flip-flop's clock is the previous stage's output, so the state transitions do not all happen at the same instant -- there is a cascaded delay before the whole register reflects the true new state, and during that window any external logic reading the count can sample an invalid transitional state. A synchronous counter drives every flip-flop from the identical global clock, so all bits transition together and the register's state is only ever observed as one of the intended, correctly-defined states -- essential when pulse rates are high enough that ripple delay becomes a significant fraction of the clock period.",
             r"Pada rangkaian sekuensial, \emph{state berikutnya} hanya valid setelah setiap flip-flop benar-benar meng-latch menggunakan edge clock referensi yang sama. Pada ripple counter, clock setiap flip-flop adalah output tahap sebelumnya, sehingga transisi state tidak terjadi pada saat yang sama persis -- ada delay bertingkat sebelum seluruh register merefleksikan state baru yang sebenarnya, dan selama jendela waktu itu logika eksternal yang membaca hitungan bisa membaca state transisi yang tidak valid. Synchronous counter menggerakkan setiap flip-flop dari clock global yang identik, sehingga semua bit bertransisi bersamaan dan state register hanya pernah teramati sebagai salah satu state yang dimaksud dan terdefinisi dengan benar -- penting ketika laju pulsa cukup tinggi sehingga delay ripple menjadi porsi signifikan dari periode clock."),
        ],
    },
    13: {
        "topic": "Konversi Data: ADC",
        "subcpmk": "Sub-CPMK 6",
        "cpmk": "CPMK-4 (CPL-1)",
        "problems": [
            ("Foundational",
             r"An ADC has a resolution of 10 bits. How many distinct digital output codes can it produce, and what is this number's general formula in terms of the bit count $n$?",
             r"Sebuah ADC memiliki resolusi 10 bit. Berapa banyak kode output digital berbeda yang dapat dihasilkannya, dan bagaimana rumus umum angka ini dalam bentuk jumlah bit $n$?",
             r"General formula: $2^n$ distinct codes. For $n{=}10$: $2^{10} = 1024$ \textbf{distinct output codes} (from 0 to 1023).",
             r"Rumus umum: $2^n$ kode berbeda. Untuk $n{=}10$: $2^{10} = 1024$ \textbf{kode output berbeda} (dari 0 hingga 1023)."),
            ("Application",
             r"An 8-bit ADC has $V_{ref}=5$V. Compute its step size (quantization resolution) and the digital output code for an analog input of $3.1$V.",
             r"Sebuah ADC 8-bit memiliki $V_{ref}=5$V. Hitung step size (resolusi kuantisasi) dan kode output digital untuk input analog $3{,}1$V.",
             r"Step $=V_{ref}/2^n = 5/256 \approx 0.01953$V (19.53mV). Code $=\text{round}(V_{in}/\text{step}) = \text{round}(3.1/0.01953) \approx \text{round}(158.7) = 159_{10} = 10011111_2$.",
             r"Step $=V_{ref}/2^n = 5/256 \approx 0{,}01953$V (19,53mV). Kode $=\text{round}(V_{in}/\text{step}) = \text{round}(3{,}1/0{,}01953) \approx \text{round}(158{,}7) = 159_{10} = 10011111_2$."),
            ("Analytical",
             r"An avionics airspeed sensor produces a smoothly varying analog signal containing components up to 50\,Hz. The onboard ADC samples this signal at only 60\,Hz. Explain, referencing the Nyquist criterion, why this sampling rate is inadequate, name the resulting artifact, and state the minimum sampling rate that would avoid it.",
             r"Sensor airspeed avionik menghasilkan sinyal analog yang berubah halus mengandung komponen hingga 50\,Hz. ADC onboard mengambil sampel sinyal ini hanya pada 60\,Hz. Jelaskan, dengan merujuk kriteria Nyquist, mengapa laju sampling ini tidak memadai, sebutkan artefak yang dihasilkan, dan sebutkan laju sampling minimum yang menghindarinya.",
             r"The Nyquist criterion requires the sampling rate to be at least twice the highest frequency component in the signal ($f_s \geq 2f_{max}$). Here $2\times50\text{Hz}=100\text{Hz}$ is required, but the ADC samples at only 60\,Hz -- \textbf{undersampling}. The resulting artifact is \textbf{aliasing}: high-frequency content folds back and appears as false lower-frequency signal in the digitized output, which for an airspeed sensor could cause the displayed reading to fluctuate incorrectly or lag real changes, a serious flight-safety concern. \textbf{Minimum safe sampling rate: just above 100\,Hz} (in practice higher still, with margin for an anti-aliasing filter's roll-off).",
             r"Kriteria Nyquist mensyaratkan laju sampling minimal dua kali komponen frekuensi tertinggi dalam sinyal ($f_s \geq 2f_{max}$). Di sini dibutuhkan $2\times50\text{Hz}=100\text{Hz}$, tetapi ADC hanya mengambil sampel pada 60\,Hz -- \textbf{undersampling}. Artefak yang dihasilkan adalah \textbf{aliasing}: konten frekuensi tinggi terlipat balik dan muncul sebagai sinyal frekuensi rendah palsu pada output digital, yang untuk sensor airspeed dapat menyebabkan pembacaan yang ditampilkan berfluktuasi secara keliru atau tertinggal dari perubahan nyata, masalah keselamatan penerbangan yang serius. \textbf{Laju sampling minimum aman: sedikit di atas 100\,Hz} (dalam praktik lebih tinggi lagi, dengan margin untuk roll-off filter anti-aliasing)."),
        ],
    },
}

if __name__ == "__main__":
    results = []
    for n, m in MEETINGS.items():
        tex = build_exercise_tex(COURSE_NAME, COURSE_CODE, n, m["topic"], m["subcpmk"], m["cpmk"], m["problems"])
        res = compile_exercise("Digital_Technic_Logic", n, tex)
        results.append(res)
        status = "OK" if res["ok"] else "FAIL"
        print(f"[{status}] meeting {res['meeting']} exercise: {res['size_kb']} KB errors={res['errors']}")
