"""Chapter 7 — Coordinate Geometry: 3 concepts, 15 questions."""
from .helpers import formula_box, step_box, tip_box, comparison_table, key_point, info_box, svg_coordinate_grid

LESSONS = {}
QUESTIONS = {}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1 · Distance Formula
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.coord_geom.distance"] = {
    "title": "📏 Distance Formula — Measuring Across the Grid",
    "hook": "How far apart are two cities on a map if you can only measure horizontal and vertical distances? The distance formula — a direct application of Pythagoras — gives the 'straight line' distance between any two points!",
    "explanation": (
        "<p>The distance between two points <b>(x₁, y₁)</b> and <b>(x₂, y₂)</b>:</p>"
        + formula_box("d = √[(x₂ − x₁)² + (y₂ − y₁)²]", "Distance Formula")
        + svg_coordinate_grid(
            points=[(1, 2, "A(1,2)", "#1565C0"), (4, 6, "B(4,6)", "#E65100")],
            lines=[(1, 2, 4, 2, "#999"), (4, 2, 4, 6, "#999"), (1, 2, 4, 6, "#E65100")],
            xrange=(0, 6), yrange=(0, 7), width=240, height=200
        )
        + '<div style="text-align:center;font-size:0.8rem;color:#666">d = √[(4−1)² + (6−2)²] = √[9+16] = √25 = 5</div>'
        + key_point("<b>Special case:</b> Distance from origin: d = √(x² + y²)")
        + tip_box("To check collinearity: three points A, B, C are collinear if AB + BC = AC (or any permutation).")
    ),
    "worked_example": (
        "<b>Example:</b> Find the distance between (−3, 2) and (1, −1).<br><br>"
        + step_box([
            ("Apply formula", "d = √[(1−(−3))² + (−1−2)²]"),
            ("Compute", "= √[(4)² + (−3)²] = √[16 + 9] = √25 = 5"),
        ])
    ),
    "try_this": {
        "question": "Check if the points (1, 5), (2, 3), and (−2, −1) are collinear.",
        "hint": "Find all three distances. If AB + BC = AC (or similar), they're collinear.",
        "answer": "AB = √(1+4) = √5. BC = √(16+16) = √32 = 4√2. AC = √(9+36) = √45 = 3√5. AB + BC = √5 + 4√2 ≈ 2.24 + 5.66 = 7.90. AC = 3√5 ≈ 6.71. Since AB+BC ≠ AC (and no other combination works), they are NOT collinear."
    },
    "fun_fact": "GPS navigation uses a 3D version of this formula to calculate the distance between your phone and satellites orbiting Earth!"
}

QUESTIONS["math10.coord_geom.distance"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.coord_geom.distance"],
     "question": "Find the distance between (3, 4) and (−1, 1).",
     "hint": "d = √[(3−(−1))² + (4−1)²].",
     "expected_answer": "d = √[16 + 9] = √25 = 5."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.coord_geom.distance"],
     "question": "Find a point on the y-axis equidistant from (5, −2) and (−3, 2).",
     "hint": "Point on y-axis: (0, y). Set distance to (5,−2) = distance to (−3,2).",
     "expected_answer": "√(25 + (y+2)²) = √(9 + (y−2)²). Square: 25 + y²+4y+4 = 9 + y²−4y+4. 29 + 4y = 13 − 4y. 8y = −16. y = −2. Point: (0, −2)."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.coord_geom.distance"],
     "question": "Show that the points (1, 7), (4, 2), (−1, −1) and (−4, 4) are vertices of a square.",
     "hint": "Find all four sides and both diagonals. Square: all sides equal, diagonals equal.",
     "expected_answer": "AB = √(9+25) = √34. BC = √(25+9) = √34. CD = √(9+25) = √34. DA = √(25+9) = √34. All sides = √34. Diagonal AC = √(4+64) = √68. Diagonal BD = √(64+4) = √68. Diagonals equal. ∴ ABCD is a square."},
    {"id": 4, "type": "word_problem", "difficulty": 0.65, "concepts_tested": ["math10.coord_geom.distance"],
     "question": "Find the value of x if the distance between (x, 5) and (3, 1) is 5 units.",
     "hint": "√((x−3)² + 16) = 5. Square both sides.",
     "expected_answer": "(x−3)² + 16 = 25 → (x−3)² = 9 → x−3 = ±3. x = 6 or x = 0."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.coord_geom.distance"],
     "question": "Find the coordinates of a point equidistant from A(−5, 4), B(−1, −2), and C(5, 2). (This is the circumcentre of △ABC.)",
     "hint": "Let P(x,y). PA = PB → one equation. PA = PC → another. Solve simultaneously.",
     "expected_answer": "PA² = PB²: (x+5)²+(y−4)² = (x+1)²+(y+2)² → 10x−8y+25−16 = 2x+4y+1−4 → 8x−12y+12 = 0 → 2x−3y = −3 …(1). PA² = PC²: (x+5)²+(y−4)² = (x−5)²+(y−2)² → 10x−8y+41 = −10x−4y+29 → 20x−4y = −12 → 5x−y = −3 …(2). From (2): y = 5x+3. Sub in (1): 2x−15x−9 = −3 → −13x = 6 → x = −6/13. y = −30/13+3 = 9/13. Centre: (−6/13, 9/13)."},
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2 · Section Formula and Midpoint
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.coord_geom.section"] = {
    "title": "✂️ Section Formula — Finding Points that Divide Segments",
    "hook": "Where is the point that divides the line joining (2, 3) and (8, 9) in the ratio 2:1? It's not the midpoint — it's closer to (8, 9). The section formula tells you exactly where!",
    "explanation": (
        "<p>Point P dividing the line joining <b>A(x₁,y₁)</b> and <b>B(x₂,y₂)</b> in ratio <b>m:n</b>:</p>"
        + formula_box("P = ((mx₂ + nx₁)/(m+n), (my₂ + ny₁)/(m+n))", "Section Formula")
        + formula_box("Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2)", "Midpoint (when m = n = 1)")
        + formula_box("Centroid = ((x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3)", "Centroid of Triangle")
        + tip_box("The section formula uses 'cross-weighting': x-coordinate of P = (m × farther x + n × closer x) / (m+n).")
        + info_box("For <b>external division</b>, replace n with −n in the formula.")
    ),
    "worked_example": (
        "<b>Example:</b> Find the point dividing the join of (1, −2) and (4, 7) in ratio 2:1.<br><br>"
        + step_box([
            ("Identify", "A(1,−2), B(4,7), m:n = 2:1"),
            ("x-coordinate", "(2×4 + 1×1)/(2+1) = (8+1)/3 = 3"),
            ("y-coordinate", "(2×7 + 1×(−2))/(2+1) = (14−2)/3 = 4"),
            ("Result", "Point is (3, 4)"),
        ])
    ),
    "try_this": {
        "question": "Find the midpoint of A(−1, 5) and B(7, −3). Also find the centroid of the triangle with vertices (0, 0), (6, 0), (3, 9).",
        "hint": "Midpoint: average the coordinates. Centroid: average all three vertices.",
        "answer": "Midpoint = ((−1+7)/2, (5−3)/2) = (3, 1). Centroid = ((0+6+3)/3, (0+0+9)/3) = (3, 3)."
    },
    "fun_fact": "The centroid of a triangle is its 'center of gravity' — if you cut a triangle from cardboard and balance it on a pin at the centroid, it would balance perfectly!"
}

QUESTIONS["math10.coord_geom.section"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.coord_geom.section"],
     "question": "Find the midpoint of (4, −2) and (−8, 6).",
     "hint": "Average the x-coordinates and y-coordinates.",
     "expected_answer": "Midpoint = ((4−8)/2, (−2+6)/2) = (−2, 2)."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.coord_geom.section"],
     "question": "Find the point dividing the line joining (2, 3) and (7, 8) in ratio 3:2.",
     "hint": "P = ((3×7+2×2)/5, (3×8+2×3)/5).",
     "expected_answer": "x = (21+4)/5 = 5. y = (24+6)/5 = 6. Point: (5, 6)."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.coord_geom.section"],
     "question": "In what ratio does the point (3, 4) divide the segment joining (1, 2) and (7, 8)?",
     "hint": "Let ratio be k:1. Then 3 = (7k+1)/(k+1). Solve for k.",
     "expected_answer": "(7k+1)/(k+1) = 3 → 7k+1 = 3k+3 → 4k = 2 → k = 1/2. Ratio = 1/2 : 1 = 1:2."},
    {"id": 4, "type": "word_problem", "difficulty": 0.65, "concepts_tested": ["math10.coord_geom.section"],
     "question": "Find the ratio in which the y-axis divides the line joining A(−4, 6) and B(10, −3). Also find the point of intersection.",
     "hint": "On y-axis, x = 0. Use section formula: 0 = (10k − 4)/(k + 1).",
     "expected_answer": "0 = (10k − 4)/(k+1) → 10k = 4 → k = 2/5. Ratio = 2:5. y = (−3×2/5 + 6)/(2/5 + 1) = (−6/5 + 6)/(7/5) = (24/5)/(7/5) = 24/7. Point: (0, 24/7)."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.coord_geom.section"],
     "question": "Find the coordinates of the points that trisect (divide into 3 equal parts) the line segment joining (4, −1) and (−2, −3).",
     "hint": "First trisection point divides in 1:2, second in 2:1.",
     "expected_answer": "P₁ (ratio 1:2): x = (1×(−2)+2×4)/3 = 6/3 = 2. y = (1×(−3)+2×(−1))/3 = −5/3. P₁ = (2, −5/3). P₂ (ratio 2:1): x = (2×(−2)+1×4)/3 = 0/3 = 0. y = (2×(−3)+1×(−1))/3 = −7/3. P₂ = (0, −7/3)."},
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 3 · Area of Triangle (Coordinate)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.coord_geom.area_triangle"] = {
    "title": "📐 Area of a Triangle Using Coordinates",
    "hook": "You have three corners of a triangle on a map: (2, 1), (6, 1), and (4, 5). Without drawing it, can you find its area? There's a neat formula using just the coordinates!",
    "explanation": (
        "<p>Area of a triangle with vertices <b>(x₁,y₁), (x₂,y₂), (x₃,y₃)</b>:</p>"
        + formula_box("Area = ½ |x₁(y₂ − y₃) + x₂(y₃ − y₁) + x₃(y₁ − y₂)|", "Coordinate Area Formula")
        + key_point("Always take the <b>absolute value</b> (|...|) — area can't be negative!")
        + key_point("<b>Collinearity test:</b> If Area = 0, the three points lie on the same line (they're collinear).")
        + tip_box("Memory trick: Write coordinates as columns, multiply diagonally right−left, take half the absolute difference.")
    ),
    "worked_example": (
        "<b>Example:</b> Find the area of the triangle with vertices (1, 2), (4, 6), (7, 2).<br><br>"
        + step_box([
            ("Label coordinates", "(x₁,y₁)=(1,2), (x₂,y₂)=(4,6), (x₃,y₃)=(7,2)"),
            ("Apply formula", "Area = ½|1(6−2) + 4(2−2) + 7(2−6)|"),
            ("Compute", "= ½|4 + 0 + (−28)| = ½|−24| = ½ × 24 = 12 sq units"),
        ])
    ),
    "try_this": {
        "question": "Check if the points (1, 2), (3, 6), and (5, 10) are collinear.",
        "hint": "Find the area. If it's 0, they're collinear.",
        "answer": "Area = ½|1(6−10) + 3(10−2) + 5(2−6)| = ½|−4 + 24 − 20| = ½|0| = 0. Yes, they are collinear!"
    },
    "fun_fact": "This formula is actually the 'Shoelace Formula' — named because the cross-multiplication pattern looks like lacing up a shoe!"
}

QUESTIONS["math10.coord_geom.area_triangle"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.coord_geom.area_triangle"],
     "question": "Find the area of the triangle with vertices (0, 0), (4, 0), (0, 3).",
     "hint": "Apply the coordinate area formula, or note this is a right triangle.",
     "expected_answer": "Area = ½|0(0−3) + 4(3−0) + 0(0−0)| = ½|0+12+0| = 6. (Or: ½ × base × height = ½ × 4 × 3 = 6.)"},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.coord_geom.area_triangle"],
     "question": "Find the area of the triangle with vertices (2, 3), (−1, 0), (2, −4).",
     "hint": "Area = ½|x₁(y₂−y₃) + x₂(y₃−y₁) + x₃(y₁−y₂)|.",
     "expected_answer": "= ½|2(0+4) + (−1)(−4−3) + 2(3−0)| = ½|8 + 7 + 6| = ½(21) = 10.5 sq units."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.coord_geom.area_triangle"],
     "question": "For what value of k are the points (7, −2), (5, 1), and (3, k) collinear?",
     "hint": "Collinear means area = 0. Set the area formula to 0 and solve for k.",
     "expected_answer": "0 = ½|7(1−k) + 5(k+2) + 3(−2−1)|. 7−7k+5k+10−9 = 0. −2k+8 = 0. k = 4."},
    {"id": 4, "type": "word_problem", "difficulty": 0.65, "concepts_tested": ["math10.coord_geom.area_triangle"],
     "question": "Find the area of the quadrilateral with vertices A(1,1), B(7,−3), C(12,2), D(7,21) by splitting into two triangles.",
     "hint": "Split along diagonal AC: Area = Area(△ABC) + Area(△ACD).",
     "expected_answer": "△ABC: ½|1(−3−2)+7(2−1)+12(1+3)| = ½|−5+7+48| = 25. △ACD: ½|1(2−21)+12(21−1)+7(1−2)| = ½|−19+240−7| = ½(214) = 107. Total = 25+107 = 132 sq units."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.coord_geom.area_triangle"],
     "question": "If A(2, 1), B(6, 1), C(6, 5) are three vertices of a parallelogram ABCD, find vertex D and the area of the parallelogram.",
     "hint": "In a parallelogram, midpoints of diagonals are the same. Midpoint of AC = midpoint of BD.",
     "expected_answer": "Midpoint AC = ((2+6)/2, (1+5)/2) = (4, 3). If D = (x,y), midpoint BD = ((6+x)/2, (1+y)/2) = (4,3). So x = 2, y = 5. D = (2, 5). Area of parallelogram = 2 × Area(△ABC) = 2 × ½|2(1−5)+6(5−1)+6(1−1)| = |−8+24+0| = 16 sq units."},
]
