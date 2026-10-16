#!/usr/bin/env python3
"""Digital_Technic_Data (AV0303DT) meetings 1-4 -- extracted verbatim from the
hand-authored lecture.tex files (this course has no python content generator;
the source of truth is ~/courses/Digital_Technic_Data/lectures/meeting{1..4}/lecture.tex).
Used only to build the bilingual deck; the original lecture.tex/.pdf are untouched."""

COURSE   = "Digital_Technic_Data"
SUBJECT  = "DIGITAL TECHNIC -- DIGITAL DATA TRANSMISSION"
SUBTITLE = "Digital Data Transmission"
REF      = "Modul 05 EASA -- Digital Techniques \\& Electronic Instrument Systems; Floyd, \\emph{Digital Fundamentals}"
CLO = [
 "Explain and apply the principles of digital data encoding in data transmission.",
 "Explain the principles of digital data decoding and error detection techniques in data transmission.",
 "Explain the working principle of the cathode ray tube (CRT) as a digital data display device.",
 "Explain the characteristics of electrostatic discharge sensitive (ESD) devices and their handling procedures.",
 "Explain the principles of fiber optic data transmission and software management control.",
]
I = lambda *xs: list(xs)
M = {}

M[1] = ("Encoding Data Digital: Prinsip \\& Jenis Encoder (NRZ/RZ)",
  "Students are able to explain the principle and basic types of digital data encoder (NRZ/RZ).",
  I("Explain why raw binary data is encoded before transmission.",
    "Describe Non-Return-to-Zero (NRZ) encoding.",
    "Describe Return-to-Zero (RZ) encoding and compare it with NRZ."),
  [("Why Encode Data?",
    r"""\textbf{Encoding} converts a stream of binary data (1s and 0s) into a physical signal (voltage levels over time) suited for transmission.\begin{itemize}\item Helps the receiver recover timing (clock synchronization).\item Reduces DC bias and improves noise immunity on the transmission line.\item Different encoding schemes trade off bandwidth, complexity, and reliability.\end{itemize}"""),
   ("Non-Return-to-Zero (NRZ)",
    r"""In \textbf{NRZ}, the signal level stays HIGH for a 1 and LOW for a 0 for the full bit period -- it never returns to a zero/neutral level between bits.\begin{itemize}\item Simple to generate; efficient use of bandwidth.\item Long runs of identical bits give no transitions, making clock recovery difficult.\end{itemize}"""),
   ("Return-to-Zero (RZ)",
    r"""In \textbf{RZ}, the signal returns to a zero/neutral level partway through every bit period, even for consecutive identical bits.\begin{itemize}\item Guarantees at least one transition per bit, easing clock recovery.\item Requires roughly double the bandwidth of NRZ for the same bit rate.\end{itemize}"""),
   ("NRZ vs RZ",
    r"""\begin{center}\begin{tabular}{l|l|l}\hline & NRZ & RZ\\\hline Bandwidth & lower & higher\\ Clock recovery & harder & easier\\ Complexity & simpler & more complex\\\hline\end{tabular}\end{center}""")],
  I("Encoding converts binary data into a transmission-ready signal.",
    "NRZ holds level for the full bit period; simple but weak clock recovery on long runs.",
    "RZ returns to zero mid-bit, easing clock recovery at the cost of bandwidth."),
  I("Sketch the NRZ waveform for the bit sequence 1011001.",
    "Sketch the RZ waveform for the same sequence.",
    "Explain why long runs of identical bits are problematic for NRZ."))

M[2] = ("Encoding Lanjutan: Manchester \\& Differential Manchester",
  "Students are able to explain Manchester and Differential Manchester encoding techniques.",
  I("Recall the clock-recovery limitation of NRZ/RZ.",
    "Describe Manchester encoding.",
    "Describe Differential Manchester encoding and its advantage."),
  [("Why Go Beyond NRZ/RZ?",
    r"""NRZ struggles with clock recovery on long identical-bit runs; RZ fixes this but costs bandwidth.\begin{itemize}\item \textbf{Manchester} encodings guarantee a transition in the \emph{middle} of every bit -- self-clocking without RZ's extra bandwidth cost.\end{itemize}"""),
   ("Manchester Encoding",
    r"""Each bit is represented by a transition at the bit's midpoint:\begin{itemize}\item Bit 1: transition from LOW to HIGH (or HIGH to LOW, by convention).\item Bit 0: the opposite transition.\item Guarantees a mid-bit transition for every bit -- excellent clock recovery.\end{itemize}Used in classic Ethernet (10BASE-T/802.3)."""),
   ("Differential Manchester Encoding",
    r"""Bit value is encoded by the \textbf{presence or absence of a transition at the start} of the bit period, not by the mid-bit transition direction:\begin{itemize}\item Bit 0: transition at the start of the bit period.\item Bit 1: no transition at the start.\item A mid-bit transition is still always present, for clocking.\item More noise-immune: polarity reversals on the line do not corrupt the data.\end{itemize}Used in Token Ring networks."""),
   ("Comparison",
    r"""\begin{center}\begin{tabular}{l|l|l}\hline & Manchester & Differential Manchester\\\hline Bit encoding & transition direction & transition presence/absence\\ Clock recovery & guaranteed & guaranteed\\ Polarity immunity & no & yes\\\hline\end{tabular}\end{center}""")],
  I("Manchester encoding places a transition at every bit's midpoint for reliable clock recovery.",
    "Differential Manchester encodes bit value by transition presence/absence, adding polarity immunity.",
    "Both trade extra bandwidth for a strong, self-clocking, noise-tolerant signal."),
  I("Sketch the Manchester waveform for the bit sequence 1011001.",
    "Sketch the Differential Manchester waveform for the same sequence.",
    "Explain one advantage of Differential Manchester over standard Manchester."))

M[3] = ("Decoding Data Digital",
  "Students are able to explain the principle and types of digital data decoder.",
  I("Explain the general principle of decoding as the inverse of encoding.",
    "Describe how a receiver recovers the clock and bit values from an NRZ/RZ waveform.",
    "Describe how a receiver decodes a Manchester / Differential Manchester waveform.",
    "Explain common causes of decoding errors (jitter, noise, DC bias)."),
  [("Recap: Meeting 1--2",
    r"""\begin{itemize}
\item \textbf{M01} -- Encoding converts binary data into a physical signal. NRZ holds level for the full bit; RZ returns to zero mid-bit for easier clocking, at the cost of bandwidth.
\item \textbf{M02} -- Manchester encoding forces a transition at every bit's midpoint (self-clocking). Differential Manchester encodes bit value by transition presence/absence, adding polarity immunity.
\end{itemize}
\vspace{0.2cm}
Today we flip the problem around: given the received waveform, how does the receiver recover the original bits? This is \textbf{decoding}."""),
   ("What Is Decoding?",
    r"""\textbf{Decoding} is the process performed at the receiver that converts a received physical signal (voltage levels over time) back into the original binary data stream.

\begin{itemize}
\item Decoding is the \textbf{inverse operation} of encoding.
\item The decoder must know which encoding scheme was used at the transmitter -- it applies the matching decision rule.
\item A correct decode requires the receiver to (1) recover bit timing (the clock) and (2) correctly sample the signal level or transition at each bit.
\end{itemize}"""),
   ("The Decoding Pipeline",
    r"""\begin{center}
\begin{tikzpicture}[node distance=0.6cm,
block/.style={rectangle,draw,rounded corners,minimum width=2.4cm,minimum height=0.9cm,align=center,fill=blue!10,font=\footnotesize}]
\node[block] (line) {Received\\Line Signal};
\node[block,right=of line] (clk) {Clock\\Recovery};
\node[block,right=of clk] (samp) {Sampling /\\Decision};
\node[block,right=of samp] (bits) {Recovered\\Bit Stream};
\draw[-{Latex},thick] (line)--(clk);
\draw[-{Latex},thick] (clk)--(samp);
\draw[-{Latex},thick] (samp)--(bits);
\end{tikzpicture}
\end{center}
\vspace{0.2cm}
\textbf{Clock recovery} extracts bit-timing information from the signal itself (self-clocking codes) or from a separate clock line. \textbf{Sampling/decision} then reads the level or transition at the correct instant to decide 0 or 1."""),
   ("Decoding NRZ",
    r"""\textbf{NRZ decoding rule:} sample the signal level at the middle of each bit period.
\begin{itemize}
\item Level HIGH $\Rightarrow$ bit 1; level LOW $\Rightarrow$ bit 0.
\item \textbf{Key weakness:} NRZ carries no self-clocking information. If the receiver's local clock is not already synchronized (e.g. via a separate clock line or a known bit rate), long runs of identical bits cause \textbf{clock drift} and sampling at the wrong instant.
\item In practice, NRZ decoding depends on an external or previously synchronized clock reference.
\end{itemize}"""),
   ("Decoding RZ",
    r"""\textbf{RZ decoding rule:} because the signal always returns to zero partway through the bit, the receiver can detect a pulse (non-zero level) within the bit window.
\begin{itemize}
\item Pulse present in the bit window $\Rightarrow$ bit 1; no pulse $\Rightarrow$ bit 0.
\item Since every bit period contains at least one transition (to zero), the receiver can re-synchronize its clock on every bit -- easier clock recovery than NRZ.
\item Trade-off recap: this reliability costs roughly double the bandwidth of NRZ for the same bit rate.
\end{itemize}"""),
   ("Worked Example -- Decoding NRZ",
    r"""A receiver samples the following NRZ waveform, one sample per bit period:
\begin{center}
\begin{tikzpicture}[x=1.3cm,y=0.9cm]
\foreach \x in {0,...,7} \draw[gray!35] (\x,-0.15) -- (\x,1.25);
\draw[blue,thick] (0,1)--(1,1)--(1,0)--(3,0)--(3,1)--(4,1)--(4,0)--(5,0)--(5,1)--(7,1);
\node at (0.5,-0.45) {\scriptsize ?};
\node at (1.5,-0.45) {\scriptsize ?};
\node at (2.5,-0.45) {\scriptsize ?};
\node at (3.5,-0.45) {\scriptsize ?};
\node at (4.5,-0.45) {\scriptsize ?};
\node at (5.5,-0.45) {\scriptsize ?};
\node at (6.5,-0.45) {\scriptsize ?};
\end{tikzpicture}
\end{center}
\textbf{Solution:} sample midpoint of each cell -- HIGH,LOW,LOW,HIGH,LOW,HIGH,HIGH $\Rightarrow$ decoded bits $=1001011$."""),
   ("Decoding Manchester",
    r"""\textbf{Manchester decoding rule:} examine the direction of the transition at the \emph{middle} of each bit cell.
\begin{itemize}
\item Transition LOW$\to$HIGH at mid-bit $\Rightarrow$ bit 1.
\item Transition HIGH$\to$LOW at mid-bit $\Rightarrow$ bit 0.
\item Because every bit cell guarantees a mid-bit transition, the receiver can continuously re-synchronize its clock -- this is why Manchester is called \textbf{self-clocking}.
\item The decoder uses a phase-locked loop (PLL) or edge-triggered logic in real hardware to lock onto these transitions.
\end{itemize}"""),
   ("Decoding Differential Manchester",
    r"""\textbf{Differential Manchester decoding rule:} examine whether there \emph{is} a transition at the \textbf{start} of the bit cell (ignore the mid-bit transition, which is always present for clocking only).
\begin{itemize}
\item Transition present at the start of the cell $\Rightarrow$ bit 0.
\item No transition at the start of the cell $\Rightarrow$ bit 1.
\item Because bit value depends only on transition \emph{presence}, not \emph{polarity}, this decoding is immune to a polarity reversal of the whole line (e.g. wires swapped).
\end{itemize}"""),
   ("Worked Example -- Decoding Manchester",
    r"""A receiver observes this Manchester waveform (8 bit cells):
\begin{center}
\begin{tikzpicture}[x=1.3cm,y=0.9cm]
\foreach \x in {0,...,8} \draw[gray!35] (\x,-0.15) -- (\x,1.25);
\draw[red,thick]
(0,0)--(0.5,0)--(0.5,1)--(1.5,1)--(1.5,0)--(2,0)--(2,1)--(2.5,1)--(2.5,0)--(3.5,0)--(3.5,1)--(4,1)--(4,0)--(4.5,0)--(4.5,1)--(5.5,1)--(5.5,0)--(6,0)--(6,1)--(6.5,1)--(6.5,0)--(7.5,0)--(7.5,1)--(8,1);
\end{tikzpicture}
\end{center}
\textbf{Solution:} read mid-cell transition direction for each of the 8 cells -- LOW$\to$HIGH,HIGH$\to$LOW,LOW$\to$HIGH,HIGH$\to$LOW,LOW$\to$HIGH,HIGH$\to$LOW,LOW$\to$HIGH,HIGH$\to$LOW $\Rightarrow$ decoded bits $=10101010$."""),
   ("Why Decoding Can Go Wrong",
    r"""Even with a correct encoding scheme, real channels can cause decoding errors:
\begin{itemize}
\item \textbf{Jitter} -- small timing variations shift transitions away from their ideal instant, risking a wrong sample.
\item \textbf{Noise} -- voltage spikes can be misread as a transition that never happened (or hide a real one).
\item \textbf{DC bias / attenuation} -- a weakened or offset signal may blur the distinction between HIGH and LOW.
\item \textbf{Clock drift} -- especially serious for non-self-clocking codes like plain NRZ over long bit runs.
\end{itemize}"""),
   ("Clock Recovery in Practice",
    r"""Real receiver hardware recovers the clock using a \textbf{Phase-Locked Loop (PLL)}:
\begin{itemize}
\item The PLL locks its internal oscillator phase to the transitions present in the incoming signal.
\item For self-clocking codes (RZ, Manchester, Differential Manchester), every bit supplies a timing reference, so the PLL stays locked reliably.
\item For NRZ, the PLL has nothing to lock onto during long identical-bit runs, so a separate clock line or a strict maximum run-length limit is often required.
\end{itemize}
\textbf{Design takeaway:} the choice of line code at the transmitter directly determines how reliably the receiver's decoder can recover the clock."""),
   ("Decoder Comparison",
    r"""\begin{center}
\renewcommand{\arraystretch}{1.2}
\begin{tabular}{l|l|l|l}\hline
 & NRZ & RZ & Manchester\\\hline
Decision rule & level at mid-bit & pulse present? & transition direction\\
Self-clocking & no & yes & yes\\
Sensitive to & long runs & bandwidth cost & noise on edges\\\hline
\end{tabular}
\end{center}
\vspace{0.2cm}
Every decoding scheme is the mirror image of its matching encoder from Meetings 1--2 -- decoding always assumes the receiver knows which scheme is in use."""),
   ("In-Class Practice",
    r'''Work with your neighbor:
\begin{enumerate}
\item Decode the NRZ waveform: HIGH,HIGH,LOW,LOW,HIGH,LOW for 6 bit periods. (Answer: $110010$.)
\item A Manchester receiver sees a HIGH$\to$LOW transition at the midpoint of bit cell 4. What bit value is this? (Answer: 0.)
\item Explain in one sentence why Differential Manchester decoding does not care about which wire is "positive."
\end{enumerate}'''),
   ("Decoding in Avionics Data Buses",
    r"""Avionics data buses rely on correct, reliable decoding to keep flight-critical data trustworthy:
\begin{itemize}
\item \textbf{ARINC 429} uses a bipolar RZ-style waveform; receiver ICs decode level and polarity per bit slot.
\item \textbf{MIL-STD-1553} uses Manchester II encoding specifically because self-clocking decoding tolerates cable length and minor timing variation on a shared bus.
\item Bus transceiver chips integrate clock recovery and decision logic in hardware -- the same principles from this lecture, applied at megabit speeds.
\end{itemize}""")],
  I("Decoding is the inverse of encoding: recover bit timing (clock recovery), then sample or read transitions to recover the bits.",
    "NRZ decoding needs an external clock reference; RZ, Manchester, and Differential Manchester are self-clocking.",
    "Manchester decodes by transition direction; Differential Manchester decodes by transition presence, which adds polarity immunity.",
    "Jitter, noise, DC bias, and clock drift are the main real-world causes of decoding errors."),
  I("Given the NRZ waveform for bit sequence $1101001$, describe how a receiver decodes each bit and state any risk of clock drift.",
    "Given a Manchester waveform, decode the bit sequence from its transition directions (waveform provided in the exercise sheet).",
    "Explain why Differential Manchester decoding is preferred over standard Manchester in noisy environments where polarity may be uncertain."))

M[4] = ("Deteksi Kesalahan Data: Parity, Checksum \\& CRC",
  "Students are able to explain data error-detection techniques: parity check, checksum, and cyclic redundancy check (CRC).",
  I("Explain why transmission errors occur and why they must be detected.",
    "Compute and verify a parity bit (even/odd parity).",
    "Compute and verify a simple checksum.",
    "Compute and verify a CRC remainder using modulo-2 division."),
  [("Recap: Meeting 1--3",
    r"""\begin{itemize}
\item \textbf{M01--M02} -- Encoding schemes (NRZ, RZ, Manchester, Differential Manchester) turn bits into physical signals.
\item \textbf{M03} -- Decoding recovers the bits at the receiver, but noise, jitter, and drift can still cause a wrong bit to be read.
\end{itemize}
\vspace{0.2cm}
Today's question: once bits are decoded, how does the receiver know whether the decoded data is \textbf{correct}? This is \textbf{error detection}."""),
   ("Why Transmission Errors Happen",
    r"""No real transmission channel is perfect.
\begin{itemize}
\item Electrical noise, electromagnetic interference (EMI), and crosstalk can flip a bit from 0 to 1 or vice versa.
\item Weak signal amplitude, long cable runs, and poor connections increase error probability.
\item In avionics, engines, radar, and high-power systems are strong EMI sources near data cables.
\end{itemize}
\vspace{0.15cm}
Because errors cannot be fully eliminated, digital systems add \textbf{redundant bits} that let the receiver detect (and sometimes correct) errors."""),
   ("Error Detection -- The General Idea",
    r"""\begin{center}
\begin{tikzpicture}[node distance=0.6cm,
block/.style={rectangle,draw,rounded corners,minimum width=2.4cm,minimum height=0.9cm,align=center,fill=blue!10,font=\footnotesize}]
\node[block] (data) {Data};
\node[block,right=of data] (enc) {Add Check\\Bits};
\node[block,right=of enc,fill=red!10] (ch) {Channel\\(noise)};
\node[block,right=of ch] (chk) {Recompute\\\& Compare};
\draw[-{Latex},thick] (data)--(enc);
\draw[-{Latex},thick] (enc)--(ch);
\draw[-{Latex},thick] (ch)--(chk);
\end{tikzpicture}
\end{center}
\vspace{0.2cm}
The transmitter computes extra \textbf{check bits} from the data using a known rule; the receiver recomputes the same rule on the received data and compares. A mismatch means an error occurred."""),
   ("Parity Check -- Concept",
    r"""\textbf{Parity check} appends a single bit so that the total number of 1's in the codeword follows a fixed rule.
\begin{itemize}
\item \textbf{Even parity:} total number of 1's (including the parity bit) is even.
\item \textbf{Odd parity:} total number of 1's is odd.
\item Simple, fast, and cheap -- widely used in UART/serial communication.
\item \textbf{Limitation:} only reliably detects an \emph{odd} number of bit errors; an even number of flipped bits can go undetected.
\end{itemize}"""),
   ("Worked Example -- Even Parity",
    r"""Data to send: $D = 1011000$ (7 bits).
\[
\text{Number of 1's} = 3 \ (\text{odd}) \quad \Rightarrow \quad \text{parity bit } P = 1 \ (\text{to make total even})
\]
\begin{center}
\renewcommand{\arraystretch}{1.2}
\begin{tabular}{|c|c|c|c|c|c|c|c|}
\hline
\multicolumn{7}{|c|}{Data (7 bits)} & Parity\\\hline
1&0&1&1&0&0&0&1\\\hline
\end{tabular}
\end{center}
\textbf{Codeword transmitted:} $C=10110001$ (8 bits, 4 ones -- even, as required)."""),
   ("Checksum -- Concept",
    r"""\textbf{Checksum} splits the data into fixed-size blocks (e.g. bytes or words), sums them arithmetically, and sends the sum (or its complement) alongside the data.
\begin{itemize}
\item The receiver re-sums the received blocks and compares against the received checksum.
\item Detects a broader range of errors than a single parity bit, at low computational cost.
\item Used in Internet protocols (IP, UDP, TCP headers) and many simple file-transfer formats.
\item \textbf{Limitation:} certain error patterns that preserve the sum (e.g. compensating errors) can still go undetected.
\end{itemize}"""),
   ("Worked Example -- Simple Checksum",
    r"""Data words (4-bit blocks): $1101,\ 1011,\ 0110$.
\[
1101 + 1011 + 0110 = ?
\]
Binary addition: $1101+1011=11000$; $11000+0110=11110$.
\vspace{0.1cm}
If the sum overflows the block size, the carry is wrapped around (added back) -- this is the same principle used in the Internet checksum.
\vspace{0.1cm}
\textbf{Transmitted:} the three data words plus the computed checksum word. The receiver repeats the sum and checks for a match."""),
   ("Cyclic Redundancy Check (CRC) -- Concept",
    r"""\textbf{CRC} treats the data bits as a polynomial and divides it (using modulo-2 / XOR arithmetic) by a fixed \textbf{generator polynomial} $G$.
\begin{itemize}
\item The \textbf{remainder} of this division becomes the CRC check bits, appended to the data.
\item The receiver performs the same division on the received codeword; a remainder of \textbf{zero} means no error was detected.
\item CRC catches far more error patterns than parity or simple checksum, including many multi-bit burst errors -- this is why it is the standard in networking and storage.
\end{itemize}"""),
   ("Worked Example -- CRC Encoding",
    r"""Message $M=1101$, generator $G=1011$ (degree 3 $\Rightarrow$ append 3 zero bits).
\[
1101\underline{000}\ \div\ 1011 \ \text{(mod-2 division)}
\]
\begin{center}
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{r l}
$1101$ XOR $1011$ & $=0110$\\
bring down 0 $\to 1100$, XOR $1011$ & $=0111$\\
bring down 0 $\to 1110$, XOR $1011$ & $=0101$\\
bring down 0 $\to 1010$, XOR $1011$ & $=0001$\\
\end{tabular}
\end{center}
\textbf{Remainder (CRC) $=001$} $\Rightarrow$ \textbf{Codeword transmitted} $=1101001$."""),
   ("Worked Example -- CRC Checking",
    r"""\textbf{Case A -- no error:} receiver divides $1101001$ by $1011$ again $\Rightarrow$ remainder $=000$ $\Rightarrow$ \textbf{codeword accepted}.
\vspace{0.2cm}
\textbf{Case B -- one bit flips} (bit 6 changes $0\to1$): received word $=1101011$.
\begin{center}
\renewcommand{\arraystretch}{1.1}
\begin{tabular}{r l}
$1101$ XOR $1011$ & $=0110$\\
bring 0 $\to 1100$, XOR $1011$ & $=0111$\\
bring 1 $\to 1111$, XOR $1011$ & $=0100$\\
bring 1 $\to 1001$, XOR $1011$ & $=0010$\\
\end{tabular}
\end{center}
\textbf{Remainder $=010 \neq 000$} $\Rightarrow$ \textbf{ERROR DETECTED}."""),
   ("Comparing Parity, Checksum, and CRC",
    r"""\begin{center}
\renewcommand{\arraystretch}{1.2}
\begin{tabular}{l|l|l|l}\hline
 & Parity & Checksum & CRC\\\hline
Overhead & 1 bit & 1 block & fixed (e.g. 8/16/32 bits)\\
Detection strength & weak & moderate & strong\\
Computation & very cheap & cheap & moderate (division)\\
Typical use & UART/serial & IP/UDP/TCP & Ethernet, storage, buses\\\hline
\end{tabular}
\end{center}
\vspace{0.15cm}
The stronger the detection, the more computation and/or overhead is required -- system designers choose based on how critical the data is."""),
   ("Detection vs Correction",
    r"""It is important to distinguish two different goals:
\begin{itemize}
\item \textbf{Error detection} (this meeting's topic) -- only tells the receiver \emph{that} an error occurred, so it can request retransmission or discard the data.
\item \textbf{Error correction} (e.g. Hamming codes, forward error correction) -- allows the receiver to actually \emph{fix} the error without retransmission.
\end{itemize}
Parity, checksum, and CRC as covered today are all \textbf{detection-only} schemes -- the standard choice in most avionics data buses, which prefer to discard corrupted data rather than risk using an incorrectly "corrected" value."""),
   ("In-Class Practice",
    r"""Work with your neighbor:
\begin{enumerate}
\item Compute the odd-parity bit for data $D=1001100$. (Answer: 3 ones, already odd $\Rightarrow P=0$.)
\item A receiver computes a checksum on received data and it does \emph{not} match the transmitted checksum. What should the receiver do? (Answer: flag the data as corrupted; request retransmission or discard.)
\item Why can parity miss a 2-bit error while CRC is far less likely to miss it?
\end{enumerate}"""),
   ("Error Detection in Avionics Systems",
    r"""Error detection is a safety-critical function in avionics data transmission:
\begin{itemize}
\item \textbf{ARINC 429} words include a parity bit for basic error checking on point-to-point avionics links.
\item \textbf{MIL-STD-1553} messages use parity per word plus higher-level protocol checks.
\item \textbf{ARINC 664 / AFDX} (modern avionics networks) use CRC (as in standard Ethernet) for strong error detection on switched avionics networks.
\item A flight computer that silently accepts corrupted sensor data could make an incorrect control decision -- this is why detection schemes are mandatory, not optional.
\end{itemize}""")],
  I("Transmission errors are inevitable; digital systems add redundant check bits to detect them.",
    "Parity check is simple but only reliably catches an odd number of bit errors.",
    "Checksum sums data blocks and catches more error patterns, used widely in networking.",
    "CRC uses modulo-2 polynomial division and gives the strongest detection of the three -- the standard for networks, storage, and modern avionics buses."),
  I("Compute the even-parity bit for data $D=1110010$ and show the transmitted codeword.",
    "Compute a simple checksum for the two 4-bit blocks $1001$ and $0111$.",
    "Given message $M=1010$ and generator $G=1101$, compute the CRC remainder and the transmitted codeword using modulo-2 division."))
