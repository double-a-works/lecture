#!/usr/bin/env python3
"""Technical_English (curriculum §1) — meetings 1-8. Build via build_slides."""
from build_slides import build_deck, compile_meeting

COURSE   = "Technical_English"
SUBJECT  = "TECHNICAL ENGLISH"
SUBTITLE = "English for Aviation Maintenance Technicians"
REF      = "Betty S. Azar, Understanding and Using English Grammar; FAA-H-8083-30 Aircraft Maintenance Manual conventions"
CLO = [
 "Use verb tenses and modal auxiliaries accurately in technical English communication.",
 "Construct passive sentences and adjective clauses in technical English writing.",
 "Use connecting words, supplementary grammar units, and preposition combinations accurately in technical texts.",
 "Read and understand aviation technical documents (Aircraft Maintenance Manual) in English.",
]

I = lambda *xs: list(xs)
M = {}

# ---------------- Meeting 1: Verb Tenses ----------------
M[1] = ("Verb Tenses: Simple, Continuous, Perfect",
  "Students are able to use verb tenses (simple, continuous, perfect) accurately in technical context.",
  I("Identify the form of simple, continuous, and perfect tenses.",
    "Choose the correct tense for a maintenance report or instruction.",
    "Rewrite a sentence correctly when the tense is wrong."),
  [("Why Tenses Matter in Maintenance English",
    r"""A technician's logbook entry, work order, or AMM step must say exactly \emph{when}
    something happened or happens -- the wrong tense can make a completed inspection sound
    like a pending one.
    \begin{itemize}
    \item Maintenance records are legal documents: tense signals completed vs. ongoing vs. planned work.
    \item This meeting reviews the three tense families: simple, continuous (progressive), perfect.
    \end{itemize}"""),
   ("The Three Tense Families",
    r"""\begin{center}\renewcommand{\arraystretch}{1.3}
    \begin{tabular}{|l|l|l|}\hline
    \textbf{Family} & \textbf{Focus} & \textbf{Example (present)}\\\hline
    Simple & fact, habit, routine & inspects \\
    Continuous & action in progress & is inspecting \\
    Perfect & result / connection to another time & has inspected \\\hline
    \end{tabular}\end{center}
    Each family exists in past, present, and future -- giving nine basic tense combinations."""),
   ("Simple Tenses",
    r"""\begin{itemize}
    \item \textbf{Simple present:} routine facts, checklists, standard procedures.\\
    \emph{The technician \underline{checks} the oil level every 50 flight hours.}
    \item \textbf{Simple past:} a completed, dated action.\\
    \emph{The mechanic \underline{replaced} the brake pads on 12 October.}
    \item \textbf{Simple future (will):} a planned future action.\\
    \emph{The inspector \underline{will sign} the release-to-service form tomorrow.}
    \end{itemize}"""),
   ("Continuous (Progressive) Tenses",
    r"""\begin{itemize}
    \item \textbf{Present continuous:} happening right now, or a temporary arrangement.\\
    \emph{The crew \underline{is torquing} the wheel bolts at this moment.}
    \item \textbf{Past continuous:} was in progress when something else happened.\\
    \emph{The AME \underline{was removing} the panel when the alarm sounded.}
    \item \textbf{Future continuous:} will be in progress at a stated future time.\\
    \emph{At 09:00 tomorrow the team \underline{will be performing} the A-check.}
    \end{itemize}"""),
   ("Perfect Tenses",
    r"""\begin{itemize}
    \item \textbf{Present perfect:} past action with present relevance; no exact time stated.\\
    \emph{The AMM \underline{has been updated} to revision 12.}
    \item \textbf{Past perfect:} an action completed before another past action.\\
    \emph{The leak \underline{had started} before the pilot reported low pressure.}
    \item \textbf{Future perfect:} will be completed before a stated future time.\\
    \emph{By Friday the shop \underline{will have finished} the engine overhaul.}
    \end{itemize}"""),
   ("Timeline of the Nine Core Tenses",
    r"""\begin{center}
    \begin{tikzpicture}[scale=0.95,>={Latex}]
      \draw[thick,->] (-4.3,0) -- (4.3,0) node[right] {\footnotesize time};
      \node at (-3,0.35) {\footnotesize PAST};
      \node at (0,0.35) {\footnotesize PRESENT};
      \node at (3,0.35) {\footnotesize FUTURE};
      \draw[fill=orange!60] (-3,0) circle (2pt);
      \draw[fill=orange!60] (0,0) circle (2pt);
      \draw[fill=orange!60] (3,0) circle (2pt);
      \draw[decorate,decoration={brace,amplitude=4pt},thick] (-3.9,-0.3) -- (-3,-0.3)
        node[midway,below=4pt]{\scriptsize perfect: before this point};
      \draw[dashed] (-1.1,0.1) rectangle (1.1,-1.0);
      \node[align=center] at (0,-0.6) {\scriptsize continuous: action\\\scriptsize spreads around the point};
    \end{tikzpicture}
    \end{center}
    Simple = a point; continuous = a stretch around the point; perfect = looking back from the point."""),
   ("Common Errors in Maintenance Writing",
    r"""\begin{itemize}
    \item Using simple present for a one-time completed action:
    \emph{\textcolor{red}{He fix the panel yesterday.}} $\to$ \emph{He \underline{fixed} the panel yesterday.}
    \item Mixing perfect and simple past without a clear time anchor:
    \emph{\textcolor{red}{I have inspected it yesterday.}} $\to$ \emph{I \underline{inspected} it yesterday.}
    \item Forgetting the auxiliary in continuous forms:
    \emph{\textcolor{red}{The team working now.}} $\to$ \emph{The team \underline{is working} now.}
    \end{itemize}"""),
   ("Practice 1 -- Problem",
    r"Correct the tense: \emph{``The hydraulic system leak since yesterday.''}"),
   ("Practice 1 -- Solution",
    r"""\emph{The hydraulic system \underline{has been leaking} since yesterday.}
    \\(present perfect continuous -- started in the past, still true now)"""),
   ("Practice 2 -- Problem",
    r"Choose the correct tense: \emph{``By the time the inspector arrives, the crew (finish) the check.''}"),
   ("Practice 2 -- Solution",
    r"""\emph{...the crew \underline{will have finished} the check.}
    \\(future perfect -- completed before a future point in time)"""),
  ],
  I("Simple, continuous, and perfect tenses each answer a different time question.",
    "Maintenance logbooks depend on correct tense to show completed vs. ongoing work.",
    "Perfect tenses connect two time points; continuous spreads an action around one point."),
  I("Correct three tense errors from sample logbook sentences.",
    "Write five logbook sentences using five different tenses.",
    "Identify the tense family in ten AMM excerpt sentences."))

# ---------------- Meeting 2: Modal auxiliaries ----------------
M[2] = ("Modal Auxiliaries and Similar Expressions",
  "Students are able to use modal auxiliaries and similar expressions in technical instructions.",
  I("Identify modal auxiliaries and their meanings (ability, permission, obligation, possibility).",
    "Distinguish obligation modals (must/have to/should) in regulatory text.",
    "Rewrite instructions using appropriate modals and semi-modals."),
  [("What Modals Do",
    r"""Modal auxiliaries (\textit{can, could, may, might, must, shall, should, will, would})
    add meaning about \textbf{ability, permission, obligation, possibility, or necessity}
    without changing the main verb's form (always base form after a modal).
    \begin{itemize}
    \item AMM steps and CASR regulations rely heavily on modals to show what is
    \emph{required} versus \emph{recommended} versus \emph{permitted}.
    \end{itemize}"""),
   ("Modals of Obligation and Necessity",
    r"""\begin{center}\renewcommand{\arraystretch}{1.3}
    \begin{tabular}{|l|l|p{5.3cm}|}\hline
    \textbf{Modal} & \textbf{Strength} & \textbf{Example}\\\hline
    must / have to & strong, mandatory & The torque value \underline{must} meet the AMM spec.\\
    should / ought to & recommended & Technicians \underline{should} wear eye protection.\\
    need not / don't have to & not necessary & You \underline{don't have to} remove the cowling for this check.\\
    must not & prohibited & Personnel \underline{must not} smoke near fuel tanks.\\\hline
    \end{tabular}\end{center}"""),
   ("Modals of Permission and Ability",
    r"""\begin{itemize}
    \item \textbf{Permission:} \emph{may} (formal), \emph{can} (informal) --
    \emph{Only a licensed AME \underline{may} sign the release-to-service.}
    \item \textbf{Ability:} \emph{can}, \emph{could} (past), \emph{be able to} --
    \emph{The borescope \underline{can} reach the third-stage compressor blades.}
    \item \textbf{Requesting permission:} \emph{Could/May I disconnect the battery first?}
    \end{itemize}"""),
   ("Modals of Possibility and Deduction",
    r"""\begin{itemize}
    \item \textbf{Possibility:} \emph{may, might, could} --
    \emph{The vibration \underline{might} indicate an unbalanced fan blade.}
    \item \textbf{Strong deduction:} \emph{must} --
    \emph{The breaker tripped twice; there \underline{must} be a short circuit.}
    \item \textbf{Deduction that something is false:} \emph{can't} --
    \emph{That reading \underline{can't} be correct -- recheck the sensor.}
    \end{itemize}"""),
   ("Obligation Strength -- A Visual Scale",
    r"""\begin{center}
    \begin{tikzpicture}[>={Latex}]
      \draw[thick,->] (0,0) -- (10,0);
      \foreach \x/\lab in {0/{not necessary},2.5/{recommended},5/{strong advice},7.5/{mandatory},10/{prohibited}}
        \draw (\x,0.08) -- (\x,-0.08) node[below,align=center,font=\footnotesize] {\lab};
      \node[above,font=\footnotesize] at (0,0.1) {needn't};
      \node[above,font=\footnotesize] at (2.5,0.1) {could};
      \node[above,font=\footnotesize] at (5,0.1) {should};
      \node[above,font=\footnotesize] at (7.5,0.1) {must};
      \node[above,font=\footnotesize] at (10,0.1) {must not};
    \end{tikzpicture}
    \end{center}
    Reading regulatory text precisely means distinguishing \emph{should} (advisory) from
    \emph{must} (mandatory) -- CASR and AMM wording is deliberate."""),
   ("Semi-Modals and Related Expressions",
    r"""\begin{itemize}
    \item \textit{be supposed to}: expected by rule or schedule --
    \emph{The inspection \underline{is supposed to} occur every 100 hours.}
    \item \textit{be allowed to} / \textit{be permitted to}: formal permission --
    \emph{Trainees \underline{are not permitted to} sign off major repairs alone.}
    \item \textit{had better}: strong advice with a negative consequence if ignored --
    \emph{You \underline{had better} torque that fitting, or it will leak.}
    \end{itemize}"""),
   ("Modals in Passive Instructions (Preview)",
    r"""Modals combine with passive voice often in AMM procedure steps:
    \emph{The fastener \underline{must be torqued} to 25 Nm.}
    \\\emph{The panel \underline{should not be removed} without disconnecting power first.}
    \\Pattern: \textbf{modal + be + past participle}. This combination will return in Meeting 3
    (The Passive)."""),
   ("Practice 1 -- Problem",
    r"Choose the best modal: \emph{``Technicians \_\_\_\_ disconnect the battery before working on the electrical bus.''}"),
   ("Practice 1 -- Solution",
    r"""\emph{Technicians \underline{must} disconnect the battery...}
    \\(safety-critical step -- mandatory, not merely advisory)"""),
   ("Practice 2 -- Problem",
    r"Identify the meaning of the modal: \emph{``The gauge might be faulty.''}"),
   ("Practice 2 -- Solution",
    r"""\textbf{Possibility/deduction} -- the speaker is not certain, only suggesting a
    possible explanation for an observed reading, not stating a fact."""),
  ],
  I("Modals add meaning (obligation, permission, ability, possibility) without changing verb form.",
    "Regulatory text distinguishes mandatory (must) from advisory (should) language precisely.",
    "Modal + be + past participle previews passive instructions."),
  I("Classify ten modal sentences from a sample AMM extract by meaning.",
    "Rewrite five instructions choosing the correct strength of modal.",
    "Write three sentences each for obligation, permission, and possibility."))

# ---------------- Meeting 3: The Passive ----------------
M[3] = ("The Passive Voice",
  "Students are able to construct and understand passive sentences in technical manuals.",
  I("Form the passive in different tenses.",
    "Explain why technical manuals favor the passive voice.",
    "Convert active sentences from a maintenance context into passive and vice versa."),
  [("Active vs. Passive: The Core Idea",
    r"""\begin{itemize}
    \item \textbf{Active:} subject performs the action --
    \emph{The technician \underline{replaced} the filter.}
    \item \textbf{Passive:} subject receives the action --
    \emph{The filter \underline{was replaced} (by the technician).}
    \item Formula: \textbf{be + past participle}, with the agent optional (``by...'').
    \end{itemize}"""),
   ("Why Manuals Prefer the Passive",
    r"""\begin{itemize}
    \item AMM procedures describe \emph{what happens to the part}, not who does it --
    the actor is often irrelevant or implied (``the technician'').
    \item Passive voice keeps the object of the action as the sentence's focus and subject,
    matching how checklists are organized (component-first).
    \item Example: \emph{The access panel \underline{is secured} with eight screws.}
    (focus: the panel, not the person securing it.)
    \end{itemize}"""),
   ("Passive Across the Tenses",
    r"""\begin{center}\renewcommand{\arraystretch}{1.3}
    \begin{tabular}{|l|l|}\hline
    \textbf{Tense} & \textbf{Passive example}\\\hline
    Simple present & The fuel filter \underline{is inspected} monthly.\\
    Simple past & The seal \underline{was replaced} last week.\\
    Present perfect & The AD \underline{has been complied with}.\\
    Future (will) & The engine \underline{will be tested} tomorrow.\\
    Modal + passive & The bolt \underline{must be torqued} to spec.\\\hline
    \end{tabular}\end{center}"""),
   ("Step-by-Step Conversion: Active $\\to$ Passive",
    r"""\begin{enumerate}
    \item Move the active object to the subject position.
    \item Add the correct form of \textbf{be} matching the original tense.
    \item Change the main verb to its \textbf{past participle}.
    \item Optionally add \emph{by + agent} if the agent matters.
    \end{enumerate}
    Example: \emph{The crew checked the tires.} $\to$
    \emph{The tires \underline{were checked} (by the crew).}"""),
   ("Worked Conversion Example",
    r"""\begin{center}
    \begin{tikzpicture}[>={Latex},node distance=1.1cm]
      \node[draw,fill=blue!10,rounded corners] (a) {The AME torqued the nut.};
      \node[draw,fill=orange!15,rounded corners,below=of a] (b) {The nut was torqued (by the AME).};
      \draw[->,thick] (a) -- (b) node[midway,right,font=\footnotesize] {passive transform};
    \end{tikzpicture}
    \end{center}
    Object \emph{``the nut''} becomes the new subject; \emph{torqued} stays as a past participle
    after \emph{was}."""),
   ("Passive with Modals (Reviewing Meeting 2)",
    r"""\begin{itemize}
    \item \emph{The panel \underline{must be removed} before inspection.}
    \item \emph{This fastener \underline{should not be reused}.}
    \item \emph{The component \underline{can be replaced} without special tools.}
    \end{itemize}
    Pattern: \textbf{modal + be + past participle} -- very common in regulatory and AMM steps."""),
   ("Common Passive Errors",
    r"""\begin{itemize}
    \item Missing \textbf{be}: \emph{\textcolor{red}{The panel removed yesterday.}} $\to$
    \emph{The panel \underline{was removed} yesterday.}
    \item Wrong participle form: \emph{\textcolor{red}{The part was broke.}} $\to$
    \emph{The part \underline{was broken}.}
    \item Overusing passive where the actor matters for accountability
    (e.g.\ sign-off statements should often stay active: \emph{``I certify that...''}).
    \end{itemize}"""),
   ("Practice 1 -- Problem",
    r"Convert to passive: \emph{``The inspector found a crack in the spar.''}"),
   ("Practice 1 -- Solution",
    r"""\emph{A crack \underline{was found} in the spar (by the inspector).}"""),
   ("Practice 2 -- Problem",
    r"Convert to passive with a modal: \emph{``You must replace this gasket every overhaul.''}"),
   ("Practice 2 -- Solution",
    r"""\emph{This gasket \underline{must be replaced} every overhaul.}"""),
  ],
  I("Passive = be + past participle; the agent is optional.",
    "AMM and regulatory text favor passive to keep the component as the focus.",
    "Modal + be + past participle is the standard instruction pattern."),
  I("Convert five active maintenance sentences to passive.",
    "Find three passive sentences in a sample AMM page and identify their tense.",
    "Rewrite two passive sentences back into active voice."))

# ---------------- Meeting 4: Adjective clause ----------------
M[4] = ("Adjective Clauses (Relative Clauses)",
  "Students are able to construct and understand adjective clauses in technical descriptions.",
  I("Identify relative pronouns (who, which, that, whose) and their use.",
    "Form restrictive adjective clauses describing a part or procedure.",
    "Reduce adjective clauses to shorter modifying phrases where appropriate."),
  [("What an Adjective Clause Does",
    r"""An \textbf{adjective (relative) clause} modifies a noun, giving extra identifying
    information -- very common in technical descriptions that define a part precisely.
    \begin{itemize}
    \item \emph{The valve \underline{that controls fuel flow} is located aft of the firewall.}
    \item The clause \emph{that controls fuel flow} tells us exactly which valve.
    \end{itemize}"""),
   ("Relative Pronouns",
    r"""\begin{center}\renewcommand{\arraystretch}{1.3}
    \begin{tabular}{|l|l|p{5.3cm}|}\hline
    \textbf{Pronoun} & \textbf{Refers to} & \textbf{Example}\\\hline
    who & people & the AME \underline{who} signed the log\\
    which & things & the bolt \underline{which} sheared\\
    that & people or things & the sensor \underline{that} failed\\
    whose & possession & the aircraft \underline{whose} engine overheated\\\hline
    \end{tabular}\end{center}"""),
   ("Restrictive vs. Non-Restrictive Clauses",
    r"""\begin{itemize}
    \item \textbf{Restrictive} (no commas): essential to identify the noun --
    \emph{The technician \underline{who performed the inspection}} signed the form.
    (tells us \emph{which} technician -- essential.)
    \item \textbf{Non-restrictive} (commas): extra, non-essential information --
    \emph{The engine, \underline{which was overhauled last year}, passed the test run.}
    (the engine is already identified; the clause just adds detail.)
    \item \emph{that} is used only in restrictive clauses, never after a comma.
    \end{itemize}"""),
   ("Subject vs. Object Relative Clauses",
    r"""\begin{itemize}
    \item \textbf{Subject clause} -- relative pronoun is the subject of its clause, cannot be omitted:
    \emph{the part \underline{that} \underline{failed}} (``that'' = subject of ``failed'').
    \item \textbf{Object clause} -- relative pronoun is the object, can often be omitted:
    \emph{the part (\underline{that}) \underline{the inspector rejected}}
    (``that'' = object of ``rejected''; may be dropped in informal writing, kept in formal manuals).
    \end{itemize}"""),
   ("Reducing Adjective Clauses to Phrases",
    r"""\begin{center}
    \begin{tikzpicture}[>={Latex}]
      \node[draw,fill=blue!10,rounded corners,text width=7.5cm,align=left] (a)
        {The panel \textbf{that is located} on the lower fuselage must be removed first.};
      \node[draw,fill=orange!15,rounded corners,text width=7.5cm,align=left,below=0.5cm of a] (b)
        {The panel \textbf{located} on the lower fuselage must be removed first.};
      \draw[->,thick] (a) -- (b) node[midway,right,font=\footnotesize] {reduce};
    \end{tikzpicture}
    \end{center}
    Drop \emph{that/which + be}; keep the participle. Works only when the relative pronoun is
    the subject of the clause."""),
   ("Adjective Clauses in AMM Descriptions",
    r"""\begin{itemize}
    \item \emph{The circuit breaker \underline{that protects the fuel pump} is labeled FP-1.}
    \item \emph{Inspect all fasteners \underline{whose torque marks are missing}.}
    \item \emph{The AD \underline{which was issued in 2024} applies to this serial number range.}
    \end{itemize}
    Precision matters: a missing or misplaced adjective clause can change which component a
    step refers to."""),
   ("Common Errors",
    r"""\begin{itemize}
    \item Using \emph{which} for people: \emph{\textcolor{red}{the AME which signed}} $\to$
    \emph{the AME \underline{who} signed}.
    \item Adding a comma before a restrictive \emph{that}-clause (not allowed):
    \emph{\textcolor{red}{the part, that failed,}} $\to$ \emph{the part \underline{that failed}}.
    \item Dropping the subject relative pronoun (not allowed):
    \emph{\textcolor{red}{the sensor failed is faulty}} $\to$ \emph{the sensor \underline{that} failed is faulty}.
    \end{itemize}"""),
   ("Practice 1 -- Problem",
    r"Combine: \emph{``The technician inspected the landing gear. The landing gear showed signs of corrosion.''}"),
   ("Practice 1 -- Solution",
    r"""\emph{The technician inspected the landing gear \underline{that showed signs of corrosion}.}"""),
   ("Practice 2 -- Problem",
    r"Reduce the clause: \emph{``The bracket that is mounted near the spar must be replaced.''}"),
   ("Practice 2 -- Solution",
    r"""\emph{The bracket \underline{mounted} near the spar must be replaced.}"""),
  ],
  I("Relative pronouns (who/which/that/whose) introduce adjective clauses that identify a noun.",
    "Restrictive clauses use no commas; that never follows a comma.",
    "Subject-relative clauses can reduce to a participle phrase."),
  I("Combine five sentence pairs into adjective clauses.",
    "Mark five AMM-style sentences as restrictive or non-restrictive.",
    "Reduce three adjective clauses to shorter phrases."))

# ---------------- Meeting 5: Showing relationship between ideas ----------------
M[5] = ("Showing Relationship Between Ideas",
  "Students are able to use connecting words to show relationships between ideas in technical text.",
  I("Classify connectors by relationship (cause/effect, contrast, addition, sequence, condition).",
    "Punctuate coordinating and subordinating conjunctions correctly.",
    "Combine two technical sentences using the correct connector."),
  [("Why Connectors Matter",
    r"""Technical writing links facts, causes, warnings, and steps.
    A wrong connector can reverse the intended meaning --
    \emph{``...however the engine stopped''} is very different from
    \emph{``...therefore the engine stopped.''}
    \begin{itemize}
    \item This meeting organizes connectors by the \emph{relationship} they express.
    \end{itemize}"""),
   ("Cause and Effect",
    r"""\begin{center}\renewcommand{\arraystretch}{1.3}
    \begin{tabular}{|l|p{6.5cm}|}\hline
    \textbf{Connector} & \textbf{Example}\\\hline
    because / since & The flight was delayed \underline{because} the sensor failed.\\
    therefore / as a result & The sensor failed; \underline{therefore}, the flight was delayed.\\
    due to / owing to (+ noun) & The delay was \underline{due to} sensor failure.\\\hline
    \end{tabular}\end{center}
    \emph{because} joins clauses; \emph{due to} takes a noun phrase, not a full clause."""),
   ("Contrast",
    r"""\begin{center}\renewcommand{\arraystretch}{1.3}
    \begin{tabular}{|l|p{6.5cm}|}\hline
    \textbf{Connector} & \textbf{Example}\\\hline
    but / yet & The part is used, \underline{but} it passed inspection.\\
    however & The gauge read normal; \underline{however}, vibration was excessive.\\
    although / even though & \underline{Although} the AD was complied with, the issue recurred.\\
    despite / in spite of (+ noun) & \underline{Despite} the repair, the leak continued.\\\hline
    \end{tabular}\end{center}"""),
   ("Addition and Sequence",
    r"""\begin{itemize}
    \item \textbf{Addition:} \emph{and, in addition, moreover, furthermore} --
    \emph{The filter was replaced; \underline{in addition}, the line was flushed.}
    \item \textbf{Sequence:} \emph{first, next, then, after that, finally} --
    \emph{\underline{First} disconnect power; \underline{then} remove the panel.}
    \end{itemize}"""),
   ("Condition",
    r"""\begin{itemize}
    \item \emph{if} -- real/possible condition: \emph{\underline{If} the reading exceeds limits, reject the part.}
    \item \emph{unless} -- ``if not'': \emph{Do not install the part \underline{unless} it is tagged serviceable.}
    \item \emph{provided that} -- formal condition: \emph{The aircraft may fly \underline{provided that} the MEL item is placarded.}
    \end{itemize}"""),
   ("Relationship Map",
    r"""\begin{center}
    \begin{tikzpicture}[>={Latex},every node/.style={font=\footnotesize}]
      \node[draw,circle,fill=blue!10] (c) at (0,0) {IDEA A};
      \node[draw,circle,fill=orange!15] (e) at (5,0) {IDEA B};
      \draw[->,thick] (c) -- node[above]{because / since} (e);
      \draw[->,thick,bend left=40] (c) to node[above]{but / however} (e);
      \draw[->,thick,bend right=40] (c) to node[below]{and / in addition} (e);
      \draw[->,thick,dashed] (c) -- node[below,yshift=-14pt]{if / unless} (e);
    \end{tikzpicture}
    \end{center}
    The same two ideas can be connected in at least four different logical ways -- choosing
    the right one changes the meaning of the instruction."""),
   ("Punctuation Rules",
    r"""\begin{itemize}
    \item Coordinating conjunction (and, but, so) joining two full clauses: comma before it.\\
    \emph{The part failed, \underline{so} it was replaced.}
    \item Subordinating conjunction (because, although, if) at the \emph{start} of a sentence: comma after the clause.\\
    \emph{\underline{Although} the torque was correct, the bolt loosened.}
    \item Transition word (however, therefore) joining two sentences: semicolon before, comma after.\\
    \emph{The pressure was normal; \underline{however}, the alarm triggered.}
    \end{itemize}"""),
   ("Practice 1 -- Problem",
    r"Combine with a cause/effect connector: \emph{``The bearing overheated. The technician replaced it.''}"),
   ("Practice 1 -- Solution",
    r"""\emph{The bearing overheated; \underline{therefore}, the technician replaced it.}
    \\or: \emph{\underline{Because} the bearing overheated, the technician replaced it.}"""),
   ("Practice 2 -- Problem",
    r"Combine with a contrast connector: \emph{``The part is serviceable. It shows minor corrosion.''}"),
   ("Practice 2 -- Solution",
    r"""\emph{\underline{Although} it shows minor corrosion, the part is serviceable.}"""),
  ],
  I("Connectors are grouped by the logical relationship they express.",
    "because/although join clauses; due to/despite take a noun phrase.",
    "Punctuation differs between coordinating conjunctions, subordinators, and transitions."),
  I("Classify ten connectors by relationship type.",
    "Combine five sentence pairs using a connector from each category.",
    "Punctuate five connector sentences correctly."))

# ---------------- Meeting 6: Supplementary Grammar Units ----------------
M[6] = ("Supplementary Grammar Units",
  "Students are able to apply supplementary grammar units (article, quantifier, conditional sentence).",
  I("Use definite/indefinite articles correctly with technical nouns.",
    "Use quantifiers appropriately with countable and uncountable technical nouns.",
    "Form conditional sentences (zero, first, second) for procedures and troubleshooting."),
  [("Articles: a / an / the / (no article)",
    r"""\begin{center}\renewcommand{\arraystretch}{1.3}
    \begin{tabular}{|l|p{6.6cm}|}\hline
    \textbf{Use} & \textbf{Example}\\\hline
    a/an -- first mention, one of many & Install \underline{a} new gasket.\\
    the -- specific, already known & Torque \underline{the} gasket you just installed.\\
    (no article) -- general/uncountable & \underline{\ \ } Hydraulic fluid is flammable.\\\hline
    \end{tabular}\end{center}
    Rule of thumb: first mention of a countable item $\to$ \emph{a/an}; every mention after
    that $\to$ \emph{the}, because it is now specific/identified."""),
   ("Countable and Uncountable Technical Nouns",
    r"""\begin{itemize}
    \item \textbf{Countable:} bolt(s), panel(s), sensor(s), aircraft (same singular/plural) --
    can use \emph{a/an}, numbers, \emph{many, few}.
    \item \textbf{Uncountable:} fuel, oil, equipment, information, damage --
    cannot use \emph{a/an} or numbers directly; use \emph{much, little}, or a counter
    (\emph{a litre of fuel}, \emph{a piece of equipment}).
    \item Common error: \emph{\textcolor{red}{an equipment}} $\to$ \emph{a piece of equipment} / \emph{equipment}.
    \end{itemize}"""),
   ("Quantifiers",
    r"""\begin{center}\renewcommand{\arraystretch}{1.3}
    \begin{tabular}{|l|l|l|}\hline
    & \textbf{Countable} & \textbf{Uncountable}\\\hline
    large amount & many, a number of & much, a great deal of\\
    small amount & few, a few & little, a little\\
    general & some, any, all & some, any, all\\\hline
    \end{tabular}\end{center}
    \emph{Few} fasteners remain (almost none -- negative). \emph{A few} fasteners remain
    (some, a small positive amount) -- the article changes the meaning."""),
   ("Conditional Sentences: Zero Conditional",
    r"""\textbf{Zero conditional} -- general truths, standard procedures, cause-and-effect that
    is always true:
    \[ \text{If} + \text{present simple}, \quad \text{present simple} \]
    \emph{If the fuel pressure \underline{drops} below 5 psi, the warning light \underline{illuminates}.}
    \\Used for physics/engineering facts and standard system behavior -- not a hypothetical."""),
   ("First Conditional",
    r"""\textbf{First conditional} -- real, likely future situation and its result:
    \[ \text{If} + \text{present simple}, \quad \text{will} + \text{base verb} \]
    \emph{If the reading \underline{exceeds} the limit, the technician \underline{will reject}
    the part.}
    \\Used for troubleshooting instructions and real possible outcomes."""),
   ("Second Conditional",
    r"""\textbf{Second conditional} -- hypothetical/unlikely or contrary-to-fact present situation:
    \[ \text{If} + \text{past simple}, \quad \text{would} + \text{base verb} \]
    \emph{If the aircraft \underline{had} no circuit breakers, a short \underline{would damage}
    the whole bus.}
    \\Used for ``what if'' safety discussions and hypothetical failure scenarios, not actual
    standing instructions."""),
   ("Conditional Comparison",
    r"""\begin{center}
    \begin{tikzpicture}[>={Latex},every node/.style={font=\footnotesize,align=center}]
      \node[draw,fill=blue!10,rounded corners,text width=3.6cm] (z) at (0,0) {Zero\\always true fact};
      \node[draw,fill=orange!15,rounded corners,text width=3.6cm] (f) at (4.2,0) {First\\real future possibility};
      \node[draw,fill=green!15,rounded corners,text width=3.6cm] (s) at (8.4,0) {Second\\hypothetical, unlikely};
      \draw[->,thick] (z) -- (f); \draw[->,thick] (f) -- (s);
    \end{tikzpicture}
    \end{center}
    Moving right = moving from certain/general fact toward imagined possibility."""),
   ("Practice 1 -- Problem",
    r"Choose a/an/the: \emph{``Replace \_\_\_ gasket with \_\_\_ new one; torque \_\_\_ gasket to spec.''}"),
   ("Practice 1 -- Solution",
    r"""\emph{Replace \underline{the} gasket with \underline{a} new one; torque \underline{the}
    gasket to spec.} (first ``the'' = specific gasket already known from context; ``a'' = first
    mention of the replacement; second ``the'' = now specific.)"""),
   ("Practice 2 -- Problem",
    r"Form a first conditional: \emph{``(oil pressure / drop) / (pilot / abort takeoff)''}"),
   ("Practice 2 -- Solution",
    r"""\emph{If the oil pressure \underline{drops}, the pilot \underline{will abort} the takeoff.}"""),
  ],
  I("Article choice depends on whether the noun is new information or already identified.",
    "Quantifiers differ for countable vs. uncountable technical nouns.",
    "Zero/first/second conditionals move from general fact to real possibility to hypothetical."),
  I("Fill in ten articles in a maintenance paragraph.",
    "Choose correct quantifiers for five countable/uncountable nouns.",
    "Write one sentence each for zero, first, and second conditional."))

# ---------------- Meeting 7: Preposition combinations ----------------
M[7] = ("Preposition Combinations",
  "Students are able to use preposition combinations accurately.",
  I("Identify common verb + preposition and adjective + preposition combinations.",
    "Use prepositions of place, time, and movement correctly in technical description.",
    "Correct preposition errors in sample maintenance sentences."),
  [("Why Prepositions Are Hard -- and Important",
    r"""Prepositions rarely follow a simple logical rule and must largely be learned as fixed
    combinations. In technical English they control precise meaning: \emph{``check for
    leaks''} vs. \emph{``check the leaks''} are not interchangeable in standard usage.
    \begin{itemize}
    \item This meeting groups the combinations technicians use most often.
    \end{itemize}"""),
   ("Verb + Preposition Combinations",
    r"""\begin{center}\renewcommand{\arraystretch}{1.3}
    \begin{tabular}{|l|p{6.3cm}|}\hline
    \textbf{Combination} & \textbf{Example}\\\hline
    check \underline{for} & Check \underline{for} fuel leaks around the fitting.\\
    consist \underline{of} & The kit consists \underline{of} four fasteners and a gasket.\\
    comply \underline{with} & The aircraft complies \underline{with} AD 2024-05.\\
    result \underline{in} / result \underline{from} & Corrosion resulted \underline{from} moisture ingress.\\
    refer \underline{to} & Refer \underline{to} chapter 32 for gear procedures.\\\hline
    \end{tabular}\end{center}"""),
   ("Adjective + Preposition Combinations",
    r"""\begin{center}\renewcommand{\arraystretch}{1.3}
    \begin{tabular}{|l|p{6.3cm}|}\hline
    \textbf{Combination} & \textbf{Example}\\\hline
    responsible \underline{for} & The AME is responsible \underline{for} the release.\\
    familiar \underline{with} & Trainees must be familiar \underline{with} the AMM.\\
    compatible \underline{with} & The part is compatible \underline{with} earlier models.\\
    prone \underline{to} & This joint is prone \underline{to} fatigue cracking.\\\hline
    \end{tabular}\end{center}"""),
   ("Prepositions of Place (Technical Description)",
    r"""\begin{center}
    \begin{tikzpicture}[scale=0.8,>={Latex}]
      \draw[thick,fill=blue!10] (0,0) rectangle (6,1.2);
      \node at (3,0.6) {\footnotesize FUSELAGE};
      \node[draw,fill=orange!25,minimum width=1cm,minimum height=0.5cm] (comp) at (1.5,2.1) {};
      \node[above] at (1.5,2.4) {\footnotesize on top of};
      \node[draw,fill=green!25,minimum width=0.6cm,minimum height=0.6cm] (below) at (3,-0.9) {};
      \node[below] at (3,-1.2) {\footnotesize beneath / under};
      \node[draw,fill=red!25,minimum width=0.5cm,minimum height=1.2cm] (aft) at (7,0.6) {};
      \node[right] at (7.4,0.6) {\footnotesize aft of};
      \node[draw,fill=yellow!25,minimum width=0.5cm,minimum height=1.2cm] (fwd) at (-1,0.6) {};
      \node[left] at (-1.4,0.6) {\footnotesize forward of};
    \end{tikzpicture}
    \end{center}
    \emph{on, under/beneath, forward of, aft of, adjacent to, between} -- standard spatial
    vocabulary for locating components relative to a reference structure."""),
   ("Prepositions of Time and Sequence",
    r"""\begin{itemize}
    \item \emph{within} -- a deadline window: \emph{Report the defect \underline{within} 24 hours.}
    \item \emph{by} -- a deadline point: \emph{Complete the check \underline{by} 1600 hours.}
    \item \emph{before / after} -- sequence: \emph{Torque-check \underline{after} the first 10 flight hours.}
    \item \emph{during} -- an ongoing period: \emph{Do not operate the system \underline{during} refueling.}
    \end{itemize}"""),
   ("Prepositions of Movement",
    r"""\begin{itemize}
    \item \emph{through} -- Route the wire \underline{through} the grommet.
    \item \emph{across} -- The crack extends \underline{across} the panel.
    \item \emph{into} -- Insert the pin \underline{into} the bracket.
    \item \emph{out of} -- Remove the filter element \underline{out of} the housing.
    \end{itemize}"""),
   ("Common Errors",
    r"""\begin{itemize}
    \item \emph{\textcolor{red}{comply to}} $\to$ \emph{comply \underline{with}}.
    \item \emph{\textcolor{red}{responsible of}} $\to$ \emph{responsible \underline{for}}.
    \item \emph{\textcolor{red}{check the leaks}} (meaning ``look for'') $\to$ \emph{check \underline{for} leaks}.
    \item Confusing \emph{in} (enclosed) with \emph{on} (surface): a component is
    \emph{\underline{in} the fuselage} but a placard is \emph{\underline{on} the fuselage}.
    \end{itemize}"""),
   ("Practice 1 -- Problem",
    r"Fill the preposition: \emph{``This bracket is prone \_\_\_ corrosion and must comply \_\_\_ the latest AD.''}"),
   ("Practice 1 -- Solution",
    r"""\emph{...prone \underline{to} corrosion and must comply \underline{with} the latest AD.}"""),
   ("Practice 2 -- Problem",
    r"Fill the preposition: \emph{``Route the hydraulic line \_\_\_ the grommet, \_\_\_ of the spar.''}"),
   ("Practice 2 -- Solution",
    r"""\emph{Route the hydraulic line \underline{through} the grommet, \underline{forward} of the spar.}"""),
  ],
  I("Verb/adjective + preposition pairs are largely fixed and must be learned as combinations.",
    "Place prepositions (forward of, aft of, beneath) describe component location precisely.",
    "Time prepositions (within, by, before/after) control compliance deadlines in regulatory text."),
  I("Fill in ten preposition gaps from a sample AMM paragraph.",
    "Write five sentences locating a component using place prepositions.",
    "Correct five common preposition errors."))

# ---------------- Meeting 8: AMM reading practice ----------------
M[8] = ("Reading and Understanding the Aircraft Maintenance Manual (AMM)",
  "Students are able to read and understand the structure and vocabulary of the Aircraft Maintenance Manual (AMM).",
  I("Explain the ATA chapter numbering structure of an AMM.",
    "Identify warning/caution/note conventions and their meaning.",
    "Apply tenses, passive voice, adjective clauses, connectors, and prepositions from Meetings 1--7 to read a real AMM-style procedure."),
  [("This Meeting: Putting It All Together",
    r"""Meetings 1--7 covered tenses, modals, passive, adjective clauses, connectors,
    supplementary grammar, and prepositions. A real AMM procedure uses \textbf{all of them
    together} in a dense, highly compressed style. This meeting practices reading that style
    directly."""),
   ("ATA Chapter Structure",
    r"""Commercial/general aviation manuals follow the \textbf{ATA iSpec 2200 / ATA 100}
    numbering scheme so any technician can find a topic in any manufacturer's manual.
    \begin{center}\renewcommand{\arraystretch}{1.25}
    \begin{tabular}{|l|l|}\hline
    \textbf{Chapter} & \textbf{Subject}\\\hline
    ATA 21 & Air Conditioning\\
    ATA 24 & Electrical Power\\
    ATA 27 & Flight Controls\\
    ATA 32 & Landing Gear\\
    ATA 72 & Engine\\\hline
    \end{tabular}\end{center}
    Chapter $\to$ Section $\to$ Subject, e.g.\ \textbf{32-41-00}: Chapter 32 (Landing Gear),
    Section 41 (Wheels), Subject 00 (general)."""),
   ("Warning / Caution / Note Conventions",
    r"""\begin{center}
    \begin{tikzpicture}[node distance=0.4cm,>={Latex}]
      \node[draw,fill=red!15,rounded corners,text width=10.5cm,align=left] (w)
        {\textbf{WARNING:} Condition that, if ignored, could result in \underline{injury or death}.};
      \node[draw,fill=yellow!20,rounded corners,text width=10.5cm,align=left,below=of w] (c)
        {\textbf{CAUTION:} Condition that, if ignored, could result in \underline{equipment damage}.};
      \node[draw,fill=blue!10,rounded corners,text width=10.5cm,align=left,below=of c] (n)
        {\textbf{NOTE:} Additional information to \underline{aid the procedure}, no safety/damage risk.};
    \end{tikzpicture}
    \end{center}
    These three always appear \emph{before} the step they apply to, never after."""),
   ("Reading a Procedure: Imperative Mood",
    r"""AMM steps are written in the \textbf{imperative mood} (command form, no subject) --
    the implied subject is always ``you, the technician.''
    \begin{itemize}
    \item \emph{\underline{Disconnect} the battery.} \quad \emph{\underline{Remove} the access panel.}
    \item Passive sometimes replaces imperative for component-focused facts:
    \emph{The panel \underline{is secured} by eight screws.} (fact, not a command)
    \end{itemize}"""),
   ("Sample AMM Procedure -- Annotated",
    r"""\footnotesize
    \textbf{32-41-00 Wheel Removal}\\
    WARNING: Ensure the aircraft \underline{is supported}\emph{[passive]} on jacks \underline{before}
    \emph{[time prep.]} removing any wheel.\\
    1. Disconnect the brake line \underline{that is connected}\emph{[adj.\ clause, passive]}
    to the wheel assembly.\\
    2. \underline{If} \emph{[conditional]} the tire pressure \underline{exceeds}\emph{[simple
    present]} the AMM limit, deflate it \underline{before}\emph{[time prep.]} proceeding.\\
    3. Remove the axle nut; \underline{then}\emph{[sequence]} withdraw the wheel \underline{from}
    \emph{[prep.\ movement]} the axle."""),
   ("Decoding the Sample: Why Each Form Was Used",
    r"""\begin{itemize}
    \item Passive (\emph{is supported}) -- focus is on the aircraft's state, not who jacked it.
    \item Adjective clause (\emph{that is connected to...}) -- identifies exactly which brake line.
    \item Conditional (\emph{If...exceeds...}) -- a real, possible branch in the procedure.
    \item Sequence connector (\emph{then}) -- orders steps without renumbering.
    \item Preposition (\emph{from the axle}) -- precise direction of removal.
    \end{itemize}"""),
   ("Reading Strategy for Dense Technical Text",
    r"""\begin{enumerate}
    \item Find the main verb of each sentence first (often imperative or passive).
    \item Locate WARNING/CAUTION/NOTE blocks before reading the numbered steps.
    \item Resolve each adjective clause to confirm exactly which component is meant.
    \item Check every conditional (\emph{if/unless}) for a branch you must not skip.
    \item Cross-reference the ATA chapter number if a step says ``refer to...''
    \end{enumerate}"""),
   ("Practice 1 -- Problem",
    r"Identify the ATA chapter for ``Engine'' and explain the 32-41-00 numbering pattern."),
   ("Practice 1 -- Solution",
    r"""Engine = \textbf{ATA 72}.
    \\32-41-00 = Chapter 32 (Landing Gear) -- Section 41 (Wheels) -- Subject 00 (general)."""),
   ("Practice 2 -- Problem",
    r"In the sample procedure, label which grammar form each underlined phrase uses: \emph{``is supported''}, \emph{``that is connected''}, \emph{``If...exceeds''}."),
   ("Practice 2 -- Solution",
    r"""\emph{is supported} -- passive voice.
    \\\emph{that is connected} -- adjective clause (passive inside it).
    \\\emph{If...exceeds} -- first conditional (real possible condition)."""),
  ],
  I("AMM chapters follow the ATA iSpec 2200 numbering system (chapter-section-subject).",
    "WARNING/CAUTION/NOTE always precede the step they apply to.",
    "A single AMM sentence combines passive, adjective clauses, conditionals, and prepositions from every prior meeting."),
  I("Find and label one example each of passive, adjective clause, conditional, and preposition in a sample AMM page.",
    "Explain the ATA numbering of three given chapter codes.",
    "Rewrite one AMM step from passive into an imperative command."))

if __name__ == "__main__":
    order = [1,2,3,4,5,6,7,8]
    results = []
    for n in order:
        title, subclo, ind, slides, summ, asg = M[n]
        tex = build_deck(COURSE, SUBJECT, SUBTITLE, REF, CLO, n, title, subclo, ind, slides, summ, asg)
        results.append(compile_meeting(COURSE, n, tex))
        print(results[-1], flush=True)
    print("DONE", COURSE)
