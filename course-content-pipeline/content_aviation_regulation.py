#!/usr/bin/env python3
"""Aviation_Regulation (curriculum §2) — meetings 1-8. Build via build_slides."""
from build_slides import build_deck, compile_meeting

COURSE   = "Aviation_Regulation"
SUBJECT  = "AVIATION REGULATION"
SUBTITLE = "International and National Aviation Law for Maintenance Personnel"
REF      = "Chicago Convention on International Civil Aviation (1944) and Annexes; Civil Aviation Safety Regulations (CASR) Part 21/43/65/91, DGCA Indonesia"
CLO = [
 "Explain the framework of international and national aviation law as the basis of regulatory compliance.",
 "Explain airworthiness requirements and CASR Part 21, 43, 65, and 91 provisions.",
 "Explain air transport operations, operator organization and management, and operator economics related to maintenance.",
 "Explain Approved Maintenance Organization (AMO) requirements and aircraft maintenance personnel licensing.",
 "Explain the role of the state aviation regulatory body and the certification/documentation process.",
]

I = lambda *xs: list(xs)
M = {}

# ---------------- Meeting 1 ----------------
M[1] = ("International and State Aviation Laws",
  "Students are able to explain international and state aviation law (ICAO, aviation law, CASR framework).",
  I("Explain the purpose and structure of the Chicago Convention and ICAO Annexes.",
    "Identify the 'five freedoms of the air' and state sovereignty over airspace.",
    "Explain how Indonesia's national aviation law (UU Penerbangan) implements ICAO standards through CASR."),
  [("Why Aviation Needs International Law",
    r"""Aircraft routinely cross national borders in minutes, so aviation safety and
    airspace sovereignty cannot rely on a single country's rules alone.
    \begin{itemize}
    \item International law creates \textbf{common minimum standards} every member state agrees to.
    \item National law (CASR in Indonesia) then implements those standards locally and adds
    country-specific requirements.
    \end{itemize}"""),
   ("The Chicago Convention (1944)",
    r"""Signed in Chicago in 1944 by 52 states, the \textbf{Convention on International Civil
    Aviation} is the foundational treaty of civil aviation.
    \begin{itemize}
    \item Created \textbf{ICAO} (International Civil Aviation Organization), a UN specialized agency.
    \item Established the principle that every state has \textbf{complete and exclusive
    sovereignty} over the airspace above its territory (Article 1).
    \item Created a framework of 19 Annexes covering technical standards (licensing,
    airworthiness, operations, accident investigation, etc.).
    \end{itemize}"""),
   ("ICAO Structure and Annexes",
    r"""\begin{center}
    \begin{tikzpicture}[>={Latex},node distance=0.5cm]
      \node[draw,fill=blue!10,rounded corners] (icao) {ICAO (UN agency, Montreal)};
      \node[draw,fill=orange!15,rounded corners,below left=0.9cm and 1.0cm of icao] (sarps) {SARPs (Annexes 1--19)};
      \node[draw,fill=orange!15,rounded corners,below right=0.9cm and 1.0cm of icao] (states) {Contracting States (193)};
      \draw[->,thick] (icao) -- (sarps);
      \draw[->,thick] (icao) -- (states);
      \node[draw,fill=green!15,rounded corners,below=0.9cm of states] (casr) {National regulation (e.g.\ CASR, Indonesia)};
      \draw[->,thick] (states) -- (casr);
    \end{tikzpicture}
    \end{center}
    ICAO issues \textbf{Standards and Recommended Practices (SARPs)}; each state then
    adopts them into binding national regulation."""),
   ("Key ICAO Annexes for Maintenance Personnel",
    r"""\begin{center}\renewcommand{\arraystretch}{1.3}
    \begin{tabular}{|l|p{7cm}|}\hline
    \textbf{Annex} & \textbf{Subject}\\\hline
    Annex 1 & Personnel Licensing\\
    Annex 6 & Operation of Aircraft\\
    Annex 8 & Airworthiness of Aircraft\\
    Annex 13 & Aircraft Accident and Incident Investigation\\
    Annex 19 & Safety Management\\\hline
    \end{tabular}\end{center}"""),
   ("Airspace Sovereignty and the Five Freedoms",
    r"""Each state controls its own airspace, but international air transport needs
    negotiated traffic rights, commonly summarized as the \textbf{Freedoms of the Air}:
    \begin{enumerate}
    \item Fly across a state's territory without landing.
    \item Land for non-traffic purposes (e.g.\ refueling).
    \item Carry traffic from home state to the foreign state.
    \item Carry traffic from the foreign state back to the home state.
    \item Carry traffic between two foreign states on a route that starts/ends at home.
    \end{enumerate}
    These freedoms are granted through \textbf{bilateral or multilateral air services
    agreements}, not automatically by the Chicago Convention."""),
   ("From International Standard to National Rule",
    r"""\begin{itemize}
    \item \textbf{UU No.\ 1 Tahun 2009} tentang Penerbangan is Indonesia's primary aviation law,
    establishing the legal authority of the Directorate General of Civil Aviation (DGCA/Ditjen Hubud).
    \item \textbf{CASR (Civil Aviation Safety Regulations)} are Indonesia's detailed technical
    regulations, modeled closely on ICAO Annexes and (for many parts) the US FARs.
    \item Where ICAO SARPs and national CASR differ, a state must file a \textbf{difference}
    with ICAO -- transparency is required, not automatic compliance.
    \end{itemize}"""),
   ("Why This Matters for a Maintenance Technician",
    r"""\begin{itemize}
    \item Your license (CASR 65) and your organization's approval (CASR 145/AMO) both trace
    their legal authority back through national law to the Chicago Convention framework.
    \item An aircraft maintained in Indonesia under CASR, but operated into another ICAO
    member state, is recognized internationally \emph{because} both states implement
    the same ICAO baseline.
    \item This is why CASR part numbers in this course closely parallel the international
    Annex structure -- they are not arbitrary.
    \end{itemize}"""),
   ("Practice 1 -- Problem",
    r"Explain the relationship between ICAO SARPs and Indonesia's CASR."),
   ("Practice 1 -- Solution",
    r"""ICAO issues Standards and Recommended Practices (SARPs) through its Annexes as a
    minimum global baseline. Indonesia, as a contracting state, implements these SARPs into
    binding domestic regulation (CASR), adapted to its national legal system (UU Penerbangan)
    and operational context. Any deviation must be filed with ICAO as a difference."""),
   ("Practice 2 -- Problem",
    r"Which Freedom of the Air allows an airline to carry passengers from its home country directly into a foreign country?"),
   ("Practice 2 -- Solution",
    r"""The \textbf{Third Freedom} -- the right to carry traffic from the home state to the
    foreign (treaty) state."""),
  ],
  I("The Chicago Convention (1944) created ICAO and the Annex system of SARPs.",
    "States hold sovereignty over their airspace; traffic rights are negotiated separately.",
    "Indonesia implements ICAO standards through UU Penerbangan and CASR."),
  I("Identify which ICAO Annex covers a given regulatory topic (five examples).",
    "Explain the five freedoms of the air with one example each.",
    "Trace the legal chain from ICAO Annex 8 to a specific CASR part."))

# ---------------- Meeting 2 ----------------
M[2] = ("Airworthiness Requirements",
  "Students are able to explain airworthiness requirements.",
  I("Define airworthiness and distinguish type certification from continuing airworthiness.",
    "Explain the role of Airworthiness Directives (AD) and Service Bulletins (SB).",
    "Explain the Minimum Equipment List (MEL) and its operational effect."),
  [("What Does 'Airworthy' Mean?",
    r"""An aircraft is \textbf{airworthy} when it conforms to its approved type design and is
    in a condition for safe operation.
    \begin{itemize}
    \item Two conditions must both be true: \textbf{conformity} (built/maintained as designed)
    and \textbf{condition for safe operation} (no defect that compromises safety).
    \item Airworthiness is not a one-time event -- it must be \textbf{continuously} maintained
    throughout the aircraft's operational life.
    \end{itemize}"""),
   ("Two Pillars of Airworthiness",
    r"""\begin{center}
    \begin{tikzpicture}[>={Latex},node distance=1.2cm]
      \node[draw,fill=blue!10,rounded corners,text width=5cm,align=center] (a)
        {\textbf{Initial / Type Airworthiness}\\design approval, type certificate, production certificate};
      \node[draw,fill=orange!15,rounded corners,text width=5cm,align=center,right=1.2cm of a] (b)
        {\textbf{Continuing Airworthiness}\\maintenance, inspections, AD compliance, CofA renewal};
      \draw[->,thick] (a) -- node[above,font=\footnotesize]{aircraft enters service} (b);
    \end{tikzpicture}
    \end{center}
    This course (and CASR Part 43/91) focuses mainly on the second pillar -- keeping an
    already-certificated aircraft airworthy over its lifetime."""),
   ("Airworthiness Directives (AD)",
    r"""An \textbf{Airworthiness Directive} is a legally enforceable regulation issued by the
    state of design (or validated by the state of registry) when an unsafe condition is found
    in a type design.
    \begin{itemize}
    \item ADs are \textbf{mandatory} -- compliance is not optional, unlike a Service Bulletin.
    \item Each AD specifies the unsafe condition, the required action, and a
    \textbf{compliance time} (a specific date, flight-hour limit, or cycle limit).
    \item Non-compliance with an applicable AD makes the aircraft \textbf{not airworthy}.
    \end{itemize}"""),
   ("AD vs. Service Bulletin (SB)",
    r"""\begin{center}\renewcommand{\arraystretch}{1.3}
    \begin{tabular}{|l|p{4.4cm}|p{4.4cm}|}\hline
    & \textbf{Airworthiness Directive} & \textbf{Service Bulletin}\\\hline
    Issued by & State regulator (e.g.\ FAA, EASA, DGCA) & Manufacturer\\
    Mandatory? & Yes, legally binding & No, unless referenced/mandated by an AD\\
    Purpose & Correct an unsafe condition & Recommend improvement or inform of an issue\\\hline
    \end{tabular}\end{center}
    An AD sometimes \emph{mandates} compliance with a specific SB -- at that point the SB's
    actions become legally required."""),
   ("Minimum Equipment List (MEL)",
    r"""The \textbf{MEL} lists equipment that may be \emph{inoperative} for a flight while
    still maintaining an acceptable level of safety, under specified conditions.
    \begin{itemize}
    \item Derived from the \textbf{Master Minimum Equipment List (MMEL)} issued by the
    manufacturer/state of design, then tailored by the operator for its own CASR 121/135 operations.
    \item An inoperative item under MEL must be \textbf{placarded} and usually has an
    operational or maintenance limitation (e.g.\ ``repair within 3 days -- Category B'').
    \item The MEL does \emph{not} override airworthiness; it defines a controlled condition
    under which dispatch remains legal.
    \end{itemize}"""),
   ("MEL Categories (Repair Interval Example)",
    r"""\begin{center}\renewcommand{\arraystretch}{1.3}
    \begin{tabular}{|c|l|}\hline
    \textbf{Category} & \textbf{Typical max.\ repair interval}\\\hline
    A & As specified in the remarks column (no fixed interval)\\
    B & 3 consecutive calendar days\\
    C & 10 consecutive calendar days\\
    D & 120 consecutive calendar days\\\hline
    \end{tabular}\end{center}
    Deferring a defect under the MEL still \textbf{starts a clock} -- it is a controlled,
    time-limited exception, not a permanent waiver."""),
   ("Certificate of Airworthiness (Preview)",
    r"""A \textbf{Certificate of Airworthiness (C of A)} is the document that formally
    confirms an aircraft meets its approved design and is maintained in a condition for
    safe operation.
    \begin{itemize}
    \item Issued initially at type-design compliance, then kept valid through continuing
    airworthiness management (scheduled maintenance, AD compliance, defect rectification).
    \item Detailed issuance procedure is covered later in this course (Meeting 11).
    \end{itemize}"""),
   ("Practice 1 -- Problem",
    r"Explain why compliance with an Airworthiness Directive is mandatory while compliance with a Service Bulletin is usually not."),
   ("Practice 1 -- Solution",
    r"""An AD is issued by the state regulator as a legally binding correction for a
    confirmed unsafe condition -- it carries the force of law. A Service Bulletin is issued
    by the manufacturer as a recommendation and is only mandatory if an AD specifically
    references and requires it."""),
   ("Practice 2 -- Problem",
    r"An aircraft has an inoperative MEL Category C item. What does this mean operationally?"),
   ("Practice 2 -- Solution",
    r"""The item may remain inoperative for up to \textbf{10 consecutive calendar days}
    under the conditions/placards specified in the MEL, after which it must be repaired or
    the dispatch relief no longer applies."""),
  ],
  I("Airworthiness requires both design conformity and safe operating condition, maintained continuously.",
    "Airworthiness Directives are mandatory; Service Bulletins are not, unless mandated by an AD.",
    "The MEL permits time-limited dispatch with specified inoperative equipment."),
  I("Compare an AD and an SB for the same hypothetical defect.",
    "Explain MEL categories A-D and their repair intervals.",
    "Explain what makes an aircraft 'not airworthy' despite having a valid C of A."))

# ---------------- Meeting 3 ----------------
M[3] = ("CASR Part 21, 43, 65, and 91",
  "Students are able to explain the provisions of CASR Part 21, 43, 65, and 91.",
  I("Explain the scope of CASR Part 21 (certification procedures).",
    "Explain the scope of CASR Part 43 (maintenance, rebuilding, alteration).",
    "Explain the scope of CASR Part 65 (certification of airmen other than flight crew) and Part 91 (general operating rules)."),
  [("CASR: Indonesia's Technical Rulebook",
    r"""\textbf{Civil Aviation Safety Regulations (CASR)} are Indonesia's detailed
    airworthiness and operational regulations, issued by the Minister of Transportation /
    DGCA under the authority of UU No.\ 1/2009. Each \textbf{Part} covers one regulatory domain,
    paralleling the structure of the US FARs and ICAO Annexes."""),
   ("Four Parts Covered This Meeting",
    r"""\begin{center}
    \begin{tikzpicture}[>={Latex},node distance=0.5cm]
      \node[draw,fill=blue!10,rounded corners,text width=2.6cm,align=center] (p21) {\textbf{Part 21}\\Certification Procedures};
      \node[draw,fill=orange!15,rounded corners,text width=2.6cm,align=center,right=0.4cm of p21] (p43) {\textbf{Part 43}\\Maintenance};
      \node[draw,fill=green!15,rounded corners,text width=2.6cm,align=center,right=0.4cm of p43] (p65) {\textbf{Part 65}\\Airmen Certification};
      \node[draw,fill=yellow!20,rounded corners,text width=2.6cm,align=center,right=0.4cm of p65] (p91) {\textbf{Part 91}\\General Operating Rules};
    \end{tikzpicture}
    \end{center}
    Together they cover \emph{how an aircraft design is approved}, \emph{how it is
    maintained}, \emph{who may perform/approve that maintenance}, and \emph{how the
    aircraft may be operated}."""),
   ("CASR Part 21 -- Certification Procedures for Products and Parts",
    r"""\begin{itemize}
    \item Governs issuance of \textbf{Type Certificates (TC)}, \textbf{Production
    Certificates (PC)}, and \textbf{Certificates of Airworthiness (C of A)}.
    \item Defines approval routes for parts: \textbf{Parts Manufacturer Approval (PMA)},
    \textbf{Technical Standard Order (TSO)} authorization.
    \item Establishes \textbf{Supplemental Type Certificates (STC)} for approved
    modifications to an existing type design.
    \item Relevance to maintenance: any replacement part must trace to an approved source
    (TC holder, PMA, or approved STC) to remain airworthy.
    \end{itemize}"""),
   ("CASR Part 43 -- Maintenance, Preventive Maintenance, Rebuilding, and Alteration",
    r"""\begin{itemize}
    \item Defines what counts as \textbf{maintenance}, \textbf{preventive maintenance},
    \textbf{rebuilding}, and \textbf{alteration} -- each has different authorization requirements.
    \item Requires maintenance to be performed using \textbf{current data} (AMM, SB, AD) and
    recorded accurately (Appendix-style recordkeeping requirements).
    \item Defines \textbf{major repairs/alterations} vs.\ \textbf{minor} -- majors need
    specific approved data and additional documentation (e.g.\ Form 337-equivalent).
    \item This Part is the direct legal basis for the maintenance recordkeeping and
    AMM-following practices discussed in Technical English Meeting 8.
    \end{itemize}"""),
   ("CASR Part 65 -- Certification: Airmen Other Than Flight Crew Members",
    r"""\begin{itemize}
    \item Covers licensing for \textbf{Aircraft Maintenance Engineers (AME)}, repairmen,
    dispatchers, and other non-flight-crew certificated personnel.
    \item Specifies \textbf{eligibility} (age, experience, training), \textbf{knowledge and
    practical tests}, and \textbf{privileges and limitations} of each license rating
    (airframe, powerplant, avionics ratings).
    \item Requires \textbf{recency of experience} to exercise license privileges --
    a license alone does not permit signing off work indefinitely without staying current.
    \item This Part is the direct legal basis of the AME license this course prepares students for.
    \end{itemize}"""),
   ("CASR Part 91 -- General Operating and Flight Rules",
    r"""\begin{itemize}
    \item Baseline operating rules applicable to \textbf{all} civil aircraft in Indonesian
    airspace (unless superseded by more specific parts for commercial operators, e.g.\ Part 121/135).
    \item Covers \textbf{pilot-in-command responsibility}, airworthiness/documents to be
    carried on board, \textbf{inspection intervals} (annual/100-hour style requirements),
    and the operator's duty to comply with ADs and MEL conditions.
    \item Relevance to maintenance: Part 91 is where the \emph{operational consequence} of a
    maintenance decision (e.g.\ MEL deferral) actually takes legal effect for the flight.
    \end{itemize}"""),
   ("How the Four Parts Interact",
    r"""\begin{center}
    \begin{tikzpicture}[>={Latex},node distance=0.9cm]
      \node[draw,fill=blue!10,rounded corners] (p21) {Part 21: design/part approved};
      \node[draw,fill=orange!15,rounded corners,below=of p21] (p43) {Part 43: maintenance performed \& recorded};
      \node[draw,fill=green!15,rounded corners,below=of p43] (p65) {Part 65: performed/approved by a licensed AME};
      \node[draw,fill=yellow!20,rounded corners,below=of p65] (p91) {Part 91: aircraft legally operated};
      \draw[->,thick] (p21)--(p43); \draw[->,thick] (p43)--(p65); \draw[->,thick] (p65)--(p91);
    \end{tikzpicture}
    \end{center}
    A single maintenance action touches all four parts: the part used must be Part-21-approved,
    the work must follow Part 43, be certified by a Part-65 license holder, before the
    aircraft can legally fly under Part 91."""),
   ("Practice 1 -- Problem",
    r"A technician installs a replacement part on an aircraft. Which CASR Part governs whether that part is an approved source?"),
   ("Practice 1 -- Solution",
    r"""\textbf{Part 21} -- it governs certification of products and parts (TC, PMA, TSO,
    STC), establishing which sources are legally approved for installation."""),
   ("Practice 2 -- Problem",
    r"Distinguish the role of Part 43 from Part 65 using the maintenance sign-off process."),
   ("Practice 2 -- Solution",
    r"""Part 43 defines \emph{what} counts as maintenance/alteration and how it must be
    performed and recorded. Part 65 defines \emph{who} is legally certificated (licensed) to
    perform or approve that work. Part 43 is about the task; Part 65 is about the person."""),
  ],
  I("Part 21 governs design/part approval; Part 43 governs maintenance performance and recording.",
    "Part 65 governs who may perform/certify maintenance; Part 91 governs general operation.",
    "A single maintenance action must satisfy all four parts to keep the aircraft legally airworthy and operable."),
  I("Map five maintenance scenarios to the correct CASR Part.",
    "Explain major vs. minor alteration under Part 43 with one example each.",
    "Explain one privilege and one limitation of a Part 65 AME license."))

# ---------------- Meeting 4 ----------------
M[4] = ("Air Transport Operations",
  "Students are able to explain air transport operations.",
  I("Distinguish scheduled, non-scheduled, and cargo air transport operations.",
    "Explain the Air Operator Certificate (AOC) process and its relationship to maintenance.",
    "Explain operational control and the role of maintenance in dispatch reliability."),
  [("What Is 'Air Transport Operation'?",
    r"""An \textbf{air transport operation} is the commercial carriage of passengers, cargo,
    or mail by air for remuneration -- distinct from private/general aviation flying.
    \begin{itemize}
    \item Regulated in Indonesia primarily under \textbf{CASR Part 121} (scheduled/large
    aircraft) and \textbf{Part 135} (non-scheduled/smaller aircraft commuter and on-demand).
    \item Operators must hold an \textbf{Air Operator Certificate (AOC)} before conducting
    commercial operations.
    \end{itemize}"""),
   ("Categories of Air Transport Operations",
    r"""\begin{center}\renewcommand{\arraystretch}{1.3}
    \begin{tabular}{|l|p{7cm}|}\hline
    \textbf{Category} & \textbf{Description}\\\hline
    Scheduled & Fixed routes/timetables published in advance, open to the public (Part 121/135)\\
    Non-scheduled (charter) & On-demand flights, not on a fixed public timetable\\
    Cargo-only & Carriage of freight/mail, no passengers\\
    General aviation & Non-commercial; outside AOC/Part 121/135 scope\\\hline
    \end{tabular}\end{center}"""),
   ("The Air Operator Certificate (AOC)",
    r"""An \textbf{AOC} is issued by the DGCA after the operator demonstrates the
    organization, personnel, equipment, and procedures to conduct safe commercial operations.
    \begin{itemize}
    \item Requires an approved \textbf{Operations Manual} and (for maintenance) a
    \textbf{Continuing Airworthiness Maintenance Program (CAMP)} or equivalent.
    \item Requires the operator to have, or contract, an \textbf{Approved Maintenance
    Organization (AMO)} to perform required maintenance (covered in Meeting 7).
    \item An AOC specifies the aircraft types, routes/areas of operation, and the kinds
    of operation (e.g.\ day/night, IFR) the operator is authorized for.
    \end{itemize}"""),
   ("AOC Certification Process (Five Phases)",
    r"""\begin{center}
    \begin{tikzpicture}[>={Latex},node distance=0.35cm]
      \node[draw,fill=blue!10,rounded corners,text width=2.3cm,align=center] (p1) {1.\ Pre-application};
      \node[draw,fill=orange!15,rounded corners,text width=2.3cm,align=center,right=0.3cm of p1] (p2) {2.\ Formal application};
      \node[draw,fill=green!15,rounded corners,text width=2.3cm,align=center,right=0.3cm of p2] (p3) {3.\ Document evaluation};
      \node[draw,fill=yellow!20,rounded corners,text width=2.3cm,align=center,right=0.3cm of p3] (p4) {4.\ Demonstration \& inspection};
      \node[draw,fill=red!15,rounded corners,text width=2.3cm,align=center,right=0.3cm of p4] (p5) {5.\ Certification};
    \end{tikzpicture}
    \end{center}
    Phase 4 includes proving-flights and verifying the maintenance system actually works as
    documented, not just that the manuals exist."""),
   ("Operational Control and Dispatch",
    r"""\textbf{Operational control} is the authority to initiate, continue, divert, or
    terminate a flight -- it belongs to the operator (shared between PIC and a dispatcher
    for large operators).
    \begin{itemize}
    \item Before dispatch, the aircraft's airworthiness status (open defects, MEL items, AD
    compliance) must be confirmed current -- this is where maintenance and operations meet directly.
    \item A \textbf{technical/dispatch release} typically must be signed by maintenance
    personnel confirming the aircraft is airworthy for the flight.
    \end{itemize}"""),
   ("Maintenance's Role in Dispatch Reliability",
    r"""\begin{itemize}
    \item \textbf{Dispatch reliability} measures the percentage of flights departing without
    a technical delay or cancellation -- a key operator performance and economic metric.
    \item Line maintenance (transit checks, defect rectification, MEL management) directly
    determines whether an aircraft is ready at its scheduled departure time.
    \item Poor maintenance planning (e.g.\ unresolved recurring defects) degrades dispatch
    reliability and increases cost -- connecting this meeting to Meeting 6 (operator economics).
    \end{itemize}"""),
   ("Practice 1 -- Problem",
    r"Explain the difference between scheduled and non-scheduled air transport operations, with one Indonesian regulatory reference each."),
   ("Practice 1 -- Solution",
    r"""Scheduled operations run on a published timetable, open to the public, typically
    conducted by larger operators under \textbf{CASR Part 121}. Non-scheduled (charter)
    operations are on-demand, not on a fixed public timetable, typically conducted under
    \textbf{CASR Part 135} for smaller aircraft/commuter operations."""),
   ("Practice 2 -- Problem",
    r"What must an operator demonstrate before an AOC is issued, specifically regarding maintenance?"),
   ("Practice 2 -- Solution",
    r"""The operator must demonstrate an approved Continuing Airworthiness Maintenance
    Program (or equivalent) and access to an Approved Maintenance Organization (AMO) capable
    of performing the required maintenance for its aircraft types."""),
  ],
  I("Air transport operations are classified as scheduled, non-scheduled, or cargo under Part 121/135.",
    "An AOC requires proof of organization, personnel, procedures, and a working maintenance system.",
    "Maintenance readiness directly determines dispatch reliability, linking operations and maintenance economics."),
  I("Classify three example flights as scheduled, non-scheduled, or cargo.",
    "List the five phases of AOC certification in order.",
    "Explain why a dispatch/technical release requires a maintenance signature."))

# ---------------- Meeting 5 ----------------
M[5] = ("Organization and Management of the Operator",
  "Students are able to explain organization and management of a flight operator.",
  I("Explain the required management positions (Accountable Manager, Nominated Post Holders) under CASR.",
    "Explain the Safety Management System (SMS) as part of operator organization.",
    "Explain the relationship between the Quality/Compliance Monitoring function and maintenance."),
  [("Why Regulators Require a Defined Organization",
    r"""Safety accountability must be traceable to a named individual, not diffused across a
    company. CASR (following ICAO Annex 19/6) requires operators to define a management
    structure with clear, named responsibilities before an AOC is granted."""),
   ("The Accountable Manager",
    r"""\begin{itemize}
    \item The \textbf{Accountable Manager} is the single individual with \emph{corporate
    authority} for ensuring all operations can be financed and carried out to the standard
    required by the regulator -- typically the CEO/Managing Director.
    \item Legally answerable to the DGCA for the operator's compliance, even though day-to-day
    technical decisions are delegated to post holders.
    \item Must ensure adequate resources (budget, staffing, facilities) are available --
    compliance cannot be claimed as "unaffordable" after the fact.
    \end{itemize}"""),
   ("Nominated Post Holders (Typical Structure)",
    r"""\begin{center}
    \begin{tikzpicture}[>={Latex},node distance=0.5cm]
      \node[draw,fill=blue!10,rounded corners] (am) {Accountable Manager};
      \node[draw,fill=orange!15,rounded corners,below left=0.8cm and 2.6cm of am] (ops) {Post Holder: Flight Operations};
      \node[draw,fill=green!15,rounded corners,below=0.8cm of am] (maint) {Post Holder: Maintenance};
      \node[draw,fill=yellow!20,rounded corners,below right=0.8cm and 2.6cm of am] (crew) {Post Holder: Crew Training};
      \draw[->,thick] (am)--(ops); \draw[->,thick] (am)--(maint); \draw[->,thick] (am)--(crew);
    \end{tikzpicture}
    \end{center}
    The \textbf{Post Holder: Maintenance} is specifically responsible for ensuring aircraft
    are maintained to an airworthy standard -- this role interfaces directly with the AMO (Meeting 7)."""),
   ("Safety Management System (SMS)",
    r"""An \textbf{SMS} is a systematic approach to managing safety: policy, risk management,
    assurance, and promotion (the ICAO Annex 19 "four pillars").
    \begin{itemize}
    \item \textbf{Safety policy \& objectives} -- top management commitment, documented.
    \item \textbf{Safety risk management} -- hazard identification, risk assessment/mitigation.
    \item \textbf{Safety assurance} -- monitoring performance, internal audits, corrective action.
    \item \textbf{Safety promotion} -- training and communication of safety information.
    \end{itemize}
    Maintenance defects and occurrences feed directly into the SMS hazard/risk process."""),
   ("Quality / Compliance Monitoring Function",
    r"""\begin{itemize}
    \item A \textbf{Quality (Compliance Monitoring) System} independently audits whether
    the operator actually follows its own approved manuals and the applicable CASR.
    \item Distinct from SMS: SMS manages \emph{safety risk}; Quality/Compliance Monitoring
    verifies \emph{regulatory and procedural compliance}. The two work together but answer
    different questions.
    \item Audit findings against maintenance procedures (e.g.\ incomplete logbook entries,
    expired tool calibration) must be tracked to closure -- this is the internal check before
    the DGCA's external audit.
    \end{itemize}"""),
   ("How This Organization Protects Maintenance Quality",
    r"""\begin{itemize}
    \item Clear post-holder accountability prevents maintenance decisions from being overridden
    by commercial pressure without an accountable, named decision-maker.
    \item SMS ensures recurring technical defects are analyzed for systemic causes, not just
    individually rectified.
    \item Compliance monitoring provides the evidence trail the DGCA expects during
    AOC/AMO renewal audits.
    \end{itemize}"""),
   ("Practice 1 -- Problem",
    r"Explain the difference between the Accountable Manager and the Post Holder: Maintenance."),
   ("Practice 1 -- Solution",
    r"""The Accountable Manager holds overall corporate authority and legal answerability to
    the regulator for the whole operation, including ensuring resources are available. The
    Post Holder: Maintenance is the nominated individual specifically responsible for the
    day-to-day airworthiness and maintenance standard of the fleet, reporting within that structure."""),
   ("Practice 2 -- Problem",
    r"Distinguish the purpose of SMS from Quality/Compliance Monitoring."),
   ("Practice 2 -- Solution",
    r"""SMS proactively manages safety \emph{risk} (identifying hazards and mitigating them
    before harm occurs). Quality/Compliance Monitoring independently verifies that the
    operator is actually following its approved procedures and the applicable regulations --
    a compliance check, not primarily a risk-prediction tool."""),
  ],
  I("CASR requires a named Accountable Manager and nominated post holders for key functions.",
    "SMS manages safety risk through policy, risk management, assurance, and promotion.",
    "Quality/Compliance Monitoring independently verifies regulatory and procedural compliance."),
  I("Draw the post-holder organization chart for a hypothetical small operator.",
    "List the four pillars of SMS with one maintenance-related example each.",
    "Explain one difference between SMS and Quality/Compliance Monitoring."))

# ---------------- Meeting 6 ----------------
M[6] = ("Operator Economics Related to Maintenance",
  "Students are able to explain aspects of operator economics related to maintenance.",
  I("Explain direct and indirect maintenance costs.",
    "Explain how maintenance decisions affect dispatch reliability and operating cost.",
    "Explain the trade-off between scheduled (preventive) maintenance cost and unscheduled (corrective) maintenance cost."),
  [("Maintenance as a Cost Center -- and a Safety Requirement",
    r"""Maintenance is simultaneously a \textbf{regulatory obligation} (airworthiness, Meeting
    2-3) and one of an airline's \textbf{largest controllable operating costs}, typically
    10-20\% of total direct operating cost. Economics does not override airworthiness, but
    understanding cost structure explains real-world maintenance planning decisions."""),
   ("Direct Maintenance Cost (DMC)",
    r"""\begin{itemize}
    \item \textbf{Labor} -- technician hours (line, base, shop maintenance).
    \item \textbf{Material} -- consumables, rotable/repairable spare parts, consignment stock.
    \item \textbf{Maintenance-related overhead} -- tooling, facilities, MRO contract fees.
    \end{itemize}
    DMC is usually expressed per flight hour or per flight cycle to allow comparison
    across fleet types and airlines."""),
   ("Indirect Costs of Poor Maintenance",
    r"""\begin{center}
    \begin{tikzpicture}[>={Latex},node distance=0.5cm]
      \node[draw,fill=blue!10,rounded corners] (defect) {Unresolved recurring defect};
      \node[draw,fill=orange!15,rounded corners,below=of defect] (delay) {Technical delay / cancellation};
      \node[draw,fill=green!15,rounded corners,below=of delay] (cost) {Passenger compensation, crew/aircraft repositioning, lost revenue};
      \draw[->,thick] (defect)--(delay); \draw[->,thick] (delay)--(cost);
    \end{tikzpicture}
    \end{center}
    Indirect costs from a single significant delay or cancellation can exceed the direct
    repair cost many times over -- this is why dispatch reliability (Meeting 4) is tracked
    as a financial metric, not only an operational one."""),
   ("Scheduled vs. Unscheduled Maintenance Cost Trade-off",
    r"""\begin{center}\renewcommand{\arraystretch}{1.3}
    \begin{tabular}{|l|p{4.6cm}|p{4.4cm}|}\hline
    & \textbf{Scheduled (preventive)} & \textbf{Unscheduled (corrective)}\\\hline
    Timing & Planned, predictable & Reactive, unpredictable\\
    Direct cost & Generally lower per event & Often higher per event (urgency, parts expediting)\\
    Indirect cost & Minimal (planned downtime) & High (delay, cancellation, AOG)\\\hline
    \end{tabular}\end{center}
    Over-maintaining wastes resources; under-maintaining shifts cost from planned to
    unplanned (usually at a higher total cost) -- the maintenance program (Meeting 2's CAMP)
    is designed to find the economic and safety optimum."""),
   ("Aircraft on Ground (AOG)",
    r"""\textbf{AOG} status means an aircraft cannot be legally dispatched until a specific
    defect is resolved -- the most economically severe maintenance event.
    \begin{itemize}
    \item Triggers expedited parts shipping, overtime labor, possible aircraft swaps, and
    schedule disruption across the network, not just the single flight.
    \item A well-run maintenance program (MEL use where legal, spares pooling, predictive
    maintenance) reduces AOG frequency without compromising airworthiness.
    \end{itemize}"""),
   ("Maintenance Cost Levers Technicians Influence Directly",
    r"""\begin{itemize}
    \item Accurate, complete logbook/defect reporting (links to Technical English Meeting 8)
    reduces repeat troubleshooting cost.
    \item Correct first-time fault diagnosis avoids re-opening the same defect (a key driver
    of indirect delay cost).
    \item Proper use of the MEL (Meeting 2) legally defers low-risk defects, protecting
    dispatch reliability without compromising safety.
    \end{itemize}"""),
   ("Practice 1 -- Problem",
    r"Explain why an AOG event is more economically damaging than a routine scheduled check of similar repair scope."),
   ("Practice 1 -- Solution",
    r"""An AOG event is unplanned: it disrupts the flight schedule, often requires
    expedited parts/overtime labor, may force aircraft swaps or passenger compensation, and
    causes lost revenue -- indirect costs the airline did not plan for. A scheduled check of
    similar scope is planned into non-revenue downtime, so it avoids these indirect costs
    even if the direct repair cost is similar."""),
   ("Practice 2 -- Problem",
    r"Give two concrete actions a technician can take that reduce indirect maintenance cost without compromising airworthiness."),
   ("Practice 2 -- Solution",
    r"""(1) Writing precise, complete defect/logbook entries so the next technician does not
    need to re-diagnose the fault from scratch. (2) Correctly applying the MEL to legally
    defer a qualifying low-risk defect rather than causing an unnecessary delay, while
    tracking the repair interval to closure."""),
  ],
  I("Direct maintenance cost (labor, material, overhead) is usually measured per flight hour/cycle.",
    "Indirect costs from delays/cancellations/AOG often exceed direct repair costs.",
    "Scheduled maintenance trades planned, lower-risk cost against unscheduled maintenance's unplanned, higher total cost."),
  I("Classify five cost examples as direct or indirect maintenance cost.",
    "Explain the AOG cost chain from defect to network disruption.",
    "Identify two technician actions that reduce indirect cost without compromising airworthiness."))

# ---------------- Meeting 7 ----------------
M[7] = ("Approved Maintenance Organizations (AMO)",
  "Students are able to explain requirements for an Approved Maintenance Organization (AMO).",
  I("Explain the purpose and approval basis of an AMO under CASR Part 145-equivalent regulation.",
    "Explain the required facilities, personnel, and quality system of an AMO.",
    "Explain the AMO's Certificate of Release to Service (CRS) and its legal significance."),
  [("What Is an AMO and Why It Exists",
    r"""An \textbf{Approved Maintenance Organization (AMO)} is a company specifically
    certificated by the DGCA to perform maintenance, preventive maintenance, and alteration
    on aircraft/components, under its own approved procedures and quality system.
    \begin{itemize}
    \item An individually licensed AME (Part 65) may have personal privileges, but
    commercial/complex maintenance is normally required to be performed \emph{under} an AMO's
    certificate so the \emph{organization}, not just the individual, is accountable.
    \item This parallels ICAO Annex 8/EASA Part-145/FAA Part 145 organizational maintenance approvals.
    \end{itemize}"""),
   ("AMO Approval Requirements -- Overview",
    r"""\begin{center}\renewcommand{\arraystretch}{1.25}
    \begin{tabular}{|l|p{7.2cm}|}\hline
    \textbf{Area} & \textbf{Requirement}\\\hline
    Facilities & Adequate hangar/shop space, environment control, tooling and equipment per approved scope\\
    Personnel & Sufficient qualified staff, including a nominated Quality Manager / accountable manager\\
    Procedures & Approved Maintenance Organization Exposition (MOE) describing the quality system and procedures\\
    Scope of approval & Explicit rating/limitation list: aircraft types, components, and kinds of work authorized\\\hline
    \end{tabular}\end{center}"""),
   ("The Maintenance Organization Exposition (MOE)",
    r"""\begin{itemize}
    \item The \textbf{MOE} is the AMO's master procedures manual, approved by the DGCA, and
    is functionally similar to the Operations Manual for an AOC holder.
    \item Must describe: organizational structure, scope of work, quality system,
    maintenance procedures, personnel qualification requirements, and record-keeping practices.
    \item The AMO's actual day-to-day maintenance \textbf{must match} what the MOE describes --
    this is exactly what Quality/Compliance Monitoring audits check (links to Meeting 5).
    \end{itemize}"""),
   ("AMO Internal Quality System",
    r"""\begin{itemize}
    \item Independent internal audits of maintenance work against approved data and procedures.
    \item Personnel competency and training records, including recurrent training.
    \item A defect/occurrence reporting process that feeds the operator's SMS
    (links to Meeting 5).
    \item Supplier/vendor control -- parts and sub-contracted work must come from
    traceable, approved sources (links to Part 21, Meeting 3).
    \end{itemize}"""),
   ("Certificate of Release to Service (CRS)",
    r"""A \textbf{CRS} is the formal statement, signed by an authorized certifying staff
    member of the AMO, that maintenance has been completed in accordance with approved
    data and the aircraft/component is airworthy for the work performed.
    \begin{itemize}
    \item Legally, an aircraft may not return to service after maintenance without a valid CRS.
    \item The CRS references the specific work order, the applicable approved data (AMM/SB/AD),
    and the certifying staff's license number.
    \item A CRS issued without the work actually meeting approved data is both a
    regulatory violation and a direct airworthiness hazard.
    \end{itemize}"""),
   ("From Work Order to Legal Airworthiness -- The AMO Chain",
    r"""\begin{center}
    \begin{tikzpicture}[>={Latex},node distance=0.4cm]
      \node[draw,fill=blue!10,rounded corners,text width=2.3cm,align=center] (wo) {Work order issued};
      \node[draw,fill=orange!15,rounded corners,text width=2.3cm,align=center,right=0.3cm of wo] (perf) {Task performed per approved data};
      \node[draw,fill=green!15,rounded corners,text width=2.3cm,align=center,right=0.3cm of perf] (qc) {Quality/inspection check};
      \node[draw,fill=yellow!20,rounded corners,text width=2.3cm,align=center,right=0.3cm of qc] (crs) {CRS signed by certifying staff};
      \node[draw,fill=red!15,rounded corners,text width=2.3cm,align=center,right=0.3cm of crs] (rts) {Aircraft returned to service};
    \end{tikzpicture}
    \end{center}
    Every link in this chain is individually auditable -- the AMO's quality system exists to
    make sure no link is skipped."""),
   ("Practice 1 -- Problem",
    r"Explain why complex commercial maintenance is normally required to be performed under an AMO certificate rather than solely under an individual's Part 65 license."),
   ("Practice 1 -- Solution",
    r"""An AMO certificate places accountability on the \emph{organization} -- its
    facilities, quality system, procedures, and oversight -- in addition to the individual
    certifying staff member's license. This provides layered assurance (organizational
    quality system + individual competency) appropriate for complex commercial maintenance,
    rather than relying on one individual's judgment alone."""),
   ("Practice 2 -- Problem",
    r"What must a valid Certificate of Release to Service (CRS) reference, and what is its legal effect?"),
   ("Practice 2 -- Solution",
    r"""A valid CRS must reference the specific work order, the approved data used (AMM/SB/AD
    as applicable), and the certifying staff member's license number. Its legal effect is
    that the aircraft/component may not be legally returned to service for that work until
    the CRS is signed."""),
  ],
  I("An AMO is organizationally certificated and approved against its own Maintenance Organization Exposition (MOE).",
    "AMO approval covers facilities, personnel, procedures, and an explicit scope of work.",
    "A Certificate of Release to Service (CRS) is the legal precondition for returning an aircraft/component to service."),
  I("List the four main areas of AMO approval requirements.",
    "Explain what the MOE must describe.",
    "Explain what a CRS must reference and why it matters legally."))

# ---------------- Meeting 8 ----------------
M[8] = ("Approved Maintenance License Requirements",
  "Students are able to explain requirements for aircraft maintenance personnel licensing.",
  I("Explain eligibility requirements for a CASR Part 65 AME license.",
    "Explain license ratings, privileges, and limitations.",
    "Explain recency of experience and license renewal/revalidation requirements."),
  [("The AME License: Purpose",
    r"""An \textbf{Aircraft Maintenance Engineer (AME)} license is the personal
    certification (CASR Part 65) that authorizes an individual to perform and/or certify
    specific aircraft maintenance tasks -- distinct from, but working alongside, an AMO's
    organizational certificate (Meeting 7)."""),
   ("Eligibility Requirements (Typical Structure)",
    r"""\begin{center}\renewcommand{\arraystretch}{1.3}
    \begin{tabular}{|l|p{7.3cm}|}\hline
    \textbf{Requirement} & \textbf{Typical content}\\\hline
    Age & Minimum age set by regulation (commonly 18 or 21 depending on rating)\\
    Knowledge & Pass written examinations on applicable subjects (regulations, airframe/powerplant/avionics fundamentals)\\
    Experience & Minimum documented practical experience (e.g.\ structured training program or supervised OJT hours)\\
    Skill & Pass a practical/oral test demonstrating competence on representative tasks\\\hline
    \end{tabular}\end{center}"""),
   ("License Ratings",
    r"""A license is issued with one or more \textbf{ratings} defining its scope:
    \begin{itemize}
    \item \textbf{Airframe} -- structures, systems appropriate to airframe maintenance.
    \item \textbf{Powerplant} -- engine and related systems.
    \item \textbf{Avionics / Instrument-Electrical} -- avionics, electrical, and instrument systems.
    \item Ratings may be further limited by \textbf{aircraft type} (type rating) for complex
    aircraft, especially large transport category aircraft.
    \end{itemize}"""),
   ("Privileges and Limitations",
    r"""\begin{itemize}
    \item \textbf{Privilege:} what the license holder \emph{may} do -- e.g.\ certify
    maintenance within the scope of their rating(s).
    \item \textbf{Limitation:} what the license holder \emph{may not} do -- e.g.\ a
    powerplant-rated AME may not certify avionics work without the corresponding rating.
    \item Privileges apply only \textbf{within the scope of the rating held} -- a license is
    not a blanket authorization to work on any aircraft system.
    \end{itemize}"""),
   ("Recency of Experience",
    r"""\begin{center}
    \begin{tikzpicture}[>={Latex}]
      \draw[thick,->] (0,0) -- (9,0) node[right,font=\footnotesize]{time};
      \foreach \x in {0,3,6,9} \draw (\x,0.1) -- (\x,-0.1);
      \node[below,font=\footnotesize] at (0,-0.15) {licensed};
      \node[below,font=\footnotesize] at (4.5,-0.15) {must show recent experience};
      \node[below,font=\footnotesize] at (9,-0.15) {privileges remain valid};
      \draw[decorate,decoration={brace,amplitude=5pt},thick] (0,0.3) -- (9,0.3)
        node[midway,above=4pt,font=\footnotesize]{typically a 24-month rolling window};
    \end{tikzpicture}
    \end{center}
    Holding a license is \textbf{not sufficient} to exercise its privileges -- the holder
    must also demonstrate recent, relevant practical experience within a defined period, or
    complete refresher training/assessment before exercising privileges again."""),
   ("Renewal, Revalidation, and Record-Keeping",
    r"""\begin{itemize}
    \item Licenses are typically subject to periodic \textbf{revalidation}, which may require
    evidence of recency, continued good standing, and sometimes recurrent training.
    \item The license holder (not only the AMO) is personally responsible for maintaining
    evidence of recency -- this connects directly to accurate personal training/experience records.
    \item A certifying signature (CRS, Meeting 7) made outside the scope of a valid, current
    rating is a regulatory violation, independent of whether the work itself was done correctly.
    \end{itemize}"""),
   ("Linking License Requirements Back to the Course",
    r"""\begin{itemize}
    \item Part 65 (this meeting) defines \emph{who} may certify work.
    \item Part 43 (Meeting 3) defines \emph{how} the work must be performed/recorded.
    \item The AMO (Meeting 7) provides the organizational framework the licensed individual
    works within for commercial maintenance.
    \item Together, Parts 21/43/65/91 and the AMO system form the complete legal chain from
    an approved part to a legally returned-to-service aircraft.
    \end{itemize}"""),
   ("Practice 1 -- Problem",
    r"Explain why holding an AME license is not, by itself, sufficient to legally certify maintenance work."),
   ("Practice 1 -- Solution",
    r"""The license holder must also be exercising privileges \emph{within the scope of a
    current, valid rating} and must meet recency-of-experience requirements. A license with
    an expired recency period, or work outside the holder's rating, means the certifying
    signature is not legally valid even though the license itself has not been revoked."""),
   ("Practice 2 -- Problem",
    r"A powerplant-rated AME is asked to certify avionics troubleshooting work. Is this permitted? Why or why not?"),
   ("Practice 2 -- Solution",
    r"""Not permitted. License privileges apply only within the scope of the rating held;
    a powerplant rating does not confer authority over avionics/instrument-electrical work.
    The task would require an AME holding the appropriate avionics rating."""),
  ],
  I("An AME license (Part 65) requires age, knowledge, experience, and skill eligibility to be met.",
    "License ratings (airframe, powerplant, avionics) define the scope of privileges; work outside that scope is not permitted.",
    "Recency of experience and revalidation are required to keep license privileges exercisable, separate from the license's validity."),
  I("List the four eligibility requirement categories for an AME license.",
    "Explain the difference between a license privilege and a license limitation.",
    "Explain why recency of experience matters even for a currently valid license."))

if __name__ == "__main__":
    order = [1,2,3,4,5,6,7,8]
    results = []
    for n in order:
        title, subclo, ind, slides, summ, asg = M[n]
        tex = build_deck(COURSE, SUBJECT, SUBTITLE, REF, CLO, n, title, subclo, ind, slides, summ, asg)
        results.append(compile_meeting(COURSE, n, tex))
        print(results[-1], flush=True)
    print("DONE", COURSE)
