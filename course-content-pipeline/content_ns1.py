#!/usr/bin/env python3
"""Natural_Science_1 (§4) — Mathematics + Chemistry ONLY (Physics is OUT).
Meetings 1-8,10-17."""
from build_slides import build_deck, compile_meeting

COURSE   = "Natural_Science_1"
SUBJECT  = "NATURAL SCIENCE 1"
SUBTITLE = "Applied Mathematics and Chemistry for Engineering"
REF      = "Engineering Mathematics (K.A. Stroud); General Chemistry (Chang \\& Goldsby)"
CLO = [
 "Perform arithmetic, algebraic manipulation, and scientific-calculator operations precisely.",
 "Formulate spatial and angular parameters using geometry and trigonometry.",
 "Apply logarithms and calculus (differentiation and integration) to engineering quantities.",
 "Classify chemical elements and analyze atomic, molecular, and crystal structure.",
 "Evaluate mixtures and the mechanical properties of engineering materials.",
]
I = lambda *xs: list(xs)
M = {}

M[1] = ("Mathematics: Arithmetic \\& Scientific Calculator",
  "Students are able to perform arithmetic operations and operate a scientific calculator precisely.",
  I("Apply order of operations.",
    "Use scientific notation and significant figures.",
    "Operate scientific-calculator functions."),
  [("Order of Operations",
    r"Evaluate in the order \textbf{BODMAS}: Brackets, Orders (powers/roots),"
    r" Division/Multiplication, Addition/Subtraction."
    r"\\Example: $2 + 3\times4^2 = 2 + 3\times16 = 50$."),
   ("Scientific Notation",
    r"Write numbers as $a\times10^{n}$ with $1\le|a|<10$."
    r"\begin{itemize}\item $48\,000 = 4.8\times10^{4}$."
    r"\item $0.00027 = 2.7\times10^{-4}$."
    r"\item Significant figures track measurement precision.\end{itemize}"),
   ("Using the Calculator",
    r"\begin{itemize}\item Set degree/radian mode correctly."
    r"\item Use $EXP$/$\times10^x$ for scientific notation, not $\times 10\;\hat{}\;x$ by hand."
    r"\item Respect the calculator's operator precedence with brackets."
    r"\item Round only at the final step.\end{itemize}")],
  I("BODMAS fixes the order of operations.",
    "Scientific notation and significant figures handle large/small values.",
    "Correct calculator mode and bracketing prevent errors."),
  I("Evaluate $5 + 2\\times(3^2 - 4)$.",
    "Write $0.000561$ and $92\\,300$ in scientific notation.",
    "Explain why final-step rounding matters."))

M[2] = ("Mathematics: Algebra",
  "Students are able to manipulate basic algebraic equations.",
  I("Simplify algebraic expressions.",
    "Solve linear equations.",
    "Solve quadratic equations."),
  [("Simplifying Expressions",
    r"Combine like terms and apply the distributive law."
    r"\\$3x + 2(x-4) = 3x + 2x - 8 = 5x - 8$."
    r"\\Laws of indices: $x^a x^b = x^{a+b}$, $\;(x^a)^b = x^{ab}$."),
   ("Linear Equations",
    r"Isolate the unknown by inverse operations."
    r"\\$3x - 5 = 16 \Rightarrow 3x = 21 \Rightarrow x = 7$."
    r"\\Always apply the same operation to both sides."),
   ("Quadratic Equations",
    r"For $ax^2+bx+c=0$: $\;x = \dfrac{-b\pm\sqrt{b^2-4ac}}{2a}$."
    r"\\The discriminant $b^2-4ac$ tells the nature of the roots:"
    r" positive (two real), zero (one), negative (complex).")],
  I("Simplify by combining like terms and using index laws.",
    "Linear equations are solved by inverse operations.",
    "The quadratic formula solves $ax^2+bx+c=0$."),
  I("Simplify $4(2x-3) - 2(x+1)$.",
    "Solve $5x + 7 = 3x - 5$.",
    "Solve $x^2 - 5x + 6 = 0$."))

M[3] = ("Mathematics: Geometry",
  "Students are able to formulate spatial parameters using geometry.",
  I("Compute areas and perimeters.",
    "Compute volumes and surface areas.",
    "Apply the Pythagorean theorem."),
  [("Plane Figures",
    r"\begin{center}\begin{tabular}{l|l|l}\hline"
    r"Shape & Area & Perimeter\\\hline"
    r"Rectangle & $lw$ & $2(l+w)$\\ Triangle & $\tfrac12 bh$ & $a+b+c$\\"
    r"Circle & $\pi r^2$ & $2\pi r$\\\hline\end{tabular}\end{center}"),
   ("Solids",
    r"\begin{center}\begin{tabular}{l|l|l}\hline"
    r"Solid & Volume & Surface\\\hline"
    r"Box & $lwh$ & $2(lw+lh+wh)$\\ Cylinder & $\pi r^2 h$ & $2\pi r(r+h)$\\"
    r"Sphere & $\tfrac43\pi r^3$ & $4\pi r^2$\\\hline\end{tabular}\end{center}"),
   ("Pythagorean Theorem",
    r"For a right triangle: $c^2 = a^2 + b^2$."
    r"\\Example: legs 3 and 4 give hypotenuse $\sqrt{9+16}=5$."
    r"\\Used to find distances and diagonal lengths.")],
  I("Standard formulas give area and perimeter of plane figures.",
    "Volume and surface formulas cover common solids.",
    "The Pythagorean theorem finds right-triangle sides."),
  I("Find the area and circumference of a circle with $r=6$ cm.",
    "Find the volume of a cylinder with $r=2$, $h=10$.",
    "Find the hypotenuse for legs 5 and 12."))

M[4] = ("Mathematics: Trigonometry",
  "Students are able to formulate angular parameters using trigonometry.",
  I("Define sine, cosine, tangent from a right triangle.",
    "Convert between degrees and radians.",
    "Apply trigonometric identities and the unit circle.",
    "Solve right triangles for engineering measurements."),
  [("Why Trigonometry Matters in Engineering",
    r"\begin{itemize}"
    r"\item Angles and lengths relate directly through trigonometric ratios."
    r"\item Avionics uses trig for antenna bearing, flight-path angles, and force resolution."
    r"\item This meeting builds ratio definitions up to solving full right triangles."
    r"\end{itemize}"),
   ("Trigonometric Ratios (SOH-CAH-TOA)",
    r"In a right triangle with angle $\theta$, hypotenuse $hyp$, side opposite $\theta$ ($opp$),"
    r" and side adjacent to $\theta$ ($adj$):"
    r"\\$\sin\theta = \dfrac{opp}{hyp}, \quad \cos\theta = \dfrac{adj}{hyp}, \quad \tan\theta = \dfrac{opp}{adj}$."
    r"\\Mnemonic: \textbf{SOH-CAH-TOA}."),
   ("The Unit Circle",
    r"On a circle of radius 1 centred at the origin, a point at angle $\theta$"
    r" from the positive $x$-axis has coordinates $(\cos\theta,\sin\theta)$."
    r"\begin{itemize}\item $\sin\theta$ and $\cos\theta$ are never larger than 1 in magnitude."
    r"\item Signs of $\sin,\cos,\tan$ change by quadrant (ASTC rule)."
    r"\end{itemize}"),
   ("Degrees and Radians",
    r"$180^\circ = \pi$ radians, so $1^\circ = \pi/180$ rad and $1\text{ rad}=180/\pi$ degrees."
    r"\begin{center}\begin{tabular}{c|c|c|c|c}\hline"
    r"Degrees & $0^\circ$&$30^\circ$&$45^\circ$&$90^\circ$\\\hline"
    r"Radians & $0$&$\pi/6$&$\pi/4$&$\pi/2$\\\hline"
    r"\end{tabular}\end{center}"
    r"Radians are required in calculus and most engineering formulas."),
   ("Common Angle Values",
    r"\begin{center}\begin{tabular}{c|c|c|c}\hline"
    r"$\theta$ & $\sin\theta$ & $\cos\theta$ & $\tan\theta$\\\hline"
    r"$0^\circ$ & $0$ & $1$ & $0$\\"
    r"$30^\circ$ & $1/2$ & $\sqrt3/2$ & $1/\sqrt3$\\"
    r"$45^\circ$ & $\sqrt2/2$ & $\sqrt2/2$ & $1$\\"
    r"$60^\circ$ & $\sqrt3/2$ & $1/2$ & $\sqrt3$\\"
    r"$90^\circ$ & $1$ & $0$ & undefined\\\hline"
    r"\end{tabular}\end{center}"),
   ("Key Identities",
    r"\begin{itemize}"
    r"\item Pythagorean identity: $\sin^2\theta + \cos^2\theta = 1$."
    r"\item Quotient identity: $\tan\theta = \sin\theta/\cos\theta$."
    r"\item Reciprocal ratios: $\csc\theta=1/\sin\theta$, $\sec\theta=1/\cos\theta$, $\cot\theta=1/\tan\theta$."
    r"\item Used to resolve forces, velocities, and signal phases into components.\end{itemize}"),
   ("Solving a Right Triangle",
    r"Given one side and one acute angle (besides the right angle), every other side and angle can be found:"
    r"\begin{enumerate}\item Identify which ratio relates the known and unknown sides."
    r"\item Rearrange for the unknown and substitute."
    r"\item Use $\theta_1+\theta_2=90^\circ$ for the remaining acute angle.\end{enumerate}"),
   ("In-Class Practice: Instructions",
    r"Work each pair of slides in order: attempt the problem first, then compare against"
    r" the solution shown on the following slide before moving on."),
   ("Practice 1 -- Problem",
    r"A 3-4-5 right triangle has legs 3 and 4 with hypotenuse 5."
    r"\\Find $\sin\theta$, $\cos\theta$, $\tan\theta$ for the smallest angle $\theta$"
    r" (opposite the side of length 3)."),
   ("Practice 1 -- Solution",
    r"Opposite $=3$, adjacent $=4$, hypotenuse $=5$."
    r"\\$\sin\theta = 3/5 = 0.6$, \quad $\cos\theta = 4/5 = 0.8$, \quad $\tan\theta = 3/4 = 0.75$."),
   ("Practice 2 -- Problem",
    r"Convert $120^\circ$ to radians, and convert $\tfrac{5\pi}{6}$ rad to degrees."),
   ("Practice 2 -- Solution",
    r"$120^\circ \times \dfrac{\pi}{180} = \dfrac{2\pi}{3}$ rad."
    r"\\$\dfrac{5\pi}{6}\times\dfrac{180}{\pi} = 150^\circ$."),
   ("Practice 3 -- Problem",
    r"Verify the identity $\sin^2 30^\circ + \cos^2 30^\circ = 1$ using the table of common angle values."),
   ("Practice 3 -- Solution",
    r"$\sin30^\circ=1/2 \Rightarrow \sin^2 30^\circ = 1/4$."
    r"\\$\cos30^\circ=\sqrt3/2 \Rightarrow \cos^2 30^\circ = 3/4$."
    r"\\Sum: $1/4+3/4=1$. \checkmark"),
   ("Practice 4 -- Problem",
    r"A ladder 10 m long leans against a wall, making a $60^\circ$ angle with the ground."
    r" How high up the wall does it reach?"),
   ("Practice 4 -- Solution",
    r"Height is opposite the $60^\circ$ angle, hypotenuse $=10$."
    r"\\$\sin 60^\circ = h/10 \Rightarrow h = 10\sin60^\circ = 10(\sqrt3/2)\approx8.66$ m.")],
  I("SOH-CAH-TOA defines the trig ratios from a right triangle.",
    "$180^\\circ$ equals $\\pi$ radians; the unit circle extends ratios to any angle.",
    "$\\sin^2\\theta+\\cos^2\\theta=1$ is the fundamental identity.",
    "A right triangle is fully solvable given one side and one acute angle."),
  I("Find $\\sin$, $\\cos$, $\\tan$ for a 5-12-13 triangle's smallest angle.",
    "Convert $210^\\circ$ to radians and $\\pi/3$ rad to degrees.",
    "Verify $\\sin^2 45^\\circ + \\cos^2 45^\\circ = 1$.",
    "A ramp of length 6 m rises at $20^\\circ$; find its vertical height."))

M[5] = ("Mathematics: Logarithms",
  "Students are able to apply logarithms and natural logarithms to engineering scales.",
  I("Define log and ln.",
    "Apply logarithm laws.",
    "Use logs for engineering scales (e.g. decibels)."),
  [("Definition",
    r"$\log_b x = y \iff b^y = x$."
    r"\begin{itemize}\item Common log: base 10 ($\log$)."
    r"\item Natural log: base $e\approx2.718$ ($\ln$).\end{itemize}"),
   ("Logarithm Laws",
    r"\begin{itemize}"
    r"\item $\log(xy) = \log x + \log y$."
    r"\item $\log(x/y) = \log x - \log y$."
    r"\item $\log(x^n) = n\log x$."
    r"\end{itemize}"),
   ("Engineering Use",
    r"Logs compress wide-ranging quantities onto usable scales."
    r"\begin{itemize}\item Decibels: $\text{dB} = 10\log_{10}(P/P_0)$."
    r"\item pH $= -\log_{10}[\mathrm{H}^+]$."
    r"\item $\ln$ appears in decay/growth: $N=N_0 e^{-kt}$.\end{itemize}")],
  I("A logarithm is the inverse of exponentiation.",
    "Product/quotient/power laws simplify log expressions.",
    "Logs give decibel, pH, and decay scales."),
  I("Evaluate $\\log_{10} 1000$ and $\\ln e^3$.",
    "Expand $\\log(x^2 y / z)$.",
    "Compute the dB gain for a power ratio of 100."))

M[6] = ("Mathematics: Differentiation",
  "Students are able to compute rates of change using basic differentiation.",
  I("State the meaning of a derivative.",
    "Apply the power rule.",
    "Interpret a derivative as a rate."),
  [("The Derivative",
    r"The derivative $\dfrac{dy}{dx}$ is the instantaneous rate of change ---"
    r" the slope of the curve at a point."),
   ("Basic Rules",
    r"\begin{itemize}"
    r"\item Power rule: $\dfrac{d}{dx}x^n = n x^{n-1}$."
    r"\item Constant: $\dfrac{d}{dx}c = 0$."
    r"\item Sum: differentiate term by term."
    r"\item $\dfrac{d}{dx}e^x = e^x$, $\;\dfrac{d}{dx}\ln x = 1/x$."
    r"\end{itemize}"),
   ("Interpreting Rates",
    r"If $s(t)$ is position, $s'(t)$ is velocity."
    r"\\Example: $s = 3t^2 \Rightarrow v = 6t$."
    r"\\In circuits, $i = C\,dv/dt$ links current to changing voltage.")],
  I("A derivative is an instantaneous rate of change (slope).",
    "The power rule differentiates polynomials.",
    "Derivatives model velocity, current, and other rates."),
  I("Differentiate $y = 4x^3 - 2x + 7$.",
    "Find the velocity for $s = 5t^2 + 3t$.",
    "Differentiate $y = e^x + \\ln x$."))

M[7] = ("Mathematics: Integration",
  "Students are able to compute accumulation using basic integration.",
  I("State the meaning of an integral.",
    "Apply the power rule for integration.",
    "Evaluate a definite integral."),
  [("The Integral",
    r"Integration reverses differentiation and measures accumulated area under a curve."),
   ("Basic Rules",
    r"\begin{itemize}"
    r"\item Power rule: $\displaystyle\int x^n\,dx = \frac{x^{n+1}}{n+1} + C\;(n\neq-1)$."
    r"\item $\displaystyle\int e^x\,dx = e^x + C$."
    r"\item $\displaystyle\int \frac1x\,dx = \ln|x| + C$."
    r"\end{itemize}"),
   ("Definite Integrals",
    r"$\displaystyle\int_a^b f(x)\,dx = F(b) - F(a)$."
    r"\\Example: $\displaystyle\int_0^2 3x^2\,dx = [x^3]_0^2 = 8$."
    r"\\In circuits, charge $q = \int i\,dt$ accumulates current over time.")],
  I("Integration reverses differentiation and gives area.",
    "The power rule integrates polynomials (plus constant $C$).",
    "A definite integral is $F(b)-F(a)$."),
  I("Integrate $\\int (6x^2 - 4x)\\,dx$.",
    "Evaluate $\\int_1^3 2x\\,dx$.",
    "Explain the meaning of the constant of integration."))

M[8] = ("Applied Mathematics Review",
  "Students are able to integrate all applied-mathematics concepts (Meetings 1--7).",
  I("Combine algebra, trig, logs, and calculus.",
    "Solve mixed exercises.",
    "Prepare for the midterm."),
  [("Scope (Meetings 1--7)",
    r"\begin{itemize}\item Arithmetic, scientific notation, algebra."
    r"\item Geometry and trigonometry.\item Logarithms; differentiation and integration.\end{itemize}"),
   ("Worked Mixed Problem",
    r"A signal $v(t) = 10\sin(t)$; find its rate of change and its average over $[0,\pi]$."
    r"\\$v'(t) = 10\cos(t)$; $\displaystyle\int_0^\pi 10\sin t\,dt = 20$ (before dividing by $\pi$)."
    r"\\Combines trig, differentiation, and integration."),
   ("Exam Strategy",
    r"\begin{itemize}\item State formulas before substituting."
    r"\item Keep radian/degree mode correct.\item Carry the $+C$ in indefinite integrals."
    r"\item Check units and significant figures.\end{itemize}")],
  I("Meetings 1--7 combine into mixed quantitative problems.",
    "Trig, differentiation, and integration often appear together.",
    "Mode, $+C$, and units are common pitfalls."),
  I("Differentiate and then integrate $y = 3\\sin x$.",
    "Solve a quadratic and check with the discriminant.",
    "Build a formula sheet for the midterm."))

# ---- second half: Chemistry + Materials ----
M[10] = ("Chemistry: Chemical Elements",
  "Students are able to classify chemical elements on the periodic table.",
  I("Read atomic number and mass.",
    "Describe periodic-table organization.",
    "Distinguish metals, non-metals, metalloids."),
  [("Why Elements Matter in Engineering",
    r"Every engineering material -- conductors, insulators, semiconductors, alloys -- is built"
    r" from elements. Knowing where an element sits on the periodic table predicts how it behaves."),
   ("Elements and Atomic Number",
    r"An element is a substance of one kind of atom, identified uniquely by its"
    r" \textbf{atomic number} $Z$ (number of protons in the nucleus)."
    r"\\Example: hydrogen $Z=1$, carbon $Z=6$, silicon $Z=14$."),
   ("Atomic Mass",
    r"Atomic mass $\approx$ protons + neutrons (mass number $A$)."
    r"\\Isotopes of the same element share $Z$ but differ in neutron count, hence in $A$."
    r"\\The periodic table lists the average atomic mass across natural isotopes."),
   ("Periods and Groups",
    r"\begin{itemize}"
    r"\item \textbf{Periods:} horizontal rows; atomic number increases left to right."
    r"\item \textbf{Groups:} vertical columns; elements share similar valence-electron count"
    r" and therefore similar chemical behaviour."
    r"\item Group 1 (alkali metals) and Group 17 (halogens) are classic examples of shared behaviour.\end{itemize}"),
   ("Metals vs Non-metals",
    r"\begin{center}\begin{tabular}{l|l}\hline"
    r"Metals & Non-metals\\\hline"
    r"Conductive (heat/electricity) & Generally insulating\\"
    r" Malleable, ductile & Brittle (if solid)\\"
    r" Lose electrons easily & Gain electrons easily\\"
    r" Left/centre of table & Upper right of table\\\hline"
    r"\end{tabular}\end{center}"),
   ("Metalloids",
    r"Metalloids (B, Si, Ge, As, ...) lie on the zig-zag dividing line between metals and non-metals."
    r"\begin{itemize}\item Intermediate conductivity -- neither good conductors nor good insulators."
    r"\item Silicon and germanium are the foundation of semiconductor electronics.\end{itemize}"),
   ("In-Class Practice: Instructions",
    r"Attempt each problem before checking the solution on the following slide."),
   ("Practice 1 -- Problem",
    r"Carbon has atomic number 6. State its number of protons and, for a neutral atom,"
    r" its number of electrons."),
   ("Practice 1 -- Solution",
    r"Protons $=Z=6$. A neutral atom has equal protons and electrons, so electrons $=6$."),
   ("Practice 2 -- Problem",
    r"Classify sodium (Na), sulfur (S), and silicon (Si) as metal, non-metal, or metalloid."),
   ("Practice 2 -- Solution",
    r"Na: metal (Group 1, conductive, reactive)."
    r"\\S: non-metal (Group 16, insulating)."
    r"\\Si: metalloid (Group 14, semiconductor).")],
  I("Elements are defined by atomic number $Z$; atomic mass adds neutrons.",
    "Periods and groups organize the periodic table by row and shared behaviour.",
    "Metals, non-metals, and metalloids differ in conductivity and electron behaviour."),
  I("State the atomic number and symbol of oxygen and germanium.",
    "Explain the difference between a period and a group.",
    "Why are metalloids important for electronics?"))

M[11] = ("Chemistry: Atomic \\& Molecular Structure",
  "Students are able to analyze atomic and molecular structure and bonding.",
  I("Describe the atom's structure.",
    "Explain electron shells and valence electrons.",
    "Distinguish ionic and covalent bonds."),
  [("Structure of the Atom",
    r"\begin{itemize}"
    r"\item \textbf{Nucleus:} protons ($+$) and neutrons (neutral), containing nearly all the mass."
    r"\item \textbf{Electrons ($-$):} occupy shells around the nucleus, contributing almost no mass."
    r"\item Neutral atom: number of protons = number of electrons."
    r"\end{itemize}"),
   ("Electron Shells",
    r"Electrons fill shells in order of increasing energy from the nucleus outward."
    r"\\Simple shell capacities: $2, 8, 8, \dots$ (first three shells)."
    r"\\The outermost occupied shell holds the \textbf{valence electrons}, which drive bonding."),
   ("The Octet Rule",
    r"Atoms tend to gain, lose, or share electrons to achieve 8 valence electrons"
    r" (a full outer shell), the arrangement of the noble gases."
    r"\\This stability drive explains why atoms bond at all."),
   ("Ionic Bonding",
    r"\begin{itemize}\item One atom transfers valence electron(s) to another."
    r"\item Forms oppositely charged ions that attract electrostatically."
    r"\item Typically metal + non-metal, e.g. Na (loses 1 e$^-$) + Cl (gains 1 e$^-$) $\to$ NaCl.\end{itemize}"),
   ("Covalent Bonding",
    r"\begin{itemize}\item Atoms share valence electron pairs instead of transferring them."
    r"\item Typically between non-metals, e.g. H$_2$O, CO$_2$, O$_2$."
    r"\item Shared pairs let both atoms count toward a full outer shell.\end{itemize}"),
   ("Ionic vs Covalent -- Comparison",
    r"\begin{center}\begin{tabular}{l|l}\hline"
    r"Ionic & Covalent\\\hline"
    r"electron transfer & electron sharing\\ metal + non-metal & non-metal + non-metal\\"
    r"forms crystal lattice & forms discrete molecules\\ e.g. NaCl & e.g. H$_2$O\\\hline\end{tabular}\end{center}"),
   ("In-Class Practice: Instructions",
    r"Attempt each problem before checking the solution on the following slide."),
   ("Practice 1 -- Problem",
    r"Sodium has $Z=11$. Using shell capacities $2,8,8,\dots$, find its shell structure"
    r" and its number of valence electrons."),
   ("Practice 1 -- Solution",
    r"$11 = 2+8+1$, so shells hold $2,8,1$ electrons."
    r"\\Valence electrons $=1$ (outermost shell), which is why sodium readily loses one electron."),
   ("Practice 2 -- Problem",
    r"Classify the bonding in NaCl and in H$_2$O, and explain why in each case."),
   ("Practice 2 -- Solution",
    r"NaCl: ionic -- metal Na transfers an electron to non-metal Cl."
    r"\\H$_2$O: covalent -- non-metal H and O share electron pairs.")],
  I("Atoms have a proton/neutron nucleus with electrons filling shells.",
    "Valence electrons and the octet rule drive bonding behaviour.",
    "Ionic bonds transfer electrons; covalent bonds share them."),
  I("Draw the shell structure of a chlorine atom ($Z=17$).",
    "Explain the octet rule in your own words.",
    "Classify the bonding in MgO and in CO$_2$."))

M[12] = ("Chemistry: Crystal Structure",
  "Students are able to analyze crystal structures forming solids.",
  I("Define a crystal lattice.",
    "Name common metallic structures and packing fractions.",
    "Relate structure to mechanical/electrical properties."),
  [("Crystalline vs Amorphous Solids",
    r"A crystal has atoms arranged in a repeating 3-D pattern --- the \textbf{lattice}."
    r"\\Amorphous solids (e.g. glass) lack this long-range order; their atoms are frozen in a"
    r" disordered arrangement."),
   ("The Unit Cell",
    r"The \textbf{unit cell} is the smallest repeating block that, stacked in 3-D,"
    r" reproduces the whole crystal. Its geometry defines the packing fraction --"
    r" the fraction of space occupied by atoms."),
   ("Common Metal Structures",
    r"\begin{center}\begin{tabular}{l|l|l}\hline"
    r"Structure & Packing & Example\\\hline"
    r"BCC (body-centred cubic) & 68\% & Fe (steel), Cr\\"
    r" FCC (face-centred cubic) & 74\% & Al, Cu, Ni\\"
    r" HCP (hexagonal close-packed) & 74\% & Ti, Zn, Mg\\\hline"
    r"\end{tabular}\end{center}"),
   ("Structure and Mechanical Properties",
    r"\begin{itemize}"
    r"\item Denser, more symmetric packing (FCC) $\to$ more slip systems $\to$ often more ductile."
    r"\item Grain boundaries (where crystal orientation changes) impede dislocation motion,"
    r" increasing strength (smaller grains = stronger material)."
    r"\item BCC metals like steel can be strong but less ductile at low temperature.\end{itemize}"),
   ("Crystal Structure in Electronics",
    r"Silicon's \textbf{diamond-cubic} lattice -- a highly ordered, tetrahedrally-bonded structure --"
    r" underlies semiconductor devices."
    r"\\Defects and impurities in this lattice (doping) are precisely what make transistors possible."),
   ("In-Class Practice: Instructions",
    r"Attempt each problem before checking the solution on the following slide."),
   ("Practice 1 -- Problem",
    r"Aluminium is FCC with 74\% packing. Explain why aluminium is both a good electrical"
    r" conductor and relatively ductile, in terms of its structure."),
   ("Practice 1 -- Solution",
    r"FCC's dense, symmetric packing gives many close-packed slip planes, allowing atoms to slide"
    r" past each other easily -- hence ductility."
    r"\\Metallic bonding (delocalized electrons) independently gives good conductivity;"
    r" the FCC lattice does not hinder electron flow."),
   ("Practice 2 -- Problem",
    r"Explain, in one or two sentences, why a crystalline solid has a sharp melting point"
    r" while an amorphous solid (like glass) softens gradually over a range of temperatures."),
   ("Practice 2 -- Solution",
    r"In a crystal, every atom sits in an identical, repeating bonding environment, so all bonds"
    r" break at essentially the same temperature -- a sharp melting point."
    r"\\In an amorphous solid, bonding environments vary throughout the material, so bonds break"
    r" progressively over a range of temperatures.")],
  I("Crystals have a repeating lattice; amorphous solids do not.",
    "BCC, FCC, and HCP are common metal structures with different packing fractions.",
    "Structure influences ductility, strength, and semiconductor behaviour."),
  I("Define a crystal lattice and unit cell.",
    "Give the packing fraction and an example for BCC.",
    "Explain how FCC structure relates to ductility."))

M[13] = ("Chemistry: Colloids",
  "Students are able to distinguish colloids among mixture types.",
  I("Classify mixtures by particle size.",
    "Define a colloid and its dispersed/continuous phases.",
    "Describe the Tyndall effect and colloid stability."),
  [("Why Mixture Classification Matters",
    r"Engineering materials and fluids (paints, lubricants, composites, fuel emulsions) are often"
    r" colloids, not true solutions -- their stability and behaviour depend on particle size."),
   ("Types of Mixtures by Particle Size",
    r"\begin{center}\begin{tabular}{l|l|l}\hline"
    r"Type & Particle size & Settles?\\\hline"
    r"Solution & $<1$ nm & no\\ Colloid & 1--1000 nm & no (stable suspension)\\"
    r" Suspension & $>1000$ nm & yes (settles over time)\\\hline"
    r"\end{tabular}\end{center}"),
   ("What Is a Colloid",
    r"A colloid has one substance (the \textbf{dispersed phase}) spread through another"
    r" (the \textbf{continuous phase}) without dissolving."
    r"\begin{itemize}\item Examples: milk (fat in water), fog (water in air), gels, paints."
    r"\item Particles are too small to settle under gravity but too large to dissolve.\end{itemize}"),
   ("Types of Colloids",
    r"\begin{center}\begin{tabular}{l|l|l}\hline"
    r"Dispersed & Continuous & Example\\\hline"
    r"Liquid & Gas & Fog (aerosol)\\ Solid & Liquid & Paint (sol)\\"
    r" Liquid & Liquid & Milk (emulsion)\\ Gas & Liquid & Foam\\\hline"
    r"\end{tabular}\end{center}"),
   ("The Tyndall Effect",
    r"Colloidal particles are large enough to scatter a beam of light, making the beam visible"
    r" as it passes through -- the \textbf{Tyndall effect}."
    r"\\True solutions do not scatter light (the beam is invisible passing through)."
    r" This is the simplest experimental test to distinguish a colloid from a solution."),
   ("Colloid Stability",
    r"\begin{itemize}\item Colloidal particles often carry like electric charges, repelling each"
    r" other and preventing clumping (coagulation)."
    r"\item Heating, adding electrolytes, or removing the stabilizing charge can destabilize a"
    r" colloid, causing particles to aggregate and settle.\end{itemize}"),
   ("In-Class Practice: Instructions",
    r"Attempt each problem before checking the solution on the following slide."),
   ("Practice 1 -- Problem",
    r"Classify milk, salt water, and muddy (river) water as a solution, colloid, or suspension,"
    r" and justify each using particle size and settling behaviour."),
   ("Practice 1 -- Solution",
    r"Salt water: solution (ions $<1$ nm, never settles)."
    r"\\Milk: colloid (fat droplets 1--1000 nm, does not settle, shows Tyndall effect)."
    r"\\Muddy water: suspension (particles $>1000$ nm, settles when left standing)."),
   ("Practice 2 -- Problem",
    r"You shine a laser pointer through two clear liquids. In liquid A the beam is invisible;"
    r" in liquid B the beam path is clearly visible. Which is more likely a colloid, and why?"),
   ("Practice 2 -- Solution",
    r"Liquid B is more likely a colloid -- the visible beam path is the Tyndall effect, caused"
    r" by light scattering off particles in the 1--1000 nm range. Liquid A is likely a true"
    r" solution, since light passes through without scattering.")],
  I("Mixtures are solutions, colloids, or suspensions by particle size and settling behaviour.",
    "A colloid has a dispersed phase spread through a continuous phase without dissolving.",
    "The Tyndall effect (light scattering) identifies colloids and distinguishes them from solutions."),
  I("Classify fog, sugar water, and sand-in-water.",
    "Name the dispersed and continuous phase of a foam.",
    "Explain why the Tyndall effect does not occur in a true solution."))

M[14] = ("Chemistry: Solutions \\& Solvents",
  "Students are able to characterize solutions, solvents, and concentration.",
  I("Define solute, solvent, solution.",
    "Compute concentration by molarity and mass percent.",
    "Explain the factors governing solubility."),
  [("Solution Basics",
    r"\begin{itemize}"
    r"\item \textbf{Solute:} the substance being dissolved (present in smaller amount)."
    r"\item \textbf{Solvent:} the substance doing the dissolving (often water; present in larger amount)."
    r"\item \textbf{Solution:} a homogeneous (uniform) mixture of solute and solvent.\end{itemize}"),
   ("Molarity",
    r"Molarity $M = \dfrac{\text{moles of solute}}{\text{litres of solution}}$, units mol/L."
    r"\\Example: dissolving 0.5 mol of solute in 2 L of solution gives $M = 0.5/2 = 0.25$ mol/L."),
   ("Mass Percent Concentration",
    r"Mass percent $= \dfrac{\text{mass of solute}}{\text{mass of solution}}\times100\%$."
    r"\\Example: 10 g salt dissolved to make 200 g solution total gives"
    r" $10/200\times100\% = 5\%$ by mass."),
   ("Dilution",
    r"Adding solvent lowers concentration while moles of solute stay fixed:"
    r"\\$M_1V_1 = M_2V_2$."
    r"\\Example: diluting 1 L of 2 M solution to 4 L gives $M_2 = (2)(1)/4 = 0.5$ M."),
   ("Solubility Factors",
    r"\begin{itemize}\item \textbf{Temperature:} usually raises solubility of solids in liquids,"
    r" but lowers solubility of gases in liquids."
    r"\item \textbf{Pressure:} strongly affects gas solubility (higher pressure, more gas dissolves)."
    r"\item \textbf{Polarity:} ``like dissolves like'' -- polar solvents (water) dissolve polar/ionic"
    r" solutes; non-polar solvents dissolve non-polar solutes.\end{itemize}"),
   ("Saturation",
    r"A solution is \textbf{saturated} when it holds the maximum solute that can dissolve at that"
    r" temperature; adding more solute leaves undissolved solid at the bottom."
    r" A supersaturated solution holds more than the saturation point but is unstable."),
   ("In-Class Practice: Instructions",
    r"Attempt each problem before checking the solution on the following slide."),
   ("Practice 1 -- Problem",
    r"Compute the molarity of a solution containing 1.5 mol of solute in 3 L of solution."),
   ("Practice 1 -- Solution",
    r"$M = 1.5\text{ mol}/3\text{ L} = 0.5$ mol/L."),
   ("Practice 2 -- Problem",
    r"A solution is made from 25 g of sugar dissolved to make 500 g of solution total."
    r" Find the mass percent concentration."),
   ("Practice 2 -- Solution",
    r"Mass percent $=25/500\times100\% = 5\%$."),
   ("Practice 3 -- Problem",
    r"You have 2 L of a 3 M solution. How much water must be added to dilute it to 1 M"
    r" (assume volumes add directly)?"),
   ("Practice 3 -- Solution",
    r"$M_1V_1=M_2V_2 \Rightarrow (3)(2)=(1)V_2 \Rightarrow V_2=6$ L total."
    r"\\Water to add $=6-2=4$ L.")],
  I("A solution is solute dissolved uniformly in solvent.",
    "Molarity and mass percent quantify concentration; dilution follows $M_1V_1=M_2V_2$.",
    "Temperature, pressure, and polarity govern solubility."),
  I("Compute the molarity of 0.8 mol in 4 L.",
    "Identify solute and solvent in seawater.",
    "Dilute 500 mL of 4 M solution to 2 M -- find the final volume."))

M[15] = ("Materials: Hardness \\& Ductility",
  "Students are able to evaluate mechanical properties of engineering materials.",
  I("Define hardness, ductility, and brittleness.",
    "Describe standard test methods for each property.",
    "Relate mechanical properties to material choice in avionics."),
  [("Why Mechanical Properties Matter",
    r"Choosing the right material for an aircraft part means balancing strength, weight,"
    r" and how the material responds to indentation, bending, and stretching."),
   ("Hardness",
    r"\textbf{Hardness:} a material's resistance to localized surface indentation or scratching."
    r"\\Harder materials resist wear better but are often more brittle."),
   ("Ductility and Brittleness",
    r"\begin{itemize}\item \textbf{Ductility:} ability to deform plastically (permanently) before"
    r" fracturing -- can be drawn into wire without breaking."
    r"\item \textbf{Brittleness:} fractures with little or no plastic deformation -- the opposite"
    r" of ductility.\item \textbf{Malleability:} similar to ductility but for rolling/hammering"
    r" into sheets.\end{itemize}"),
   ("Hardness Testing Methods",
    r"\begin{center}\begin{tabular}{l|l}\hline"
    r"Test & Principle\\\hline"
    r"Brinell & steel/carbide ball indenter, measure indent diameter\\"
    r" Rockwell & indenter depth under load, direct dial reading\\"
    r" Vickers & diamond pyramid indenter, precise for thin/hard samples\\\hline"
    r"\end{tabular}\end{center}"),
   ("Ductility Testing: The Tensile Test",
    r"A sample is pulled until it fractures, while stress and strain are recorded."
    r"\begin{itemize}\item \textbf{\% elongation} = increase in length / original length $\times100\%$,"
    r" a direct measure of ductility."
    r"\item The stress-strain curve also reveals yield strength and ultimate strength.\end{itemize}"),
   ("Material Selection Trade-offs",
    r"\begin{itemize}"
    r"\item Aircraft skin: light, ductile alloys (aluminium) that can absorb impact without cracking."
    r"\item Cutting tools, bearings: hard materials (hardened steel, carbide) that resist wear."
    r"\item General trade-off: increasing hardness (e.g. by heat treatment) usually reduces ductility.\end{itemize}"),
   ("In-Class Practice: Instructions",
    r"Attempt each problem before checking the solution on the following slide."),
   ("Practice 1 -- Problem",
    r"A metal sample 100 mm long is stretched to 108 mm before it fractures."
    r" Compute its \% elongation and comment on its ductility."),
   ("Practice 1 -- Solution",
    r"\% elongation $= (108-100)/100\times100\% = 8\%$."
    r"\\An 8\% elongation indicates a reasonably ductile material (brittle materials typically"
    r" show well under 5\% elongation)."),
   ("Practice 2 -- Problem",
    r"An aircraft designer must choose between a hard, brittle alloy and a softer, ductile alloy"
    r" for the outer skin panel. Which is generally preferred, and why?"),
   ("Practice 2 -- Solution",
    r"The ductile alloy is generally preferred for skin panels -- it can absorb impact energy"
    r" and deform rather than crack under stress, and it is easier to form into curved panels"
    r" during manufacturing.")],
  I("Hardness resists indentation; ductility allows plastic deformation before fracture.",
    "Brinell/Rockwell/Vickers test hardness; the tensile test gives \\% elongation for ductility.",
    "Material selection trades hardness against ductility for the application."),
  I("Define hardness and brittleness.",
    "Name two hardness tests and one ductility test.",
    "Explain why cutting tools use hard materials rather than ductile ones."))

M[16] = ("Chemistry \\& Materials Review",
  "Students are able to integrate chemistry and materials concepts (Meetings 10--15).",
  I("Combine structure, bonding, and properties.",
    "Solve integrated exercises across all Meeting 10--15 topics.",
    "Relate chemistry to material selection."),
  [("Scope (Meetings 10--15)",
    r"\begin{itemize}\item M10: Elements, atomic number, periodic table organization."
    r"\item M11: Atomic/molecular structure, ionic vs covalent bonding."
    r"\item M12: Crystal structure (BCC/FCC/HCP), structure-property links."
    r"\item M13: Colloids and mixture classification, Tyndall effect."
    r"\item M14: Solutions, molarity, mass percent, dilution."
    r"\item M15: Hardness, ductility, and material selection.\end{itemize}"),
   ("Integration Example: Aluminium",
    r"Metallic bonding (delocalized electrons, from M11) and FCC packing (74\%, from M12) together"
    r" explain why aluminium is both a good electrical conductor and ductile enough to form"
    r" aircraft skin panels (M15) -- linking bonding, crystal structure, and mechanical"
    r" properties to a real material choice."),
   ("Integration Example: Silicon",
    r"Silicon is a metalloid (M10) with a diamond-cubic crystal lattice (M12), whose atomic"
    r" bonding (M11, covalent) gives it intermediate conductivity -- the basis of semiconductor"
    r" electronics."),
   ("Exam Strategy",
    r"\begin{itemize}\item Connect structure $\to$ bonding $\to$ property $\to$ application in every answer."
    r"\item Show concentration calculations step by step with units labelled."
    r"\item Use correct units throughout (mol, mol/L, \%).\end{itemize}"),
   ("In-Class Practice: Instructions",
    r"These integrated problems combine two or more topics from Meetings 10--15."),
   ("Practice 1 -- Problem",
    r"Classify the bonding in NaCl (M11), then explain how this bonding leads to NaCl forming"
    r" an ordered crystal lattice (M12) rather than an amorphous solid."),
   ("Practice 1 -- Solution",
    r"NaCl bonding is ionic (Na transfers an electron to Cl, forming Na$^+$ and Cl$^-$)."
    r"\\The electrostatic attraction between oppositely-charged ions is strongest when each ion"
    r" is surrounded by an ordered arrangement of opposite-charge neighbours -- this drives the"
    r" formation of a regular, repeating crystal lattice rather than a disordered solid."),
   ("Practice 2 -- Problem",
    r"A 250 mL colloidal suspension is prepared by dispersing 5 g of solid in water."
    r" (a) Compute its mass percent concentration (assume solution mass $\approx$ 250 g)."
    r" (b) Would you expect this mixture to show the Tyndall effect? Why?"),
   ("Practice 2 -- Solution",
    r"(a) Mass percent $= 5/250\times100\% = 2\%$."
    r"\\(b) Yes -- as a colloid (particles 1--1000 nm), it scatters light and shows the"
    r" Tyndall effect, unlike a true solution.")],
  I("Meetings 10--15 link elements, bonding, crystal structure, mixtures, and mechanical properties.",
    "Real material choices (aluminium, silicon) tie the concepts together.",
    "Clear units and structure-property reasoning matter for exam answers."),
  I("Explain aluminium's conductivity and ductility from its structure.",
    "Compute a molarity and a mass percent for a chosen solution.",
    "Relate crystal structure to a mechanical property for a metal of your choice."))

M[17] = ("Integrated Review (Pre-Final)",
  "Students are able to integrate all Natural Science 1 concepts (Meetings 10--16) for the final exam.",
  I("Combine mathematics and chemistry as needed.",
    "Solve integrated post-midterm exercises.",
    "Confirm readiness for the final."),
  [("Final Scope",
    r"Emphasis on Meetings 10--16 (chemistry and materials): elements, atomic/molecular"
    r" structure, bonding, crystal structure, colloids, solutions, and mechanical properties --"
    r" with applied mathematics (M1--M8) as a supporting tool for calculations."),
   ("Recap: Bonding \\& Structure",
    r"\begin{itemize}\item Ionic bonding (electron transfer) vs covalent bonding (electron sharing)."
    r"\item Crystal lattices (BCC/FCC/HCP) explain density, ductility, and semiconductor behaviour."
    r"\end{itemize}"),
   ("Recap: Mixtures \\& Solutions",
    r"\begin{itemize}\item Solutions, colloids, suspensions differ by particle size and settling."
    r"\item Molarity $M=\text{mol}/\text{L}$, mass percent, and dilution $M_1V_1=M_2V_2$."
    r"\end{itemize}"),
   ("Recap: Mechanical Properties",
    r"\begin{itemize}\item Hardness (Brinell/Rockwell/Vickers) vs ductility (tensile test, \% elongation)."
    r"\item Material selection always trades one property against another.\end{itemize}"),
   ("Integration Example",
    r"Compute the concentration of a prepared solution (algebra + units), then"
    r" reason about how solute structure (bonding, polarity) affects solubility --- combining"
    r" quantitative math with chemical understanding."),
   ("Final Exam Strategy",
    r"\begin{itemize}\item Read each question for the concept being tested before calculating."
    r"\item Show quantitative work step by step -- partial credit rewards visible reasoning."
    r"\item Keep chemical units consistent (mol, mol/L, \%, nm)."
    r"\item Manage time across mixed math and chemistry questions.\end{itemize}"),
   ("In-Class Practice: Instructions",
    r"These integrated problems mirror the mixed style of the final exam."),
   ("Practice 1 -- Problem",
    r"A 4 M stock solution is diluted from 500 mL to 2 L. (a) Find the new molarity."
    r" (b) Is the resulting solution more likely to remain a true solution or form a colloid,"
    r" if the solute is a small dissolved ion (e.g. Na$^+$)?"),
   ("Practice 1 -- Solution",
    r"(a) $M_1V_1=M_2V_2 \Rightarrow (4)(0.5)=M_2(2) \Rightarrow M_2=1$ M."
    r"\\(b) A true solution -- dissolved ions are $<1$ nm, far smaller than the 1--1000 nm"
    r" colloidal range, so it never forms a colloid regardless of dilution."),
   ("Practice 2 -- Problem",
    r"Two unknown metal samples are tested: Sample X has FCC structure and high \% elongation."
    r" Sample Y has a disordered (amorphous) structure and shatters under stress."
    r" Which sample would you choose for an aircraft skin panel, and why?"),
   ("Practice 2 -- Solution",
    r"Sample X -- FCC structure with high \% elongation indicates good ductility, meaning it"
    r" can absorb impact energy by deforming rather than fracturing, which is essential for"
    r" a structural skin panel. Sample Y's brittleness makes it unsuitable.")],
  I("The final emphasizes chemistry/materials with supporting math.",
    "Quantitative and conceptual reasoning combine across all post-midterm topics.",
    "Consistent units and shown work are essential."),
  I("Prepare a solution of target molarity and show the calculation.",
    "Explain a solubility trend using bonding/structure.",
    "Build a combined formula/concept sheet for the final."))

if __name__ == "__main__":
    order = [1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17]
    for n in order:
        title, subclo, ind, slides, summ, asg = M[n]
        tex = build_deck(COURSE, SUBJECT, SUBTITLE, REF, CLO, n, title, subclo, ind, slides, summ, asg)
        print(compile_meeting(COURSE, n, tex), flush=True)
    print("DONE", COURSE)
