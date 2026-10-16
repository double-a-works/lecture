#!/usr/bin/env python3
"""Digital_Technic_Micro (§14) — meetings 1-8,10-17."""
from build_slides import build_deck, compile_meeting

COURSE   = "Digital_Technic_Micro"
SUBJECT  = "DIGITAL TECHNIC -- MICROPROCESSOR SYSTEMS"
SUBTITLE = "Microprocessor Systems"
REF      = "Digital Design and Computer Architecture. ARM Edition by Sarah Harris, David Harris"
CLO = [
 "Explain the basic architecture of a microcomputer and the function of its units (CPU, ALU, registers).",
 "Analyze the system bus and the fetch--execute cycle.",
 "Classify memory devices (RAM, ROM) and analyze memory organization and addressing.",
 "Classify integrated circuits and logic families (TTL/CMOS) and read datasheets.",
 "Explain display devices (LED, seven-segment, LCD) and their interfacing with a microcomputer.",
]
I = lambda *xs: list(xs)
M = {}

M[1] = ("Basic Microcomputer: General Architecture",
  "Students are able to explain the basic architecture of a microcomputer and the function of its units.",
  I("Identify CPU, memory, and I/O.",
    "Describe how buses connect the units.",
    "Relate the model to embedded avionics."),
  [("Why Study Microcomputer Architecture?",
    r"""Every modern avionics Line Replaceable Unit (LRU) -- flight management computers,
    autopilots, engine indicators -- is built around a microcomputer core.
    \begin{itemize}
    \item Understanding the architecture is essential for troubleshooting, maintenance, and
    safe handling of avionics equipment.
    \item This meeting builds the mental model: what a microcomputer is made of, and how the pieces
    communicate.
    \end{itemize}"""),
   ("What Is a Microcomputer?",
    r"""A microcomputer integrates a \textbf{microprocessor (CPU)}, \textbf{memory}, and
    \textbf{I/O} on a system connected by buses.
    \begin{itemize}
    \item CPU: executes instructions.
    \item Memory: stores the program and the data it works on.
    \item I/O: interfaces to the outside world.
    \end{itemize}"""),
   ("Core Building Blocks",
    r"""\begin{itemize}
    \item \textbf{CPU:} fetches, decodes, and executes instructions.
    \item \textbf{Memory:} stores the program (instructions) and the data the program works on.
    \item \textbf{I/O:} the interface to sensors, switches, displays, and other systems.
    \end{itemize}
    Each block on its own cannot compute -- the system works only because they are connected
    and coordinated by buses."""),
   ("The System Bus (Preview)",
    r"""\begin{itemize}
    \item \textbf{Address bus:} carries the memory/I-O location the CPU wants to access.
    \item \textbf{Data bus:} carries the actual value being read or written.
    \item \textbf{Control bus:} carries timing and command signals (read/write, clock, interrupts).
    \end{itemize}
    We study the bus and the fetch--execute cycle in full detail next meeting."""),
   ("Putting It Together: Block Diagram",
    r"""\begin{center}\begin{tikzpicture}[node distance=1cm,
    block/.style={rectangle,draw,rounded corners,minimum width=2.6cm,minimum height=0.8cm,align=center,fill=blue!10}]
    \node[block](cpu){CPU};\node[block,right=of cpu](mem){Memory};\node[block,below=of cpu](io){I/O};
    \draw[<->,thick](cpu)--(mem);\draw[<->,thick](cpu)--(io);\end{tikzpicture}\end{center}
    All units share the system bus -- address, data, and control lines run to every block."""),
   ("Von Neumann vs Harvard Architecture",
    r"""\begin{itemize}
    \item \textbf{Von Neumann:} one shared memory and bus for both instructions and data --
    simpler, used in most general-purpose microcomputers.
    \item \textbf{Harvard:} separate memory and buses for instructions and data --
    common in DSPs and many microcontrollers.
    \item Trade-off: Von Neumann is simpler and cheaper; Harvard allows simultaneous
    instruction fetch and data access, which is faster.
    \end{itemize}"""),
   ("Microcomputer vs Microprocessor vs Microcontroller",
    r"""\begin{itemize}
    \item \textbf{Microprocessor:} the CPU chip alone (e.g. Intel 8085, an ARM core).
    \item \textbf{Microcontroller:} CPU + memory + I/O on one chip (e.g. AVR, PIC) --
    common in embedded sensors.
    \item \textbf{Microcomputer:} a complete computing system built around a CPU, with
    external memory/I-O boards.
    \end{itemize}"""),
   ("Microcomputers in Avionics LRUs",
    r"""\begin{itemize}
    \item Flight Management Computer (FMS) -- navigation and performance calculations.
    \item Engine Indicating and Crew Alerting System (EICAS) -- data acquisition and display.
    \item Autopilot / Flight Control Computer -- sensor input, control-law computation, actuator output.
    \end{itemize}
    Each of these is, internally, a microcomputer following the CPU--memory--I-O model from
    this lecture."""),
   ("Typical I/O Devices",
    r"""\begin{itemize}
    \item \textbf{Inputs:} switches, sensors (temperature, pressure, position), keypads.
    \item \textbf{Outputs:} displays, indicator lamps, actuators, audio warnings.
    \item I/O devices connect through interface circuits (buffers, ADC/DAC, drivers) --
    not directly to the CPU pins.
    \end{itemize}"""),
   ("Common Pitfalls \\& Tips",
    r"""\begin{itemize}
    \item Confusing a microprocessor (a chip) with a microcomputer (a full system).
    \item Assuming a microcontroller needs external memory -- it usually has memory built in.
    \item Forgetting that I/O needs interface circuitry, not a direct wire to the CPU.
    \end{itemize}"""),
   ("In-Class Discussion",
    r"""\begin{enumerate}
    \item Identify the CPU, memory, and I/O in a smartphone.
    \item Would an autopilot computer more likely use Von Neumann or Harvard architecture? Why?
    \item Name one avionics LRU and describe what its I/O devices might be.
    \end{enumerate}""")],
  I("A microcomputer combines CPU, memory, and I/O over buses.",
    "The CPU executes; memory stores; I/O connects to the world.",
    "Microprocessor, microcontroller, and microcomputer differ in integration."),
  I("Draw the block diagram of a microcomputer.",
    "Distinguish a microprocessor from a microcontroller.",
    "Give an avionics example of an embedded microcomputer.",
    "Explain one advantage of Harvard architecture over Von Neumann."))

M[2] = ("CPU, ALU \\& Registers",
  "Students are able to explain the internal units of a CPU.",
  I("Describe the control unit and ALU.",
    "Explain the role of registers.",
    "Name key special registers (PC, IR, ACC)."),
  [("Inside the CPU",
    r"""\begin{itemize}
    \item \textbf{Control Unit (CU):} decodes instructions and sequences operations.
    \item \textbf{ALU:} performs arithmetic and logic.
    \item \textbf{Registers:} fast on-chip storage.
    \end{itemize}"""),
   ("The Control Unit in Detail",
    r"""\begin{itemize}
    \item Fetches the next instruction from memory (address given by the PC).
    \item Decodes the instruction to determine which operation and operands are involved.
    \item Generates the control/timing signals that drive the ALU, registers, and buses to
    execute the instruction.
    \end{itemize}
    The control unit does not compute values itself -- it \textit{orchestrates} the other units."""),
   ("The ALU",
    r"""The Arithmetic Logic Unit computes on operands from registers.
    \begin{itemize}
    \item Arithmetic: add, subtract.
    \item Logic: AND, OR, NOT, XOR.
    \item Sets status flags: zero, carry, sign, overflow.
    \end{itemize}"""),
   ("ALU Worked Example: Binary Addition",
    r"""Add $5_{10}+3_{10}$ using 4-bit registers:
    \[ \begin{array}{r} 0101\\ +\,0011\\\hline 1000\end{array} \]
    Result: $1000_2 = 8_{10}$. No carry out of bit 3, so Carry $=0$, Zero $=0$, Sign $=0$
    (unsigned interpretation)."""),
   ("Status Flags in Detail",
    r"""\begin{itemize}
    \item \textbf{Zero (Z):} set when the ALU result is exactly 0.
    \item \textbf{Carry (C):} set when addition produces a carry out of the most significant bit
    (or a borrow in subtraction).
    \item \textbf{Sign (S):} copies the most significant bit of the result (1 = negative, signed).
    \item \textbf{Overflow (V):} set when a signed result exceeds the representable range.
    \end{itemize}
    Flags let the control unit make decisions -- conditional branches test flag values."""),
   ("Key Registers",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Register & Role\\\hline
    PC & address of next instruction\\ IR & holds the current instruction\\
    ACC & accumulator (ALU result)\\ SP & stack pointer\\
    MAR & memory address register (address about to be accessed)\\
    MDR & memory data register (data being transferred)\\
    Flags & status bits (Z, C, S, V)\\\hline
    \end{tabular}\end{center}"""),
   ("General-Purpose vs Special-Purpose Registers",
    r"""\begin{itemize}
    \item \textbf{Special-purpose registers} (PC, IR, SP, Flags) each have one fixed job in the
    fetch--execute cycle.
    \item \textbf{General-purpose registers} hold temporary data/operands for the programmer
    or compiler to use freely.
    \item More general-purpose registers usually means less traffic to slower main memory --
    a key performance factor.
    \end{itemize}"""),
   ("Register Width and Word Size",
    r"""\begin{itemize}
    \item An 8-bit register stores $0$--$255$ (unsigned) or $-128$ to $127$ (signed).
    \item A 16-bit register stores $0$--$65{,}535$ (unsigned).
    \item Word size affects the range of numbers, the size of addresses, and how much memory
    a CPU can directly access.
    \end{itemize}"""),
   ("Walkthrough: Executing One Add Instruction",
    r"""\begin{enumerate}
    \item \textbf{Fetch:} PC points to the instruction; the CU loads it into IR; PC increments.
    \item \textbf{Decode:} the CU recognizes an ADD operation and identifies the operand registers.
    \item \textbf{Execute:} the ALU adds the operands; the result goes to ACC; flags update.
    \end{enumerate}
    This fetch--decode--execute pattern is the heartbeat of every microcomputer -- the full
    cycle is the topic of the next meeting."""),
   ("Common Pitfalls \\& Tips",
    r"""\begin{itemize}
    \item Confusing the accumulator (holds a value) with the program counter (holds an address).
    \item Forgetting that flags reflect the \textit{last} ALU operation, not a running total.
    \item Assuming overflow and carry are the same thing -- they answer different questions
    (signed vs unsigned).
    \end{itemize}"""),
   ("In-Class Practice",
    r"""\begin{enumerate}
    \item Add $9_{10}$ and $7_{10}$ using 4-bit registers. Does the Carry flag set? Why?
    \item Explain, in one sentence, what each of PC, IR, and ACC does.
    \item Why might a CPU need both general-purpose and special-purpose registers?
    \end{enumerate}""")],
  I("The CPU contains a control unit, ALU, and registers.",
    "The ALU does arithmetic/logic and sets flags.",
    "PC, IR, ACC, SP, and flags are core registers."),
  I("List three ALU operations and the flags they can set.",
    "State the role of the program counter.",
    "Explain why registers are faster than RAM.",
    "Trace PC, IR, and ACC through one ADD instruction."))

M[3] = ("System Bus \\& Fetch--Execute Cycle",
  "Students are able to analyze the system bus and the fetch--execute cycle.",
  I("Describe data, address, and control buses.",
    "Trace the fetch--execute cycle.",
    "Relate bus width to capability."),
  [("The System Bus",
    r"\begin{itemize}"
    r"\item \textbf{Data bus:} carries instructions/data (width = word size)."
    r"\item \textbf{Address bus:} selects a location; n lines address $2^n$ cells."
    r"\item \textbf{Control bus:} read/write, clock, interrupt signals."
    r"\end{itemize}"),
   ("Fetch--Execute Cycle",
    r"\begin{enumerate}"
    r"\item PC $\to$ address bus; read instruction into IR."
    r"\item CU decodes the instruction."
    r"\item ALU/registers execute it; PC advances."
    r"\end{enumerate}"
    r"The cycle repeats continuously."),
   ("Bus Width Matters",
    r"\begin{center}\begin{tabular}{c|c}\hline"
    r"Address lines & Addressable memory\\\hline"
    r"16 & 64 KB\\ 20 & 1 MB\\ 32 & 4 GB\\\hline\end{tabular}\end{center}"
    r"Wider address bus $\Rightarrow$ more addressable memory.")],
  I("Data, address, and control buses form the system bus.",
    "Fetch-decode-execute repeats for each instruction.",
    "n address lines address $2^n$ locations."),
  I("How much memory can a 24-bit address bus reach?",
    "List the three steps of the fetch-execute cycle.",
    "State the function of the control bus."))

M[4] = ("Lab: Microcomputer Architecture Simulation",
  "Students are able to simulate and observe basic microcomputer architecture behaviour.",
  I("Load a simple program into a simulator.",
    "Observe register and bus activity.",
    "Trace instruction execution."),
  [("Simulation Goals",
    r"Using a CPU simulator, students observe how instructions move data through"
    r" registers, the ALU, and memory over the system bus."),
   ("Simple Program",
    r"A short routine to add two numbers:"
    r"\begin{itemize}\item LOAD A --- fetch operand into ACC."
    r"\item ADD B --- ALU adds; result in ACC.\item STORE C --- write result to memory.\end{itemize}"
    r"Watch PC, IR, and ACC change each step."),
   ("What to Record",
    r"\begin{itemize}"
    r"\item PC value before/after each instruction."
    r"\item ACC and flag changes."
    r"\item Address/data bus contents during fetch and execute."
    r"\end{itemize}"
    r"Compare observed behaviour with the fetch-execute theory.")],
  I("A simulator makes the fetch-execute cycle observable.",
    "LOAD/ADD/STORE traces data through registers and the ALU.",
    "Recording PC, ACC, and bus activity confirms the theory."),
  I("Write a 3-instruction program to compute $C=A+B$.",
    "Record the PC and ACC after each step.",
    "Explain what appears on the address bus during a fetch."))

M[5] = ("Memory Devices: Classification (RAM/ROM)",
  "Students are able to classify memory devices (RAM and ROM).",
  I("Distinguish volatile and non-volatile memory.",
    "Define RAM and ROM.",
    "Place memory types in a hierarchy."),
  [("Volatile vs Non-Volatile",
    r"\begin{itemize}"
    r"\item \textbf{Volatile:} loses contents without power (RAM)."
    r"\item \textbf{Non-volatile:} retains contents without power (ROM, Flash)."
    r"\end{itemize}"),
   ("RAM and ROM",
    r"\begin{center}\begin{tabular}{l|l|l}\hline"
    r" & RAM & ROM\\\hline"
    r"Volatile & yes & no\\ Writable & yes & limited/no\\ Use & working data & firmware\\\hline"
    r"\end{tabular}\end{center}"),
   ("Memory Hierarchy",
    r"Fastest/smallest at top, slowest/largest at bottom:"
    r"\begin{itemize}\item Registers\item Cache\item Main memory (RAM)"
    r"\item Non-volatile storage (ROM/Flash/disk)\end{itemize}")],
  I("Memory is volatile (RAM) or non-volatile (ROM/Flash).",
    "RAM holds working data; ROM holds firmware.",
    "The hierarchy trades speed for capacity."),
  I("Classify RAM and ROM by volatility and writability.",
    "Order the memory hierarchy from fastest to slowest.",
    "Give one avionics use of non-volatile memory."))

M[6] = ("RAM \\& ROM Types and Characteristics",
  "Students are able to identify RAM/ROM subtypes and their characteristics.",
  I("Distinguish SRAM and DRAM.",
    "Distinguish PROM, EPROM, EEPROM, Flash.",
    "Match a type to an application."),
  [("SRAM vs DRAM",
    r"\begin{center}\begin{tabular}{l|l|l}\hline"
    r" & SRAM & DRAM\\\hline"
    r"Cell & flip-flop & capacitor\\ Refresh & no & yes\\ Speed & fast & slower\\"
    r"Density & low & high\\ Use & cache & main memory\\\hline\end{tabular}\end{center}"),
   ("ROM Family",
    r"\begin{itemize}"
    r"\item \textbf{PROM:} programmed once."
    r"\item \textbf{EPROM:} erased by UV light."
    r"\item \textbf{EEPROM:} electrically erasable, byte-wise."
    r"\item \textbf{Flash:} electrically erasable in blocks; dominant today."
    r"\end{itemize}"),
   ("Choosing Memory",
    r"\begin{itemize}"
    r"\item Fast scratch working data $\to$ SRAM/DRAM."
    r"\item Firmware that rarely changes $\to$ Flash/EEPROM."
    r"\item One-time calibration constants $\to$ PROM/OTP."
    r"\end{itemize}")],
  I("SRAM uses flip-flops (fast); DRAM uses capacitors (dense, needs refresh).",
    "PROM/EPROM/EEPROM/Flash differ in erase method.",
    "Application drives memory choice."),
  I("Give two differences between SRAM and DRAM.",
    "Order PROM, EPROM, EEPROM, Flash by erase flexibility.",
    "Which memory stores boot firmware, and why?"))

M[7] = ("Memory Organization \\& Addressing (Memory Map)",
  "Students are able to analyze memory organization, addressing, and memory maps.",
  I("Compute address range from address lines.",
    "Read a memory map.",
    "Explain address decoding."),
  [("Addressing Basics",
    r"An $m$-line address bus with $b$-bit words gives $2^m$ locations of $b$ bits each."
    r"\\Total capacity $= 2^m \times b$ bits."
    r"\\Example: 16 lines, 8-bit words $= 64$ K $\times$ 8 = 64 KB."),
   ("Memory Map",
    r"A memory map assigns address ranges to devices."
    r"\begin{center}\begin{tabular}{l|l}\hline"
    r"Range & Device\\\hline"
    r"0000--3FFF & ROM (firmware)\\ 4000--7FFF & RAM\\ 8000--BFFF & I/O ports\\\hline"
    r"\end{tabular}\end{center}"),
   ("Address Decoding",
    r"Decoding logic activates the correct chip for a given address range,"
    r" using the high address bits as chip-select. This prevents two devices"
    r" responding to the same address.")],
  I("Capacity = $2^m$ locations times word width.",
    "A memory map partitions the address space among devices.",
    "Address decoding selects one device per address."),
  I("Compute the capacity for 18 address lines and 16-bit words.",
    "Read the given memory map and identify the RAM range.",
    "Explain the purpose of chip-select logic."))

M[8] = ("Integrated Review (Pre-Midterm)",
  "Students are able to integrate microcomputer architecture and memory (Meetings 1--7).",
  I("Combine architecture and memory concepts.",
    "Solve integrated exercises.",
    "Prepare for the midterm."),
  [("Midterm Scope (Meetings 1--7)",
    r"\begin{itemize}\item Microcomputer architecture; CPU/ALU/registers."
    r"\item System bus and fetch-execute cycle.\item Memory classification, types, and addressing.\end{itemize}"),
   ("Integration Example",
    r"Trace a LOAD instruction: PC drives the address bus, ROM returns the opcode"
    r" on the data bus, the CU decodes it, and the ALU/registers execute --- linking"
    r" architecture, bus, and memory map in one flow."),
   ("Common Mistakes",
    r"\begin{itemize}"
    r"\item Confusing data-bus width with address-bus width."
    r"\item Miscomputing $2^m$ capacity."
    r"\item Mixing up SRAM/DRAM properties."
    r"\end{itemize}")],
  I("Meetings 1--7 combine into one instruction-trace flow.",
    "Keep data-bus and address-bus widths distinct.",
    "Capacity math is $2^m$ times word width."),
  I("Trace a full fetch-execute for a LOAD using a given memory map.",
    "Compute capacity for a 20-line, 8-bit system.",
    "List SRAM vs DRAM differences from memory."))

M[10] = ("Integrated Circuits (IC) \\& Integration Scale",
  "Students are able to classify integrated circuits and their scale of integration.",
  I("Define an integrated circuit.",
    "Order SSI, MSI, LSI, VLSI.",
    "Relate scale to gate count."),
  [("Starting the Second Half of the Course",
    r"""Meetings 1--8 built the microcomputer model conceptually (CPU, buses, memory).
    \begin{itemize}
    \item Meetings 10--17 look at the physical building blocks: the \textbf{integrated circuits}
    that implement those units, and the \textbf{displays} that let a microcomputer talk to a human.
    \item We start with what an IC is and how the field classifies them by complexity.
    \end{itemize}"""),
   ("What Is an Integrated Circuit?",
    r"""An \textbf{integrated circuit (IC)} packs many transistors, resistors, and their
    interconnections onto a single piece of semiconductor (usually silicon).
    \begin{itemize}
    \item Replaces what would otherwise be many discrete components wired on a board.
    \item Fabricated photolithographically -- thousands to billions of devices per chip.
    \item The building block of every digital system studied in this course.
    \end{itemize}"""),
   ("Scales of Integration",
    r"""\begin{center}\begin{tabular}{l|l|l}\hline
    Scale & Gates (approx.) & Era / Example\\\hline
    SSI & 1--10 & basic gates (e.g.\ 7400 quad NAND)\\
    MSI & 10--100 & counters, decoders, multiplexers\\
    LSI & 100--10{,}000 & early microprocessors\\
    VLSI & $>10{,}000$ & modern microprocessors, memory chips\\\hline
    \end{tabular}\end{center}
    Some references add ULSI ($>1$ million gates) for the most complex modern chips."""),
   ("From SSI to VLSI: A Historical View",
    r"""\begin{itemize}
    \item 1960s: SSI -- a handful of gates per chip (early logic families).
    \item 1970s: MSI/LSI -- the first microprocessors (e.g.\ Intel 4004, 8085) at LSI scale.
    \item 1980s onward: VLSI -- million-plus-transistor microprocessors and memory.
    \item Each jump roughly follows \textbf{Moore's Law}: transistor count per chip doubling
    approximately every two years.
    \end{itemize}"""),
   ("Why Integration Matters",
    r"""\begin{itemize}
    \item \textbf{Size and weight:} critical in avionics, where every gram affects fuel and
    payload -- higher integration means fewer, smaller, lighter modules.
    \item \textbf{Power:} integrated transistors switch with far less power than discrete
    equivalents wired together.
    \item \textbf{Cost per function:} fabrication cost is amortized over millions of gates.
    \item \textbf{Reliability:} fewer solder joints and external wires means fewer failure points --
    directly relevant to flight-critical hardware.
    \end{itemize}"""),
   ("Classifying a Given Chip",
    r"""To classify a chip's scale, estimate its equivalent gate count from its function:
    \begin{itemize}
    \item A single logic gate package (e.g.\ 74LS08 quad AND) $\to$ SSI.
    \item A 4-bit counter or 8:1 multiplexer $\to$ MSI.
    \item An 8-bit microprocessor (thousands of gates) $\to$ LSI.
    \item A modern 64-bit CPU or gigabyte memory chip $\to$ VLSI.
    \end{itemize}"""),
   ("Trade-offs of Higher Integration",
    r"""\begin{itemize}
    \item Higher integration is not "free": fabrication defects grow with die area, so
    very large chips can have lower manufacturing yield.
    \item Debugging and testing a VLSI chip internally is far harder than testing SSI gates
    directly with a probe.
    \item Repair is impossible at the transistor level -- a faulty VLSI chip is simply replaced.
    \end{itemize}"""),
   ("Common Pitfalls \\& Tips",
    r"""\begin{itemize}
    \item Forgetting the scale boundaries are approximate, not exact cutoffs -- always
    reason about order of magnitude, not a hard number.
    \item Confusing "number of pins" with "number of gates" -- a chip can have few pins but
    many internal gates (e.g.\ a microprocessor).
    \item Mixing up SSI (simplest) and VLSI (most complex) order.
    \end{itemize}"""),
   ("Practice 1 -- Problem",
    r"Define SSI, MSI, LSI, and VLSI with their approximate gate ranges."),
   ("Practice 1 -- Solution",
    r"""SSI: 1--10 gates. MSI: 10--100 gates. LSI: 100--10,000 gates. VLSI: $>10{,}000$ gates."""),
   ("Practice 2 -- Problem",
    r"Explain two benefits of higher integration for avionics equipment specifically."),
   ("Practice 2 -- Solution",
    r"""(1) Reduced size and weight -- directly improves aircraft fuel efficiency and payload capacity.
    \\(2) Improved reliability -- fewer discrete solder joints and external wires means fewer
    potential failure points in flight-critical systems."""),
   ("Practice 3 -- Problem",
    r"Classify a modern 64-bit microprocessor by integration scale, and justify your answer."),
   ("Practice 3 -- Solution",
    r"""VLSI (in fact, often further described as ULSI). A modern 64-bit CPU contains many
    hundreds of millions to billions of transistors -- far beyond the $>10{,}000$-gate VLSI threshold."""),
   ("Practice 4 -- Problem",
    r"A single chip contains four independent 2-input AND gates and nothing else. What integration scale is this, and why might a designer still choose such a simple chip today?"),
   ("Practice 4 -- Solution",
    r"""This is SSI (a classic 74-series quad-AND package, roughly 4 gates).
    \\Designers still use SSI glue logic for simple, well-isolated functions (e.g.\ one
    extra AND gate for an enable signal) where adding a whole programmable VLSI device
    would be unnecessary cost and complexity for the task.""")],
  I("An IC integrates many transistors on one chip.",
    "SSI to VLSI orders chips by gate count.",
    "Integration reduces size, power, and cost."),
  I("Define SSI, MSI, LSI, VLSI with gate ranges.",
    "Explain two benefits of integration for avionics.",
    "Classify a modern microprocessor by scale."))

M[11] = ("Logic Families (TTL / CMOS)",
  "Students are able to compare logic families TTL and CMOS.",
  I("Describe TTL and CMOS technologies.",
    "Compare power, speed, and noise margin.",
    "State interfacing considerations."),
  [("What Is a Logic Family?",
    r"""A \textbf{logic family} is a set of ICs built with the same underlying transistor
    technology and electrical conventions, so parts within the family interoperate directly.
    \begin{itemize}
    \item The two dominant families in this course: \textbf{TTL} and \textbf{CMOS}.
    \item Choosing a family affects speed, power consumption, noise immunity, and how a
    circuit interfaces with other chips.
    \end{itemize}"""),
   ("TTL: Transistor-Transistor Logic",
    r"""\begin{itemize}
    \item Built from bipolar junction transistors (BJTs).
    \item Fast switching, but draws continuous (static) current even when idle -- higher
    power consumption than CMOS.
    \item Standard supply: 5V $\pm$ 5\%.
    \item Historically the dominant family (7400 series) from the 1960s--1980s.
    \end{itemize}"""),
   ("CMOS: Complementary Metal-Oxide-Semiconductor",
    r"""\begin{itemize}
    \item Built from complementary pairs of MOSFETs (one PMOS, one NMOS per gate).
    \item Extremely low \textbf{static} power -- current flows mainly only \emph{while switching}.
    \item Higher transistor density than TTL for the same die area -- key to VLSI scaling.
    \item Wide supply-voltage range (historically 3--15V; modern CMOS logic often 1.8--5V).
    \end{itemize}"""),
   ("Detailed Comparison",
    r"""\begin{center}\begin{tabular}{l|l|l}\hline
    & TTL & CMOS\\\hline
    Static power & high & very low\\ Dynamic power & moderate & rises with switching frequency\\
    Speed & fast & fast (modern processes)\\
    Noise margin & moderate & high\\ Supply & 5V (fixed) & wide range\\
    Density & lower & higher\\\hline\end{tabular}\end{center}"""),
   ("Logic Levels \\& Noise Margin",
    r"""\begin{itemize}
    \item $V_{IH}$/$V_{IL}$: minimum input HIGH / maximum input LOW voltage a gate reliably recognizes.
    \item $V_{OH}$/$V_{OL}$: guaranteed output HIGH / LOW voltage a gate produces.
    \item \textbf{Noise margin} $= V_{OH}-V_{IH}$ (high side) or $V_{IL}-V_{OL}$ (low side) --
    how much noise a signal can tolerate before being misread.
    \item CMOS typically has wider noise margins than TTL, making it more robust in noisy
    environments such as an aircraft's electrical system.
    \end{itemize}"""),
   ("Fan-Out",
    r"""\textbf{Fan-out} is the maximum number of standard inputs one output can reliably drive.
    \begin{itemize}
    \item Limited by the output's drive current versus each input's required current.
    \item TTL outputs sink/source limited current, capping fan-out to other TTL inputs.
    \item CMOS inputs draw almost no static current, so CMOS fan-out is very high --
    though high-speed switching still loads the output with capacitance.
    \end{itemize}"""),
   ("Interfacing TTL and CMOS",
    r"""\begin{itemize}
    \item Always match logic levels ($V_{IH}/V_{IL}$, $V_{OH}/V_{OL}$) between the driving
    and receiving family before connecting them directly.
    \item Use a \textbf{level shifter/translator} IC when supply voltages differ significantly.
    \item \textbf{CMOS inputs must never be left floating} -- an undriven CMOS input can sit
    at an intermediate voltage, turning on both the PMOS and NMOS transistors simultaneously
    and causing excess current draw (and unpredictable logic behaviour).
    \item Tie unused CMOS inputs firmly to $V_{CC}$ or GND through a pull-up/pull-down.
    \end{itemize}"""),
   ("Common Pitfalls \\& Tips",
    r"""\begin{itemize}
    \item Assuming all "5V logic" chips are automatically compatible -- always check
    $V_{IH}/V_{IL}$ thresholds, not just the supply voltage.
    \item Leaving unused CMOS inputs floating "because they're not connected to anything important."
    \item Forgetting that CMOS dynamic power \emph{rises} with switching frequency, unlike its
    near-zero static power.
    \end{itemize}"""),
   ("Practice 1 -- Problem",
    r"Give two differences between TTL and CMOS."),
   ("Practice 1 -- Solution",
    r"""(1) TTL uses bipolar transistors and draws continuous static current; CMOS uses
    complementary MOSFETs with very low static power.
    \\(2) TTL has a fixed 5V supply; CMOS operates over a much wider supply-voltage range."""),
   ("Practice 2 -- Problem",
    r"Why must CMOS inputs not be left floating?"),
   ("Practice 2 -- Solution",
    r"""A floating CMOS input can settle at an intermediate voltage that partially turns on
    both the PMOS and NMOS transistors of the input stage simultaneously, causing excessive
    (and unpredictable) current draw and possible logic-level ambiguity."""),
   ("Practice 3 -- Problem",
    r"State one reason CMOS dominates modern ICs over TTL."),
   ("Practice 3 -- Solution",
    r"""CMOS's very low static power consumption and higher transistor density allow far
    more gates to be packed onto a chip (VLSI/ULSI scale) without excessive heat or power draw --
    something bipolar TTL cannot match at the same integration level."""),
   ("Practice 4 -- Problem",
    r"A 5V TTL output ($V_{OH,min}=2.4$V) drives a CMOS input requiring $V_{IH,min}=3.5$V. Will this interface reliably, and what should be done if not?"),
   ("Practice 4 -- Solution",
    r"""No -- the TTL output's guaranteed HIGH ($2.4$V minimum) is below the CMOS input's
    required HIGH threshold ($3.5$V), so the CMOS gate may not reliably register a HIGH.
    \\Fix: add a pull-up resistor to $V_{CC}$ on the TTL output, or use a dedicated
    TTL-to-CMOS level-shifting buffer/translator IC.""")],
  I("TTL is bipolar; CMOS is complementary MOSFET with low static power.",
    "CMOS has better noise margin and density.",
    "Interfacing requires matched levels and fan-out."),
  I("Give two differences between TTL and CMOS.",
    "Why must CMOS inputs not be left floating?",
    "State one reason CMOS dominates modern ICs."))

M[12] = ("IC Electrical Characteristics \\& Packaging",
  "Students are able to analyze IC electrical characteristics and packaging for component selection.",
  I("Interpret voltage and current ratings.",
    "Explain fan-out and propagation delay.",
    "Identify common package types."),
  [("Why Electrical Characteristics Matter",
    r"""Choosing the right IC for a design means more than matching its logic function --
    it must also survive and perform correctly within its rated electrical limits.
    \begin{itemize}
    \item Every parameter in this meeting comes straight from a manufacturer's \textbf{datasheet}.
    \item Getting these numbers wrong can destroy a chip or make a circuit unreliable in the field.
    \end{itemize}"""),
   ("Absolute Maximum Ratings",
    r"""\begin{itemize}
    \item Supply voltage range and tolerance (e.g.\ $5\text{V}\pm5\%$).
    \item Maximum input voltage, maximum output current, maximum power dissipation.
    \item Storage and operating temperature range.
    \item \textbf{Exceeding} any absolute maximum rating, even briefly, risks permanent
    damage -- these are not "recommended," they are hard limits.
    \end{itemize}"""),
   ("Logic Threshold Voltages",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Symbol & Meaning\\\hline
    $V_{IH}$ & minimum input voltage read as logic HIGH\\
    $V_{IL}$ & maximum input voltage read as logic LOW\\
    $V_{OH}$ & guaranteed minimum output voltage for HIGH\\
    $V_{OL}$ & guaranteed maximum output voltage for LOW\\\hline
    \end{tabular}\end{center}
    Noise margin (high) $=V_{OH}-V_{IH}$; noise margin (low) $=V_{IL}-V_{OL}$."""),
   ("Drive Currents \\& Power Dissipation",
    r"""\begin{itemize}
    \item $I_{OH}$: current an output can \textbf{source} while staying above $V_{OH}$.
    \item $I_{OL}$: current an output can \textbf{sink} while staying below $V_{OL}$.
    \item Power dissipation $P = V_{CC}\times I_{CC}$ (plus switching losses) -- determines
    heat generated and cooling/derating requirements.
    \end{itemize}"""),
   ("Timing: Propagation Delay",
    r"""\textbf{Propagation delay} ($t_{PD}$) is the time from a valid input change to the
    corresponding output change.
    \begin{itemize}
    \item Limits the maximum clock frequency a circuit built from that gate can achieve.
    \item Given as $t_{PLH}$ (low-to-high) and $t_{PHL}$ (high-to-low); datasheets often quote
    the worse (larger) of the two as the design limit.
    \item Cascading gates adds their propagation delays -- critical for timing budget in a
    synchronous design.
    \end{itemize}"""),
   ("Fan-Out Revisited",
    r"""\textbf{Fan-out} = how many standard inputs one output can reliably drive without
    violating $V_{OH}/V_{OL}$ guarantees.
    \[ \text{Fan-out} \approx \min\left(\frac{I_{OH}}{I_{IH}}, \frac{I_{OL}}{I_{IL}}\right) \]
    Exceeding fan-out degrades output voltage margins and can cause logic errors under load."""),
   ("IC Packaging Types",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Package & Note\\\hline
    DIP & Dual In-line Package -- through-hole, easy prototyping\\
    SOIC & Small-Outline IC -- surface-mount, compact\\
    QFP & Quad Flat Package -- many pins on all four sides, flat\\
    BGA & Ball Grid Array -- solder balls under the chip, highest density\\\hline
    \end{tabular}\end{center}
    Denser packages (QFP, BGA) suit high pin-count VLSI chips; DIP suits low pin-count,
    hand-solderable or socketed prototyping."""),
   ("Selecting a Package for Avionics",
    r"""\begin{itemize}
    \item Vibration and thermal cycling favor solder-friendly, well-supported packages.
    \item High pin-count VLSI (microprocessors, FPGAs) typically forces BGA or QFP.
    \item Repairability and inspection ease sometimes favor larger, visible-lead packages
    when the choice is otherwise open.
    \end{itemize}"""),
   ("Practice 1 -- Problem",
    r"Define fan-out and propagation delay."),
   ("Practice 1 -- Solution",
    r"""Fan-out: the maximum number of standard logic inputs one output can reliably drive
    while remaining within its $V_{OH}/V_{OL}$ guarantees.
    \\Propagation delay: the time between a valid input change and the resulting output
    change at a gate."""),
   ("Practice 2 -- Problem",
    r"List the four logic-threshold voltages and what each one represents."),
   ("Practice 2 -- Solution",
    r"""$V_{IH}$ -- minimum input voltage read as HIGH. $V_{IL}$ -- maximum input voltage
    read as LOW. $V_{OH}$ -- guaranteed minimum output HIGH voltage. $V_{OL}$ -- guaranteed
    maximum output LOW voltage."""),
   ("Practice 3 -- Problem",
    r"Name a package suited to a high pin-count VLSI chip, and explain why DIP would be unsuitable there."),
   ("Practice 3 -- Solution",
    r"""BGA (or QFP) suits high pin-count VLSI chips because their pins/balls can be packed
    densely under or around the whole chip footprint.
    \\DIP is unsuitable at high pin counts because its two rows of through-hole pins along
    only two edges would make the package impractically long."""),
   ("Practice 4 -- Problem",
    r"A gate has $I_{OH}=400\,\mu A$ and each connected input requires $I_{IH}=40\,\mu A$. What is the fan-out limit from the HIGH-side current alone?"),
   ("Practice 4 -- Solution",
    r"""Fan-out $=I_{OH}/I_{IH} = 400/40 = 10$.
    \\The output can reliably drive up to 10 standard inputs before $V_{OH}$ guarantees are at risk (the LOW-side limit must also be checked and the smaller of the two used).""")],
  I("Datasheet ratings define safe operating limits.",
    "Propagation delay and fan-out bound speed and loading.",
    "Packages range from DIP to BGA by density."),
  I("Define fan-out and propagation delay.",
    "List the four logic-threshold voltages.",
    "Name a package suited to high pin counts."))

M[13] = ("Lab: IC Datasheet Identification",
  "Students are able to read IC datasheets to identify and select components.",
  I("Locate key parameters in a datasheet.",
    "Interpret a pinout diagram.",
    "Verify operating conditions."),
  [("Why This Lab Matters",
    r"""Meetings 10--12 gave the vocabulary (integration scale, logic families, electrical
    characteristics). This lab meeting puts it to direct, practical use.
    \begin{itemize}
    \item Every component selection in real avionics maintenance and design starts with
    reading a manufacturer's datasheet correctly.
    \item Misreading a datasheet is one of the most common causes of field failures and
    rework in electronics.
    \end{itemize}"""),
   ("Datasheet Structure Overview",
    r"""\begin{itemize}
    \item \textbf{Functional description} and block diagram -- what the chip does internally.
    \item \textbf{Pin configuration (pinout)} -- physical pin assignments.
    \item \textbf{Absolute maximum ratings} -- hard survival limits (Meeting 12).
    \item \textbf{Recommended operating conditions} -- the safe range for normal operation
    (narrower than absolute maximums).
    \item \textbf{Electrical characteristics} -- $V_{IH}/V_{IL}/V_{OH}/V_{OL}$, currents, power.
    \item \textbf{Timing characteristics} -- propagation delay, setup/hold times.
    \end{itemize}"""),
   ("Reading a Pinout Diagram",
    r"""Identify $V_{CC}$ (power), GND (ground), inputs, and outputs from the pin diagram.
    \begin{itemize}
    \item Example: a 74LS08 quad 2-input AND gate has 14 pins -- pin 14 = $V_{CC}$,
    pin 7 = GND, and four independent AND gates occupy the remaining 12 pins (2 inputs +
    1 output each).
    \item Pin 1 is conventionally marked by a notch or dot on the package for orientation.
    \end{itemize}"""),
   ("Absolute Maximum vs. Recommended Operating Conditions",
    r"""\begin{center}\begin{tabular}{l|l|l}\hline
    & Absolute Max & Recommended\\\hline
    Supply & e.g.\ $-0.5$ to $7$V & e.g.\ $4.75$--$5.25$V\\
    Range use & never exceed (damage risk) & normal design target\\\hline
    \end{tabular}\end{center}
    Designing at the edge of the recommended range still leaves margin before hitting the
    absolute maximum -- good practice for reliability."""),
   ("Electrical Characteristics Table (Example Reading)",
    r"""A typical TTL datasheet electrical table might list, at $V_{CC}=5$V, $25^{\circ}$C:
    \begin{center}\begin{tabular}{l|l}\hline
    Parameter & Typical Value\\\hline
    $V_{IH}$(min) & 2.0V\\ $V_{IL}$(max) & 0.8V\\
    $V_{OH}$(min) & 2.4V\\ $V_{OL}$(max) & 0.4V\\\hline
    \end{tabular}\end{center}
    These four numbers alone let you check interfacing compatibility (Meeting 11)."""),
   ("Timing Characteristics (Example Reading)",
    r"""A datasheet timing section lists, e.g., $t_{PLH}=15$ns, $t_{PHL}=12$ns for a gate.
    \begin{itemize}
    \item Use the larger of the two as the worst-case propagation delay for timing budgets.
    \item For sequential parts (flip-flops), also check setup time ($t_{su}$) and hold
    time ($t_h$) relative to the clock edge.
    \end{itemize}"""),
   ("Verifying Component Suitability: A Checklist",
    r"""\begin{enumerate}
    \item Confirm supply voltage matches the design's available rail.
    \item Check logic-level compatibility with neighboring chips ($V_{IH}/V_{IL}$ vs.\ $V_{OH}/V_{OL}$).
    \item Confirm drive current ($I_{OH}/I_{OL}$) meets the fan-out/load requirement.
    \item Confirm propagation delay meets the design's required clock rate.
    \item Confirm operating temperature range covers the application's environment.
    \end{enumerate}"""),
   ("Common Pitfalls \\& Tips",
    r"""\begin{itemize}
    \item Reading "typical" values as guaranteed -- always design against "min"/"max" columns,
    not "typical," for reliable operation across manufacturing variation.
    \item Confusing pin \emph{numbers} (physical location) with pin \emph{names/functions}.
    \item Overlooking the temperature range -- a part rated for $0$--$70^{\circ}$C commercial
    grade may not survive an avionics environment requiring extended/military range.
    \end{itemize}"""),
   ("Practice 1 -- Problem",
    r"Identify the $V_{CC}$ and GND pins of a 74LS08 (14-pin quad 2-input AND gate)."),
   ("Practice 1 -- Solution",
    r"""Pin 14 = $V_{CC}$ (power). Pin 7 = GND (ground) -- the standard diagonal placement
    used across the 74-series 14-pin DIP family."""),
   ("Practice 2 -- Problem",
    r"List the datasheet sections you would check, in order, to pick a gate IC for a new design."),
   ("Practice 2 -- Solution",
    r"""(1) Functional description/block diagram -- confirm it does the right logic function.
    (2) Pinout -- confirm pin count and layout fit the board.
    (3) Recommended operating conditions -- confirm supply voltage fits.
    (4) Electrical characteristics -- confirm logic-level and current compatibility.
    (5) Timing characteristics -- confirm speed meets the design's clock rate."""),
   ("Practice 3 -- Problem",
    r"Explain why absolute maximum ratings must not be exceeded, even briefly."),
   ("Practice 3 -- Solution",
    r"""Absolute maximum ratings define the hard physical/electrical limits beyond which the
    silicon or package can suffer permanent damage (e.g.\ junction breakdown, thermal damage).
    \\Unlike recommended operating conditions, there is no "margin" beyond an absolute
    maximum -- exceeding it risks immediate or latent (delayed) failure."""),
   ("Practice 4 -- Problem",
    r"A datasheet lists a chip's operating temperature as $0^\circ$C to $70^\circ$C (commercial grade). Is this suitable for an aircraft avionics bay, and what should you check instead?"),
   ("Practice 4 -- Solution",
    r"""Not necessarily suitable -- avionics bays can see wider temperature extremes than a
    commercial-grade part guarantees.
    \\Check the datasheet for an industrial ($-40^\circ$C to $85^\circ$C) or
    military/aerospace-qualified ($-55^\circ$C to $125^\circ$C) grade version of the same part.""")],
  I("Datasheets give function, pinout, ratings, and timing.",
    "The pinout locates power, ground, inputs, and outputs.",
    "Selection verifies voltage, level, current, and timing."),
  I("Identify $V_{CC}$ and GND pins of a 74LS08.",
    "List the datasheet sections you would check to pick a gate IC.",
    "Explain why absolute maximum ratings must not be exceeded."))

M[14] = ("Displays: LED \\& Seven-Segment",
  "Students are able to explain LED and seven-segment displays and their interfacing.",
  I("Explain LED operation and current limiting.",
    "Describe seven-segment structure.",
    "Distinguish common-anode and common-cathode."),
  [("From Logic to Human-Readable Output",
    r"""Meetings 10--13 covered the ICs that compute; now we turn to \textbf{displays} --
    how a microcomputer shows its results to a human operator.
    \begin{itemize}
    \item Displays are the most common output peripheral in avionics cockpits and test equipment.
    \item We start with the simplest: the LED, then build up to the seven-segment digit display.
    \end{itemize}"""),
   ("The Light-Emitting Diode (LED)",
    r"""An LED is a diode that emits light when forward-biased, conducting current from
    anode to cathode.
    \begin{itemize}
    \item Forward voltage drop $V_{LED}$ is roughly constant (e.g.\ $\approx2$V for a red LED)
    once conducting -- it is \emph{not} a resistor and does not obey Ohm's law directly.
    \item Exceeding the rated forward current permanently damages the LED.
    \end{itemize}"""),
   ("Current-Limiting Resistor",
    r"""Because an LED's own resistance is nonlinear, a \textbf{series resistor} sets the
    safe operating current from a fixed supply:
    \[ R = \frac{V_{supply}-V_{LED}}{I_{LED}} \]
    Example: $V_{supply}=5$V, $V_{LED}=2$V, $I_{LED}=10$mA:
    \[ R = (5-2)/0.01 = 300\,\Omega \]"""),
   ("Seven-Segment Display Structure",
    r"""Seven LEDs, labelled a--g, arranged to form the shape of digits 0--9, plus often an
    eighth LED for the decimal point (dp).
    \begin{itemize}
    \item Lighting a specific subset of segments forms each digit's shape.
    \item Driven by a \textbf{BCD-to-seven-segment decoder} IC that converts a 4-bit
    binary-coded-decimal input into the correct segment pattern.
    \end{itemize}"""),
   ("Segment Patterns for Digits",
    r"""\begin{center}\begin{tabular}{c|l}\hline
    Digit & Segments lit (a b c d e f g)\\\hline
    0 & a b c d e f\\ 1 & b c\\ 2 & a b d e g\\ 3 & a b c d g\\
    4 & b c f g\\ 8 & a b c d e f g\\\hline
    \end{tabular}\end{center}
    Each row is exactly the decoder's truth-table output for that BCD input."""),
   ("Common Anode vs. Common Cathode",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Type & Turn segment ON\\\hline
    Common anode & drive segment LOW (sink current)\\
    Common cathode & drive segment HIGH (source current)\\\hline
    \end{tabular}\end{center}
    \begin{itemize}
    \item Common anode: all segment anodes tied to $V_{CC}$; each segment's cathode pulled
    LOW individually to light it.
    \item Common cathode: all segment cathodes tied to GND; each segment's anode driven
    HIGH individually to light it.
    \item The decoder/driver IC must match the display's polarity.
    \end{itemize}"""),
   ("Multiplexing Multiple Digits (Preview)",
    r"""Driving several seven-segment digits with individual wires for every segment of
    every digit would need too many pins.
    \begin{itemize}
    \item Instead, segments of all digits are wired in parallel, and only \emph{one digit's}
    common pin is enabled at a time, cycled rapidly (multiplexing).
    \item Fast enough cycling makes all digits appear continuously lit to the human eye --
    covered in depth next meeting.
    \end{itemize}"""),
   ("Common Pitfalls \\& Tips",
    r"""\begin{itemize}
    \item Omitting the current-limiting resistor -- directly connecting an LED to a supply
    destroys it almost instantly.
    \item Mixing up common-anode and common-cathode wiring/decoder choice -- the display
    will show nothing (or the wrong pattern) if mismatched.
    \item Forgetting the decimal point segment when wiring or programming a display.
    \end{itemize}"""),
   ("Practice 1 -- Problem",
    r"Compute the current-limiting resistor for a 2V LED at 15 mA from a 5V supply."),
   ("Practice 1 -- Solution",
    r"""$R = (V_{supply}-V_{LED})/I_{LED} = (5-2)/0.015 = 200\,\Omega$."""),
   ("Practice 2 -- Problem",
    r"List the segments lit to display the digit 3 on a seven-segment display."),
   ("Practice 2 -- Solution",
    r"""Digit 3 lights segments a, b, c, d, g (the top, upper-right, lower-right, bottom,
    and middle segments)."""),
   ("Practice 3 -- Problem",
    r"State how to turn a segment ON in a common-anode display, and why."),
   ("Practice 3 -- Solution",
    r"""Drive the segment's cathode LOW (sink current through it) -- because in a
    common-anode display, all segment anodes already sit at $V_{CC}$, so a segment only
    conducts (lights) when its cathode is pulled to a lower potential, completing the circuit."""),
   ("Practice 4 -- Problem",
    r"A designer accidentally connects a common-cathode seven-segment display to a decoder IC designed for common-anode displays. What symptom would you expect, and why?"),
   ("Practice 4 -- Solution",
    r"""The display would show the \textbf{inverse} pattern of what is intended (segments
    that should be off light up, and vice versa), or stay fully dark/fully lit depending on
    the decoder's idle output state.
    \\Cause: a common-anode decoder drives segments LOW to turn them on, but a
    common-cathode display needs its segments driven HIGH to light -- the polarity mismatch
    inverts every segment's behaviour.""")],
  I("An LED needs a current-limiting resistor.",
    "A seven-segment display lights segments a--g to form digits.",
    "Common-anode and common-cathode differ in drive polarity."),
  I("Compute the resistor for a 2V LED at 15 mA from 5V.",
    "List the segments lit to display the digit 3.",
    "State how to turn a segment on in a common-anode display."))

M[15] = ("Displays: Dot-Matrix \\& LCD",
  "Students are able to explain dot-matrix and LCD displays.",
  I("Describe dot-matrix scanning.",
    "Explain LCD operation.",
    "Compare display technologies."),
  [("Beyond Single Digits",
    r"""Seven-segment displays (Meeting 14) only show digits and a few letters.
    \begin{itemize}
    \item Full text and graphics need finer-grained displays: \textbf{dot-matrix} and
    \textbf{LCD} technologies.
    \item Both appear throughout avionics: annunciator panels, multi-function displays,
    and test-equipment readouts.
    \end{itemize}"""),
   ("Dot-Matrix Display Structure",
    r"""An $m\times n$ grid of individually addressable LEDs (or, on larger panels,
    incandescent/other elements), typically $5\times7$ or $8\times8$ per character cell.
    \begin{itemize}
    \item Each LED sits at the intersection of one row line and one column line.
    \item Turning on a specific pattern of intersections draws a character or simple graphic.
    \end{itemize}"""),
   ("Multiplexed Scanning",
    r"""Wiring every LED with its own dedicated pair of control lines would need
    $m\times n$ connections -- far too many for a practical display.
    \begin{itemize}
    \item Instead, rows and columns are wired so only $m+n$ lines are needed.
    \item The controller activates one row at a time, driving the correct column pattern
    for that row, then moves to the next row -- \textbf{multiplexing}.
    \item Cycling through all rows fast enough (well above the eye's flicker-fusion rate,
    roughly 50--60 Hz) makes the whole grid appear continuously and steadily lit.
    \end{itemize}"""),
   ("Liquid-Crystal Display (LCD) Principle",
    r"""LCDs \textbf{modulate} light passing through them rather than emitting their own light.
    \begin{itemize}
    \item A liquid-crystal layer twists polarized light when an electric field is applied,
    blocking or passing light through a polarizing filter.
    \item Because the panel does not generate light itself, most LCDs need a
    \textbf{backlight} behind the panel for visibility.
    \item Much lower power than an equivalent-size emissive (LED) display.
    \end{itemize}"""),
   ("Character LCDs \\& the HD44780 Controller",
    r"""\begin{itemize}
    \item Common character LCDs (e.g.\ 16$\times$2, meaning 16 characters $\times$ 2 rows)
    are built around the industry-standard \textbf{HD44780} controller.
    \item The controller has a built-in character generator ROM, an internal DDRAM
    (display data RAM) holding what is currently shown, and a simple command/data interface.
    \item A microcomputer sends commands (clear, cursor position) and character data over
    a 4-bit or 8-bit parallel bus (or a serial adapter) to this controller.
    \end{itemize}"""),
   ("Passive vs. Active Matrix",
    r"""\begin{itemize}
    \item \textbf{Passive matrix:} pixels are addressed only briefly during a row/column
    scan, similar in spirit to LED multiplexing -- simpler, cheaper, but slower response
    and lower contrast at large sizes.
    \item \textbf{Active matrix (TFT):} each pixel has its own transistor holding its state
    between refresh scans -- much better contrast, response time, and image quality, used
    in modern glass-cockpit multi-function displays.
    \end{itemize}"""),
   ("Comparing LED Matrix and LCD",
    r"""\begin{center}\begin{tabular}{l|l|l}\hline
    & LED matrix & LCD\\\hline
    Emits light & yes (self-luminous) & no (needs backlight)\\
    Power & higher & low\\
    Content & dots/simple graphics & text/detailed graphics\\
    Viewing in direct sun & often excellent & can wash out (backlight-dependent)\\\hline
    \end{tabular}\end{center}"""),
   ("Common Pitfalls \\& Tips",
    r"""\begin{itemize}
    \item Assuming an LCD "generates" light -- it only modulates backlight or ambient light.
    \item Scanning a dot-matrix display too slowly -- visible flicker or dim, uneven brightness results.
    \item Confusing the HD44780's command mode and data (character) mode -- sending
    character codes while the controller expects a command corrupts the display.
    \end{itemize}"""),
   ("Practice 1 -- Problem",
    r"Explain multiplexing in a dot-matrix display and why it is necessary."),
   ("Practice 1 -- Solution",
    r"""Multiplexing activates one row at a time with the correct column pattern, cycling
    through all rows fast enough that the human eye perceives a steady, complete image.
    \\It is necessary because wiring every LED individually would require $m\times n$
    control lines instead of just $m+n$, which is impractical for larger displays."""),
   ("Practice 2 -- Problem",
    r"State one advantage and one drawback of LCDs compared to LED matrix displays."),
   ("Practice 2 -- Solution",
    r"""Advantage: much lower power consumption for a given display size.
    \\Drawback: needs a backlight to be visible (it does not emit its own light), and can
    have slower response time or lower contrast (especially passive-matrix types) than
    self-luminous LED displays."""),
   ("Practice 3 -- Problem",
    r"Name the common controller for character LCDs and one piece of information it stores internally."),
   ("Practice 3 -- Solution",
    r"""HD44780. It stores the currently displayed characters in its internal DDRAM
    (display data RAM), and has a character generator ROM defining each character's dot pattern."""),
   ("Practice 4 -- Problem",
    r"A 16x2 character LCD shows garbled characters intermittently. The microcomputer's software sends commands and character data over the same 8-bit bus without checking a status/control line. What is the likely cause?"),
   ("Practice 4 -- Solution",
    r"""The software is likely writing data before the HD44780 has finished processing the
    previous command (violating the controller's busy/timing requirements), or it is not
    correctly toggling the register-select (RS) line to distinguish command bytes from
    character-data bytes -- causing some data to be misinterpreted as commands or vice versa.""")],
  I("Dot-matrix displays are multiplexed LED grids.",
    "LCDs modulate light and use low power.",
    "LED and LCD trade brightness for power."),
  I("Explain multiplexing in a dot-matrix display.",
    "State one advantage and one drawback of LCDs.",
    "Name the common controller for character LCDs."))

M[16] = ("Display Interfacing with Microcomputer",
  "Students are able to interface displays with a microcomputer.",
  I("Explain parallel vs serial display interfaces.",
    "Describe driver and decoder ICs.",
    "Outline software driving of a display."),
  [("Closing the Loop: Microcomputer to Display",
    r"""Meetings 14--15 covered display technologies themselves. This meeting connects
    them back to the microcomputer architecture from Meetings 1--8: how does a CPU
    actually command a display to show something?
    \begin{itemize}
    \item The interface must translate the CPU's digital output into the specific timing
    and signal levels each display technology requires.
    \end{itemize}"""),
   ("Parallel Interfaces",
    r"""\begin{itemize}
    \item Multiple data lines (e.g.\ 4 or 8 bits) carry a full character/segment pattern
    simultaneously.
    \item Fast -- a full word transfers in one bus cycle.
    \item Uses more I/O pins on the microcomputer -- can be a limiting resource on small
    microcontrollers.
    \item Typical for direct seven-segment segment drive or 8-bit character LCD interfaces.
    \end{itemize}"""),
   ("Serial Interfaces",
    r"""\begin{itemize}
    \item Data sent one bit at a time over one or two signal lines, using a defined
    protocol and timing.
    \item \textbf{SPI:} clock + data line(s) + chip-select, simple and fast, point-to-point.
    \item \textbf{I\textsuperscript{2}C:} two shared lines (SDA, SCL) can address multiple
    devices on the same bus using device addresses.
    \item Uses far fewer pins than parallel -- valuable when I/O pins are scarce -- at the
    cost of needing shift/timing logic (usually handled by the peripheral's controller).
    \end{itemize}"""),
   ("Parallel vs. Serial: Trade-off Summary",
    r"""\begin{center}\begin{tabular}{l|l|l}\hline
    & Parallel & Serial\\\hline
    Pin count & high & low\\ Speed per transfer & fast & slower (bit-by-bit)\\
    Wiring complexity & higher (many traces) & lower\\
    Typical use & local, pin-rich systems & pin-limited, longer-distance links\\\hline
    \end{tabular}\end{center}"""),
   ("Driver and Decoder ICs",
    r"""\begin{itemize}
    \item \textbf{BCD-to-seven-segment decoder:} converts a 4-bit binary-coded-decimal
    value into the correct 7-segment pattern (Meeting 14) -- offloads this translation
    from CPU software into dedicated hardware.
    \item \textbf{Current-driver ICs:} supply the higher current LED segments or dot-matrix
    rows need, beyond what a microcomputer's I/O pin can source/sink directly.
    \item \textbf{Multiplex controllers:} automatically cycle through multiple digits/rows
    of a display, refreshing each in turn without ongoing CPU intervention.
    \end{itemize}"""),
   ("LCD Controller Interfacing (HD44780 Example)",
    r"""\begin{itemize}
    \item Control lines: RS (register select: command vs.\ data), R/W (read/write), E (enable strobe).
    \item Data lines: 4-bit mode (half the pins, two writes per byte) or 8-bit mode
    (all pins, one write per byte).
    \item Software must issue an initialization sequence, then commands (clear display,
    set cursor) interleaved with character data, obeying the RS line.
    \end{itemize}"""),
   ("Driving a Display in Software: General Steps",
    r"""\begin{enumerate}
    \item Configure the relevant I/O port pins as outputs (direction registers).
    \item Send the initial setup/configuration command sequence required by the display/controller.
    \item Send the segment pattern or character data for what should be shown.
    \item For multiplexed displays: refresh each digit/row in turn, fast enough to avoid
    visible flicker (well above roughly 50--60 Hz refresh).
    \item Insert precise timing delays where the display's datasheet requires them
    (e.g.\ HD44780 command execution times).
    \end{enumerate}"""),
   ("Common Pitfalls \\& Tips",
    r"""\begin{itemize}
    \item Forgetting to configure I/O pins as outputs before writing to them -- the display
    will not respond even if the code "sends" the right values.
    \item Refreshing a multiplexed display too slowly, causing visible flicker or dim/uneven digits.
    \item Ignoring an LCD controller's required command-execution delay, corrupting subsequent data.
    \item Choosing parallel interfacing on a pin-starved microcontroller instead of serial.
    \end{itemize}"""),
   ("Practice 1 -- Problem",
    r"Compare parallel and serial display interfaces in terms of pin count and speed."),
   ("Practice 1 -- Solution",
    r"""Parallel: uses more pins (one per bit transferred) but transfers a full word in one
    cycle -- faster per transfer.
    \\Serial: uses very few pins (e.g.\ 2 for I2C) but transfers one bit at a time, so is
    slower per transfer, though often still fast enough for display refresh rates."""),
   ("Practice 2 -- Problem",
    r"Explain the role of a BCD-to-7-segment decoder in a display interface."),
   ("Practice 2 -- Solution",
    r"""It converts a compact 4-bit binary-coded-decimal value (as computed/stored by the
    CPU) into the corresponding 7-bit segment-on/off pattern needed to display that digit,
    moving this translation work out of CPU software and into dedicated hardware."""),
   ("Practice 3 -- Problem",
    r"Outline the steps to drive a multiplexed 4-digit seven-segment display in software."),
   ("Practice 3 -- Solution",
    r"""(1) Configure segment and digit-select pins as outputs.
    (2) For each digit in turn: output that digit's segment pattern, then enable only that
    digit's common line while disabling the others.
    (3) Hold briefly, then move to the next digit, repeating fast enough (well above
    flicker-fusion rate) that all digits appear simultaneously and steadily lit."""),
   ("Practice 4 -- Problem",
    r"A microcontroller has only 6 free I/O pins remaining but needs to drive a 16x2 character LCD, which normally needs at least 10 pins (RS, E, and 8 data lines minimum). What two changes make this feasible?"),
   ("Practice 4 -- Solution",
    r"""(1) Use the HD44780's 4-bit data mode instead of 8-bit mode, cutting the data lines
    from 8 to 4 (at the cost of sending each byte as two 4-bit nibbles).
    \\(2) Tie R/W permanently to GND (write-only operation, never reading the LCD's busy
    flag) to save one more pin, using fixed software delays instead.
    \\Together: RS + E + 4 data lines = 6 pins, exactly matching what is available.""")],
  I("Displays connect via parallel or serial interfaces.",
    "Decoder/driver ICs translate and supply current.",
    "Software configures ports and refreshes the display."),
  I("Compare parallel and serial display interfaces.",
    "Explain the role of a BCD-to-7-segment decoder.",
    "Outline the steps to drive a multiplexed display in software."))

M[17] = ("Integrated Review (Pre-Final)",
  "Students are able to integrate IC and display concepts (Meetings 10--16) for the final exam.",
  I("Combine IC selection and display interfacing.",
    "Solve integrated post-midterm exercises.",
    "Confirm readiness for the final."),
  [("Final Scope (Meetings 10--16)",
    r"""\begin{itemize}
    \item ICs: integration scale (SSI--VLSI), logic families (TTL/CMOS).
    \item Electrical characteristics, timing, packaging, and datasheet reading.
    \item Displays: LED, seven-segment, dot-matrix, LCD, and their interfacing.
    \end{itemize}"""),
   ("Recap: IC Selection Chain",
    r"""\begin{enumerate}
    \item Identify the required logic function and estimate integration scale.
    \item Choose a logic family (TTL/CMOS) compatible with the rest of the design.
    \item Verify electrical characteristics ($V_{IH}/V_{IL}/V_{OH}/V_{OL}$, currents, timing)
    against the datasheet.
    \item Select a package suited to the assembly method and pin count.
    \end{enumerate}"""),
   ("Recap: Display Formulas",
    r"""\begin{itemize}
    \item LED series resistor: $R=(V_{supply}-V_{LED})/I_{LED}$.
    \item Multiplexed refresh must exceed roughly 50--60 Hz per digit/row to avoid flicker.
    \item Common-anode drives segments LOW to light; common-cathode drives HIGH.
    \end{itemize}"""),
   ("Recap: Interfacing Concepts",
    r"""\begin{itemize}
    \item Parallel: more pins, faster per transfer. Serial (SPI/I2C): fewer pins, bit-by-bit.
    \item Decoder/driver ICs (e.g.\ BCD-to-7-segment) offload translation from CPU software.
    \item Fan-out and logic-level matching must be checked whenever two different-family
    chips are connected directly.
    \end{itemize}"""),
   ("Integration Example: Full Design Trace",
    r"""Select a decoder IC and interface it to a seven-segment display driven by a microcomputer:
    \begin{enumerate}
    \item Choose a CMOS BCD-to-7-segment decoder for low static power (Meetings 10--11).
    \item Check its datasheet: supply range, $V_{OH}/V_{OL}$, and output drive current
    against the display's segment current requirement (Meetings 12--13).
    \item Compute the LED series resistor for each segment from $V_{supply}$, $V_{LED}$,
    and target $I_{LED}$ (Meeting 14).
    \item Decide common-anode or common-cathode wiring to match the decoder's output polarity.
    \item If driving multiple digits, add multiplexing logic and a refresh loop in software
    or via a multiplex controller IC (Meetings 15--16).
    \end{enumerate}
    This single design touches every topic from Meetings 10--16."""),
   ("Cross-Topic Pitfalls",
    r"""\begin{itemize}
    \item Selecting a chip for its logic function while forgetting to check current/voltage compatibility.
    \item Forgetting the LED resistor calculation when moving from theory to a real circuit.
    \item Mismatching common-anode/common-cathode wiring to the driver's output polarity.
    \item Underestimating multiplex refresh rate, causing visible flicker.
    \end{itemize}"""),
   ("Final Exam Strategy",
    r"""\begin{itemize}
    \item Justify every component choice with specific datasheet numbers, not just "it should work."
    \item Track logic levels carefully whenever a question mixes TTL and CMOS parts.
    \item Show the LED resistor formula and refresh-rate reasoning explicitly -- partial
    credit rewards visible working.
    \item Draw a block diagram first for any multi-stage interfacing question.
    \end{itemize}"""),
   ("Practice 1 -- Problem",
    r"Select and justify a decoder IC family (TTL or CMOS) for a battery-powered, low-power seven-segment display design."),
   ("Practice 1 -- Solution",
    r"""CMOS is the better choice: its very low static power consumption directly extends
    battery life compared to TTL, which draws continuous current even when idle -- a
    decisive factor whenever power budget matters."""),
   ("Practice 2 -- Problem",
    r"Compute the series resistor for a common-cathode seven-segment display's segments, using $V_{supply}=5$V, $V_{LED}=2.1$V, and a target $I_{LED}=12$mA. Also state a plausible refresh rate if 4 digits are multiplexed."),
   ("Practice 2 -- Solution",
    r"""$R=(5-2.1)/0.012 \approx 242\,\Omega$ (nearest standard value $\approx240\,\Omega$ or $270\,\Omega$).
    \\For 4 multiplexed digits to each appear flicker-free at $\geq$60 Hz per digit, the
    full 4-digit cycle should repeat at $\geq 4\times60=240$ Hz, i.e.\ each digit is lit
    for at most about $1/240\text{s}\approx4.2$ms per cycle."""),
   ("Practice 3 -- Problem",
    r"Draw/describe the microcomputer-to-display interface block diagram for a 4-digit multiplexed seven-segment readout."),
   ("Practice 3 -- Solution",
    r"""Microcomputer $\to$ (parallel or serial bus) $\to$ BCD-to-7-segment decoder
    $\to$ current-limiting resistors $\to$ 7-segment display segments;
    separately, microcomputer $\to$ digit-select lines $\to$ transistor drivers $\to$
    each digit's common anode/cathode, cycled in sync with the segment pattern output."""),
   ("Practice 4 -- Problem",
    r"A design uses a TTL decoder ($V_{OH,min}=2.4$V) to drive a CMOS-based multiplex controller ($V_{IH,min}=3.5$V), and the display flickers erratically at only some digit positions. Diagnose the likely cause."),
   ("Practice 4 -- Solution",
    r"""The TTL decoder's guaranteed HIGH output ($2.4$V) is below the CMOS controller's
    required HIGH input threshold ($3.5$V) -- an interfacing mismatch from Meeting 11.
    \\Depending on exact voltage margins and noise, some transitions may be read correctly
    and others not, producing intermittent, position-dependent flicker rather than a
    complete, consistent failure. Fix: add a pull-up resistor or a proper level-shifting buffer.""")],
  I("Meetings 10--16 combine IC selection with display interfacing.",
    "Datasheet numbers justify component choices.",
    "Block diagrams and resistor/timing math structure answers."),
  I("Select and justify a decoder IC for a seven-segment display.",
    "Compute the series resistor and a plausible refresh rate.",
    "Draw the microcomputer-to-display interface block diagram."))

if __name__ == "__main__":
    order = [1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17]
    for n in order:
        title, subclo, ind, slides, summ, asg = M[n]
        tex = build_deck(COURSE, SUBJECT, SUBTITLE, REF, CLO, n, title, subclo, ind, slides, summ, asg)
        print(compile_meeting(COURSE, n, tex), flush=True)
    print("DONE", COURSE)
