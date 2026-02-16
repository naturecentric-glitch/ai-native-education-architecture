#!/usr/bin/env python3
"""
NCERT K-12 Course Template Generator (Class 1–12)
===================================================
Generates seed curriculum JSON for EVERY NCERT subject from Class 1 to 12,
plus competitive exam courses (JEE, NEET).

All course data is stored as pure Python data structures.
The generator logic is the reusable TEMPLATE.

DESIGN PRINCIPLES:
  1. Minimal seed concepts (2-4 per chapter) — Gemini expands the rest
  2. Systematic: grade → subject → chapters → concepts
  3. Consistent naming: {subject}{grade} (e.g. math3, science7, hindi5)
  4. Every concept follows: (suffix, title, bloom, difficulty, [prereq_suffixes])
  5. Prereqs are "chapter_key.suffix" within the same course

Run:  python -m tools.generate_curricula

To add a new course: add seed data + entry to ALL_COURSES below, re-run.
To expand with AI:   python -m tools.expand_with_gemini --all
"""

import json
from pathlib import Path

CONTENT_DIR = Path(__file__).resolve().parent.parent / "data" / "content"


# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────

def _c(suffix, title, bloom="understand", diff=0.3, prereqs=None):
    """Shorthand concept tuple constructor."""
    return (suffix, title, bloom, diff, prereqs or [])


# ══════════════════════════════════════════════════════════════════════════════
#  CLASS 1 — Mathematics, English, Hindi, EVS
# ══════════════════════════════════════════════════════════════════════════════

MATH1_CHAPTERS = [
    ("shapes_space", "Shapes and Space", [
        _c("flat_solid", "Flat and Solid Shapes Around Us", "remember", 0.1),
        _c("patterns", "Patterns with Shapes", "understand", 0.15, ["shapes_space.flat_solid"]),
    ]),
    ("numbers_1_9", "Numbers from One to Nine", [
        _c("counting", "Counting Objects 1-9", "remember", 0.1),
        _c("number_names", "Writing Number Names", "remember", 0.1, ["numbers_1_9.counting"]),
    ]),
    ("addition", "Addition", [
        _c("add_story", "Addition Through Stories", "understand", 0.15),
        _c("add_single", "Adding Single-Digit Numbers", "apply", 0.2, ["addition.add_story"]),
    ]),
    ("subtraction", "Subtraction", [
        _c("sub_story", "Subtraction Through Stories", "understand", 0.15),
        _c("sub_single", "Subtracting Single-Digit Numbers", "apply", 0.2, ["subtraction.sub_story"]),
    ]),
    ("numbers_10_20", "Numbers from Ten to Twenty", [
        _c("teen_numbers", "Understanding Teen Numbers", "understand", 0.15),
        _c("place_value_intro", "Tens and Ones (Introduction)", "understand", 0.2, ["numbers_10_20.teen_numbers"]),
    ]),
    ("time", "Time", [
        _c("daily_routine", "Time in Daily Routine — Morning, Afternoon, Night", "understand", 0.1),
        _c("reading_clock", "Reading a Clock — Hour Hand", "apply", 0.2, ["time.daily_routine"]),
    ]),
    ("measurement", "Measurement", [
        _c("long_short", "Long and Short — Comparing Lengths", "understand", 0.1),
        _c("heavy_light", "Heavy and Light — Comparing Weights", "understand", 0.1),
    ]),
    ("numbers_21_99", "Numbers Twenty-One to Ninety-Nine", [
        _c("counting_tens", "Counting by Tens", "understand", 0.2),
        _c("two_digit_numbers", "Reading and Writing Two-Digit Numbers", "apply", 0.2, ["numbers_21_99.counting_tens"]),
    ]),
    ("money", "Money", [
        _c("coins", "Identifying Coins and Notes", "remember", 0.1),
        _c("simple_transactions", "Simple Buying and Selling", "apply", 0.2, ["money.coins"]),
    ]),
]

ENGLISH1_CHAPTERS = [
    ("alphabet", "The Alphabet", [
        _c("letters", "Recognising Letters A-Z", "remember", 0.1),
        _c("sounds", "Letter Sounds — Phonics Basics", "understand", 0.15, ["alphabet.letters"]),
    ]),
    ("words", "Simple Words", [
        _c("three_letter", "Three-Letter Words (CVC)", "apply", 0.15),
        _c("sight_words", "Common Sight Words", "remember", 0.15),
    ]),
    ("sentences", "Simple Sentences", [
        _c("reading_sentences", "Reading Simple Sentences", "understand", 0.2),
        _c("writing_sentences", "Writing Simple Sentences", "apply", 0.25, ["sentences.reading_sentences"]),
    ]),
    ("stories", "Stories and Poems", [
        _c("listening", "Listening to Stories", "understand", 0.1),
        _c("picture_reading", "Reading with Pictures", "understand", 0.15),
    ]),
]

HINDI1_CHAPTERS = [
    ("varnmala", "वर्णमाला (Hindi Alphabet)", [
        _c("swar", "स्वर — Vowels अ-औ", "remember", 0.1),
        _c("vyanjan", "व्यंजन — Consonants क-ज्ञ", "remember", 0.15, ["varnmala.swar"]),
    ]),
    ("matra", "मात्राएँ (Matras)", [
        _c("basic_matra", "Basic Matras — ा ि ी ु ू", "understand", 0.2),
        _c("matra_words", "Reading Words with Matras", "apply", 0.25, ["matra.basic_matra"]),
    ]),
    ("shabd_rachna", "शब्द रचना (Word Formation)", [
        _c("two_letter", "Two-Letter Words", "apply", 0.15),
        _c("three_letter", "Three-Letter Words", "apply", 0.2, ["shabd_rachna.two_letter"]),
    ]),
    ("kavita_kahani", "कविता और कहानी", [
        _c("rhymes", "Hindi Rhymes and Poems", "understand", 0.1),
        _c("stories", "Simple Hindi Stories", "understand", 0.15),
    ]),
]

EVS1_CHAPTERS = [
    ("my_family", "My Family", [
        _c("family_members", "Family Members and Relationships", "understand", 0.1),
        _c("helping_at_home", "Helping at Home", "understand", 0.1),
    ]),
    ("my_body", "My Body", [
        _c("body_parts", "Body Parts and Their Functions", "remember", 0.1),
        _c("good_habits", "Good Habits — Hygiene and Health", "understand", 0.15, ["my_body.body_parts"]),
    ]),
    ("plants_around", "Plants Around Us", [
        _c("types_plants", "Types of Plants — Big and Small", "understand", 0.1),
        _c("parts_plant", "Parts of a Plant", "remember", 0.1),
    ]),
    ("animals_around", "Animals Around Us", [
        _c("pet_wild", "Pet Animals and Wild Animals", "understand", 0.1),
        _c("animal_homes", "Homes of Animals", "understand", 0.1),
    ]),
    ("food_we_eat", "Food We Eat", [
        _c("healthy_food", "Healthy Food and Junk Food", "understand", 0.1),
        _c("food_sources", "Where Does Our Food Come From?", "understand", 0.15),
    ]),
]

# ══════════════════════════════════════════════════════════════════════════════
#  CLASS 2 — Mathematics, English, Hindi, EVS
# ══════════════════════════════════════════════════════════════════════════════

MATH2_CHAPTERS = [
    ("numbers_100", "Numbers Up to 100", [
        _c("counting_100", "Counting to 100", "remember", 0.1),
        _c("comparing", "Comparing Numbers — Greater, Smaller", "understand", 0.15, ["numbers_100.counting_100"]),
        _c("ordering", "Ordering Numbers", "apply", 0.2, ["numbers_100.comparing"]),
    ]),
    ("addition_sub", "Addition and Subtraction", [
        _c("add_two_digit", "Adding Two-Digit Numbers", "apply", 0.2),
        _c("sub_two_digit", "Subtracting Two-Digit Numbers", "apply", 0.2),
        _c("word_problems", "Word Problems on Addition and Subtraction", "apply", 0.25, ["addition_sub.add_two_digit", "addition_sub.sub_two_digit"]),
    ]),
    ("shapes", "Shapes and Patterns", [
        _c("2d_shapes", "Circle, Square, Triangle, Rectangle", "remember", 0.1),
        _c("patterns_repeat", "Repeating Patterns", "understand", 0.15, ["shapes.2d_shapes"]),
    ]),
    ("measurement", "Measurement", [
        _c("length", "Measuring Length — Hand Span, Foot", "apply", 0.15),
        _c("capacity", "Full, Half-Full, Empty", "understand", 0.1),
    ]),
    ("time_calendar", "Time and Calendar", [
        _c("days_months", "Days of Week and Months of Year", "remember", 0.1),
        _c("reading_clock2", "Reading Clock — Hours and Half-Hours", "apply", 0.2, ["time_calendar.days_months"]),
    ]),
    ("money2", "Money", [
        _c("counting_money", "Counting Coins and Notes", "apply", 0.15),
        _c("making_amounts", "Making Amounts Using Different Coins", "apply", 0.2, ["money2.counting_money"]),
    ]),
    ("multiplication_intro", "Introduction to Multiplication", [
        _c("groups_of", "Equal Groups — Groups of 2, 3, 5", "understand", 0.2),
        _c("skip_counting", "Skip Counting", "apply", 0.2, ["multiplication_intro.groups_of"]),
    ]),
]

ENGLISH2_CHAPTERS = [
    ("reading", "Reading Skills", [
        _c("short_passages", "Reading Short Passages", "understand", 0.15),
        _c("comprehension", "Answering Questions from Passage", "apply", 0.2, ["reading.short_passages"]),
    ]),
    ("grammar_basics", "Basic Grammar", [
        _c("nouns", "Nouns — Naming Words", "understand", 0.15),
        _c("verbs", "Verbs — Action Words", "understand", 0.15),
        _c("singular_plural", "Singular and Plural", "apply", 0.2, ["grammar_basics.nouns"]),
    ]),
    ("writing2", "Writing", [
        _c("picture_comp", "Picture Composition", "apply", 0.2),
        _c("short_paragraph", "Writing Short Paragraphs", "apply", 0.25, ["writing2.picture_comp"]),
    ]),
    ("vocabulary", "Vocabulary Building", [
        _c("opposites", "Opposites (Antonyms)", "understand", 0.15),
        _c("rhyming_words", "Rhyming Words", "understand", 0.15),
    ]),
]

HINDI2_CHAPTERS = [
    ("padhan", "पढ़ना (Reading)", [
        _c("simple_passages", "Simple Hindi Passages", "understand", 0.15),
        _c("comprehension", "Comprehension Questions", "apply", 0.2, ["padhan.simple_passages"]),
    ]),
    ("lekhan", "लेखन (Writing)", [
        _c("shabdh_lekhan", "Word Writing Practice", "apply", 0.15),
        _c("vakya_rachna", "Sentence Formation", "apply", 0.2, ["lekhan.shabdh_lekhan"]),
    ]),
    ("vyakaran_basics", "बुनियादी व्याकरण", [
        _c("sangya", "संज्ञा — Nouns", "understand", 0.15),
        _c("sarvanam", "सर्वनाम — Pronouns", "understand", 0.15),
        _c("vachan", "वचन — Singular and Plural", "apply", 0.2, ["vyakaran_basics.sangya"]),
    ]),
]

EVS2_CHAPTERS = [
    ("my_neighbourhood", "My Neighbourhood", [
        _c("places", "Places in My Neighbourhood", "understand", 0.1),
        _c("helpers", "Community Helpers", "understand", 0.1),
    ]),
    ("plants2", "Plants and Trees", [
        _c("importance", "Importance of Plants", "understand", 0.15),
        _c("growth", "How Plants Grow — Seed to Plant", "understand", 0.15),
    ]),
    ("animals2", "Animals and Birds", [
        _c("habitats", "Habitats — Land, Water, Air", "understand", 0.15),
        _c("food_animals", "What Animals Eat", "understand", 0.15),
    ]),
    ("water_air", "Water and Air", [
        _c("uses_water", "Uses of Water", "understand", 0.1),
        _c("air_importance", "Importance of Clean Air", "understand", 0.1),
    ]),
    ("safety", "Safety", [
        _c("road_safety", "Road Safety Rules", "understand", 0.1),
        _c("safety_at_home", "Safety at Home", "understand", 0.1),
    ]),
]

# ══════════════════════════════════════════════════════════════════════════════
#  CLASS 3 — Mathematics, English, Hindi, EVS
# ══════════════════════════════════════════════════════════════════════════════

MATH3_CHAPTERS = [
    ("numbers_1000", "Numbers Up to 1000", [
        _c("place_value", "Place Value — Hundreds, Tens, Ones", "understand", 0.2),
        _c("expanded_form", "Expanded Form of Numbers", "apply", 0.2, ["numbers_1000.place_value"]),
        _c("comparing_ordering", "Comparing and Ordering 3-Digit Numbers", "apply", 0.25, ["numbers_1000.expanded_form"]),
    ]),
    ("addition_sub3", "Addition and Subtraction (3-digit)", [
        _c("add_carry", "Addition with Carrying", "apply", 0.25),
        _c("sub_borrow", "Subtraction with Borrowing", "apply", 0.25),
        _c("word_problems3", "Word Problems", "apply", 0.3, ["addition_sub3.add_carry", "addition_sub3.sub_borrow"]),
    ]),
    ("multiplication3", "Multiplication", [
        _c("tables_2_10", "Multiplication Tables 2 to 10", "remember", 0.2),
        _c("multiply_2digit", "Multiplying 2-Digit by 1-Digit", "apply", 0.3, ["multiplication3.tables_2_10"]),
    ]),
    ("division3", "Division", [
        _c("sharing_equally", "Equal Sharing — Division Concept", "understand", 0.2),
        _c("division_facts", "Division Facts from Multiplication", "apply", 0.25, ["division3.sharing_equally"]),
    ]),
    ("fractions_intro", "Fractions (Introduction)", [
        _c("half_quarter", "Half, Quarter, Three-Quarters", "understand", 0.2),
        _c("fraction_picture", "Fractions from Pictures", "understand", 0.2, ["fractions_intro.half_quarter"]),
    ]),
    ("geometry3", "Geometry", [
        _c("lines_curves", "Straight Lines, Curved Lines", "understand", 0.15),
        _c("shapes_properties", "Properties of Basic Shapes", "understand", 0.2, ["geometry3.lines_curves"]),
    ]),
    ("measurement3", "Measurement", [
        _c("length_cm_m", "Length in Centimetres and Metres", "apply", 0.2),
        _c("weight_kg", "Weight in Kilograms and Grams", "apply", 0.2),
    ]),
    ("money3", "Money", [
        _c("bills", "Making Bills and Calculating Change", "apply", 0.25),
        _c("money_word_problems", "Word Problems on Money", "apply", 0.3, ["money3.bills"]),
    ]),
    ("time3", "Time", [
        _c("minutes", "Reading Clock — Hours and Minutes", "apply", 0.2),
        _c("duration", "Duration of Events", "apply", 0.25, ["time3.minutes"]),
    ]),
    ("data_handling3", "Data Handling", [
        _c("tally_marks", "Recording Data with Tally Marks", "apply", 0.15),
        _c("pictograph", "Reading and Making Pictographs", "apply", 0.2, ["data_handling3.tally_marks"]),
    ]),
]

ENGLISH3_CHAPTERS = [
    ("reading3", "Reading Comprehension", [
        _c("stories_poems", "Reading Stories and Poems", "understand", 0.2),
        _c("answering_questions", "Answering Questions — Who, What, Where, When", "apply", 0.25, ["reading3.stories_poems"]),
    ]),
    ("grammar3", "Grammar", [
        _c("articles", "Articles — A, An, The", "apply", 0.2),
        _c("pronouns", "Pronouns — He, She, It, They", "understand", 0.2),
        _c("tenses_intro", "Present and Past Tense (Introduction)", "apply", 0.25, ["grammar3.pronouns"]),
    ]),
    ("writing3", "Writing Skills", [
        _c("paragraph", "Paragraph Writing", "apply", 0.25),
        _c("informal_letter", "Informal Letter Writing", "apply", 0.3, ["writing3.paragraph"]),
    ]),
    ("vocabulary3", "Vocabulary", [
        _c("synonyms", "Synonyms", "understand", 0.2),
        _c("homophones", "Homophones — Words that Sound Alike", "understand", 0.2),
    ]),
]

HINDI3_CHAPTERS = [
    ("padhan3", "पढ़ना — Reading", [
        _c("stories", "Hindi Stories with Comprehension", "understand", 0.2),
        _c("poetry", "Hindi Poetry", "understand", 0.2),
    ]),
    ("vyakaran3", "व्याकरण — Grammar", [
        _c("ling", "लिंग — Gender", "understand", 0.2),
        _c("vachan3", "वचन — Number", "understand", 0.2),
        _c("kaal_intro", "काल — Tense Introduction", "understand", 0.25, ["vyakaran3.ling"]),
    ]),
    ("lekhan3", "लेखन — Writing", [
        _c("nibandh", "Short Essay Writing", "apply", 0.25),
        _c("patra_lekhan", "Letter Writing", "apply", 0.3, ["lekhan3.nibandh"]),
    ]),
]

EVS3_CHAPTERS = [
    ("family_friends", "Family and Friends", [
        _c("relationships", "Relationships and Responsibilities", "understand", 0.15),
        _c("festivals", "Festivals We Celebrate", "understand", 0.1),
    ]),
    ("food3", "Food", [
        _c("food_variety", "Food Variety in India", "understand", 0.15),
        _c("cooking_methods", "Different Ways of Cooking", "understand", 0.15),
    ]),
    ("shelter", "Shelter", [
        _c("types_houses", "Different Types of Houses", "understand", 0.15),
        _c("materials_used", "Materials Used in Building Houses", "understand", 0.15),
    ]),
    ("travel", "Travel", [
        _c("means_transport", "Means of Transport — Land, Water, Air", "understand", 0.15),
        _c("maps_directions", "Maps and Directions", "understand", 0.2, ["travel.means_transport"]),
    ]),
    ("things_we_make", "Things We Make and Do", [
        _c("materials", "Natural and Man-Made Materials", "understand", 0.15),
        _c("crafts", "Indian Crafts and Artisans", "understand", 0.15),
    ]),
]

# ══════════════════════════════════════════════════════════════════════════════
#  CLASS 4 — Mathematics, English, Hindi, EVS
# ══════════════════════════════════════════════════════════════════════════════

MATH4_CHAPTERS = [
    ("large_numbers", "Large Numbers", [
        _c("place_value4", "Place Value — Up to Ten Thousand", "understand", 0.2),
        _c("indian_system", "Indian Number System", "understand", 0.25, ["large_numbers.place_value4"]),
    ]),
    ("addition_sub4", "Addition and Subtraction (Large Numbers)", [
        _c("add_4digit", "Adding 4-Digit Numbers", "apply", 0.25),
        _c("sub_4digit", "Subtracting 4-Digit Numbers", "apply", 0.25),
    ]),
    ("multiplication4", "Multiplication", [
        _c("multiply_2by2", "Multiplying 2-Digit by 2-Digit", "apply", 0.3),
        _c("multiply_word", "Word Problems on Multiplication", "apply", 0.35, ["multiplication4.multiply_2by2"]),
    ]),
    ("division4", "Division", [
        _c("long_division", "Long Division — 2-Digit by 1-Digit", "apply", 0.3),
        _c("division_word", "Word Problems on Division", "apply", 0.35, ["division4.long_division"]),
    ]),
    ("factors_multiples", "Factors and Multiples", [
        _c("factors", "Factors of a Number", "understand", 0.25),
        _c("multiples", "Multiples of a Number", "understand", 0.25),
    ]),
    ("fractions4", "Fractions", [
        _c("types_fractions", "Like, Unlike, Proper, Improper Fractions", "understand", 0.25),
        _c("equivalent", "Equivalent Fractions", "apply", 0.3, ["fractions4.types_fractions"]),
        _c("compare_fractions", "Comparing Fractions", "apply", 0.3, ["fractions4.equivalent"]),
    ]),
    ("decimals_intro", "Decimals (Introduction)", [
        _c("tenths", "Tenths — Place Value of Decimals", "understand", 0.25),
        _c("decimal_money", "Decimals in Money", "apply", 0.3, ["decimals_intro.tenths"]),
    ]),
    ("geometry4", "Geometry", [
        _c("angles_intro", "Introduction to Angles", "understand", 0.2),
        _c("symmetry", "Lines of Symmetry", "understand", 0.2),
        _c("perimeter", "Perimeter of Simple Shapes", "apply", 0.25, ["geometry4.angles_intro"]),
    ]),
    ("measurement4", "Measurement", [
        _c("conversion", "Converting Units — mm, cm, m, km", "apply", 0.25),
        _c("area_intro", "Introduction to Area — Counting Squares", "understand", 0.25),
    ]),
    ("data_handling4", "Data Handling", [
        _c("bar_graphs", "Reading and Drawing Bar Graphs", "apply", 0.25),
        _c("tables", "Frequency Tables", "apply", 0.2),
    ]),
    ("patterns4", "Patterns", [
        _c("number_patterns", "Number Patterns and Sequences", "understand", 0.2),
        _c("magic_squares", "Magic Squares and Puzzles", "apply", 0.3, ["patterns4.number_patterns"]),
    ]),
]

ENGLISH4_CHAPTERS = [
    ("reading4", "Reading and Comprehension", [
        _c("unseen_passage", "Unseen Passage — Factual", "apply", 0.25),
        _c("poetry4", "Poetry Appreciation", "understand", 0.2),
    ]),
    ("grammar4", "Grammar", [
        _c("tenses4", "Tenses — Past, Present, Future", "apply", 0.25),
        _c("adjectives", "Adjectives — Describing Words", "understand", 0.2),
        _c("prepositions", "Prepositions — in, on, at, under, between", "apply", 0.25),
    ]),
    ("writing4", "Writing Skills", [
        _c("story_writing", "Story Writing from Outlines", "create", 0.3),
        _c("diary_entry", "Diary Entry", "apply", 0.3),
    ]),
    ("vocabulary4", "Vocabulary", [
        _c("prefixes_suffixes", "Prefixes and Suffixes", "understand", 0.25),
        _c("idioms", "Common Idioms and Phrases", "understand", 0.25),
    ]),
]

HINDI4_CHAPTERS = [
    ("gadya", "गद्य — Prose", [
        _c("stories4", "Hindi Stories with Questions", "understand", 0.2),
        _c("comprehension4", "Comprehension from Stories", "apply", 0.25, ["gadya.stories4"]),
    ]),
    ("padya", "पद्य — Poetry", [
        _c("poems4", "Hindi Poems", "understand", 0.2),
        _c("bhav_arth", "Meaning and Feelings in Poems", "analyze", 0.25, ["padya.poems4"]),
    ]),
    ("vyakaran4", "व्याकरण — Grammar", [
        _c("visheshan", "विशेषण — Adjectives", "understand", 0.2),
        _c("kriya", "क्रिया — Verbs", "understand", 0.2),
        _c("vakya_bhed", "वाक्य भेद — Types of Sentences", "understand", 0.25),
    ]),
    ("lekhan4", "लेखन — Writing", [
        _c("anuched", "अनुच्छेद लेखन — Paragraph Writing", "apply", 0.25),
        _c("chitrakatha", "चित्रकथा — Picture Story", "create", 0.3, ["lekhan4.anuched"]),
    ]),
]

EVS4_CHAPTERS = [
    ("food_agriculture", "Food and Agriculture", [
        _c("crops", "Crops — Kharif and Rabi", "understand", 0.2),
        _c("farmer_life", "Life of a Farmer", "understand", 0.2),
    ]),
    ("water4", "Water", [
        _c("water_sources", "Sources of Water", "understand", 0.15),
        _c("water_conservation", "Water Conservation", "apply", 0.2, ["water4.water_sources"]),
    ]),
    ("our_environment", "Our Environment", [
        _c("living_nonliving", "Living and Non-Living Things", "understand", 0.15),
        _c("deforestation", "Effects of Deforestation", "understand", 0.2),
    ]),
    ("our_body", "Our Body", [
        _c("organ_systems", "Organ Systems — Digestive, Respiratory", "understand", 0.2),
        _c("diseases", "Common Diseases and Prevention", "understand", 0.2),
    ]),
    ("maps_globe", "Maps and Globe", [
        _c("directions", "Directions — North, South, East, West", "understand", 0.15),
        _c("reading_maps", "Reading Simple Maps", "apply", 0.2, ["maps_globe.directions"]),
    ]),
]

# ══════════════════════════════════════════════════════════════════════════════
#  CLASS 5 — Mathematics, English, Hindi, EVS
# ══════════════════════════════════════════════════════════════════════════════

MATH5_CHAPTERS = [
    ("large_numbers5", "Large Numbers (Lakhs and Beyond)", [
        _c("lakhs", "Place Value Up to Lakhs", "understand", 0.25),
        _c("roman_numerals", "Roman Numerals", "apply", 0.25),
        _c("estimation", "Estimation and Rounding", "apply", 0.3, ["large_numbers5.lakhs"]),
    ]),
    ("operations5", "Operations on Large Numbers", [
        _c("add_sub_large", "Addition and Subtraction of Large Numbers", "apply", 0.3),
        _c("multiply_large", "Multiplication of 3-Digit by 2-Digit", "apply", 0.3),
        _c("divide_large", "Division of 4-Digit by 2-Digit", "apply", 0.35, ["operations5.multiply_large"]),
    ]),
    ("fractions5", "Fractions", [
        _c("add_sub_fractions", "Addition and Subtraction of Fractions", "apply", 0.3),
        _c("mixed_numbers", "Mixed Numbers and Improper Fractions", "apply", 0.3),
    ]),
    ("decimals5", "Decimals", [
        _c("decimal_place_value", "Decimal Place Value — Tenths, Hundredths", "understand", 0.25),
        _c("add_sub_decimals", "Addition and Subtraction of Decimals", "apply", 0.3, ["decimals5.decimal_place_value"]),
    ]),
    ("geometry5", "Geometry", [
        _c("angles5", "Measuring Angles with Protractor", "apply", 0.25),
        _c("triangles_quad", "Triangles and Quadrilaterals — Properties", "understand", 0.3, ["geometry5.angles5"]),
        _c("circles", "Circle — Radius, Diameter, Circumference", "understand", 0.3),
    ]),
    ("area_perimeter5", "Area and Perimeter", [
        _c("perimeter5", "Perimeter of Rectangles and Irregular Shapes", "apply", 0.25),
        _c("area5", "Area of Rectangle and Square", "apply", 0.3, ["area_perimeter5.perimeter5"]),
    ]),
    ("patterns5", "Patterns and Sequences", [
        _c("growing_patterns", "Growing Number Patterns", "understand", 0.25),
        _c("rules", "Finding Rules in Patterns", "apply", 0.3, ["patterns5.growing_patterns"]),
    ]),
    ("data_handling5", "Data Handling", [
        _c("bar_graph5", "Bar Graphs — Drawing and Interpreting", "apply", 0.25),
        _c("line_graph_intro", "Introduction to Line Graphs", "understand", 0.25),
    ]),
    ("volume5", "Volume", [
        _c("volume_intro", "Volume — Counting Unit Cubes", "understand", 0.25),
        _c("volume_cuboid", "Volume of Cuboid", "apply", 0.3, ["volume5.volume_intro"]),
    ]),
]

ENGLISH5_CHAPTERS = [
    ("reading5", "Reading and Comprehension", [
        _c("factual", "Factual and Descriptive Passages", "apply", 0.25),
        _c("literary", "Literary — Stories and Poems", "understand", 0.25),
    ]),
    ("grammar5", "Grammar", [
        _c("tenses5", "Tenses — Simple, Continuous, Perfect", "apply", 0.3),
        _c("modals", "Modals — can, could, may, should", "apply", 0.3),
        _c("punctuation", "Punctuation — Full Stop, Comma, Question Mark, Apostrophe", "apply", 0.25),
    ]),
    ("writing5", "Writing Skills", [
        _c("essay5", "Essay Writing — Descriptive", "create", 0.3),
        _c("letter5", "Formal and Informal Letters", "apply", 0.3),
        _c("notice", "Notice Writing", "apply", 0.3),
    ]),
    ("vocabulary5", "Vocabulary and Word Power", [
        _c("word_meanings", "Contextual Word Meanings", "understand", 0.25),
        _c("one_word", "One Word Substitution", "apply", 0.3),
    ]),
]

HINDI5_CHAPTERS = [
    ("gadya5", "गद्य — Prose", [
        _c("stories5", "Hindi Stories with Deep Comprehension", "understand", 0.25),
        _c("passage_answer", "Passage-Based Questions", "apply", 0.3, ["gadya5.stories5"]),
    ]),
    ("padya5", "पद्य — Poetry", [
        _c("poems5", "Hindi Poems with Explanation", "understand", 0.25),
        _c("bhavarth", "भावार्थ — Meaning and Interpretation", "analyze", 0.3, ["padya5.poems5"]),
    ]),
    ("vyakaran5", "व्याकरण — Grammar", [
        _c("sandhi", "संधि — Basic Word Joining", "understand", 0.3),
        _c("upsarg_pratyay", "उपसर्ग और प्रत्यय — Prefixes and Suffixes", "understand", 0.3),
        _c("muhavare", "मुहावरे — Idioms", "apply", 0.3),
    ]),
    ("lekhan5", "लेखन — Writing", [
        _c("nibandh5", "निबंध लेखन — Essay Writing", "create", 0.3),
        _c("patra5", "पत्र लेखन — Letter Writing", "apply", 0.3),
    ]),
]

EVS5_CHAPTERS = [
    ("super_senses", "Super Senses", [
        _c("animal_senses", "How Animals See, Hear, Smell", "understand", 0.2),
        _c("night_animals", "Animals That Are Active at Night", "understand", 0.2),
    ]),
    ("seeds_seeds", "Seeds and Seeds", [
        _c("seed_dispersal", "How Seeds Travel", "understand", 0.2),
        _c("germination", "Germination — Seed to Plant", "understand", 0.2),
    ]),
    ("experiments_water", "Experiments with Water", [
        _c("dissolving", "Things That Dissolve in Water", "apply", 0.2),
        _c("evaporation", "Evaporation and Condensation", "apply", 0.25, ["experiments_water.dissolving"]),
    ]),
    ("mapping", "Mapping Our Neighbourhood", [
        _c("symbols_maps", "Symbols on Maps", "understand", 0.2),
        _c("scale_distance", "Scale and Distance", "apply", 0.25, ["mapping.symbols_maps"]),
    ]),
    ("social_topics", "Social Topics", [
        _c("who_does_what", "Who Does What — Division of Labour", "understand", 0.2),
        _c("like_unlike", "Similarities and Differences Among People", "understand", 0.2),
    ]),
]

# ══════════════════════════════════════════════════════════════════════════════
#  CLASS 6-12 SUBJECTS
#  (Subjects that already existed in the previous generator — re-included
#   with identical seeds for continuity. Also adding NEW missing subjects.)
# ══════════════════════════════════════════════════════════════════════════════

# ── Math 6 (seed data — original math6 was created separately, this re-seeds) ─
MATH6_CHAPTERS = [
    ("knowing_numbers", "Knowing Our Numbers", [
        _c("place_value6", "Place Value System — Lakhs and Crores", "understand", 0.2),
        _c("comparing6", "Comparing and Ordering Large Numbers", "apply", 0.25, ["knowing_numbers.place_value6"]),
        _c("estimation6", "Estimation and Rounding Off", "apply", 0.3, ["knowing_numbers.comparing6"]),
    ]),
    ("whole_numbers", "Whole Numbers", [
        _c("properties_wn", "Properties of Whole Numbers", "understand", 0.25),
        _c("number_line", "Number Line Operations", "apply", 0.3, ["whole_numbers.properties_wn"]),
    ]),
    ("playing_numbers", "Playing with Numbers", [
        _c("divisibility", "Divisibility Rules", "apply", 0.3),
        _c("hcf_lcm", "HCF and LCM", "apply", 0.35, ["playing_numbers.divisibility"]),
    ]),
    ("basic_geometry", "Basic Geometrical Ideas", [
        _c("point_line_plane", "Points, Lines, Line Segments, Rays", "understand", 0.2),
        _c("curves_polygons", "Curves, Polygons and Angles", "understand", 0.25, ["basic_geometry.point_line_plane"]),
    ]),
    ("understanding_shapes", "Understanding Elementary Shapes", [
        _c("measuring_angles", "Measuring Angles", "apply", 0.25),
        _c("types_triangles6", "Types of Triangles and Quadrilaterals", "understand", 0.3, ["understanding_shapes.measuring_angles"]),
        _c("3d_shapes", "3D Shapes — Faces, Edges, Vertices", "understand", 0.3),
    ]),
    ("integers6", "Integers", [
        _c("intro_integers", "Introduction to Negative Numbers", "understand", 0.25),
        _c("add_sub_integers", "Addition and Subtraction of Integers", "apply", 0.3, ["integers6.intro_integers"]),
    ]),
    ("fractions6", "Fractions", [
        _c("types6", "Types of Fractions", "understand", 0.25),
        _c("operations6", "Comparing, Adding, Subtracting Fractions", "apply", 0.3, ["fractions6.types6"]),
    ]),
    ("decimals6", "Decimals", [
        _c("decimal_concepts", "Decimal Concepts and Place Value", "understand", 0.25),
        _c("decimal_operations", "Operations on Decimals", "apply", 0.3, ["decimals6.decimal_concepts"]),
    ]),
    ("data_handling6", "Data Handling", [
        _c("pictograph6", "Pictographs and Bar Graphs", "apply", 0.25),
        _c("mean6", "Mean (Average)", "apply", 0.3, ["data_handling6.pictograph6"]),
    ]),
    ("mensuration6", "Mensuration", [
        _c("perimeter6", "Perimeter of Common Shapes", "apply", 0.25),
        _c("area6", "Area of Rectangle, Square, Triangle", "apply", 0.3, ["mensuration6.perimeter6"]),
    ]),
    ("algebra6", "Algebra", [
        _c("variables6", "Use of Variables and Constants", "understand", 0.25),
        _c("expressions6", "Algebraic Expressions", "apply", 0.3, ["algebra6.variables6"]),
        _c("equations6", "Simple Equations", "apply", 0.35, ["algebra6.expressions6"]),
    ]),
    ("ratio_proportion", "Ratio and Proportion", [
        _c("ratio6", "Concept of Ratio", "understand", 0.25),
        _c("proportion6", "Proportion and Unitary Method", "apply", 0.3, ["ratio_proportion.ratio6"]),
    ]),
    ("symmetry6", "Symmetry", [
        _c("line_symmetry", "Line of Symmetry", "understand", 0.2),
        _c("symmetry_figures", "Symmetry in Common Figures", "apply", 0.25, ["symmetry6.line_symmetry"]),
    ]),
    ("practical_geometry6", "Practical Geometry", [
        _c("constructions6", "Constructing Lines, Angles, Perpendiculars", "apply", 0.3),
        _c("circle_construction", "Constructing Circles", "apply", 0.25),
    ]),
]

# ── Math 7 ──
MATH7_CHAPTERS = [
    ("integers", "Integers", [
        _c("properties", "Properties of Integers", "understand", 0.25),
        _c("add_sub", "Addition and Subtraction of Integers", "apply", 0.3, ["integers.properties"]),
        _c("mul_div", "Multiplication and Division of Integers", "apply", 0.35, ["integers.add_sub"]),
    ]),
    ("fractions_decimals", "Fractions and Decimals", [
        _c("mul_fractions", "Multiplication of Fractions", "apply", 0.3),
        _c("div_fractions", "Division of Fractions", "apply", 0.35, ["fractions_decimals.mul_fractions"]),
        _c("operations_decimals", "Operations on Decimals", "apply", 0.3),
    ]),
    ("data_handling", "Data Handling", [
        _c("arithmetic_mean", "Arithmetic Mean", "apply", 0.3),
        _c("bar_graphs", "Bar Graphs", "apply", 0.3),
        _c("probability_intro", "Chance and Probability", "understand", 0.35, ["data_handling.bar_graphs"]),
    ]),
    ("simple_equations", "Simple Equations", [
        _c("solving_equations", "Solving Simple Equations", "apply", 0.35),
        _c("word_problems_eq", "Word Problems with Equations", "apply", 0.4, ["simple_equations.solving_equations"]),
    ]),
    ("lines_angles", "Lines and Angles", [
        _c("related_angles", "Complementary and Supplementary Angles", "understand", 0.25),
        _c("parallel_transversal", "Parallel Lines and Transversal", "apply", 0.4, ["lines_angles.related_angles"]),
    ]),
    ("triangles", "The Triangle and Its Properties", [
        _c("angle_sum", "Angle Sum Property", "understand", 0.3),
        _c("exterior_angle", "Exterior Angle Property", "apply", 0.35, ["triangles.angle_sum"]),
        _c("pythagoras_intro", "Pythagoras Property (Introduction)", "understand", 0.4, ["triangles.angle_sum"]),
    ]),
    ("congruence", "Congruence of Triangles", [
        _c("criteria_congruence", "Criteria for Congruence (SSS, SAS, ASA, RHS)", "apply", 0.4),
    ]),
    ("comparing_quantities", "Comparing Quantities", [
        _c("percentage", "Percentage", "apply", 0.3),
        _c("profit_loss", "Profit, Loss and Discount", "apply", 0.4, ["comparing_quantities.percentage"]),
        _c("simple_interest", "Simple Interest", "apply", 0.4, ["comparing_quantities.percentage"]),
    ]),
    ("rational_numbers", "Rational Numbers", [
        _c("intro_rationals", "Introduction to Rational Numbers", "understand", 0.3),
        _c("operations_rationals", "Operations on Rational Numbers", "apply", 0.4, ["rational_numbers.intro_rationals"]),
    ]),
    ("perimeter_area", "Perimeter and Area", [
        _c("area_parallelogram", "Area of Parallelogram and Triangle", "apply", 0.3),
        _c("area_circle", "Circumference and Area of Circle", "apply", 0.4, ["perimeter_area.area_parallelogram"]),
    ]),
    ("algebraic_expressions", "Algebraic Expressions", [
        _c("terms_coefficients", "Terms, Factors and Coefficients", "understand", 0.25),
        _c("add_sub_expressions", "Adding and Subtracting Algebraic Expressions", "apply", 0.35, ["algebraic_expressions.terms_coefficients"]),
    ]),
    ("exponents", "Exponents and Powers", [
        _c("laws_exponents", "Laws of Exponents", "apply", 0.35),
        _c("standard_form", "Standard Form of Large Numbers", "apply", 0.3, ["exponents.laws_exponents"]),
    ]),
    ("symmetry7", "Symmetry", [
        _c("rotational_symmetry", "Rotational Symmetry", "understand", 0.3),
    ]),
    ("solid_shapes", "Visualising Solid Shapes", [
        _c("nets_solids", "Nets of 3D Shapes", "understand", 0.3),
        _c("cross_sections", "Cross Sections", "analyze", 0.35, ["solid_shapes.nets_solids"]),
    ]),
]

# ── Math 8-12 seeds (compact — kept shorter for Gemini expansion) ──
MATH8_CHAPTERS = [
    ("rational_numbers", "Rational Numbers", [
        _c("properties", "Properties of Rational Numbers", "understand", 0.3),
        _c("between_rationals", "Rational Numbers Between Two Rationals", "apply", 0.35, ["rational_numbers.properties"]),
    ]),
    ("linear_equations", "Linear Equations in One Variable", [
        _c("solving_linear", "Solving Linear Equations", "apply", 0.3),
        _c("word_problems", "Applications of Linear Equations", "apply", 0.45, ["linear_equations.solving_linear"]),
    ]),
    ("quadrilaterals", "Understanding Quadrilaterals", [
        _c("angle_sum_quad", "Angle Sum Property of Quadrilaterals", "apply", 0.3),
        _c("special_quads", "Properties of Parallelogram, Rhombus, Trapezium", "analyze", 0.4, ["quadrilaterals.angle_sum_quad"]),
    ]),
    ("data_handling8", "Data Handling", [
        _c("pie_charts", "Pie Charts", "apply", 0.35),
        _c("probability", "Probability — Equally Likely Outcomes", "apply", 0.4),
    ]),
    ("squares_roots", "Squares and Square Roots", [
        _c("perfect_squares", "Perfect Squares and Properties", "understand", 0.3),
        _c("finding_sqrt", "Finding Square Roots", "apply", 0.4, ["squares_roots.perfect_squares"]),
    ]),
    ("cubes_roots", "Cubes and Cube Roots", [
        _c("cube_root", "Perfect Cubes and Cube Roots", "apply", 0.4),
    ]),
    ("comparing_quantities8", "Comparing Quantities", [
        _c("compound_interest", "Compound Interest", "apply", 0.4),
        _c("discount_tax", "Discount, Tax and Sales Tax", "apply", 0.35),
    ]),
    ("algebraic_identities", "Algebraic Expressions and Identities", [
        _c("multiplication", "Multiplication of Polynomials", "apply", 0.35),
        _c("standard_identities", "Standard Algebraic Identities", "apply", 0.4, ["algebraic_identities.multiplication"]),
    ]),
    ("mensuration8", "Mensuration", [
        _c("area_trapezium", "Area of Trapezium and Polygon", "apply", 0.35),
        _c("surface_area_volume", "Surface Area and Volume of Cube, Cuboid, Cylinder", "apply", 0.45, ["mensuration8.area_trapezium"]),
    ]),
    ("exponents_powers8", "Exponents and Powers", [
        _c("negative_exponents", "Negative Exponents and Laws", "apply", 0.35),
    ]),
    ("proportion", "Direct and Inverse Proportions", [
        _c("direct_inverse", "Direct and Inverse Proportion", "apply", 0.3),
    ]),
    ("factorisation", "Factorisation", [
        _c("using_identities", "Factorisation Using Identities", "apply", 0.4),
    ]),
    ("graphs8", "Introduction to Graphs", [
        _c("linear_graphs", "Linear Graphs and Plotting Points", "apply", 0.35),
    ]),
]

MATH9_CHAPTERS = [
    ("number_systems", "Number Systems", [
        _c("irrational_numbers", "Irrational Numbers and Real Number Line", "understand", 0.35),
        _c("laws_radicals", "Laws of Radicals and Exponents", "apply", 0.45, ["number_systems.irrational_numbers"]),
    ]),
    ("polynomials", "Polynomials", [
        _c("zeroes_polynomial", "Zeroes and Factoring Polynomials", "apply", 0.4),
        _c("remainder_factor", "Remainder and Factor Theorem", "apply", 0.5, ["polynomials.zeroes_polynomial"]),
    ]),
    ("coordinate_geometry", "Coordinate Geometry", [
        _c("cartesian_plane", "Cartesian Plane and Plotting Points", "apply", 0.35),
    ]),
    ("linear_eq_two_var", "Linear Equations in Two Variables", [
        _c("graphical_solution", "Graphical Representation of Linear Equations", "apply", 0.4),
    ]),
    ("euclid_geometry", "Introduction to Euclid's Geometry", [
        _c("axioms_postulates", "Euclid's Axioms and Postulates", "understand", 0.3),
    ]),
    ("lines_angles9", "Lines and Angles", [
        _c("parallel_transversal", "Parallel Lines and Transversal", "apply", 0.4),
        _c("angle_sum_triangle", "Angle Sum Property of Triangle", "apply", 0.35, ["lines_angles9.parallel_transversal"]),
    ]),
    ("triangles9", "Triangles", [
        _c("congruence_criteria", "Congruence Criteria (SAS, ASA, SSS, RHS)", "apply", 0.4),
        _c("triangle_inequalities", "Inequalities in Triangles", "analyze", 0.45, ["triangles9.congruence_criteria"]),
    ]),
    ("quadrilaterals9", "Quadrilaterals", [
        _c("properties_parallelogram", "Properties of Parallelogram", "apply", 0.4),
        _c("midpoint_theorem", "Mid-Point Theorem", "apply", 0.45, ["quadrilaterals9.properties_parallelogram"]),
    ]),
    ("circles9", "Circles", [
        _c("angle_subtended", "Angle Subtended by a Chord", "apply", 0.4),
        _c("cyclic_quadrilateral", "Cyclic Quadrilateral", "apply", 0.45, ["circles9.angle_subtended"]),
    ]),
    ("constructions9", "Constructions", [
        _c("construct_triangle", "Construction of Triangles", "apply", 0.4),
    ]),
    ("herons_formula", "Heron's Formula", [
        _c("herons", "Area Using Heron's Formula", "apply", 0.4),
    ]),
    ("surface_area_volume9", "Surface Areas and Volumes", [
        _c("cuboid_cylinder", "Surface Area and Volume of Cuboid, Cylinder", "apply", 0.35),
        _c("cone_sphere", "Surface Area and Volume of Cone, Sphere", "apply", 0.4, ["surface_area_volume9.cuboid_cylinder"]),
    ]),
    ("statistics9", "Statistics", [
        _c("mean_median_mode", "Mean, Median and Mode", "apply", 0.35),
    ]),
    ("probability9", "Probability", [
        _c("experimental_prob", "Experimental Probability", "understand", 0.35),
    ]),
]

MATH10_CHAPTERS = [
    ("real_numbers", "Real Numbers", [
        _c("euclid_division", "Euclid's Division Lemma", "understand", 0.4),
        _c("fundamental_theorem", "Fundamental Theorem of Arithmetic", "apply", 0.45, ["real_numbers.euclid_division"]),
    ]),
    ("polynomials10", "Polynomials", [
        _c("zeroes_relationship", "Relationship Between Zeroes and Coefficients", "apply", 0.4),
        _c("division_algorithm", "Division Algorithm for Polynomials", "apply", 0.5, ["polynomials10.zeroes_relationship"]),
    ]),
    ("linear_eq_pair", "Pair of Linear Equations in Two Variables", [
        _c("algebraic_methods", "Substitution, Elimination, Cross-Multiplication", "apply", 0.45),
        _c("word_problems10", "Word Problems on Linear Equation Pairs", "apply", 0.5, ["linear_eq_pair.algebraic_methods"]),
    ]),
    ("quadratic_equations", "Quadratic Equations", [
        _c("quadratic_formula", "Quadratic Formula", "apply", 0.45),
        _c("nature_of_roots", "Nature of Roots (Discriminant)", "analyze", 0.5, ["quadratic_equations.quadratic_formula"]),
    ]),
    ("arithmetic_progressions", "Arithmetic Progressions", [
        _c("ap_nth_term", "Introduction to AP — nth Term", "understand", 0.35),
        _c("sum_of_ap", "Sum of First n Terms", "apply", 0.45, ["arithmetic_progressions.ap_nth_term"]),
    ]),
    ("triangles10", "Triangles", [
        _c("similarity_criteria", "Similarity of Triangles", "apply", 0.45),
        _c("pythagoras_theorem", "Pythagoras Theorem and Converse", "apply", 0.45, ["triangles10.similarity_criteria"]),
    ]),
    ("coordinate_geometry10", "Coordinate Geometry", [
        _c("distance_formula", "Distance and Section Formula", "apply", 0.4),
        _c("area_triangle_coord", "Area of Triangle (Coordinates)", "apply", 0.5, ["coordinate_geometry10.distance_formula"]),
    ]),
    ("trigonometry", "Introduction to Trigonometry", [
        _c("trig_ratios", "Trigonometric Ratios", "understand", 0.4),
        _c("trig_identities", "Trigonometric Identities", "apply", 0.5, ["trigonometry.trig_ratios"]),
    ]),
    ("trig_applications", "Applications of Trigonometry", [
        _c("heights_distances", "Heights and Distances", "apply", 0.5),
    ]),
    ("circles10", "Circles", [
        _c("tangent_theorems", "Tangent to a Circle — Theorems", "apply", 0.5),
    ]),
    ("constructions10", "Constructions", [
        _c("tangent_construction", "Construction of Tangents to a Circle", "apply", 0.45),
    ]),
    ("areas_circles", "Areas Related to Circles", [
        _c("sector_segment", "Area of Sector and Segment", "apply", 0.45),
    ]),
    ("surface_area_volume10", "Surface Areas and Volumes", [
        _c("combination_solids", "Surface Area and Volume of Combined Solids", "apply", 0.5),
        _c("frustum", "Frustum of a Cone", "apply", 0.5, ["surface_area_volume10.combination_solids"]),
    ]),
    ("statistics10", "Statistics", [
        _c("mean_median_mode_grouped", "Mean, Median, Mode of Grouped Data", "apply", 0.4),
        _c("ogive", "Cumulative Frequency and Ogives", "apply", 0.45, ["statistics10.mean_median_mode_grouped"]),
    ]),
    ("probability10", "Probability", [
        _c("theoretical_prob", "Theoretical Probability", "apply", 0.4),
    ]),
]

MATH11_CHAPTERS = [
    ("sets", "Sets", [
        _c("set_notation", "Set Notation, Types and Venn Diagrams", "apply", 0.3),
    ]),
    ("relations_functions", "Relations and Functions", [
        _c("relations", "Relations — Domain, Codomain, Range", "understand", 0.35),
        _c("functions", "Functions — Types and Graphs", "apply", 0.4, ["relations_functions.relations"]),
    ]),
    ("trig_functions", "Trigonometric Functions", [
        _c("trig_all_angles", "Trigonometric Functions of Any Angle", "apply", 0.4),
        _c("trig_identities11", "Trigonometric Identities and Equations", "apply", 0.5, ["trig_functions.trig_all_angles"]),
    ]),
    ("induction", "Principle of Mathematical Induction", [
        _c("pmi", "PMI — Principle and Applications", "apply", 0.5),
    ]),
    ("complex_numbers", "Complex Numbers", [
        _c("complex_intro", "Complex Numbers — Algebra and Argand Plane", "apply", 0.45),
    ]),
    ("linear_inequalities", "Linear Inequalities", [
        _c("solving_graphical", "Solving and Graphical Solution of Inequalities", "apply", 0.4),
    ]),
    ("permutations", "Permutations and Combinations", [
        _c("pnc", "Permutations and Combinations", "apply", 0.45),
    ]),
    ("binomial", "Binomial Theorem", [
        _c("binomial_theorem", "Binomial Theorem and General Term", "apply", 0.5),
    ]),
    ("sequences", "Sequences and Series", [
        _c("ap_gp", "AP and GP — nth Term and Sum", "apply", 0.4),
    ]),
    ("straight_lines", "Straight Lines", [
        _c("forms_of_line", "Various Forms of Equation of a Line", "apply", 0.4),
    ]),
    ("conic_sections", "Conic Sections", [
        _c("circle_parabola", "Circle and Parabola", "apply", 0.45),
        _c("ellipse_hyperbola", "Ellipse and Hyperbola", "apply", 0.5, ["conic_sections.circle_parabola"]),
    ]),
    ("three_d_intro", "Introduction to 3D Geometry", [
        _c("distance_3d", "Coordinate Axes and Distance in 3D", "apply", 0.4),
    ]),
    ("limits_derivatives", "Limits and Derivatives", [
        _c("limits", "Limits — Algebra of Limits", "apply", 0.45),
        _c("derivatives", "Derivatives — First Principles", "apply", 0.5, ["limits_derivatives.limits"]),
    ]),
    ("reasoning", "Mathematical Reasoning", [
        _c("statements", "Statements, Connectives and Validation", "understand", 0.35),
    ]),
    ("statistics11", "Statistics", [
        _c("variance_sd", "Measures of Dispersion — Variance, SD", "apply", 0.45),
    ]),
    ("probability11", "Probability", [
        _c("axiomatic_prob", "Axiomatic Approach to Probability", "apply", 0.45),
    ]),
]

MATH12_CHAPTERS = [
    ("relations_functions12", "Relations and Functions", [
        _c("types_functions", "Types of Relations and Functions", "apply", 0.45),
        _c("composition", "Composition of Functions and Inverse", "apply", 0.5, ["relations_functions12.types_functions"]),
    ]),
    ("inverse_trig", "Inverse Trigonometric Functions", [
        _c("properties", "Domain, Range and Properties", "apply", 0.5),
    ]),
    ("matrices", "Matrices", [
        _c("operations", "Types and Operations on Matrices", "apply", 0.4),
        _c("inverse_matrix", "Transpose, Symmetric and Invertible Matrices", "apply", 0.5, ["matrices.operations"]),
    ]),
    ("determinants", "Determinants", [
        _c("determinant_calc", "Calculation and Properties of Determinants", "apply", 0.4),
        _c("cramers_rule", "Cramer's Rule and Inverse", "apply", 0.55, ["determinants.determinant_calc"]),
    ]),
    ("continuity", "Continuity and Differentiability", [
        _c("continuity_diff", "Continuity and Differentiability", "apply", 0.45),
        _c("chain_rule", "Chain Rule, Implicit and Log Differentiation", "apply", 0.55, ["continuity.continuity_diff"]),
    ]),
    ("derivatives_app", "Application of Derivatives", [
        _c("maxima_minima", "Rate of Change, Tangents, Maxima and Minima", "apply", 0.5),
    ]),
    ("integrals", "Integrals", [
        _c("indefinite", "Indefinite Integrals — Methods", "apply", 0.45),
        _c("definite", "Definite Integrals — Fundamental Theorem", "apply", 0.5, ["integrals.indefinite"]),
    ]),
    ("integrals_app", "Application of Integrals", [
        _c("area_curves", "Area Under and Between Curves", "apply", 0.5),
    ]),
    ("diff_equations", "Differential Equations", [
        _c("variable_separable", "Order, Degree and Variable Separable", "apply", 0.5),
    ]),
    ("vectors", "Vector Algebra", [
        _c("vectors_ops", "Vectors — Dot and Cross Product", "apply", 0.45),
    ]),
    ("three_d", "Three Dimensional Geometry", [
        _c("line_plane", "Lines and Planes in 3D", "apply", 0.5),
    ]),
    ("linear_programming", "Linear Programming", [
        _c("lpp", "Formulation and Graphical Solution of LPP", "apply", 0.45),
    ]),
    ("probability12", "Probability", [
        _c("bayes_theorem", "Conditional Probability and Bayes' Theorem", "apply", 0.5),
        _c("random_variable", "Random Variable and Distributions", "apply", 0.55, ["probability12.bayes_theorem"]),
    ]),
]

# ── Science 6-10 (compact seeds) ──
SCIENCE6_CHAPTERS = [
    ("food", "Food: Where Does it Come From?", [
        _c("food_sources", "Sources of Food", "understand", 0.15),
        _c("herbivore_carnivore", "Herbivores, Carnivores and Omnivores", "understand", 0.2),
    ]),
    ("components_food", "Components of Food", [
        _c("nutrients", "Nutrients and Balanced Diet", "understand", 0.25),
    ]),
    ("fibre_fabric", "Fibre to Fabric", [
        _c("fibres", "Plant and Animal Fibres", "understand", 0.2),
    ]),
    ("sorting_materials", "Sorting Materials into Groups", [
        _c("properties_materials", "Properties and Grouping of Materials", "understand", 0.2),
    ]),
    ("separation", "Separation of Substances", [
        _c("methods", "Methods — Filtration, Evaporation, Sieving", "apply", 0.25),
    ]),
    ("changes", "Changes Around Us", [
        _c("reversible", "Reversible and Irreversible Changes", "understand", 0.2),
    ]),
    ("plants6", "Getting to Know Plants", [
        _c("plant_parts", "Parts of a Plant and Their Functions", "understand", 0.2),
    ]),
    ("body_movements", "Body Movements", [
        _c("joints", "Types of Joints and Movement", "understand", 0.25),
    ]),
    ("living_organisms", "Living Organisms and Their Surroundings", [
        _c("habitat", "Habitat and Adaptation", "understand", 0.2),
    ]),
    ("motion_measurement", "Motion and Measurement", [
        _c("types_motion", "Types of Motion and Standard Units", "understand", 0.2),
    ]),
    ("light6", "Light, Shadows and Reflections", [
        _c("shadows", "Transparent, Translucent, Opaque and Shadows", "understand", 0.2),
    ]),
    ("electricity6", "Electricity and Circuits", [
        _c("electric_circuit", "Electric Circuit and Conductors", "understand", 0.25),
    ]),
    ("magnets6", "Fun with Magnets", [
        _c("poles_attraction", "Poles of Magnet — Attraction and Repulsion", "understand", 0.25),
    ]),
    ("water6", "Water", [
        _c("water_cycle", "Water Cycle and Conservation", "understand", 0.25),
    ]),
    ("air6", "Air Around Us", [
        _c("composition", "Composition and Importance of Air", "understand", 0.2),
    ]),
    ("garbage", "Garbage In, Garbage Out", [
        _c("waste_management", "Reduce, Reuse, Recycle and Composting", "apply", 0.2),
    ]),
]

SCIENCE7_CHAPTERS = [
    ("nutrition_plants", "Nutrition in Plants", [
        _c("photosynthesis", "Photosynthesis and Modes of Nutrition", "understand", 0.3),
    ]),
    ("nutrition_animals", "Nutrition in Animals", [
        _c("digestion_humans", "Human Digestive System", "understand", 0.3),
    ]),
    ("heat7", "Heat", [
        _c("conduction_convection", "Conduction, Convection and Radiation", "understand", 0.35),
    ]),
    ("acids_bases7", "Acids, Bases and Salts", [
        _c("neutralisation", "Indicators and Neutralisation", "apply", 0.35),
    ]),
    ("physical_chemical", "Physical and Chemical Changes", [
        _c("chemical_change", "Physical vs Chemical Changes", "understand", 0.25),
    ]),
    ("weather", "Weather, Climate and Adaptations", [
        _c("adaptations", "Climate Adaptations of Animals", "understand", 0.3),
    ]),
    ("soil7", "Soil", [
        _c("soil_profile", "Soil Profile and Types", "understand", 0.25),
    ]),
    ("respiration7", "Respiration in Organisms", [
        _c("aerobic_anaerobic", "Aerobic and Anaerobic Respiration", "understand", 0.35),
    ]),
    ("transport7", "Transportation in Animals and Plants", [
        _c("circulatory", "Circulatory System", "understand", 0.35),
    ]),
    ("reproduction_plants7", "Reproduction in Plants", [
        _c("sexual_asexual", "Sexual and Asexual Reproduction", "understand", 0.3),
    ]),
    ("motion_time", "Motion and Time", [
        _c("speed_graph", "Speed and Distance-Time Graphs", "apply", 0.35),
    ]),
    ("electric_current7", "Electric Current and Effects", [
        _c("heating_magnetic", "Heating and Magnetic Effect", "understand", 0.35),
    ]),
    ("light7", "Light", [
        _c("reflection_dispersion", "Reflection and Dispersion", "understand", 0.3),
    ]),
    ("water7", "Water: A Precious Resource", [
        _c("water_management", "Water Management and Harvesting", "apply", 0.3),
    ]),
    ("forests7", "Forests: Our Lifeline", [
        _c("food_chains", "Food Chains and Forest Ecosystem", "understand", 0.3),
    ]),
]

SCIENCE8_CHAPTERS = [
    ("crop_production", "Crop Production and Management", [_c("agricultural_practices", "Agricultural Practices and Crop Types", "understand", 0.25)]),
    ("microorganisms", "Microorganisms", [_c("useful_harmful", "Useful and Harmful Microorganisms", "understand", 0.3)]),
    ("synthetic_fibres", "Synthetic Fibres and Plastics", [_c("types_fibres", "Types of Synthetic Fibres and Plastics", "understand", 0.25)]),
    ("metals_nonmetals8", "Metals and Non-Metals", [_c("chemical_properties", "Physical and Chemical Properties", "apply", 0.4)]),
    ("coal_petroleum", "Coal and Petroleum", [_c("fossil_fuels", "Fossil Fuels — Formation and Conservation", "understand", 0.25)]),
    ("combustion8", "Combustion and Flame", [_c("combustion_types", "Types of Combustion and Flame Structure", "understand", 0.25)]),
    ("conservation8", "Conservation of Plants and Animals", [_c("biodiversity", "Biodiversity and Conservation", "understand", 0.3)]),
    ("cell8", "Cell: Structure and Functions", [_c("cell_organelles", "Plant and Animal Cell — Organelles", "understand", 0.4)]),
    ("reproduction_animals8", "Reproduction in Animals", [_c("sexual_asexual8", "Sexual and Asexual Reproduction", "understand", 0.35)]),
    ("adolescence", "Reaching the Age of Adolescence", [_c("puberty_hormones", "Puberty and Hormones", "understand", 0.3)]),
    ("force_pressure", "Force and Pressure", [_c("pressure", "Types of Forces, Pressure and Atmospheric Pressure", "apply", 0.35)]),
    ("friction8", "Friction", [_c("types_friction", "Types of Friction and Applications", "understand", 0.3)]),
    ("sound8", "Sound", [_c("loudness_pitch", "Vibration, Loudness, Pitch and Frequency", "apply", 0.35)]),
    ("chemical_effects", "Chemical Effects of Electric Current", [_c("electroplating", "Conductivity and Electroplating", "apply", 0.35)]),
    ("natural_phenomena", "Some Natural Phenomena", [_c("lightning_earthquake", "Lightning and Earthquakes", "understand", 0.3)]),
    ("light8", "Light", [_c("reflection_laws", "Laws of Reflection and Human Eye", "understand", 0.3)]),
    ("stars_solar", "Stars and the Solar System", [_c("solar_system", "Moon, Planets and Solar System", "understand", 0.25)]),
    ("pollution8", "Pollution of Air and Water", [_c("pollution", "Causes and Prevention of Pollution", "understand", 0.25)]),
]

SCIENCE9_CHAPTERS = [
    ("matter", "Matter in Our Surroundings", [_c("states_change", "States of Matter and Change of State", "understand", 0.3)]),
    ("pure_matter", "Is Matter Around Us Pure?", [_c("separation_techniques", "Mixtures, Solutions, Separation Techniques", "apply", 0.35)]),
    ("atoms_molecules", "Atoms and Molecules", [_c("mole_concept", "Atomic Mass, Molecular Mass and Mole Concept", "apply", 0.5)]),
    ("atomic_structure9", "Structure of the Atom", [_c("bohr_model", "Subatomic Particles and Bohr's Model", "understand", 0.4)]),
    ("cell_fundamental", "The Fundamental Unit of Life", [_c("cell_structure", "Cell Structure and Organelles", "understand", 0.35)]),
    ("tissues", "Tissues", [_c("plant_animal_tissues", "Plant and Animal Tissues", "understand", 0.35)]),
    ("diversity9", "Diversity in Living Organisms", [_c("five_kingdoms", "Five Kingdom Classification", "understand", 0.35)]),
    ("motion9", "Motion", [
        _c("speed_velocity", "Speed, Velocity and Acceleration", "apply", 0.4),
        _c("equations_of_motion", "Equations of Motion", "apply", 0.5, ["motion9.speed_velocity"]),
    ]),
    ("force_laws", "Force and Laws of Motion", [
        _c("newtons_laws", "Newton's Three Laws of Motion", "apply", 0.45),
        _c("momentum", "Momentum and Conservation", "apply", 0.5, ["force_laws.newtons_laws"]),
    ]),
    ("gravitation9", "Gravitation", [_c("universal_gravitation", "Universal Law of Gravitation and Free Fall", "apply", 0.45)]),
    ("work_energy9", "Work and Energy", [_c("conservation_energy", "Work, KE, PE and Conservation of Energy", "apply", 0.4)]),
    ("sound9", "Sound", [_c("characteristics", "Frequency, Amplitude, Speed, Echo and Resonance", "apply", 0.4)]),
    ("health9", "Why Do We Fall Ill?", [_c("infectious_diseases", "Health, Disease and Prevention", "understand", 0.3)]),
    ("natural_resources9", "Natural Resources", [_c("biogeochemical_cycles", "Biogeochemical Cycles", "understand", 0.35)]),
    ("food_resources9", "Improvement in Food Resources", [_c("crop_animal", "Crop Improvement and Animal Husbandry", "understand", 0.3)]),
]

SCIENCE10_CHAPTERS = [
    ("chemical_reactions", "Chemical Reactions and Equations", [_c("types_balancing", "Types of Reactions and Balancing Equations", "apply", 0.4)]),
    ("acids_bases_salts10", "Acids, Bases and Salts", [_c("indicators_ph", "Indicators, pH and Reactions", "apply", 0.4)]),
    ("metals_nonmetals10", "Metals and Non-metals", [_c("reactivity_extraction", "Reactivity Series and Extraction of Metals", "apply", 0.45)]),
    ("carbon_compounds", "Carbon and its Compounds", [_c("bonding_functional", "Covalent Bonding, Hydrocarbons, Functional Groups", "apply", 0.5)]),
    ("periodic_table10", "Periodic Classification of Elements", [_c("modern_periodic", "Modern Periodic Table and Trends", "understand", 0.4)]),
    ("life_processes", "Life Processes", [_c("nutrition_respiration", "Nutrition, Respiration, Transportation, Excretion", "understand", 0.35)]),
    ("control_coordination", "Control and Coordination", [_c("nervous_hormones", "Nervous System and Hormones", "understand", 0.4)]),
    ("reproduction10", "How Do Organisms Reproduce?", [_c("sexual_asexual10", "Sexual and Asexual Reproduction", "understand", 0.35)]),
    ("heredity_evolution", "Heredity and Evolution", [_c("mendels_laws", "Mendel's Laws and Evolution", "understand", 0.4)]),
    ("light_reflection", "Light — Reflection and Refraction", [_c("mirrors_lenses", "Spherical Mirrors and Lenses", "apply", 0.45)]),
    ("human_eye10", "Human Eye and Colourful World", [_c("defects_dispersion", "Defects of Vision, Scattering, Dispersion", "apply", 0.4)]),
    ("electricity10", "Electricity", [_c("ohms_law_power", "Ohm's Law, Resistance, Electric Power", "apply", 0.45)]),
    ("magnetic_effects10", "Magnetic Effects of Electric Current", [_c("em_induction", "Magnetic Field and Electromagnetic Induction", "apply", 0.45)]),
    ("sources_energy10", "Sources of Energy", [_c("conventional_nonconv", "Conventional and Non-Conventional Energy", "understand", 0.3)]),
    ("environment10", "Our Environment", [_c("ecosystem_ozone", "Ecosystem Components and Ozone Depletion", "understand", 0.3)]),
]

# ── Physics 11-12, Chemistry 11-12, Biology 11-12 (compact) ──
PHYSICS11_CHAPTERS = [
    ("units", "Units and Measurements", [_c("dimensions", "SI Units and Dimensional Analysis", "apply", 0.4)]),
    ("straight_line_motion", "Motion in a Straight Line", [_c("kinematics_1d", "Kinematic Equations and Free Fall", "apply", 0.4)]),
    ("motion_plane", "Motion in a Plane", [_c("projectile_circular", "Vectors, Projectile and Circular Motion", "apply", 0.5)]),
    ("laws_motion", "Laws of Motion", [_c("newtons_friction", "Newton's Laws and Friction", "apply", 0.45)]),
    ("work_energy_power", "Work, Energy and Power", [_c("conservation_collisions", "Work-Energy Theorem, Conservation, Collisions", "apply", 0.5)]),
    ("rotational_motion", "Rotational Motion", [_c("moi_angular_momentum", "Centre of Mass, Moment of Inertia, Angular Momentum", "apply", 0.55)]),
    ("gravitation11", "Gravitation", [_c("field_orbital", "Gravitational Field, PE and Orbital Motion", "apply", 0.5)]),
    ("mech_solids", "Mechanical Properties of Solids", [_c("stress_strain", "Stress, Strain and Elastic Moduli", "apply", 0.45)]),
    ("mech_fluids", "Mechanical Properties of Fluids", [_c("bernoulli_viscosity", "Pascal's Law, Bernoulli, Viscosity, Surface Tension", "apply", 0.5)]),
    ("thermal", "Thermal Properties of Matter", [_c("heat_transfer", "Thermal Expansion, Calorimetry, Heat Transfer", "apply", 0.4)]),
    ("thermodynamics11", "Thermodynamics", [_c("laws_engines", "First and Second Law, Entropy, Carnot Cycle", "apply", 0.55)]),
    ("kinetic_theory", "Kinetic Theory", [_c("gas_laws_kinetic", "Ideal Gas Laws, Kinetic Theory", "apply", 0.5)]),
    ("oscillations", "Oscillations", [_c("shm_energy", "SHM, Energy, Damped and Forced Oscillations", "apply", 0.5)]),
    ("waves11", "Waves", [_c("superposition_standing", "Wave Equation, Superposition, Standing Waves, Beats", "apply", 0.5)]),
]

PHYSICS12_CHAPTERS = [
    ("electric_charges", "Electric Charges and Fields", [_c("coulombs_gauss", "Coulomb's Law and Gauss's Law", "apply", 0.5)]),
    ("electrostatic_potential", "Electrostatic Potential and Capacitance", [_c("potential_capacitance", "Potential, Capacitors and Energy Stored", "apply", 0.5)]),
    ("current_electricity", "Current Electricity", [_c("kirchhoffs", "Ohm's Law, Kirchhoff's Laws, Wheatstone Bridge", "apply", 0.5)]),
    ("magnetism_current", "Moving Charges and Magnetism", [_c("biot_ampere", "Lorentz Force, Biot-Savart, Ampere's Law", "apply", 0.55)]),
    ("magnetism_matter", "Magnetism and Matter", [_c("magnetic_materials", "Dia-, Para-, Ferromagnetic Materials", "understand", 0.4)]),
    ("em_induction", "Electromagnetic Induction", [_c("faradays_lenz", "Faraday's Law, Lenz's Law, Inductance", "apply", 0.5)]),
    ("ac", "Alternating Current", [_c("lcr_transformers", "LCR Circuits, Resonance, Transformers", "apply", 0.55)]),
    ("em_waves", "Electromagnetic Waves", [_c("em_spectrum", "EM Spectrum and Properties", "understand", 0.4)]),
    ("ray_optics", "Ray Optics", [_c("reflection_refraction_instruments", "Reflection, Refraction, Prism, TIR, Instruments", "apply", 0.5)]),
    ("wave_optics", "Wave Optics", [_c("interference_diffraction", "Young's Slit, Diffraction, Polarisation", "apply", 0.55)]),
    ("dual_nature", "Dual Nature of Radiation and Matter", [_c("photoelectric_debroglie", "Photoelectric Effect and de Broglie", "apply", 0.5)]),
    ("atoms12", "Atoms", [_c("bohr_spectrum", "Bohr Model and Hydrogen Spectrum", "apply", 0.5)]),
    ("nuclei", "Nuclei", [_c("binding_radioactivity", "Binding Energy, Radioactivity, Fission, Fusion", "apply", 0.5)]),
    ("semiconductors", "Semiconductor Electronics", [_c("pn_junction_transistor", "p-n Junction, Transistor, Logic Gates", "apply", 0.5)]),
]

CHEMISTRY11_CHAPTERS = [
    ("basic_concepts", "Some Basic Concepts of Chemistry", [_c("mole_stoichiometry", "Mole Concept and Stoichiometry", "apply", 0.45)]),
    ("atomic_structure11", "Structure of Atom", [_c("quantum_config", "Quantum Numbers, Orbitals, Electron Configuration", "apply", 0.45)]),
    ("classification11", "Classification of Elements and Periodicity", [_c("periodic_trends", "Modern Periodic Table and Trends", "apply", 0.4)]),
    ("chemical_bonding", "Chemical Bonding and Molecular Structure", [_c("vsepr_hybridisation", "Ionic, Covalent, VSEPR, Hybridisation", "apply", 0.55)]),
    ("states_matter11", "States of Matter", [_c("gas_laws_intermolecular", "Gas Laws and Intermolecular Forces", "apply", 0.4)]),
    ("thermodynamics_chem", "Thermodynamics", [_c("enthalpy_gibbs", "Enthalpy, Hess's Law, Gibbs Energy", "apply", 0.5)]),
    ("equilibrium11", "Equilibrium", [_c("chemical_ionic_eq", "Chemical and Ionic Equilibrium, pH, Buffers", "apply", 0.5)]),
    ("redox", "Redox Reactions", [_c("balancing_redox", "Oxidation Numbers and Balancing Redox", "apply", 0.45)]),
    ("hydrogen11", "Hydrogen", [_c("hydrogen_water", "Hydrogen Properties, Preparation, Water Chemistry", "understand", 0.3)]),
    ("s_block", "The s-Block Elements", [_c("alkali_alkaline", "Alkali and Alkaline Earth Metals", "understand", 0.35)]),
    ("p_block_11", "Some p-Block Elements", [_c("group_13_14", "Group 13 and 14 Elements", "understand", 0.35)]),
    ("organic_basics", "Organic Chemistry — Basic Principles", [_c("iupac_mechanisms", "IUPAC Nomenclature, Isomerism, Mechanisms", "apply", 0.55)]),
    ("hydrocarbons11", "Hydrocarbons", [_c("alkanes_alkenes_aromatic", "Alkanes, Alkenes, Alkynes, Aromatic", "understand", 0.45)]),
    ("environmental11", "Environmental Chemistry", [_c("pollution_green", "Pollution and Green Chemistry", "understand", 0.3)]),
]

CHEMISTRY12_CHAPTERS = [
    ("solid_state", "The Solid State", [_c("crystal_defects", "Crystal Lattice, Packing, Defects", "apply", 0.5)]),
    ("solutions12", "Solutions", [_c("colligative", "Concentration Terms and Colligative Properties", "apply", 0.5)]),
    ("electrochemistry12", "Electrochemistry", [_c("nernst_electrolysis", "Galvanic Cells, Nernst Equation, Electrolysis", "apply", 0.5)]),
    ("chemical_kinetics", "Chemical Kinetics", [_c("rate_order", "Rate Law, Order, Integrated Rate Equations", "apply", 0.5)]),
    ("surface_chemistry", "Surface Chemistry", [_c("adsorption_colloids", "Adsorption and Colloids", "understand", 0.4)]),
    ("isolation", "Isolation of Elements", [_c("metallurgy", "Metallurgical Processes and Refining", "understand", 0.4)]),
    ("p_block_12", "The p-Block Elements", [_c("groups_15_18", "Groups 15, 16, 17 and 18 Elements", "understand", 0.4)]),
    ("d_f_block", "The d- and f-Block Elements", [_c("transition_metals", "Transition Metals, Lanthanoids, Actinoids", "understand", 0.4)]),
    ("coordination12", "Coordination Compounds", [_c("nomenclature_bonding", "Nomenclature, Isomerism, VBT and CFT", "apply", 0.55)]),
    ("haloalkanes", "Haloalkanes and Haloarenes", [_c("sn1_sn2_elimination", "SN1, SN2, Elimination Reactions", "apply", 0.5)]),
    ("alcohols12", "Alcohols, Phenols and Ethers", [_c("reactions_alcohols", "Preparation and Reactions", "apply", 0.45)]),
    ("aldehydes_ketones", "Aldehydes, Ketones and Carboxylic Acids", [_c("nucleophilic_addition", "Nucleophilic Addition and Carboxylic Acids", "apply", 0.5)]),
    ("amines12", "Amines", [_c("classification_reactions", "Classification, Preparation and Reactions", "apply", 0.45)]),
    ("biomolecules12", "Biomolecules", [_c("carbs_proteins_nucleic", "Carbohydrates, Proteins, Nucleic Acids", "understand", 0.4)]),
    ("polymers12", "Polymers", [_c("classification_polymers", "Classification and Important Polymers", "understand", 0.3)]),
]

BIOLOGY11_CHAPTERS = [
    ("living_world", "The Living World", [_c("taxonomy", "Diversity and Taxonomical Hierarchy", "understand", 0.25)]),
    ("biological_classification", "Biological Classification", [_c("five_kingdoms", "Five Kingdom Classification", "understand", 0.3)]),
    ("plant_kingdom", "Plant Kingdom", [_c("algae_to_angiosperms", "Algae to Angiosperms, Life Cycles", "understand", 0.35)]),
    ("animal_kingdom", "Animal Kingdom", [_c("classification_phyla", "Classification — Porifera to Mammals", "understand", 0.35)]),
    ("morphology_plants", "Morphology of Flowering Plants", [_c("root_stem_leaf_flower", "Root, Stem, Leaf, Flower", "understand", 0.3)]),
    ("anatomy_plants", "Anatomy of Flowering Plants", [_c("tissue_system", "Tissue Systems and Internal Structure", "understand", 0.4)]),
    ("cell_unit", "Cell: The Unit of Life", [_c("cell_organelles", "Cell Theory and Organelles", "understand", 0.4)]),
    ("biomolecules11", "Biomolecules", [_c("carbs_proteins_enzymes", "Carbs, Proteins, Lipids and Enzymes", "understand", 0.4)]),
    ("cell_cycle", "Cell Cycle and Division", [_c("mitosis_meiosis", "Mitosis and Meiosis", "understand", 0.4)]),
    ("transport_plants11", "Transport in Plants", [_c("water_mineral_transport", "Water and Mineral Transport", "understand", 0.35)]),
    ("photosynthesis11", "Photosynthesis", [_c("light_dark_reactions", "Light Reactions, Calvin Cycle, C3/C4/CAM", "understand", 0.5)]),
    ("respiration_plants", "Respiration in Plants", [_c("glycolysis_krebs", "Glycolysis, Krebs Cycle, ETC", "understand", 0.5)]),
    ("plant_growth", "Plant Growth and Development", [_c("hormones_growth", "Growth Phases and Plant Hormones", "understand", 0.4)]),
    ("digestion11", "Digestion and Absorption", [_c("digestive_system", "Human Digestive System and Absorption", "understand", 0.4)]),
    ("breathing11", "Breathing and Exchange of Gases", [_c("gas_exchange", "Respiratory System and Gas Exchange", "apply", 0.4)]),
    ("circulation11", "Body Fluids and Circulation", [_c("heart_circulation", "Blood, Heart and Circulatory System", "understand", 0.4)]),
    ("excretion11", "Excretory Products", [_c("nephron_regulation", "Nephron, Urine Formation, Regulation", "apply", 0.45)]),
    ("locomotion11", "Locomotion and Movement", [_c("skeletal_muscular", "Skeletal and Muscular System", "understand", 0.35)]),
    ("neural_control", "Neural Control and Coordination", [_c("neuron_brain", "Neuron, Nerve Impulse, Brain, Spinal Cord", "understand", 0.4)]),
    ("chemical_coordination", "Chemical Coordination", [_c("endocrine_hormones", "Endocrine Glands and Hormonal Regulation", "understand", 0.4)]),
]

BIOLOGY12_CHAPTERS = [
    ("reproduction_organisms", "Reproduction in Organisms", [_c("asexual_sexual", "Asexual and Sexual Reproduction", "understand", 0.3)]),
    ("sexual_reproduction_plants", "Sexual Reproduction in Flowering Plants", [_c("pollination_fertilisation", "Pollination, Fertilisation, Embryo Development", "understand", 0.4)]),
    ("human_reproduction", "Human Reproduction", [_c("gametogenesis_dev", "Reproductive System, Gametogenesis, Development", "understand", 0.45)]),
    ("reproductive_health", "Reproductive Health", [_c("contraception_art", "Reproductive Health, Contraception, ART", "understand", 0.35)]),
    ("inheritance", "Principles of Inheritance", [_c("mendels_linkage", "Mendel's Laws, Linkage, Sex-Linked Inheritance", "apply", 0.45)]),
    ("molecular_inheritance", "Molecular Basis of Inheritance", [_c("dna_transcription", "DNA Structure, Replication, Transcription, Translation", "apply", 0.55)]),
    ("evolution12", "Evolution", [_c("mechanisms_human", "Origin of Life, Natural Selection, Human Evolution", "understand", 0.4)]),
    ("human_health12", "Human Health and Disease", [_c("diseases_immunity", "Common Diseases and Immunity", "understand", 0.35)]),
    ("food_production", "Enhancement in Food Production", [_c("breeding_husbandry", "Plant Breeding, Tissue Culture, Animal Husbandry", "understand", 0.35)]),
    ("microbes_welfare", "Microbes in Human Welfare", [_c("industrial_biogas", "Industrial Production, Biogas, Sewage Treatment", "understand", 0.3)]),
    ("biotech_principles", "Biotechnology: Principles", [_c("rdna_pcr", "rDNA Technology and PCR", "apply", 0.5)]),
    ("biotech_applications", "Biotechnology Applications", [_c("gm_gene_therapy", "GM Organisms and Gene Therapy", "understand", 0.45)]),
    ("ecology_organisms", "Organisms and Populations", [_c("population_dynamics", "Habitat, Niche, Population Growth", "apply", 0.4)]),
    ("ecosystem12", "Ecosystem", [_c("energy_nutrient", "Energy Flow and Nutrient Cycling", "understand", 0.4)]),
    ("biodiversity12", "Biodiversity and Conservation", [_c("conservation_strategies", "Levels and Conservation Strategies", "apply", 0.35)]),
    ("environmental_issues", "Environmental Issues", [_c("pollution_deforestation", "Pollution, Deforestation, Waste Management", "understand", 0.3)]),
]

# ── Social Science: History 6-12, Geography 6-12, Civics/Political Science 6-12 ──
HISTORY6_CHAPTERS = [
    ("what_where", "What, Where, How and When?", [_c("studying_past", "How We Study the Past", "understand", 0.2)]),
    ("earliest_societies", "On the Trail of the Earliest People", [_c("hunters_gatherers", "Hunters and Gatherers", "understand", 0.2)]),
    ("first_farmers", "From Gathering to Growing Food", [_c("farming_herding", "Farming and Herding", "understand", 0.2)]),
    ("first_cities", "In the Earliest Cities", [_c("harappan", "Harappan Civilisation", "understand", 0.3)]),
    ("kingdoms", "Kingdoms, Kings and Early Republic", [_c("mahajanapadas", "Mahajanapadas and Republics", "understand", 0.3)]),
    ("new_ideas", "New Questions and Ideas", [_c("buddha_mahavira", "Buddha and Mahavira", "understand", 0.3)]),
    ("ashoka", "Ashoka, the Emperor Who Gave Up War", [_c("mauryan_empire", "Mauryan Empire and Ashoka", "understand", 0.3)]),
    ("villages", "Vital Villages, Thriving Towns", [_c("iron_tools", "Iron Tools and Agriculture", "understand", 0.25)]),
    ("traders", "Traders, Kings and Pilgrims", [_c("silk_road", "Silk Road and Trade Routes", "understand", 0.3)]),
    ("buildings", "New Empires and Kingdoms", [_c("gupta_dynasty", "Gupta Dynasty and Other Kingdoms", "understand", 0.3)]),
]

HISTORY7_CHAPTERS = [
    ("tracing_changes", "Tracing Changes Through a Thousand Years", [_c("medieval_sources", "Sources and Periodisation", "understand", 0.25)]),
    ("new_kings", "New Kings and Kingdoms", [_c("rajput_dynasties", "Rajput and Other Dynasties", "understand", 0.3)]),
    ("delhi_sultans", "The Delhi Sultans", [_c("sultanate", "Delhi Sultanate — Rulers and Administration", "understand", 0.3)]),
    ("mughal_empire", "The Mughal Empire", [_c("mughal_rulers", "Mughal Rulers and Administration", "understand", 0.35)]),
    ("rulers_buildings", "Rulers and Buildings", [_c("architecture", "Medieval Architecture — Temples, Mosques, Forts", "understand", 0.3)]),
    ("devotional_paths", "Devotional Paths to the Divine", [_c("bhakti_sufi", "Bhakti and Sufi Movements", "understand", 0.3)]),
    ("towns_traders", "Towns, Traders and Craftspeople", [_c("medieval_trade", "Medieval Trade and Urban Centres", "understand", 0.3)]),
    ("tribes_nomads", "Tribes, Nomads and Settled Communities", [_c("tribal_societies", "Tribal Societies in India", "understand", 0.25)]),
]

HISTORY8_CHAPTERS = [
    ("modern_period", "How, When and Where", [_c("periodisation", "Periodisation and Sources", "understand", 0.25)]),
    ("trade_to_territory", "From Trade to Territory", [_c("east_india_company", "East India Company and Expansion", "understand", 0.3)]),
    ("ruling_countryside", "Ruling the Countryside", [_c("revenue_systems", "Revenue Systems and Indigo Rebellion", "understand", 0.35)]),
    ("revolt_1857", "When People Rebel — 1857", [_c("causes_spread", "Causes, Spread and Aftermath of 1857", "understand", 0.35)]),
    ("women_reform", "Women, Caste and Reform", [_c("social_reformers", "Social Reformers and Movements", "understand", 0.3)]),
    ("national_movement", "The National Movement: 1870s–1947", [_c("gandhian_era", "Congress, Gandhian Era, Independence", "understand", 0.4)]),
    ("india_after_independence", "India After Independence", [_c("constitution_making", "Constitution Making and State Integration", "understand", 0.3)]),
]

HISTORY9_CHAPTERS = [
    ("french_revolution", "The French Revolution", [_c("causes_impact", "Causes, Events and Impact", "understand", 0.35)]),
    ("russian_revolution", "Socialism in Europe and the Russian Revolution", [_c("socialism_revolution", "Socialism and Russian Revolution", "understand", 0.35)]),
    ("nazism", "Nazism and the Rise of Hitler", [_c("nazi_germany", "Rise of Hitler and Nazi Ideology", "understand", 0.35)]),
    ("forest_society", "Forest Society and Colonialism", [_c("colonial_forests", "Colonialism and Forest Communities", "understand", 0.3)]),
    ("pastoralists", "Pastoralists in the Modern World", [_c("nomadic_life", "Nomadic Pastoralists — India and Africa", "understand", 0.3)]),
]

HISTORY10_CHAPTERS = [
    ("nationalism_europe", "The Rise of Nationalism in Europe", [_c("nation_state", "Nation States and National Movements", "understand", 0.35)]),
    ("nationalism_india", "Nationalism in India", [_c("ncm_cdm_quit", "Non-Cooperation, Civil Disobedience, Quit India", "understand", 0.4)]),
    ("making_global", "The Making of a Global World", [_c("globalisation_history", "Trade, Migration and Global Connections", "understand", 0.35)]),
    ("industrialisation", "The Age of Industrialisation", [_c("industrial_revolution", "Industrialisation in Britain and India", "understand", 0.35)]),
    ("print_culture", "Print Culture and the Modern World", [_c("print_revolution", "Print Revolution and Its Impact", "understand", 0.3)]),
]

GEOGRAPHY6_CHAPTERS = [
    ("earth_solar", "The Earth in the Solar System", [_c("solar_system", "Solar System and the Earth", "understand", 0.2)]),
    ("globe", "Globe: Latitudes and Longitudes", [_c("lat_long", "Latitudes, Longitudes and Time Zones", "understand", 0.3)]),
    ("motions_earth", "Motions of the Earth", [_c("rotation_revolution", "Rotation and Revolution", "understand", 0.25)]),
    ("maps", "Maps", [_c("types_components", "Types and Components of Maps", "understand", 0.25)]),
    ("domains_earth", "Major Domains of the Earth", [_c("lithosphere_hydrosphere", "Lithosphere, Hydrosphere, Atmosphere, Biosphere", "understand", 0.3)]),
    ("india_diversity", "Our Country — India", [_c("physical_features", "Physical Features of India", "understand", 0.3)]),
]

GEOGRAPHY7_CHAPTERS = [
    ("environment", "Environment", [_c("natural_human", "Natural and Human Environment", "understand", 0.2)]),
    ("inside_earth", "Inside Our Earth", [_c("layers_rocks", "Layers of Earth and Types of Rocks", "understand", 0.3)]),
    ("our_changing_earth", "Our Changing Earth", [_c("weathering_erosion", "Weathering, Erosion and Deposition", "understand", 0.3)]),
    ("air_water", "Air and Water", [_c("atmosphere_water_cycle", "Atmosphere Composition and Water Cycle", "understand", 0.3)]),
    ("natural_vegetation", "Natural Vegetation and Wildlife", [_c("forests_grasslands", "Forests, Grasslands and Wildlife", "understand", 0.25)]),
    ("human_environment", "Human Environment Interactions", [_c("settlement_transport", "Settlements and Transport", "understand", 0.3)]),
]

GEOGRAPHY8_CHAPTERS = [
    ("resources", "Resources", [_c("types_conservation", "Types of Resources and Conservation", "understand", 0.25)]),
    ("land_soil_water", "Land, Soil, Water and Wildlife", [_c("land_use_soil", "Land Use, Soil Types and Conservation", "understand", 0.3)]),
    ("mineral_power", "Mineral and Power Resources", [_c("minerals_energy", "Minerals and Energy Resources", "understand", 0.3)]),
    ("agriculture8", "Agriculture", [_c("farming_types_crops", "Types of Farming and Major Crops", "understand", 0.3)]),
    ("industries8", "Industries", [_c("classification_regions", "Classification and Industrial Regions", "understand", 0.3)]),
    ("human_resources8", "Human Resources", [_c("population_density", "Population Distribution and Change", "understand", 0.3)]),
]

GEOGRAPHY9_CHAPTERS = [
    ("india_size", "India — Size and Location", [_c("location_extent", "Location, Extent and Neighbours", "understand", 0.2)]),
    ("physical_features9", "Physical Features of India", [_c("mountains_plains_plateaus", "Mountains, Plains and Plateaus", "understand", 0.3)]),
    ("drainage", "Drainage", [_c("river_systems", "Himalayan and Peninsular Rivers", "understand", 0.3)]),
    ("climate9", "Climate", [_c("monsoon", "Monsoon and Climate Controls", "understand", 0.3)]),
    ("natural_vegetation9", "Natural Vegetation and Wildlife", [_c("forest_types", "Forest Types and Wildlife Conservation", "understand", 0.3)]),
    ("population9", "Population", [_c("growth_distribution", "Population Growth and Distribution", "understand", 0.3)]),
]

GEOGRAPHY10_CHAPTERS = [
    ("resources_dev", "Resources and Development", [_c("types_planning", "Resource Types and Planning", "understand", 0.3)]),
    ("forest_wildlife10", "Forest and Wildlife Resources", [_c("conservation10", "Conservation Strategies", "understand", 0.3)]),
    ("water_resources10", "Water Resources", [_c("dams_harvesting", "Dams and Rainwater Harvesting", "understand", 0.3)]),
    ("agriculture10", "Agriculture", [_c("types_crops10", "Types of Farming and Major Crops", "understand", 0.3)]),
    ("minerals_energy10", "Minerals and Energy Resources", [_c("distribution_conservation", "Distribution and Conservation", "understand", 0.3)]),
    ("manufacturing10", "Manufacturing Industries", [_c("classification_impact", "Classification, Agglomeration and Impact", "understand", 0.3)]),
    ("lifelines", "Lifelines of National Economy", [_c("transport_communication", "Transport, Communication and Trade", "understand", 0.3)]),
]

CIVICS6_CHAPTERS = [
    ("diversity", "Understanding Diversity", [_c("unity_diversity", "Unity in Diversity — India", "understand", 0.2)]),
    ("government", "What Is Government?", [_c("democracy_levels", "Democracy and Levels of Government", "understand", 0.2)]),
    ("panchayati_raj", "Panchayati Raj", [_c("local_governance", "Gram Panchayat and Local Self-Government", "understand", 0.25)]),
    ("urban_admin", "Urban Administration", [_c("municipality", "Municipal Corporation and Functions", "understand", 0.25)]),
    ("livelihoods", "Rural Livelihoods and Urban Livelihoods", [_c("rural_urban", "Rural and Urban Livelihoods", "understand", 0.25)]),
]

CIVICS7_CHAPTERS = [
    ("equality", "On Equality", [_c("equality_india", "Equality in Indian Democracy", "understand", 0.25)]),
    ("role_government", "Role of the Government in Health", [_c("health_services", "Public Health Services", "understand", 0.25)]),
    ("state_government", "How the State Government Works", [_c("legislature_executive", "Legislature and Executive", "understand", 0.3)]),
    ("gender", "Growing Up as Boys and Girls", [_c("gender_roles", "Gender Roles and Stereotypes", "understand", 0.25)]),
    ("media", "Understanding Media", [_c("media_democracy", "Media and Its Role in Democracy", "understand", 0.25)]),
    ("markets", "Markets Around Us", [_c("weekly_market", "Weekly Markets and Shopping Complexes", "understand", 0.2)]),
]

CIVICS8_CHAPTERS = [
    ("constitution", "The Indian Constitution", [_c("key_features", "Key Features of the Constitution", "understand", 0.3)]),
    ("secularism", "Understanding Secularism", [_c("secularism_india", "Secularism and State-Religion Separation", "understand", 0.3)]),
    ("parliament", "Parliament", [_c("law_making", "Role of Parliament and Law Making", "understand", 0.3)]),
    ("judiciary8", "Judiciary", [_c("judicial_system", "Structure of Indian Judiciary", "understand", 0.3)]),
    ("marginalisation", "Understanding Marginalisation", [_c("rights_marginalised", "Marginalised Communities and Rights", "understand", 0.3)]),
    ("public_facilities", "Public Facilities", [_c("role_government", "Government's Role in Public Facilities", "understand", 0.3)]),
]

CIVICS9_CHAPTERS = [
    ("democracy9", "What Is Democracy? Why Democracy?", [_c("features_merits", "Features and Merits of Democracy", "understand", 0.3)]),
    ("constitutional_design", "Constitutional Design", [_c("making_constitution", "Making of Indian Constitution", "understand", 0.3)]),
    ("electoral_politics", "Electoral Politics", [_c("elections_india", "Elections in India", "understand", 0.3)]),
    ("institutions", "Working of Institutions", [_c("legislature_executive_judiciary", "Legislature, Executive and Judiciary", "understand", 0.35)]),
    ("democratic_rights", "Democratic Rights", [_c("fundamental_rights", "Fundamental Rights", "understand", 0.3)]),
]

CIVICS10_CHAPTERS = [
    ("power_sharing", "Power Sharing", [_c("forms_power_sharing", "Forms of Power Sharing", "understand", 0.3)]),
    ("federalism", "Federalism", [_c("indian_federalism", "Indian Federalism and Decentralisation", "understand", 0.35)]),
    ("democracy_diversity", "Democracy and Diversity", [_c("social_differences", "Social Differences and Democracy", "understand", 0.3)]),
    ("gender_religion_caste", "Gender, Religion and Caste", [_c("politics_diversity", "Gender, Religion, Caste in Politics", "understand", 0.3)]),
    ("political_parties", "Political Parties", [_c("party_system", "Party System in India", "understand", 0.3)]),
    ("outcomes_democracy", "Outcomes of Democracy", [_c("evaluating_democracy", "Evaluating Democracy", "analyze", 0.35)]),
]

# ── Political Science 11-12 ──
POLSCI11_CHAPTERS = [
    ("constitution_why", "Constitution: Why and How?", [_c("making_of", "Making of the Indian Constitution", "understand", 0.3)]),
    ("rights", "Rights in the Indian Constitution", [_c("fundamental_rights11", "Fundamental Rights and Duties", "understand", 0.35)]),
    ("election_representation", "Election and Representation", [_c("electoral_system", "Electoral System in India", "understand", 0.35)]),
    ("executive", "Executive", [_c("president_pm_council", "President, PM and Council of Ministers", "understand", 0.35)]),
    ("legislature", "Legislature", [_c("parliament_functions", "Parliament — Functions and Lawmaking", "understand", 0.35)]),
    ("judiciary11", "Judiciary", [_c("supreme_high_court", "Supreme Court, High Courts, Judicial Review", "understand", 0.35)]),
    ("federalism11", "Federalism", [_c("centre_state", "Centre-State Relations", "understand", 0.35)]),
    ("local_governments", "Local Governments", [_c("73rd_74th_amendments", "73rd and 74th Constitutional Amendments", "understand", 0.3)]),
]

POLSCI12_CHAPTERS = [
    ("cold_war", "The Cold War Era", [_c("bipolar_world", "Bipolar World and Cold War", "understand", 0.35)]),
    ("end_bipolarity", "The End of Bipolarity", [_c("soviet_collapse", "Collapse of Soviet Union", "understand", 0.35)]),
    ("us_hegemony", "US Hegemony in World Politics", [_c("us_power", "US Dominance and Resistance", "understand", 0.35)]),
    ("international_orgs", "International Organisations", [_c("un_reforms", "UN and Reforms", "understand", 0.3)]),
    ("security", "Security in the Contemporary World", [_c("traditional_nontraditional", "Traditional and Non-Traditional Security", "understand", 0.35)]),
    ("globalisation12", "Globalisation", [_c("political_economic", "Political and Economic Globalisation", "understand", 0.3)]),
]

# ── Economics 9-10 (already covered, re-included compactly) ──
ECONOMICS9_CHAPTERS = [
    ("village_economy", "The Story of Village Palampur", [_c("factors_production", "Factors of Production", "understand", 0.25)]),
    ("people_resource", "People as Resource", [_c("human_capital", "Human Capital and Unemployment", "understand", 0.3)]),
    ("poverty", "Poverty as a Challenge", [_c("poverty_measurement", "Poverty Line, Measurement, Alleviation", "understand", 0.3)]),
    ("food_security", "Food Security in India", [_c("pds", "Food Security and PDS", "understand", 0.3)]),
]

ECONOMICS10_CHAPTERS = [
    ("development", "Development", [_c("hdi", "Development Perspectives and HDI", "understand", 0.3)]),
    ("sectors_economy", "Sectors of the Indian Economy", [_c("primary_secondary_tertiary", "Primary, Secondary, Tertiary Sectors", "understand", 0.3)]),
    ("money_credit", "Money and Credit", [_c("banking", "Functions of Money and Banking", "understand", 0.3)]),
    ("globalisation10", "Globalisation", [_c("mncs_impact", "MNCs, Trade and Impact on India", "understand", 0.3)]),
    ("consumer_rights", "Consumer Rights", [_c("consumer_protection", "Consumer Awareness and Protection Act", "understand", 0.3)]),
]

# ── Economics 11-12 ──
ECONOMICS11_CHAPTERS = [
    ("indian_economy", "Indian Economy on the Eve of Independence", [_c("colonial_economy", "Colonial Economy and Its Impact", "understand", 0.3)]),
    ("indian_economy_reforms", "Economic Reforms Since 1991", [_c("lp_g", "Liberalisation, Privatisation, Globalisation", "understand", 0.35)]),
    ("poverty_hd", "Poverty and Human Development", [_c("poverty_trends", "Poverty Trends and Human Development", "understand", 0.3)]),
    ("employment", "Employment: Growth, Informalisation", [_c("employment_trends", "Employment Trends and Informal Sector", "understand", 0.3)]),
    ("infrastructure", "Infrastructure", [_c("energy_health_education", "Energy, Health and Education Infrastructure", "understand", 0.3)]),
    ("rural_development", "Rural Development", [_c("rural_credit", "Rural Credit, Marketing and Diversification", "understand", 0.3)]),
    ("environment_sd", "Environment and Sustainable Development", [_c("sustainable_dev", "Sustainable Development Strategies", "understand", 0.3)]),
]

ECONOMICS12_CHAPTERS = [
    ("micro_intro", "Introduction to Microeconomics", [_c("economy_types", "Central Problems and Types of Economies", "understand", 0.3)]),
    ("demand_supply", "Theory of Consumer Behaviour / Demand and Supply", [_c("demand_supply_curves", "Demand, Supply Curves and Equilibrium", "apply", 0.4)]),
    ("production_costs", "Production and Costs", [_c("production_function", "Production Function and Cost Curves", "apply", 0.4)]),
    ("market_forms", "Market Forms — Perfect Competition, Monopoly", [_c("price_output", "Price and Output Determination", "apply", 0.45)]),
    ("national_income", "National Income Accounting", [_c("gdp_methods", "GDP and Methods of Calculation", "apply", 0.4)]),
    ("money_banking12", "Money and Banking", [_c("money_supply_rbi", "Money Supply, RBI and Credit Creation", "apply", 0.4)]),
    ("govt_budget", "Government Budget and the Economy", [_c("fiscal_policy", "Fiscal Policy, Revenue, Expenditure", "apply", 0.4)]),
    ("balance_of_payments", "Balance of Payments", [_c("bop_forex", "BOP, Foreign Exchange and Exchange Rate", "apply", 0.45)]),
]

# ── English 6-10 Grammar (general, covers classes 6-10) ──
ENGLISH_GRAMMAR_CHAPTERS = [
    ("parts_of_speech", "Parts of Speech", [
        _c("nouns_pronouns", "Nouns and Pronouns", "understand", 0.2),
        _c("verbs_tenses", "Verbs and Tenses", "apply", 0.3, ["parts_of_speech.nouns_pronouns"]),
    ]),
    ("sentence_structure", "Sentence Structure", [
        _c("simple_compound_complex", "Simple, Compound and Complex Sentences", "apply", 0.35),
    ]),
    ("tenses", "Tenses", [
        _c("all_tenses", "Present, Past and Future — Simple, Continuous, Perfect", "apply", 0.3),
    ]),
    ("voice_speech", "Active-Passive Voice and Direct-Indirect Speech", [
        _c("active_passive", "Active and Passive Voice", "apply", 0.35),
        _c("direct_indirect", "Direct and Indirect Speech", "apply", 0.4, ["voice_speech.active_passive"]),
    ]),
    ("comprehension", "Reading Comprehension", [
        _c("unseen_passages", "Unseen Passages and Note Making", "apply", 0.35),
    ]),
    ("writing_skills", "Writing Skills", [
        _c("letter_essay", "Letter, Essay and Article Writing", "create", 0.4),
    ]),
]

# ── Hindi 6-10 (general) ──
HINDI6_CHAPTERS = [
    ("gadya6", "गद्य — Prose", [_c("stories_lessons", "Stories and Lessons with Comprehension", "understand", 0.25)]),
    ("padya6", "पद्य — Poetry", [_c("poems_bhav", "Poems and Their Meaning", "understand", 0.25)]),
    ("vyakaran6", "व्याकरण", [
        _c("sangya_sarvanam", "संज्ञा, सर्वनाम, विशेषण", "understand", 0.25),
        _c("kaal_vakya", "काल और वाक्य भेद", "apply", 0.3, ["vyakaran6.sangya_sarvanam"]),
    ]),
    ("lekhan6", "लेखन", [_c("nibandh_patra", "निबंध और पत्र लेखन", "apply", 0.3)]),
]

HINDI7_CHAPTERS = [
    ("gadya7", "गद्य — Prose", [_c("lessons7", "Hindi Lessons with Comprehension", "understand", 0.25)]),
    ("padya7", "पद्य — Poetry", [_c("kavita7", "Hindi Poems and Bhavarth", "understand", 0.25)]),
    ("vyakaran7", "व्याकरण", [
        _c("kriya_kaal", "क्रिया और काल", "apply", 0.3),
        _c("samas_intro", "समास परिचय", "understand", 0.3),
    ]),
    ("lekhan7", "लेखन", [_c("essay_letter7", "Essay and Letter Writing", "apply", 0.3)]),
]

HINDI8_CHAPTERS = [
    ("gadya8", "गद्य", [_c("lessons8", "Stories, Essays with Questions", "understand", 0.3)]),
    ("padya8", "पद्य", [_c("kavita8", "Poems with Deep Interpretation", "analyze", 0.3)]),
    ("vyakaran8", "व्याकरण", [
        _c("samas8", "समास — Compound Words", "apply", 0.3),
        _c("alankar", "अलंकार — Figures of Speech", "understand", 0.3),
        _c("sandhi8", "संधि", "apply", 0.35, ["vyakaran8.samas8"]),
    ]),
    ("lekhan8", "लेखन", [_c("essay_letter8", "Essay, Letter, Report Writing", "apply", 0.35)]),
]

HINDI9_CHAPTERS = [
    ("kshitij", "क्षितिज — Kshitij (Prose and Poetry)", [_c("lessons9", "Prose and Poetry with Questions", "understand", 0.3)]),
    ("kritika", "कृतिका — Kritika", [_c("stories9", "Stories — Comprehension and Analysis", "analyze", 0.35)]),
    ("vyakaran9", "व्याकरण", [_c("grammar_topics", "पद परिचय, रचना, वाक्य परिवर्तन", "apply", 0.35)]),
    ("lekhan9", "लेखन", [_c("writing9", "Essay, Letter, Dialogue Writing", "apply", 0.35)]),
]

HINDI10_CHAPTERS = [
    ("kshitij10", "क्षितिज — Kshitij", [_c("lessons10", "Prose and Poetry with Questions", "understand", 0.3)]),
    ("kritika10", "कृतिका — Kritika", [_c("stories10", "Stories — Analysis", "analyze", 0.35)]),
    ("vyakaran10", "व्याकरण", [_c("grammar10", "वाच्य, पद परिचय, रचना", "apply", 0.35)]),
    ("lekhan10", "लेखन", [_c("writing10", "Essay, Letter, Advertisement Writing", "apply", 0.35)]),
]

# ── Computer Science 11-12 ──
PYTHON_INTRO_CHAPTERS = [
    ("getting_started", "Getting Started with Python", [_c("variables_io", "Variables, Data Types, Input/Output", "apply", 0.2)]),
    ("operators", "Operators and Expressions", [_c("arithmetic_logical", "Arithmetic, Comparison and Logical Operators", "apply", 0.25)]),
    ("control_flow", "Control Flow", [_c("if_for_while", "if-elif-else, for, while Loops", "apply", 0.3)]),
    ("strings", "Strings", [_c("string_methods", "String Operations and Methods", "apply", 0.3)]),
    ("lists_tuples", "Lists and Tuples", [_c("list_operations", "List Operations and Comprehension", "apply", 0.35)]),
    ("dictionaries_sets", "Dictionaries and Sets", [_c("dict_methods", "Dictionary and Set Operations", "apply", 0.3)]),
    ("functions", "Functions", [_c("defining_scope", "Functions, Parameters, Scope, Lambda", "apply", 0.35)]),
    ("file_handling", "File Handling", [_c("read_write_csv", "File Read/Write, CSV, JSON", "apply", 0.35)]),
    ("error_handling", "Error Handling", [_c("try_except", "try, except, finally", "apply", 0.35)]),
    ("oop", "Object-Oriented Programming", [_c("classes_inheritance", "Classes, Objects, Inheritance", "apply", 0.45)]),
]

CS11_CHAPTERS = [
    ("computer_overview", "Computer System Overview", [_c("hardware_software", "Hardware, Software and OS", "understand", 0.25)]),
    ("encoding", "Encoding Schemes and Number Systems", [_c("binary_hex", "Binary, Octal, Hexadecimal, ASCII, Unicode", "apply", 0.3)]),
    ("python_basics", "Python Basics", [_c("data_types_operators", "Data Types, Operators, Expressions", "apply", 0.3)]),
    ("flow_control", "Flow of Control", [_c("conditional_loops", "Conditional Statements and Loops", "apply", 0.35)]),
    ("strings_lists", "Strings, Lists, Tuples, Dictionaries", [_c("data_structures", "Strings, Lists, Tuples, Dictionaries", "apply", 0.35)]),
    ("societal_impact", "Societal, Legal and Ethical Aspects", [_c("cybercrime_ethics", "Cybercrime, Ethics, IPR", "understand", 0.25)]),
]

CS12_CHAPTERS = [
    ("functions12", "Functions in Python", [_c("functions_scope", "Functions, Scope, Recursion", "apply", 0.4)]),
    ("file_handling12", "File Handling", [_c("text_binary_csv", "Text, Binary and CSV Files", "apply", 0.4)]),
    ("data_structures12", "Data Structures — Stacks and Queues", [_c("stack_queue", "Stack and Queue Implementation", "apply", 0.45)]),
    ("databases", "Database Concepts and SQL", [_c("sql_queries", "SQL — DDL, DML, Queries, Joins", "apply", 0.45)]),
    ("python_sql", "Python-Database Interface", [_c("mysql_connector", "Python-MySQL Connectivity", "apply", 0.45)]),
    ("networking", "Computer Networks", [_c("network_concepts", "Network Types, Protocols, Topologies", "understand", 0.35)]),
]

# ── Accountancy 11-12, Business Studies 11-12 ──
ACCOUNTANCY11_CHAPTERS = [
    ("accounting_intro", "Introduction to Accounting", [_c("meaning_terms", "Meaning, Objectives and Basic Terms", "understand", 0.25)]),
    ("accounting_theory", "Theory Base of Accounting", [_c("gaap_concepts", "GAAP, Concepts and Conventions", "understand", 0.3)]),
    ("journal_ledger", "Recording of Transactions", [_c("journal_ledger", "Journal Entries and Ledger Posting", "apply", 0.35)]),
    ("trial_balance", "Trial Balance and Rectification", [_c("trial_rectification", "Trial Balance and Error Rectification", "apply", 0.4)]),
    ("financial_statements", "Financial Statements", [_c("trading_pl_bs", "Trading A/c, P&L A/c, Balance Sheet", "apply", 0.4)]),
]

ACCOUNTANCY12_CHAPTERS = [
    ("partnership_fundamentals", "Accounting for Partnership — Fundamentals", [_c("profit_sharing", "Partnership Deed, Profit Sharing, Interest", "apply", 0.4)]),
    ("goodwill", "Goodwill: Nature and Valuation", [_c("goodwill_methods", "Methods of Goodwill Valuation", "apply", 0.4)]),
    ("reconstitution", "Reconstitution of Partnership", [_c("admission_retirement", "Admission, Retirement, Death of Partner", "apply", 0.5)]),
    ("dissolution", "Dissolution of Partnership Firm", [_c("dissolution_accounts", "Settlement of Accounts", "apply", 0.45)]),
    ("share_capital", "Accounting for Share Capital", [_c("issue_shares", "Issue and Forfeiture of Shares", "apply", 0.45)]),
    ("debentures", "Issue and Redemption of Debentures", [_c("issue_redemption", "Issue and Redemption of Debentures", "apply", 0.45)]),
    ("financial_statements12", "Financial Statements of a Company", [_c("statement_preparation", "Balance Sheet and Statement of P&L", "apply", 0.5)]),
    ("cash_flow", "Cash Flow Statement", [_c("cash_flow_prep", "Preparation of Cash Flow Statement", "apply", 0.5)]),
]

BUSINESS_STUDIES11_CHAPTERS = [
    ("nature_purpose", "Nature and Purpose of Business", [_c("business_concept", "Business, Profession, Employment", "understand", 0.2)]),
    ("forms_business", "Forms of Business Organisation", [_c("sole_partnership_company", "Sole Proprietorship, Partnership, Company", "understand", 0.3)]),
    ("public_private", "Public, Private and Global Enterprises", [_c("public_private_mnc", "Public Sector, Private Sector, MNCs", "understand", 0.3)]),
    ("business_services", "Business Services", [_c("banking_insurance", "Banking, Insurance and Communication", "understand", 0.3)]),
    ("emerging_modes", "Emerging Modes of Business", [_c("ecommerce_bpo", "E-Commerce, BPO, KPO", "understand", 0.3)]),
    ("social_responsibility", "Social Responsibility of Business", [_c("csr_ethics", "CSR and Business Ethics", "understand", 0.25)]),
    ("trade", "Internal and International Trade", [_c("domestic_international", "Domestic Trade and International Trade", "understand", 0.3)]),
]

BUSINESS_STUDIES12_CHAPTERS = [
    ("management", "Nature and Significance of Management", [_c("management_functions", "Management Functions and Levels", "understand", 0.3)]),
    ("principles_management", "Principles of Management", [_c("fayol_taylor", "Fayol's and Taylor's Principles", "understand", 0.35)]),
    ("business_environment", "Business Environment", [_c("economic_legal_political", "Economic, Legal and Political Environment", "understand", 0.3)]),
    ("planning", "Planning", [_c("planning_process", "Planning Process and Types of Plans", "understand", 0.3)]),
    ("organising", "Organising", [_c("structure_delegation", "Structure, Delegation and Decentralisation", "understand", 0.3)]),
    ("staffing", "Staffing", [_c("recruitment_training", "Recruitment, Selection and Training", "understand", 0.3)]),
    ("directing", "Directing", [_c("leadership_motivation", "Leadership, Motivation and Communication", "understand", 0.3)]),
    ("controlling", "Controlling", [_c("control_process", "Controlling Process and Techniques", "understand", 0.3)]),
    ("financial_management", "Financial Management", [_c("capital_structure", "Capital Structure and Financial Planning", "apply", 0.4)]),
    ("marketing", "Marketing Management", [_c("marketing_mix", "Marketing Mix — 4Ps", "apply", 0.35)]),
]

# ── Competitive Exams ──
JEE_MATH_CHAPTERS = [
    ("algebra", "Algebra", [_c("quadratic_matrices_pnc", "Quadratics, Matrices, P&C, Binomial", "apply", 0.55)]),
    ("calculus", "Calculus", [_c("limits_diff_int_de", "Limits, Differentiation, Integration, DEs", "apply", 0.6)]),
    ("coordinate_jee", "Coordinate Geometry", [_c("lines_circles_conics", "Lines, Circles, Conics", "apply", 0.55)]),
    ("vectors_3d", "Vectors and 3D Geometry", [_c("vectors_planes", "Vectors, Lines and Planes in 3D", "apply", 0.55)]),
    ("trigonometry_jee", "Trigonometry", [_c("trig_equations_inverse", "Trigonometric Equations and Inverse Trig", "apply", 0.55)]),
    ("probability_jee", "Probability and Statistics", [_c("prob_distributions", "Probability and Distributions", "apply", 0.55)]),
]

NEET_BIOLOGY_CHAPTERS = [
    ("diversity_living", "Diversity in Living World", [_c("taxonomy_kingdoms", "Taxonomy and Five Kingdoms", "apply", 0.4)]),
    ("cell_biology", "Cell Biology", [_c("cell_division_biomolecules", "Cell Structure, Division, Biomolecules", "apply", 0.45)]),
    ("plant_physiology", "Plant Physiology", [_c("photosynthesis_respiration", "Photosynthesis and Respiration", "apply", 0.5)]),
    ("human_physiology", "Human Physiology", [_c("digestion_circulation_excretion", "Digestion, Circulation, Excretion, Neural", "apply", 0.5)]),
    ("reproduction_neet", "Reproduction", [_c("plant_human_reproduction", "Plant and Human Reproduction", "apply", 0.4)]),
    ("genetics_neet", "Genetics and Evolution", [_c("mendelian_molecular_evolution", "Mendelian, Molecular Genetics, Evolution", "apply", 0.55)]),
    ("biotechnology_neet", "Biotechnology", [_c("rdna_applications", "rDNA, GM Crops, Gene Therapy", "apply", 0.5)]),
    ("ecology_neet", "Ecology", [_c("ecosystem_biodiversity_env", "Ecosystems, Biodiversity, Environmental Issues", "apply", 0.4)]),
]


# ══════════════════════════════════════════════════════════════════════════════
#  MASTER COURSE REGISTRY — ALL courses defined here
# ══════════════════════════════════════════════════════════════════════════════

def _course(cid, title, subject, grade, board, icon, color, desc, chapters):
    """Compact course definition helper."""
    return {
        "course_id": cid, "title": title, "subject": subject,
        "grade": grade, "board": board, "icon": icon, "color": color,
        "description": desc, "chapters": chapters,
    }


ALL_COURSES = [
    # ── Class 1 ─────────────────────────────────────────────────────────────
    _course("math1", "Class 1 Mathematics", "mathematics", 1, "NCERT", "🔢", "#F39C12",
            "NCERT Class 1 Mathematics — numbers, addition, subtraction, shapes, time, money.", MATH1_CHAPTERS),
    _course("english1", "Class 1 English", "english", 1, "NCERT", "📖", "#2C3E50",
            "NCERT Class 1 English — alphabet, phonics, simple words, sentences, stories.", ENGLISH1_CHAPTERS),
    _course("hindi1", "Class 1 Hindi", "hindi", 1, "NCERT", "🇮🇳", "#E74C3C",
            "NCERT Class 1 Hindi — वर्णमाला, मात्राएँ, शब्द रचना, कविता और कहानी.", HINDI1_CHAPTERS),
    _course("evs1", "Class 1 EVS", "evs", 1, "NCERT", "🌿", "#27AE60",
            "NCERT Class 1 EVS — family, body, plants, animals, food.", EVS1_CHAPTERS),

    # ── Class 2 ─────────────────────────────────────────────────────────────
    _course("math2", "Class 2 Mathematics", "mathematics", 2, "NCERT", "🔢", "#F39C12",
            "NCERT Class 2 Mathematics — numbers up to 100, addition, subtraction, shapes, time, money.", MATH2_CHAPTERS),
    _course("english2", "Class 2 English", "english", 2, "NCERT", "📖", "#2C3E50",
            "NCERT Class 2 English — reading, basic grammar, writing, vocabulary.", ENGLISH2_CHAPTERS),
    _course("hindi2", "Class 2 Hindi", "hindi", 2, "NCERT", "🇮🇳", "#E74C3C",
            "NCERT Class 2 Hindi — पढ़ना, लेखन, बुनियादी व्याकरण.", HINDI2_CHAPTERS),
    _course("evs2", "Class 2 EVS", "evs", 2, "NCERT", "🌿", "#27AE60",
            "NCERT Class 2 EVS — neighbourhood, plants, animals, water, safety.", EVS2_CHAPTERS),

    # ── Class 3 ─────────────────────────────────────────────────────────────
    _course("math3", "Class 3 Mathematics", "mathematics", 3, "NCERT", "🔢", "#F39C12",
            "NCERT Class 3 Mathematics — numbers up to 1000, multiplication, division, fractions, geometry.", MATH3_CHAPTERS),
    _course("english3", "Class 3 English", "english", 3, "NCERT", "📖", "#2C3E50",
            "NCERT Class 3 English — comprehension, grammar, writing, vocabulary.", ENGLISH3_CHAPTERS),
    _course("hindi3", "Class 3 Hindi", "hindi", 3, "NCERT", "🇮🇳", "#E74C3C",
            "NCERT Class 3 Hindi — पढ़ना, व्याकरण, लेखन.", HINDI3_CHAPTERS),
    _course("evs3", "Class 3 EVS", "evs", 3, "NCERT", "🌿", "#27AE60",
            "NCERT Class 3 EVS — family, food, shelter, travel, crafts.", EVS3_CHAPTERS),

    # ── Class 4 ─────────────────────────────────────────────────────────────
    _course("math4", "Class 4 Mathematics", "mathematics", 4, "NCERT", "🔢", "#F39C12",
            "NCERT Class 4 Mathematics — large numbers, fractions, decimals, geometry, data handling.", MATH4_CHAPTERS),
    _course("english4", "Class 4 English", "english", 4, "NCERT", "📖", "#2C3E50",
            "NCERT Class 4 English — reading, grammar, writing, vocabulary.", ENGLISH4_CHAPTERS),
    _course("hindi4", "Class 4 Hindi", "hindi", 4, "NCERT", "🇮🇳", "#E74C3C",
            "NCERT Class 4 Hindi — गद्य, पद्य, व्याकरण, लेखन.", HINDI4_CHAPTERS),
    _course("evs4", "Class 4 EVS", "evs", 4, "NCERT", "🌿", "#27AE60",
            "NCERT Class 4 EVS — food, water, environment, body, maps.", EVS4_CHAPTERS),

    # ── Class 5 ─────────────────────────────────────────────────────────────
    _course("math5", "Class 5 Mathematics", "mathematics", 5, "NCERT", "🔢", "#F39C12",
            "NCERT Class 5 Mathematics — large numbers, fractions, decimals, geometry, area, volume.", MATH5_CHAPTERS),
    _course("english5", "Class 5 English", "english", 5, "NCERT", "📖", "#2C3E50",
            "NCERT Class 5 English — reading, grammar, writing, vocabulary.", ENGLISH5_CHAPTERS),
    _course("hindi5", "Class 5 Hindi", "hindi", 5, "NCERT", "🇮🇳", "#E74C3C",
            "NCERT Class 5 Hindi — गद्य, पद्य, व्याकरण, लेखन.", HINDI5_CHAPTERS),
    _course("evs5", "Class 5 EVS", "evs", 5, "NCERT", "🌿", "#27AE60",
            "NCERT Class 5 EVS — senses, seeds, water, mapping, social topics.", EVS5_CHAPTERS),

    # ── Class 6 ─────────────────────────────────────────────────────────────
    _course("math6", "Class 6 Mathematics", "mathematics", 6, "NCERT", "🔢", "#4A90D9",
            "NCERT Class 6 Mathematics — numbers, geometry, integers, fractions, algebra, ratio.", MATH6_CHAPTERS),
    _course("science6", "Class 6 Science", "science", 6, "NCERT", "🔬", "#27AE60",
            "NCERT Class 6 Science — food, materials, plants, motion, light, electricity.", SCIENCE6_CHAPTERS),
    _course("english6", "Class 6 English", "english", 6, "NCERT", "📖", "#2C3E50",
            "NCERT Class 6 English — reading, grammar, writing, vocabulary.", ENGLISH_GRAMMAR_CHAPTERS),
    _course("hindi6", "Class 6 Hindi", "hindi", 6, "NCERT", "🇮🇳", "#E74C3C",
            "NCERT Class 6 Hindi — Vasant गद्य, पद्य, व्याकरण, लेखन.", HINDI6_CHAPTERS),
    _course("history6", "Class 6 History", "history", 6, "NCERT", "📜", "#C0392B",
            "NCERT Class 6 History — ancient India, earliest people, first cities, empires.", HISTORY6_CHAPTERS),
    _course("geography6", "Class 6 Geography", "geography", 6, "NCERT", "🌍", "#2980B9",
            "NCERT Class 6 Geography — earth, globe, maps, major domains.", GEOGRAPHY6_CHAPTERS),
    _course("civics6", "Class 6 Civics", "civics", 6, "NCERT", "⚖️", "#D35400",
            "NCERT Class 6 Civics — diversity, government, panchayati raj, livelihoods.", CIVICS6_CHAPTERS),

    # ── Class 7 ─────────────────────────────────────────────────────────────
    _course("math7", "Class 7 Mathematics", "mathematics", 7, "NCERT", "🔢", "#4A90D9",
            "NCERT Class 7 Mathematics — integers, fractions, algebra, geometry, data handling.", MATH7_CHAPTERS),
    _course("science7", "Class 7 Science", "science", 7, "NCERT", "🔬", "#27AE60",
            "NCERT Class 7 Science — nutrition, heat, acids, respiration, motion, light.", SCIENCE7_CHAPTERS),
    _course("hindi7", "Class 7 Hindi", "hindi", 7, "NCERT", "🇮🇳", "#E74C3C",
            "NCERT Class 7 Hindi — Vasant गद्य, पद्य, व्याकरण, लेखन.", HINDI7_CHAPTERS),
    _course("history7", "Class 7 History", "history", 7, "NCERT", "📜", "#C0392B",
            "NCERT Class 7 History — medieval India, Delhi Sultans, Mughals, Bhakti-Sufi.", HISTORY7_CHAPTERS),
    _course("geography7", "Class 7 Geography", "geography", 7, "NCERT", "🌍", "#2980B9",
            "NCERT Class 7 Geography — environment, earth's interior, air, water, vegetation.", GEOGRAPHY7_CHAPTERS),
    _course("civics7", "Class 7 Civics", "civics", 7, "NCERT", "⚖️", "#D35400",
            "NCERT Class 7 Civics — equality, government, gender, media, markets.", CIVICS7_CHAPTERS),

    # ── Class 8 ─────────────────────────────────────────────────────────────
    _course("math8", "Class 8 Mathematics", "mathematics", 8, "NCERT", "🔢", "#4A90D9",
            "NCERT Class 8 Mathematics — rational numbers, quadrilaterals, mensuration, algebra.", MATH8_CHAPTERS),
    _course("science8", "Class 8 Science", "science", 8, "NCERT", "🔬", "#27AE60",
            "NCERT Class 8 Science — microorganisms, metals, cell, force, sound, stars.", SCIENCE8_CHAPTERS),
    _course("hindi8", "Class 8 Hindi", "hindi", 8, "NCERT", "🇮🇳", "#E74C3C",
            "NCERT Class 8 Hindi — Vasant गद्य, पद्य, व्याकरण, लेखन.", HINDI8_CHAPTERS),
    _course("history8", "Class 8 History", "history", 8, "NCERT", "📜", "#C0392B",
            "NCERT Class 8 History — British rule, 1857 revolt, nationalism, independence.", HISTORY8_CHAPTERS),
    _course("geography8", "Class 8 Geography", "geography", 8, "NCERT", "🌍", "#2980B9",
            "NCERT Class 8 Geography — resources, agriculture, industries, human resources.", GEOGRAPHY8_CHAPTERS),
    _course("civics8", "Class 8 Civics", "civics", 8, "NCERT", "⚖️", "#D35400",
            "NCERT Class 8 Civics — constitution, secularism, parliament, judiciary.", CIVICS8_CHAPTERS),

    # ── Class 9 ─────────────────────────────────────────────────────────────
    _course("math9", "Class 9 Mathematics", "mathematics", 9, "NCERT", "📐", "#3B7DD8",
            "NCERT Class 9 Mathematics — number systems, polynomials, geometry, statistics.", MATH9_CHAPTERS),
    _course("science9", "Class 9 Science", "science", 9, "NCERT", "⚗️", "#229954",
            "NCERT Class 9 Science — matter, atoms, cells, motion, force, gravitation.", SCIENCE9_CHAPTERS),
    _course("hindi9", "Class 9 Hindi", "hindi", 9, "NCERT", "🇮🇳", "#E74C3C",
            "NCERT Class 9 Hindi — क्षितिज, कृतिका, व्याकरण, लेखन.", HINDI9_CHAPTERS),
    _course("history9", "Class 9 History", "history", 9, "NCERT", "📜", "#C0392B",
            "NCERT Class 9 History — French Revolution, Russian Revolution, Nazism.", HISTORY9_CHAPTERS),
    _course("geography9", "Class 9 Geography", "geography", 9, "NCERT", "🌍", "#2980B9",
            "NCERT Class 9 Geography — India — size, physical features, drainage, climate.", GEOGRAPHY9_CHAPTERS),
    _course("civics9", "Class 9 Civics", "civics", 9, "NCERT", "⚖️", "#D35400",
            "NCERT Class 9 Civics — democracy, constitution, elections, rights.", CIVICS9_CHAPTERS),
    _course("economics9", "Class 9 Economics", "economics", 9, "NCERT", "💰", "#F39C12",
            "NCERT Class 9 Economics — village economy, human capital, poverty, food security.", ECONOMICS9_CHAPTERS),

    # ── Class 10 ────────────────────────────────────────────────────────────
    _course("math10", "Class 10 Mathematics", "mathematics", 10, "NCERT", "📐", "#3B7DD8",
            "NCERT Class 10 Mathematics — real numbers, quadratics, trigonometry, statistics.", MATH10_CHAPTERS),
    _course("science10", "Class 10 Science", "science", 10, "NCERT", "⚗️", "#229954",
            "NCERT Class 10 Science — chemical reactions, life processes, electricity, light.", SCIENCE10_CHAPTERS),
    _course("hindi10", "Class 10 Hindi", "hindi", 10, "NCERT", "🇮🇳", "#E74C3C",
            "NCERT Class 10 Hindi — क्षितिज, कृतिका, व्याकरण, लेखन.", HINDI10_CHAPTERS),
    _course("history10", "Class 10 History", "history", 10, "NCERT", "📜", "#C0392B",
            "NCERT Class 10 History — nationalism in Europe and India, industrialisation.", HISTORY10_CHAPTERS),
    _course("geography10", "Class 10 Geography", "geography", 10, "NCERT", "🌍", "#2980B9",
            "NCERT Class 10 Geography — resources, water, agriculture, manufacturing.", GEOGRAPHY10_CHAPTERS),
    _course("civics10", "Class 10 Civics", "civics", 10, "NCERT", "⚖️", "#D35400",
            "NCERT Class 10 Civics — power sharing, federalism, political parties.", CIVICS10_CHAPTERS),
    _course("economics10", "Class 10 Economics", "economics", 10, "NCERT", "💰", "#F39C12",
            "NCERT Class 10 Economics — development, sectors, money, globalisation.", ECONOMICS10_CHAPTERS),

    # ── Class 11 ────────────────────────────────────────────────────────────
    _course("math11", "Class 11 Mathematics", "mathematics", 11, "NCERT", "∑", "#2E6EC7",
            "NCERT Class 11 Mathematics — sets, trigonometry, complex numbers, calculus, conics.", MATH11_CHAPTERS),
    _course("physics11", "Class 11 Physics", "physics", 11, "NCERT", "⚛️", "#8E44AD",
            "NCERT Class 11 Physics — mechanics, thermodynamics, oscillations, waves.", PHYSICS11_CHAPTERS),
    _course("chemistry11", "Class 11 Chemistry", "chemistry", 11, "NCERT", "🧪", "#E67E22",
            "NCERT Class 11 Chemistry — atomic structure, bonding, thermodynamics, organic.", CHEMISTRY11_CHAPTERS),
    _course("biology11", "Class 11 Biology", "biology", 11, "NCERT", "🧬", "#16A085",
            "NCERT Class 11 Biology — diversity, cell biology, plant and human physiology.", BIOLOGY11_CHAPTERS),
    _course("economics11", "Class 11 Economics", "economics", 11, "NCERT", "💰", "#F39C12",
            "NCERT Class 11 Indian Economic Development.", ECONOMICS11_CHAPTERS),
    _course("accountancy11", "Class 11 Accountancy", "accountancy", 11, "NCERT", "📊", "#1ABC9C",
            "NCERT Class 11 Accountancy — principles, journal, ledger, financial statements.", ACCOUNTANCY11_CHAPTERS),
    _course("business11", "Class 11 Business Studies", "business_studies", 11, "NCERT", "🏢", "#9B59B6",
            "NCERT Class 11 Business Studies — business forms, services, trade.", BUSINESS_STUDIES11_CHAPTERS),
    _course("polsci11", "Class 11 Political Science", "political_science", 11, "NCERT", "🏛️", "#2C3E50",
            "NCERT Class 11 Political Science — Indian Constitution at Work.", POLSCI11_CHAPTERS),
    _course("cs11", "Class 11 Computer Science", "computer_science", 11, "NCERT", "💻", "#3776AB",
            "NCERT Class 11 Computer Science — Python, encoding, computer systems.", CS11_CHAPTERS),

    # ── Class 12 ────────────────────────────────────────────────────────────
    _course("math12", "Class 12 Mathematics", "mathematics", 12, "NCERT", "∫", "#2E6EC7",
            "NCERT Class 12 Mathematics — relations, calculus, vectors, 3D, probability.", MATH12_CHAPTERS),
    _course("physics12", "Class 12 Physics", "physics", 12, "NCERT", "⚛️", "#8E44AD",
            "NCERT Class 12 Physics — electrostatics, current, optics, modern physics.", PHYSICS12_CHAPTERS),
    _course("chemistry12", "Class 12 Chemistry", "chemistry", 12, "NCERT", "🧪", "#E67E22",
            "NCERT Class 12 Chemistry — solutions, electrochemistry, organic, biomolecules.", CHEMISTRY12_CHAPTERS),
    _course("biology12", "Class 12 Biology", "biology", 12, "NCERT", "🧬", "#16A085",
            "NCERT Class 12 Biology — reproduction, genetics, evolution, biotechnology, ecology.", BIOLOGY12_CHAPTERS),
    _course("economics12", "Class 12 Economics", "economics", 12, "NCERT", "💰", "#F39C12",
            "NCERT Class 12 Macro/Micro Economics.", ECONOMICS12_CHAPTERS),
    _course("accountancy12", "Class 12 Accountancy", "accountancy", 12, "NCERT", "📊", "#1ABC9C",
            "NCERT Class 12 Accountancy — partnership, share capital, debentures, financial statements.", ACCOUNTANCY12_CHAPTERS),
    _course("business12", "Class 12 Business Studies", "business_studies", 12, "NCERT", "🏢", "#9B59B6",
            "NCERT Class 12 Business Studies — management, planning, organising, marketing.", BUSINESS_STUDIES12_CHAPTERS),
    _course("polsci12", "Class 12 Political Science", "political_science", 12, "NCERT", "🏛️", "#2C3E50",
            "NCERT Class 12 Political Science — Contemporary World Politics.", POLSCI12_CHAPTERS),
    _course("cs12", "Class 12 Computer Science", "computer_science", 12, "NCERT", "💻", "#3776AB",
            "NCERT Class 12 Computer Science — Python advanced, SQL, networking.", CS12_CHAPTERS),

    # ── General / Cross-Grade ───────────────────────────────────────────────
    _course("english_grammar", "English Grammar & Writing Skills", "english", 0, "General", "📝", "#34495E",
            "English grammar, comprehension and writing — suitable for classes 6-10.", ENGLISH_GRAMMAR_CHAPTERS),
    _course("python_intro", "Introduction to Python Programming", "computer_science", 0, "General", "🐍", "#3776AB",
            "Python programming from scratch — variables, loops, functions, OOP, files.", PYTHON_INTRO_CHAPTERS),

    # ── Competitive Exams ───────────────────────────────────────────────────
    _course("jee_math", "JEE Mathematics", "mathematics", 0, "JEE", "🎯", "#E74C3C",
            "JEE Main + Advanced Mathematics.", JEE_MATH_CHAPTERS),
    _course("neet_biology", "NEET Biology", "biology", 0, "NEET", "🎯", "#27AE60",
            "NEET Biology — comprehensive.", NEET_BIOLOGY_CHAPTERS),
]


# ══════════════════════════════════════════════════════════════════════════════
#  GENERATOR LOGIC — Pure template, course data above is pure DATA
# ══════════════════════════════════════════════════════════════════════════════

def _auto_description(title: str, chapter_title: str) -> str:
    return f"{title} — part of the chapter on {chapter_title}."


def _auto_key_ideas(title: str) -> list[str]:
    words = title.split("—")[0].strip() if "—" in title else title
    return [
        f"Core principles of {words.lower()}",
        f"Step-by-step problem solving for {words.lower()}",
        f"Real-world applications of {words.lower()}",
    ]


def build_curriculum(course_def: dict) -> dict:
    """Build a full curriculum JSON from compact seed data."""
    course_id = course_def["course_id"]
    chapters_out = []

    for ch_idx, (ch_key, ch_title, concepts) in enumerate(course_def["chapters"], 1):
        ch_id = f"ch{ch_idx:02d}"
        concepts_out = []

        for suffix, title, bloom, diff, prereqs in concepts:
            full_id = f"{course_id}.{ch_key}.{suffix}"
            resolved_prereqs = [f"{course_id}.{p}" for p in prereqs]

            concepts_out.append({
                "concept_id": full_id,
                "title": title,
                "bloom_level": bloom,
                "difficulty": round(diff, 2),
                "prerequisites": resolved_prereqs,
                "description": _auto_description(title, ch_title),
                "key_ideas": _auto_key_ideas(title),
            })

        chapters_out.append({
            "chapter_id": ch_id,
            "title": ch_title,
            "concepts": concepts_out,
        })

    return {
        "course_id": course_id,
        "title": course_def["title"],
        "chapters": chapters_out,
    }


def build_registry_entry(course_def: dict) -> dict:
    return {
        "course_id": course_def["course_id"],
        "title": course_def["title"],
        "subject": course_def["subject"],
        "grade": course_def["grade"],
        "board": course_def["board"],
        "language": "english",
        "icon": course_def["icon"],
        "color": course_def["color"],
        "description": course_def["description"],
        "curriculum_file": f"{course_def['course_id']}/curriculum.json",
        "status": "active",
    }


def generate_all():
    """Generate all curriculum JSON files and update courses.json."""
    print("🏗️  Generating NCERT K-12 course curricula...")

    registry_path = CONTENT_DIR / "courses.json"
    registry = {"courses": []}

    total_concepts = 0
    total_chapters = 0

    for course_def in ALL_COURSES:
        cid = course_def["course_id"]

        curriculum = build_curriculum(course_def)
        n_chapters = len(curriculum["chapters"])
        n_concepts = sum(len(ch["concepts"]) for ch in curriculum["chapters"])
        total_concepts += n_concepts
        total_chapters += n_chapters

        course_dir = CONTENT_DIR / cid
        course_dir.mkdir(parents=True, exist_ok=True)
        out_path = course_dir / "curriculum.json"
        with open(out_path, "w") as f:
            json.dump(curriculum, f, indent=2, ensure_ascii=False)

        registry["courses"].append(build_registry_entry(course_def))

        grade_str = f"Class {course_def['grade']:2d}" if course_def['grade'] else "General  "
        print(f"   {course_def['icon']} {grade_str} {cid:22s} — {n_chapters:2d} ch, {n_concepts:3d} concepts")

    registry["courses"].sort(key=lambda c: (c["grade"], c["course_id"]))

    with open(registry_path, "w") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)

    n_courses = len(registry["courses"])
    print(f"\n✅ Done! {n_courses} courses, {total_chapters} chapters, {total_concepts} seed concepts generated.")
    print(f"📁 Registry: {registry_path}")
    print(f"\n💡 Next: python -m tools.expand_with_gemini --all  (to expand with Gemini)")


if __name__ == "__main__":
    generate_all()
