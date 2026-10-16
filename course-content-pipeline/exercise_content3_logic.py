#!/usr/bin/env python3
"""Bilingual practice-problem content for Digital_Technic_Logic meetings 10-13.
Each problem tuple: (level, en_problem, id_problem, en_solution, id_solution).
All numeric answers independently verified before authoring."""

EXERCISES = {}

EXERCISES[("Digital_Technic_Logic", 10)] = dict(
    course_name="Digital Technic: Digital Logic Fundamentals",
    course_code="AV0301DT",
    topic="Flip-Flops: Terminology \\& Types (SR, D)",
    subcpmk="Mampu menjelaskan terminologi flip-flop dan operasi flip-flop SR dan D.",
    cpmk="CPMK-4 (CPL-1)",
    problems=[
        ("Foundational",
         r"An SR latch starts at $Q=0$. Apply $(S,R)=(1,0)$ for one step, then $(S,R)=(0,0)$. Give $Q$ after each step and name the operation performed each time.",
         r"Sebuah SR latch mulai dari $Q=0$. Terapkan $(S,R)=(1,0)$ satu langkah, lalu $(S,R)=(0,0)$. Berikan $Q$ setelah tiap langkah dan sebutkan operasinya.",
         r"Step 1 $(S{=}1,R{=}0)$: Set $\Rightarrow Q=1$. Step 2 $(S{=}0,R{=}0)$: Hold $\Rightarrow Q$ stays 1.",
         r"Langkah 1 $(S{=}1,R{=}0)$: Set $\Rightarrow Q=1$. Langkah 2 $(S{=}0,R{=}0)$: Hold $\Rightarrow Q$ tetap 1."),
        ("Application",
         r"A D flip-flop starts at $Q=0$. On four consecutive clock edges the D input is $0,1,1,0$. List $Q$ after each edge.",
         r"Sebuah flip-flop D mulai dari $Q=0$. Pada empat edge clock berturutan, input D adalah $0,1,1,0$. Sebutkan $Q$ setelah tiap edge.",
         r"Since $Q_{next}=D$ each edge: edge1 $D{=}0\Rightarrow Q{=}0$; edge2 $D{=}1\Rightarrow Q{=}1$; edge3 $D{=}1\Rightarrow Q{=}1$; edge4 $D{=}0\Rightarrow Q{=}0$. Sequence: $0,1,1,0$.",
         r"Karena $Q_{next}=D$ tiap edge: edge1 $D{=}0\Rightarrow Q{=}0$; edge2 $D{=}1\Rightarrow Q{=}1$; edge3 $D{=}1\Rightarrow Q{=}1$; edge4 $D{=}0\Rightarrow Q{=}0$. Urutan: $0,1,1,0$."),
        ("Analytical",
         r"A wiring fault asserts both $S=1$ and $R=1$ on an SR flip-flop encoding a landing-gear-locked discrete. Using the SR truth table, explain why this is dangerous, and explain why a D flip-flop-based design avoids the problem entirely.",
         r"Kesalahan pengkabelan mengaktifkan $S=1$ dan $R=1$ bersamaan pada flip-flop SR yang merepresentasikan status landing-gear-locked. Gunakan tabel kebenaran SR untuk menjelaskan mengapa ini berbahaya, dan jelaskan mengapa desain berbasis flip-flop D menghindarinya sepenuhnya.",
         r"$S=R=1$ is the forbidden state: both $Q$ and $\overline{Q}$ are forced to the same level; when the fault clears, the next state is an unpredictable race, so the indicated gear position could be wrong. A D flip-flop encodes the status as a single D bit from one sensor line, so no contradictory S/R combination can ever exist -- the forbidden state is eliminated by construction.",
         r"$S=R=1$ adalah kondisi terlarang: $Q$ dan $\overline{Q}$ dipaksa ke level yang sama; saat kesalahan hilang, next state menjadi race yang tidak dapat diprediksi, sehingga posisi gear yang ditunjukkan bisa salah. Flip-flop D mengkodekan status sebagai satu bit D dari satu jalur sensor, sehingga kombinasi S/R yang kontradiktif tidak pernah mungkin terjadi -- kondisi terlarang tereliminasi sejak desain."),
    ])

EXERCISES[("Digital_Technic_Logic", 11)] = dict(
    course_name="Digital Technic: Digital Logic Fundamentals",
    course_code="AV0301DT",
    topic="Flip-Flops: JK, T \\& Applications",
    subcpmk="Mampu menganalisis flip-flop JK dan T serta aplikasinya (counter/register).",
    cpmk="CPMK-4 (CPL-1)",
    problems=[
        ("Foundational",
         r"A JK flip-flop is at $Q=1$. Apply $(J,K)=(1,1)$ for one clock edge. What is $Q$ after the edge, and what operation occurred?",
         r"Flip-flop JK berada pada $Q=1$. Terapkan $(J,K)=(1,1)$ untuk satu edge clock. Berapa $Q$ setelah edge, dan operasi apa yang terjadi?",
         r"$J=K=1 \Rightarrow$ toggle $\Rightarrow Q_{next}=\overline{Q}=0$.",
         r"$J=K=1 \Rightarrow$ toggle $\Rightarrow Q_{next}=\overline{Q}=0$."),
        ("Application",
         r"Two T flip-flops are cascaded (stage 1 clocked by the input, stage 2 clocked by stage 1's $Q$), both with $T=1$. If the input clock is 8 kHz, what is stage 2's output frequency?",
         r"Dua flip-flop T dikaskade (tahap 1 diclock oleh input, tahap 2 diclock oleh $Q$ tahap 1), keduanya $T=1$. Jika clock input 8 kHz, berapa frekuensi output tahap 2?",
         r"Each $T=1$ stage divides frequency by 2; two cascaded stages divide by 4: $8\text{ kHz}/4=2$ kHz.",
         r"Tiap tahap $T=1$ membagi frekuensi dengan 2; dua tahap berkaskade membagi dengan 4: $8\text{ kHz}/4=2$ kHz."),
        ("Analytical",
         r"Using the excitation table, determine the $J,K$ values needed to move a flip-flop from $Q=0$ to $Q_{next}=1$, and explain why a don't-care appears in this transition.",
         r"Menggunakan tabel eksitasi, tentukan nilai $J,K$ yang dibutuhkan untuk membawa flip-flop dari $Q=0$ ke $Q_{next}=1$, dan jelaskan mengapa muncul don't-care pada transisi ini.",
         r"For $0\to1$: $J=1,K=X$. $J$ must be 1 to set the output; $K$ is don't-care because with $J=1$, whether $K=0$ (set) or $K=1$ (toggle from 0), the result is the same $Q_{next}=1$.",
         r"Untuk $0\to1$: $J=1,K=X$. $J$ harus 1 agar output di-set; $K$ don't-care karena dengan $J=1$, baik $K=0$ (set) maupun $K=1$ (toggle dari 0), hasilnya sama-sama $Q_{next}=1$."),
    ])

EXERCISES[("Digital_Technic_Logic", 12)] = dict(
    course_name="Digital Technic: Digital Logic Fundamentals",
    course_code="AV0301DT",
    topic="Shift Registers \\& Counters",
    subcpmk="Mampu menganalisis shift register dan counter sebagai rangkaian sekuensial.",
    cpmk="CPMK-4 (CPL-1)",
    problems=[
        ("Foundational",
         r"A 4-bit SIPO shift register ($Q_3Q_2Q_1Q_0$, new bit enters at $Q_3$) starts at $0000$. Serial input bits $1,1,0,1$ arrive one per clock, oldest first. What is the register content after all 4 bits have shifted in?",
         r"Shift register SIPO 4-bit ($Q_3Q_2Q_1Q_0$, bit baru masuk di $Q_3$) mulai dari $0000$. Bit serial $1,1,0,1$ masuk satu per clock, bit tertua lebih dulu. Berapa isi register setelah 4 bit masuk?",
         r"Clock1 in=1: $1000$. Clock2 in=1: $1100$. Clock3 in=0: $0110$. Clock4 in=1: $1011$. Final content: $1011_2$.",
         r"Clock1 in=1: $1000$. Clock2 in=1: $1100$. Clock3 in=0: $0110$. Clock4 in=1: $1011$. Isi akhir: $1011_2$."),
        ("Application",
         r"A 4-bit synchronous binary up-counter starts at $0000$. After how many clock pulses does it first return to $0000$, and what decimal value does it hold immediately before that?",
         r"Counter biner sinkron up-counter 4-bit mulai dari $0000$. Setelah berapa pulsa clock ia kembali ke $0000$ pertama kali, dan berapa nilai desimal tepat sebelum itu?",
         r"A 4-bit counter counts $0$ to $15$ ($2^4-1$) then wraps on the 16th pulse. Value immediately before the wrap is $15$ ($1111_2$).",
         r"Counter 4-bit menghitung $0$ hingga $15$ ($2^4-1$) lalu berulang pada pulsa ke-16. Nilai tepat sebelum berulang adalah $15$ ($1111_2$)."),
        ("Analytical",
         r"Design the extra logic needed for a mod-12 counter built from 4 flip-flops (which naturally count 0--15), referencing the mod-6 example from this meeting.",
         r"Rancang logika tambahan untuk counter mod-12 dibangun dari 4 flip-flop (yang secara alami menghitung 0--15), merujuk pada contoh mod-6 dari pertemuan ini.",
         r"A 4-bit counter naturally counts $0$--$15$; for mod-12 it must reset after reaching 11 ($1011_2$). Decode state 12 ($1100_2$) with an AND gate and use it to asynchronously clear all flip-flops back to $0000$ -- exactly like the mod-6 example decoding state 6 to force a reset. Sequence becomes $0,\dots,11,0,1,\dots$.",
         r"Counter 4-bit secara alami menghitung $0$--$15$; untuk mod-12 harus reset setelah mencapai 11 ($1011_2$). Decode status 12 ($1100_2$) dengan gerbang AND dan gunakan untuk me-reset asinkron semua flip-flop ke $0000$ -- persis seperti contoh mod-6 yang men-decode status 6 untuk memaksa reset. Urutan menjadi $0,\dots,11,0,1,\dots$."),
    ])

EXERCISES[("Digital_Technic_Logic", 13)] = dict(
    course_name="Digital Technic: Digital Logic Fundamentals",
    course_code="AV0301DT",
    topic="Analog-to-Digital Conversion (ADC)",
    subcpmk="Mampu menjelaskan konversi data (ADC/DAC) dan arsitektur dasar mikrokomputer.",
    cpmk="CPMK-5 (CPL-1)",
    problems=[
        ("Foundational",
         r"Compute the step size (resolution) of a 12-bit ADC with $V_{ref}=5$V.",
         r"Hitung step size (resolusi) ADC 12-bit dengan $V_{ref}=5$V.",
         r"Step $=V_{ref}/2^n = 5/4096 \approx 1.22$ mV.",
         r"Step $=V_{ref}/2^n = 5/4096 \approx 1{,}22$ mV."),
        ("Application",
         r"A signal has frequency components up to 20 kHz. What is the minimum sampling rate needed per Nyquist, and what happens if a designer samples at exactly 30 kHz?",
         r"Sebuah sinyal memiliki komponen frekuensi hingga 20 kHz. Berapa laju sampling minimum menurut Nyquist, dan apa yang terjadi jika sampling dilakukan tepat pada 30 kHz?",
         r"Minimum $f_s > 2\times20\text{ kHz}=40$ kHz. Sampling at 30 kHz is below the Nyquist rate, so aliasing occurs: content between 15--20 kHz folds back and appears as false lower frequencies.",
         r"Minimum $f_s > 2\times20\text{ kHz}=40$ kHz. Sampling pada 30 kHz berada di bawah laju Nyquist, sehingga terjadi aliasing: konten 15--20 kHz terlipat balik dan muncul sebagai frekuensi rendah palsu."),
        ("Analytical",
         r"An 8-bit SAR ADC ($V_{ref}=5$V) reads a code of $200_{10}$. What analog voltage does this represent, and how many comparison steps did the SAR conversion take?",
         r"ADC SAR 8-bit ($V_{ref}=5$V) membaca kode $200_{10}$. Berapa tegangan analog yang direpresentasikan, dan berapa langkah perbandingan yang dibutuhkan konversi SAR?",
         r"Step $=5/256\approx19.53$ mV. Voltage $\approx200\times19.53\text{ mV}\approx3.91$ V. An 8-bit SAR conversion takes exactly 8 comparison steps.",
         r"Step $=5/256\approx19{,}53$ mV. Tegangan $\approx200\times19{,}53\text{ mV}\approx3{,}91$ V. Konversi SAR 8-bit membutuhkan tepat 8 langkah perbandingan."),
    ])
