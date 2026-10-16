#!/usr/bin/env python3
"""Digital_Technic_Logic (§13) — meetings 1-8,10-17. Build via build_slides."""
from build_slides import build_deck, compile_meeting

COURSE   = "Digital_Technic_Logic"
SUBJECT  = "DIGITAL TECHNIC"
SUBTITLE = "Digital Logic Fundamentals and Introduction to Microcomputers"
REF      = "Digital Design and Computer Architecture. ARM Edition by Sarah Harris, David Harris"
CLO = [
 "Explain digital number systems and perform conversions among decimal, binary, octal, and hexadecimal.",
 "Analyze signed numbers and perform basic digital arithmetic in binary.",
 "Analyze and simplify combinational logic circuits using logic gates and Boolean algebra.",
 "Explain the terminology and operation of flip-flops and analyze sequential logic circuits.",
 "Explain data conversion (ADC/DAC) and the basic architecture of microcomputers.",
]

I = lambda *xs: list(xs)

# Each meeting: (title, subclo, indicators, slides[(title,body)], summary, assignments)
M = {}

M[1] = ("Number Systems: Decimal--Binary Conversion",
  "Students are able to convert numbers between the decimal and binary systems precisely.",
  I("Explain positional weighting in the decimal and binary systems.",
    "Convert decimal integers to binary and back.",
    "Convert fractional decimal values to binary."),
  [("Why Number Systems Matter in Avionics",
    r"""Avionics computers represent physical measurements -- altitude, airspeed, temperature -- as
    \textbf{digital signals} inside processors, displays, and data buses.
    \begin{itemize}
    \item Digital circuits recognize only two states: 0 and 1 (binary).
    \item Engineers must translate confidently between human-friendly decimal values and
    machine-native binary, octal, and hexadecimal representations.
    \item This meeting builds that foundation: converting decimal $\leftrightarrow$ binary precisely.
    \end{itemize}"""),
   ("Positional Number Systems (Radix)",
    r"""A number system represents a value using a fixed \textbf{base} (radix) $r$ and positional weights.
    \[ N = \sum_{i} d_i \times r^{\,i} \]
    \begin{itemize}
    \item $d_i$: the digit at position $i$, counted from 0 at the radix point.
    \item $r$: the radix -- decimal $r{=}10$, binary $r{=}2$.
    \item Position index increases leftward; fractional positions use negative $i$.
    \end{itemize}
    Example: $1011_2 = 1\cdot2^3+0\cdot2^2+1\cdot2^1+1\cdot2^0 = 11_{10}$."""),
   ("The Binary System \\& Terminology",
    r"""\begin{center}\begin{tabular}{c|c|c|c|c|c|c|c|c}\hline
    Position & 7&6&5&4&3&2&1&0\\\hline
    Weight $2^n$ & 128&64&32&16&8&4&2&1\\\hline
    \end{tabular}\end{center}
    \begin{itemize}
    \item \textbf{Bit:} one binary digit (0 or 1).
    \item \textbf{Nibble:} 4 bits. \textbf{Byte:} 8 bits.
    \item \textbf{MSB} = most significant (leftmost) bit; \textbf{LSB} = least significant (rightmost) bit.
    \end{itemize}"""),
   ("Decimal $\\to$ Binary: Division Algorithm",
    r"""\textbf{Repeated division by 2}, collecting remainders:
    \begin{enumerate}
    \item Divide the decimal number by 2; record the quotient and the remainder.
    \item Repeat the division on the new quotient until the quotient is 0.
    \item Read the remainders from \textbf{bottom to top} -- that sequence is the binary result.
    \end{enumerate}
    Each division step extracts exactly one bit, least significant bit first."""),
   ("Worked Example: Convert $45_{10}$",
    r"""\begin{center}\begin{tabular}{c|c|c}\hline
    Step & Quotient & Remainder\\\hline
    $45\div2$ & 22 & 1\\ $22\div2$ & 11 & 0\\ $11\div2$ & 5 & 1\\
    $5\div2$ & 2 & 1\\ $2\div2$ & 1 & 0\\ $1\div2$ & 0 & 1\\\hline
    \end{tabular}\end{center}
    Reading upward: $45_{10} = 101101_2$.
    Check: $32+8+4+1 = 45$. \checkmark"""),
   ("Worked Example: Convert $178_{10}$",
    r"""\begin{center}\begin{tabular}{c|c|c}\hline
    Step & Quotient & Remainder\\\hline
    $178\div2$ & 89 & 0\\ $89\div2$ & 44 & 1\\ $44\div2$ & 22 & 0\\
    $22\div2$ & 11 & 0\\ $11\div2$ & 5 & 1\\ $5\div2$ & 2 & 1\\
    $2\div2$ & 1 & 0\\ $1\div2$ & 0 & 1\\\hline
    \end{tabular}\end{center}
    Reading upward: $178_{10} = 10110010_2$.
    Check: $128+32+16+2 = 178$. \checkmark"""),
   ("Fractional Decimal $\\to$ Binary: Multiplication Algorithm",
    r"""\begin{enumerate}
    \item Multiply the fractional part by 2.
    \item Record the integer part produced (0 or 1) as the next bit.
    \item Repeat on the new fractional part until it reaches 0 (or the desired precision is met).
    \item Read the recorded bits from \textbf{top to bottom}.
    \end{enumerate}
    This mirrors the division algorithm, but works on the fractional side of the radix point."""),
   ("Worked Example: Convert $0.625_{10}$",
    r"""\begin{center}\begin{tabular}{c|c|c}\hline
    Step & Multiply & Bit\\\hline
    $0.625\times2$ & $=1.25$ & 1\\ $0.25\times2$ & $=0.5$ & 0\\ $0.5\times2$ & $=1.0$ & 1\\\hline
    \end{tabular}\end{center}
    The fractional part reached 0, so we stop.
    Reading top to bottom: $0.625_{10} = 0.101_2$."""),
   ("Binary $\\to$ Decimal: Weighted Sum (with Fractions)",
    r"""Sum the weight of every 1-bit, using negative powers of two after the radix point.
    \[ 110101.101_2 = (32{+}16{+}4{+}1) + (0.5{+}0.125) = 53.625_{10} \]
    \begin{itemize}
    \item Integer part: $110101_2 = 53_{10}$.
    \item Fractional part: $.101_2 = 2^{-1}+2^{-3} = 0.625_{10}$.
    \end{itemize}"""),
   ("Common Pitfalls \\& Tips",
    r"""\begin{itemize}
    \item Reading the remainders in the wrong order -- integer conversion reads \textbf{bottom-up}.
    \item Forgetting that the multiplication method reads \textbf{top-down} for fractions.
    \item Losing track of bit position when summing weights for binary-to-decimal.
    \item Some decimal fractions (e.g. $0.1_{10}$) never terminate in binary -- real systems truncate or round.
    \end{itemize}"""),
   ("In-Class Practice",
    r"""Work through these with a partner, then check with the instructor:
    \begin{enumerate}
    \item Convert $67_{10}$ to binary.
    \item Convert $0.8125_{10}$ to binary.
    \item Convert $101110.011_2$ to decimal.
    \end{enumerate}""")],
  I("Binary uses base 2 with weights that are powers of two.",
    "Decimal-to-binary uses repeated division by 2; binary-to-decimal sums bit weights.",
    "Fractional parts use negative powers of two."),
  I("Convert $45_{10}$ and $178_{10}$ to binary.",
    "Convert $10110110_2$ to decimal.",
    "Convert $0.6875_{10}$ to binary.",
    "Convert $92.375_{10}$ to binary, integer and fractional parts."))

M[2] = ("Octal and Hexadecimal Conversion",
  "Students are able to convert numbers in the octal and hexadecimal systems across bases.",
  I("Convert between binary and octal using 3-bit groups.",
    "Convert between binary and hexadecimal using 4-bit groups.",
    "Convert octal/hex values to decimal."),
  [("Why Octal and Hexadecimal?",
    r"""Long binary strings are hard for humans to read and easy to mistranscribe.
    \begin{itemize}
    \item \textbf{Octal} and \textbf{hexadecimal} group binary bits into compact digits.
    \item Hexadecimal is the standard for memory addresses, machine code, and register dumps
    in microcomputers and avionics data buses.
    \item Because $8=2^3$ and $16=2^4$, converting to/from binary is simple grouping -- no long division needed.
    \end{itemize}"""),
   ("Octal and Hexadecimal Digit Tables",
    r"""\begin{itemize}
    \item Octal (base 8): digits 0--7, each maps to exactly \textbf{3} binary bits.
    \item Hexadecimal (base 16): digits 0--9 then A--F (representing 10--15), each maps to \textbf{4} bits (a nibble).
    \end{itemize}
    \begin{center}\begin{tabular}{c|c||c|c}\hline
    Hex & Binary & Hex & Binary\\\hline
    0&0000&8&1000\\ 1&0001&9&1001\\ 2&0010&A&1010\\ 3&0011&B&1011\\
    4&0100&C&1100\\ 5&0101&D&1101\\ 6&0110&E&1110\\ 7&0111&F&1111\\\hline
    \end{tabular}\end{center}"""),
   ("Binary $\\to$ Octal: Group by 3",
    r"""\begin{enumerate}
    \item Starting from the radix point, group bits into sets of 3 (pad with zeros if needed).
    \item Convert each group directly to its octal digit.
    \end{enumerate}
    Example: $11010110_2 \to 011\,010\,110 \to 3\,2\,6 = 326_8$."""),
   ("Binary $\\to$ Hex: Group by 4",
    r"""\begin{enumerate}
    \item Starting from the radix point, group bits into sets of 4 (pad with zeros if needed).
    \item Convert each group directly to its hex digit.
    \end{enumerate}
    Example: $11010110_2 \to 1101\,0110 \to D\,6 = D6_{16}$."""),
   ("Worked Example: Convert $10111011_2$",
    r"""Group by 3 (pad to 9 bits): $010\,111\,011 \to 2\,7\,3 = 273_8$.
    \vspace{0.2cm}\\
    Group by 4 (already 8 bits): $1011\,1011 \to B\,B = BB_{16}$."""),
   ("Octal/Hex $\\to$ Decimal via Positional Weights",
    r"""Apply the same weighted-sum formula, using the base's own radix.
    \[ 326_8 = 3\cdot64+2\cdot8+6\cdot1 = 214_{10} \qquad D6_{16} = 13\cdot16+6\cdot1 = 214_{10} \]
    Both equal the same binary value, $11010110_2$, confirming the conversions agree."""),
   ("Worked Example: Convert $2F7_{16}$",
    r"""Expand each hex digit to a 4-bit nibble: $2{=}0010$, $F{=}1111$, $7{=}0111$.
    \[ 2F7_{16} = 0010\,1111\,0111_2 \]
    Weighted sum: $2\cdot256 + 15\cdot16 + 7\cdot1 = 512+240+7 = 759_{10}$."""),
   ("Decimal $\\leftrightarrow$ Hex Directly (Division by 16)",
    r"""The same repeated-division algorithm works with radix 16 -- remainders 10--15 become A--F.
    \begin{center}\begin{tabular}{c|c|c}\hline
    Step & Quotient & Remainder\\\hline
    $250\div16$ & 15 & 10 (A)\\ $15\div16$ & 0 & 15 (F)\\\hline
    \end{tabular}\end{center}
    Reading upward: $250_{10} = FA_{16}$. Check: $15\cdot16+10 = 250$."""),
   ("Fractional Conversions (Advanced)",
    r"""The multiplication algorithm extends directly to any target radix.
    \begin{itemize}
    \item Convert $0.5_{10}$ to hex: $0.5\times16=8.0 \Rightarrow 0.5_{10}=0.8_{16}$.
    \item Convert $0.1_{16}$ to decimal: one hex fractional digit has weight $16^{-1}$, so
    $0.1_{16} = 1/16 = 0.0625_{10}$.
    \end{itemize}"""),
   ("Common Pitfalls \\& Tips",
    r"""\begin{itemize}
    \item Forgetting to pad binary groups with zeros at the boundary before grouping.
    \item Mixing up octal (3-bit) and hex (4-bit) group sizes.
    \item Misreading hex letters A--F as decimal digits when computing weighted sums.
    \item Always verify: convert your answer back to binary as a cross-check.
    \end{itemize}"""),
   ("In-Class Practice",
    r"""\begin{enumerate}
    \item Convert $11001010_2$ to octal and hexadecimal.
    \item Convert $1F4_{16}$ to binary and decimal.
    \item Convert $0.75_{10}$ to hexadecimal.
    \end{enumerate}""")],
  I("Octal groups 3 bits; hexadecimal groups 4 bits.",
    "Grouping/ungrouping binary is the fastest route between these bases.",
    "Positional weights convert octal and hex directly to decimal."),
  I("Convert $10111011_2$ to octal and hexadecimal.",
    "Convert $2F7_{16}$ to binary and decimal.",
    "Convert $754_8$ to hexadecimal.",
    "Convert $0.3125_{10}$ to hexadecimal."))

M[3] = ("Signed Numbers",
  "Students are able to represent signed numbers using sign-magnitude and complements.",
  I("Explain sign-magnitude representation.",
    "Form one's complement and two's complement.",
    "Determine the range of an n-bit signed number."),
  [("Representing Sign",
    r"Three common schemes for an n-bit signed integer:"
    r"\begin{itemize}"
    r"\item \textbf{Sign-magnitude:} MSB = sign, remaining bits = magnitude."
    r"\item \textbf{One's complement:} negative = bitwise NOT of the positive."
    r"\item \textbf{Two's complement:} one's complement $+\,1$ (the modern standard)."
    r"\end{itemize}"),
   ("Two's Complement",
    r"To negate: invert all bits, then add 1."
    r"\begin{center}\begin{tabular}{l|l}\hline"
    r"$+5$ (8-bit) & $00000101$\\"
    r"invert & $11111010$\\"
    r"$+1$ & $11111011 = -5$\\\hline"
    r"\end{tabular}\end{center}"
    r"The MSB still indicates sign; arithmetic works without special cases."),
   ("Range of n-bit Signed Numbers",
    r"Two's complement range: $-2^{\,n-1}$ to $+2^{\,n-1}-1$."
    r"\begin{center}\begin{tabular}{c|c|c}\hline"
    r"Bits & Min & Max\\\hline"
    r"8 & $-128$ & $+127$\\ 16 & $-32768$ & $+32767$\\\hline"
    r"\end{tabular}\end{center}"
    r"Only two's complement has a single representation of zero.")],
  I("Sign-magnitude, one's and two's complement represent negatives differently.",
    "Two's complement is the standard: invert and add one.",
    "An n-bit two's-complement value ranges $-2^{n-1}$ to $2^{n-1}-1$."),
  I("Represent $-19$ in 8-bit sign-magnitude, one's and two's complement.",
    "What decimal is $10110100_2$ in two's complement?",
    "State the range of a 12-bit two's-complement number."))

M[4] = ("Binary Arithmetic",
  "Students are able to perform binary addition and subtraction systematically, including two's complement.",
  I("Add binary numbers with carry.",
    "Subtract using two's-complement addition.",
    "Detect overflow in signed arithmetic."),
  [("Binary Addition",
    r"Add bit by bit with carry, like decimal but base 2."
    r"\begin{center}\begin{tabular}{r}\hline"
    r"$\;\;1011$\\ $+\,0110$\\\hline $10001$\\\hline\end{tabular}\end{center}"
    r"Rules: $0+0=0$, $1+0=1$, $1+1=10$ (carry)."),
   ("Subtraction via Two's Complement",
    r"$A - B = A + (\text{two's complement of }B)$."
    r"\\Compute $7-5$ in 4 bits: $0111 + 1011 = 1\,0010$."
    r"\\Discard the final carry-out $\Rightarrow 0010_2 = 2_{10}$."),
   ("Overflow Detection",
    r"Signed overflow occurs when adding two same-sign operands yields the opposite sign."
    r"\begin{itemize}"
    r"\item $+\,+\,\to\,-$ : overflow."
    r"\item $-\,-\,\to\,+$ : overflow."
    r"\item Different signs never overflow."
    r"\end{itemize}"
    r"Carry-out $\neq$ overflow in signed arithmetic.")],
  I("Binary addition propagates carries bit by bit.",
    "Subtraction is addition of the two's complement, discarding the final carry.",
    "Signed overflow is detected from operand and result signs."),
  I("Compute $10110 + 01101$ in binary.",
    "Compute $12 - 9$ using 5-bit two's complement.",
    "Show that $0110+0011$ (4-bit signed) overflows or not."))

M[5] = ("Logic Gates \\& Boolean Algebra",
  "Students are able to analyze and simplify combinational circuits using logic gates and Boolean algebra.",
  I("Build truth tables for AND, OR, NOT, NAND, NOR, XOR.",
    "State the basic laws of Boolean algebra.",
    "Simplify simple Boolean expressions."),
  [("Basic and Derived Gates",
    r"\begin{center}\begin{tabular}{c|c}\hline"
    r"Gate & Function\\\hline"
    r"NOT & $\overline{A}$\\ AND & $A\cdot B$\\ OR & $A+B$\\"
    r"NAND & $\overline{A\cdot B}$\\ NOR & $\overline{A+B}$\\ XOR & $A\oplus B$\\\hline"
    r"\end{tabular}\end{center}"
    r"NAND and NOR are \textbf{universal} --- any function can be built from them."),
   ("Boolean Laws",
    r"\begin{itemize}"
    r"\item Identity: $A+0=A$, \quad $A\cdot1=A$."
    r"\item Null: $A+1=1$, \quad $A\cdot0=0$."
    r"\item Complement: $A+\overline{A}=1$, \quad $A\cdot\overline{A}=0$."
    r"\item De Morgan: $\overline{A+B}=\overline{A}\,\overline{B}$, \quad $\overline{A\cdot B}=\overline{A}+\overline{B}$."
    r"\end{itemize}"),
   ("Simplification Example",
    r"Simplify $Y = A\overline{B} + AB$."
    r"\\$= A(\overline{B}+B) = A\cdot1 = A$."
    r"\vspace{0.2cm}\\Fewer gates $\Rightarrow$ lower cost, delay, and power.")],
  I("Six gates cover all basic logic; NAND/NOR are universal.",
    "Boolean laws (identity, complement, De Morgan) rewrite expressions.",
    "Simplification reduces gate count and delay."),
  I("Write the truth table of $Y = \\overline{A}B + A\\overline{B}$ and name the gate.",
    "Use De Morgan to expand $\\overline{A\\cdot B \\cdot C}$.",
    "Simplify $Y = (A+B)(A+\\overline{B})$."))

M[6] = ("Combinational Logic Circuits",
  "Students are able to simplify and design combinational logic circuits, e.g. with Karnaugh maps.",
  I("Derive a Boolean expression from a truth table.",
    "Minimize expressions using a Karnaugh map.",
    "Draw the simplified gate circuit."),
  [("From Truth Table to Expression",
    r"Sum-of-products (SOP): OR together the minterms where output is 1."
    r"\begin{center}\begin{tabular}{cc|c}\hline"
    r"$A$&$B$&$Y$\\\hline 0&0&0\\0&1&1\\1&0&1\\1&1&0\\\hline\end{tabular}\end{center}"
    r"$Y = \overline{A}B + A\overline{B} = A\oplus B$."),
   ("Karnaugh Map",
    r"A K-map groups adjacent 1s (in powers of two) to eliminate variables."
    r"\begin{itemize}"
    r"\item Adjacent cells differ by one variable (Gray-code order)."
    r"\item Larger groups $\Rightarrow$ simpler terms."
    r"\item Wrap-around edges are adjacent."
    r"\end{itemize}"
    r"A group of 2 removes 1 variable; a group of 4 removes 2."),
   ("Design Flow",
    r"\begin{enumerate}"
    r"\item Specify behaviour as a truth table."
    r"\item Extract SOP, then minimize (algebra or K-map)."
    r"\item Draw the gate-level circuit."
    r"\end{enumerate}"
    r"Result: a correct circuit with the fewest gates.")],
  I("SOP expressions come directly from truth-table 1s.",
    "K-maps minimize by grouping adjacent minterms.",
    "The design flow goes spec to truth table to minimized circuit."),
  I("Build the SOP for a 3-input majority function.",
    "Minimize $F=\\sum m(0,1,2,3)$ of two variables with a K-map.",
    "Draw the gate circuit for $Y=A\\oplus B$ using AND/OR/NOT."))

M[7] = ("Review: Number Systems \\& Combinational Logic",
  "Students are able to integrate number systems and combinational logic (Meetings 1--6) to solve digital problems.",
  I("Combine conversion and logic in one problem.",
    "Solve mixed exercises accurately.",
    "Prepare comprehensively for evaluation."),
  [("Why an Integration Meeting?",
    r"""Real digital problems rarely test one topic in isolation --- a single design task
    might require converting a sensor value, checking for signed overflow, and simplifying
    a control-logic expression, all in the same problem.
    \begin{itemize}
    \item This meeting stitches Meetings 1--6 together with mixed exercises.
    \item Goal: recognize which tool (conversion, arithmetic, or Boolean algebra)
    a sub-problem needs, then apply it correctly.
    \end{itemize}"""),
   ("Recap: Number Systems",
    r"""\begin{center}\begin{tabular}{c|c|c|c}\hline
    Decimal & Binary & Octal & Hex\\\hline
    45 & 101101 & 055 & 2D\\ 178 & 10110010 & 262 & B2\\\hline
    \end{tabular}\end{center}
    \begin{itemize}
    \item Decimal $\leftrightarrow$ binary: repeated division (bottom-up) / weighted sum.
    \item Binary $\leftrightarrow$ octal/hex: group into 3-bit / 4-bit chunks.
    \end{itemize}"""),
   ("Recap: Signed Numbers \\& Range",
    r"""\begin{itemize}
    \item Two's complement: invert all bits, add 1.
    \item n-bit range: $-2^{n-1}$ to $+2^{n-1}-1$.
    \end{itemize}
    \begin{center}\begin{tabular}{c|c|c}\hline
    Bits & Min & Max\\\hline 4 & $-8$ & $+7$\\ 8 & $-128$ & $+127$\\\hline
    \end{tabular}\end{center}"""),
   ("Recap: Binary Arithmetic \\& Overflow",
    r"""\begin{itemize}
    \item Addition: bit-by-bit with carry, same as decimal in base 2.
    \item Subtraction: $A-B = A + \text{two's complement}(B)$, discard final carry-out.
    \item Signed overflow: same-sign operands producing an opposite-sign result.
    \item Overflow $= C_{in}\oplus C_{out}$ of the MSB position.
    \end{itemize}"""),
   ("Recap: Boolean Algebra Laws",
    r"""\begin{itemize}
    \item Identity: $A+0=A$, $A\cdot1=A$. Null: $A+1=1$, $A\cdot0=0$.
    \item Complement: $A+\overline{A}=1$, $A\cdot\overline{A}=0$.
    \item De Morgan: $\overline{A+B}=\overline{A}\,\overline{B}$, $\overline{A\cdot B}=\overline{A}+\overline{B}$.
    \item Distributive/absorption laws also simplify expressions before drawing gates.
    \end{itemize}"""),
   ("Recap: Karnaugh Maps",
    r"""\begin{itemize}
    \item Group adjacent 1-cells in powers of two (1, 2, 4, 8, ...).
    \item Bigger groups $\Rightarrow$ fewer literals in the resulting term.
    \item Map edges wrap around (leftmost column is adjacent to rightmost).
    \item Combine all groups with OR to get the minimized SOP expression.
    \end{itemize}"""),
   ("Integrated Worked Example",
    r"""Design a 4-bit adder with an overflow indicator, encoding two decimal inputs first.
    \begin{enumerate}
    \item Convert $6_{10}$ and $5_{10}$ to 4-bit two's complement: $0110$, $0101$.
    \item Add: $0110+0101 = 1011_2$.
    \item Check sign: both inputs positive (MSB 0), result negative (MSB 1) $\Rightarrow$ overflow.
    \item Overflow logic: $V = C_3 \oplus C_4$ (carry into vs.\ out of the MSB).
    \end{enumerate}
    This single problem touches conversion, arithmetic, and Boolean logic for the flag."""),
   ("Cross-Topic Pitfalls",
    r"""\begin{itemize}
    \item Forgetting which conversion direction reads top-down vs.\ bottom-up.
    \item Confusing unsigned carry-out with signed overflow.
    \item Skipping simplification and drawing an unminimized (larger) circuit.
    \item Not labelling the radix (subscript) on intermediate results.
    \end{itemize}"""),
   ("Practice 1 -- Problem",
    r"Convert $B3_{16}$ to binary, then to decimal."),
   ("Practice 1 -- Solution",
    r"""$B{=}1011$, $3{=}0011$ $\Rightarrow B3_{16} = 10110011_2$.
    \\Weighted sum: $128+32+16+2+1 = 179_{10}$.
    \\Check via hex weights: $11\cdot16+3\cdot1 = 176+3 = 179_{10}$. \checkmark"""),
   ("Practice 2 -- Problem",
    r"Add $00101101_2$ and $10110011_2$ (8-bit, unsigned) and separately check signed overflow (two's complement)."),
   ("Practice 2 -- Solution",
    r"""Unsigned: $00101101 + 10110011 = 11100000_2$ (no carry out of bit 7, so no unsigned carry).
    \\Signed check: $00101101$ is $+45$ (positive), $10110011$ is negative (MSB=1)
    $\Rightarrow$ operands have different signs, so \textbf{overflow cannot occur} by the same-sign rule."""),
   ("Practice 3 -- Problem",
    r"Simplify $Y = \overline{A}\,\overline{B}\,C + \overline{A}BC + AB C$ using Boolean algebra or a K-map, then draw the minimized gate circuit."),
   ("Practice 3 -- Solution",
    r"""Factor: $Y = \overline{A}C(\overline{B}+B) + ABC = \overline{A}C + ABC = C(\overline{A}+AB) = C(\overline{A}+B)$.
    \\Minimized: $Y = \overline{A}C + BC$ --- a 2-input AND/AND/OR circuit (3 gates instead of the original 3 AND + 1 OR of 3 terms)."""),
   ("Practice 4 -- Problem",
    r"A 4-bit magnitude comparator control signal must assert when two two's-complement inputs are equal AND their sum would overflow. Sketch the reasoning."),
   ("Practice 4 -- Solution",
    r"""\begin{enumerate}
    \item Equality: $EQ = \prod_i (\overline{A_i \oplus B_i})$ --- XNOR every bit pair, AND the results.
    \item Overflow: $V = C_3 \oplus C_4$ from the adder's MSB stage.
    \item Control signal: $Z = EQ \cdot V$ --- combine with a single AND gate.
    \end{enumerate}
    This shows how conversion-free Boolean reasoning composes with the arithmetic overflow flag.""")],
  I("Meetings 1--6 combine into end-to-end digital problems.",
    "Overflow and conversion checks catch most errors.",
    "Verification by back-conversion and Boolean laws are reliable habits."),
  I("Convert $B3_{16}$ to binary, then add $00101101_2$ and report overflow.",
    "Minimize a 3-variable function of your choice and draw it.",
    "Prepare a one-page formula sheet for the midterm."))

M[8] = ("Integrated Review (Pre-Midterm)",
  "Students are able to solve integrated problems in preparation for the mid-semester exam.",
  I("Solve integrated exercises under time.",
    "Identify and correct common mistakes.",
    "Confirm readiness for the midterm."),
  [("Midterm Scope",
    r"""The midterm (Meeting 9) covers \textbf{Meetings 1--8} end to end:
    \begin{itemize}
    \item Number systems: decimal, binary, octal, hexadecimal, and fractional conversions.
    \item Signed representation: sign-magnitude, one's and two's complement, range.
    \item Binary arithmetic: addition, subtraction, and overflow detection.
    \item Logic gates, Boolean algebra, and K-map minimization.
    \item Combinational design flow: truth table $\to$ SOP $\to$ minimized circuit.
    \end{itemize}"""),
   ("Formula Sheet: Conversions",
    r"""\begin{itemize}
    \item Decimal $\to$ binary: repeated division by 2 (remainders bottom-up).
    \item Fractional decimal $\to$ binary: repeated multiplication by 2 (bits top-down).
    \item Binary $\leftrightarrow$ octal: group by 3. Binary $\leftrightarrow$ hex: group by 4.
    \item Any base $\to$ decimal: $N=\sum_i d_i r^i$.
    \end{itemize}"""),
   ("Formula Sheet: Signed Numbers \\& Arithmetic",
    r"""\begin{itemize}
    \item Two's complement: invert, add 1. Range: $-2^{n-1}$ to $2^{n-1}-1$.
    \item $A-B = A + \text{two's complement}(B)$, discard carry-out.
    \item Overflow $=C_{in}\oplus C_{out}$ of the sign bit; only same-sign operands can overflow.
    \end{itemize}"""),
   ("Formula Sheet: Boolean Algebra \\& K-Maps",
    r"""\begin{itemize}
    \item De Morgan: $\overline{A+B}=\overline{A}\,\overline{B}$; $\overline{AB}=\overline{A}+\overline{B}$.
    \item SOP directly from truth-table 1-rows (minterms).
    \item K-map groups of $2^k$ adjacent cells remove $k$ variables from the term.
    \end{itemize}"""),
   ("Common Mistakes",
    r"""\begin{itemize}
    \item Forgetting to pad bits before grouping to octal/hex.
    \item Confusing carry-out (unsigned) with signed overflow.
    \item Dropping the $+1$ step in two's complement.
    \item Not simplifying before drawing gates -- costs marks even if the truth table is right.
    \item Misreading K-map cell adjacency at the map's wrap-around edges.
    \end{itemize}"""),
   ("Time-Management Strategy",
    r"""\begin{itemize}
    \item Skim the whole exam first; do the fastest problems first to bank points.
    \item Show intermediate steps -- partial credit rewards visible working.
    \item Reserve the last 5 minutes to re-check overflow signs and radix labels.
    \end{itemize}"""),
   ("Practice 1 -- Problem",
    r"Convert $214_{10}$ to binary, octal, and hexadecimal."),
   ("Practice 1 -- Solution",
    r"""$214_{10} = 11010110_2$ (repeated division).
    \\Group by 3: $011\,010\,110 \to 326_8$.
    \\Group by 4: $1101\,0110 \to D6_{16}$."""),
   ("Practice 2 -- Problem",
    r"Represent $-37_{10}$ in 8-bit two's complement, and state the range of an 8-bit signed number."),
   ("Practice 2 -- Solution",
    r"""$+37 = 00100101_2$. Invert: $11011010$. Add 1: $11011011_2 = -37_{10}$.
    \\8-bit signed range: $-128$ to $+127$."""),
   ("Practice 3 -- Problem",
    r"Minimize $F=\sum m(1,3,5,7)$ over 3 variables ($A,B,C$) using a K-map."),
   ("Practice 3 -- Solution",
    r"""Minterms 1,3,5,7 all have $C{=}1$ (odd minterms).
    \\Grouping all four cells (a group of 4) removes both $A$ and $B$: $F = C$.
    \\Verify: minterm 1 ($001$), 3 ($011$), 5 ($101$), 7 ($111$) all end in 1. \checkmark"""),
   ("Practice 4 -- Problem",
    r"A 5-bit signed register holds $-9_{10}$. Add $6_{10}$ to it and determine if overflow occurs."),
   ("Practice 4 -- Solution",
    r"""$-9$ in 5-bit two's complement: $+9=01001$, invert $10110$, $+1=10111$.
    \\$6 = 00110$. Sum: $10111+00110 = 11101_2$.
    \\Result $11101$ = $-3_{10}$ (correct: $-9+6=-3$). Operands have different signs, so
    overflow cannot occur -- and indeed the result is correct.""")],
  I("Midterm covers Meetings 1--8 end to end.",
    "Most errors come from padding, overflow, and the two's-complement +1.",
    "Timed self-checked practice builds readiness."),
  I("Complete the timed practice set and mark your own work.",
    "List every formula you needed and memorize gaps.",
    "Redo any problem you missed from a clean start."))

# ---- second half ----
M[10] = ("Flip-Flops: Terminology \\& Types (SR, D)",
  "Students are able to explain flip-flop terminology and the operation of SR and D flip-flops.",
  I("Define latch, flip-flop, clock, and edge-triggering.",
    "Describe the SR flip-flop and its forbidden state.",
    "Describe the D flip-flop."),
  [("From Combinational to Sequential Memory",
    r"""Every circuit studied so far (Meetings 1--8) was \textbf{combinational}: output depends
    only on the present inputs, with no memory of the past.
    \begin{itemize}
    \item Real systems (counters, registers, flight-computer state machines) must \textbf{remember}
    previous values.
    \item A \textbf{memory element} (latch or flip-flop) stores one bit by feeding its own output
    back as an input -- a feedback loop.
    \item This meeting starts sequential logic: terminology, then the SR and D flip-flops.
    \end{itemize}"""),
   ("Latch vs. Flip-Flop",
    r"""\begin{itemize}
    \item \textbf{Latch:} \emph{level-sensitive} -- output can change any time the enable/clock
    input is at its active level.
    \item \textbf{Flip-flop:} \emph{edge-triggered} -- output changes only at the instant the clock
    transitions (rising edge $\uparrow$ or falling edge $\downarrow$).
    \item Edge-triggering avoids "racing" -- multiple unwanted changes while the clock level is held.
    \item Outputs are labelled $Q$ (the stored bit) and $\overline{Q}$ (its complement).
    \end{itemize}"""),
   ("The SR Latch (Gate Level)",
    r"""Built from two cross-coupled NOR (or NAND) gates -- the simplest memory circuit.
    \begin{itemize}
    \item \textbf{S} (Set) $\to$ forces $Q=1$.
    \item \textbf{R} (Reset) $\to$ forces $Q=0$.
    \item When $S=R=0$, the latch \textbf{holds} its last value -- this feedback is the memory.
    \end{itemize}"""),
   ("SR Flip-Flop Truth Table",
    r"""\begin{center}\begin{tabular}{cc|c|l}\hline
    $S$&$R$&$Q_{next}$&Meaning\\\hline
    0&0&$Q$&hold (no change)\\ 0&1&0&reset\\ 1&0&1&set\\ 1&1&forbidden&both outputs forced --- invalid\\\hline
    \end{tabular}\end{center}
    $S=R=1$ is invalid because both $Q$ and $\overline{Q}$ would be forced to the same
    logic level, breaking the complementary-output assumption once $S,R$ both return to 0."""),
   ("Clocked SR Flip-Flop",
    r"""Adding a clock (CLK) input gates the S and R signals so they only take effect on
    an active clock edge or level.
    \[ S' = S\cdot CLK, \qquad R' = R\cdot CLK \]
    \begin{itemize}
    \item Between active clock periods, the flip-flop ignores $S$ and $R$ and holds its state.
    \item This is the bridge from asynchronous latches to synchronous, clock-driven systems.
    \end{itemize}"""),
   ("The D Flip-Flop",
    r"""The \textbf{D (Data / Delay)} flip-flop removes the forbidden state entirely by feeding
    a single input through an inverter to internally generate $S$ and $R$.
    \begin{center}\begin{tabular}{c|c}\hline $D$&$Q_{next}$\\\hline 0&0\\1&1\\\hline\end{tabular}\end{center}
    \begin{itemize}
    \item $Q_{next}=D$: whatever is on $D$ at the active clock edge becomes the new $Q$.
    \item It is the standard storage element for registers, pipelines, and memory cells.
    \end{itemize}"""),
   ("Characteristic Equation \\& Timing Diagram",
    r"""The \textbf{characteristic equation} summarizes next-state behaviour in one formula:
    D flip-flop: $Q_{next}=D$. SR flip-flop: $Q_{next}=S+\overline{R}\,Q$ (with $SR=0$ enforced).
    \begin{itemize}
    \item A timing diagram plots CLK, inputs, and $Q$ against time.
    \item $Q$ only changes exactly at the rising (or falling) clock edge, never in between.
    \end{itemize}"""),
   ("Common Pitfalls \\& Tips",
    r"""\begin{itemize}
    \item Treating a latch's enable input as if it were an edge-triggered clock.
    \item Forgetting the SR forbidden state exists -- always check $S=R=1$ separately.
    \item Reading $Q_{next}$ at the wrong time -- it is defined \emph{after} the active edge.
    \item Confusing $D$ (drives $Q_{next}$ directly) with $S/R$ (which set or reset relative to old $Q$).
    \end{itemize}"""),
   ("Practice 1 -- Problem",
    r"Complete the SR flip-flop truth table for all four $(S,R)$ combinations and mark the invalid row."),
   ("Practice 1 -- Solution",
    r"""$00\to Q$ (hold); $01\to 0$ (reset); $10\to1$ (set); $11\to$ forbidden
    (both $Q,\overline{Q}$ forced to 0, violating $Q\neq\overline{Q}$ once $S,R\to0$)."""),
   ("Practice 2 -- Problem",
    r"Given CLK pulses at $t=1,3,5,7$ and $D=1,0,1,1$ at those instants (starting $Q=0$), draw/describe $Q$ after each clock edge."),
   ("Practice 2 -- Solution",
    r"""$t{=}1$: $D{=}1\Rightarrow Q{=}1$. $t{=}3$: $D{=}0\Rightarrow Q{=}0$.
    $t{=}5$: $D{=}1\Rightarrow Q{=}1$. $t{=}7$: $D{=}1\Rightarrow Q{=}1$ (no change).
    \\$Q$ only updates exactly at each rising edge, holding steady between edges."""),
   ("Practice 3 -- Problem",
    r"Explain, using the SR truth table, why $S=1,R=1$ cannot be allowed in a working design."),
   ("Practice 3 -- Solution",
    r"""With $S=R=1$ both NOR gates output 0, forcing $Q=\overline{Q}=0$ simultaneously.
    \\If $S,R$ then both drop to 0 at the same instant, the next state is unpredictable
    (depends on gate delay mismatches) -- a race condition. Designers simply forbid this input combination."""),
   ("Practice 4 -- Problem",
    r"A D flip-flop currently holds $Q=1$. Its D input is tied to $\overline{Q}$ (its own complement). Describe what happens on each clock edge."),
   ("Practice 4 -- Solution",
    r"""Since $Q_{next}=D=\overline{Q}$, the flip-flop \textbf{toggles} every clock edge:
    $1\to0\to1\to0\dots$
    \\This is exactly how a T (toggle) flip-flop can be built from a D flip-flop -- previewed next meeting.""")],
  I("Flip-flops store one bit and update on a clock edge.",
    "The SR flip-flop has a forbidden $S=R=1$ state.",
    "The D flip-flop simply latches its input, $Q_{next}=D$."),
  I("Complete the SR truth table and mark the invalid row.",
    "Draw the timing of a D flip-flop for a given clock and D.",
    "Explain the difference between a latch and a flip-flop."))

M[11] = ("Flip-Flops: JK, T \\& Applications",
  "Students are able to analyze JK and T flip-flops and their applications (counters/registers).",
  I("Describe the JK flip-flop and toggle behaviour.",
    "Describe the T flip-flop.",
    "Explain counter and register applications."),
  [("Fixing the SR Forbidden State",
    r"""Last meeting's SR flip-flop had one flaw: $S=R=1$ was forbidden.
    \begin{itemize}
    \item The \textbf{JK flip-flop} (named after Jack Kilby) resolves this by feeding $Q$ and
    $\overline{Q}$ back to gate the inputs.
    \item When both inputs are asserted, instead of an invalid state, the flip-flop
    \textbf{toggles} to the opposite value.
    \item This makes JK the most versatile flip-flop -- it can emulate SR, D, and T behaviour.
    \end{itemize}"""),
   ("JK Flip-Flop Truth Table",
    r"""\begin{center}\begin{tabular}{cc|c|l}\hline $J$&$K$&$Q_{next}$&Meaning\\\hline
    0&0&$Q$&hold\\ 0&1&0&reset\\ 1&0&1&set\\ 1&1&$\overline{Q}$&toggle\\\hline\end{tabular}\end{center}
    Characteristic equation: $Q_{next} = J\overline{Q} + \overline{K}\,Q$."""),
   ("Master-Slave Construction",
    r"""A single-latch JK can "race" if $J=K=1$ and the clock level stays active long enough
    to toggle more than once.
    \begin{itemize}
    \item \textbf{Master-slave} JK uses two latches in series: master captures on one clock
    phase, slave releases on the other.
    \item Modern designs instead use \textbf{edge-triggered} JK flip-flops, sampling inputs
    only at the exact clock edge -- avoiding the race entirely.
    \end{itemize}"""),
   ("The T (Toggle) Flip-Flop",
    r"""Tie $J=K=T$ to collapse the JK table into a single input.
    \begin{center}\begin{tabular}{c|c}\hline $T$&$Q_{next}$\\\hline 0&$Q$\\1&$\overline{Q}$\\\hline\end{tabular}\end{center}
    Characteristic equation: $Q_{next} = T \oplus Q$.
    \\$T=1$ flips the state every clock edge -- ideal for frequency division and counters."""),
   ("Excitation Tables",
    r"""An \textbf{excitation table} answers the reverse question: given a desired
    $Q\to Q_{next}$ transition, what inputs are required?
    \begin{center}\begin{tabular}{cc|cc|cc}\hline
    $Q$&$Q_{next}$&$J$&$K$&$D$&$T$\\\hline
    0&0&0&X&0&0\\ 0&1&1&X&1&1\\ 1&0&X&1&0&1\\ 1&1&X&0&1&0\\\hline
    \end{tabular}\end{center}
    X = don't-care. Excitation tables are the starting point for sequential circuit design."""),
   ("Application: Frequency Division",
    r"""Each T (or toggling JK) flip-flop divides its clock frequency by 2.
    \begin{itemize}
    \item 1 stage: $f/2$. \quad 2 stages: $f/4$. \quad $n$ stages: $f/2^n$.
    \item Cascading toggle flip-flops is the basis of a binary ripple counter.
    \end{itemize}"""),
   ("Application: Registers",
    r"""\begin{itemize}
    \item \textbf{Registers} use D flip-flops (one per bit) sharing a common clock to
    store a multi-bit word simultaneously.
    \item An 8-bit register = 8 D flip-flops; all update on the same clock edge.
    \item Registers hold CPU operands, addresses, and pipeline data (foreshadowing Meeting 15/16).
    \end{itemize}"""),
   ("Common Pitfalls \\& Tips",
    r"""\begin{itemize}
    \item Forgetting JK's toggle row ($J=K=1$) -- easy to mistake for "forbidden" out of habit.
    \item Using level-sensitive JK without considering the race condition.
    \item Mixing up excitation tables (design direction) with truth tables (analysis direction).
    \end{itemize}"""),
   ("Practice 1 -- Problem",
    r"Complete the JK flip-flop truth table including the toggle row, and give its characteristic equation."),
   ("Practice 1 -- Solution",
    r"""$00\to Q$, $01\to0$, $10\to1$, $11\to\overline{Q}$.
    \\Characteristic equation: $Q_{next}=J\overline{Q}+\overline{K}Q$."""),
   ("Practice 2 -- Problem",
    r"Show how three T flip-flops (each fed the previous stage's $Q$ as its clock) divide an input clock by 8."),
   ("Practice 2 -- Solution",
    r"""Each stage with $T=1$ toggles once per input clock edge it receives, halving frequency:
    stage 1 output $=f/2$, stage 2 (clocked by stage 1) $=f/4$, stage 3 (clocked by stage 2) $=f/8$.
    \\Three cascaded toggle stages divide by $2^3=8$."""),
   ("Practice 3 -- Problem",
    r"Using the excitation table, find the required $J,K$ to take a flip-flop from $Q=1$ to $Q_{next}=0$."),
   ("Practice 3 -- Solution",
    r"""From the $1\to0$ row of the excitation table: $J=X$ (don't care), $K=1$.
    \\Any $J$ works as long as $K=1$, since $K=1$ forces a reset/toggle-to-0 from $Q=1$."""),
   ("Practice 4 -- Problem",
    r"Explain how to build a D flip-flop's behaviour using a JK flip-flop (i.e.\ find $J,K$ in terms of $D$)."),
   ("Practice 4 -- Solution",
    r"""Want $Q_{next}=D$ always. Setting $J=D$ and $K=\overline{D}$ gives:
    if $D=1$: $J{=}1,K{=}0\Rightarrow Q_{next}=1$; if $D=0$: $J{=}0,K{=}1\Rightarrow Q_{next}=0$.
    \\So $J=D,\ K=\overline{D}$ makes a JK flip-flop behave exactly like a D flip-flop.""")],
  I("The JK flip-flop toggles when $J=K=1$.",
    "The T flip-flop toggles when $T=1$, dividing frequency.",
    "Flip-flops build counters and registers."),
  I("Complete the JK truth table including the toggle row.",
    "Show how three T flip-flops divide a clock by 8.",
    "Explain how D flip-flops form a 4-bit register."))

M[12] = ("Sequential Logic Circuits",
  "Students are able to analyze sequential logic circuits (registers and counters).",
  I("Distinguish combinational and sequential logic.",
    "Analyze a shift register.",
    "Analyze a ripple counter."),
  [("Combinational vs. Sequential Logic",
    r"""\begin{itemize}
    \item \textbf{Combinational:} output depends only on the current inputs (Meetings 5--8).
    \item \textbf{Sequential:} output depends on current inputs \emph{and} stored state
    (flip-flops from Meetings 10--11).
    \item Sequential circuits always contain memory elements and a clock that sequences
    state changes.
    \end{itemize}
    This meeting builds two classic sequential building blocks: shift registers and counters."""),
   ("State Diagrams \\& Tables",
    r"""A sequential circuit's behaviour is captured by a \textbf{state diagram}: circles
    for states, arrows labelled with input/output for transitions.
    \begin{itemize}
    \item \textbf{Moore machine:} output depends only on the current state.
    \item \textbf{Mealy machine:} output depends on state \emph{and} current input.
    \item A state table lists, for every (state, input) pair, the next state and output.
    \end{itemize}"""),
   ("Shift Register Basics",
    r"""D flip-flops connected in series, each stage's $Q$ feeding the next stage's $D$,
    all sharing one clock.
    \begin{itemize}
    \item Each clock edge shifts every bit one position down the chain.
    \item Used for serial-to-parallel conversion, delay lines, and serial communication.
    \end{itemize}"""),
   ("Shift Register Variants",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Variant & Meaning\\\hline
    SISO & Serial-In, Serial-Out\\ SIPO & Serial-In, Parallel-Out\\
    PISO & Parallel-In, Serial-Out\\ PIPO & Parallel-In, Parallel-Out\\\hline
    \end{tabular}\end{center}
    SIPO is common for driving displays from a single serial data line;
    PISO is common for reading parallel switches over a single serial line."""),
   ("Ripple (Asynchronous) Counter",
    r"""Cascaded toggle flip-flops; each stage's $Q$ output clocks the next stage.
    \begin{itemize}
    \item An $n$-stage counter counts $0$ to $2^n-1$ then wraps around.
    \item \textbf{Ripple}: each stage's change propagates (with delay) to trigger the next --
    the count "ripples" through, stage by stage.
    \item Total propagation delay = sum of each flip-flop's individual delay -- limits max speed.
    \end{itemize}"""),
   ("Synchronous Counter",
    r"""All flip-flops share the \emph{same} clock signal; combinational logic determines
    each flip-flop's $J,K$ (or $T$) inputs so all bits update simultaneously.
    \begin{itemize}
    \item Eliminates ripple delay -- much faster for wide counters.
    \item More gates needed (each stage needs its own next-state logic).
    \item Preferred design in high-speed microcomputers and avionics timing circuits.
    \end{itemize}"""),
   ("Up, Down, and Modulo-N Counters",
    r"""\begin{itemize}
    \item \textbf{Up-counter:} increments each clock. \textbf{Down-counter:} decrements.
    \item \textbf{Modulo-N (mod-N):} resets to 0 after reaching $N-1$, even if $N\neq2^n$
    (e.g.\ a decade/mod-10 counter for BCD digits, reset logic clears it at count 10).
    \end{itemize}"""),
   ("Common Pitfalls \\& Tips",
    r"""\begin{itemize}
    \item Confusing SIPO (serial in) with PISO (serial out) -- read the acronym letter by letter.
    \item Assuming ripple counters are "free" -- their cumulative delay is a real speed limit.
    \item Forgetting a mod-N counter needs extra reset/decode logic beyond plain toggling.
    \end{itemize}"""),
   ("Practice 1 -- Problem",
    r"State one difference between combinational and sequential logic, and give one example circuit of each."),
   ("Practice 1 -- Solution",
    r"""Combinational: output depends only on present inputs (example: a full adder).
    \\Sequential: output depends on present inputs and stored state (example: a 4-bit counter)."""),
   ("Practice 2 -- Problem",
    r"Draw/describe a 3-bit SIPO shift register receiving the serial bit sequence $1,0,1$ (one bit per clock, oldest bit first)."),
   ("Practice 2 -- Solution",
    r"""Start $Q_2Q_1Q_0 = 000$.
    \\Clock 1 (in=1): $100$. Clock 2 (in=0): $010$. Clock 3 (in=1): $101$.
    \\After 3 clocks the register holds $101_2$, available in parallel on $Q_2Q_1Q_0$."""),
   ("Practice 3 -- Problem",
    r"Give the count sequence of a 3-bit ripple (binary) counter for 5 clock pulses, starting from 000."),
   ("Practice 3 -- Solution",
    r"""$000\to001\to010\to011\to100\to101$ (after 5 pulses).
    \\Each stage toggles when the previous stage falls from 1 to 0, rippling the carry upward."""),
   ("Practice 4 -- Problem",
    r"A mod-6 counter must count $0,1,2,3,4,5,0,1,\dots$ using 3 flip-flops. What extra logic is needed beyond a plain 3-bit binary counter?"),
   ("Practice 4 -- Solution",
    r"""A plain 3-bit counter counts $0$--$7$. To force it to reset at 6:
    \\Add a decoder (AND gate) that detects state $110_2$ (6) and asynchronously clears all
    flip-flops back to $000$, so the sequence skips 6 and 7 and restarts at 0.""")],
  I("Sequential logic adds stored state to combinational logic.",
    "Shift registers move data one bit per clock.",
    "Ripple counters cascade toggle flip-flops."),
  I("State one difference between combinational and sequential logic.",
    "Draw a 3-bit SIPO shift register.",
    "Give the count sequence of a 3-bit ripple counter."))

M[13] = ("Data Conversion: ADC",
  "Students are able to explain analog-to-digital conversion (ADC) principles.",
  I("Explain sampling and quantization.",
    "Describe resolution and step size.",
    "Name ADC uses in avionics."),
  [("Why Convert Analog to Digital?",
    r"""Sensors (airspeed, altitude, temperature, strain gauges) produce continuous
    \textbf{analog} voltages; microcomputers only process discrete \textbf{digital} values.
    \begin{itemize}
    \item An \textbf{ADC (Analog-to-Digital Converter)} bridges the two worlds.
    \item Every digital flight instrument depends on an ADC somewhere in its signal chain.
    \end{itemize}"""),
   ("Sampling",
    r"""\textbf{Sampling} measures the analog signal's instantaneous value at regular
    time intervals, spaced by the sampling period $T_s = 1/f_s$.
    \begin{itemize}
    \item \textbf{Nyquist criterion:} $f_s > 2f_{max}$, where $f_{max}$ is the highest
    frequency component in the signal.
    \item Violating Nyquist causes \textbf{aliasing}: high-frequency content folds back and
    appears as a false low-frequency signal in the digital output.
    \end{itemize}"""),
   ("Quantization",
    r"""\textbf{Quantization} maps each sampled voltage to the nearest of $2^n$ discrete levels.
    \begin{itemize}
    \item Because analog values are continuous but the levels are discrete, quantization
    always introduces a small error: \textbf{quantization error}, up to $\pm\tfrac12$ LSB.
    \item More bits $n$ $\Rightarrow$ more levels $\Rightarrow$ smaller error, at the cost of
    more conversion time and circuit complexity.
    \end{itemize}"""),
   ("Resolution \\& Step Size",
    r"""An $n$-bit ADC has $2^n$ output codes; the voltage represented by one code step is
    \[ \text{Step (LSB)} = \frac{V_{ref}}{2^n} \]
    \begin{center}\begin{tabular}{c|c|c}\hline Bits&Levels&Step ($V_{ref}=5$V)\\\hline
    8 & 256 & $19.5$ mV\\ 10 & 1024 & $4.88$ mV\\ 12 & 4096 & $1.22$ mV\\\hline\end{tabular}\end{center}"""),
   ("ADC Architectures (Overview)",
    r"""\begin{itemize}
    \item \textbf{Flash ADC:} a bank of comparators compares the input to $2^n{-}1$
    reference levels simultaneously -- extremely fast, but needs many comparators.
    \item \textbf{Successive Approximation (SAR):} binary-searches the input value one bit
    at a time using a DAC in the feedback loop -- good speed/accuracy/cost balance,
    the most common general-purpose ADC.
    \item \textbf{Dual-slope (integrating):} integrates the input then a reference, timing
    the result -- slow but very accurate and noise-resistant, used in precision instruments.
    \end{itemize}"""),
   ("The SAR Conversion Process",
    r"""\begin{enumerate}
    \item Start with the MSB guessed as 1, rest 0; compare the DAC output to the input.
    \item If DAC output $>$ input, clear that bit; otherwise keep it set.
    \item Move to the next bit and repeat, from MSB to LSB.
    \end{enumerate}
    An $n$-bit SAR conversion takes exactly $n$ comparison steps."""),
   ("ADC in Avionics",
    r"""\begin{itemize}
    \item Air data computers digitize pitot-static pressure sensors via ADC.
    \item Engine parameter sensors (EGT, oil pressure, RPM) feed ADC channels for EICAS display.
    \item Multiple analog sensor channels are often time-multiplexed into one ADC to save cost.
    \end{itemize}"""),
   ("Common Pitfalls \\& Tips",
    r"""\begin{itemize}
    \item Forgetting the Nyquist rate is a strict inequality ($f_s > 2f_{max}$, not $\geq$ in practice --
    real systems use extra margin).
    \item Confusing resolution (number of bits/levels) with accuracy (how close to the true value).
    \item Mixing up step size units -- always divide $V_{ref}$ by $2^n$, not $2^n-1$, per convention here.
    \end{itemize}"""),
   ("Practice 1 -- Problem",
    r"Compute the step size of a 10-bit ADC with $V_{ref}=3.3$V."),
   ("Practice 1 -- Solution",
    r"""Step $= V_{ref}/2^n = 3.3/1024 \approx 3.22$ mV per code step."""),
   ("Practice 2 -- Problem",
    r"State the minimum sampling rate for a signal whose highest frequency component is 4 kHz, and explain what happens if you sample slower."),
   ("Practice 2 -- Solution",
    r"""Minimum $f_s > 2\times4\text{ kHz} = 8$ kHz (Nyquist).
    \\Sampling slower than 8 kHz causes \textbf{aliasing}: the high-frequency content folds
    back and is misread as a lower, false frequency in the digital signal."""),
   ("Practice 3 -- Problem",
    r"An 8-bit ADC with $V_{ref}=5$V reads a code of $102_{10}$. What analog voltage does this represent?"),
   ("Practice 3 -- Solution",
    r"""Step $=5/256\approx19.53$ mV.
    \\Voltage $\approx 102 \times 19.53\text{ mV} \approx 1.99$ V."""),
   ("Practice 4 -- Problem",
    r"A SAR ADC converts a 12-bit sample. How many comparison steps does one conversion take, and why is SAR often preferred over flash ADCs in general-purpose designs?"),
   ("Practice 4 -- Solution",
    r"""A 12-bit SAR conversion takes exactly 12 comparison steps (one bit resolved per step).
    \\SAR needs only 1 comparator and 1 DAC regardless of resolution, versus a flash ADC's
    $2^{12}-1 = 4095$ comparators -- far cheaper and lower power for the same resolution,
    at the cost of being slower than flash.""")],
  I("ADC turns analog sensor signals into digital values.",
    "Sampling and quantization define the conversion; Nyquist bounds $f_s$.",
    "Resolution is $V_{ref}/2^n$."),
  I("Compute the step size of a 10-bit ADC with $V_{ref}=3.3$V.",
    "State the minimum sampling rate for a 4 kHz signal.",
    "Explain aliasing in one sentence."))

M[14] = ("Data Conversion: DAC",
  "Students are able to explain digital-to-analog conversion (DAC) principles.",
  I("Explain how a DAC reconstructs an analog signal.",
    "Describe binary-weighted and R-2R DACs.",
    "Relate resolution to output steps."),
  [("Purpose of a DAC",
    r"""A \textbf{DAC (Digital-to-Analog Converter)} converts a digital code back into a
    proportional analog voltage or current -- the reverse operation of the ADC studied last meeting.
    \begin{itemize}
    \item Used to drive actuators, control-surface servos, audio outputs, and analog displays.
    \item Every closed-loop digital control system (autopilot, engine control) needs a DAC
    to turn its computed digital command back into a physical analog signal.
    \end{itemize}"""),
   ("Binary-Weighted Resistor DAC",
    r"""Each input bit switches a current through a resistor scaled by a power of two:
    $R, R/2, R/4, \dots, R/2^{n-1}$, and an op-amp sums the resulting currents.
    \begin{itemize}
    \item More significant bits use smaller resistors (larger current contribution).
    \item Drawback: requires a wide range of precise resistor values -- hard to fabricate
    accurately as $n$ grows (e.g.\ an 8-bit DAC needs resistor ratios spanning 128:1).
    \end{itemize}"""),
   ("R-2R Ladder DAC",
    r"""Uses \textbf{only two} resistor values ($R$ and $2R$) arranged in a ladder network.
    \begin{itemize}
    \item Every bit's contribution is derived the same way regardless of position, so
    manufacturing only needs one resistor ratio to be accurate.
    \item Far easier and cheaper to fabricate precisely than binary-weighted -- the
    dominant architecture in practical integrated DACs.
    \end{itemize}"""),
   ("Resolution \\& Output Formula",
    r"""For an $n$-bit DAC with digital input code $D$ (as an integer $0$ to $2^n-1$):
    \[ V_{out} = V_{ref}\cdot \frac{D}{2^n} \]
    Example: 8-bit DAC, $V_{ref}=5$V, code $10000000_2 = 128_{10}$:
    \[ V_{out} = 5\cdot 128/256 = 2.5\text{V} \]"""),
   ("DAC Step Size \\& Full-Scale Output",
    r"""\begin{itemize}
    \item Step size (1 LSB) $= V_{ref}/2^n$ -- same formula shape as ADC resolution.
    \item Full-scale output (all bits = 1) is slightly less than $V_{ref}$:
    $V_{FS} = V_{ref}\cdot(2^n-1)/2^n$, never reaching $V_{ref}$ exactly.
    \item Finer resolution (more bits) gives a smoother reconstructed waveform.
    \end{itemize}"""),
   ("Settling Time \\& Glitches",
    r"""\begin{itemize}
    \item \textbf{Settling time:} how long the output takes to stabilize within a specified
    error band after the input code changes -- bounds the DAC's maximum update rate.
    \item \textbf{Glitches:} brief incorrect output spikes during a code transition
    (e.g.\ $0111\to1000$) caused by switches not changing at exactly the same instant.
    \item A reconstruction (low-pass) filter after the DAC smooths steps and glitches into
    a continuous analog waveform.
    \end{itemize}"""),
   ("DAC in Avionics",
    r"""\begin{itemize}
    \item Autopilot computers output DAC signals to drive control-surface servo actuators.
    \item Cockpit analog gauges (where still used) are driven from a digital source via DAC.
    \item Audio warning/annunciator tones are often synthesized digitally then converted by DAC.
    \end{itemize}"""),
   ("Common Pitfalls \\& Tips",
    r"""\begin{itemize}
    \item Forgetting full-scale output never reaches $V_{ref}$ exactly (it stops at $(2^n{-}1)/2^n$ of it).
    \item Confusing DAC step size with ADC quantization error -- similar formula, opposite direction of conversion.
    \item Assuming DAC output is instantly clean -- settling time and glitches are real, especially at code
    boundaries with many bits changing at once.
    \end{itemize}"""),
   ("Practice 1 -- Problem",
    r"Compute the output of a 6-bit DAC ($V_{ref}=3.3$V) for code $101000_2$."),
   ("Practice 1 -- Solution",
    r"""$101000_2 = 40_{10}$. \quad $V_{out} = 3.3 \times 40/64 \approx 2.06$V."""),
   ("Practice 2 -- Problem",
    r"State one advantage of the R-2R ladder DAC over the binary-weighted resistor DAC."),
   ("Practice 2 -- Solution",
    r"""R-2R needs only two resistor values ($R$, $2R$) for any resolution, so it is far
    easier to manufacture with high precision than binary-weighted, which needs a wide,
    precisely scaled range of resistor values."""),
   ("Practice 3 -- Problem",
    r"How many output levels does a 10-bit DAC have, and what is its full-scale output for $V_{ref}=5$V?"),
   ("Practice 3 -- Solution",
    r"""Levels $=2^{10}=1024$.
    \\Full-scale $V_{FS} = 5\times(1024-1)/1024 \approx 4.995$V (never reaches exactly 5V)."""),
   ("Practice 4 -- Problem",
    r"A 4-bit DAC ($V_{ref}=8$V) must output approximately $5.0$V. Which digital code should be applied, and what is the actual output?"),
   ("Practice 4 -- Solution",
    r"""Step size $=8/16=0.5$V. Target code $D\approx5.0/0.5=10$, i.e.\ $1010_2$.
    \\Actual output $=8\times10/16=5.0$V exactly -- code $1010_2$ is the correct choice.""")],
  I("A DAC reconstructs an analog voltage from a digital code.",
    "Binary-weighted and R-2R are common architectures.",
    "$V_{out}=V_{ref}\\cdot D/2^n$."),
  I("Compute the output of a 6-bit DAC ($V_{ref}=3.3$V) for code $101000$.",
    "State one advantage of the R-2R ladder.",
    "How many output levels does a 10-bit DAC have?"))

M[15] = ("Computer Terminology",
  "Students are able to explain computer terminology relevant to microcomputers.",
  I("Define bit, byte, word, and bus.",
    "Explain CPU and memory roles.",
    "Relate terminology to microcomputer structure."),
  [("Why Terminology Matters",
    r"""Meetings 10--14 covered flip-flops and ADC/DAC -- the low-level building blocks.
    \begin{itemize}
    \item Before assembling them into a microcomputer (Meeting 16), we need a shared
    vocabulary for the units, storage, and communication paths involved.
    \item This terminology also appears throughout every avionics maintenance manual and
    datasheet you will read professionally.
    \end{itemize}"""),
   ("Data Units",
    r"""\begin{itemize}
    \item \textbf{Bit:} one binary digit (0 or 1) -- the smallest unit of information.
    \item \textbf{Nibble:} 4 bits (one hex digit).
    \item \textbf{Byte:} 8 bits -- the standard unit for addressing memory.
    \item \textbf{Word:} the CPU's natural data width, e.g.\ 8, 16, 32, or 64 bits, depending
    on the processor family.
    \end{itemize}"""),
   ("CPU, Memory, and Registers",
    r"""\begin{itemize}
    \item \textbf{CPU (Central Processing Unit):} fetches, decodes, and executes instructions.
    \item \textbf{Memory:} stores both the program's instructions and the data it works on
    (RAM = working storage, ROM = permanent firmware).
    \item \textbf{Registers:} very fast storage locations built directly into the CPU, used
    for operands and intermediate results.
    \end{itemize}"""),
   ("Buses: The Communication Backbone",
    r"""A \textbf{bus} is a shared set of wires carrying signals between the CPU, memory, and I/O.
    \begin{itemize}
    \item \textbf{Data bus:} carries the actual value being read or written; bidirectional.
    \item \textbf{Address bus:} carries the memory/I-O location the CPU wants to access;
    unidirectional (CPU drives it).
    \item \textbf{Control bus:} carries timing and command signals (read/write, clock,
    interrupt requests).
    \end{itemize}"""),
   ("Input/Output (I/O) Terminology",
    r"""\begin{itemize}
    \item \textbf{Peripheral:} any device attached to the CPU beyond core memory
    (sensors, displays, actuators, communication ports).
    \item \textbf{Port:} the addressable interface point where a peripheral connects to the bus.
    \item \textbf{Interrupt:} a signal that pauses normal CPU execution to service an urgent
    event (e.g.\ a sensor threshold exceeded), then resumes where it left off.
    \end{itemize}"""),
   ("Addressing Terminology",
    r"""\begin{itemize}
    \item \textbf{Address:} a numeric label identifying one memory location or I/O port.
    \item \textbf{Address space:} the full range of addresses a system can generate,
    $2^m$ locations for an $m$-bit address bus.
    \item \textbf{Memory-mapped I/O:} peripherals share the same address space as memory,
    accessed with ordinary read/write instructions.
    \end{itemize}"""),
   ("Firmware, Software, and Instructions",
    r"""\begin{itemize}
    \item \textbf{Instruction:} one CPU operation encoded as a binary pattern (opcode + operands).
    \item \textbf{Program:} an ordered sequence of instructions.
    \item \textbf{Firmware:} software stored in non-volatile memory (ROM/Flash), tightly
    coupled to specific hardware -- the norm in avionics LRUs.
    \end{itemize}"""),
   ("Common Pitfalls \\& Tips",
    r"""\begin{itemize}
    \item Confusing "byte" (always 8 bits) with "word" (varies by CPU architecture).
    \item Mixing up address bus (selects \emph{where}) with data bus (carries \emph{what}).
    \item Treating "software" and "firmware" as interchangeable -- firmware implies
    non-volatile, hardware-specific storage.
    \end{itemize}"""),
   ("Practice 1 -- Problem",
    r"How many bytes are in a 32-bit word?"),
   ("Practice 1 -- Solution",
    r"""$32\text{ bits}/8\text{ bits per byte} = 4$ bytes."""),
   ("Practice 2 -- Problem",
    r"Name the three buses and their functions."),
   ("Practice 2 -- Solution",
    r"""Data bus -- carries the value being transferred.
    \\Address bus -- selects which memory/I-O location is accessed.
    \\Control bus -- carries timing and command signals (read/write, clock, interrupts)."""),
   ("Practice 3 -- Problem",
    r"Explain the difference between a register and RAM."),
   ("Practice 3 -- Solution",
    r"""A register is a small number of very fast storage locations built into the CPU chip
    itself, holding operands/results during execution.
    \\RAM is external (or on-chip but separate) working memory, larger in capacity but
    slower to access than registers, holding the broader program's data."""),
   ("Practice 4 -- Problem",
    r"A system has a 16-bit address bus. What is its total address space, and how many bytes of memory can it directly address?"),
   ("Practice 4 -- Solution",
    r"""Address space $=2^{16}=65{,}536$ locations.
    \\If each address selects one byte, the system can directly address $65{,}536$ bytes $=64$ KB.""")],
  I("Bit, byte, and word describe data sizes.",
    "CPU, memory, and registers are the core components.",
    "Data, address, and control buses connect them."),
  I("How many bytes are in a 32-bit word?",
    "Name the three buses and their functions.",
    "Explain the difference between a register and RAM."))

M[16] = ("Introduction to Microcomputer Architecture",
  "Students are able to explain basic microcomputer architecture as an introduction to digital systems.",
  I("Describe the von Neumann model.",
    "Explain the fetch-execute cycle.",
    "Relate architecture to avionics computers."),
  [("Bringing the Pieces Together",
    r"""Meetings 10--15 gave the parts: flip-flops (memory), ADC/DAC (the analog interface),
    and terminology (bit/byte/word/bus).
    \begin{itemize}
    \item This meeting assembles them into the classic \textbf{microcomputer architecture} --
    the model underlying essentially every digital computer, from a phone to a flight computer.
    \end{itemize}"""),
   ("The Von Neumann Model",
    r"""A microcomputer has a CPU, memory, and I/O connected by a shared system bus,
    with instructions and data sharing the \emph{same} memory space.
    \begin{itemize}
    \item \textbf{CPU:} control unit + ALU + registers.
    \item \textbf{Memory:} holds both the program (instructions) and its data.
    \item \textbf{I/O:} sensors, displays, actuators -- the interface to the outside world.
    \end{itemize}"""),
   ("Von Neumann vs. Harvard Architecture",
    r"""\begin{itemize}
    \item \textbf{Von Neumann:} one memory, one bus for both instructions and data --
    simpler and cheaper, but instruction fetch and data access compete for the same bus.
    \item \textbf{Harvard:} separate memories/buses for instructions and data -- allows
    simultaneous fetch and data access, common in DSPs and microcontrollers needing
    predictable timing (e.g.\ flight-control loops).
    \end{itemize}"""),
   ("The Fetch--Execute Cycle in Detail",
    r"""\begin{enumerate}
    \item \textbf{Fetch:} the Program Counter (PC) supplies the instruction's address on
    the address bus; memory returns the instruction on the data bus into the
    Instruction Register (IR); PC increments.
    \item \textbf{Decode:} the control unit interprets the opcode in the IR, identifying
    the operation and its operands.
    \item \textbf{Execute:} the ALU/registers/memory perform the operation; results are
    written back and status flags update.
    \end{enumerate}
    This cycle repeats continuously, instruction after instruction, for the life of the program."""),
   ("Instruction Cycle Timing",
    r"""\begin{itemize}
    \item Each cycle phase (fetch, decode, execute) takes one or more clock periods,
    depending on the CPU's design.
    \item Simple CPUs execute phases strictly in sequence; advanced CPUs \textbf{pipeline}
    phases so several instructions are in different phases simultaneously, raising throughput.
    \item Clock frequency $\times$ cycles-per-instruction determines execution speed.
    \end{itemize}"""),
   ("Microprocessor, Microcontroller, Microcomputer",
    r"""\begin{itemize}
    \item \textbf{Microprocessor:} the CPU chip alone.
    \item \textbf{Microcontroller:} CPU + memory + I/O integrated on one chip -- common in
    embedded sensor nodes.
    \item \textbf{Microcomputer:} a complete system built around a CPU with external
    memory/I-O boards, as modelled by von Neumann above.
    \end{itemize}"""),
   ("Microcomputers in Avionics",
    r"""\begin{itemize}
    \item \textbf{FCC} (Flight Control Computer): reads sensor data, computes control laws,
    drives actuators.
    \item \textbf{FMC} (Flight Management Computer): navigation and performance computations.
    \item \textbf{FADEC} (Full Authority Digital Engine Control): closed-loop digital engine
    control, sampling sensors and commanding fuel/actuator outputs every fetch--execute cycle.
    \item All three follow the same CPU--memory--I-O--bus model from this meeting.
    \end{itemize}"""),
   ("Common Pitfalls \\& Tips",
    r"""\begin{itemize}
    \item Confusing the \emph{fetch} phase (getting the instruction) with the \emph{execute}
    phase (performing it) -- they use the bus for different purposes.
    \item Assuming Harvard architecture is strictly "better" -- it costs more hardware
    (separate memories/buses) for the timing benefit.
    \item Forgetting the PC increments during fetch, before the instruction is even decoded.
    \end{itemize}"""),
   ("Practice 1 -- Problem",
    r"List the three steps of the fetch-execute cycle and state what happens to the PC in each."),
   ("Practice 1 -- Solution",
    r"""Fetch: PC's address is read from memory into IR; PC increments.
    \\Decode: control unit interprets the IR; PC is unchanged.
    \\Execute: ALU/registers/memory perform the operation; PC unchanged unless the instruction is a jump/branch."""),
   ("Practice 2 -- Problem",
    r"Name the CPU sub-units and their roles."),
   ("Practice 2 -- Solution",
    r"""Control unit -- fetches/decodes instructions and generates sequencing signals.
    \\ALU -- performs arithmetic and logic operations.
    \\Registers -- fast on-chip storage for operands, results, and control values (PC, IR, etc.)."""),
   ("Practice 3 -- Problem",
    r"Give two avionics examples of microcomputers and one sensor/actuator each might interact with."),
   ("Practice 3 -- Solution",
    r"""FADEC -- reads engine RPM/temperature sensors, commands the fuel-metering actuator.
    \\FCC -- reads attitude/rate gyros, commands control-surface servo actuators."""),
   ("Practice 4 -- Problem",
    r"Explain why a Harvard architecture might be chosen over Von Neumann for a real-time flight-control microcontroller."),
   ("Practice 4 -- Solution",
    r"""Harvard's separate instruction and data buses let the CPU fetch the next instruction
    while simultaneously accessing data memory, avoiding bus contention.
    \\This gives more predictable, faster cycle timing -- critical for a hard real-time
    control loop where missing a deadline could destabilize the aircraft.""")],
  I("The von Neumann model shares memory for code and data.",
    "The fetch-decode-execute cycle drives every instruction.",
    "Avionics flight computers are microcomputers of this form."),
  I("List the three steps of the fetch-execute cycle.",
    "Name the CPU sub-units and their roles.",
    "Give two avionics examples of microcomputers."))

M[17] = ("Integrated Review (Pre-Final)",
  "Students are able to integrate flip-flops, data conversion, and microcomputers (Meetings 10--16) for the final exam.",
  I("Connect sequential logic, conversion, and architecture.",
    "Solve integrated post-midterm exercises.",
    "Confirm readiness for the final exam."),
  [("Final Scope (Meetings 10--16)",
    r"""\begin{itemize}
    \item Flip-flops: SR, D, JK, T -- terminology, truth tables, characteristic/excitation equations.
    \item Sequential circuits: shift registers, ripple and synchronous counters.
    \item ADC: sampling, quantization, resolution, SAR conversion.
    \item DAC: binary-weighted, R-2R, resolution, settling time.
    \item Computer terminology and microcomputer architecture: CPU, buses, fetch--execute cycle.
    \end{itemize}"""),
   ("Recap: Flip-Flops",
    r"""\begin{center}\begin{tabular}{c|c}\hline
    Type & $Q_{next}$\\\hline SR & $S+\overline{R}Q$ (with $SR=0$)\\
    D & $D$\\ JK & $J\overline{Q}+\overline{K}Q$\\ T & $T\oplus Q$\\\hline
    \end{tabular}\end{center}
    Sequential circuits combine flip-flops with a clock to add memory to a design."""),
   ("Recap: ADC/DAC Formulas",
    r"""\begin{itemize}
    \item ADC/DAC step size: $V_{ref}/2^n$.
    \item DAC output: $V_{out}=V_{ref}\cdot D/2^n$.
    \item Nyquist sampling: $f_s > 2f_{max}$.
    \end{itemize}"""),
   ("Recap: Microcomputer Architecture",
    r"""\begin{itemize}
    \item Von Neumann: shared memory/bus for code and data.
    \item Fetch $\to$ Decode $\to$ Execute, repeated every instruction.
    \item Data, address, and control buses connect CPU, memory, and I/O.
    \end{itemize}"""),
   ("Integration Example: Sensor-to-Actuator Chain",
    r"""A complete avionics control loop ties every post-midterm topic together:
    \begin{enumerate}
    \item \textbf{Sensor} produces an analog signal (e.g.\ pressure transducer).
    \item \textbf{ADC} samples and quantizes it into a digital word.
    \item \textbf{Microcomputer} (CPU + memory + registers, clocked by flip-flops)
    fetches, decodes, and executes control-law instructions on the digitized value.
    \item \textbf{DAC} converts the computed digital command back to an analog voltage.
    \item \textbf{Actuator} (e.g.\ servo) responds to the analog signal.
    \end{enumerate}
    Sequential logic (registers, counters) sequences and times every stage of this chain."""),
   ("Cross-Topic Pitfalls",
    r"""\begin{itemize}
    \item Mixing up ADC direction (analog $\to$ digital) with DAC (digital $\to$ analog).
    \item Forgetting flip-flop next-state depends on the \emph{clock edge}, not input level alone.
    \item Confusing address bus width (address space) with data bus width (word size).
    \end{itemize}"""),
   ("Final Exam Strategy",
    r"""\begin{itemize}
    \item Draw block diagrams to structure multi-stage answers (sensor$\to$ADC$\to\dots$).
    \item Track bit widths carefully through every ADC/DAC calculation.
    \item State flip-flop next-state directly from the characteristic equation when possible --
    faster than rebuilding the full truth table under time pressure.
    \item Budget time evenly; integrated questions are worth more but are not proportionally longer.
    \end{itemize}"""),
   ("Practice 1 -- Problem",
    r"Sketch a sensor-to-actuator digital chain and label each stage (5 blocks)."),
   ("Practice 1 -- Solution",
    r"""Sensor $\to$ ADC $\to$ Microcomputer (CPU+memory+registers) $\to$ DAC $\to$ Actuator.
    \\Each arrow represents a signal conversion or a bus transfer; the microcomputer's
    fetch--execute cycle processes the digitized sensor value between ADC and DAC."""),
   ("Practice 2 -- Problem",
    r"Compute the ADC step size and the corresponding DAC output for an 8-bit system with $V_{ref}=5$V and code $01100100_2$."),
   ("Practice 2 -- Solution",
    r"""Step size $=5/256\approx19.53$mV.
    \\$01100100_2 = 100_{10}$. \quad $V_{out}=5\times100/256\approx1.95$V."""),
   ("Practice 3 -- Problem",
    r"A JK flip-flop with $J=1,K=1$ is clocked 3 times starting from $Q=0$. What is $Q$ after each clock edge?"),
   ("Practice 3 -- Solution",
    r"""$J=K=1$ means toggle every edge: $Q_0=0 \to Q_1=1 \to Q_2=0 \to Q_3=1$."""),
   ("Practice 4 -- Problem",
    r"A 16-bit address bus microcomputer reads a sensor through a 10-bit ADC, computes a control law, then outputs through an 8-bit DAC. Identify one bit-width mismatch risk in this design and how to handle it."),
   ("Practice 4 -- Solution",
    r"""The ADC produces a 10-bit value but the DAC only accepts 8 bits -- directly writing
    the ADC code to the DAC would truncate 2 bits of resolution.
    \\Handle it by either scaling/rounding the 10-bit value down to 8 bits in software
    before output, or choosing a DAC with matching (or greater) resolution than the ADC.""")],
  I("Meetings 10--16 combine into a sensor-to-actuator chain.",
    "ADC/DAC math depends on tracking bit widths.",
    "Block diagrams structure integrated answers."),
  I("Sketch a sensor-to-actuator digital chain and label each stage.",
    "Compute ADC step and DAC output for a chosen 8-bit code.",
    "Build a formula sheet for the final exam."))

if __name__ == "__main__":
    order = [1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17]
    results = []
    for n in order:
        title, subclo, ind, slides, summ, asg = M[n]
        tex = build_deck(COURSE, SUBJECT, SUBTITLE, REF, CLO, n, title, subclo, ind, slides, summ, asg)
        results.append(compile_meeting(COURSE, n, tex))
        print(results[-1], flush=True)
    print("DONE", COURSE)
