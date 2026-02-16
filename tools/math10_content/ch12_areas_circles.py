"""Chapter 12 — Areas Related to Circles: 3 concepts, 15 questions."""
from .helpers import formula_box, step_box, tip_box, comparison_table, definition_box, key_point, info_box, svg_circle

LESSONS = {}
QUESTIONS = {}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1 · Perimeter and Area of a Circle (Basics)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.areas_circles.basics"] = {
    "title": "⭕ Circle Basics — Circumference and Area Revisited",
    "hook": "A circular garden has radius 7 m. How much fencing do you need? How much grass seed to cover it? These are the two fundamental circle calculations — and they both revolve around the magical number π!",
    "explanation": (
        formula_box("Circumference = 2πr = πd", "Perimeter of a circle")
        + formula_box("Area = πr²", "Area of a circle")
        + comparison_table(
            ["Quantity", "Formula", "Example (r = 7)", "Using π = 22/7"],
            [["Circumference", "2πr", "2 × 22/7 × 7 = 44 cm", "44 cm"],
             ["Area", "πr²", "22/7 × 49 = 154 cm²", "154 cm²"],
             ["Semicircle perimeter", "πr + 2r", "22 + 14 = 36 cm", "36 cm"],
             ["Semicircle area", "πr²/2", "77 cm²", "77 cm²"]]
        )
        + key_point("π ≈ 22/7 ≈ 3.14159... Use 22/7 when r is a multiple of 7. Use 3.14 otherwise.")
        + tip_box("Semicircle perimeter ≠ half the circumference! Don't forget the diameter (the straight edge).")
    ),
    "worked_example": (
        "<b>Example:</b> The wheels of a car have diameter 80 cm. How many complete revolutions does each wheel make in travelling 352 m?<br><br>"
        + step_box([
            ("Distance per revolution = circumference", "= πd = π × 80 = 80π cm"),
            ("Convert total distance", "352 m = 35200 cm"),
            ("Number of revolutions", "35200 / (80π) = 35200 / (80 × 22/7) = 35200 / (1760/7) = 35200 × 7/1760 = 140"),
        ])
    ),
    "try_this": {
        "question": "A wire is bent into a circle of radius 21 cm. If the same wire is bent into a square, find the side of the square.",
        "hint": "Wire length = circumference of circle = perimeter of square.",
        "answer": "Wire = 2π(21) = 2 × 22/7 × 21 = 132 cm. Side of square = 132/4 = 33 cm."
    },
    "fun_fact": "The Indian mathematician Aryabhata (476 AD) calculated π as 3.1416 — accurate to 4 decimal places — over 1500 years ago!"
}

QUESTIONS["math10.areas_circles.basics"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.areas_circles.basics"],
     "question": "Find the area and circumference of a circle with radius 14 cm. (Use π = 22/7)",
     "hint": "Area = πr², Circumference = 2πr.",
     "expected_answer": "Area = 22/7 × 14² = 22/7 × 196 = 616 cm². Circumference = 2 × 22/7 × 14 = 88 cm."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.areas_circles.basics"],
     "question": "The circumference of a circle is 44 cm. Find its area.",
     "hint": "2πr = 44 → r = 44/(2π).",
     "expected_answer": "2πr = 44 → r = 44/(2 × 22/7) = 44 × 7/44 = 7 cm. Area = 22/7 × 49 = 154 cm²."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.areas_circles.basics"],
     "question": "A circular park of radius 20 m has a path 5 m wide around it. Find the area of the path.",
     "hint": "Path area = Area of outer circle − Area of inner circle.",
     "expected_answer": "Outer radius = 25 m. Path area = π(25)² − π(20)² = π(625 − 400) = 225π ≈ 225 × 3.14 = 706.5 m²."},
    {"id": 4, "type": "word_problem", "difficulty": 0.6, "concepts_tested": ["math10.areas_circles.basics"],
     "question": "The minute hand of a clock is 14 cm long. Find the area swept by it in 5 minutes.",
     "hint": "In 5 minutes, the minute hand sweeps 5/60 × 360° = 30°. Area swept = sector area.",
     "expected_answer": "Angle = 30°. Area = (30/360) × πr² = (1/12) × 22/7 × 196 = (1/12) × 616 = 154/3 ≈ 51.33 cm²."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.areas_circles.basics"],
     "question": "A wire of length 44 cm is bent into a circle, then re-bent into a square. Which encloses more area and by how much?",
     "hint": "Circle: 2πr = 44 → r = 7. Square: 4s = 44 → s = 11.",
     "expected_answer": "Circle: r = 7, area = 154 cm². Square: s = 11, area = 121 cm². Circle encloses more by 154 − 121 = 33 cm². (A circle always encloses the maximum area for a given perimeter!)"},
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2 · Sectors and Segments
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.areas_circles.sector_segment"] = {
    "title": "🍕 Sectors and Segments — Slicing a Circle",
    "hook": "A sector is a 'pizza slice' of a circle. A segment is a region between a chord and an arc — like the shape of a cross-section of a tunnel. Let's master the formulas for both!",
    "explanation": (
        definition_box("Sector", "The region enclosed between two radii and an arc. Like a pizza slice. 🍕")
        + definition_box("Segment", "The region between a chord and its arc. Like a 'D' shape or a tunnel cross-section.")
        + formula_box("Arc length = (θ/360°) × 2πr", "Length of arc")
        + formula_box("Sector area = (θ/360°) × πr²", "Area of sector")
        + formula_box("Segment area = Sector area − Triangle area", "Area of minor segment")
        + comparison_table(
            ["Part", "Minor (< 180°)", "Major (> 180°)"],
            [["Arc", "Shorter arc", "Longer arc"],
             ["Sector", "Smaller region", "Larger region"],
             ["Segment", "Smaller region", "Larger region"]]
        )
        + key_point("Major sector area = πr² − Minor sector area.<br>Major segment area = πr² − Minor segment area.")
        + tip_box("Triangle area in a sector with angle θ: Area = ½r²sin θ (using the formula ½ab sin C with a = b = r).")
    ),
    "worked_example": (
        "<b>Example:</b> Find the area of a sector with radius 10 cm and angle 90°. Also find the area of the corresponding segment.<br><br>"
        + step_box([
            ("Sector area", "(90/360) × π(10)² = (1/4)(100π) = 25π ≈ 78.54 cm²"),
            ("Triangle area (right triangle)", "½ × 10 × 10 = 50 cm²"),
            ("Segment area", "Sector − Triangle = 25π − 50 ≈ 78.54 − 50 = 28.54 cm²"),
        ])
    ),
    "try_this": {
        "question": "Find the area of a sector of a circle of radius 21 cm with angle 60°. Also find the arc length.",
        "hint": "Sector area = (60/360) × πr². Arc = (60/360) × 2πr.",
        "answer": "Sector = (1/6) × 22/7 × 441 = (1/6) × 1386 = 231 cm². Arc = (1/6) × 2 × 22/7 × 21 = (1/6) × 132 = 22 cm."
    },
    "fun_fact": "The area formula (θ/360°) × πr² works because a sector is literally a 'fraction of a circle.' A 90° sector is 1/4 of the full circle, 60° is 1/6, and so on!"
}

QUESTIONS["math10.areas_circles.sector_segment"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.areas_circles.sector_segment"],
     "question": "Find the length of an arc of a circle of radius 7 cm which subtends an angle of 60° at the centre.",
     "hint": "Arc = (θ/360) × 2πr.",
     "expected_answer": "(60/360) × 2 × 22/7 × 7 = (1/6) × 44 = 22/3 ≈ 7.33 cm."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.areas_circles.sector_segment"],
     "question": "Find the area of a sector of radius 14 cm and angle 45°.",
     "hint": "Area = (45/360) × πr² = (1/8) × π × 196.",
     "expected_answer": "(1/8) × 22/7 × 196 = (1/8) × 616 = 77 cm²."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.areas_circles.sector_segment"],
     "question": "A chord of a circle of radius 12 cm subtends an angle of 120° at the centre. Find the area of the corresponding minor segment. (Use π = 3.14, √3 = 1.73.)",
     "hint": "Segment = Sector − Triangle. Sector = (120/360)πr². Triangle: angle = 120°, so area = ½r²sin120°.",
     "expected_answer": "Sector = (1/3) × 3.14 × 144 = 150.72 cm². Triangle = ½ × 144 × sin 120° = ½ × 144 × (√3/2) = 36√3 = 62.28 cm². Segment = 150.72 − 62.28 = 88.44 cm²."},
    {"id": 4, "type": "word_problem", "difficulty": 0.65, "concepts_tested": ["math10.areas_circles.sector_segment"],
     "question": "The minute hand of a clock is 21 cm long. Find the area swept by it between 6:00 AM and 6:35 AM.",
     "hint": "35 minutes → angle = 35/60 × 360° = 210°.",
     "expected_answer": "Angle = 210°. Area = (210/360) × 22/7 × 21² = (7/12) × 22/7 × 441 = (7/12) × 1386 = 808.5 cm²."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.areas_circles.sector_segment"],
     "question": "Find the area of the shaded region in a circle of radius 7 cm, if the shaded region is a segment corresponding to a chord that subtends 90° at the centre.",
     "hint": "Minor segment = sector (90°) − right triangle. Major segment = full circle − minor segment.",
     "expected_answer": "Sector = (90/360) × 22/7 × 49 = (1/4) × 154 = 38.5 cm². Triangle = ½ × 7 × 7 = 24.5 cm². Minor segment = 38.5 − 24.5 = 14 cm². Major segment = 154 − 14 = 140 cm²."},
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 3 · Areas of Combined Figures
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.areas_circles.combined_figures"] = {
    "title": "🎨 Combined Figures — Mixing Shapes Creatively",
    "hook": "A flower bed is shaped like a square with semicircles on each side. A running track has two straight sides and two semicircular ends. How do you find these areas? By combining and subtracting basic shapes!",
    "explanation": (
        "<p><b>Strategy for combined figures:</b></p>"
        + step_box([
            ("Identify the basic shapes", "Rectangles, triangles, circles, semicircles, sectors"),
            ("Decide: add or subtract?", "Shaded = Total − Unshaded, or sum of parts"),
            ("Calculate each part", "Use the appropriate formula"),
            ("Combine", "Add or subtract to get the final answer"),
        ], "#7B1FA2")
        + comparison_table(
            ["Common Pattern", "Formula"],
            [["Circle inside square", "Shaded = Square − Circle = s² − πr² (r = s/2)"],
             ["Square inside circle", "Shaded = Circle − Square = πr² − s² (s = r√2)"],
             ["Semicircles on square sides", "Add semicircle areas to square"],
             ["Track (rectangle + 2 semicircles)", "Area = l×w + πr² (two semicircles = one circle)"]]
        )
        + tip_box("Always draw and label the figure first. Break complex shapes into known shapes.")
    ),
    "worked_example": (
        "<b>Example:</b> Find the area of the shaded region where a circle of radius 7 cm is inscribed in a square.<br><br>"
        + step_box([
            ("Square side = diameter = 14 cm", "Area of square = 196 cm²"),
            ("Area of circle", "22/7 × 49 = 154 cm²"),
            ("Shaded = Square − Circle", "196 − 154 = 42 cm²"),
        ])
    ),
    "try_this": {
        "question": "A rectangular park 50 m × 30 m has semicircles drawn on each of the shorter sides. Find the total area.",
        "hint": "Two semicircles of diameter 30 m = one full circle of radius 15 m. Add to the rectangle.",
        "answer": "Rectangle = 50 × 30 = 1500 m². Two semicircles = π(15)² = 225π ≈ 706.86 m². Total = 1500 + 706.86 ≈ 2206.86 m²."
    },
    "fun_fact": "The Venn diagram (overlapping circles) is actually a combined figure problem! The overlapping area is found using the inclusion-exclusion principle — the same idea used here."
}

QUESTIONS["math10.areas_circles.combined_figures"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.areas_circles.combined_figures"],
     "question": "A square has side 14 cm. Four quadrants (quarter circles) of radius 7 cm are drawn at each corner. Find the area of the remaining region.",
     "hint": "4 quarter circles = 1 full circle. Remaining = Square − Circle.",
     "expected_answer": "Square = 14² = 196 cm². Four quadrants = πr² = 22/7 × 49 = 154 cm². Remaining = 196 − 154 = 42 cm²."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.areas_circles.combined_figures"],
     "question": "Find the area of a track which is a rectangle of 100 m × 40 m with a semicircle at each shorter end.",
     "hint": "Two semicircles of diameter 40 m = one full circle of radius 20 m.",
     "expected_answer": "Rectangle = 100 × 40 = 4000 m². Circle = π(20)² = 400π ≈ 1256.64 m². Total track area = 4000 + 1256.64 = 5256.64 m²."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.areas_circles.combined_figures"],
     "question": "A circle is inscribed in an equilateral triangle of side 12 cm. Find the area between the triangle and the circle. (Inradius = side/(2√3).)",
     "hint": "r = 12/(2√3) = 2√3 cm. Area of triangle = (√3/4) × 12².",
     "expected_answer": "r = 12/(2√3) = 2√3 cm. Triangle area = (√3/4)(144) = 36√3 ≈ 62.35 cm². Circle area = π(2√3)² = 12π ≈ 37.7 cm². Shaded = 62.35 − 37.7 = 24.65 cm²."},
    {"id": 4, "type": "word_problem", "difficulty": 0.65, "concepts_tested": ["math10.areas_circles.combined_figures"],
     "question": "In a circle of radius 21 cm, an equilateral triangle is inscribed. Find the area of the shaded region between them. (For inscribed equilateral triangle: side = r√3.)",
     "hint": "Side = 21√3. Triangle area = (√3/4)(21√3)². Circle area = πr².",
     "expected_answer": "Side = 21√3 cm. Triangle area = (√3/4)(21√3)² = (√3/4)(1323) = 1323√3/4 ≈ 572.76 cm². Circle area = 22/7 × 441 = 1386 cm². Shaded = 1386 − 572.76 = 813.24 cm²."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.areas_circles.combined_figures"],
     "question": "In a square of side 14 cm, four circles each of radius 3.5 cm are drawn, one centred at each corner. Also, a circle of radius 3.5 cm is drawn at the centre. Find the area not covered by any circle.",
     "hint": "At each corner, only a quarter-circle lies inside the square. The centre circle is fully inside.",
     "expected_answer": "Square = 196 cm². Four corner quarter-circles = 4 × (1/4)π(3.5)² = π(3.5)² = 22/7 × 12.25 = 38.5 cm². Centre circle = π(3.5)² = 38.5 cm². Total circle area inside = 38.5 + 38.5 = 77 cm². Uncovered = 196 − 77 = 119 cm²."},
]
