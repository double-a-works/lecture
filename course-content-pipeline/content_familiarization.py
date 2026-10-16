#!/usr/bin/env python3
"""Basic_Aircraft_Familiarization — meetings 1-8 (first half). Build via build_slides."""
from build_slides import build_deck, compile_meeting

COURSE   = "Basic_Aircraft_Familiarization"
SUBJECT  = "BASIC AIRCRAFT FAMILIARIZATION"
SUBTITLE = "Fundamentals of Aircraft Structures, Systems, and Flight Controls"
REF      = "EASA Part-66 Module 11A -- Turbine Aeroplane Structures and Systems; FAA-H-8083-31 Aviation Maintenance Technician Handbook -- Airframe"
CLO = [
 "Explain aircraft classification and basic airframe anatomy (fuselage, wing, empennage, nacelle/pylon).",
 "Explain the aircraft axes of motion and the primary and secondary flight control systems along with their supporting structure (load path).",
 "Explain airframe materials and structures (metallic and composite) and the landing gear system.",
 "Explain the general working principles of the aircraft powerplant, fuel, hydraulic, and pneumatic systems.",
 "Explain basic electrical and instrument/avionics systems and apply documentation, marking, ground handling, and aircraft safety equipment procedures in accordance with regulations.",
]

I = lambda *xs: list(xs)

# Each meeting: (title, subclo, indicators, slides[(title,body)], summary, assignments)
M = {}

M[1] = ("Aviation Industry Overview \\& Aircraft Classification",
  "Students are able to explain the brief history, classification, and categories of aircraft.",
  I("Explain the brief history and development of the aviation industry.",
    "Classify aircraft by category and intended use.",
    "Identify the general external layout of a fixed-wing aircraft."),
  [("Why Study Aircraft Familiarization?",
    r"""This course is the entry point for every later Aeronautical Engineering subject.
    \begin{itemize}
    \item Every structural, propulsion, and avionics course assumes you already know the
    parts of an aircraft and their names.
    \item Since the Wright Brothers' discovery of powered flight about 100 years ago,
    the aviation sector has fundamentally changed the world.
    \item This meeting starts at the top: the aviation industry, its history, and how
    aircraft are classified.
    \end{itemize}"""),
   ("Aviation by the Numbers",
    r"""\begin{itemize}
    \item In 2019, the number of scheduled passengers boarded by the global airline
    industry reached over \textbf{4.54 billion people}.
    \item In Indonesia, in December 2017 the number of domestic aircraft passengers
    reached \textbf{8.34 million}, decreasing to \textbf{7.93 million} passengers in
    December 2019.
    \item These figures show why the aviation mechanic's role is vital to the national
    and global air transportation industry.
    \end{itemize}"""),
   ("The Aviation Mechanic's Role",
    r"""\begin{itemize}
    \item The Aviation Mechanic plays a vital part in the air transportation industry.
    \item The nature of the occupation requires both initial training and subsequent
    in-service training, providing the skills and technical knowledge needed to perform
    ``return-to-service'' work with the highest precision and efficiency possible.
    \item Technological advances in aviation occur at an extremely rapid rate, creating a
    continuous need for updated instructional programs for aviation maintenance technicians.
    \end{itemize}"""),
   ("Where the Word ``Aviation'' Comes From",
    r"""\begin{itemize}
    \item \textbf{Aviation} is a noun of action from the stem of the Latin \emph{avis}
    (``bird''), with the suffix \emph{-ation} meaning action or progress -- the art or
    act of flying.
    \item The term was coined in 1863 by the French pioneer Guillaume Joseph Gabriel de
    La Landelle (1812--1886) in ``Aviation ou Navigation aerienne sans ballons.''
    \end{itemize}"""),
   ("Nine Eras of Aircraft Development History",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Era & Period\\\hline
    1) Early Years & 200 BC -- 1860\\
    2) Pre-Powered Flight & 1860 -- 1903\\
    3) Early Powered Flight & 1903 -- 1914\\
    4) World War I & 1914 -- 1918\\
    5) Records Attempts & 1918 -- 1939\\
    6) World War II & 1939 -- 1945\\
    7) Jets and Speed & 1945 -- 1970s\\
    8) Efficiency & 1970s -- Present\\
    9) Space & 1950s -- Present\\\hline
    \end{tabular}\end{center}"""),
   ("Era 1: Early Years / Primitive Era (200 BC -- 1860 AD)",
    r"""\begin{enumerate}
    \item Tower jumping -- the Greek legend of Daedalus and Icarus.
    \item Man-carrying kites (China, 5th century BC).
    \item Rotor-wing toys (Chinese \emph{zhuqingting}, Japanese \emph{taketombo}, 400 BC).
    \item Hot air balloon (China, 3rd century BC -- the sky lantern).
    \item Renaissance (Leonardo da Vinci, 15th century).
    \end{enumerate}"""),
   ("Greek Mythology: Daedalus and Icarus",
    r"""\begin{itemize}
    \item Daedalus was a skilled craftsman and inventor, known for creating the Labyrinth
    on Crete.
    \item To escape King Minos, Daedalus fashioned wings for himself and his son Icarus,
    using feathers and wax.
    \item Despite his father's warnings, Icarus flew too close to the sun, causing the
    wax to melt and leading to his tragic fall into the sea.
    \end{itemize}"""),
   ("Renaissance Era: Leonardo da Vinci (1452--1519)",
    r"""\begin{itemize}
    \item Italian artist and inventor who produced the first drawing of a flying machine,
    and around 500 sketches in total.
    \item Foresaw the parachute, the helicopter, and the aircraft centuries before they
    were built.
    \item Conceived an early \textbf{ornithopter} -- a flying machine that flaps its
    wings like a bird.
    \end{itemize}"""),
   ("Lighter Than Air: The Montgolfier Brothers (1783)",
    r"""\begin{itemize}
    \item Etienne and Joseph Montgolfier flew the hot air balloon -- man's first flight.
    \item On 21 November 1783, an 8 km (5 mile) flight across the French city carried
    Pilatre de Rozier and the Marquis d'Arlandes.
    \item During the American Civil War (1862--1865), observation balloons were used to
    monitor troops and spot artillery.
    \end{itemize}"""),
   ("Lighter Than Air: Giffard and Cayley",
    r"""\begin{itemize}
    \item \textbf{Henri Giffard} (French, 1825--1882): in 1852, flew the first successful
    power-driven airship -- 143 feet long, fitted with a 3 HP steam engine.
    \item \textbf{Sir George Cayley} (1773--1857), the ``Father of Aerial Navigation'':
    in 1800 established many principles of aircraft design; in 1849 built a full-size
    glider and flew it a few meters, towed by a rope.
    \end{itemize}"""),
   ("Era 2: Pre-Powered Flight (1860 -- 1903)",
    r"""\begin{itemize}
    \item \textbf{Otto Lilienthal} (1890--1896), Germany's pioneer of gliding.
    \item \textbf{Nicolaus August Otto} (1832--1891): the first commercially successful
    internal combustion engine was created by Etienne Lenoir around 1860; the first
    modern internal combustion engine was created in 1876 by Nicolaus Otto.
    \end{itemize}"""),
   ("Era 3: Early Powered Flight (1903 -- 1914)",
    r"""Key figures of the era: Samuel Pierpont Langley, the Wright Brothers (Orville and
    Wilbur), Glenn Curtiss, Glenn L.\ Martin, Louis Bleriot, Cal Rogers, and Lincoln
    Beachey.
    \begin{itemize}
    \item Inventions: aircraft motors, propellers, three-axis flight controls, wheeled
    landing gear, and float planes.
    \item Records were set for speed, distance, and endurance; air races became popular
    in America and Europe.
    \end{itemize}"""),
   ("The Wright Brothers and Their Rivals",
    r"""\begin{itemize}
    \item \textbf{Samuel Pierpont Langley} (1834--1906): in October 1894, his Aerodrome
    No.\ 4 made a short hop of 130 feet over the Potomac River.
    \item \textbf{Wright Brothers} (1871--1948): first sustained, controlled powered
    flight in 1903.
    \item \textbf{Glenn Curtiss} (1878--1930): joined the Aerial Experiment Association
    in 1907, invited by Alexander Graham Bell; in 1908 built Aerodrome \#3, the famous
    \emph{June Bug}.
    \item \textbf{Louis Bleriot} (1872--1936), French inventor: first aircraft to fly
    across the English Channel, July 1909.
    \end{itemize}"""),
   ("Era 4: World War I (1914 -- 1918)",
    r"""Aircraft manufacturing countries: British, French, German, American, Italian.
    \begin{center}\begin{tabular}{l|l}\hline
    Aircraft & Origin / Note\\\hline
    Fokker Eindecker & German -- famous fighter with a synchronized machine gun\\
    Bristol Type 22 & British\\
    Siemens-Schuckert & German\\
    Sopwith Camel & British\\
    Handley Page 0/400 & British -- long-range bomber\\
    Gotha G V & German -- long-range bomber\\\hline
    \end{tabular}\end{center}
    What's new in the WWI era: increased horsepower engines (80--160 HP), rotary
    air-cooled and water-cooled engines, multi-engine aircraft, dirigibles (steered
    airships), and advanced armament."""),
   ("Era 5: Records Attempts (1918 -- 1930)",
    r"""\begin{itemize}
    \item \textbf{Charles Lindbergh}: self-trained pilot, flew air mail, made the first
    solo flight from New York to Paris across the Atlantic (1927); later a test pilot and
    national aviation expert.
    \item \textbf{Barnstorming}: stunt pilots performed tricks individually or in groups
    called flying circuses -- the first major form of civil aviation in the history of
    aviation. Pilots bought surplus WWI aircraft and flew them to fairs, selling rides
    and performing aerobatics.
    \item After WWI, aviation increased rapidly: surplus aircraft were readily available,
    numerous pilots were trained, and public interest in flying was great.
    \end{itemize}"""),
   ("Early Airlines and Early Airliners",
    r"""\begin{itemize}
    \item On 1 January 1914, the world's first scheduled passenger airline service took
    off, operating between St.\ Petersburg and Tampa, Florida -- the St.\ Petersburg-Tampa
    Airboat Line, using a Model 14 Benoist airboat (1,250 lb, 26 ft long, 44 ft wingspan,
    75 hp engine, top speed 64 mph). It lasted only four months but paved the way for
    today's daily transcontinental flights.
    \end{itemize}
    \begin{center}\begin{tabular}{l|l}\hline
    Airliner & Specification\\\hline
    Ford Tri-Motor & 3 engines, 100 mph cruise, 14 passengers\\
    Douglas DC-3 & 2 engines, 180 mph, 24 passengers\\\hline
    \end{tabular}\end{center}
    Pan American Airlines opened the world's first transatlantic passenger service in
    1939, between New York and Marseille, using amphibious aircraft."""),
   ("Era 6: World War II (1939 -- 1945)",
    r"""World War II involved all of the major countries of the world; aviation made
    giant advances during this period.
    \begin{itemize}
    \item Pressurized bomber cabins, all-weather flight, jet propulsion.
    \item Enormous numbers of aircraft produced; radar and radio navigation.
    \item Principal US cargo aircraft: C-46 Commando, C-47 Dakota, C-54 Skymaster, and
    C-69 Constellation.
    \item The US Army used its first helicopter in WWII: the Sikorsky R-4 Hoverfly.
    \end{itemize}"""),
   ("The First Jet Engines",
    r"""\begin{itemize}
    \item The first patent of a jet engine was issued in 1930 to \textbf{Sir Frank Whittle}.
    \item \textbf{1939}: the Heinkel He 178, the first jet-propelled aeroplane to fly,
    powered by Von Ohain's He S3B engine, made its first take-off on 27 August 1939 --
    the first jet aircraft to fly.
    \item What's new in WWII: turbocharged/supercharged piston engines, jet engines,
    rocket engines, long-range multi-engine aircraft, radio navigation and
    communication, and pressurized high-altitude aircraft.
    \end{itemize}"""),
   ("Era 7: Jets and Speed (1945 -- 1958)",
    r"""\begin{itemize}
    \item \textbf{4 October 1947}: Charles ``Chuck'' Yeager became the first person to
    fly beyond the speed of sound, reaching 1,015 km/h (670 mph) at 42,000 feet in the
    Bell X-1.
    \item A \textbf{sonic boom} is the sound produced when an object moving faster than
    the speed of sound creates shock waves that manifest as a loud, booming noise.
    \item Civilian aviation developed the Beech Bonanza and the Cessna 170, modernized
    versions of which are still in production today.
    \end{itemize}"""),
   ("The Jet Airliner Era Begins",
    r"""\begin{itemize}
    \item Early 1950s British jets led the way: the De Havilland Comet and the Vickers
    Viscount turboprop.
    \item \textbf{3 May 1952}: the first jet passenger airliner entered service, De
    Havilland Comet 1 ``G-ALYP, Yoke Peter,'' flying from London to Johannesburg.
    \item The American industry followed with the faster, longer-range Boeing 707 and
    Douglas DC-8; the 707 was the first jet ``Air Force One'' presidential aircraft.
    \item \textbf{9 February 1969}: the first ``Jumbo'' jet, the Boeing 747, made its
    first flight; the DC-10, Lockheed L-1011, and 747 became the very large jet airliners
    of the 1960s.
    \item \textbf{9 April 1969}: the first supersonic passenger airliner, Concorde, made
    its first flight.
    \end{itemize}"""),
   ("Records and Business Aviation in the Jet Age",
    r"""\begin{itemize}
    \item \textbf{6 November 1957}: the Fairey Rotodyne, the first VTOL (Vertical
    Take-Off and Landing) airliner -- a combined helicopter and autogyro that is also a
    fixed-wing aircraft, the old concept later used for the V-22 Osprey.
    \item Civilian business aviation entered the jet age with the turboprop-powered
    Beechcraft King Air and the jet-powered North American Sabreliner and Learjet.
    \end{itemize}"""),
   ("Era 8: Efficiency (1980s -- Present)",
    r"""\begin{itemize}
    \item \textbf{14--23 December 1986}: the Voyager aircraft flew nonstop and
    unrefuelled around the world in 9 days, 3 minutes, and 44 seconds, piloted by Dick
    Rutan and Jeana Yeager (wingspan 33.8 m / 111 ft).
    \item Commercial airliners were developed to be more economical to operate:
    derivative aircraft with more efficient engines (MD-11, B747-400); twin-engine
    designs with ETOPS (B757, B767, B777, A300, A310); today's efficient airliners
    (A350, A320, B787, B737).
    \item Retirement of quad-engine types (B747, A340, A380) has started for their
    earlier-built airframes.
    \end{itemize}"""),
   ("Era 9: Space Age (1958 -- Present)",
    r"""The Space Age is a period encompassing activities related to the space race,
    space exploration, and space technology.
    \begin{itemize}
    \item \textbf{16 July 1969}: Apollo 11 -- astronauts Neil Armstrong, Buzz Aldrin, and
    Michael Collins were launched atop the Saturn V rocket.
    \item \textbf{12 April 1981}: the first reusable spacecraft, the Space Shuttle, took off.
    \item \textbf{6 February 2018}: SpaceX's Falcon Heavy reusable side boosters landed
    in unison at Cape Canaveral, making SpaceX the operator of one of the world's most
    capable operational launch vehicles.
    \end{itemize}"""),
   ("Meet the Modern Fleet: Airbus A330-300",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Parameter & A330-300\\\hline
    Cockpit crew & Two\\
    Typical capacity & 300 (36J + 264Y), max seating 440\\
    Length / Wingspan & 63.67 m / 60.3 m\\
    MTOW / OEW & 242{,}000 kg / 129{,}400 kg\\
    Engines & 2 x Trent 700, 64{,}500--71{,}100 lbf each\\
    Cruise / Range & Mach 0.82 / 11{,}750 km\\\hline
    \end{tabular}\end{center}"""),
   ("Meet the Modern Fleet: Airbus A320 \\& Boeing 737-900ER",
    r"""\begin{center}\begin{tabular}{l|l|l}\hline
    Parameter & Airbus A320 & Boeing 737-900ER\\\hline
    Cockpit crew & Two & Two\\
    Typical capacity & 150 (2-class) & 177--215\\
    Length / Wingspan & 37.57 m / 35.8 m & 42.11 m / 34.32 m\\
    MTOW & 78 t & 85{,}139 kg\\
    Engines & 2 x CFM56-5B & 2 x CFM56-7B\\
    Cruise / Range & Mach 0.78 / 3{,}300 nmi & Mach 0.79 / 2{,}950 nmi\\\hline
    \end{tabular}\end{center}"""),
   ("Meet the Modern Fleet: ATR-72",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Parameter & ATR-72\\\hline
    Crew / Capacity & 2 / 70 seats at 30 in.\ pitch\\
    Length / Wingspan / Height & 27.17 m / 27.05 m / 7.65 m\\
    Empty weight / MTOW & 13{,}311 kg / 23{,}000 kg\\
    Powerplant & 2 x PW127M turboprop, 2{,}475 shp\\
    Cruise speed / Range & 510 km/h / 1{,}528 km (825 nmi)\\
    Service ceiling & 7{,}600 m (25{,}000 ft)\\\hline
    \end{tabular}\end{center}
    Turboprops like the ATR-72 fill the short-range regional role that jets are less
    fuel-efficient at, complementing the jet airliners covered on the previous slides."""),
   ("Branches of the Aviation Industry",
    r"""\begin{itemize}
    \item \textbf{Commercial aviation:} scheduled passenger and cargo airlines.
    \item \textbf{Military aviation:} fighters, transports, trainers, and support aircraft.
    \item \textbf{General aviation:} private, business, agricultural, and recreational flying.
    \item \textbf{MRO (Maintenance, Repair \& Overhaul):} keeps aircraft airworthy throughout their service life.
    \item \textbf{Manufacturing:} airframe, engine, and component makers supplying all the branches above.
    \end{itemize}"""),
   ("Manufacturing: Major Aircraft Manufacturers",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Manufacturer & Notable Products\\\hline
    Boeing (USA) & 737, 777, 787\\
    Airbus (Europe) & A320, A350, A380\\
    Embraer (Brazil) & E-Jet regional airliners\\
    ATR (France/Italy) & ATR 72 regional turboprop\\
    Bombardier (Canada) & Business jets (formerly regional jets)\\\hline
    \end{tabular}\end{center}"""),
   ("Aviation Regulatory Bodies",
    r"""\begin{itemize}
    \item \textbf{ICAO} (International Civil Aviation Organization) -- UN agency setting
    global standards that national regulators adopt.
    \item \textbf{FAA} (USA) and \textbf{EASA} (Europe) -- major regional certification authorities.
    \item \textbf{DGCA} (Indonesia) -- Directorate General of Civil Aviation, the national
    regulator this course's standards reference.
    \item \textbf{IATA} -- airline industry association setting operational and commercial standards.
    \end{itemize}
    Every aircraft type, airline, and maintenance organization operates under one or more
    of these regulatory frameworks."""),
   ("Classification by Wing Configuration",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Category & Description\\\hline
    Fixed-wing & Lift from wings moving through air at forward speed\\
    Rotary-wing & Lift from rotating blades (helicopters)\\
    Lighter-than-air & Buoyancy lift (balloons, airships)\\
    Monoplane & One pair of wings (modern standard)\\
    Biplane & Two stacked wing pairs (early aircraft, some aerobatic types)\\\hline
    \end{tabular}\end{center}"""),
   ("Classification by Powerplant Type",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Powerplant & Typical Use\\\hline
    Piston (reciprocating) & Light general-aviation aircraft, trainers\\
    Turboprop & Regional airliners, cargo, military transports\\
    Turbojet & Early jet airliners, some military fighters\\
    Turbofan & Modern airliners and business jets (most common today)\\\hline
    \end{tabular}\end{center}
    Powerplant details are covered in depth in Meetings 13--14."""),
   ("Classification by Number of Engines",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Configuration & Example\\\hline
    Single-engine & Small trainers, light GA aircraft\\
    Twin-engine & Most airliners and business jets\\
    Tri-jet & Older designs (e.g.\ McDonnell Douglas MD-11), now rare\\
    Quad-engine & Very large or long-range aircraft (e.g.\ Airbus A380)\\\hline
    \end{tabular}\end{center}
    More engines add redundancy and thrust but also weight, drag, and maintenance cost --
    modern twin-engine designs dominate because engine reliability has made extra engines
    less necessary."""),
   ("Classification by Category / Intended Use",
    r"""\begin{itemize}
    \item \textbf{Commercial transport:} passenger and cargo airliners.
    \item \textbf{Military:} fighter, bomber, trainer, transport, reconnaissance.
    \item \textbf{General aviation:} private, business, agricultural, experimental.
    \item \textbf{Special-purpose:} firefighting, medical evacuation, aerial survey.
    \end{itemize}
    A single airframe can sometimes serve more than one category (e.g.\ a transport
    aircraft adapted for military cargo)."""),
   ("Airworthiness Categories (Regulatory View)",
    r"""Regulators (EASA, FAA) define certification categories that shape design requirements.
    \begin{itemize}
    \item \textbf{CS-23 / Part 23:} normal, utility, aerobatic, and commuter small aircraft.
    \item \textbf{CS-25 / Part 25:} large transport-category aircraft (airliners).
    \item \textbf{CS-27/29 / Part 27/29:} normal and transport-category rotorcraft.
    \end{itemize}
    Category determines the structural and safety margins an aircraft must meet."""),
   ("Aircraft Size Classification by MTOW",
    r"""Maximum Take-Off Weight (MTOW) is a common way to size an aircraft.
    \begin{center}\begin{tabular}{l|l}\hline
    Class & Example\\\hline
    Light & Small GA aircraft (under 5{,}700 kg)\\
    Regional & Turboprop/regional jet (15--40 tonnes)\\
    Narrow-body & Single-aisle airliner (60--90 tonnes)\\
    Wide-body & Twin-aisle airliner (150--300+ tonnes)\\
    Very large & A380-class (500+ tonnes)\\\hline
    \end{tabular}\end{center}"""),
   ("Classification by Range",
    r"""\begin{center}\begin{tabular}{l|l|l}\hline
    Category & Typical Range & Example\\\hline
    Short-haul & Under 1{,}500 km & Regional turboprop\\
    Medium-haul & 1{,}500--4{,}000 km & Narrow-body airliner\\
    Long-haul & Over 4{,}000 km & Wide-body airliner\\\hline
    \end{tabular}\end{center}
    Range depends on fuel capacity, structural weight, and engine efficiency --
    all topics covered later in this course."""),
   (r"Narrow-Body vs.\ Wide-Body Aircraft",
    r"""\begin{center}\begin{tabular}{l|l|l}\hline
    Aspect & Narrow-Body & Wide-Body\\\hline
    Cabin aisles & One & Two\\
    Typical use & Short/medium-haul & Long-haul\\
    Example & Boeing 737, Airbus A320 & Boeing 777, Airbus A350\\\hline
    \end{tabular}\end{center}"""),
   ("General External Layout of a Fixed-Wing Aircraft",
    r"""Picture a typical airliner from the side and label its five major sections:
    \begin{enumerate}
    \item \textbf{Fuselage} -- the main body, housing the cockpit, cabin, and cargo.
    \item \textbf{Wings} -- mounted left and right of the fuselage, generating lift.
    \item \textbf{Empennage} -- the tail assembly, providing stability and control.
    \item \textbf{Powerplant} -- engines, mounted on the wing, fuselage, or tail.
    \item \textbf{Landing gear} -- wheels supporting the aircraft on the ground.
    \end{enumerate}
    Every later meeting in this course studies one or more of these five sections in detail."""),
   (r"Comparison: Fixed-Wing vs.\ Rotary-Wing Aircraft",
    r"""\begin{center}\begin{tabular}{l|l|l}\hline
    Aspect & Fixed-Wing & Rotary-Wing\\\hline
    Takeoff/landing & Needs a runway & Vertical takeoff/landing\\
    Cruise speed & Generally higher & Generally lower\\
    Hover capability & No & Yes\\
    Typical role & Long-range transport & Rescue, utility, short-range\\\hline
    \end{tabular}\end{center}"""),
   ("Reading an Aircraft Type Designator",
    r"""Aircraft type codes follow manufacturer-specific patterns.
    \begin{itemize}
    \item \textbf{B738} = Boeing 737-800; \textbf{A320} = Airbus A320.
    \item The number in the family name usually indicates the specific variant (e.g.\
    737-700 vs.\ 737-800 differ mainly in fuselage length and capacity).
    \item Recognizing type codes lets maintenance, ATC, and operations staff communicate
    exact aircraft variants quickly and unambiguously.
    \end{itemize}"""),
   ("Aircraft Identification: Registration Marks",
    r"""\begin{itemize}
    \item Every aircraft carries a unique \textbf{registration mark} (tail number), assigned
    by its country of registration.
    \item Indonesian-registered aircraft use the prefix \textbf{PK-} (e.g.\ PK-XXX).
    \item The registration links the specific airframe to its maintenance records,
    airworthiness certificate, and ownership history.
    \item Detailed documentation and marking requirements are covered in Meeting 16.
    \end{itemize}"""),
   ("Case Study: Wright Flyer to Modern Airliner",
    r"""\begin{center}\begin{tabular}{l|l|l}\hline
    Aspect & Wright Flyer (1903) & Modern Airliner\\\hline
    Structure & Wood, fabric, wire bracing & Aluminum/composite semi-monocoque\\
    Powerplant & 12 hp piston engine & Turbofan engines (tens of thousands of hp equiv.)\\
    Range & About 260 m (first flight) & Thousands of kilometers\\
    Crew/passengers & 1 pilot & 2 pilots, 100s of passengers\\\hline
    \end{tabular}\end{center}
    Every later meeting in this course explains one piece of how that gap was closed."""),
   ("Case Study: Composite Materials and the 787",
    r"""\begin{itemize}
    \item The Boeing 787 was the first airliner built with an airframe that is roughly
    half composite material by weight (fuselage and wings).
    \item Composites are lighter than aluminum for the same strength, reducing fuel burn.
    \item This shift changed how modern airliners are classified and maintained --
    covered in depth in Meetings 10--11.
    \end{itemize}"""),
   ("Common Misconceptions in Aircraft Classification",
    r"""\begin{itemize}
    \item \textbf{Myth:} more engines always means a safer aircraft. \textbf{Fact:} modern
    twin-engine reliability makes extra engines mostly unnecessary for safety.
    \item \textbf{Myth:} wide-body always means larger passenger capacity than narrow-body.
    \textbf{Fact:} a long narrow-body can carry more passengers than a short wide-body.
    \item \textbf{Myth:} classification by category and by certification basis (CS-23/CS-25)
    are the same thing. \textbf{Fact:} they are related but separate systems.
    \end{itemize}"""),
   ("Applied Scenario: Identifying an Unfamiliar Aircraft",
    r"""You are on the ramp and see an aircraft you do not recognize. Work through these
    questions in order:
    \begin{enumerate}
    \item How many wings, and in what configuration (mono/biplane)?
    \item Where are the engines mounted, and how many are there?
    \item What is the tail configuration (conventional, T-tail, etc.)?
    \item Based on size and layout, what category does it likely belong to?
    \end{enumerate}
    This same systematic approach is used throughout the course to describe any aircraft."""),
   ("Applied Scenario: Classifying by Silhouette",
    r"""From a distance, an aircraft's silhouette alone reveals much of its classification.
    \begin{enumerate}
    \item Tail shape (conventional, T-tail, V-tail) narrows down the empennage type.
    \item Wing sweep angle hints at cruise speed (straight = slow, swept = fast jet).
    \item Number and position of engines (wing-mounted, tail-mounted) narrows the aircraft family.
    \end{enumerate}
    Experienced ramp and ATC personnel identify aircraft types this way routinely."""),
   ("Applied Scenario: Choosing an Aircraft for a Mission",
    r"""A charter operator needs to move 150 passengers 3{,}000 km. Work through the choice:
    \begin{enumerate}
    \item Passenger count and range point toward a narrow-body, medium-haul airliner.
    \item Twin-engine turbofan is the standard powerplant choice for this mission size.
    \item A wide-body would be oversized for this mission, while a regional turboprop
    lacks the range.
    \end{enumerate}"""),
   ("In-Class Practice",
    r"""Discuss with a partner, then check with the instructor:
    \begin{enumerate}
    \item Name three branches of the aviation industry and one aircraft type typical of each.
    \item Classify a small twin-engine turboprop airliner by wing configuration, powerplant, and category.
    \item Explain why certification category (e.g.\ CS-23 vs.\ CS-25) affects aircraft design.
    \end{enumerate}"""),
   ("Extended In-Class Practice / Group Discussion",
    r"""In small groups, discuss and be ready to present:
    \begin{enumerate}
    \item Pick a real airliner (any type). Classify it by wing configuration, powerplant,
    number of engines, size class, and range category.
    \item Debate: for a new regional airline, would you choose a narrow-body jet or a
    turboprop? Justify with range, passenger count, and airport infrastructure.
    \item Identify one historical milestone (pre-jet or jet-age) and explain how it changed
    aircraft classification or capability.
    \end{enumerate}""")],
  I("The aviation industry spans commercial, military, general aviation, MRO, and manufacturing.",
    "Aircraft are classified by wing configuration, powerplant type, and intended use.",
    "A fixed-wing aircraft's five major sections are fuselage, wings, empennage, powerplant, and landing gear."),
  I("List the five major external sections of a fixed-wing aircraft.",
    "Classify a given aircraft by wing configuration and powerplant type.",
    "Explain the difference between CS-23 and CS-25 certification categories.",
    "Describe one historical milestone that changed commercial aviation."))

M[2] = ("Aircraft Anatomy: Fuselage \\& Wing",
  "Students are able to identify and explain the function of the fuselage and wing.",
  I("Explain the functions of the fuselage.",
    "Explain the structural types of the fuselage.",
    "Explain the functions and configurations of the wing."),
  [("Why Fuselage and Wing Anatomy Matters",
    r"""The fuselage and wing are the two largest structural assemblies of an aircraft.
    \begin{itemize}
    \item The fuselage houses crew, passengers, cargo, and systems, and ties every other
    structure together.
    \item The wing generates the lift that keeps the aircraft airborne.
    \item Correctly naming their zones and configurations is essential before studying
    structure (Meeting 6) or flight controls (Meetings 4--5).
    \end{itemize}"""),
   ("Fuselage Functions",
    r"""\begin{itemize}
    \item Houses the flight crew, passengers, and cargo.
    \item Provides the central structural backbone connecting wings, empennage, and
    (on many designs) the landing gear and engines.
    \item Carries and protects avionics, environmental control, and other systems.
    \item Must resist bending, torsion, and internal pressurization loads simultaneously.
    \end{itemize}"""),
   ("Fuselage Pressurization Basics",
    r"""\begin{itemize}
    \item At cruise altitude, outside air pressure is too low to breathe comfortably --
    the fuselage cabin is pressurized to a comfortable equivalent altitude.
    \item The fuselage skin and frames must resist this pressure difference on every flight,
    in addition to flight loads -- a cycle repeated on every takeoff and landing.
    \item This is a major reason the fuselage uses a circular or near-circular cross-section:
    a circle spreads pressure load evenly, with no weak corners.
    \end{itemize}"""),
   ("Fuselage Doors and Emergency Exits",
    r"""\begin{itemize}
    \item \textbf{Passenger/crew doors:} main boarding doors, usually plug-type so cabin
    pressure helps seal them shut in flight.
    \item \textbf{Emergency exits:} additional exits (often over the wing) sized and spaced
    by regulation for rapid evacuation.
    \item \textbf{Cargo doors:} larger, often on the fuselage side, for loading freight and baggage.
    \item Every door cutout is a structural discontinuity that must be reinforced --
    a preview of the stress-concentration concept in Meeting 6.
    \end{itemize}"""),
   ("Fuselage Structural Types",
    r"""The fuselage can be divided into four structural categories:
    \begin{center}\begin{tabular}{l|l}\hline
    Type & Description\\\hline
    Truss & Welded/bolted framework of struts; skin carries little load\\
    Geodetic & Lattice of spiraling, load-sharing structural members under the skin\\
    Monocoque & Skin alone carries the load, built up from bulkhead, former, and skin\\
    Semi-monocoque & Skin, longeron, stringer, former, ring, and bulkhead share the load\\\hline
    \end{tabular}\end{center}
    Almost all modern aircraft use semi-monocoque fuselage construction, detailed further
    in Meeting 6."""),
   ("Monocoque and Semi-Monocoque Components",
    r"""\begin{itemize}
    \item \textbf{Monocoque} construction consists of several parts: \emph{bulkhead},
    \emph{former}, and \emph{skin} -- the skin itself is the primary load-carrying member.
    \item \textbf{Semi-monocoque} construction consists of: \emph{skin}, \emph{longeron},
    \emph{stringer}, \emph{former}, \emph{ring}, and \emph{bulkhead} -- an internal frame
    shares the load with the skin.
    \item \textbf{Truss} and \textbf{Geodetic} airframes came earlier: truss uses a welded
    strut framework, while geodetic uses a spiraling lattice of load-sharing members,
    both typically covered with a non-structural or lightly loaded skin.
    \end{itemize}"""),
   ("Fuselage Materials Overview (Preview)",
    r"""\begin{itemize}
    \item Most fuselages today are built from \textbf{aluminum alloys} -- light, strong,
    and well understood after decades of service history.
    \item Newer designs (e.g.\ Boeing 787) use \textbf{carbon-fiber composite} fuselage
    barrels -- lighter still, and resistant to fatigue cracking.
    \item Material choice affects manufacturing method, inspection technique, and repair
    procedure -- the full comparison is covered in Meetings 10--11.
    \end{itemize}"""),
   ("Fuselage Zones",
    r"""A transport aircraft fuselage is commonly divided into zones along its length:
    \begin{itemize}
    \item \textbf{Nose section} -- radome, avionics bay, sometimes nose landing gear.
    \item \textbf{Cockpit (flight deck)} -- crew stations and flight instruments.
    \item \textbf{Cabin} -- passenger seating or cargo compartment.
    \item \textbf{Tail cone} -- aft structure connecting the cabin to the empennage.
    \end{itemize}"""),
   ("Fuselage Nose Section in Detail",
    r"""\begin{itemize}
    \item \textbf{Radome:} the rounded, non-metallic nose cap that houses the weather radar
    antenna while letting radar signals pass through.
    \item Below/behind the radome sits the \textbf{avionics bay}, holding flight computers
    and electronic equipment, often with external access panels.
    \item On many transport aircraft, the \textbf{nose landing gear} retracts into a bay
    just aft of the avionics compartment.
    \end{itemize}"""),
   ("Fuselage Cargo Compartment",
    r"""\begin{itemize}
    \item Located below the passenger cabin floor on most transport aircraft.
    \item Divided into forward and aft cargo holds, separated by the wing center-section structure.
    \item Often \textbf{unpressurized-adjacent} but still temperature-controlled, and fitted
    with fire-detection and suppression systems.
    \item Cargo doors are typically larger and structurally reinforced compared to
    passenger doors.
    \end{itemize}"""),
   (r"Fuselage Cross-Section: Single-Aisle vs.\ Twin-Aisle Cabin",
    r"""\begin{center}\begin{tabular}{l|l|l}\hline
    Aspect & Single-Aisle & Twin-Aisle\\\hline
    Typical seating & 3--3 or 3--2 across & 2--4--2 or 3--3--3 across\\
    Boarding/deplaning & Slower (one aisle) & Faster (two aisles)\\
    Typical fuselage diameter & About 3.5--4 m & About 5--6 m\\\hline
    \end{tabular}\end{center}
    This ties directly to the narrow-body/wide-body classification introduced in Meeting 1."""),
   ("Wing Functions",
    r"""\begin{itemize}
    \item Primary function: generate \textbf{lift} to support the aircraft's weight in flight.
    \item Often houses fuel tanks (integral or bladder tanks within the wing structure).
    \item Provides the mounting point for primary and secondary flight control surfaces
    (Meetings 4--5) and, on many aircraft, the engines.
    \item Transfers aerodynamic loads inward to the fuselage through its structure.
    \end{itemize}"""),
   ("Wing Fuel Tank Types",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Type & Description\\\hline
    Integral (wet wing) & Wing structure itself sealed to hold fuel directly; most common\\
    Bladder tank & Flexible fuel cell fitted inside the wing cavity; older/lighter aircraft\\
    Auxiliary/center tank & Extra tank in the fuselage center section for range\\\hline
    \end{tabular}\end{center}"""),
   ("Wing-to-Fuselage Attachment (Carry-Through Structure)",
    r"""\begin{itemize}
    \item The two wing halves are joined to the fuselage through a heavy \textbf{center-wing
    box}, sometimes called the carry-through structure.
    \item This structure transfers wing bending and shear loads from one wing, across the
    fuselage, to the opposite wing.
    \item It is one of the most heavily loaded and most closely inspected parts of the
    entire airframe.
    \end{itemize}"""),
   ("Wing-to-Fuselage Fairing",
    r"""\begin{itemize}
    \item A streamlined panel covering the joint where the wing meets the fuselage.
    \item Smooths airflow across the junction, reducing drag ("interference drag") that
    would otherwise occur at a sharp intersection.
    \item Also conceals wiring, plumbing, and structural fittings that cross between the
    wing and fuselage.
    \end{itemize}"""),
   ("Leading Edge and Trailing Edge Terminology",
    r"""\begin{itemize}
    \item \textbf{Leading edge:} the forward-most edge of the wing, first to meet the
    oncoming air; often houses slats (Meeting 5) and anti-ice systems.
    \item \textbf{Trailing edge:} the rear-most edge of the wing; carries the ailerons and
    flaps (Meetings 4--5).
    \item Every flight control surface studied later in this course is described relative
    to these two reference edges.
    \end{itemize}"""),
   ("The Bernoulli Principle",
    r"""\begin{itemize}
    \item The narrow part of a pipe becomes a venturi, speeding up the flow through it --
    this same effect is used in the upper part of a wing's airfoil shape.
    \item Air moving faster over the curved upper surface produces lower pressure than the
    slower air beneath, and that pressure difference is a key source of lift.
    \end{itemize}"""),
   ("Airfoil Terminology",
    r"""\begin{itemize}
    \item \textbf{Chord line:} the straight line connecting the leading edge (LE) and
    trailing edge (TE).
    \item \textbf{Camber line:} the line that divides the airfoil into equal upper and
    lower areas.
    \item \textbf{Angle of attack:} the angle created between the relative wind and the
    airfoil chord line.
    \item \textbf{Maximum camber:} the farthest distance between the chord line and the
    camber line.
    \end{itemize}"""),
   ("Number of Wings: Monoplane and Biplane",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Configuration & Description\\\hline
    Monoplane & One pair of wings -- the modern standard\\
    Biplane & Two stacked pairs of wings -- common on early aircraft\\\hline
    \end{tabular}\end{center}"""),
   ("Wing Position: High, Mid, Low, and Parasol",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Position & Typical Use\\\hline
    High wing & Cargo/utility aircraft -- easier ground loading, more ground clearance\\
    Mid wing & Aerobatic, some military -- balanced aerodynamics\\
    Low wing & Most airliners, fighters -- shorter landing gear, easier fuel/engine access\\
    Parasol wing & Mounted above the fuselage on struts, not fused to it\\\hline
    \end{tabular}\end{center}"""),
   ("Cantilever and Semi-Cantilever Wings",
    r"""\begin{itemize}
    \item \textbf{Semi-cantilever:} the wing load is supported by external bracing (struts
    or wires running from the wing to the fuselage or landing gear).
    \item \textbf{Cantilever:} the wing is not equipped with external bracing -- the wing
    structure alone carries all the load, as on nearly all modern aircraft.
    \end{itemize}"""),
   ("Parts of Wing Construction",
    r"""\begin{itemize}
    \item \textbf{Spar} -- the main wing structure.
    \item \textbf{Rib} -- gives the wing its airfoil shape.
    \item \textbf{Skin} -- the aerodynamic contour.
    \item \textbf{Stringer} (or stiffener) -- helps withstand load stress.
    \end{itemize}"""),
   ("Spar and Rib in Detail",
    r"""\begin{itemize}
    \item \textbf{Spar:} the main wing structure; made of metal or wood; parallel to the
    lateral axis; designed to withstand bending and shear stress.
    \item \textbf{Rib:} shapes the wing airfoil, and is also used in flight control and
    stabilizer construction; made of metal or wood; parallel to the longitudinal axis.
    \end{itemize}"""),
   ("Skin and Stringer",
    r"""\begin{itemize}
    \item \textbf{Skin} provides the aerodynamic contour and is the first member to
    withstand aerodynamic stress.
    \item \textbf{Stringer} is a part of the wing which helps the structure withstand
    load stress, running along the span between the ribs.
    \end{itemize}"""),
   ("Functions Built Into the Wing",
    r"""\begin{itemize}
    \item \textbf{Access panel} -- for maintenance access to internal components.
    \item \textbf{Drain hole} -- lets moisture and fuel condensation escape the structure.
    \item \textbf{Walkway} -- a reinforced area where technicians can safely step.
    \item \textbf{Jacking point} -- a reinforced point used to lift the aircraft with a jack.
    \end{itemize}"""),
   (r"High-Wing vs.\ Low-Wing: Ground Operations Deep-Dive",
    r"""\begin{itemize}
    \item \textbf{High-wing:} propellers/engines sit higher off the ground, reducing
    foreign-object-damage (FOD) risk on unpaved strips; cargo loads directly under the wing.
    \item \textbf{Low-wing:} landing gear can be shorter (mounted in the wing), saving
    structural weight; fuel and engine access is easier from ground level with simple stands.
    \item Airlines overwhelmingly choose low-wing for airliners because of the landing-gear
    weight saving; utility/cargo operators often prefer high-wing for ground clearance.
    \end{itemize}"""),
   ("Wing Geometry: Dihedral and Anhedral",
    r"""\begin{itemize}
    \item \textbf{Dihedral:} wingtips angled \emph{upward} from the wing root; improves
    lateral (roll) stability by resisting sideslip.
    \item \textbf{Anhedral:} wingtips angled \emph{downward}; reduces excess lateral stability,
    common on high-wing aircraft that are already very stable in roll.
    \item Most low-wing airliners use dihedral; most high-wing utility aircraft use little
    or slight anhedral.
    \end{itemize}"""),
   ("Wing Twist (Washout)",
    r"""\begin{itemize}
    \item \textbf{Washout:} the wingtip is built with a slightly lower angle of incidence
    than the wing root, so the tip flies at a lower angle of attack than the root.
    \item This makes the wing root stall \emph{before} the tip, keeping aileron control
    effective even as the aircraft approaches a stall.
    \item Washout is a built-in structural/aerodynamic safety feature, not a moving part.
    \end{itemize}"""),
   (r"Wing Root vs.\ Wing Tip",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Wing Root (near fuselage) & Wing Tip (outboard end)\\\hline
    Thickest, most heavily loaded section & Thinnest section, lightest loads\\
    Larger chord (in tapered wings) & Smaller chord\\
    Carries wing-to-fuselage attachment & Often carries a wingtip device\\\hline
    \end{tabular}\end{center}"""),
   ("Wingtip Devices: Winglets and Sharklets",
    r"""\begin{itemize}
    \item \textbf{Winglets/sharklets} are small near-vertical extensions at the wingtip.
    \item They reduce \textbf{wingtip vortices} -- swirling airflow that spills from the
    high-pressure lower surface to the low-pressure upper surface at the tip.
    \item Reducing these vortices lowers induced drag, improving fuel efficiency without
    increasing wingspan (which is limited by airport gate size).
    \end{itemize}"""),
   ("Wing Efficiency: Span and Aspect Ratio (Concept)",
    r"""\begin{itemize}
    \item \textbf{Wingspan:} tip-to-tip distance across the wing.
    \item \textbf{Aspect ratio:} qualitatively, how long and narrow the wing is compared to
    its average width (chord).
    \item Long, narrow wings (high aspect ratio) are aerodynamically efficient -- used on
    gliders and long-range airliners.
    \item Short, wide wings (low aspect ratio) are more structurally compact and maneuverable --
    common on fighters.
    \end{itemize}"""),
   ("Case Study: Cabin Pressurization and Fuselage Integrity",
    r"""\begin{itemize}
    \item In 1954, two de Havilland Comet airliners broke apart in flight due to metal
    fatigue cracks starting at square window cutouts, under repeated pressurization cycling.
    \item The fix: later aircraft (including the Comet itself) adopted \textbf{rounded window
    and door cutouts} to avoid the sharp-corner stress concentration.
    \item This single incident permanently changed how every fuselage cutout is designed --
    a direct link to the stress-concentration concept in Meeting 6.
    \end{itemize}"""),
   ("Case Study: Winglet Fuel Savings",
    r"""\begin{itemize}
    \item Airlines retrofitting older narrow-body aircraft with winglets have reported
    fuel savings of roughly 3--5 percent on typical medium-haul routes.
    \item The saving comes almost entirely from reduced induced drag (fewer wingtip vortices),
    not from any change in wing area.
    \item Because winglets add wingspan-equivalent efficiency without exceeding airport gate
    span limits, most new-generation narrow-bodies (737 MAX, A320neo) include them from
    the factory.
    \end{itemize}"""),
   ("Applied Scenario: Reading a Wing and Fuselage from a Photo",
    r"""Given a side and front photo of an unfamiliar aircraft, work through:
    \begin{enumerate}
    \item Is the wing mounted high, low, or mid on the fuselage?
    \item Is the wing planform straight, tapered, swept, or delta?
    \item Is the fuselage shape consistent with truss, monocoque, or semi-monocoque construction?
    \end{enumerate}
    These same observations are the first step of every structural inspection."""),
   ("Applied Scenario: Estimating Passenger Capacity from Fuselage Width",
    r"""Given a fuselage cross-section, capacity can be estimated in three steps:
    \begin{enumerate}
    \item Measure fuselage internal width to judge seat-abreast count (e.g.\ 6-abreast for
    narrow-body, 8--10-abreast for wide-body).
    \item Count the number of aisles (one for narrow-body, two for wide-body) from the cross-section.
    \item Combine abreast count with typical seat pitch to estimate rows, then total seats.
    \end{enumerate}"""),
   ("Applied Scenario: Identifying Wingtip Device Type",
    r"""Looking at a wingtip from the front of the aircraft:
    \begin{enumerate}
    \item No extension, wing simply ends -- a plain (non-optimized) wingtip.
    \item A small upward blended curve -- a winglet or sharklet.
    \item A split surface angling both up and down -- a split-scimitar winglet, a further
    refinement seen on some re-engined narrow-bodies.
    \end{enumerate}"""),
   ("In-Class Practice",
    r"""\begin{enumerate}
    \item Name the three fuselage structural types and identify which is used by nearly
    all modern aircraft.
    \item List three functions of the wing besides generating lift.
    \item Explain the difference between dihedral and anhedral, and give an aircraft
    type typical of each.
    \end{enumerate}"""),
   ("Extended In-Class Practice / Group Discussion",
    r"""In small groups, discuss and be ready to present:
    \begin{enumerate}
    \item Sketch a fuselage cross-section and label pressurization-relevant features
    (skin, frame, window cutout).
    \item Debate: for a new short-haul feeder aircraft, would you specify a high-wing or
    low-wing configuration? Justify using ground-operations trade-offs.
    \item Explain, in your own words, how the Comet failures changed fuselage cutout design.
    \end{enumerate}""")],
  I("The fuselage houses crew/cargo and ties the airframe together; semi-monocoque is the modern standard.",
    "The wing generates lift, stores fuel, and mounts flight controls and often engines.",
    "Wing position (high/low/mid) and geometry (dihedral/anhedral) affect stability and ground handling."),
  I("Sketch and label the four fuselage zones of a transport aircraft.",
    "Compare truss, monocoque, and semi-monocoque fuselage construction.",
    r"Explain how wing position (high vs.\ low) affects ground operations.",
    "Explain the stability effect of dihedral versus anhedral wings."))

M[3] = ("Aircraft Anatomy: Empennage, Nacelle \\& Pylon",
  "Students are able to identify and explain the function of the empennage, nacelle, and pylon.",
  I("Explain the function of the empennage and its components.",
    "Explain the function of the nacelle.",
    "Explain the function of the pylon."),
  [("Why the Tail and Engine Mounts Matter",
    r"""After the fuselage and wing (Meeting 2), the remaining external assemblies provide
    \textbf{stability} and \textbf{propulsion integration}.
    \begin{itemize}
    \item The empennage keeps the aircraft stable and controllable in pitch and yaw.
    \item The nacelle and pylon safely house and mount the engine(s) to the airframe.
    \item Together with the fuselage and wing, these complete the whole-aircraft picture
    needed before studying flight controls (Meeting 4).
    \end{itemize}"""),
   ("Empennage Overview and Functions",
    r"""The \textbf{empennage} (tail assembly) is mounted at the rear of the fuselage.
    \begin{itemize}
    \item Provides \textbf{longitudinal stability} (pitch) and \textbf{directional stability} (yaw).
    \item Houses the primary pitch and yaw control surfaces.
    \item Typically consists of a horizontal stabilizer and a vertical stabilizer.
    \end{itemize}"""),
   ("Empennage Structural Members (Preview)",
    r"""\begin{itemize}
    \item Like the wing (Meeting 2), the empennage has its own spars, ribs, and skin.
    \item The \textbf{fin spar} and \textbf{stabilizer spar} carry bending loads from
    aerodynamic forces on the tail surfaces into the rear fuselage.
    \item Because tail surfaces are smaller than the wing but must resist gust and control
    loads, their structure is proportionally very stiff for its size.
    \end{itemize}"""),
   ("Horizontal Stabilizer and Elevator",
    r"""\begin{itemize}
    \item \textbf{Horizontal stabilizer:} the fixed horizontal surface; resists unwanted
    pitching and keeps the nose steady in cruise.
    \item \textbf{Elevator:} the hinged, movable trailing-edge surface on the horizontal
    stabilizer; deflecting it changes pitch (nose up/down).
    \item On some aircraft, the entire horizontal stabilizer moves (a "stabilator") instead
    of using a separate elevator.
    \end{itemize}"""),
   ("Horizontal Stabilizer Trim (Trimmable Stabilizer)",
    r"""\begin{itemize}
    \item On most transport aircraft, the entire horizontal stabilizer can be slowly
    repositioned (trimmed) in addition to the elevator moving on its trailing edge.
    \item This is called a \textbf{trimmable horizontal stabilizer (THS)}, distinct from the
    small trim tabs covered in Meeting 5.
    \item Trimming the stabilizer relieves the constant elevator force needed to hold a
    given pitch attitude, especially as fuel burns off and the center of gravity shifts.
    \end{itemize}"""),
   ("Stabilator Deep-Dive",
    r"""\begin{itemize}
    \item A \textbf{stabilator} is a single horizontal tail surface that pivots as a whole
    to control pitch, replacing the separate fixed-stabilizer-plus-elevator arrangement.
    \item Common on some light aircraft and high-speed military jets, where a small elevator
    alone would lose effectiveness at high speed.
    \item Often fitted with a small \textbf{anti-servo tab} that moves with the stabilator
    to increase the pilot's control feel, since a stabilator alone can feel too sensitive.
    \end{itemize}"""),
   (r"Elevator vs.\ Stabilator Comparison",
    r"""\begin{center}\begin{tabular}{l|l|l}\hline
    Aspect & Elevator (on fixed stabilizer) & Stabilator\\\hline
    Moving surface & Trailing-edge tab only & Entire horizontal tail\\
    Typical use & Most transport/GA aircraft & Some light aircraft, high-speed jets\\
    Pitch authority at speed & Can reduce at high speed & Remains effective at high speed\\\hline
    \end{tabular}\end{center}"""),
   ("Vertical Stabilizer and Rudder",
    r"""\begin{itemize}
    \item \textbf{Vertical stabilizer (fin):} the fixed vertical surface; resists unwanted
    yawing and keeps the nose pointed into the relative wind.
    \item \textbf{Rudder:} the hinged, movable trailing-edge surface on the vertical
    stabilizer; deflecting it changes yaw (nose left/right).
    \item Rudder and elevator functions are studied further as primary flight controls
    in Meeting 4.
    \end{itemize}"""),
   ("Dorsal Fin",
    r"""\begin{itemize}
    \item A small, fixed fin-like extension running forward from the base of the vertical
    stabilizer along the upper fuselage.
    \item Adds directional (yaw) stability at high angles of sideslip, when the main
    vertical stabilizer alone could stall aerodynamically.
    \item Visually recognizable as the smooth ``blend'' between the fuselage spine and the
    leading edge of the fin.
    \end{itemize}"""),
   ("Ventral Fin",
    r"""\begin{itemize}
    \item A small fixed fin mounted under the rear fuselage, below the horizontal stabilizer.
    \item Improves directional stability and helps prevent a dangerous ``deep stall'' or
    spin on some tail configurations, particularly T-tails.
    \item Also protects the rear fuselage from tail strikes during a nose-high takeoff
    or landing.
    \end{itemize}"""),
   ("Rudder Travel Limiter (Concept)",
    r"""\begin{itemize}
    \item A system that automatically reduces the maximum rudder deflection available as
    airspeed increases.
    \item At high speed, full rudder deflection could overstress the vertical stabilizer --
    the limiter protects the structure while still allowing full authority at low speed.
    \item This is a preview of how flight control authority is matched to structural limits,
    a theme that returns in Meeting 6 (load path) and later avionics meetings.
    \end{itemize}"""),
   ("Tail Cone: The Rearmost Fuselage Section",
    r"""\begin{itemize}
    \item The \textbf{tail cone} is the rearmost area of the fuselage; the stabilizer is
    normally installed on the tail cone.
    \item Other parts are sometimes installed in the tail cone as well: passenger door
    and stair, cargo door, engine, Auxiliary Power Unit (APU), and speed brake.
    \end{itemize}"""),
   ("Empennage Configurations",
    r"""Normally, there are three types of empennage:
    \begin{center}\begin{tabular}{l|l}\hline
    Configuration & Description\\\hline
    Conventional & Horizontal stabilizer mounted low on the fuselage, below the fin tip\\
    T-type & Horizontal stabilizer mounted at the top of the vertical fin\\
    V-type & Two slanted surfaces equipped with a \emph{ruddervator}\\\hline
    \end{tabular}\end{center}"""),
   ("T-Tail: Advantages and Disadvantages",
    r"""\begin{itemize}
    \item \textbf{Advantage:} horizontal stabilizer sits clear of engine exhaust and wing
    wake, giving cleaner airflow and more consistent pitch control.
    \item \textbf{Advantage:} keeps the horizontal surfaces away from rear-mounted engines.
    \item \textbf{Disadvantage:} the vertical fin must be structurally stronger to support
    the horizontal stabilizer's weight and loads at its tip.
    \item \textbf{Disadvantage:} at very high angles of attack, a T-tail can suffer a
    dangerous ``deep stall'' if the wing wake blankets the tail.
    \end{itemize}"""),
   ("Cruciform Tail: Advantages and Disadvantages",
    r"""\begin{itemize}
    \item \textbf{Advantage:} a middle-ground compromise -- some clearance from fuselage
    wake without the full structural penalty of a T-tail.
    \item \textbf{Advantage:} lower deep-stall risk than a full T-tail.
    \item \textbf{Disadvantage:} still adds more structural complexity than a conventional
    low-mounted tail.
    \end{itemize}"""),
   ("V-Tail (Ruddervator): Advantages and Disadvantages",
    r"""\begin{itemize}
    \item Two slanted surfaces combine pitch and yaw control using \textbf{ruddervators}
    -- each surface moves both symmetrically (pitch) and differentially (yaw).
    \item \textbf{Advantage:} fewer surfaces mean less wetted area and potentially less drag.
    \item \textbf{Disadvantage:} the control mixing (combining pitch and yaw commands into
    two surfaces) is mechanically and electronically more complex.
    \item Used on a small number of light aircraft and some unmanned aircraft; rare on
    transport-category airliners.
    \end{itemize}"""),
   ("Tail Strike: Ground Clearance Concept",
    r"""\begin{itemize}
    \item A \textbf{tail strike} occurs when the rear fuselage or tail-mounted engines
    contact the runway during an overly steep takeoff rotation or landing flare.
    \item Empennage configuration affects risk: tail-mounted engines and low ground
    clearance increase exposure compared to wing-mounted-engine designs.
    \item Airliners are fitted with a \textbf{tail skid} or strike protection on
    tail-strike-prone types, and pilots are trained to limit rotation rate.
    \end{itemize}"""),
   ("Nacelle: Function and Structure",
    r"""A \textbf{nacelle} is the streamlined housing around an engine (most often seen on
    turbofan/turboprop installations).
    \begin{itemize}
    \item Encloses and protects the engine core and accessories.
    \item Shapes airflow into the engine inlet and around the engine for low drag (an
    aerodynamic fairing).
    \item Includes the \textbf{cowling} panels, which open for maintenance access.
    \end{itemize}"""),
   ("Nacelle Components: Inlet, Cowling, Exhaust",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Component & Function\\\hline
    Inlet (intake lip) & Directs smooth, undisturbed airflow into the fan/compressor\\
    Fan cowl & Hinged panels around the fan case; opens for daily inspection\\
    Thrust reverser cowl & Redirects/reverses exhaust for braking after landing\\
    Exhaust nozzle & Accelerates exhaust gas rearward to produce thrust\\\hline
    \end{tabular}\end{center}"""),
   ("Nacelle Anti-Ice",
    r"""\begin{itemize}
    \item The nacelle inlet lip is a leading edge, so it is prone to ice buildup in flight,
    just like the wing leading edge.
    \item Most turbine engines route hot compressor bleed air through the inlet lip to
    prevent ice from forming or to shed it before it can be ingested.
    \item Ice ingested into the engine core can damage fan blades and disrupt airflow,
    so nacelle anti-ice is treated as a safety-critical system.
    \end{itemize}"""),
   ("Thrust Reverser (Brief)",
    r"""\begin{itemize}
    \item A mechanism, housed in the nacelle, that redirects engine exhaust forward instead
    of rearward immediately after touchdown.
    \item Common types: \textbf{cascade-type} (on turbofans, redirects fan air through
    louvered cascades) and \textbf{clamshell-type} (rear doors pivot to block and reverse flow).
    \item Reduces landing roll distance and brake wear, especially on wet or contaminated runways.
    \end{itemize}"""),
   ("Pylon: Function and Structure",
    r"""A \textbf{pylon} is the structural link between the nacelle/engine and the wing
    (or fuselage).
    \begin{itemize}
    \item Transfers engine thrust and weight loads into the main wing or fuselage structure.
    \item Positions the engine at the correct distance and angle from the airframe for
    aerodynamic and safety reasons (e.g.\ fan-blade clearance from the ground).
    \item Often contains fuel, hydraulic, and electrical lines running to the engine.
    \end{itemize}"""),
   ("Pylon Structural Load Path (Preview)",
    r"""\begin{enumerate}
    \item Engine thrust and weight act on the engine mounts, at the front and rear of the engine.
    \item The mounts transfer these loads into the pylon structure.
    \item The pylon carries the combined load inward to a strong fitting on the wing
    (or fuselage) main structure.
    \item From there, the load joins the wing's own load path, described fully in Meeting 6.
    \end{enumerate}"""),
   (r"Engine Mount Types: Rigid vs.\ Isolated",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Mount Type & Description\\\hline
    Rigid mount & Direct metal-to-metal attachment; simple, transmits more vibration\\
    Isolated (vibration-damped) mount & Uses elastomeric or spring elements to absorb vibration\\\hline
    \end{tabular}\end{center}
    Most modern turbofan installations use isolated mounts to reduce vibration transmitted
    into the wing structure and cabin."""),
   ("Engine Mounting Position Comparison",
    r"""\begin{center}\begin{tabular}{l|l|l}\hline
    Mounting & Typical Aircraft & Trade-off\\\hline
    Wing-mounted (pylon, underslung) & Most airliners & Easy access, but ground clearance limits engine size\\
    Fuselage/tail-mounted & Business jets, some regional jets & Quieter cabin, but complex tail structure\\
    Over-wing & A few STOL/regional designs & FOD protection, less common layout\\\hline
    \end{tabular}\end{center}
    In practice, a nacelle installation is described by where the engine sits: in the
    fuselage, at the wing root, in the tail, or underwing/in the wing itself."""),
   ("Turboprop Nacelle: The Orange Peel Cowling",
    r"""\begin{itemize}
    \item Turboprop nacelles commonly use an \textbf{orange peel} type cowling -- multiple
    curved panels that open outward like the peel of an orange for full engine access.
    \item This is distinct from turbofan cowlings, which typically use large hinged fan
    and thrust-reverser cowl doors (Meeting 3's earlier nacelle-components slide).
    \item Nacelle in fuselage and underwing nacelle installations both need this kind of
    quick-opening access for line maintenance between flights.
    \end{itemize}"""),
   ("Doors and Windows",
    r"""\begin{itemize}
    \item \textbf{Doors} are an access for crew/passengers and for maintenance purposes.
    \item \textbf{Windows} are a visual access to and from the aircraft, inside to outside.
    \item Windows can be divided by location: cockpit windows, passenger windows, and
    door-integrated windows.
    \end{itemize}"""),
   ("Case Study: DC-10/MD-11 S-Duct Tail Engine",
    r"""\begin{itemize}
    \item The McDonnell Douglas DC-10 and MD-11 used a third engine mounted in the tail,
    fed by a curved ``S-duct'' inlet through the base of the vertical stabilizer.
    \item This tri-jet layout added redundancy and thrust but made the third engine
    difficult to access for maintenance compared to wing-mounted engines.
    \item As twin-engine reliability improved (Meeting 1), tri-jet designs like this were
    phased out in favor of simpler, cheaper-to-maintain twins.
    \end{itemize}"""),
   ("Case Study: Why Business Jets Favor Tail-Mounted Engines",
    r"""\begin{itemize}
    \item Business jets are smaller and lighter than airliners, so the extra structural
    weight of a reinforced tail is proportionally less costly.
    \item Tail mounting keeps the wing aerodynamically ``clean,'' improving high-speed
    cruise efficiency for a design that prioritizes speed over payload.
    \item Passengers sit ahead of the engines, giving a quieter cabin -- an important
    selling point for executive travel.
    \end{itemize}"""),
   (r"Comparison: Podded vs.\ Buried Engine Installation",
    r"""\begin{center}\begin{tabular}{l|l|l}\hline
    Aspect & Podded (in nacelle) & Buried (in fuselage/wing root)\\\hline
    Access for maintenance & Easy & Difficult\\
    Aerodynamic drag & Some nacelle drag & Can be lower if well integrated\\
    Typical use & Nearly all modern airliners & Some older military/supersonic designs\\\hline
    \end{tabular}\end{center}"""),
   (r"Comparison: Twin-Tail vs.\ Single-Tail Engine Layouts",
    r"""\begin{itemize}
    \item Most aircraft use a single vertical stabilizer (single-tail).
    \item Some fighters and a few transport designs use \textbf{twin vertical stabilizers},
    improving directional stability and providing redundancy if one fin is damaged.
    \item Twin tails add weight and complexity, so they are reserved for designs where the
    stability or redundancy benefit clearly outweighs that cost.
    \end{itemize}"""),
   ("Applied Scenario: Why Underslung Wing Mounting Dominates Airliners",
    r"""Most large airliners mount engines under the wing on pylons rather than on the tail.
    \begin{enumerate}
    \item The wing structure is already strong (it must carry lift loads), so it can
    absorb engine thrust and weight with modest extra reinforcement.
    \item Mounting away from the fuselage keeps cabin noise and vibration lower.
    \item Engine changes and maintenance are far easier at ground level than at the tail.
    \end{enumerate}
    Business jets often accept tail-mounted engines instead, trading some maintenance
    access for a cleaner wing and quieter cabin, which matters more for their smaller size."""),
   ("Applied Scenario: Identifying Empennage Configuration from Silhouette",
    r"""Looking at an aircraft's tail from the side:
    \begin{enumerate}
    \item Horizontal stabilizer mounted low, below the fin tip -- conventional tail.
    \item Horizontal stabilizer mounted at the very top of the fin -- T-tail.
    \item Horizontal stabilizer mounted partway up the fin -- cruciform tail.
    \item Two slanted surfaces, no separate vertical fin visible -- V-tail.
    \end{enumerate}"""),
   ("In-Class Practice",
    r"""\begin{enumerate}
    \item Name the two main surfaces of the empennage and the control surface each carries.
    \item Compare a conventional tail and a T-tail configuration.
    \item Explain the difference in function between a nacelle and a pylon.
    \end{enumerate}"""),
   ("Extended In-Class Practice / Group Discussion",
    r"""In small groups, discuss and be ready to present:
    \begin{enumerate}
    \item Sketch and label a T-tail aircraft, marking the fin spar, stabilizer, elevator, and rudder.
    \item Debate: for a new regional jet, would you choose wing-mounted or tail-mounted
    engines? Justify using noise, maintenance, and structural trade-offs.
    \item Explain why a rudder travel limiter is needed at high airspeed but not at low airspeed.
    \end{enumerate}""")],
  I("The empennage provides pitch and yaw stability through the horizontal and vertical stabilizers.",
    "The nacelle houses and streamlines the engine; the pylon structurally attaches it to the airframe.",
    "Empennage configuration and engine mounting position both involve structural and maintenance trade-offs."),
  I("Label the horizontal stabilizer, elevator, vertical stabilizer, and rudder on a tail diagram.",
    "Compare conventional, T-tail, and V-tail empennage configurations.",
    "Explain the function of a pylon versus a nacelle.",
    "Give one advantage and one disadvantage of tail-mounted engines."))

M[4] = ("Aircraft Axes of Motion \\& Primary Flight Controls",
  "Students are able to explain the aircraft axes of motion and the primary flight control surfaces.",
  I("Explain the three axes of aircraft motion.",
    "Explain the function of the aileron, elevator, and rudder.",
    "Relate cockpit control inputs to control-surface deflection and resulting motion."),
  [("Why Axes and Controls Matter",
    r"""An aircraft must be deliberately maneuvered and kept stable in three dimensions.
    \begin{itemize}
    \item Every maneuver -- a turn, a climb, a landing flare -- is a combination of
    rotation about one or more axes.
    \item Primary flight controls are the surfaces the pilot uses to command that rotation.
    \item This meeting connects the aircraft's physical axes to the ailerons, elevator,
    and rudder introduced anatomically in Meetings 2--3.
    \end{itemize}"""),
   ("The Three Axes of Motion",
    r"""All three axes pass through the aircraft's \textbf{center of gravity (CG)}.
    \begin{center}\begin{tabular}{l|l|l}\hline
    Axis & Direction & Motion\\\hline
    Longitudinal & Nose to tail & Roll\\
    Lateral & Wingtip to wingtip & Pitch\\
    Vertical & Top to bottom & Yaw\\\hline
    \end{tabular}\end{center}"""),
   ("Center of Gravity and the Three Axes",
    r"""\begin{itemize}
    \item The \textbf{center of gravity (CG)} is the point where the aircraft's entire
    weight can be considered to act.
    \item All three rotational axes pass through the CG -- moving the CG changes how the
    aircraft responds to control inputs.
    \item An aft CG makes the aircraft more pitch-sensitive; a forward CG makes it more
    stable but requires more elevator effort, previewing the trim discussion in Meeting 5.
    \end{itemize}"""),
   ("Roll: Longitudinal Axis",
    r"""\begin{itemize}
    \item \textbf{Roll} rotates the aircraft around the longitudinal (nose-to-tail) axis,
    tipping the wings up or down relative to the horizon.
    \item Controlled by the \textbf{ailerons}, hinged surfaces near each wingtip's trailing edge.
    \item Ailerons move in opposite directions: one up, one down, on opposite wings.
    \end{itemize}"""),
   ("Roll Rate and Control Response (Concept)",
    r"""\begin{itemize}
    \item \textbf{Roll rate} is how quickly the aircraft rotates about the longitudinal
    axis for a given aileron deflection.
    \item Longer wingspan and higher aspect ratio (Meeting 2) generally give a slower roll
    rate, since the ailerons act at the end of a longer lever arm against more inertia.
    \item Fighter aircraft are designed for high roll rate; long-span gliders and airliners
    accept a slower, gentler roll response.
    \end{itemize}"""),
   ("Aileron Differential Deflection",
    r"""\begin{itemize}
    \item In many designs the \textbf{up-going} aileron deflects farther than the
    \textbf{down-going} aileron for the same control input.
    \item This is called \textbf{differential deflection}, and it is a simple mechanical
    way to reduce adverse yaw (Meeting 4's later topic).
    \item By deflecting less on the down-going side, less extra drag is created there,
    partially balancing the drag from the up-going side.
    \end{itemize}"""),
   ("Frise Ailerons (Reducing Adverse Yaw)",
    r"""\begin{itemize}
    \item A \textbf{Frise aileron} has a hinge set back from its leading edge, so the
    leading edge of the up-going aileron projects slightly below the wing surface.
    \item That projecting edge deliberately adds drag on the up-going (low-drag) side,
    balancing the drag naturally created by the down-going aileron.
    \item Frise ailerons and differential deflection are two different mechanical answers
    to the same adverse-yaw problem.
    \end{itemize}"""),
   ("Pitch: Lateral Axis",
    r"""\begin{itemize}
    \item \textbf{Pitch} rotates the aircraft around the lateral (wingtip-to-wingtip) axis,
    raising or lowering the nose.
    \item Controlled by the \textbf{elevator}, on the horizontal stabilizer's trailing edge.
    \item Nose-up elevator deflection raises the nose; nose-down deflection lowers it.
    \end{itemize}"""),
   ("Elevator Authority and CG Range",
    r"""\begin{itemize}
    \item \textbf{Elevator authority} is the amount of pitch control available for a given
    elevator deflection.
    \item Every aircraft has a certified forward and aft CG limit; loading outside that
    range can leave too little elevator authority to control pitch safely.
    \item This is why weight-and-balance calculations are mandatory before every flight,
    not just a formality.
    \end{itemize}"""),
   (r"Stabilizer vs.\ Elevator Roles (Recap)",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Surface & Role\\\hline
    Horizontal stabilizer (fixed/trimmable) & Sets baseline pitch trim, resists steady loads\\
    Elevator (hinged, pilot-commanded) & Provides moment-to-moment pitch control\\\hline
    \end{tabular}\end{center}
    Recall from Meeting 3 that on some aircraft a stabilator combines both roles into one
    moving surface."""),
   ("Yaw: Vertical Axis",
    r"""\begin{itemize}
    \item \textbf{Yaw} rotates the aircraft around the vertical (top-to-bottom) axis,
    swinging the nose left or right.
    \item Controlled by the \textbf{rudder}, on the vertical stabilizer's trailing edge.
    \item Rudder deflection to the left swings the nose left, and vice versa.
    \end{itemize}"""),
   ("Rudder Authority and Crosswind Landings",
    r"""\begin{itemize}
    \item In a crosswind landing, the rudder is used to align the aircraft's nose with the
    runway centerline while the ailerons hold the upwind wing down.
    \item Every aircraft type has a certified \textbf{maximum demonstrated crosswind}, set
    largely by how much rudder authority is available.
    \item Beyond that limit, the rudder cannot generate enough yaw force to keep the
    aircraft aligned with the runway during touchdown.
    \end{itemize}"""),
   ("Rudder and Engine-Out Control",
    r"""\begin{itemize}
    \item On a multi-engine aircraft, losing one engine creates \textbf{asymmetric thrust}
    -- the remaining engine(s) push the nose toward the dead engine.
    \item The rudder counters this yaw, keeping the aircraft tracking straight.
    \item Aircraft are certified with a \textbf{minimum control speed} below which the
    rudder cannot fully counter the worst-case engine-out yaw.
    \end{itemize}"""),
   ("Primary Flight Control: Formal Definitions",
    r"""\begin{itemize}
    \item \textbf{Aileron:} controls lateral movement along the longitudinal axis (roll).
    \item \textbf{Elevator:} controls longitudinal movement along the lateral axis (pitch).
    \item \textbf{Rudder:} controls longitudinal movement along the vertical axis (yaw).
    \item All primary flight controls are airfoil-profile surfaces attached to the main
    airfoil surfaces -- the wing or the stabilizer.
    \end{itemize}"""),
   ("Cockpit Control, Surface, Axis, and Rotation",
    r"""\begin{center}\begin{tabular}{l|l|l|l}\hline
    Cockpit Control & Control Surface & Axis & Rotation\\\hline
    Wheel (left/right) & Ailerons & Longitudinal (roll) & Rolling\\
    Column (pull/push) & Elevators & Lateral (pitch) & Pitching\\
    Pedal (pressed right/left) & Rudder & Vertical (yaw) & Yawing\\\hline
    \end{tabular}\end{center}
    A single control wheel or column commands both roll and pitch; the rudder always has
    separate foot pedals."""),
   (r"Cable vs.\ Hydraulic vs.\ Fly-by-Wire Control Systems",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    System & Description\\\hline
    Mechanical (cable/pulley) & Direct cables link cockpit controls to surfaces\\
    Hydro-mechanical & Cables move a hydraulic valve; hydraulics move the surface\\
    Fly-by-wire & Electronic signals from the controls command hydraulic actuators\\\hline
    \end{tabular}\end{center}
    Larger, faster aircraft need hydraulic or fly-by-wire assistance because the
    aerodynamic force on the control surface is too high to move by cable alone."""),
   ("Fly-by-Wire Concept (Brief)",
    r"""\begin{itemize}
    \item In a \textbf{fly-by-wire} system, the pilot's control input is converted to an
    electronic signal, not a direct mechanical link.
    \item A flight control computer interprets the signal, applies safety limits, and
    commands hydraulic actuators to move the surface.
    \item Benefits include lighter controls, automatic protection against exceeding
    structural limits, and easier integration with autopilot systems.
    \end{itemize}"""),
   (r"Comparison: Manual vs.\ Powered Flight Controls",
    r"""\begin{center}\begin{tabular}{l|l|l}\hline
    Aspect & Manual (Cable) & Powered (Hydraulic/FBW)\\\hline
    Typical aircraft & Light GA aircraft & Airliners, business jets\\
    Pilot effort & Direct, can be heavy at speed & Light, often artificially simulated\\
    Weight/complexity & Low & Higher, but enables larger aircraft\\\hline
    \end{tabular}\end{center}"""),
   ("Adverse Yaw (Qualitative)",
    r"""When ailerons roll the aircraft, they can also produce an unwanted yaw in the
    opposite direction, called \textbf{adverse yaw}.
    \begin{itemize}
    \item The down-going aileron creates more drag than the up-going aileron.
    \item That extra drag yaws the nose toward the \emph{outside} of the intended turn.
    \item Pilots counter it with a coordinated rudder input in the direction of the turn.
    \end{itemize}"""),
   (r"Comparison: Differential Aileron vs.\ Frise Aileron",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Method & How It Reduces Adverse Yaw\\\hline
    Differential deflection & Up-going aileron moves farther than down-going aileron\\
    Frise aileron & Set-back hinge exposes leading edge, adding drag on the up-going side\\\hline
    \end{tabular}\end{center}
    Some aircraft combine both methods for maximum adverse-yaw reduction."""),
   ("Case Study: Adverse Yaw in Early Aircraft Design",
    r"""\begin{itemize}
    \item Early aircraft with simple, non-differential ailerons suffered noticeably from
    adverse yaw, making coordinated turns difficult for inexperienced pilots.
    \item Designers responded first with differential aileron linkages, then with the
    Frise aileron profile, before pilot training alone was relied upon.
    \item Today's designs combine mechanical solutions (differential/Frise) with pilot
    rudder coordination -- neither alone fully eliminates adverse yaw.
    \end{itemize}"""),
   ("Coupling Between Axes",
    r"""\begin{itemize}
    \item Rolling into a turn also changes the vertical component of lift, so pitch
    (and elevator input) often must be adjusted at the same time.
    \item Yawing the nose slightly changes airflow over the wings, which can induce a
    small roll -- axes are rarely commanded in complete isolation.
    \item Coordinated flight uses aileron, elevator, and rudder together, not one at a time.
    \end{itemize}"""),
   ("Control Surface Balance (Mass/Aerodynamic Balance)",
    r"""\begin{itemize}
    \item \textbf{Mass balance:} a weight added ahead of a control surface's hinge line to
    shift its center of gravity closer to the hinge.
    \item \textbf{Aerodynamic balance:} shaping part of the surface ahead of the hinge so
    airflow helps move it, reducing pilot effort.
    \item Both techniques also help prevent flutter, the next topic.
    \end{itemize}"""),
   ("Flutter (Concept)",
    r"""\begin{itemize}
    \item \textbf{Flutter} is a dangerous, self-reinforcing vibration that can occur when
    aerodynamic force, structural elasticity, and inertia interact at certain speeds.
    \item An unbalanced or loose control surface is far more prone to flutter than a
    properly mass-balanced one.
    \item Flutter can grow rapidly and cause structural failure, which is why control
    surface balance and stiffness are strictly controlled in design and maintenance.
    \end{itemize}"""),
   ("Primary Control Surface Failure: Redundancy Concept",
    r"""\begin{itemize}
    \item Transport aircraft rarely rely on a single control path for any primary surface.
    \item Multiple hydraulic systems, and often multiple actuators per surface, allow
    continued control if one system fails.
    \item Some aircraft also split a single control surface (e.g.\ two independent aileron
    panels per wing) so that one panel's failure does not remove roll control entirely.
    \end{itemize}"""),
   ("Case Study: Rudder Hardover Incident",
    r"""\begin{itemize}
    \item A \textbf{rudder hardover} is an uncommanded full rudder deflection caused by a
    control-system malfunction.
    \item Past incidents involving this failure mode led to redesigned rudder actuator
    control units and mandatory inspection programs across affected fleets.
    \item This illustrates why even a well-understood, decades-old system like the rudder
    is still subject to ongoing airworthiness directives and design review.
    \end{itemize}"""),
   ("Trim Tab Preview (Tie to Meeting 5)",
    r"""\begin{itemize}
    \item Holding a constant control force to maintain pitch, roll, or yaw in cruise is
    tiring and imprecise over a long flight.
    \item A small \textbf{trim tab} on a primary control surface lets the pilot cancel out
    that steady force without touching the primary control link.
    \item Meeting 5 covers trim tabs, flaps, slats, and spoilers -- the systems that work
    alongside the primary controls introduced today.
    \end{itemize}"""),
   ("Applied Scenario: Rolling Into a Turn",
    r"""A pilot banks the aircraft to the right to begin a turn. Trace the sequence:
    \begin{enumerate}
    \item Control wheel moved right $\Rightarrow$ right aileron up, left aileron down.
    \item Higher lift on the left wing, lower lift on the right wing $\Rightarrow$ aircraft rolls right.
    \item Down-going left aileron's extra drag causes adverse yaw to the left.
    \item Pilot applies light right rudder to coordinate the turn and keep the nose aligned.
    \end{enumerate}"""),
   ("Applied Scenario: Crosswind Landing Technique",
    r"""Landing with a crosswind from the right, the pilot:
    \begin{enumerate}
    \item Applies right aileron to bank slightly into the wind, keeping the aircraft over
    the runway centerline.
    \item Applies left rudder to align the nose (and fuselage) straight down the runway.
    \item Holds this crossed-control input through touchdown, since the crosswind does not stop.
    \end{enumerate}"""),
   ("Applied Scenario: Engine-Out Directional Control",
    r"""The left engine of a twin-engine aircraft fails just after takeoff. Trace the response:
    \begin{enumerate}
    \item Remaining right engine thrust yaws the nose to the left.
    \item Pilot applies right rudder to counter the yaw and keep the aircraft tracking straight.
    \item If speed is below minimum control speed, the rudder cannot fully counter the yaw --
    which is why that speed is a hard certification limit.
    \end{enumerate}"""),
   ("Applied Scenario: Diagnosing Uncommanded Roll",
    r"""An aircraft rolls unexpectedly with no aileron input from the pilot. Work through the checks:
    \begin{enumerate}
    \item Check for asymmetric spoiler deployment (Meeting 5) -- a common non-aileron
    cause of unwanted roll.
    \item Check for a jammed or disconnected aileron linkage on one side.
    \item Check for asymmetric icing or damage changing lift on one wing.
    \end{enumerate}"""),
   ("In-Class Practice",
    r"""\begin{enumerate}
    \item Match each axis (longitudinal, lateral, vertical) to its motion (roll, pitch, yaw)
    and controlling surface.
    \item Explain what cockpit input produces a nose-down pitch change.
    \item Explain why adverse yaw occurs and how a pilot corrects for it.
    \end{enumerate}"""),
   ("Extended In-Class Practice / Group Discussion",
    r"""In small groups, discuss and be ready to present:
    \begin{enumerate}
    \item Explain the difference between differential ailerons and Frise ailerons using a diagram.
    \item Debate: why do airliners use fly-by-wire or hydraulic controls instead of simple cables?
    \item Walk through the full control sequence, axis by axis, for a coordinated climbing left turn.
    \end{enumerate}""")],
  I("The three axes of motion -- longitudinal, lateral, vertical -- correspond to roll, pitch, and yaw.",
    "Ailerons control roll, the elevator controls pitch, and the rudder controls yaw.",
    "Adverse yaw links roll and yaw, requiring coordinated aileron and rudder input."),
  I("Draw the three axes of motion through an aircraft's center of gravity and label each motion.",
    "Explain the control-surface and cockpit-input path for a roll to the left.",
    "Explain what adverse yaw is and how a pilot corrects for it.",
    "Describe what happens to the ailerons, elevator, and rudder during a coordinated right turn."))

M[5] = ("Secondary Flight Controls \\& High-Lift Devices",
  "Students are able to explain secondary flight control systems and high-lift devices.",
  I("Explain the function of trim tabs.",
    "Explain the function and types of flaps and slats.",
    "Explain the function of spoilers/speedbrakes."),
  [("Why Secondary Controls and High-Lift Devices Matter",
    r"""Primary flight controls (Meeting 4) maneuver the aircraft; secondary controls and
    high-lift devices make flight \textbf{easier and safer at the extremes} -- steady
    cruise and slow-speed takeoff/landing.
    \begin{itemize}
    \item Trim relieves constant pilot control pressure in cruise.
    \item Flaps and slats let an aircraft take off and land at much lower speeds.
    \item Spoilers manage lift and drag on demand, including on the ground.
    \end{itemize}"""),
   ("Trim Tabs",
    r"""\begin{itemize}
    \item A \textbf{trim tab} is a small hinged surface on a primary control surface's
    trailing edge (elevator, aileron, or rudder).
    \item It is adjusted to hold a desired control position \emph{without} the pilot
    continuously applying force.
    \item Elevator trim is the most commonly used, keeping pitch attitude steady in cruise.
    \end{itemize}"""),
   (r"Trim Tab Types: Fixed vs.\ Adjustable",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Type & Description\\\hline
    Fixed (ground-adjustable) & Bent on the ground by maintenance; not moved in flight\\
    Pilot-controllable & Adjusted from the cockpit during flight, most common on transports\\
    Anti-servo tab & Moves with a stabilator to add control feel (Meeting 3)\\\hline
    \end{tabular}\end{center}"""),
   ("Aileron Trim and Rudder Trim",
    r"""\begin{itemize}
    \item Elevator trim is the most common, but many aircraft also have \textbf{aileron
    trim} and \textbf{rudder trim}.
    \item Aileron trim corrects a persistent wing-heavy tendency, often from fuel imbalance
    or asymmetric loading.
    \item Rudder trim corrects a persistent yaw tendency, useful for sustained asymmetric
    thrust conditions such as one engine at reduced power.
    \end{itemize}"""),
   ("Autopilot and Trim (Brief)",
    r"""\begin{itemize}
    \item An engaged autopilot commands the primary control surfaces directly, but it also
    drives the trim system to keep the aircraft trimmed for the current flight condition.
    \item This means that if the autopilot disconnects unexpectedly, the aircraft is left
    trimmed for its last condition, not necessarily hands-off neutral.
    \item A \textbf{trim runaway} (trim moving uncommanded) is treated as a serious
    malfunction requiring an immediate, memorized pilot response.
    \end{itemize}"""),
   ("Flaps: Function and Effect",
    r"""\begin{itemize}
    \item \textbf{Flaps} are hinged panels on the wing's trailing edge, near the root.
    \item Extending flaps increases wing camber and (for some types) wing area, increasing
    lift \emph{and} drag at a given speed.
    \item This allows safe flight, takeoff, and landing at lower airspeeds than a clean
    (flaps-up) wing would allow.
    \end{itemize}"""),
   ("Flap Extension Speed Limits (Concept)",
    r"""\begin{itemize}
    \item Every flap setting has a maximum speed at which it may be safely extended,
    called \textbf{VFE} (velocity, flaps extended).
    \item Exceeding VFE with flaps out risks structural overload of the flap and its
    extension mechanism, since aerodynamic load rises sharply with speed.
    \item Cockpit airspeed indicators mark this limit so pilots retract flaps before
    accelerating past it.
    \end{itemize}"""),
   ("Flap Types",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Type & Description\\\hline
    Plain & Simple hinged panel, rotates down from the wing trailing edge\\
    Split & Only the lower surface hinges down; higher drag, less lift than slotted types\\
    Slotted & A gap directs high-energy air over the flap, adding lift efficiently\\
    Fowler & Slides aft and down, increasing both wing area and camber\\\hline
    \end{tabular}\end{center}
    Fowler flaps are the most effective and common on modern airliners."""),
   ("Fowler Flap Track Mechanism (Brief)",
    r"""\begin{itemize}
    \item Fowler flaps ride on curved \textbf{tracks} mounted beneath the wing, driven by
    a screwjack or hydraulic actuator.
    \item As the flap extends, it slides aft along the track before rotating downward --
    the combined motion increases wing area before adding camber.
    \item The exposed track fairings visible under an airliner's wing during approach are
    the external housing for this mechanism.
    \end{itemize}"""),
   ("Flap Asymmetry Protection",
    r"""\begin{itemize}
    \item Flaps normally extend evenly on both wings, driven by a common shaft or synchronized system.
    \item A \textbf{flap asymmetry} (one side extended more than the other) creates
    uncommanded roll, since lift differs between the wings.
    \item Modern aircraft include sensors that detect asymmetry and automatically stop
    flap movement, alerting the crew before the condition becomes hazardous.
    \end{itemize}"""),
   ("Slats and Leading-Edge Devices",
    r"""\begin{itemize}
    \item \textbf{Slats} are movable panels on the wing's leading edge.
    \item Extending a slat opens a slot that channels air smoothly over the wing's upper
    surface at high angles of attack.
    \item This delays airflow separation (stall), allowing an even lower safe speed when
    combined with trailing-edge flaps.
    \end{itemize}"""),
   (r"Slat Types: Leading-Edge Slats vs.\ Fixed Slots",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Type & Description\\\hline
    Movable slat & Extends/retracts with the flap system; used on most transports\\
    Fixed slot & Permanently open slot; simple, common on light training aircraft\\\hline
    \end{tabular}\end{center}
    A fixed slot gives some of a slat's stall-delay benefit with no moving parts, at the
    cost of extra drag in cruise -- an acceptable trade for a slow-flying trainer."""),
   ("Krueger Flaps",
    r"""\begin{itemize}
    \item A \textbf{Krueger flap} is a leading-edge device that folds out and down from
    the wing's lower surface, rather than sliding aft like a slat.
    \item It effectively droops and extends the leading edge, increasing camber near the
    wing root to delay stall there.
    \item Often used near the wing root (inboard), sometimes paired with true slats further
    outboard on the same wing.
    \end{itemize}"""),
   (r"Comparison: Slats vs.\ Krueger Flaps",
    r"""\begin{center}\begin{tabular}{l|l|l}\hline
    Aspect & Slat & Krueger Flap\\\hline
    Motion & Slides forward/down, opens a slot & Folds down from lower wing surface\\
    Typical location & Outboard, along most of the span & Often inboard, near the wing root\\
    Mechanism complexity & Higher & Generally simpler\\\hline
    \end{tabular}\end{center}"""),
   ("Spoilers and Speedbrakes",
    r"""\begin{itemize}
    \item \textbf{Spoilers} are panels on the wing's upper surface that deploy upward to
    disrupt (spoil) airflow.
    \item \textbf{In flight:} used symmetrically as speedbrakes to increase drag and descend
    faster, or asymmetrically (one wing only) to assist roll control.
    \item \textbf{On landing:} deployed fully ("lift dumpers") to destroy lift, press the
    wheels onto the runway, and shorten the landing roll.
    \end{itemize}"""),
   ("Spoiler Panel Layout: Inboard and Outboard",
    r"""\begin{itemize}
    \item Spoiler panels are arranged in a row along the wing's upper surface, split into
    \textbf{inboard} and \textbf{outboard} groups.
    \item Outboard panels are typically used for roll assistance in flight, closer to the
    aileron and away from engine wake.
    \item Inboard panels are typically reserved for ground and speedbrake use, closer to
    the fuselage where roll authority matters less.
    \end{itemize}"""),
   (r"Ground Spoilers vs.\ Flight Spoilers",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Type & Use\\\hline
    Flight spoilers & Deploy partially in flight, for descent or roll assist\\
    Ground spoilers & Deploy fully, only after touchdown (or rejected takeoff)\\\hline
    \end{tabular}\end{center}
    Ground spoilers are typically interlocked so they cannot deploy fully while airborne,
    preventing an accidental loss of lift."""),
   ("Speedbrake Handle and Cockpit Operation (Brief)",
    r"""\begin{itemize}
    \item Pilots command spoilers through a dedicated \textbf{speedbrake lever} in the cockpit,
    separate from the flap lever.
    \item Positions typically include: stowed, armed (for automatic ground deployment on
    landing), and manually extended positions for in-flight use.
    \item Arming the spoilers before landing lets them deploy automatically at touchdown
    without a separate pilot action during a busy phase of flight.
    \end{itemize}"""),
   (r"Comparison: Flaps vs.\ Slats vs.\ Spoilers",
    r"""\begin{center}\begin{tabular}{l|l|l|l}\hline
    Device & Location & Primary Effect & When Used\\\hline
    Flaps & Trailing edge, wing root & Increase lift and drag & Takeoff, approach, landing\\
    Slats & Leading edge & Delay stall (higher AoA) & Takeoff, approach, landing\\
    Spoilers & Upper wing surface & Reduce lift, increase drag & Descent, roll assist, landing roll\\\hline
    \end{tabular}\end{center}"""),
   ("High-Lift System Interconnection",
    r"""\begin{itemize}
    \item On most transport aircraft, flaps and slats are extended together using a single
    cockpit lever with detented positions.
    \item An internal mechanical or electronic interconnect ensures the slat schedule
    matches the selected flap setting -- the crew cannot extend one without the other.
    \item This interconnection exists because flap-only or slat-only combinations were
    found in testing to give unpredictable stall behavior.
    \end{itemize}"""),
   ("Stall Speed and High-Lift Devices (Concept)",
    r"""\begin{itemize}
    \item A wing stalls when it exceeds its critical angle of attack, regardless of airspeed.
    \item Flaps and slats do not prevent a stall -- they change the speed and angle at which
    it occurs, by increasing the maximum lift the wing can produce.
    \item This is why every stall-speed figure published for an aircraft is always quoted
    for a specific flap/slat configuration, not as a single fixed number.
    \end{itemize}"""),
   ("Other Secondary Devices (Brief)",
    r"""\begin{itemize}
    \item \textbf{Servo tabs:} small tabs that aerodynamically help move a large primary
    control surface, reducing the pilot's control force.
    \item \textbf{Balance tabs:} move opposite to the main surface to reduce the force
    needed to hold a deflection.
    \item These are refinements of the trim-tab concept applied to control \emph{feel}
    rather than trim.
    \end{itemize}"""),
   ("Case Study: Asymmetric Flap Incident",
    r"""\begin{itemize}
    \item Several historical accidents and incidents have involved a flap that failed to
    extend evenly, producing an uncommanded roll during approach.
    \item Investigations of these events directly drove the flap-asymmetry sensors and
    automatic-stop systems now standard on modern airliners.
    \item The lesson generalizes: any system creating asymmetric lift across the wingspan
    needs a dedicated monitoring and protection system.
    \end{itemize}"""),
   ("Case Study: Spoiler Deployment on Landing Rollout",
    r"""\begin{itemize}
    \item If ground spoilers fail to deploy after touchdown, the wings still generate
    significant lift, reducing weight on the wheels and cutting braking effectiveness.
    \item This has contributed to runway overrun incidents on wet or contaminated runways
    in aviation history.
    \item As a result, spoiler deployment is cross-checked by the crew as a standard item
    during the landing rollout, not assumed automatic.
    \end{itemize}"""),
   (r"Comparison: Powered vs.\ Manual Trim Systems",
    r"""\begin{center}\begin{tabular}{l|l|l}\hline
    Aspect & Manual Trim Wheel & Powered (Electric) Trim\\\hline
    Typical aircraft & Light GA aircraft & Airliners, business jets\\
    Pilot input & Physically rotates a wheel & Switch commands an electric motor\\
    Failure mode & Rare, purely mechanical & Requires runaway-trim protection logic\\\hline
    \end{tabular}\end{center}"""),
   ("Applied Scenario: Configuring for Approach and Landing",
    r"""As an airliner descends for landing, its configuration changes in stages:
    \begin{enumerate}
    \item Spoilers/speedbrakes extend briefly to help the initial descent.
    \item Flaps extend in stages, increasing lift and drag as speed decreases.
    \item Slats extend together with flaps to protect against stall at low speed.
    \item After touchdown, spoilers deploy fully as lift dumpers to shorten the landing roll.
    \end{enumerate}"""),
   ("Takeoff Configuration: Flap/Slat Setting",
    r"""\begin{enumerate}
    \item Flaps and slats are set to an intermediate takeoff position -- enough extra lift
    to shorten the takeoff roll, without the high drag of a full landing setting.
    \item Spoilers remain stowed (except armed for a possible rejected takeoff).
    \item Trim is set according to the calculated takeoff weight and CG, so the aircraft
    rotates predictably at the correct speed.
    \end{enumerate}"""),
   ("Applied Scenario: Rejected Takeoff and Spoiler/Brake Use",
    r"""During takeoff roll, the crew rejects the takeoff below decision speed. Trace the sequence:
    \begin{enumerate}
    \item Thrust levers are brought to idle (or reverse, if fitted) immediately.
    \item Armed ground spoilers deploy automatically on the wheels touching down/weight-on-wheels,
    destroying lift and pressing the aircraft onto its brakes.
    \item Wheel brakes, now fully loaded by spoiler-dumped lift, provide maximum stopping force.
    \end{enumerate}
    This is why ground spoilers are armed before every takeoff, not just before landing."""),
   ("Applied Scenario: Diagnosing a Flap Asymmetry Warning",
    r"""A flap asymmetry warning illuminates during approach. Work through the response:
    \begin{enumerate}
    \item Flap movement automatically stops at the current position (Meeting 5's asymmetry
    protection system).
    \item The crew checks aircraft handling for any roll tendency and compensates with
    aileron/trim as needed.
    \item Approach speed is increased to compensate for the reduced (and possibly uneven)
    lift from the stuck flap configuration.
    \end{enumerate}"""),
   ("Common Misconceptions About High-Lift Devices",
    r"""\begin{itemize}
    \item \textbf{Myth:} flaps and slats always move together as one device.
    \textbf{Fact:} they are separate systems, mechanically interconnected for scheduling.
    \item \textbf{Myth:} more flap is always better for landing. \textbf{Fact:} full flap
    adds drag that can be undesirable in a strong crosswind or engine-out landing.
    \item \textbf{Myth:} spoilers and speedbrakes are different devices. \textbf{Fact:} on
    most aircraft they are the same panels, just used differently.
    \end{itemize}"""),
   ("In-Class Practice",
    r"""\begin{enumerate}
    \item Explain why extending flaps allows an aircraft to approach at a lower airspeed.
    \item Compare the function of slats and flaps.
    \item Explain the two different uses of spoilers: in flight and on the ground.
    \end{enumerate}"""),
   ("Extended In-Class Practice / Group Discussion",
    r"""In small groups, discuss and be ready to present:
    \begin{enumerate}
    \item Compare a Krueger flap and a slat on a labeled wing-root-to-tip diagram.
    \item Debate: why are ground spoilers deliberately prevented from deploying in flight?
    \item Walk through the full high-lift configuration change from cruise to full landing flap.
    \end{enumerate}""")],
  I("Trim tabs relieve pilot control pressure without acting as a primary control.",
    "Flaps and slats increase lift (and delay stall) for slow-speed flight, takeoff, and landing.",
    "Spoilers reduce lift and add drag, used in flight and as lift dumpers on landing."),
  I("Explain the function of a trim tab and name the surface it is most commonly fitted to.",
    "Compare plain, split, slotted, and Fowler flaps.",
    "Explain how slats delay wing stall.",
    "Describe the two operational uses of spoilers on an airliner."))

M[6] = ("Airframe Structure \\& Load Path",
  "Students are able to explain airframe structural elements and load path.",
  I("Identify primary structural elements of the wing and fuselage.",
    "Explain the concept of load path.",
    "Explain the basic types of structural loads."),
  [("Why Structural Understanding Matters",
    r"""An airframe must carry flight loads safely for tens of thousands of flight hours.
    \begin{itemize}
    \item Every external surface studied so far (Meetings 2--3) is supported by an internal
    structural skeleton.
    \item Understanding how loads travel through that skeleton is the foundation for later
    material (Meeting 10--11) and maintenance topics.
    \item This meeting names the key structural members and traces how loads move through them.
    \end{itemize}"""),
   ("Structure and Structural Integrity",
    r"""\begin{itemize}
    \item \textbf{Structure} is an arrangement and organization of interrelated elements
    in a material object or system, or the object or system so organized; a structure is
    supposed to withstand any force acting upon it.
    \item \textbf{Structural integrity} is the ability of the structure to retain its
    strength, function, and shape within acceptable limits, without failure, when
    subjected to the loads imposed throughout the structure's service life.
    \item \textbf{Stress} is force acting upon a structure, whether static or dynamic --
    the aircraft structure suffers stress performing maneuvers both in flight and on
    the ground.
    \end{itemize}"""),
   ("The Six Types of Structural Stress",
    r"""\begin{center}\begin{tabular}{l|l|l}\hline
    Stress Type & Definition & Example\\\hline
    Tensile & A force that pulls apart or stretches a material & Control cable\\
    Compressive & Stress on a material that leads to a smaller volume & Shock strut\\
    Torsional & Stress produced in a shaft due to twisting & Twisted bolt\\
    Shear & Force causing deformation by slippage along a plane & Rivet on aircraft skin\\
    Bending & Normal stress induced when a body is loaded to bend & Aircraft wing\\
    Combined & Any stress state not representable by a single component & Aircraft wing\\\hline
    \end{tabular}\end{center}"""),
   ("Stress in Detail: Tensile, Compressive, and Torsional",
    r"""\begin{itemize}
    \item \textbf{Tensile stress} refers to a force that attempts to pull apart or
    stretch a material -- example: a control cable under load.
    \item \textbf{Compressive stress} is the stress on a material that leads to a smaller
    volume -- example: a shock strut compressing on touchdown.
    \item \textbf{Torsional stress} is stress produced in a shaft due to twisting --
    example: a twisted bolt.
    \end{itemize}"""),
   ("Stress in Detail: Shear, Bending, and Combined",
    r"""\begin{itemize}
    \item \textbf{Shear stress} is a force tending to cause deformation of a material by
    slippage along a plane or planes parallel to the imposed stress -- example: a rivet
    on the aircraft skin.
    \item \textbf{Bending stress} is the normal stress induced at a point in a body
    subjected to loads that cause it to bend -- example: an aircraft wing in flight.
    \item \textbf{Combined stress} is any state of stress that cannot be represented by a
    single component of stress -- also exemplified by the aircraft wing, which
    experiences bending, shear, and torsion together.
    \end{itemize}"""),
   ("Primary Structural Elements",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Element & Location \& Function\\\hline
    Spar & Main span-wise wing beam; carries most of the wing's bending load\\
    Rib & Wing cross-section former; maintains airfoil shape, supports skin\\
    Stringer & Long, thin fuselage/wing skin stiffener, runs span-wise or fore-aft\\
    Longeron & Heavier, more widely spaced fuselage stiffener than a stringer\\
    Frame & Fuselage cross-section former, like a rib but for the fuselage\\\hline
    \end{tabular}\end{center}"""),
   (r"Stringer vs.\ Longeron Comparison",
    r"""\begin{center}\begin{tabular}{l|l|l}\hline
    Aspect & Stringer & Longeron\\\hline
    Size & Small, closely spaced & Larger, widely spaced\\
    Load carried each & Small share of bending load & Larger share of bending load\\
    Typical count per fuselage & Many (dozens) & Few (a handful, at key points)\\\hline
    \end{tabular}\end{center}
    Both run fore-aft and work together with the frames and skin to carry fuselage
    bending loads."""),
   ("Rivets and Fasteners Overview (Brief)",
    r"""\begin{itemize}
    \item \textbf{Rivets} are the most common fastener joining skin to stringers, frames, and ribs.
    \item A rivet is installed through matching holes and deformed to clamp the parts together --
    it cannot be reused once removed.
    \item \textbf{Bolts} are used at higher-load joints (e.g.\ wing-to-fuselage attachment)
    where the joint may need to be opened for inspection or replacement.
    \end{itemize}"""),
   (r"Bonded vs.\ Riveted Construction",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Method & Characteristics\\\hline
    Riveted & Mechanical fasteners; proven, easily inspected, adds small stress points\\
    Adhesive-bonded & Structural adhesive joins panels; smoother surface, no rivet holes\\\hline
    \end{tabular}\end{center}
    Composite structures (Meeting 11) rely heavily on bonding, since composite material
    does not always tolerate rivet holes as well as metal."""),
   ("Wing Structural Cross-Section",
    r"""\begin{itemize}
    \item The \textbf{spar} (often one main spar plus a rear spar) is the wing's primary
    load-carrying member, running along the span.
    \item \textbf{Ribs} are spaced along the span, giving the wing its airfoil cross-section
    and transferring skin loads to the spar.
    \item The \textbf{skin} covers ribs and spars, carrying some load and sealing fuel
    tanks in many wing designs.
    \end{itemize}"""),
   (r"Wing Spar Types: Single-Spar vs.\ Multi-Spar / Box Beam",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Type & Description\\\hline
    Single-spar & One main spar carries nearly all bending load; simple, lighter\\
    Two-spar (front/rear) & Front and rear spars share load, form a stiff torsion box with skin\\
    Multi-spar/box beam & Several spars plus skin form a very stiff box; high-speed/high-load wings\\\hline
    \end{tabular}\end{center}
    Most modern transport wings use a two-spar torsion-box design, combining strength
    with usable internal volume for fuel."""),
   ("Keel Beam (Wing Center Section Structure)",
    r"""\begin{itemize}
    \item The \textbf{keel beam} is a heavy structural beam running along the bottom
    centerline of the fuselage, through the wing center section.
    \item It helps carry the wing's bending loads across the fuselage and supports the
    cargo floor structure in that area.
    \item Along with the wing box discussed in Meeting 2, the keel beam is one of the most
    critical and closely inspected structural members on the aircraft.
    \end{itemize}"""),
   ("Fuselage Structural Cross-Section",
    r"""In a semi-monocoque fuselage (Meeting 2):
    \begin{itemize}
    \item \textbf{Frames} run around the fuselage circumference, maintaining its shape.
    \item \textbf{Longerons/stringers} run fore-aft, carrying bending loads along the
    fuselage's length.
    \item The \textbf{skin} carries shear and some bending/torsion loads together with the
    frames and stringers.
    \end{itemize}"""),
   ("Skin Panel Function and Types",
    r"""\begin{itemize}
    \item The \textbf{skin} is the outer covering of the airframe, attached to the
    underlying ribs, spars, frames, and stringers.
    \item In semi-monocoque construction, skin is a working structural member, not just
    an aerodynamic cover -- it carries shear and some bending load.
    \item Skin thickness varies across the airframe: thicker where loads are highest
    (wing root, lower fuselage), thinner where loads are lower.
    \end{itemize}"""),
   ("Fuselage Frame Spacing and Pressurization Cycles",
    r"""\begin{itemize}
    \item Frame spacing is chosen to support the skin against buckling and to resist the
    outward pressure load from cabin pressurization.
    \item Every pressurize/depressurize cycle (one per flight) very slightly stretches and
    relaxes the fuselage skin -- a repeated load that drives fatigue life (this meeting's
    later topic).
    \item Aircraft have a certified number of pressurization cycles as part of their
    structural life limit, tracked throughout their service.
    \end{itemize}"""),
   ("Pressure Bulkheads",
    r"""\begin{itemize}
    \item A \textbf{pressure bulkhead} is a dome-shaped or flat structural wall that seals
    the ends of the pressurized cabin.
    \item The \textbf{forward pressure bulkhead} typically sits just behind the radome/nose
    section; the \textbf{aft pressure bulkhead} seals the cabin ahead of the unpressurized tail cone.
    \item These bulkheads carry very high loads, since they resist the full cabin pressure
    difference across their entire area.
    \end{itemize}"""),
   ("The Load Path Concept",
    r"""A \textbf{load path} is the route a force takes as it travels through connected
    structural members to a point where it is finally reacted (balanced).
    \begin{enumerate}
    \item Aerodynamic lift acts on the wing's skin.
    \item Skin transfers that load to the nearest ribs.
    \item Ribs transfer the load into the spar.
    \item The spar carries the load inward to the wing-to-fuselage attachment fitting.
    \item The fuselage frames and longerons distribute the load through the airframe.
    \end{enumerate}"""),
   ("Load Path for Landing Gear Loads (Preview)",
    r"""\begin{enumerate}
    \item On touchdown, impact load acts upward through the wheels and shock strut.
    \item The strut transfers load into a dedicated, heavily reinforced gear attachment
    structure (often built into the wing spar or a fuselage frame).
    \item That reinforced structure spreads the load into the surrounding airframe, the
    same way the wing spar spreads lift into the fuselage.
    \end{enumerate}
    Landing gear structure and retraction are covered fully in Meeting 12."""),
   ("Load Path for Engine Thrust (Preview)",
    r"""\begin{enumerate}
    \item Engine thrust acts on the engine mounts (Meeting 3).
    \item The pylon carries that thrust load to a reinforced wing (or fuselage) attachment fitting.
    \item From there, thrust joins the wing or fuselage's general load path, reacted
    ultimately against the whole aircraft's inertia as it accelerates.
    \end{enumerate}"""),
   ("Types of Structural Loads",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Load Type & Description\\\hline
    Tension & Pulling a member apart along its length\\
    Compression & Pushing/squeezing a member along its length\\
    Shear & Sliding force between adjacent layers or members\\
    Bending & Combination of tension (one side) and compression (other side)\\
    Torsion & Twisting force about a member's long axis\\\hline
    \end{tabular}\end{center}
    Real flight loads are almost always a combination of several of these at once."""),
   ("Fatigue as Repeated Loading",
    r"""\begin{itemize}
    \item \textbf{Fatigue} is structural damage that accumulates from repeated loading and
    unloading, even when each individual load is well within the material's static strength.
    \item Every takeoff, landing, pressurization cycle, and gust adds a small amount of
    fatigue damage.
    \item Fatigue cracks typically begin at stress concentrations (the next slide) and grow
    slowly, cycle by cycle, until they are caught by inspection or, if missed, cause failure.
    \end{itemize}"""),
   (r"Static vs.\ Fatigue Loading Comparison",
    r"""\begin{center}\begin{tabular}{l|l|l}\hline
    Aspect & Static Load & Fatigue Load\\\hline
    Nature & One-time or rare large load & Small load repeated many times\\
    Failure mode & Immediate overload failure & Slow crack growth to eventual failure\\
    Design defense & Strength margin & Fail-safe/damage-tolerant design, inspection\\\hline
    \end{tabular}\end{center}"""),
   ("Stress Concentration",
    r"""\begin{itemize}
    \item Loads do not distribute evenly -- holes, cutouts, and sharp corners create
    \textbf{stress concentrations}, local areas of higher stress.
    \item Rivet holes, doors, and windows are common stress-concentration points and are
    reinforced accordingly.
    \item Fatigue cracks most often start at stress concentrations, which is why they are
    inspection focal points.
    \end{itemize}"""),
   ("Corrosion as a Structural Threat (Brief)",
    r"""\begin{itemize}
    \item \textbf{Corrosion} is chemical/electrochemical degradation of the structure,
    most often affecting aluminum airframes in humid or salt-air environments.
    \item Corrosion thins the material, reducing its strength and creating new stress
    concentrations -- it can combine with fatigue to accelerate failure.
    \item Protective coatings, sealants, and drainage design all exist specifically to
    keep moisture away from bare structure.
    \end{itemize}"""),
   ("Structural Inspection Methods (Overview)",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Method & Use\\\hline
    Visual inspection & Fast, routine check for obvious damage/corrosion\\
    Non-destructive testing (NDT) & Detects cracks not visible to the eye (e.g.\ eddy current, ultrasonic)\\
    X-ray/radiographic inspection & Reveals internal structure without disassembly\\\hline
    \end{tabular}\end{center}
    Inspection intervals are set to catch a growing crack well before it could reach a
    critical size, tying directly back to damage-tolerant design."""),
   ("Fail-Safe and Damage-Tolerant Design (Concept)",
    r"""\begin{itemize}
    \item \textbf{Fail-safe design:} the structure has multiple load paths, so if one member
    fails, others can still carry the load until the damage is found and repaired.
    \item \textbf{Damage-tolerant design:} the structure is designed and inspected so that
    a crack can be detected before it grows large enough to cause failure.
    \item Both philosophies rely on regularly scheduled structural inspections.
    \end{itemize}"""),
   ("Case Study: Aloha Airlines Flight 243",
    r"""\begin{itemize}
    \item In 1988, a Boeing 737's upper fuselage skin separated in flight due to
    undetected fatigue and corrosion damage accumulated over many pressurization cycles.
    \item The aircraft landed safely, but the event exposed gaps in inspection programs
    for aging, high-cycle aircraft.
    \item This incident led directly to industry-wide \textbf{aging-aircraft inspection
    programs} that still shape maintenance schedules today.
    \end{itemize}"""),
   ("Case Study: Fail-Safe Design Saving an Aircraft",
    r"""\begin{itemize}
    \item Fail-safe structures have, in multiple documented events, allowed aircraft to
    land safely after a single structural member failed in flight.
    \item In each case, neighboring structure (an adjacent stringer, frame, or spar cap)
    picked up the failed member's load until the aircraft could land and be repaired.
    \item These events are the real-world proof of the fail-safe design philosophy
    introduced earlier in this meeting.
    \end{itemize}"""),
   (r"Comparison: Fail-Safe vs.\ Safe-Life Design Philosophy",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Philosophy & Approach\\\hline
    Fail-safe & Multiple load paths; structure tolerates a single failure\\
    Safe-life & Component is retired before fatigue cracking can begin, based on test data\\\hline
    \end{tabular}\end{center}
    Modern airframes typically combine both: safe-life limits for some critical parts,
    fail-safe/damage-tolerant design for the surrounding structure."""),
   ("Structural Repair Concept (Doubler Plate)",
    r"""\begin{itemize}
    \item A \textbf{doubler plate} is a reinforcing panel riveted or bonded over a repaired
    area (e.g.\ around a stop-drilled crack or a corroded region).
    \item It restores the local strength lost to damage or material removal during repair.
    \item Every repair is documented and engineered to restore, not just patch, the
    original load-carrying capability of that structure.
    \end{itemize}"""),
   ("Applied Scenario: Tracing Wing Lift to the Fuselage",
    r"""During cruise, the wing generates upward lift distributed along its span.
    \begin{enumerate}
    \item Lift pressure acts on the wing's upper and lower skin panels.
    \item Skin passes the load to the nearest ribs.
    \item Ribs funnel the load into the main spar, which bends slightly under the load.
    \item The spar root attaches to a strong fitting on the fuselage centerline, where the
    load is finally reacted against the weight and inertia of the rest of the aircraft.
    \end{enumerate}"""),
   ("Applied Scenario: Tracing Landing Gear Load to the Airframe",
    r"""On a firm touchdown, trace the load:
    \begin{enumerate}
    \item Impact load enters the wheel and travels up the shock strut.
    \item The strut transfers load into its reinforced attachment fitting on the wing or fuselage.
    \item That fitting spreads the load into the surrounding spar, frames, and skin,
    exactly as the wing-lift load path does in reverse.
    \end{enumerate}"""),
   ("Applied Scenario: Identifying a Stress Concentration on an Inspection Photo",
    r"""Given a photo of a fuselage skin panel, identify likely stress-concentration points:
    \begin{enumerate}
    \item Any rivet hole, especially where several holes are closely spaced.
    \item Any cutout for a window, door, or access panel, particularly at its corners.
    \item Any visible scratch, dent, or corrosion pit that locally thins the skin.
    \end{enumerate}"""),
   ("Common Misconceptions About Structural Load",
    r"""\begin{itemize}
    \item \textbf{Myth:} the skin is just a cosmetic cover. \textbf{Fact:} in semi-monocoque
    construction, skin is a genuine load-carrying structural member.
    \item \textbf{Myth:} a stronger material always means a better structure. \textbf{Fact:}
    weight, fatigue behavior, and cost all matter alongside raw strength.
    \item \textbf{Myth:} fail-safe design means the structure can never fail.
    \textbf{Fact:} it means a single failure does not cause total loss of the structure.
    \end{itemize}"""),
   ("In-Class Practice",
    r"""\begin{enumerate}
    \item Define spar, rib, stringer, and longeron in one sentence each.
    \item Trace the load path of lift from the wing skin to the fuselage.
    \item Name the five basic types of structural load, with one real example each.
    \end{enumerate}"""),
   ("Extended In-Class Practice / Group Discussion",
    r"""In small groups, discuss and be ready to present:
    \begin{enumerate}
    \item Explain, using the Aloha Airlines case study, how fatigue and corrosion combine
    to threaten an aging airframe.
    \item Debate: is fail-safe or safe-life design more appropriate for a wing spar, and why?
    \item Sketch the full load path for engine thrust, from engine mount to fuselage.
    \end{enumerate}""")],
  I("Spars, ribs, stringers, longerons, and frames are the primary structural members of the wing and fuselage.",
    "A load path traces how a force travels through connected structure to where it is reacted.",
    "Tension, compression, shear, bending, and torsion are the five basic load types."),
  I("Label a wing cross-section with spar, rib, and skin.",
    "Describe the load path from wing lift to the fuselage centerline.",
    "Explain the difference between fail-safe and damage-tolerant design.",
    "Give a real airframe example of a member under tension and one under compression."))

M[7] = ("Review \\& Practice: Aircraft Anatomy \\& Flight Control Systems",
  "Students are able to integrate concepts of aircraft anatomy and control systems (Meetings 1--6) to describe a complete aircraft configuration.",
  I("Combine classification, anatomy, controls, and structure in one problem.",
    "Solve mixed exercises accurately.",
    "Prepare comprehensively for the midterm evaluation."),
  [("Why an Integration Meeting?",
    r"""Describing a real aircraft never uses just one topic in isolation -- a single
    walkaround inspection touches classification, anatomy, structure, and controls together.
    \begin{itemize}
    \item This meeting stitches Meetings 1--6 together with mixed review and practice.
    \item Goal: recognize which topic area a question is really asking about, then answer
    it with the correct vocabulary.
    \end{itemize}"""),
   ("Recap: Classification \\& Anatomy (Meetings 1--3)",
    r"""\begin{itemize}
    \item Aircraft classified by wing configuration, powerplant type, and category/use.
    \item Five major external sections: fuselage, wings, empennage, powerplant, landing gear.
    \item Empennage provides stability via horizontal/vertical stabilizers; nacelle houses
    the engine; pylon attaches it structurally.
    \end{itemize}"""),
   ("Recap: Size, Range \\& Business Classification (Extended)",
    r"""\begin{itemize}
    \item MTOW classes: light, regional, narrow-body, wide-body, very large (Meeting 1).
    \item Range classes: short-haul, medium-haul, long-haul, driven by fuel capacity and
    engine efficiency.
    \item Business models (full-service, low-cost, cargo) explain \emph{why} an operator
    chose a given aircraft, not just \emph{what} the aircraft is.
    \end{itemize}"""),
   ("Recap: Axes of Motion \\& Primary Controls (Meeting 4)",
    r"""\begin{center}\begin{tabular}{l|l|l}\hline
    Axis & Motion & Surface\\\hline
    Longitudinal & Roll & Aileron\\ Lateral & Pitch & Elevator\\ Vertical & Yaw & Rudder\\\hline
    \end{tabular}\end{center}
    Adverse yaw links roll and yaw, corrected with coordinated rudder input."""),
   ("Recap: Secondary Controls \\& High-Lift Devices (Meeting 5)",
    r"""\begin{itemize}
    \item Trim tabs relieve control pressure without acting as a primary control.
    \item Flaps and slats increase lift and delay stall for slow-speed flight.
    \item Spoilers reduce lift/add drag in flight, and act as lift dumpers on landing.
    \end{itemize}"""),
   ("Recap: Structure \\& Load Path (Meeting 6)",
    r"""\begin{itemize}
    \item Spar, rib, stringer, longeron, and frame are the primary structural members.
    \item Load path: skin $\to$ ribs $\to$ spar $\to$ fuselage attach fitting $\to$ frames.
    \item Five basic load types: tension, compression, shear, bending, torsion.
    \end{itemize}"""),
   ("Integration Table: Meeting-by-Meeting Topic Map",
    r"""\begin{center}\begin{tabular}{c|l}\hline
    Meeting & Core Topic\\\hline
    1 & Industry overview and aircraft classification\\
    2 & Fuselage and wing anatomy\\
    3 & Empennage, nacelle, and pylon\\
    4 & Axes of motion and primary flight controls\\
    5 & Secondary controls and high-lift devices\\
    6 & Airframe structure and load path\\\hline
    \end{tabular}\end{center}"""),
   ("Vocabulary Review: Key Terms (Meetings 1--3)",
    r"""\begin{itemize}
    \item \textbf{MTOW, narrow-body, wide-body} -- size and range classification (M1).
    \item \textbf{Semi-monocoque, dihedral, aspect ratio} -- fuselage and wing anatomy (M2).
    \item \textbf{Empennage, nacelle, pylon, T-tail} -- tail and engine-mount anatomy (M3).
    \end{itemize}"""),
   ("Vocabulary Review: Key Terms (Meetings 4--6)",
    r"""\begin{itemize}
    \item \textbf{Adverse yaw, fly-by-wire, flutter} -- primary flight controls (M4).
    \item \textbf{Fowler flap, Krueger flap, lift dumper} -- secondary controls/high-lift (M5).
    \item \textbf{Spar, longeron, fail-safe, fatigue} -- structure and load path (M6).
    \end{itemize}"""),
   ("Integrated Walkthrough: A Complete Aircraft",
    r"""Consider a twin-engine, low-wing, T-tail regional airliner:
    \begin{enumerate}
    \item \textbf{Classification:} fixed-wing, turbofan/turboprop, commercial transport category.
    \item \textbf{Anatomy:} semi-monocoque fuselage, tapered low wing, T-tail empennage,
    wing-mounted nacelles on pylons.
    \item \textbf{Controls:} ailerons/elevator/rudder for the three axes; flaps and slats
    for approach; spoilers for descent and landing roll.
    \item \textbf{Structure:} wing lift travels skin $\to$ ribs $\to$ spar $\to$ fuselage.
    \end{enumerate}
    This single description touches every topic from Meetings 1--6."""),
   ("Cross-Topic Pitfalls",
    r"""\begin{itemize}
    \item Confusing primary controls (aileron/elevator/rudder) with secondary controls
    (flaps/slats/spoilers/trim).
    \item Mixing up stringers (skin stiffeners) with spars (main load-carrying beams).
    \item Forgetting that adverse yaw requires a rudder correction, not just aileron input.
    \item Describing engine mounting without distinguishing nacelle (housing) from pylon
    (structural attachment).
    \end{itemize}"""),
   ("Common Cross-Topic Pitfalls, Part 2",
    r"""\begin{itemize}
    \item Confusing fixed structure (horizontal stabilizer, wing) with the moving control
    surface attached to it (elevator, aileron).
    \item Treating a stress concentration and a fatigue crack as the same thing -- one is a
    location, the other is the damage that can start there.
    \item Mixing up static load capacity with fatigue life -- a part can be strong enough
    for one big load yet still fail from many small repeated loads.
    \end{itemize}"""),
   ("Practice 1 -- Problem",
    r"An aircraft is described as: low-wing, twin turbofan on wing pylons, conventional tail. Classify it by powerplant type and describe its likely wing-position advantage."),
   ("Practice 1 -- Solution",
    r"""Powerplant type: turbofan (most common on modern airliners/business jets).
    \\Low-wing advantage: shorter landing gear and easier engine/fuel system access from
    the ground compared to a high-wing design."""),
   ("Practice 2 -- Problem",
    r"A pilot applies right rudder without any aileron input. Which axis is primarily affected, and what unwanted secondary motion might follow?"),
   ("Practice 2 -- Solution",
    r"""Primary axis: vertical axis (yaw) -- the nose swings right.
    \\Secondary effect: yawing changes airflow over the wings and can induce a slight roll,
    illustrating that the three axes are rarely fully independent."""),
   ("Practice 3 -- Problem",
    r"Trace the load path of lift generated by the left wing, from the wing skin to where it is finally reacted."),
   ("Practice 3 -- Solution",
    r"""Skin $\to$ ribs $\to$ main spar $\to$ wing-root attachment fitting $\to$ fuselage
    frames and longerons, which distribute the load through the rest of the airframe."""),
   ("Practice 4 -- Problem",
    r"During approach, a pilot extends flaps and slats together. Explain the combined effect on stall speed and why both are used rather than flaps alone."),
   ("Practice 4 -- Solution",
    r"""Flaps increase lift and drag at a given speed; slats delay airflow separation
    (stall) at high angle of attack.
    \\Used together, the aircraft can fly safely at a lower approach speed than flaps
    alone would allow, since slats protect against the stall that the higher-lift,
    higher-angle-of-attack flap configuration would otherwise risk."""),
   ("Practice 5 -- Problem",
    r"An aircraft has a T-tail and engines mounted on the rear fuselage. Explain one structural trade-off of this configuration compared to a conventional low-tail, wing-mounted-engine design."),
   ("Practice 5 -- Solution",
    r"""The vertical fin must be structurally stronger to carry the horizontal stabilizer's
    loads at its tip, and the rear fuselage must be reinforced for the tail-mounted engine
    mounts.
    \\In exchange, the wing stays aerodynamically cleaner and the cabin is quieter --
    a trade-off business jets often accept but large airliners usually do not."""),
   ("Practice 6 -- Problem",
    r"During a rejected takeoff, ground spoilers fail to deploy. Explain the effect on stopping performance and why."),
   ("Practice 6 -- Solution",
    r"""Without ground spoilers, the wings continue producing significant lift even at
    high speed on the runway.
    \\That lift reduces the weight pressing the wheels onto the runway, which reduces
    available braking friction and increases stopping distance."""),
   ("Practice 7 -- Problem",
    r"A wing skin panel shows a small crack starting at a rivet hole. Using the concepts of stress concentration and fail-safe design, explain why this is not necessarily an immediate emergency."),
   ("Practice 7 -- Solution",
    r"""The rivet hole is a stress concentration, a likely and expected location for a
    fatigue crack to begin.
    \\Because the structure is fail-safe, neighboring skin, stringers, and ribs share the
    load until the crack is found and repaired at the next scheduled inspection."""),
   ("Practice 8 -- Problem",
    r"Classify the following aircraft using concepts from Meetings 1--6: high-wing, twin turboprop, fixed landing gear, conventional tail, used for regional cargo runs on short unpaved strips."),
   ("Practice 8 -- Solution",
    r"""Wing configuration: high-wing monoplane. Powerplant: turboprop, twin-engine.
    \\Range/size class: short-haul, regional/light class.
    \\High-wing advantage here: better ground clearance and easier cargo loading on
    unpaved strips, consistent with its stated mission."""),
   ("Group Activity: Aircraft Walkaround Roleplay",
    r"""In pairs, one student plays inspector, one plays a new trainee.
    \begin{enumerate}
    \item The inspector points to a part of a photographed aircraft; the trainee names it
    and its function.
    \item Switch roles after five parts.
    \item Finish by having the trainee trace one load path (wing lift or landing impact)
    from start to finish, out loud.
    \end{enumerate}"""),
   ("Self-Assessment Checklist (Meetings 1--6)",
    r"""Before continuing, confirm you can do each of the following without notes:
    \begin{itemize}
    \item Classify an aircraft by wing configuration, powerplant, size, and range.
    \item Label the fuselage, wing, empennage, nacelle, and pylon on a photo.
    \item Name the axis, surface, and effect for roll, pitch, and yaw.
    \item Explain the difference between primary and secondary flight controls.
    \item Trace a load path from the wing skin to the fuselage.
    \end{itemize}"""),
   ("Study Strategy Going Into Meeting 8",
    r"""\begin{itemize}
    \item Meeting 8 is a further integrated review, immediately before the Meeting 9 midterm.
    \item Use today's self-assessment checklist to target your weakest areas first.
    \item Redo any of today's eight practice problems from a blank page, not just re-reading
    the solutions.
    \end{itemize}"""),
   ("Extended In-Class Practice / Group Discussion",
    r"""In small groups, discuss and be ready to present:
    \begin{enumerate}
    \item Pick any real aircraft and produce a full classification-to-structure description,
    using the integration table as a checklist.
    \item Debate which of today's cross-topic pitfalls is the easiest to fall into, and why.
    \item Create one new practice problem of your own, combining at least two of
    Meetings 1--6, and trade with another group to solve.
    \end{enumerate}""")],
  I("Meetings 1--6 combine into a complete description of any real aircraft.",
    "Most confusion comes from mixing up primary/secondary controls or structural member names.",
    "A systematic walkthrough (classification, anatomy, controls, structure) answers most integrated questions."),
  I("Write a full classification-to-structure description of an aircraft of your choice.",
    "Redo Practice 1--4 from a blank page without looking at the solutions.",
    "Prepare a one-page vocabulary sheet for the midterm."))

M[8] = ("Integrated Review (Pre-Midterm)",
  "Students are able to solve integrated problems in preparation for the mid-semester exam.",
  I("Solve integrated exercises under time.",
    "Identify and correct common mistakes.",
    "Confirm readiness for the midterm."),
  [("Midterm Scope",
    r"""The midterm (Meeting 9) covers \textbf{Meetings 1--8} end to end:
    \begin{itemize}
    \item Aviation industry overview and aircraft classification.
    \item Fuselage and wing anatomy; empennage, nacelle, and pylon.
    \item Axes of motion and primary flight controls.
    \item Secondary flight controls and high-lift devices.
    \item Airframe structure and load path.
    \end{itemize}"""),
   ("Summary Sheet: Classification \\& Anatomy",
    r"""\begin{itemize}
    \item Classify by wing configuration, powerplant type, and category/use.
    \item Five major sections: fuselage, wing, empennage, powerplant, landing gear.
    \item Fuselage: truss / monocoque / semi-monocoque (modern standard).
    \item Wing position: high (ground clearance) vs.\ low (shorter gear, easier access).
    \end{itemize}"""),
   ("Summary Sheet: Size, Range \\& Business Classification",
    r"""\begin{itemize}
    \item MTOW classes: light, regional, narrow-body, wide-body, very large.
    \item Range classes: short-haul, medium-haul, long-haul.
    \item Business models: full-service, low-cost carrier, cargo carrier.
    \item Regulatory bodies: ICAO (global), FAA/EASA (regional), DGCA (Indonesia).
    \end{itemize}"""),
   ("Exam Format and Question Types",
    r"""\begin{itemize}
    \item \textbf{Identification/labeling:} name a part or surface from a diagram or photo.
    \item \textbf{Short answer:} explain a function, trade-off, or comparison in a sentence or two.
    \item \textbf{Applied scenario:} trace a sequence (control input to motion, or load path)
    step by step.
    \end{itemize}
    Knowing the question type in advance helps you allocate time and choose the right
    level of detail in your answer."""),
   ("High-Yield Topics: What's Most Likely to Be Tested",
    r"""Based on Meetings 1--6, these topics recur most often across the practice problems:
    \begin{itemize}
    \item Classification (wing configuration, powerplant, category).
    \item Axis $\to$ surface $\to$ motion mapping, including adverse yaw.
    \item Flaps vs.\ slats vs.\ spoilers -- function and timing.
    \item Load path from wing lift to the fuselage attachment.
    \end{itemize}"""),
   ("Summary Sheet: Empennage, Axes \\& Primary Controls",
    r"""\begin{itemize}
    \item Empennage: horizontal stabilizer + elevator (pitch); vertical stabilizer + rudder (yaw).
    \item Nacelle houses the engine; pylon structurally attaches it to the wing/fuselage.
    \item Roll--aileron--longitudinal axis; Pitch--elevator--lateral axis; Yaw--rudder--vertical axis.
    \item Adverse yaw: down-going aileron's drag yaws the nose opposite the turn; correct with rudder.
    \end{itemize}"""),
   ("Summary Sheet: Secondary Controls \\& High-Lift Devices",
    r"""\begin{itemize}
    \item Trim tabs relieve control pressure; not a primary flight control.
    \item Flaps (plain/split/slotted/Fowler) increase lift and drag for slow flight.
    \item Slats delay stall at high angle of attack, extended together with flaps.
    \item Spoilers reduce lift/increase drag in flight and act as lift dumpers on landing.
    \end{itemize}"""),
   ("Summary Sheet: Structure \\& Load Path",
    r"""\begin{itemize}
    \item Spar (main wing beam), rib (airfoil shape), stringer/longeron (skin stiffener),
    frame (fuselage former).
    \item Load path: skin $\to$ ribs $\to$ spar $\to$ fuselage attach fitting $\to$ frames/longerons.
    \item Five load types: tension, compression, shear, bending, torsion.
    \item Fail-safe (multiple load paths) and damage-tolerant (inspectable before failure) design.
    \end{itemize}"""),
   ("Common Mistakes",
    r"""\begin{itemize}
    \item Confusing wing-position advantages (high vs.\ low) with tail-configuration
    trade-offs (conventional vs.\ T-tail).
    \item Mixing up which surface controls which axis (aileron/elevator/rudder).
    \item Treating flaps and slats as the same device -- they act on different parts of
    the wing.
    \item Naming a stringer when the question describes the main load-carrying spar, or vice versa.
    \end{itemize}"""),
   ("Time-Management Strategy",
    r"""\begin{itemize}
    \item Skim the whole exam first; answer the fastest identification questions first
    to bank points.
    \item For diagram/labeling questions, label every part you are sure of before
    reasoning through the uncertain ones.
    \item Reserve the last few minutes to re-check axis-to-surface and load-path sequences.
    \end{itemize}"""),
   ("Diagram-Labeling Practice",
    r"""Without looking at notes, label from memory (check yourself afterward):
    \begin{enumerate}
    \item The five major external sections of a fixed-wing aircraft.
    \item Horizontal stabilizer, elevator, vertical stabilizer, and rudder on a tail sketch.
    \item Spar, rib, and skin on a wing cross-section sketch.
    \end{enumerate}"""),
   ("Time-Boxed Practice Round (Concept)",
    r"""\begin{itemize}
    \item Set a timer for 10 minutes and attempt Practice 1--8 (this meeting) without
    checking solutions until time is up.
    \item This simulates real exam time pressure, which is different from untimed review.
    \item Afterward, grade honestly against the solutions and note which topics took
    longest to answer -- those need more review before Meeting 9.
    \end{itemize}"""),
   ("Practice 1 -- Problem",
    r"An aircraft has a high wing, fixed landing gear, and a single piston engine on the nose. Classify it by wing configuration, powerplant, and likely category."),
   ("Practice 1 -- Solution",
    r"""Wing configuration: high-wing monoplane.
    \\Powerplant: piston (reciprocating).
    \\Likely category: general aviation (utility/trainer type)."""),
   ("Practice 2 -- Problem",
    r"A pilot pulls the control column aft with no other input. Name the axis, the surface, and the resulting motion."),
   ("Practice 2 -- Solution",
    r"""Axis: lateral axis. Surface: elevator. Motion: pitch -- specifically, the nose
    rises (nose-up pitch)."""),
   ("Practice 3 -- Problem",
    r"During landing rollout, spoilers deploy fully. Explain their purpose at this specific moment, as opposed to their in-flight use."),
   ("Practice 3 -- Solution",
    r"""On rollout, fully deployed spoilers act as lift dumpers: they destroy remaining
    wing lift so the aircraft's full weight presses onto the wheels, improving brake and
    wheel-braking effectiveness and shortening the landing roll.
    \\In flight, the same spoilers are instead used partially, as speedbrakes or for roll assistance."""),
   ("Practice 4 -- Problem",
    r"A wing rib cracks near its trailing edge. Explain, using the load-path concept, why this does not necessarily cause immediate structural failure."),
   ("Practice 4 -- Solution",
    r"""Ribs mainly maintain airfoil shape and feed local skin loads into the spar; they
    are not the wing's main load-carrying member.
    \\Because the structure is fail-safe (multiple load paths through nearby ribs and the
    spar), the load that the cracked rib would have carried is redistributed to
    neighboring structure until the crack is found and repaired during scheduled inspection."""),
   ("Practice 5 -- Problem",
    r"An aircraft is described as narrow-body, twin-engine, medium-haul, operated by a low-cost carrier. What does each term tell you, and what does it not tell you?"),
   ("Practice 5 -- Solution",
    r"""Narrow-body: single aisle, roughly 60--90 tonne MTOW class.
    \\Twin-engine: two engines, most common modern configuration.
    \\Medium-haul: 1{,}500--4{,}000 km typical range.
    \\Low-cost carrier: describes the business model, not the airframe -- the same aircraft
    type could equally be flown by a full-service carrier."""),
   ("Practice 6 -- Problem",
    r"A T-tail aircraft is compared to a conventional-tail aircraft of similar size. Name one aerodynamic advantage and one structural disadvantage of the T-tail."),
   ("Practice 6 -- Solution",
    r"""Aerodynamic advantage: horizontal stabilizer sits clear of engine/wing wake, giving
    cleaner, more consistent airflow.
    \\Structural disadvantage: the vertical fin must be reinforced to carry the horizontal
    stabilizer's loads at its tip."""),
   ("Practice 7 -- Problem",
    r"During approach, the crew selects flaps and slats to the landing position and arms the ground spoilers. Explain the role of each action."),
   ("Practice 7 -- Solution",
    r"""Flaps/slats to landing position: maximize lift and delay stall, allowing a safe,
    lower approach speed.
    \\Arming ground spoilers: prepares them to deploy automatically at touchdown, dumping
    lift onto the wheels for maximum braking effectiveness without a separate crew action."""),
   ("Practice 8 -- Problem",
    r"A fuselage skin panel shows a small crack at a rivet hole near a window cutout. Explain, using both stress concentration and fatigue concepts, why this location is unsurprising."),
   ("Practice 8 -- Solution",
    r"""Both the rivet hole and the window cutout are stress concentrations -- local areas
    of higher stress than the surrounding skin.
    \\Repeated pressurization cycling (fatigue loading) makes stress concentrations the
    most likely place for a crack to initiate, which is exactly why they are prioritized
    during scheduled inspections."""),
   ("Common Last-Minute Mistakes to Avoid",
    r"""\begin{itemize}
    \item Leaving diagram-labeling questions until last -- do them early while memory is fresh.
    \item Writing a vague answer instead of naming the specific part or term the question asks for.
    \item Confusing similar-sounding terms (stabilizer vs.\ stabilator; spoiler vs.\ speedbrake).
    \item Running out of time on one long applied-scenario question at the expense of
    several shorter ones.
    \end{itemize}"""),
   ("Final Checklist Before the Midterm",
    r"""\begin{itemize}
    \item Completed the self-assessment checklist from Meeting 7.
    \item Redone every Practice problem from Meetings 7--8 from a blank page.
    \item Reviewed the four summary sheets and the vocabulary lists at least once each.
    \item Confirmed the exam covers Meetings 1--8 only -- nothing from Meeting 10 onward.
    \end{itemize}"""),
   ("What Comes After the Midterm",
    r"""\begin{itemize}
    \item Meeting 10 onward shifts from anatomy and controls to materials, systems, and
    powerplants: airframe materials (metallic and composite), landing gear, powerplant,
    fuel/hydraulic/pneumatic systems, and electrical/avionics basics.
    \item The vocabulary and classification skills from Meetings 1--8 remain the foundation
    for every one of those later topics.
    \item Meeting 17 provides an equivalent integrated review before the Meeting 18 final exam.
    \end{itemize}"""),
   ("Extended In-Class Practice / Group Discussion",
    r"""In small groups, discuss and be ready to present:
    \begin{enumerate}
    \item Each student writes one new practice question; trade and solve within the group.
    \item Debate which topic from Meetings 1--6 the group finds most difficult, and why.
    \item Run a rapid-fire round: one student names a term, another defines it, in under
    10 seconds each.
    \end{enumerate}""")],
  I("Midterm covers Meetings 1--8 end to end.",
    "Most errors come from mixing up similarly named parts or confusing primary and secondary controls.",
    "Timed self-checked practice with the summary sheets builds readiness."),
  I("Complete the timed practice set and mark your own work against the solutions.",
    "Build a one-page labeled diagram covering anatomy, controls, and structure.",
    "Redo any Meeting 1--7 practice problem you previously missed."))

M[10] = ("Airframe Materials: Metallic Structures",
  "Students are able to explain metallic and composite airframe materials and their structural characteristics.",
  I("Explain the properties and applications of metallic materials (aluminum, titanium, steel) on the airframe.",
    "Compare metallic materials by strength-to-weight, corrosion resistance, and typical use.",
    "Explain corrosion types and prevention methods for metallic airframe structures."),
  [("Why Airframe Materials Matter",
    r"""Every structural member named in Meeting 6 (spar, rib, stringer, frame) is made from
    a specific material chosen for a reason.
    \begin{itemize}
    \item Material choice drives an airframe's weight, strength, cost, and maintenance needs.
    \item Meetings 10--11 cover the two dominant airframe material families: metallic
    (this meeting) and composite (Meeting 11).
    \item Understanding material properties explains \emph{why} structures are built the
    way they are, not just \emph{what} they are called.
    \end{itemize}"""),
   ("Material Selection Criteria",
    r"""\begin{itemize}
    \item \textbf{Strength-to-weight ratio:} how much load a material carries per unit of weight.
    \item \textbf{Corrosion resistance:} how well the material resists environmental degradation.
    \item \textbf{Fatigue life:} how the material behaves under repeated loading (Meeting 6).
    \item \textbf{Cost and manufacturability:} how affordably and easily the material can be
    formed into aircraft parts.
    \end{itemize}
    No single material wins on every criterion -- every airframe is a compromise across them."""),
   ("Aluminum Alloys: Overview",
    r"""\begin{itemize}
    \item Aluminum alloys have been the dominant airframe material since the 1930s
    (Meeting 1's all-metal monoplane era).
    \item Roughly one-third the density of steel, with alloys reaching comparable
    strength-to-weight performance for many applications.
    \item Easy to form, machine, and rivet, with a long, well-understood service history --
    a major advantage for certification and maintenance.
    \end{itemize}"""),
   ("Aluminum Alloy Designation System (Concept)",
    r"""\begin{itemize}
    \item Aluminum alloys are identified by a four-digit number; the first digit indicates
    the primary alloying element (e.g.\ 2xxx = copper, 6xxx = magnesium/silicon, 7xxx = zinc).
    \item Different series trade off strength, corrosion resistance, and fatigue behavior.
    \item Knowing the series tells a technician roughly what performance and precautions
    to expect, without needing the exact alloy composition memorized.
    \end{itemize}"""),
   ("Common Aluminum Alloys and Uses",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Alloy & Typical Use\\\hline
    2024 & Fuselage skin, areas needing high fatigue resistance\\
    6061 & General-purpose structure, moderate strength\\
    7075 & Wing spars, high-stress fittings needing maximum strength\\\hline
    \end{tabular}\end{center}
    The right-hand column repeats the same lesson as Meeting 6: the highest-load members
    (spars) get the highest-strength alloy."""),
   ("Alclad Aluminum",
    r"""\begin{itemize}
    \item \textbf{Alclad} is high-strength aluminum sheet with a thin layer of pure aluminum
    bonded to both surfaces.
    \item The pure aluminum cladding is far more corrosion-resistant, sacrificially
    protecting the stronger (but more corrosion-prone) core alloy beneath it.
    \item Widely used for fuselage and wing skin, where corrosion resistance on an
    exposed outer surface matters most.
    \end{itemize}"""),
   ("Heat Treatment of Aluminum (Concept)",
    r"""\begin{itemize}
    \item Many aluminum alloys reach their full strength only after \textbf{heat treatment} --
    heating, rapid cooling, and then aging (naturally or artificially).
    \item Heat treatment rearranges the alloy's internal structure to resist deformation,
    significantly increasing strength.
    \item Improper heat treatment (or heat damage from a repair, such as welding) can
    silently weaken a part -- a key reason repair procedures are tightly controlled.
    \end{itemize}"""),
   ("Titanium Alloys: Overview",
    r"""\begin{itemize}
    \item Titanium alloys combine high strength with roughly 60\% the density of steel.
    \item More expensive and harder to machine than aluminum, so used selectively rather
    than throughout the airframe.
    \item Excellent corrosion resistance and retains strength at higher temperatures than
    aluminum can tolerate.
    \end{itemize}"""),
   ("Titanium: Properties and Uses",
    r"""\begin{itemize}
    \item \textbf{High strength-to-weight:} used at highly loaded fittings where aluminum
    would be too weak and steel too heavy.
    \item \textbf{Heat resistance:} used near engines and exhaust areas where aluminum
    would soften or lose strength.
    \item \textbf{Corrosion resistance:} used at fastener/fitting interfaces exposed to
    moisture or dissimilar-metal contact.
    \end{itemize}"""),
   (r"Titanium vs.\ Aluminum Comparison",
    r"""\begin{center}\begin{tabular}{l|l|l}\hline
    Aspect & Aluminum & Titanium\\\hline
    Density & Lower & About 1.6$\times$ aluminum\\
    Cost & Lower & Significantly higher\\
    Heat tolerance & Lower & Higher\\
    Typical use & Skin, general structure & Engine-area fittings, high-load joints\\\hline
    \end{tabular}\end{center}"""),
   ("Steel Alloys: Overview",
    r"""\begin{itemize}
    \item Steel alloys offer the highest strength of the three metal families covered
    this meeting, but at the highest density (weight penalty).
    \item Used only where extreme strength in a small volume outweighs the weight cost.
    \item Often alloyed with chromium, nickel, or molybdenum for added strength and
    corrosion resistance.
    \end{itemize}"""),
   ("Steel: Properties and Uses",
    r"""\begin{itemize}
    \item \textbf{Landing gear} (Meeting 12): steel's strength handles the enormous impact
    and side loads of touchdown in a compact structure.
    \item \textbf{High-stress fittings:} wing-to-fuselage attachment pins and similar
    highly loaded, small-volume parts.
    \item \textbf{Engine mount components} (Meeting 3): where high strength and heat
    resistance are both required.
    \end{itemize}"""),
   (r"Comparison: Aluminum vs.\ Titanium vs.\ Steel",
    r"""\begin{center}\begin{tabular}{l|l|l|l}\hline
    Property & Aluminum & Titanium & Steel\\\hline
    Relative density & Lowest & Middle & Highest\\
    Relative cost & Lowest & Highest & Middle\\
    Typical airframe use & Skin, general structure & Hot/high-load fittings & Landing gear\\\hline
    \end{tabular}\end{center}"""),
   ("Corrosion Types Overview",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Type & Description\\\hline
    Galvanic & Occurs where dissimilar metals contact in the presence of moisture\\
    Pitting & Small, deep localized pits, often starting at a scratch or defect\\
    Stress corrosion & Cracking from the combination of sustained stress and corrosion\\
    Exfoliation & Layers of metal lift and separate, following the grain structure\\\hline
    \end{tabular}\end{center}"""),
   ("Corrosion Prevention Methods",
    r"""\begin{itemize}
    \item \textbf{Anodizing:} an electrochemical process that builds a protective oxide
    layer on aluminum parts.
    \item \textbf{Paint and primer:} a physical barrier keeping moisture away from bare metal.
    \item \textbf{Sealant:} applied at joints, fastener holes, and panel edges to block
    moisture entry paths.
    \item \textbf{Drainage design:} holes and channels that let water escape rather than pool.
    \end{itemize}"""),
   ("Galvanic Corrosion (Concept)",
    r"""\begin{itemize}
    \item When two dissimilar metals are in contact with an electrolyte (such as moist air
    or water), one metal corrodes preferentially to protect the other.
    \item Aircraft designers separate dissimilar metals with non-conductive sealant, paint,
    or isolating washers wherever they must be joined.
    \item This is why a repair using the wrong fastener material can create a corrosion
    problem that did not exist in the original design.
    \end{itemize}"""),
   ("Metal Fatigue Recap and Material Context",
    r"""\begin{itemize}
    \item Meeting 6 introduced fatigue as damage from repeated loading, regardless of material.
    \item Different metals have different \textbf{fatigue life} characteristics --
    2024 aluminum, for example, is specifically favored for its good fatigue resistance.
    \item Material selection and fatigue-aware design work together: the right alloy in
    the right location extends the whole airframe's safe service life.
    \end{itemize}"""),
   ("Metal Forming Processes Overview (Brief)",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Process & Description\\\hline
    Rolling & Metal passed between rollers to form flat sheet or plate\\
    Extrusion & Metal pushed through a shaped die to form a constant cross-section\\
    Forging & Metal shaped under high compressive force; very strong grain structure\\
    Casting & Molten metal poured into a mold; complex shapes, lower strength\\\hline
    \end{tabular}\end{center}"""),
   ("Sheet Metal Fabrication (Brief)",
    r"""\begin{itemize}
    \item Most skin panels and many minor structural parts start as flat sheet stock.
    \item \textbf{Forming:} bending or pressing sheet into a curved or angled shape.
    \item \textbf{Stretch forming:} sheet is stretched over a form to create smooth,
    large-radius curves, common for wing and fuselage skin panels.
    \end{itemize}"""),
   ("Metal Joining Methods: Riveting Deep-Dive",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Rivet Type & Use\\\hline
    Solid rivet & Standard structural joint, installed with access to both sides\\
    Blind (pop) rivet & Installed from one side only, for limited-access locations\\
    Countersunk rivet & Sits flush with the skin surface, reducing aerodynamic drag\\\hline
    \end{tabular}\end{center}"""),
   ("Metal Joining Methods: Welding (Brief)",
    r"""\begin{itemize}
    \item Welding fuses two metal parts together using heat, sometimes with filler material.
    \item Used selectively on airframes -- more common on engine mounts, steel tube
    structures, and certain landing gear components than on riveted skin structure.
    \item Welded joints must be carefully controlled, since heat can alter the surrounding
    metal's properties (recall heat treatment, discussed earlier this meeting).
    \end{itemize}"""),
   ("Material Testing/Inspection: NDT for Metals",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Method & Best For\\\hline
    Dye penetrant & Surface-breaking cracks, visible after dye/developer application\\
    Magnetic particle & Surface and near-surface cracks in ferromagnetic (steel) parts\\
    Eddy current & Surface cracks and thickness/conductivity checks, no consumables\\
    Ultrasonic & Internal flaws, deep within thick material\\\hline
    \end{tabular}\end{center}"""),
   ("Material Certification and Traceability",
    r"""\begin{itemize}
    \item Every batch of aircraft-grade metal comes with a \textbf{material certificate}
    documenting its exact alloy, heat-treatment condition, and test results.
    \item Traceability links a specific part back to its material batch, so a discovered
    defect can be tracked to every other part made from the same batch.
    \item This is why unapproved or untraceable ("bogus") parts are a serious safety and
    regulatory concern in aviation maintenance.
    \end{itemize}"""),
   ("Case Study: Alclad Preventing Corrosion Failure",
    r"""\begin{itemize}
    \item Bare high-strength 2024 aluminum sheet is notably prone to corrosion, especially
    stress corrosion, if left unprotected.
    \item The alclad layer sacrifices itself to corrosion first, protecting the structural
    core -- extending service life significantly compared to unclad sheet.
    \item This single manufacturing step is a major reason aluminum skin panels routinely
    remain airworthy for decades of service.
    \end{itemize}"""),
   ("Case Study: Material Selection Trade-off in a Real Aircraft",
    r"""\begin{itemize}
    \item Aircraft such as the Boeing 737 remain predominantly aluminum, even as newer
    designs shift toward composite (Meeting 11).
    \item Aluminum's lower cost, decades of maintenance experience, and simpler repair
    process kept it the better choice for a high-volume, cost-sensitive narrow-body program.
    \item This illustrates that material selection is a business and engineering decision
    together, not simply "use the newest, lightest material available."
    \end{itemize}"""),
   (r"Comparison: Cast vs.\ Forged vs.\ Machined Metal Parts",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Method & Trade-off\\\hline
    Cast & Complex shapes possible, but generally lower strength\\
    Forged & Very strong grain structure, higher cost, simpler shapes\\
    Machined from billet & Precise dimensions, can waste significant raw material\\\hline
    \end{tabular}\end{center}"""),
   ("Corrosion Inspection in Practice",
    r"""\begin{itemize}
    \item \textbf{Bubbling or blistering paint} often indicates corrosion product forming beneath the surface.
    \item \textbf{White or gray powdery residue} on aluminum is a classic visible sign of
    aluminum oxide corrosion.
    \item \textbf{Pitting} appears as small dark spots or craters, often found first during
    a close visual inspection under good lighting.
    \end{itemize}"""),
   ("Applied Scenario: Choosing a Material for a Wing Spar",
    r"""A new wing spar design needs maximum strength-to-weight in a highly loaded member. Work through the choice:
    \begin{enumerate}
    \item Steel is too heavy for this application despite its strength.
    \item Titanium's strength-to-weight is excellent, but its cost is hard to justify for
    a part this large.
    \item A high-strength aluminum alloy (such as 7075) offers the best balance of
    strength, weight, and cost for this component.
    \end{enumerate}"""),
   ("Applied Scenario: Diagnosing Galvanic Corrosion at a Fastener",
    r"""An inspector finds white corrosion product around a steel fastener installed
    directly into bare aluminum structure. Work through the diagnosis:
    \begin{enumerate}
    \item Two dissimilar metals (steel and aluminum) are in direct contact.
    \item Moisture at the joint completes the conditions for galvanic corrosion.
    \item The repair should isolate the fastener from the aluminum with sealant or an
    approved coating, not just clean and reinstall the same way.
    \end{enumerate}"""),
   ("Common Misconceptions About Metal Airframes",
    r"""\begin{itemize}
    \item \textbf{Myth:} aluminum airframes do not fail from fatigue if kept corrosion-free.
    \textbf{Fact:} fatigue and corrosion are separate threats that can each act alone.
    \item \textbf{Myth:} titanium is simply "better" than aluminum. \textbf{Fact:} its cost
    and machining difficulty make it unsuitable for most of the airframe.
    \item \textbf{Myth:} welding is common throughout modern airframes. \textbf{Fact:}
    riveting and bonding dominate; welding is reserved for specific components.
    \end{itemize}"""),
   ("In-Class Practice",
    r"""\begin{enumerate}
    \item Name the three main metal families used in airframes and one typical use for each.
    \item Explain the purpose of Alclad aluminum sheet.
    \item Describe two methods used to prevent corrosion on a metal airframe.
    \end{enumerate}"""),
   ("Extended In-Class Practice / Group Discussion",
    r"""In small groups, discuss and be ready to present:
    \begin{enumerate}
    \item Debate: for a new small-aircraft landing gear, would you choose steel or
    titanium? Justify using weight, strength, and cost.
    \item Explain, using the Aluminum vs.\ Titanium vs.\ Steel comparison table, why no
    single material replaces the other two.
    \item Sketch a fastener joint between two dissimilar metals and label where sealant
    would prevent galvanic corrosion.
    \end{enumerate}""")],
  I("Aluminum, titanium, and steel each have distinct strength, weight, and cost trade-offs on the airframe.",
    "Alclad, heat treatment, and corrosion prevention methods extend metallic structure service life.",
    "Corrosion (galvanic, pitting, stress, exfoliation) is a separate threat from fatigue, requiring its own prevention and inspection."),
  I("Compare aluminum, titanium, and steel by strength-to-weight, cost, and typical airframe use.",
    "Explain the purpose of Alclad aluminum sheet.",
    "Describe galvanic corrosion and how it is prevented at a dissimilar-metal joint.",
    "Name two non-destructive testing methods used to inspect metallic structure."))

M[11] = ("Airframe Materials: Composite Structures",
  "Students are able to explain metallic and composite airframe materials and their structural characteristics.",
  I("Explain the properties and applications of composite materials (CFRP, GFRP, honeycomb) on the airframe.",
    "Compare composite and metallic structures by weight, fatigue, and corrosion behavior.",
    "Explain composite-specific damage types and their inspection methods."),
  [("Why Composite Materials Matter",
    r"""Meeting 10 covered metallic airframe materials; this meeting covers the fastest-growing
    alternative.
    \begin{itemize}
    \item Composite materials now make up roughly half the structural weight of the
    newest airliners (recall the Boeing 787 case study from Meeting 1).
    \item Composites behave very differently from metal -- in strength, fatigue,
    corrosion, damage, and repair.
    \item This meeting explains what composites are and why they are reshaping
    modern airframe design.
    \end{itemize}"""),
   ("What Is a Composite Material? (Concept)",
    r"""\begin{itemize}
    \item A \textbf{composite} combines two distinct materials to get properties neither
    has alone: reinforcing \textbf{fibers} and a surrounding \textbf{matrix} (resin).
    \item The fibers carry most of the load; the resin holds the fibers in shape and
    transfers load between them.
    \item This is conceptually similar to reinforced concrete: steel bars (fiber) carry
    tension, concrete (matrix) holds everything in place.
    \end{itemize}"""),
   (r"Fiber Types: Carbon Fiber vs.\ Fiberglass",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Fiber Type & Characteristics\\\hline
    Carbon fiber (CFRP) & Very high strength-to-weight, higher cost, primary structure\\
    Fiberglass (GFRP) & Lower strength-to-weight, lower cost, secondary/non-structural parts\\\hline
    \end{tabular}\end{center}
    CFRP = Carbon Fiber Reinforced Polymer; GFRP = Glass Fiber Reinforced Polymer."""),
   ("Resin Systems (Matrix) Overview",
    r"""\begin{itemize}
    \item \textbf{Epoxy resin} is the most common matrix for aerospace composites, offering
    good strength and heat resistance.
    \item The resin must be selected to match the manufacturing process (Meeting 11's
    layup and curing topics) and the temperature range the part will experience in service.
    \item Resin, not fiber, is usually the first material to be affected by excess heat,
    moisture absorption, or chemical exposure.
    \end{itemize}"""),
   (r"Comparison: CFRP vs.\ GFRP",
    r"""\begin{center}\begin{tabular}{l|l|l}\hline
    Aspect & CFRP & GFRP\\\hline
    Strength-to-weight & Excellent & Good, lower than CFRP\\
    Cost & Higher & Lower\\
    Typical use & Primary structure (wings, fuselage) & Fairings, radomes, interior panels\\\hline
    \end{tabular}\end{center}"""),
   ("Composite Layup Process (Concept)",
    r"""\begin{enumerate}
    \item Fiber material (in sheet or tape form) is cut to shape.
    \item Layers (\textbf{plies}) are stacked in a mold, each oriented in a specific direction.
    \item Resin is applied (or is already present, see prepreg) and the stack is compacted.
    \item The assembly is cured (hardened) under heat and pressure.
    \end{enumerate}"""),
   ("Prepreg and Autoclave Curing",
    r"""\begin{itemize}
    \item \textbf{Prepreg} fiber sheet arrives from the supplier already impregnated with
    uncured resin, kept refrigerated until use for precise, repeatable material properties.
    \item An \textbf{autoclave} is a heated, pressurized oven that cures prepreg layups,
    forcing out trapped air and ensuring uniform resin distribution.
    \item Autoclave curing produces the highest-quality structural parts, at higher cost
    and slower cycle time than simpler curing methods.
    \end{itemize}"""),
   ("Fiber Orientation and Ply Stacking (Concept)",
    r"""\begin{itemize}
    \item A single ply of fiber is strong mainly along the fiber direction, weak across it.
    \item Engineers stack plies at different angles (e.g.\ 0\textdegree, 45\textdegree,
    90\textdegree) so the laminate resists loads from multiple directions.
    \item This ply-by-ply design freedom lets composite structures be tailored to their
    exact loading, something a uniform metal sheet cannot do.
    \end{itemize}"""),
   ("Honeycomb Sandwich Structure",
    r"""\begin{itemize}
    \item A \textbf{sandwich panel} bonds two thin composite (or metal) face-sheets to a
    lightweight \textbf{honeycomb core} between them.
    \item The face-sheets carry bending loads (like the flanges of a beam); the core
    resists shear and keeps the face-sheets apart, resisting buckling.
    \item Widely used for control surfaces, fairings, and floor panels where high
    stiffness-to-weight matters more than raw strength.
    \end{itemize}"""),
   (r"Honeycomb Core Materials: Aluminum vs.\ Nomex",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Core Material & Characteristics\\\hline
    Aluminum honeycomb & Strong, lower cost, can corrode if moisture enters cells\\
    Nomex (aramid paper) honeycomb & Lighter, corrosion-immune, better fire resistance\\\hline
    \end{tabular}\end{center}"""),
   (r"Comparison: Solid Laminate vs.\ Sandwich Structure",
    r"""\begin{center}\begin{tabular}{l|l|l}\hline
    Aspect & Solid Laminate & Sandwich (Honeycomb)\\\hline
    Weight for given stiffness & Heavier & Lighter\\
    Typical use & Highly loaded primary structure & Control surfaces, fairings, floors\\
    Damage tolerance & Generally higher & Core can be crushed by impact\\\hline
    \end{tabular}\end{center}"""),
   (r"Composite vs.\ Metal: Strength-to-Weight Comparison",
    r"""\begin{itemize}
    \item CFRP composite typically offers a higher strength-to-weight ratio than aluminum
    for the same structural task.
    \item This weight saving is the primary driver behind composite adoption on the 787
    and A350 (revisited later this meeting).
    \item The saving is not automatic -- it depends on the structure being properly
    designed to exploit the fiber-direction strength described earlier.
    \end{itemize}"""),
   (r"Composite vs.\ Metal: Fatigue Behavior Comparison",
    r"""\begin{center}\begin{tabular}{l|l|l}\hline
    Aspect & Metal & Composite\\\hline
    Fatigue behavior & Cracks initiate and grow steadily & Generally excellent fatigue resistance\\
    Failure warning & Often visible crack growth & Can fail with less visible warning\\\hline
    \end{tabular}\end{center}
    Composite's excellent fatigue resistance is a major operational advantage, but it
    shifts the inspection challenge toward impact damage instead (covered later)."""),
   (r"Composite vs.\ Metal: Corrosion Resistance Comparison",
    r"""\begin{itemize}
    \item Composite material does not corrode the way aluminum or steel does -- there is
    no metal to oxidize.
    \item This eliminates an entire category of inspection and maintenance (Meeting 10's
    corrosion topics) for composite structure.
    \item However, moisture can still be absorbed into the resin or honeycomb core over
    time, which is its own inspection concern.
    \end{itemize}"""),
   (r"Comparison Table: Composite vs.\ Aluminum vs.\ Titanium",
    r"""\begin{center}\begin{tabular}{l|l|l|l}\hline
    Property & Composite (CFRP) & Aluminum & Titanium\\\hline
    Strength-to-weight & Excellent & Good & Very good\\
    Corrosion & Immune & Requires protection & Excellent\\
    Repair complexity & Specialized process & Well-established & Well-established\\\hline
    \end{tabular}\end{center}"""),
   (r"Composite Manufacturing: Hand Layup vs.\ Automated Fiber Placement",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Method & Description\\\hline
    Hand layup & Technicians place plies manually; flexible, labor-intensive\\
    Automated fiber placement (AFP) & Robotic machine lays fiber tape precisely and quickly\\\hline
    \end{tabular}\end{center}
    Large modern composite structures (e.g.\ 787 fuselage barrel sections) rely heavily
    on automated fiber placement for consistency at high production volume."""),
   ("Composite Damage Types: Delamination",
    r"""\begin{itemize}
    \item \textbf{Delamination} is separation between adjacent plies within a laminate.
    \item Often caused by impact, manufacturing defects, or moisture ingress over time.
    \item Dangerous because it can be invisible from the outside surface while
    significantly weakening the structure internally.
    \end{itemize}"""),
   ("Composite Damage Types: Disbond",
    r"""\begin{itemize}
    \item A \textbf{disbond} is separation at a bonded joint, such as between a
    honeycomb core and its face-sheet.
    \item Distinct from delamination (which is within a laminate) -- disbond is at the
    interface between two separately bonded components.
    \item Both delamination and disbond can spread under repeated loading if not caught early.
    \end{itemize}"""),
   ("Composite Damage Types: Impact Damage (BVID)",
    r"""\begin{itemize}
    \item \textbf{BVID (barely visible impact damage)} is internal damage from an impact
    (e.g.\ a dropped tool) that leaves little or no visible surface mark.
    \item The composite can suffer significant internal delamination while looking almost
    undamaged from the outside.
    \item This is why composite structures require specific NDT inspection after any
    known impact event, rather than relying on a visual check alone.
    \end{itemize}"""),
   ("Composite Damage: Why It's Different From Metal Damage (Concept)",
    r"""\begin{center}\begin{tabular}{l|l|l}\hline
    Aspect & Metal Damage & Composite Damage\\\hline
    Typical visibility & Often visible (dent, crack) & Can be internal, barely visible\\
    Growth pattern & Crack grows along the surface & Delamination can spread internally\\
    Detection approach & Visual inspection often sufficient & NDT often required after impact\\\hline
    \end{tabular}\end{center}"""),
   ("Composite Inspection Methods: Tap Test",
    r"""\begin{itemize}
    \item A simple, low-cost method: tapping the surface with a coin or small hammer and
    listening to the sound.
    \item A solid, well-bonded structure produces a sharp, consistent tone.
    \item A dull or hollow-sounding response suggests a disbond or delamination beneath
    the surface at that location.
    \end{itemize}"""),
   ("Composite Inspection Methods: Ultrasonic C-Scan",
    r"""\begin{itemize}
    \item Sends ultrasonic pulses into the composite and maps reflections across the
    entire scanned area, similar in principle to ultrasonic metal inspection (Meeting 10).
    \item Produces a detailed image showing the size, shape, and depth of internal
    delamination or disbond.
    \item Used for thorough inspection during manufacturing and after a suspected
    impact event, complementing the quick tap test.
    \end{itemize}"""),
   ("Composite Repair Concept: Bonded Patch Repair",
    r"""\begin{enumerate}
    \item Damaged material is carefully removed, often by sanding to a tapered ("scarf") edge.
    \item New fiber plies are laid up over the prepared area, matching the original
    ply orientation and count.
    \item The patch is cured (often with a portable heat blanket) and then inspected
    (tap test or ultrasonic) to confirm a sound bond.
    \end{enumerate}"""),
   ("Lightning Strike Protection",
    r"""\begin{itemize}
    \item Unlike metal, composite material does not conduct electricity well, so it cannot
    safely carry a lightning strike's current on its own.
    \item Composite skins include an embedded \textbf{conductive layer} (often a fine
    copper or bronze mesh) just beneath the surface to carry strike current safely away.
    \item This protection must be inspected and maintained, since damage to the mesh
    can leave a hidden vulnerability to lightning strikes.
    \end{itemize}"""),
   ("Fire Resistance and Composite Materials (Brief)",
    r"""\begin{itemize}
    \item Composite resins must meet strict flammability, smoke, and toxicity
    certification standards, just like any other cabin or structural material.
    \item Some resin formulations and core materials (e.g.\ Nomex honeycomb) are
    specifically chosen for improved fire resistance in critical areas.
    \item Fire behavior differs from metal: composite does not melt the way aluminum
    does, but resin can burn or char under sustained high heat.
    \end{itemize}"""),
   ("Case Study: Boeing 787 Composite Fuselage",
    r"""\begin{itemize}
    \item The 787's fuselage is built from one-piece composite barrel sections, cured
    in a large autoclave, rather than assembled from many riveted aluminum panels.
    \item This construction eliminates thousands of rivet holes (each a potential
    fatigue-stress concentration, Meeting 6) compared to a riveted aluminum fuselage.
    \item The resulting weight saving directly improves fuel efficiency, revisiting the
    Meeting 1 case study from a manufacturing perspective.
    \end{itemize}"""),
   ("Case Study: Airbus A350 Composite Wing",
    r"""\begin{itemize}
    \item The A350 uses a composite wing skin and spar structure, one of the first
    wide-body airliners to do so.
    \item Composite wings can be designed with a natural flexibility (aeroelastic tailoring)
    that improves aerodynamic efficiency across the flight envelope.
    \item As with the 787 fuselage, the wing benefits from both weight saving and
    excellent fatigue resistance over the aircraft's service life.
    \end{itemize}"""),
   (r"Comparison: Where Composites Are Used vs.\ Where Metal Remains",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Often Composite & Often Still Metal\\\hline
    Fuselage skin (newest designs), wing skin & Landing gear, engine pylons\\
    Control surfaces, fairings, radomes & Wing leading edge (erosion/impact areas)\\\hline
    \end{tabular}\end{center}
    Most modern airliners are hybrid airframes, using each material where its strengths
    matter most -- not one material throughout."""),
   ("Applied Scenario: Identifying Likely Delamination Damage",
    r"""A composite wing panel was struck by a service vehicle, leaving only a faint mark. Work through the response:
    \begin{enumerate}
    \item Recognize this as a classic BVID risk -- the surface mark may hide significant
    internal damage.
    \item A tap test is performed first as a quick screening check across the impact area.
    \item An ultrasonic C-scan follows to fully map any delamination before the aircraft
    is returned to service.
    \end{enumerate}"""),
   (r"Applied Scenario: Choosing Composite vs.\ Metal for a New Panel",
    r"""A new access panel needs to be designed. Work through the choice:
    \begin{enumerate}
    \item If weight saving and corrosion immunity matter most, and impact risk is low,
    composite is attractive.
    \item If the panel is in a high-impact-risk zone (e.g.\ near ground service equipment),
    metal's damage visibility may be preferred despite the weight penalty.
    \item If repair infrastructure at the operator's home base only supports metal repair,
    that practical constraint may decide the choice regardless of material properties.
    \end{enumerate}"""),
   ("In-Class Practice",
    r"""\begin{enumerate}
    \item Explain the difference between the fiber and the matrix in a composite material.
    \item Compare delamination and disbond.
    \item Explain why lightning strike protection is needed on composite skin but not on metal skin.
    \end{enumerate}"""),
   ("Extended In-Class Practice / Group Discussion",
    r"""In small groups, discuss and be ready to present:
    \begin{enumerate}
    \item Debate: is BVID a bigger inspection challenge than metal fatigue cracking? Justify your answer.
    \item Explain, using the 787 and A350 case studies, two different structural benefits
    of composite material.
    \item Sketch a honeycomb sandwich panel cross-section and label the face-sheets and core.
    \end{enumerate}""")],
  I("Composites combine strong fibers with a resin matrix, offering excellent strength-to-weight and fatigue resistance.",
    "Composite damage (delamination, disbond, BVID) is often less visible than metal damage and requires NDT such as tap testing or ultrasonic C-scan.",
    "Modern airliners are hybrid airframes, using composite and metal where each material's strengths matter most."),
  I("Compare CFRP and GFRP by strength, cost, and typical use.",
    "Explain the purpose of a honeycomb sandwich structure.",
    "Explain why BVID is a greater inspection challenge than typical metal impact damage.",
    "Describe why composite skins need embedded lightning strike protection."))

M[12] = ("Landing Gear System",
  "Students are able to explain the components and working principles of the landing gear system.",
  I("Explain the functions and configurations of the landing gear system.",
    "Explain the components and function of the shock strut, brakes, and steering system.",
    "Explain the landing gear retraction and emergency extension mechanism."),
  [("Why Landing Gear Matters",
    r"""The landing gear is the only part of the aircraft normally in contact with the
    ground, absorbing the full impact of every landing.
    \begin{itemize}
    \item It supports the aircraft's entire weight on the ground and absorbs touchdown impact energy.
    \item It ties directly into the airframe load path studied in Meeting 6.
    \item This meeting covers gear configuration, shock absorption, brakes, steering,
    and retraction.
    \end{itemize}"""),
   ("Landing Gear Functions",
    r"""\begin{itemize}
    \item Supports the aircraft's weight during taxi, takeoff roll, and landing rollout.
    \item Absorbs and dissipates the impact energy of touchdown.
    \item Provides steering control on the ground.
    \item Provides braking to slow and stop the aircraft.
    \end{itemize}"""),
   (r"Landing Gear Configurations: Tricycle vs.\ Tailwheel",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Configuration & Description\\\hline
    Tricycle & Nose gear forward, two main gear aft of the CG; modern standard\\
    Tailwheel (conventional) & Two main gear forward, small tailwheel aft; older/utility aircraft\\\hline
    \end{tabular}\end{center}"""),
   ("Tricycle Gear: Advantages",
    r"""\begin{itemize}
    \item Keeps the cabin floor level on the ground, more comfortable for passengers and cargo handling.
    \item Better forward visibility for the pilot during taxi.
    \item More stable during takeoff and landing rolls, resisting the tendency to
    ground-loop (uncontrolled yaw) seen in tailwheel aircraft.
    \end{itemize}"""),
   ("Tailwheel Gear: Trade-offs",
    r"""\begin{itemize}
    \item Lighter and mechanically simpler than a nose-gear installation.
    \item Provides more propeller ground clearance, useful on rough or unpaved strips.
    \item Poorer forward visibility on the ground and less directional stability during
    the takeoff/landing roll, requiring specific pilot technique and training.
    \end{itemize}"""),
   (r"Main Gear vs.\ Nose Gear: Roles",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Gear & Role\\\hline
    Main gear & Carries most of the aircraft's weight; primary braking gear\\
    Nose gear & Carries a smaller share of weight; provides ground steering\\\hline
    \end{tabular}\end{center}
    On touchdown, the main gear normally contacts the runway first, followed by the
    nose gear as the pilot lowers the nose."""),
   ("Landing Gear Arrangement by Aircraft Size",
    r"""\begin{itemize}
    \item Light aircraft: single wheel per main gear leg, single nose or tail wheel.
    \item Narrow-body airliners: single or dual wheels per main gear leg.
    \item Wide-body/very large aircraft: multiple wheels per leg, sometimes multiple
    gear legs, to spread the much higher weight across more tire contact area.
    \end{itemize}"""),
   ("Bogie (Truck) Gear for Large Aircraft",
    r"""\begin{itemize}
    \item A \textbf{bogie} (or truck) mounts multiple wheels -- often four or six -- on a
    single gear leg in a row or grid pattern.
    \item Spreads the aircraft's weight over more tire contact area, reducing pavement
    loading at any single point (important for runway and taxiway design limits).
    \item Also provides redundancy: the aircraft can often still land safely if one
    tire on a multi-wheel bogie fails.
    \end{itemize}"""),
   ("Shock Strut: Function",
    r"""\begin{itemize}
    \item The \textbf{shock strut} is the main energy-absorbing component of the landing gear leg.
    \item Converts the kinetic energy of touchdown into heat, rather than transmitting
    the full impact directly into the airframe.
    \item Also absorbs the smaller, repeated bumps encountered during taxi over an
    uneven surface.
    \end{itemize}"""),
   ("Oleo-Pneumatic Shock Strut (Concept)",
    r"""\begin{itemize}
    \item The most common shock strut type, combining compressed \textbf{air or nitrogen}
    (a spring effect) with \textbf{hydraulic fluid} forced through a metering orifice
    (a damping effect).
    \item On impact, the strut compresses, forcing fluid through the small orifice --
    this resists the motion and dissipates energy as heat.
    \item The gas cushion then extends the strut back to its normal length after the
    impact energy has been absorbed.
    \end{itemize}"""),
   (r"Comparison: Oleo-Pneumatic vs.\ Solid Spring Gear",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Type & Characteristics\\\hline
    Oleo-pneumatic & Excellent energy absorption, more parts, used on most aircraft\\
    Solid spring (steel/composite leaf) & Simple, low maintenance, less effective damping\\\hline
    \end{tabular}\end{center}
    Solid spring gear is common on light training aircraft; oleo-pneumatic dominates
    on transport-category aircraft."""),
   ("Wheels and Tires Overview",
    r"""\begin{itemize}
    \item The \textbf{wheel} is the metal hub the tire mounts on, usually splitting into
    two halves for tire installation and removal.
    \item The \textbf{tire} cushions minor runway irregularities and provides the
    friction surface for braking and steering.
    \item Aircraft tires operate at much higher pressures than automobile tires, to
    support very high loads on a relatively small contact area.
    \end{itemize}"""),
   ("Tire Construction and Pressure (Concept)",
    r"""\begin{itemize}
    \item Aircraft tires are built from multiple reinforced rubber plies, similar in
    principle to the layered construction of a composite laminate (Meeting 11).
    \item Correct inflation pressure is critical: underinflation overheats the tire and
    risks structural failure; overinflation reduces the tire's cushioning ability.
    \item Nitrogen, not plain air, is commonly used to inflate aircraft tires, since it is
    more stable across temperature changes and reduces internal oxidation.
    \end{itemize}"""),
   ("Tire Inspection: Wear and Damage Signs",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Sign & Concern\\\hline
    Tread wear beyond limit & Reduced grip, especially on a wet runway\\
    Cuts or bulges in the sidewall & Risk of sudden tire failure\\
    Flat-spotting & Localized wear from a skid, can unbalance the wheel\\\hline
    \end{tabular}\end{center}"""),
   ("Brakes: Disc Brake System",
    r"""\begin{itemize}
    \item Most aircraft use \textbf{disc brakes} on the main gear wheels, similar in
    principle to automobile disc brakes but built for far higher heat loads.
    \item Hydraulic pressure squeezes brake pads (or a stack of rotating and stationary
    discs on larger aircraft) against a disc attached to the wheel.
    \item Braking converts the aircraft's kinetic energy into heat, which is why brakes
    can glow visibly hot after a heavy landing or rejected takeoff.
    \end{itemize}"""),
   ("Anti-Skid Braking System (Concept)",
    r"""\begin{itemize}
    \item Monitors each wheel's rotation speed and automatically reduces brake pressure
    on a wheel that is about to skid (stop rotating while the aircraft still moves).
    \item A skidding tire provides far less braking friction than a rotating tire at the
    edge of skidding, so anti-skid maximizes stopping performance.
    \item Conceptually similar to an automobile anti-lock braking system (ABS), applied
    to each main gear wheel independently.
    \end{itemize}"""),
   ("Autobrake System (Brief)",
    r"""\begin{itemize}
    \item Allows the crew to pre-select a braking deceleration level before landing or
    a rejected takeoff.
    \item Applies brakes automatically at the selected rate once the aircraft is on the
    ground, without the pilot manually pressing the brake pedals.
    \item Frees the crew to focus on directional control and other tasks during a busy,
    high-workload phase of flight.
    \end{itemize}"""),
   ("Steering System (Nosewheel Steering)",
    r"""\begin{itemize}
    \item Most aircraft steer on the ground by turning the nosewheel, controlled by a
    tiller (small wheel/handle) at low speed and by rudder pedals at higher speed.
    \item Hydraulically actuated on larger aircraft, allowing tight turns for gate
    maneuvering despite the nosewheel's limited turn angle at speed.
    \item Differential braking (more brake on one main gear than the other) can provide
    additional steering assistance, especially on aircraft without nosewheel steering.
    \end{itemize}"""),
   ("Landing Gear Retraction System (Concept)",
    r"""\begin{itemize}
    \item After takeoff, hydraulic actuators retract the gear into the wing or fuselage
    to reduce drag during flight.
    \item The retraction sequence is carefully timed: gear doors, gear legs, and locking
    mechanisms must move in the correct order to avoid interference.
    \item Both the extended (down) and retracted (up) positions are held by mechanical
    locks, not just hydraulic pressure, for safety if hydraulic power is lost.
    \end{itemize}"""),
   ("Gear Doors and Sequencing",
    r"""\begin{itemize}
    \item \textbf{Gear doors} close over the wheel well after retraction, restoring a
    smooth aerodynamic surface and reducing drag.
    \item Some doors open only briefly during retraction/extension; others remain open
    whenever the gear is down.
    \item Correct door sequencing is essential -- a door that fails to open or close on
    time can jam the gear leg itself.
    \end{itemize}"""),
   ("Landing Gear Position Indication System",
    r"""\begin{itemize}
    \item Cockpit indicators show each gear leg's position, typically as three lights
    (or symbols): green for down-and-locked, red for in transit or disagreement, and
    unlit for safely retracted and locked.
    \item Position sensors on each gear leg feed this indication system, letting the
    crew confirm gear status before landing.
    \item A mismatch between commanded and actual gear position is treated as a serious
    caution requiring troubleshooting before landing.
    \end{itemize}"""),
   (r"Emergency Extension System (Concept)",
    r"""\begin{itemize}
    \item If normal hydraulic retraction/extension fails, an \textbf{emergency (alternate)
    extension} system releases the gear's uplocks.
    \item On many aircraft, gravity and airflow alone then swing the gear down into the
    locked position once released -- often called a "free-fall" extension.
    \item This system is deliberately simple and independent of the normal hydraulic
    system, since it exists specifically for when that system has failed.
    \end{itemize}"""),
   ("Landing Gear Attachment to Airframe",
    r"""\begin{itemize}
    \item The gear leg attaches to a heavily reinforced fitting on the wing spar or a
    fuselage frame, following the same load-path logic introduced in Meeting 6.
    \item This attachment must react both the vertical touchdown load and side/drag
    loads from braking and turning.
    \item Because of these high, repeated loads, gear attachment points are among the
    most closely inspected structural areas on the aircraft.
    \end{itemize}"""),
   ("Landing Gear Loads: Touchdown, Taxi, Braking",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Load Source & Description\\\hline
    Touchdown impact & Large, brief vertical load absorbed by the shock strut\\
    Taxi & Smaller, repeated loads from surface irregularities\\
    Braking & Drag (aft) load reacted through the gear attachment\\\hline
    \end{tabular}\end{center}
    Like the wing loads in Meeting 6, real landing gear loads are combinations of
    several of these acting together."""),
   ("Landing Gear Retraction Failure: Contingency Procedures (Concept)",
    r"""\begin{itemize}
    \item If a gear leg fails to indicate down-and-locked, crews follow a checklist
    that may include recycling the gear, using the emergency extension system, or
    performing a low flyby for visual confirmation from the ground.
    \item If a gear genuinely cannot be extended, crews prepare for a gear-up or
    partial-gear landing following specific emergency procedures.
    \item These procedures exist precisely because the gear is a single point of
    ground contact with no backup path if it truly fails to extend.
    \end{itemize}"""),
   ("Case Study: Gear-Up Landing Incident",
    r"""\begin{itemize}
    \item Gear-up landings have occurred historically from a combination of pilot
    distraction and, in some cases, a genuine gear system malfunction.
    \item Investigations of these events reinforced the importance of the gear position
    indication system and standardized before-landing checklists.
    \item Most gear-up landings, while causing airframe damage, have historically
    resulted in few or no serious injuries, thanks to controlled, low-speed touchdowns.
    \end{itemize}"""),
   ("Case Study: Nose Gear Collapse from Fatigue/Maintenance Error",
    r"""\begin{itemize}
    \item Several historical nose gear collapse events have been traced to fatigue
    cracking in the gear leg or a maintenance error during a previous overhaul.
    \item These events reinforced strict overhaul intervals and inspection requirements
    specific to landing gear components, separate from the general airframe program.
    \item The lesson connects directly back to Meeting 6: even a component designed
    with fail-safe principles depends on inspections actually being performed correctly.
    \end{itemize}"""),
   (r"Comparison: Fixed vs.\ Retractable Landing Gear",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Type & Trade-off\\\hline
    Fixed gear & Simpler, lighter mechanism, but constant aerodynamic drag\\
    Retractable gear & Lower cruise drag, but heavier and mechanically more complex\\\hline
    \end{tabular}\end{center}
    Fixed gear remains common on light trainers and utility aircraft, where simplicity
    outweighs the drag penalty; retractable gear dominates faster and larger aircraft."""),
   ("Applied Scenario: Diagnosing a Flat Nose Tire Before Departure",
    r"""During a pre-flight walkaround, a technician notices a nose tire looks underinflated. Work through the response:
    \begin{enumerate}
    \item Compare the tire's appearance and pressure reading against the aircraft's
    specified inflation pressure.
    \item Inspect the tire and wheel for cuts, bulges, or other visible damage that
    might explain the pressure loss.
    \item If the tire is confirmed underinflated or damaged, it must be serviced or
    replaced before the aircraft is released for flight.
    \end{enumerate}"""),
   ("Applied Scenario: Responding to a Gear Disagreement Indication",
    r"""On approach, the right main gear shows a red (in-transit/disagreement) indication instead of green. Work through the response:
    \begin{enumerate}
    \item The crew recycles the gear (retract and re-extend) following the checklist,
    since a sensor or door sequencing issue is a common cause.
    \item If the disagreement persists, the crew may attempt a low flyby past the tower
    or use another means to visually confirm gear position.
    \item If the gear still cannot be confirmed down-and-locked, the crew prepares for a
    precautionary landing following the gear-malfunction procedure.
    \end{enumerate}"""),
   ("In-Class Practice",
    r"""\begin{enumerate}
    \item Compare tricycle and tailwheel landing gear configurations.
    \item Explain how an oleo-pneumatic shock strut absorbs landing impact energy.
    \item Explain the purpose of an anti-skid braking system.
    \end{enumerate}"""),
   ("Extended In-Class Practice / Group Discussion",
    r"""In small groups, discuss and be ready to present:
    \begin{enumerate}
    \item Debate: for a bush plane operating from unpaved strips, would you choose
    tricycle or tailwheel gear? Justify your answer.
    \item Explain, step by step, how an emergency (free-fall) extension differs from
    normal hydraulic gear extension.
    \item Sketch a landing gear leg and label the shock strut, wheel/tire, and
    airframe attachment point.
    \end{enumerate}""")],
  I("Landing gear supports the aircraft's weight, absorbs touchdown impact, and provides steering and braking.",
    "Oleo-pneumatic shock struts combine gas-spring and hydraulic-damping action to absorb landing energy.",
    "Retraction, indication, and emergency extension systems together ensure the gear can be reliably confirmed down and locked before landing."),
  I("Compare tricycle and tailwheel landing gear configurations.",
    "Explain how an oleo-pneumatic shock strut absorbs impact energy.",
    "Explain the purpose of an anti-skid braking system.",
    "Describe how an emergency (free-fall) gear extension system works."))

M[13] = ("Powerplant System Overview",
  "Students are able to explain the working principles of piston and turbine aircraft engines and the general operation of fuel, hydraulic, and pneumatic systems.",
  I("Explain the working principle of the piston (reciprocating) engine.",
    "Explain the working principle of the gas turbine engine.",
    "Compare piston and turbine engines by application and efficiency."),
  [("Why Powerplant Understanding Matters",
    r"""Meeting 1 classified aircraft by powerplant type; this meeting explains how those
    powerplants actually work.
    \begin{itemize}
    \item Every aircraft needs a powerplant to generate thrust or shaft power for flight.
    \item Piston and turbine engines work on different principles, suited to different
    missions.
    \item This meeting builds the foundation for Meeting 14's fuel, hydraulic, and
    pneumatic systems, which all support the powerplant.
    \end{itemize}"""),
   ("Powerplant Types Recap",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Type & Typical Use (Meeting 1)\\\hline
    Piston (reciprocating) & Light general-aviation aircraft, trainers\\
    Turboprop & Regional airliners, cargo, military transports\\
    Turbojet & Early jet airliners, some military fighters\\
    Turbofan & Modern airliners and business jets\\\hline
    \end{tabular}\end{center}
    Piston engines and gas turbines are the two fundamentally different working
    principles behind all four types."""),
   ("Piston Engine: Basic Principle",
    r"""\begin{itemize}
    \item A piston engine converts the pressure of burning fuel-air mixture into
    reciprocating (back-and-forth) piston motion.
    \item A crankshaft converts that reciprocating motion into rotary motion, which
    turns the propeller.
    \item Most aircraft piston engines use a \textbf{four-stroke cycle}, repeating four
    distinct phases for every two crankshaft revolutions.
    \end{itemize}"""),
   ("Four-Stroke Cycle: Intake",
    r"""\begin{itemize}
    \item The piston moves downward inside the cylinder.
    \item The intake valve opens, drawing a fuel-air mixture into the cylinder.
    \item This is the first of the cycle's four strokes, setting up the charge that
    will be compressed and burned.
    \end{itemize}"""),
   ("Four-Stroke Cycle: Compression",
    r"""\begin{itemize}
    \item Both valves close, and the piston moves upward, compressing the fuel-air
    mixture into a smaller volume.
    \item Compressing the mixture before ignition significantly increases the power
    produced when it burns.
    \item Just before the piston reaches the top, a spark plug ignites the mixture,
    beginning the next stroke.
    \end{itemize}"""),
   ("Four-Stroke Cycle: Power",
    r"""\begin{itemize}
    \item The ignited fuel-air mixture burns rapidly, and the resulting high pressure
    forces the piston downward.
    \item This is the only stroke that produces usable power -- the other three strokes
    prepare for or clean up after it.
    \item The piston's downward force turns the crankshaft, which ultimately drives the propeller.
    \end{itemize}"""),
   ("Four-Stroke Cycle: Exhaust",
    r"""\begin{itemize}
    \item The exhaust valve opens, and the piston moves upward, pushing burned gases
    out of the cylinder.
    \item Once the exhaust stroke completes, the cycle immediately repeats with a
    fresh intake stroke.
    \item Each cylinder in a multi-cylinder engine is at a different stage of this
    cycle at any instant, smoothing out the engine's overall power delivery.
    \end{itemize}"""),
   ("Piston Engine Components: Cylinder, Piston, Crankshaft",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Component & Function\\\hline
    Cylinder & Chamber where combustion occurs and the piston moves\\
    Piston & Transmits combustion pressure into mechanical motion\\
    Crankshaft & Converts piston's reciprocating motion into rotary motion\\\hline
    \end{tabular}\end{center}"""),
   ("Piston Engine Components: Valves and Camshaft",
    r"""\begin{itemize}
    \item \textbf{Intake and exhaust valves} open and close to let the fuel-air mixture
    in and burned gases out, at precisely timed moments in the cycle.
    \item A \textbf{camshaft}, driven by the crankshaft, opens and closes the valves
    at the correct point in each cylinder's cycle.
    \item Correct valve timing is essential -- valves opening at the wrong moment would
    waste power or damage the engine.
    \end{itemize}"""),
   (r"Piston Engine Cooling: Air-Cooled vs.\ Liquid-Cooled",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Method & Characteristics\\\hline
    Air-cooled & Cooling fins and airflow remove heat; simpler, lighter, most common in GA\\
    Liquid-cooled & Coolant circulates heat away; more even cooling, added weight/complexity\\\hline
    \end{tabular}\end{center}
    Most light aircraft piston engines are air-cooled, relying on airflow from the
    propeller and forward motion to keep cylinder temperatures in range."""),
   ("Piston Engine Ignition System (Magneto Concept)",
    r"""\begin{itemize}
    \item Most aircraft piston engines use \textbf{magnetos} -- self-contained,
    engine-driven generators that produce spark plug ignition voltage.
    \item Because magnetos generate their own electricity, ignition continues even if
    the aircraft's electrical system fails.
    \item Aircraft engines typically have two independent magneto/ignition systems per
    engine, so a single failure does not stop the engine -- a fail-safe concept echoing
    Meeting 6.
    \end{itemize}"""),
   (r"Propeller Basics: Fixed-Pitch vs.\ Constant-Speed",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Type & Description\\\hline
    Fixed-pitch & Blade angle cannot change; simple, common on trainers\\
    Constant-speed & Blade angle adjusts automatically to maintain a set engine RPM\\\hline
    \end{tabular}\end{center}
    A constant-speed propeller lets the pilot select an efficient engine RPM across a
    wide range of airspeeds and power settings, unlike a fixed-pitch design."""),
   ("Turbine Engine: Basic Principle",
    r"""\begin{itemize}
    \item A gas turbine engine continuously draws in air, compresses it, burns fuel in
    it, and expels hot high-velocity exhaust -- unlike the piston engine's stop-start cycle.
    \item Often summarized informally as ``suck, squeeze, bang, blow'': intake,
    compression, combustion, exhaust.
    \item This continuous-flow process allows gas turbines to produce far more power for
    their weight than a piston engine of similar size.
    \end{itemize}"""),
   ("Turbine Engine Sections",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Section & Function\\\hline
    Intake & Directs smooth airflow into the compressor\\
    Compressor & Compresses incoming air to high pressure\\
    Combustor & Fuel is injected and burned in the compressed air\\
    Turbine & Extracts energy from hot gas to drive the compressor\\
    Exhaust & Expels remaining high-velocity gas, producing thrust\\\hline
    \end{tabular}\end{center}"""),
   (r"Compressor Types: Axial vs.\ Centrifugal",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Type & Description\\\hline
    Axial & Air flows straight through multiple rotating/stationary blade stages\\
    Centrifugal & Air is flung outward by a rotating disc, then redirected rearward\\\hline
    \end{tabular}\end{center}
    Large modern turbofans use axial compressors for high airflow; some smaller
    turboprops and turboshafts use centrifugal stages for their compact size."""),
   ("Combustor (Combustion Chamber) Function",
    r"""\begin{itemize}
    \item Fuel is continuously sprayed into the compressed air and ignited, burning
    steadily rather than in the piston engine's separate power strokes.
    \item Combustor design must mix fuel and air thoroughly for efficient, stable
    combustion across a wide range of power settings.
    \item The resulting very hot, high-pressure gas flows directly into the turbine section.
    \end{itemize}"""),
   ("Turbine Section Function",
    r"""\begin{itemize}
    \item Hot gas from the combustor flows over the turbine blades, spinning the turbine.
    \item The turbine is connected by a shaft to the compressor at the front of the
    engine, providing the power to keep compressing incoming air.
    \item On a turboprop or turboshaft, an additional turbine stage extracts extra
    power to drive the propeller or rotor, rather than expelling it all as jet exhaust.
    \end{itemize}"""),
   (r"Turbojet vs.\ Turbofan Comparison",
    r"""\begin{center}\begin{tabular}{l|l|l}\hline
    Aspect & Turbojet & Turbofan\\\hline
    Airflow path & All air through the engine core & Most air bypasses the core (fan)\\
    Bypass ratio & None/very low & High (most modern airliners)\\
    Fuel efficiency & Lower & Higher\\
    Noise & Louder & Quieter\\\hline
    \end{tabular}\end{center}"""),
   ("Turboprop Engine (Concept)",
    r"""\begin{itemize}
    \item A gas turbine core drives a propeller through a reduction gearbox, rather
    than producing thrust mainly from jet exhaust.
    \item The reduction gearbox slows the turbine's high rotational speed down to a
    speed suitable for an efficient propeller.
    \item Efficient at the lower speeds and altitudes typical of regional and cargo
    operations, where a pure jet would be less efficient.
    \end{itemize}"""),
   ("Turboshaft Engine (Brief)",
    r"""\begin{itemize}
    \item Similar to a turboprop, but the turbine's output shaft drives a helicopter
    rotor system instead of a propeller.
    \item Produces shaft power rather than significant direct jet thrust, matching a
    helicopter's need for rotor power rather than forward thrust.
    \item Otherwise shares the same intake-compressor-combustor-turbine architecture
    as other gas turbine types.
    \end{itemize}"""),
   (r"Comparison: Piston vs.\ Turbine Engines",
    r"""\begin{center}\begin{tabular}{l|l|l}\hline
    Aspect & Piston & Turbine\\\hline
    Power-to-weight & Lower & Much higher\\
    Complexity & Mechanically simpler & More complex, precision-built\\
    Typical use & Light GA aircraft, trainers & Airliners, business jets, military\\
    Fuel & Avgas (typically) & Jet fuel (kerosene-based)\\\hline
    \end{tabular}\end{center}"""),
   ("Engine Instruments: What Pilots Monitor (Brief)",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Instrument & Monitors\\\hline
    RPM / N1--N2 & Engine rotational speed\\
    EGT (exhaust gas temperature) & Combustion/exhaust temperature health\\
    Oil pressure and temperature & Lubrication system health\\\hline
    \end{tabular}\end{center}
    These instruments let the crew detect a developing engine problem before it
    becomes a failure."""),
   ("FADEC (Full Authority Digital Engine Control)",
    r"""\begin{itemize}
    \item A \textbf{FADEC} is a computer that automatically manages fuel flow and
    engine parameters, replacing older manual/mechanical engine controls.
    \item Continuously optimizes engine performance and protects against exceeding
    safe operating limits (such as overspeed or overtemperature).
    \item Most modern turbine engines use FADEC, similar in spirit to the fly-by-wire
    flight control computers introduced in Meeting 4.
    \end{itemize}"""),
   ("Engine Starting System (Concept)",
    r"""\begin{itemize}
    \item Turbine engines need an external or auxiliary power source to begin rotating
    the compressor before the engine can sustain itself.
    \item Common starting methods include an electric starter motor or high-pressure
    air from an auxiliary power unit (APU) or ground cart.
    \item Once the engine reaches a self-sustaining speed, fuel ignition takes over and
    the starter disengages.
    \end{itemize}"""),
   (r"Engine Thrust vs.\ Power (Concept Distinction)",
    r"""\begin{itemize}
    \item \textbf{Thrust} is a direct forward force, the natural output of a turbojet
    or turbofan's exhaust.
    \item \textbf{Power} (shaft horsepower) is rotational output, the natural output of
    a piston engine or a turboprop/turboshaft's turbine.
    \item Propeller-driven aircraft convert engine power into thrust through the
    propeller; pure jets produce thrust directly from exhaust velocity.
    \end{itemize}"""),
   ("Case Study: Why Turbofans Replaced Turbojets",
    r"""\begin{itemize}
    \item Early jet airliners used turbojets, which were loud and fuel-thirsty compared
    to today's engines.
    \item Turbofans bypass a large volume of air around the engine core, producing
    thrust more efficiently and far more quietly.
    \item This single design change is a major reason modern airliners are both
    quieter and more fuel-efficient than their 1960s counterparts.
    \end{itemize}"""),
   ("Case Study: Piston Engines Still Used in General Aviation",
    r"""\begin{itemize}
    \item Despite turbine engines' power advantage, piston engines remain standard for
    most trainers and small GA aircraft.
    \item Lower purchase price, simpler maintenance, and lower fuel cost per hour suit
    the light, low-speed missions these aircraft fly.
    \item This is the same "right tool for the mission" logic seen in Meeting 1's
    aircraft classification and Meeting 10--11's material selection discussions.
    \end{itemize}"""),
   ("Comparison: Bypass Ratio and Fuel Efficiency",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Bypass Ratio & Typical Characteristic\\\hline
    Low (turbojet, early turbofan) & Louder, less fuel-efficient, higher top speed\\
    High (modern turbofan) & Quieter, more fuel-efficient, common on airliners today\\\hline
    \end{tabular}\end{center}
    Bypass ratio compares the air that bypasses the engine core to the air that
    passes through it -- higher ratios generally mean better fuel efficiency."""),
   ("Applied Scenario: Identifying Engine Type from Sound/Silhouette",
    r"""Standing near a ramp, you hear and see an unfamiliar aircraft's engine. Work through the identification:
    \begin{enumerate}
    \item A visible propeller with a piston or turboprop-shaped nacelle suggests a
    propeller-driven aircraft.
    \item A large-diameter nacelle with no visible propeller suggests a high-bypass turbofan.
    \item A narrower, straight-through nacelle with a louder, higher-pitched sound
    suggests an older turbojet or low-bypass design.
    \end{enumerate}"""),
   ("Applied Scenario: Diagnosing a High EGT Reading",
    r"""During engine run-up, the exhaust gas temperature reads higher than normal for the power setting. Work through the response:
    \begin{enumerate}
    \item Recognize this as a potential sign of a combustion or fuel-scheduling issue.
    \item Cross-check other engine instruments (RPM, oil pressure/temperature) for
    consistency with a genuine problem versus a possible sensor fault.
    \item Follow the checklist for high EGT, which may include reducing power or
    aborting the flight, rather than continuing without investigation.
    \end{enumerate}"""),
   ("In-Class Practice",
    r"""\begin{enumerate}
    \item List the four strokes of a piston engine cycle in order.
    \item List the five main sections of a gas turbine engine in order.
    \item Explain the difference between a turbojet and a turbofan.
    \end{enumerate}"""),
   ("Extended In-Class Practice / Group Discussion",
    r"""In small groups, discuss and be ready to present:
    \begin{enumerate}
    \item Debate: for a new regional cargo aircraft, would you choose a turboprop or a
    turbofan? Justify using efficiency, speed, and mission profile.
    \item Explain, using the ``suck, squeeze, bang, blow'' summary, how a turbine
    engine's continuous cycle differs from a piston engine's four-stroke cycle.
    \item Sketch a turbofan engine cross-section and label the fan, compressor,
    combustor, and turbine.
    \end{enumerate}""")],
  I("Piston engines use a four-stroke cycle to convert combustion pressure into propeller-turning rotary motion.",
    "Gas turbine engines continuously compress, burn, and expand air through intake, compressor, combustor, turbine, and exhaust sections.",
    "Turbojet, turbofan, turboprop, and turboshaft are all gas turbine variants, distinguished by how they use their turbine's output."),
  I("List and explain the four strokes of a piston engine cycle.",
    "List the five main sections of a gas turbine engine in order.",
    "Compare turbojet and turbofan engines by bypass ratio, efficiency, and noise.",
    "Explain the difference between engine thrust and engine power."))

M[14] = ("Fuel, Hydraulic \\& Pneumatic Systems",
  "Students are able to explain the working principles of piston and turbine aircraft engines and the general operation of fuel, hydraulic, and pneumatic systems.",
  I("Explain the general function and components of the aircraft fuel system.",
    "Explain the general function and components of the aircraft hydraulic system.",
    "Explain the general function and components of the aircraft pneumatic system."),
  [("Why These Systems Matter",
    r"""Meeting 13 explained how the powerplant produces thrust and power; this meeting
    covers the three systems that support and complement it.
    \begin{itemize}
    \item The \textbf{fuel system} stores and delivers fuel to the engines.
    \item The \textbf{hydraulic system} powers flight controls, landing gear, and brakes.
    \item The \textbf{pneumatic system} uses compressed air for engine start, anti-ice,
    and cabin air supply.
    \end{itemize}"""),
   ("Fuel System: Function Overview",
    r"""\begin{itemize}
    \item Stores fuel safely and delivers it to each engine at the correct pressure
    and flow rate, under all flight conditions.
    \item Manages fuel distribution between tanks to keep the aircraft in balance.
    \item Provides the flight crew with accurate fuel quantity information for
    planning and monitoring.
    \end{itemize}"""),
   ("Fuel Storage: Wing Tanks Recap",
    r"""\begin{itemize}
    \item Meeting 2 introduced integral (wet wing) and bladder fuel tanks within the wing structure.
    \item Most transport aircraft store the majority of their fuel in the wings, with
    some designs adding a center tank in the fuselage for extra range.
    \item Storing fuel in the wings also has a structural benefit: fuel weight in the
    wing partially offsets the wing's own lift-bending load in flight.
    \end{itemize}"""),
   ("Fuel System Components: Pumps, Valves, Lines",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Component & Function\\\hline
    Fuel pump & Moves fuel from tank to engine at the required pressure\\
    Shutoff valve & Stops fuel flow, e.g.\ during an engine fire emergency\\
    Fuel lines & Route fuel from tanks, through pumps and valves, to the engines\\\hline
    \end{tabular}\end{center}"""),
   ("Fuel Quantity Indication System (Concept)",
    r"""\begin{itemize}
    \item Sensors in each tank measure fuel quantity, typically using capacitance
    probes that respond to the fuel level.
    \item The system displays total fuel and often per-tank quantity in the cockpit,
    letting the crew monitor consumption and range.
    \item Accurate indication is safety-critical -- fuel planning and in-flight
    decisions depend directly on this system's accuracy.
    \end{itemize}"""),
   ("Fuel Crossfeed System (Concept)",
    r"""\begin{itemize}
    \item Allows fuel from one tank (or side of the aircraft) to feed an engine on the
    other side.
    \item Used to correct a fuel imbalance between tanks or to continue feeding an
    engine if its normal tank's pump has failed.
    \item Normally kept off during regular operations and selected on deliberately by
    the crew when needed.
    \end{itemize}"""),
   ("Fuel Jettison System (Brief)",
    r"""\begin{itemize}
    \item Some larger aircraft can dump fuel in flight through dedicated jettison valves,
    usually near the wingtips.
    \item Used to quickly reduce aircraft weight down to the maximum landing weight
    during an emergency requiring an immediate return to land.
    \item Not fitted on smaller aircraft, where landing weight and maximum takeoff
    weight are close enough that jettisoning is unnecessary.
    \end{itemize}"""),
   (r"Fuel Types: Avgas vs.\ Jet Fuel",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Fuel Type & Used By\\\hline
    Avgas (aviation gasoline) & Piston engines\\
    Jet fuel (kerosene-based, e.g.\ Jet A-1) & Turbine engines (turbojet, turbofan, turboprop)\\\hline
    \end{tabular}\end{center}
    Fueling the wrong aircraft with the wrong fuel type is a serious, well-documented
    hazard -- fuel nozzles and placards are deliberately designed to help prevent it."""),
   ("Fuel Contamination and Quality Control",
    r"""\begin{itemize}
    \item \textbf{Water contamination} is the most common fuel quality concern, since
    water can settle to the bottom of a tank and be drawn into the engine.
    \item Fuel sumps (tank low points) include drain valves so technicians can check
    for water or debris before every flight.
    \item Fuel filters throughout the system catch particulate contamination before it
    can reach the engine.
    \end{itemize}"""),
   ("Fuel System Icing (Concept)",
    r"""\begin{itemize}
    \item At high altitude, fuel temperature can drop low enough for any dissolved
    water to form ice crystals that block fuel filters or lines.
    \item Fuel heaters or anti-icing additives are used to prevent this blockage on
    aircraft that operate at very cold conditions.
    \item This is a different mechanism from the airframe/engine anti-ice systems
    covered elsewhere in this course, but shares the same underlying cold-weather concern.
    \end{itemize}"""),
   ("Hydraulic System: Function Overview",
    r"""\begin{itemize}
    \item Uses pressurized fluid to transmit force and power throughout the aircraft.
    \item Powers flight control actuators (Meeting 4), landing gear retraction
    (Meeting 12), wheel brakes, and spoilers (Meeting 5).
    \item Provides much higher force in a smaller, lighter package than an equivalent
    mechanical or electric system could achieve.
    \end{itemize}"""),
   ("Hydraulic System Components: Pump, Reservoir, Actuator",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Component & Function\\\hline
    Reservoir & Stores hydraulic fluid, allows for expansion/contraction\\
    Pump & Pressurizes fluid, usually driven by the engine or an electric motor\\
    Actuator & Converts hydraulic pressure into mechanical motion at the end system\\\hline
    \end{tabular}\end{center}"""),
   ("Hydraulic Fluid Properties (Concept)",
    r"""\begin{itemize}
    \item Hydraulic fluid is essentially \textbf{incompressible} -- pushing on one end
    of a closed fluid system moves the other end almost instantly.
    \item This property is what lets a small pilot input produce a large, precise, and
    immediate movement at a flight control surface or gear actuator.
    \item Fluid must also resist temperature extremes and remain stable over long
    service intervals, since contaminated or degraded fluid can damage the whole system.
    \end{itemize}"""),
   ("Hydraulic System Pressure and Power (Concept)",
    r"""\begin{itemize}
    \item Hydraulic systems operate at very high pressure, allowing a compact actuator
    to produce a large force.
    \item This is the same basic principle as a hydraulic car jack, scaled up and made
    far more precise and continuously powered.
    \item High pressure also means hydraulic leaks and maintenance require strict
    safety procedures, since escaping fluid can be hazardous.
    \end{itemize}"""),
   ("Multiple Hydraulic Systems (Redundancy Concept)",
    r"""\begin{itemize}
    \item Transport aircraft typically have two or three independent hydraulic systems,
    each capable of powering critical functions on its own.
    \item This mirrors the flight control redundancy concept introduced in Meeting 4 --
    a single hydraulic system failure should not disable primary flight controls.
    \item Each system usually has its own pump, reservoir, and set of lines, physically
    separated where practical to reduce the chance of a single event disabling all of them.
    \end{itemize}"""),
   ("Hydraulic System Applications on Aircraft",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Application & Meeting Reference\\\hline
    Flight control actuation & Meeting 4 (fly-by-wire/hydraulic controls)\\
    Landing gear retraction & Meeting 12\\
    Wheel brakes & Meeting 12\\
    Spoilers/speedbrakes & Meeting 5\\\hline
    \end{tabular}\end{center}
    The hydraulic system is a common thread running through nearly every mechanical
    system covered so far in this course."""),
   ("Hydraulic Actuators (Concept)",
    r"""\begin{itemize}
    \item An \textbf{actuator} converts hydraulic pressure into linear or rotary
    mechanical motion at the point where work is actually done.
    \item A simple linear actuator is essentially a piston inside a cylinder, pushed by
    pressurized fluid on one or both sides.
    \item The actuator is the final link between the hydraulic system's stored energy
    and the physical motion of a flight control surface, gear leg, or brake.
    \end{itemize}"""),
   (r"Comparison: Hydraulic vs.\ Electric Actuation",
    r"""\begin{center}\begin{tabular}{l|l|l}\hline
    Aspect & Hydraulic & Electric\\\hline
    Force for given size & Very high & Lower for comparable size\\
    Typical use & Primary flight controls, gear, brakes & Smaller/secondary systems, newer designs\\
    Trend & Long-established & Growing (``more electric aircraft'')\\\hline
    \end{tabular}\end{center}"""),
   ("Pneumatic System: Function Overview",
    r"""\begin{itemize}
    \item Uses compressed air, rather than fluid, to perform work and supply other systems.
    \item On most turbine aircraft, this air is drawn from the engine compressor
    (Meeting 13) as \textbf{bleed air}.
    \item Provides air for engine starting, anti-ice, and cabin environmental systems.
    \end{itemize}"""),
   ("Bleed Air System (Concept)",
    r"""\begin{itemize}
    \item \textbf{Bleed air} is hot, high-pressure air tapped from a stage of the
    engine's compressor section before it reaches the combustor.
    \item This air is cooled and regulated as needed before being distributed to the
    systems that use it.
    \item Because it is diverted from the engine, excessive bleed air demand can
    slightly reduce available engine thrust -- a trade-off engineers account for in design.
    \end{itemize}"""),
   ("Pneumatic System Applications",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Application & Description\\\hline
    Anti-ice & Hot bleed air heats the wing/nacelle leading edges (Meeting 2/3 topics)\\
    Engine starting & High-pressure air spins the engine to a self-sustaining speed\\
    Cabin air supply & Bleed air is conditioned and supplied to the cabin\\\hline
    \end{tabular}\end{center}"""),
   ("Environmental Control System (ECS) Overview",
    r"""\begin{itemize}
    \item The \textbf{environmental control system} conditions bleed (or electrically
    compressed) air for cabin temperature, pressurization, and ventilation.
    \item Ties directly to Meeting 2's cabin pressurization topic -- the ECS is the
    system that actually pressurizes and conditions the air inside the fuselage.
    \item Must balance passenger comfort, air quality, and the pneumatic system's
    available capacity across all phases of flight.
    \end{itemize}"""),
   ("APU (Auxiliary Power Unit) Overview",
    r"""\begin{itemize}
    \item A small turbine engine, usually mounted in the tail cone, that provides
    electrical power and compressed air while the main engines are shut down.
    \item Lets the aircraft run cabin air conditioning, lighting, and systems at the
    gate without needing external ground power or air carts.
    \item Also commonly used to provide the compressed air needed to start the main
    engines, tying the pneumatic and powerplant-start topics together.
    \end{itemize}"""),
   (r"Comparison: Hydraulic vs.\ Pneumatic Systems",
    r"""\begin{center}\begin{tabular}{l|l|l}\hline
    Aspect & Hydraulic & Pneumatic\\\hline
    Working medium & Incompressible fluid & Compressible air\\
    Force/precision & High force, very precise & Lower precision, good for heating/flow\\
    Typical use & Flight controls, gear, brakes & Anti-ice, engine start, cabin air\\\hline
    \end{tabular}\end{center}"""),
   ("System Interdependency: How These Systems Connect",
    r"""\begin{itemize}
    \item The fuel system feeds the engine; the engine drives hydraulic pumps and
    supplies pneumatic bleed air.
    \item If an engine fails, both its dedicated hydraulic pump and its bleed air
    source are typically lost, which is why redundancy (multiple engines, multiple
    hydraulic systems, the APU) exists throughout the aircraft.
    \item Recognizing these dependencies helps explain why a single engine failure can
    affect several seemingly unrelated systems at once.
    \end{itemize}"""),
   ("Case Study: Fuel Exhaustion Incident",
    r"""\begin{itemize}
    \item Historical fuel exhaustion incidents have occurred from a combination of fuel
    quantity calculation errors and fuel gauge/indication problems.
    \item In one well-known case, a jet airliner ran out of fuel mid-flight due to a
    unit-conversion error during fueling, and was forced to glide to a safe landing.
    \item These events reinforced strict cross-checking procedures for fuel loading
    and indication, especially during unit or system changes.
    \end{itemize}"""),
   ("Case Study: Hydraulic System Failure and Redundancy",
    r"""\begin{itemize}
    \item Some historical incidents involving the loss of multiple hydraulic systems
    forced crews to control the aircraft using only differential engine thrust.
    \item These extreme cases demonstrated both the criticality of hydraulic redundancy
    and the value of separating hydraulic system routing to reduce common failure points.
    \item As a direct result, hydraulic system separation and redundancy requirements
    were strengthened across the industry.
    \end{itemize}"""),
   ("Applied Scenario: Diagnosing Low Hydraulic Pressure",
    r"""A cockpit indication shows low pressure in one of three hydraulic systems. Work through the response:
    \begin{enumerate}
    \item Confirm which systems remain fully pressurized and which aircraft functions
    they still support.
    \item Follow the checklist, which may isolate the affected system to prevent
    further fluid loss.
    \item Recognize that remaining systems, by design, still provide the critical
    functions (flight controls, gear, brakes) needed to complete the flight safely.
    \end{enumerate}"""),
   ("Applied Scenario: Fuel Imbalance Between Tanks",
    r"""The cockpit fuel indication shows significantly more fuel in the left tank than the right. Work through the response:
    \begin{enumerate}
    \item Confirm the imbalance is real (not a sensor fault) by cross-checking with
    other indications.
    \item Consider selecting fuel crossfeed to correct the imbalance, as covered
    earlier this meeting.
    \item Monitor the imbalance against operating limits, since an uncorrected
    imbalance can eventually affect aircraft handling.
    \end{enumerate}"""),
   ("Common Misconceptions About These Systems",
    r"""\begin{itemize}
    \item \textbf{Myth:} hydraulic fluid is compressible like air. \textbf{Fact:} it is
    treated as incompressible, which is exactly what makes it useful for precise control.
    \item \textbf{Myth:} bleed air and hydraulic power come from the same source.
    \textbf{Fact:} bleed air comes from the engine compressor; hydraulic power comes
    from a separate pump, though both are often engine-driven.
    \item \textbf{Myth:} the APU can replace a main engine in flight. \textbf{Fact:} the
    APU supplies electrical and pneumatic power, not flight thrust.
    \end{itemize}"""),
   ("In-Class Practice",
    r"""\begin{enumerate}
    \item Explain the function of a fuel crossfeed system.
    \item Explain why hydraulic fluid's incompressibility is useful for flight controls.
    \item Name two systems that use pneumatic bleed air.
    \end{enumerate}"""),
   ("Extended In-Class Practice / Group Discussion",
    r"""In small groups, discuss and be ready to present:
    \begin{enumerate}
    \item Debate: why do transport aircraft use multiple independent hydraulic systems
    instead of one larger system?
    \item Explain, using the fuel exhaustion case study, how a unit-conversion error
    could lead to a serious in-flight fuel problem.
    \item Sketch how bleed air travels from the engine compressor to two different
    pneumatic system applications.
    \end{enumerate}""")],
  I("The fuel system stores and delivers fuel while managing balance and quantity indication.",
    "The hydraulic system uses pressurized, incompressible fluid to power flight controls, gear, and brakes.",
    "The pneumatic system uses engine bleed air for anti-ice, engine start, and cabin air supply."),
  I("Explain the function of a fuel crossfeed system.",
    "Explain why hydraulic fluid's incompressibility makes it suited to flight control actuation.",
    "Name two systems that use pneumatic bleed air.",
    "Explain the role of the APU in supporting hydraulic and pneumatic systems on the ground."))

M[15] = ("Electrical \\& Basic Instrument/Avionics Systems",
  "Students are able to explain basic electrical and instrument/avionics systems and apply documentation, marking, ground handling, and aircraft safety equipment procedures.",
  I("Explain the components and function of the aircraft electrical system.",
    "Explain the basic flight instruments and the pitot-static system.",
    "Explain basic avionics functions: communication, navigation, and transponder."),
  [("Why Electrical \\& Avionics Systems Matter",
    r"""Every system covered so far -- flight controls, landing gear, fuel management --
    depends on the flight crew having accurate information and reliable electrical power.
    \begin{itemize}
    \item The electrical system powers instruments, avionics, lighting, and countless
    other aircraft systems.
    \item Flight instruments turn raw physical measurements into information the pilot
    can act on.
    \item This meeting covers electrical generation/distribution, basic instruments,
    and basic avionics.
    \end{itemize}"""),
   (r"Electrical Power Generation: Generator/Alternator",
    r"""\begin{itemize}
    \item Most aircraft electrical power is generated by a \textbf{generator} or
    \textbf{alternator} driven directly by the engine.
    \item Converts the engine's rotating mechanical power into electrical power, similar
    in principle to an automobile's alternator but built to aviation standards.
    \item On multi-engine aircraft, each engine typically drives its own generator,
    providing built-in electrical redundancy.
    \end{itemize}"""),
   ("Battery: Function and Backup Role",
    r"""\begin{itemize}
    \item Provides electrical power for engine starting and serves as a backup power
    source if generators fail.
    \item Ensures essential instruments and communication remain powered for a limited
    time during an electrical emergency.
    \item Must be regularly inspected and maintained, since a weak battery undermines
    this entire backup safety function.
    \end{itemize}"""),
   (r"AC vs.\ DC Electrical Power",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Type & Typical Use\\\hline
    DC (direct current) & Battery power, many light aircraft systems\\
    AC (alternating current) & Larger aircraft; efficient for high-power distribution\\\hline
    \end{tabular}\end{center}
    Larger transport aircraft often generate AC power and convert it to DC locally
    where DC is needed, since AC distributes more efficiently over long cable runs."""),
   ("Electrical Bus System (Concept)",
    r"""\begin{itemize}
    \item A \textbf{bus} is a common electrical distribution point that multiple
    systems draw power from.
    \item Aircraft typically have multiple buses (e.g.\ main, essential, battery) so
    that losing one power source does not remove power from every system at once.
    \item This mirrors the redundancy philosophy already seen in Meeting 4's flight
    controls and Meeting 14's hydraulic systems.
    \end{itemize}"""),
   ("Circuit Protection: Fuses and Circuit Breakers",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Device & Description\\\hline
    Fuse & One-time protection; melts and must be replaced after tripping\\
    Circuit breaker & Resettable protection; pops out and can be manually reset\\\hline
    \end{tabular}\end{center}
    Both devices protect wiring and equipment from damage due to excess current,
    interrupting the circuit before overheating can occur."""),
   ("Electrical Load Shedding (Concept)",
    r"""\begin{itemize}
    \item If electrical power generation is reduced (e.g.\ after a generator failure),
    non-essential equipment is automatically or manually switched off.
    \item This \textbf{load shedding} preserves remaining power for flight-critical
    systems: essential instruments, communication, and flight controls.
    \item The same underlying logic as fail-safe structural design (Meeting 6): protect
    what matters most when full capability is not available.
    \end{itemize}"""),
   (r"Static Electricity and Bonding/Grounding (Brief)",
    r"""\begin{itemize}
    \item Aircraft accumulate static electric charge from airflow friction and fuel
    movement during flight and refueling.
    \item \textbf{Bonding} connects metal components electrically so charge cannot build
    up unevenly between them; \textbf{grounding} connects the aircraft to earth during
    ground servicing.
    \item Improper bonding/grounding during refueling is a recognized fire risk, which is
    why grounding cables are a standard part of the fueling procedure.
    \end{itemize}"""),
   (r"Basic Flight Instruments Overview (``Six Pack'')",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    Instrument & Measures\\\hline
    Airspeed indicator & Aircraft speed through the air\\
    Attitude indicator & Aircraft pitch and bank angle\\
    Altimeter & Height above a reference pressure level\\
    Turn coordinator & Rate of turn and bank\\
    Heading indicator & Aircraft heading\\
    Vertical speed indicator & Rate of climb or descent\\\hline
    \end{tabular}\end{center}"""),
   ("Pitot-Static System (Concept)",
    r"""\begin{itemize}
    \item A \textbf{pitot tube} measures the pressure of oncoming air (ram air pressure).
    \item \textbf{Static ports} measure the undisturbed ambient air pressure around the aircraft.
    \item Comparing pitot and static pressure (or static pressure alone) drives the
    airspeed indicator, altimeter, and vertical speed indicator -- three instruments
    from one shared source of air pressure.
    \end{itemize}"""),
   ("Airspeed Indicator",
    r"""\begin{itemize}
    \item Compares ram air pressure (from the pitot tube) against static pressure to
    display the aircraft's speed through the air.
    \item Critical for maintaining safe margins above stall speed (Meeting 5) and below
    structural speed limits (Meeting 5's VFE, and similar limits for other configurations).
    \item Reads speed relative to the surrounding air mass, not necessarily the
    aircraft's speed over the ground.
    \end{itemize}"""),
   ("Altimeter",
    r"""\begin{itemize}
    \item Measures static air pressure and converts it to an altitude reading, since
    air pressure decreases predictably with height.
    \item Pilots set a reference pressure (local or standard) so the displayed altitude
    matches the correct reference for the phase of flight.
    \item Essential for maintaining safe vertical separation from terrain and other traffic.
    \end{itemize}"""),
   ("Vertical Speed Indicator",
    r"""\begin{itemize}
    \item Measures the \emph{rate of change} of static pressure to display how quickly
    the aircraft is climbing or descending.
    \item Helps pilots establish and maintain a stable, predictable climb or descent rate.
    \item Works from the same static pressure source as the altimeter, but shows the
    trend rather than the absolute value.
    \end{itemize}"""),
   ("Attitude Indicator (Gyroscopic, Concept)",
    r"""\begin{itemize}
    \item Displays the aircraft's pitch and bank angle relative to the horizon,
    independent of outside visibility.
    \item Traditionally driven by a spinning gyroscope that resists changes to its
    orientation in space (this meeting's next topic).
    \item Especially critical in cloud or low-visibility conditions, where the pilot
    cannot see the real horizon directly.
    \end{itemize}"""),
   ("Heading Indicator (Gyroscopic, Concept)",
    r"""\begin{itemize}
    \item Displays the aircraft's heading using a gyroscope, giving a steadier reading
    than a magnetic compass during maneuvering.
    \item Must be periodically re-aligned to the magnetic compass, since gyroscopic
    drift accumulates slowly over time.
    \item Complements primary flight controls (Meeting 4) by confirming the aircraft is
    tracking the heading the pilot intends.
    \end{itemize}"""),
   ("Turn Coordinator",
    r"""\begin{itemize}
    \item Shows the aircraft's rate of turn and roll rate, along with a ball that
    indicates whether the turn is coordinated (recall Meeting 4's adverse yaw discussion).
    \item A centered ball means the rudder and aileron inputs are properly coordinated;
    an off-center ball signals a slip or skid.
    \item Directly ties classroom flight-control theory (Meeting 4) to a real cockpit
    instrument reading.
    \end{itemize}"""),
   ("Gyroscopic Principle (Concept)",
    r"""\begin{itemize}
    \item A spinning gyroscope resists changes to the direction its spin axis points --
    a property called \textbf{rigidity in space}.
    \item Attitude and heading indicators exploit this rigidity: as the aircraft
    rotates around the gyroscope, the instrument mechanically senses that relative motion.
    \item Modern aircraft increasingly use electronic sensors (ring laser or fiber-optic
    gyros) rather than spinning mechanical gyroscopes, but the underlying physical
    principle these terms describe remains the reference concept.
    \end{itemize}"""),
   ("Pitot-Static System Errors and Blockage (Concept)",
    r"""\begin{itemize}
    \item A blocked pitot tube (e.g.\ from ice or insects) causes incorrect or frozen
    airspeed indication, since ram air pressure can no longer update correctly.
    \item A blocked static port similarly corrupts altimeter, vertical speed, and
    airspeed readings, since all three rely on static pressure.
    \item Pitot heat (an electrical heating element) is used to prevent ice blockage --
    another example of electrical systems supporting flight safety.
    \end{itemize}"""),
   ("Basic Avionics: Communication Radios (Concept)",
    r"""\begin{itemize}
    \item \textbf{Communication radios} let the crew talk to air traffic control and
    other aircraft, typically using VHF frequencies.
    \item Multiple radios are usually fitted so the crew can monitor more than one
    frequency, or retain communication if one radio fails.
    \item Clear, standardized radio communication is essential for safe separation
    from other aircraft, especially near busy airports.
    \end{itemize}"""),
   (r"Basic Avionics: Navigation Radios (VOR/GPS Concept)",
    r"""\begin{center}\begin{tabular}{l|l}\hline
    System & Description\\\hline
    VOR (VHF Omnidirectional Range) & Ground station broadcasts a directional radio signal\\
    GPS (Global Positioning System) & Satellite-based position determination\\\hline
    \end{tabular}\end{center}
    Modern aircraft primarily navigate by GPS, with VOR retained as a
    well-established backup navigation method."""),
   ("Transponder (Concept)",
    r"""\begin{itemize}
    \item A \textbf{transponder} receives a signal from ground radar and automatically
    replies with the aircraft's identity and altitude.
    \item This lets air traffic control see and identify the aircraft clearly on radar,
    beyond what a simple radar reflection alone would show.
    \item Also feeds collision-avoidance systems on other aircraft, which listen for
    nearby transponder replies to detect traffic.
    \end{itemize}"""),
   (r"Electronic Flight Instrument System (EFIS) / Glass Cockpit",
    r"""\begin{itemize}
    \item Modern aircraft replace individual mechanical instruments with digital
    displays presenting the same information (and more) on electronic screens.
    \item A \textbf{glass cockpit} combines flight instruments, navigation, and engine
    information onto a small number of large, configurable displays.
    \item Requires robust electrical power and backup systems, since a glass cockpit
    depends entirely on electricity to function, unlike some traditional mechanical instruments.
    \end{itemize}"""),
   (r"Comparison: Analog vs.\ Glass Cockpit Instruments",
    r"""\begin{center}\begin{tabular}{l|l|l}\hline
    Aspect & Analog (Mechanical) & Glass Cockpit (EFIS)\\\hline
    Power dependency & Some instruments work without power & Fully power-dependent\\
    Information density & Limited per gauge & High, configurable displays\\
    Typical aircraft & Older or light aircraft & Most modern aircraft\\\hline
    \end{tabular}\end{center}"""),
   ("Autopilot System (Brief)",
    r"""\begin{itemize}
    \item An \textbf{autopilot} automatically controls the aircraft's flight path,
    commanding the primary flight controls introduced in Meeting 4.
    \item Uses information from flight instruments (attitude, heading, altitude) as its
    reference for maintaining the desired flight path.
    \item Recall from Meeting 5 that an engaged autopilot also manages trim, keeping the
    aircraft balanced as conditions change during automated flight.
    \end{itemize}"""),
   ("Avionics Bay and Equipment Cooling (Brief)",
    r"""\begin{itemize}
    \item Electronic equipment generates heat and is sensitive to temperature and moisture,
    so avionics units are housed in a dedicated, often cooled compartment.
    \item Recall from Meeting 2 that the nose section commonly contains the avionics bay,
    just aft of the radome.
    \item Reliable cooling airflow is treated as a maintenance-critical item, since
    overheated avionics can fail or give unreliable readings.
    \end{itemize}"""),
   ("Electrical System Redundancy (Concept)",
    r"""\begin{itemize}
    \item Like the hydraulic systems in Meeting 14, electrical power is generated and
    distributed through multiple independent paths.
    \item Battery power, multiple generators, and separate buses together ensure that no
    single failure removes power from every flight-critical system at once.
    \item This redundancy theme -- repeated across flight controls, hydraulics, and now
    electrics -- is one of the central design philosophies of this entire course.
    \end{itemize}"""),
   ("Case Study: Pitot Tube Blockage Incident",
    r"""\begin{itemize}
    \item Historical incidents involving blocked or iced pitot tubes have produced
    unreliable airspeed indications during flight, some with serious consequences.
    \item Investigations of these events led to improved pitot heating standards and
    specific pilot training for recognizing and handling unreliable airspeed indications.
    \item This case reinforces why pitot heat (an electrical system) is treated as a
    safety-critical item, not merely a comfort feature.
    \end{itemize}"""),
   ("Case Study: Electrical System Failure and Backup Instruments",
    r"""\begin{itemize}
    \item Total or partial electrical failures have occurred historically from generator
    faults combined with battery or bus management issues.
    \item In well-handled cases, crews relied on battery-powered backup instruments and
    standard emergency procedures to land safely.
    \item These events are why every aircraft carries some form of minimum backup
    instrumentation independent of the main electrical generation system.
    \end{itemize}"""),
   ("Applied Scenario: Diagnosing Unreliable Airspeed Indication",
    r"""During climb, the airspeed indicator suddenly freezes at a constant value. Work through the diagnosis:
    \begin{enumerate}
    \item Recognize this as a possible pitot tube blockage (e.g.\ icing), since a
    frozen reading rather than an erratic one is a classic symptom.
    \item Cross-check other instruments (attitude, altitude, engine power) to fly a
    safe pitch and power combination without relying on the frozen airspeed reading.
    \item Confirm pitot heat is selected on, and follow the unreliable-airspeed checklist.
    \end{enumerate}"""),
   ("Applied Scenario: Responding to a Generator Failure",
    r"""A single-engine aircraft's generator fails in flight. Work through the response:
    \begin{enumerate}
    \item The battery automatically becomes the sole electrical source, so non-essential
    equipment is switched off to conserve battery life (load shedding).
    \item The crew prioritizes flight-critical instruments and communication over
    secondary systems for the remainder of the flight.
    \item The flight is typically terminated at the nearest suitable airport, since
    battery power is finite and not intended for extended operation.
    \end{enumerate}"""),
   ("In-Class Practice",
    r"""\begin{enumerate}
    \item Name the three instruments driven by the pitot-static system.
    \item Explain the difference between a fuse and a circuit breaker.
    \item Explain the function of a transponder.
    \end{enumerate}"""),
   ("Extended In-Class Practice / Group Discussion",
    r"""In small groups, discuss and be ready to present:
    \begin{enumerate}
    \item Debate: is a glass cockpit safer or riskier than traditional analog
    instruments? Justify using the redundancy concepts from this meeting.
    \item Explain, step by step, how a blocked pitot tube affects the airspeed indicator.
    \item Sketch the pitot-static system and label the pitot tube, static port, and the
    three instruments it feeds.
    \end{enumerate}""")],
  I("The electrical system generates, distributes, and protects power through generators, batteries, buses, and circuit protection devices.",
    "The pitot-static system feeds the airspeed indicator, altimeter, and vertical speed indicator from pitot and static pressure.",
    "Basic avionics (communication, navigation, transponder) and EFIS/glass cockpit displays depend on reliable electrical power."),
  I("Name the three instruments driven by the pitot-static system.",
    "Explain the difference between a fuse and a circuit breaker.",
    "Explain the function of a transponder.",
    "Explain why electrical system redundancy (multiple generators, battery backup) is essential."))

M[16] = ("Documentation, Ground Handling \\& Aircraft Safety",
  "Students are able to explain basic electrical and instrument/avionics systems and apply documentation, marking, ground handling, and aircraft safety equipment procedures.",
  I("Explain the required aircraft documents and their purpose.",
    "Explain aircraft markings and ground handling procedures.",
    "Explain the function of key aircraft safety equipment."),
  [("Why Documentation, Ground Handling \\& Safety Matter",
    r"""An airworthy, well-understood aircraft (Meetings 1--15) must still be operated
    legally, handled safely on the ground, and equipped for emergencies.
    \begin{itemize}
    \item Documentation proves an aircraft is legally and technically fit to fly.
    \item Markings and ground handling procedures keep personnel and the aircraft safe
    during routine operations.
    \item Safety equipment protects occupants when something goes wrong.
    \end{itemize}"""),
   ("Required Aircraft Documents Overview",
    r"""\begin{itemize}
    \item Every aircraft must carry a defined set of documents to fly legally, both
    on board and in the operator's records.
    \item These documents prove the aircraft is registered, airworthy, correctly loaded,
    and properly maintained.
    \item The rest of this meeting covers the most important of these documents in turn.
    \end{itemize}"""),
   ("Certificate of Airworthiness",
    r"""\begin{itemize}
    \item Issued by the national aviation authority (DGCA in Indonesia, recall Meeting 1)
    certifying the aircraft meets its approved design and safety standards.
    \item Remains valid only as long as the aircraft is maintained in accordance with its
    approved maintenance program.
    \item Without a valid Certificate of Airworthiness, an aircraft is not legally
    permitted to fly.
    \end{itemize}"""),
   ("Certificate of Registration",
    r"""\begin{itemize}
    \item Establishes the aircraft's nationality and links it to its registration mark
    (recall Meeting 1's PK- prefix for Indonesian-registered aircraft).
    \item Identifies the legal owner or operator of the aircraft.
    \item Distinct from the Certificate of Airworthiness -- registration is about legal
    ownership and nationality, airworthiness is about technical fitness to fly.
    \end{itemize}"""),
   ("Aircraft Flight Manual / POH (Brief)",
    r"""\begin{itemize}
    \item The \textbf{Aircraft Flight Manual} (or Pilot's Operating Handbook on lighter
    aircraft) defines approved operating limits, procedures, and performance data.
    \item Covers items such as maximum speeds, weight limits, and normal/emergency
    procedures specific to that aircraft type.
    \item Operating outside the flight manual's approved limits removes the aircraft
    from its certified, tested operating envelope.
    \end{itemize}"""),
   ("Weight and Balance Documentation",
    r"""\begin{itemize}
    \item Records the aircraft's empty weight, center of gravity, and how both change
    with passengers, cargo, and fuel.
    \item Directly supports the CG-range discussion from Meeting 4 -- this is the
    paperwork that confirms every flight stays within safe CG limits.
    \item Must be recalculated whenever the aircraft's configuration changes
    significantly (e.g.\ after a major repair or modification).
    \end{itemize}"""),
   ("Aircraft Logbook and Maintenance Records",
    r"""\begin{itemize}
    \item Records every inspection, repair, and modification performed on the aircraft,
    engine, and propeller throughout its service life.
    \item Supports the material traceability concept from Meeting 10 -- a documented
    history that lets any future defect be traced back to its cause.
    \item Reviewed before every flight (for currency of required inspections) and
    audited regularly by the regulator.
    \end{itemize}"""),
   ("Minimum Equipment List (MEL) Concept",
    r"""\begin{itemize}
    \item A \textbf{Minimum Equipment List} defines which instruments and systems may be
    inoperative while still permitting a legal, safe flight, under specific conditions.
    \item Not every failed item grounds the aircraft -- the MEL formally distinguishes
    genuinely flight-critical equipment from items with an acceptable workaround.
    \item Any item allowed to remain inoperative under the MEL must still be placarded
    and tracked for timely repair.
    \end{itemize}"""),
   ("Aircraft Markings: Registration Marks Recap and Detail",
    r"""\begin{itemize}
    \item Meeting 1 introduced registration marks (e.g.\ Indonesian PK- prefix) as an
    aircraft's unique identifier.
    \item Registration marks must be displayed at a minimum size and in a specified
    location (commonly the fuselage and/or wings) so they are clearly readable.
    \item Enforcement inspectors and air traffic controllers rely on these markings to
    positively identify a specific aircraft.
    \end{itemize}"""),
   ("Aircraft Markings: Placards and Warning Labels",
    r"""\begin{itemize}
    \item \textbf{Placards} are small signs fixed near specific equipment, stating
    operating limits or hazard warnings (e.g.\ maximum jacking weight, fuel type).
    \item Required placards are specified in the aircraft's type certification, not
    left to individual operator preference.
    \item Missing or illegible placards are a maintenance discrepancy, since they
    convey safety-critical information to crew and ground personnel.
    \end{itemize}"""),
   (r"Aircraft Markings: No-Step and No-Push Areas",
    r"""\begin{itemize}
    \item \textbf{No-step} markings identify areas of the wing or fuselage too thin or
    lightly built to bear a person's weight without damage.
    \item \textbf{No-push} markings identify areas that must not be used to push or pull
    the aircraft during ground handling, to avoid damaging lightweight skin or fairings.
    \item These markings directly protect the thin composite and metal skin panels
    discussed in Meetings 10--11 from accidental ground damage.
    \end{itemize}"""),
   (r"Aircraft Markings: Static Ports and Pitot Tube Warnings",
    r"""\begin{itemize}
    \item Static ports and pitot tubes (Meeting 15) are marked to prevent accidental
    blockage, tape-over, or damage during cleaning and ground servicing.
    \item Covers are often fitted when parked, marked with a conspicuous streamer to
    ensure they are visibly removed before flight.
    \item A missed pitot/static cover before departure directly causes the unreliable
    airspeed scenario discussed in Meeting 15.
    \end{itemize}"""),
   ("Ground Handling: Towing (Concept)",
    r"""\begin{itemize}
    \item Aircraft too large to be pushed by hand are moved on the ground by a tow
    tractor attached to the nose or main gear.
    \item Towing must respect gear turn-angle and tow-force limits to avoid damaging the
    nose gear steering system (Meeting 12).
    \item A trained ground crew member typically monitors the tow, since the tow
    tractor driver cannot always see the entire aircraft.
    \end{itemize}"""),
   ("Ground Handling: Chocking and Parking Brakes",
    r"""\begin{itemize}
    \item \textbf{Wheel chocks} are wedges placed against the wheels to prevent
    unintended aircraft movement while parked.
    \item Used together with (or sometimes instead of) the parking brake, since brakes
    alone can be affected by hydraulic pressure loss over time (recall Meeting 14).
    \item Standard procedure on most ramps requires chocks in place before ground crew
    approach the aircraft for servicing.
    \end{itemize}"""),
   ("Ground Handling: Marshalling Signals (Concept)",
    r"""\begin{itemize}
    \item A \textbf{marshaller} uses standardized hand signals to guide the aircraft
    into or out of a parking position.
    \item Signals cover actions such as proceed straight ahead, turn, stop, and
    apply/release brakes -- understood identically at airports worldwide.
    \item Standardization matters because the same aircraft may be marshalled by ground
    crew from many different countries and operators over its service life.
    \end{itemize}"""),
   ("Ground Handling: Ground Power and Air Start Units",
    r"""\begin{itemize}
    \item A \textbf{ground power unit (GPU)} supplies electrical power to the parked
    aircraft, letting systems run without draining the battery or running an engine.
    \item An \textbf{air start unit} supplies high-pressure air for engine starting,
    an alternative to the APU discussed in Meeting 14.
    \item Both reduce fuel burn and noise at the gate compared to running the APU or
    main engines continuously.
    \end{itemize}"""),
   ("Ground Handling: Fueling Safety Procedures",
    r"""\begin{itemize}
    \item Fueling follows strict procedures including aircraft bonding/grounding
    (Meeting 15) to prevent static discharge near flammable fuel vapor.
    \item Fire extinguishing equipment must be positioned and ready during the entire
    fueling operation.
    \item Fuel type is carefully verified against aircraft placards (Meeting 14's
    avgas/jet fuel distinction) before any fuel is transferred.
    \end{itemize}"""),
   ("Ground Handling: FOD (Foreign Object Debris) Prevention",
    r"""\begin{itemize}
    \item \textbf{FOD} refers to any object -- tools, debris, wildlife -- that can be
    ingested by an engine or damage the airframe on the ground.
    \item Ramp areas are regularly inspected and kept clear of loose debris, especially
    near engine intakes.
    \item Even a small object ingested by a turbine engine's compressor (Meeting 13)
    can cause serious internal damage.
    \end{itemize}"""),
   ("Safety Equipment: Fire Extinguishers",
    r"""\begin{itemize}
    \item Portable fire extinguishers are carried on board for cabin and cockpit fires,
    sized and located per regulatory requirement.
    \item Different extinguishing agents suit different fire types (e.g.\ electrical
    versus general combustible fires).
    \item Ground fire extinguishing equipment is also staged near the aircraft during
    fueling and engine starting, as noted earlier this meeting.
    \end{itemize}"""),
   ("Safety Equipment: Emergency Evacuation Slides",
    r"""\begin{itemize}
    \item Inflatable slides deploy automatically or manually at exit doors, allowing
    rapid passenger evacuation without stairs.
    \item Certification requires that a full aircraft can be evacuated within a strict
    time limit using only half of the available exits.
    \item Slides are inspected and repacked on a scheduled interval, since a slide that
    fails to inflate defeats its entire safety purpose.
    \end{itemize}"""),
   ("Safety Equipment: Life Vests and Rafts",
    r"""\begin{itemize}
    \item Required on aircraft operating significant distances over water.
    \item Life vests are stored at each passenger seat; life rafts (often built into
    slide/raft combination units) support the entire aircraft's occupants.
    \item Crew safety briefings cover life vest use specifically because passengers
    rarely handle this equipment outside of a real emergency.
    \end{itemize}"""),
   ("Safety Equipment: ELT (Emergency Locator Transmitter)",
    r"""\begin{itemize}
    \item An \textbf{ELT} automatically activates on a hard impact, transmitting a
    distress signal to help search-and-rescue teams locate the aircraft.
    \item Battery-powered and independent of the aircraft's main electrical system,
    similar in spirit to the standalone magneto ignition discussed in Meeting 13.
    \item Regularly tested and battery-replaced on a fixed schedule, since it must work
    reliably in the exact scenario when other systems may have failed.
    \end{itemize}"""),
   ("Safety Equipment: Oxygen Systems (Brief)",
    r"""\begin{itemize}
    \item Supplemental oxygen is required for flight crew and, on pressurized aircraft,
    for passengers if cabin pressurization (Meeting 2) is lost at altitude.
    \item Drop-down passenger oxygen masks deploy automatically on a significant
    pressurization loss.
    \item Crew oxygen systems must be immediately available, since flight crew may need
    to don masks and continue operating the aircraft during a depressurization event.
    \end{itemize}"""),
   ("Safety Equipment: First Aid Kits",
    r"""\begin{itemize}
    \item Standard first aid kits are carried for routine minor injuries during flight.
    \item Larger aircraft also carry an enhanced medical kit for more serious in-flight
    medical events, often for use under remote medical guidance.
    \item Contents, quantities, and inspection intervals are specified by regulation,
    not left to individual operator discretion.
    \end{itemize}"""),
   ("Regulatory Compliance: DGCA Oversight Recap",
    r"""\begin{itemize}
    \item Meeting 1 introduced DGCA as Indonesia's national aviation regulator.
    \item Every document, marking, and safety equipment requirement covered this
    meeting exists because a regulator (DGCA, or ICAO standards it adopts) mandates it.
    \item Compliance is not optional paperwork -- it is the practical mechanism by
    which safety standards are enforced across the whole industry.
    \end{itemize}"""),
   ("Ramp Safety: Personnel Protective Equipment",
    r"""\begin{itemize}
    \item Ground personnel working near aircraft wear high-visibility vests and hearing
    protection due to engine noise and moving vehicle traffic.
    \item Strict rules govern approaching an aircraft with engines running, especially
    near intakes and exhaust.
    \item Ramp safety protects both personnel and the aircraft -- an injured technician
    or a damaged aircraft both interrupt safe, on-time operations.
    \end{itemize}"""),
   ("Case Study: FOD Damage Incident",
    r"""\begin{itemize}
    \item Numerous documented incidents involve a turbine engine ingesting debris left
    on the ramp, causing internal damage requiring costly repair or engine replacement.
    \item These events reinforced routine ramp FOD walks (visual sweeps of the ramp
    surface) before aircraft movement.
    \item A simple, low-cost prevention step (clearing debris) avoids one of the most
    expensive and disruptive categories of ground damage.
    \end{itemize}"""),
   ("Case Study: Ground Handling Accident from Missed Chocking",
    r"""\begin{itemize}
    \item Several ground handling incidents have occurred when an aircraft moved
    unexpectedly because chocks were not placed or were removed prematurely.
    \item These events reinforced standardized ground handling checklists requiring
    chock placement to be visually confirmed before other ground work begins.
    \item This illustrates that ground handling procedures, like flight procedures,
    exist because of real historical incidents, not just theoretical caution.
    \end{itemize}"""),
   ("Applied Scenario: Pre-Departure Documentation Check",
    r"""Before a flight, a ground crew member reviews the aircraft's paperwork. Work through the check:
    \begin{enumerate}
    \item Confirm the Certificate of Airworthiness and Certificate of Registration are
    on board and valid.
    \item Confirm the weight and balance calculation for this specific flight is within
    approved limits.
    \item Confirm the maintenance logbook shows all required inspections are current,
    and check the MEL for any open items affecting this flight.
    \end{enumerate}"""),
   ("Applied Scenario: Responding to a Marshalling Signal",
    r"""A marshaller signals the aircraft to stop immediately while taxiing to the gate. Work through the response:
    \begin{enumerate}
    \item The pilot applies brakes promptly, trusting the marshaller's view of
    obstacles or hazards the flight deck may not be able to see.
    \item The crew waits for a clear follow-up signal before resuming any movement.
    \item If the marshaller's signal is unclear or contradictory, the pilot stops and
    seeks clarification rather than guessing.
    \end{enumerate}"""),
   ("In-Class Practice",
    r"""\begin{enumerate}
    \item Name three required aircraft documents and explain the purpose of each.
    \item Explain the difference between a no-step marking and a no-push marking.
    \item Name three items of aircraft safety equipment and their function.
    \end{enumerate}"""),
   ("Extended In-Class Practice / Group Discussion",
    r"""In small groups, discuss and be ready to present:
    \begin{enumerate}
    \item Debate: why does the Minimum Equipment List allow some failed equipment to
    remain inoperative rather than requiring every system to work perfectly?
    \item Explain, using the FOD case study, why a simple ramp walk is treated as a
    serious safety procedure rather than routine cleaning.
    \item Role-play a marshaller guiding an aircraft to a stop, then guiding it to a turn.
    \end{enumerate}""")],
  I("Required aircraft documents (airworthiness, registration, weight and balance, logbook) prove an aircraft is legal and fit to fly.",
    "Aircraft markings and ground handling procedures (towing, chocking, marshalling, FOD prevention) protect personnel and the aircraft.",
    "Safety equipment (fire extinguishers, evacuation slides, life vests, ELT, oxygen) protects occupants during an emergency."),
  I("Name three required aircraft documents and explain the purpose of each.",
    "Explain the purpose of no-step and no-push markings.",
    "Explain the function of an ELT and why it is battery-independent.",
    "Explain why FOD prevention and correct chocking procedures are treated as serious safety requirements."))

M[17] = ("Integrated Review \\& Practice (Pre-Final Exam)",
  "Students are able to integrate concepts of airframe materials, powerplant systems, and aircraft support systems (Meetings 10--16) in preparation for the final examination.",
  I("Combine materials, landing gear, powerplant, and support-system concepts in one problem.",
    "Solve mixed exercises accurately across Meetings 10--16.",
    "Confirm readiness for the final examination."),
  [("Why This Integration Meeting?",
    r"""Meeting 7 integrated Meetings 1--6; this meeting does the same for the
    materials- and systems-focused second half of the course.
    \begin{itemize}
    \item This meeting stitches Meetings 10--16 together with mixed review and practice.
    \item The final exam (Meeting 18) covers Meetings 10--17 -- everything after the midterm.
    \item Goal: recognize which topic area a question is really asking about, then
    answer with the correct vocabulary, just as in Meeting 7.
    \end{itemize}"""),
   (r"Recap: Airframe Materials (Meetings 10--11)",
    r"""\begin{itemize}
    \item Aluminum, titanium, and steel each trade off strength, weight, and cost differently.
    \item Alclad, heat treatment, and corrosion prevention extend metallic structure life.
    \item Composites (CFRP/GFRP, honeycomb sandwich) offer excellent strength-to-weight
    and fatigue resistance, but require different damage detection (tap test, C-scan).
    \end{itemize}"""),
   ("Recap: Landing Gear (Meeting 12)",
    r"""\begin{itemize}
    \item Tricycle gear (nose + two main) is the modern standard; tailwheel trades
    complexity for propeller clearance.
    \item The oleo-pneumatic shock strut combines a gas spring with hydraulic damping
    to absorb touchdown energy.
    \item Anti-skid brakes, retraction, indication, and emergency (free-fall) extension
    all work together to ensure safe ground operation.
    \end{itemize}"""),
   ("Recap: Powerplant (Meeting 13)",
    r"""\begin{itemize}
    \item Piston engines use a four-stroke cycle (intake, compression, power, exhaust)
    to turn a propeller.
    \item Gas turbines continuously compress, burn, and expand air through intake,
    compressor, combustor, turbine, and exhaust sections.
    \item Turbojet, turbofan, turboprop, and turboshaft are gas turbine variants,
    distinguished by how thrust or shaft power is produced.
    \end{itemize}"""),
   (r"Recap: Fuel, Hydraulic \& Pneumatic Systems (Meeting 14)",
    r"""\begin{itemize}
    \item The fuel system stores, distributes, and balances fuel between tanks.
    \item Hydraulic systems use incompressible fluid to power flight controls, gear,
    and brakes, with multiple independent systems for redundancy.
    \item Pneumatic systems use engine bleed air for anti-ice, engine start, and cabin air.
    \end{itemize}"""),
   (r"Recap: Electrical \& Avionics (Meeting 15)",
    r"""\begin{itemize}
    \item Generators/alternators, batteries, buses, and circuit protection together
    generate, distribute, and protect electrical power.
    \item The pitot-static system feeds the airspeed indicator, altimeter, and
    vertical speed indicator.
    \item Basic avionics (communication, navigation, transponder) and EFIS displays
    depend on that same electrical foundation.
    \end{itemize}"""),
   (r"Recap: Documentation, Ground Handling \& Safety (Meeting 16)",
    r"""\begin{itemize}
    \item Required documents (airworthiness, registration, weight and balance,
    logbook) prove an aircraft is legal and fit to fly.
    \item Markings and ground handling procedures (towing, chocking, marshalling, FOD
    prevention) protect personnel and the aircraft.
    \item Safety equipment (fire extinguishers, slides, life vests, ELT, oxygen)
    protects occupants during an emergency.
    \end{itemize}"""),
   (r"Integration Table: Meeting 10--16 Topic Map",
    r"""\begin{center}\begin{tabular}{c|l}\hline
    Meeting & Core Topic\\\hline
    10 & Airframe materials: metallic structures\\
    11 & Airframe materials: composite structures\\
    12 & Landing gear system\\
    13 & Powerplant system overview\\
    14 & Fuel, hydraulic, and pneumatic systems\\
    15 & Electrical and basic instrument/avionics systems\\
    16 & Documentation, ground handling, and aircraft safety\\\hline
    \end{tabular}\end{center}"""),
   (r"Vocabulary Review: Key Terms (Meetings 10--12)",
    r"""\begin{itemize}
    \item \textbf{Alclad, CFRP, delamination, BVID} -- metallic and composite materials (M10--11).
    \item \textbf{Oleo-pneumatic, bogie, anti-skid, free-fall extension} -- landing gear (M12).
    \end{itemize}"""),
   (r"Vocabulary Review: Key Terms (Meetings 13--14)",
    r"""\begin{itemize}
    \item \textbf{Four-stroke cycle, bypass ratio, FADEC} -- powerplant (M13).
    \item \textbf{Crossfeed, bleed air, APU, hydraulic actuator} -- fuel/hydraulic/pneumatic (M14).
    \end{itemize}"""),
   (r"Vocabulary Review: Key Terms (Meetings 15--16)",
    r"""\begin{itemize}
    \item \textbf{Pitot-static system, transponder, glass cockpit, load shedding} --
    electrical/avionics (M15).
    \item \textbf{Certificate of Airworthiness, MEL, FOD, ELT} -- documentation/ground
    handling/safety (M16).
    \end{itemize}"""),
   (r"Integrated Walkthrough: A Complete Aircraft (Materials \& Systems)",
    r"""Consider a twin-turbofan narrow-body airliner on the ramp before departure:
    \begin{enumerate}
    \item \textbf{Materials:} aluminum fuselage skin with composite control surfaces
    and fairings.
    \item \textbf{Landing gear:} retractable tricycle gear with oleo-pneumatic struts
    and anti-skid brakes.
    \item \textbf{Powerplant:} twin turbofans supplying thrust, bleed air, and driving
    hydraulic/electrical generation.
    \item \textbf{Support systems:} fuel balanced between wing tanks, hydraulics
    powering flight controls and gear, electrics powering avionics and instruments.
    \item \textbf{Documentation/safety:} valid airworthiness/registration certificates,
    correct markings, chocks set, safety equipment on board.
    \end{enumerate}"""),
   ("Cross-Topic Pitfalls",
    r"""\begin{itemize}
    \item Confusing composite damage (delamination, BVID) with metal damage (visible
    cracks, corrosion) -- they require different inspection methods.
    \item Mixing up bleed air (pneumatic, from the compressor) with hydraulic power
    (from a separate pump).
    \item Confusing the Certificate of Airworthiness (technical fitness) with the
    Certificate of Registration (legal ownership/nationality).
    \item Treating the pitot-static system as only feeding the airspeed indicator, when
    it also feeds the altimeter and vertical speed indicator.
    \end{itemize}"""),
   ("Practice 1 -- Problem",
    r"A wing skin panel is found to be high-strength aluminum with a pure-aluminum surface layer. Name this material and explain why the surface layer is included."),
   ("Practice 1 -- Solution",
    r"""This is Alclad aluminum sheet.
    \\The pure aluminum cladding sacrifices itself to corrosion first, protecting the
    stronger but more corrosion-prone alloy core beneath it."""),
   ("Practice 2 -- Problem",
    r"A large airliner's main landing gear leg has four wheels mounted in a row on one strut. Name this arrangement and explain its purpose."),
   ("Practice 2 -- Solution",
    r"""This is a bogie (truck) gear arrangement.
    \\It spreads the aircraft's weight over more tire contact area, reducing pavement
    loading, and provides redundancy if one tire fails."""),
   ("Practice 3 -- Problem",
    r"An engine has a large-diameter fan at the front, with most incoming air bypassing the engine core. Name this engine type and explain one advantage over a pure turbojet."),
   ("Practice 3 -- Solution",
    r"""This is a turbofan (high-bypass) engine.
    \\Advantage: significantly better fuel efficiency and lower noise than a turbojet,
    since most thrust comes from the efficiently accelerated bypass air."""),
   ("Practice 4 -- Problem",
    r"After an engine failure, a twin-engine aircraft loses one hydraulic pump and one bleed air source. Explain why both are lost together."),
   ("Practice 4 -- Solution",
    r"""Both the hydraulic pump and the bleed air source for that engine are typically
    driven directly by the engine itself.
    \\When the engine stops, anything it directly drives stops with it -- which is why
    aircraft carry multiple engines, hydraulic systems, and an APU for redundancy."""),
   ("Practice 5 -- Problem",
    r"During climb, the airspeed indicator freezes at a constant reading while the altimeter continues to work normally. Diagnose the likely cause."),
   ("Practice 5 -- Solution",
    r"""A frozen airspeed reading with a normally functioning altimeter points to a
    blocked pitot tube (commonly from icing), not a static port blockage.
    \\A static port blockage would instead affect the altimeter, vertical speed
    indicator, and airspeed indicator together."""),
   ("Practice 6 -- Problem",
    r"A ground crew member finds an aircraft's chocks missing before starting fueling. Explain the correct response and why it matters."),
   ("Practice 6 -- Solution",
    r"""Chocks must be placed and visually confirmed before ground servicing begins,
    following standard ground handling procedure.
    \\Skipping this step risks unintended aircraft movement during fueling, a
    documented cause of past ground handling accidents."""),
   ("Practice 7 -- Problem",
    r"A composite wing panel shows no visible surface damage after a minor ground vehicle contact, but the technician still orders an ultrasonic inspection. Explain why."),
   ("Practice 7 -- Solution",
    r"""Composite structures can suffer barely visible impact damage (BVID) -- internal
    delamination with little or no visible surface mark.
    \\Because visual inspection alone cannot reliably detect this, an ultrasonic
    C-scan is used to confirm the panel's internal condition after any known impact."""),
   ("Practice 8 -- Problem",
    r"An aircraft's Certificate of Airworthiness has lapsed due to an overdue inspection, but its Certificate of Registration is current. Can the aircraft legally fly? Explain."),
   ("Practice 8 -- Solution",
    r"""No -- a valid Certificate of Airworthiness is required for legal flight,
    independent of registration status.
    \\Registration establishes ownership and nationality; airworthiness certifies
    technical fitness to fly. Both are required, but they are not substitutes for each other."""),
   ("Final Exam Scope and Format",
    r"""\begin{itemize}
    \item The final exam (Meeting 18) covers Meetings 10--17 end to end -- materials,
    landing gear, powerplant, support systems, electrical/avionics, and documentation/safety.
    \item Expect the same mix of question types as the midterm: identification/labeling,
    short answer, and applied scenario questions (recall Meeting 8's exam format review).
    \item Material from Meetings 1--9 is assumed as background knowledge but is not the
    primary focus of new final-exam questions.
    \end{itemize}"""),
   (r"Self-Assessment Checklist (Meetings 10--16)",
    r"""Before continuing, confirm you can do each of the following without notes:
    \begin{itemize}
    \item Compare aluminum, titanium, steel, and composite by strength, weight, and typical use.
    \item Explain how an oleo-pneumatic shock strut absorbs landing impact.
    \item List the sections of a gas turbine engine and the strokes of a piston engine cycle.
    \item Explain the role of fuel, hydraulic, and pneumatic systems and how they connect.
    \item Explain the pitot-static system and name its three fed instruments.
    \item Name the key required documents and safety equipment covered in Meeting 16.
    \end{itemize}"""),
   ("Extended In-Class Practice / Group Discussion",
    r"""In small groups, discuss and be ready to present:
    \begin{enumerate}
    \item Pick any real aircraft and produce a full materials-to-systems description,
    using the integration table as a checklist.
    \item Debate which topic from Meetings 10--16 the group finds most difficult, and why.
    \item Create one new practice problem of your own, combining at least two of
    Meetings 10--16, and trade with another group to solve.
    \end{enumerate}""")],
  I("Meetings 10--16 combine into a complete materials-and-systems description of any real aircraft.",
    "Most confusion comes from mixing up composite/metal damage types or confusing similar support systems.",
    "A systematic walkthrough (materials, gear, powerplant, systems, documentation) answers most integrated questions."),
  I("Write a full materials-to-systems description of an aircraft of your choice.",
    "Redo Practice 1--8 from a blank page without looking at the solutions.",
    "Prepare a one-page vocabulary sheet covering Meetings 10--16 for the final exam."))

if __name__ == "__main__":
    order = [1,2,3,4,5,6,7,8]
    results = []
    for n in order:
        title, subclo, ind, slides, summ, asg = M[n]
        tex = build_deck(COURSE, SUBJECT, SUBTITLE, REF, CLO, n, title, subclo, ind, slides, summ, asg)
        results.append(compile_meeting(COURSE, n, tex))
        print(results[-1], flush=True)
    print("DONE", COURSE)
