"""Chapter 6 — Triangles: 4 concepts, 20 questions."""
from .helpers import formula_box, step_box, tip_box, comparison_table, definition_box, key_point, info_box, warning_box, svg_right_triangle

LESSONS = {}
QUESTIONS = {}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1 · Basic Proportionality Theorem (BPT / Thales' Theorem)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.triangles10.bpt"] = {
    "title": "📐 Basic Proportionality Theorem — Lines Parallel to a Side",
    "hook": "Imagine slicing a triangle with a line parallel to its base. The two pieces you cut off have a magical property: the sides are divided in exactly the same ratio! This is the Basic Proportionality Theorem (BPT).",
    "explanation": (
        definition_box("BPT (Thales' Theorem)", "If a line is drawn parallel to one side of a triangle, it divides the other two sides <b>in the same ratio</b>.")
        + '<div style="text-align:center;margin:10px 0"><svg width="260" height="200"><polygon points="130,20 30,180 230,180" fill="#E8F5E9" stroke="#2E7D32" stroke-width="2"/><line x1="65" y1="120" x2="195" y2="120" stroke="#E65100" stroke-width="2" stroke-dasharray="6"/><text x="125" y="15" text-anchor="middle" font-weight="bold">A</text><text x="20" y="195" font-weight="bold">B</text><text x="235" y="195" font-weight="bold">C</text><text x="55" y="115" font-weight="bold" fill="#E65100">D</text><text x="200" y="115" font-weight="bold" fill="#E65100">E</text><text x="130" y="135" font-size="11" fill="#E65100">DE ∥ BC</text></svg></div>'
        + formula_box("DE ∥ BC  ⟹  AD/DB = AE/EC", "BPT")
        + "<p><b>Converse:</b> If AD/DB = AE/EC, then DE ∥ BC.</p>"
        + tip_box("BPT also means AD/AB = AE/AC = DE/BC — the line divides all three ratios proportionally.")
    ),
    "worked_example": (
        "<b>Example:</b> In △ABC, DE ∥ BC with AD = 4, DB = 6, AE = 3. Find EC.<br><br>"
        + step_box([
            ("Apply BPT", "AD/DB = AE/EC"),
            ("Substitute", "4/6 = 3/EC"),
            ("Cross-multiply", "4 × EC = 6 × 3 = 18"),
            ("Solve", "EC = 18/4 = 4.5 cm"),
        ])
    ),
    "try_this": {
        "question": "In △ABC, D is on AB and E is on AC. AD = 5, AB = 12, AE = 10. Find AC if DE ∥ BC.",
        "hint": "AD/AB = AE/AC. So 5/12 = 10/AC.",
        "answer": "AC = 10 × 12/5 = 24."
    },
    "fun_fact": "Thales of Miletus (624-546 BC) is said to have measured the height of the Great Pyramid using this very principle — by comparing the shadow of the pyramid with the shadow of a stick of known height!"
}

QUESTIONS["math10.triangles10.bpt"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.triangles10.bpt"],
     "question": "In △ABC, DE ∥ BC. If AD = 3 cm, DB = 5 cm, and AE = 4.5 cm, find EC.",
     "hint": "By BPT: AD/DB = AE/EC → 3/5 = 4.5/EC.",
     "expected_answer": "3/5 = 4.5/EC → EC = 4.5 × 5/3 = 7.5 cm."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.triangles10.bpt"],
     "question": "In △PQR, a line parallel to QR meets PQ at X and PR at Y. If PX = 4, XQ = 8, and PY = 3, find YR and PR.",
     "hint": "PX/XQ = PY/YR by BPT. Then PR = PY + YR.",
     "expected_answer": "4/8 = 3/YR → YR = 6. PR = 3 + 6 = 9."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.triangles10.bpt"],
     "question": "In △ABC, DE ∥ BC with D on AB. If AD = 2x−1, DB = 2x+1, AE = x, EC = x+2. Find x.",
     "hint": "BPT: AD/DB = AE/EC. Cross multiply and solve.",
     "expected_answer": "(2x−1)/(2x+1) = x/(x+2). Cross: (2x−1)(x+2) = x(2x+1). 2x²+4x−x−2 = 2x²+x. 2x²+3x−2 = 2x²+x. 2x = 2. x = 1."},
    {"id": 4, "type": "word_problem", "difficulty": 0.65, "concepts_tested": ["math10.triangles10.bpt"],
     "question": "ABCD is a trapezium with AB ∥ DC. Diagonals intersect at O. If AO = 6, OC = 4, OB = 9, find OD.",
     "hint": "In △AOB and △COD with AB ∥ DC: AO/OC = BO/OD (by BPT in the triangles formed).",
     "expected_answer": "AO/OC = BO/OD → 6/4 = 9/OD → OD = 36/6 = 6. So OD = 6."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.triangles10.bpt"],
     "question": "In △ABC, angle bisector of ∠A meets BC at D. Prove that BD/DC = AB/AC. (Given: AB = 6, AC = 8, BC = 7. Find BD and DC.)",
     "hint": "This is the Angle Bisector Property. With AB=6, AC=8: BD/DC = 6/8 = 3/4. And BD+DC = 7.",
     "expected_answer": "BD/DC = AB/AC = 6/8 = 3/4. Let BD = 3k, DC = 4k. 3k + 4k = 7 → k = 1. BD = 3, DC = 4."},
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2 · Criteria for Similarity
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.triangles10.similarity_criteria"] = {
    "title": "🔍 Similarity Criteria — AA, SSS, SAS",
    "hook": "Have you ever enlarged a photo? The bigger photo has the same shape but different size — every angle is the same, and all dimensions are scaled by the same factor. That's similarity in geometry!",
    "explanation": (
        definition_box("Similar Triangles", "Two triangles are similar if their corresponding angles are equal AND corresponding sides are proportional. Written: △ABC ~ △DEF.")
        + "<p><b>Three ways to prove triangles are similar:</b></p>"
        + comparison_table(
            ["Criterion", "What you need", "Example"],
            [["AA (Angle-Angle)", "Two pairs of equal angles", "∠A = ∠D and ∠B = ∠E → △ABC ~ △DEF"],
             ["SSS (Side-Side-Side)", "All three side ratios equal", "AB/DE = BC/EF = CA/FD"],
             ["SAS (Side-Angle-Side)", "One equal angle between proportional sides", "∠A = ∠D and AB/DE = AC/DF"]]
        )
        + key_point("If △ABC ~ △DEF, then: AB/DE = BC/EF = CA/FD (corresponding sides in the SAME order!).")
        + warning_box("The ORDER matters! △ABC ~ △DEF means A↔D, B↔E, C↔F. Write them in the correct correspondence!")
    ),
    "worked_example": (
        "<b>Example:</b> In △ABC and △PQR: ∠A = 50°, ∠B = 70°, ∠P = 50°, ∠R = 60°. Are they similar?<br><br>"
        + step_box([
            ("Find missing angles", "∠C = 180° − 50° − 70° = 60°. ∠Q = 180° − 50° − 60° = 70°."),
            ("Compare angles", "∠A = ∠P = 50°, ∠B = ∠Q = 70°, ∠C = ∠R = 60°"),
            ("By AA criterion", "△ABC ~ △PQR (all angles match in this order)"),
        ])
    ),
    "try_this": {
        "question": "△ABC has AB = 4, BC = 6, CA = 8. △DEF has DE = 2, EF = 3, FD = 4. Are they similar?",
        "hint": "Check if all side ratios are equal: AB/DE, BC/EF, CA/FD.",
        "answer": "AB/DE = 4/2 = 2, BC/EF = 6/3 = 2, CA/FD = 8/4 = 2. All ratios equal → △ABC ~ △DEF by SSS."
    },
    "fun_fact": "Similarity is the basis of map-making! Every map is a 'similar figure' to the actual land — same shape, different scale."
}

QUESTIONS["math10.triangles10.similarity_criteria"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.triangles10.similarity_criteria"],
     "question": "In △ABC and △DEF: ∠A = ∠D = 40° and ∠C = ∠F = 75°. Are they similar? If so, write the similarity.",
     "hint": "Two angle pairs equal → AA criterion.",
     "expected_answer": "∠B = 180−40−75 = 65° = ∠E. By AA: △ABC ~ △DEF."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.triangles10.similarity_criteria"],
     "question": "△ABC ~ △DEF with AB = 6, DE = 9, BC = 8. Find EF.",
     "hint": "Corresponding sides are proportional: AB/DE = BC/EF.",
     "expected_answer": "6/9 = 8/EF → EF = 9 × 8/6 = 12."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.triangles10.similarity_criteria"],
     "question": "A vertical pole 6 m tall casts a shadow 4 m long. At the same time, a tower casts a shadow 28 m long. Find the height of the tower.",
     "hint": "Same time → same sun angle → similar triangles. Height/Shadow ratio is constant.",
     "expected_answer": "6/4 = h/28 → h = 6 × 28/4 = 42 m."},
    {"id": 4, "type": "word_problem", "difficulty": 0.65, "concepts_tested": ["math10.triangles10.similarity_criteria"],
     "question": "In △ABC, ∠B = 90°, BD ⊥ AC. Prove △ADB ~ △ABC and find BD if AB = 12, BC = 5.",
     "hint": "In △ADB and △ABC: ∠A is common, ∠ADB = ∠ABC = 90°. So AA. AC = √(144+25) = 13.",
     "expected_answer": "∠A is common, ∠ADB = ∠ABC = 90° → △ADB ~ △ABC (AA). AC = √(12²+5²) = 13. Since △ADB ~ △ABC: BD/BC = AB/AC → BD/5 = 12/13 → BD = 60/13 ≈ 4.62 cm."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.triangles10.similarity_criteria"],
     "question": "In △ABC, DE ∥ BC where D is on AB and E on AC. If AD/DB = 2/3, find DE/BC.",
     "hint": "△ADE ~ △ABC (AA, since DE ∥ BC). Ratio = AD/AB.",
     "expected_answer": "AD/AB = 2/(2+3) = 2/5. Since △ADE ~ △ABC: DE/BC = AD/AB = 2/5. So DE = (2/5)BC."},
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 3 · Areas of Similar Triangles
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.triangles10.areas_similar"] = {
    "title": "📏 Areas of Similar Triangles — The Square Rule",
    "hook": "If you double every side of a triangle, what happens to its area? It doesn't just double — it quadruples! This is the 'square rule' for similar figures.",
    "explanation": (
        definition_box("Area Ratio Theorem", "The ratio of areas of two similar triangles equals the square of the ratio of their corresponding sides.")
        + formula_box("Area(△ABC) / Area(△DEF) = (AB/DE)² = (BC/EF)² = (CA/FD)²", "Area Ratio")
        + comparison_table(
            ["Side ratio", "Area ratio", "Example"],
            [["1:1", "1:1", "Congruent (same size)"],
             ["1:2", "1:4", "Double the sides → 4× the area"],
             ["2:3", "4:9", "Sides in ratio 2:3 → areas in 4:9"],
             ["3:5", "9:25", "Sides in ratio 3:5 → areas in 9:25"]]
        )
        + tip_box("This also works with altitudes, medians, and angle bisectors: area ratio = (altitude ratio)².")
    ),
    "worked_example": (
        "<b>Example:</b> △ABC ~ △PQR with AB = 8 cm, PQ = 12 cm. If Area(△ABC) = 32 cm², find Area(△PQR).<br><br>"
        + step_box([
            ("Side ratio", "AB/PQ = 8/12 = 2/3"),
            ("Area ratio", "(2/3)² = 4/9"),
            ("Set up equation", "32 / Area(△PQR) = 4/9"),
            ("Solve", "Area(△PQR) = 32 × 9/4 = 72 cm²"),
        ])
    ),
    "try_this": {
        "question": "Two similar triangles have areas 100 cm² and 64 cm². If a side of the larger is 20 cm, find the corresponding side of the smaller.",
        "hint": "Area ratio = (side ratio)². So side ratio = √(area ratio).",
        "answer": "(side/20)² = 64/100 → side/20 = 8/10 = 4/5 → side = 16 cm."
    },
    "fun_fact": "This 'square rule' extends to all similar shapes: if you triple the radius of a circle, the area becomes 9 times larger!"
}

QUESTIONS["math10.triangles10.areas_similar"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.triangles10.areas_similar"],
     "question": "△ABC ~ △DEF with sides in ratio 3:5. If Area(△ABC) = 36 cm², find Area(△DEF).",
     "hint": "Area ratio = (side ratio)² = (3/5)² = 9/25.",
     "expected_answer": "36/Area(DEF) = 9/25 → Area(DEF) = 36 × 25/9 = 100 cm²."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.triangles10.areas_similar"],
     "question": "The areas of two similar triangles are 81 cm² and 49 cm². If the altitude of the larger triangle is 63 cm, find the corresponding altitude of the smaller.",
     "hint": "Altitude ratio = √(area ratio).",
     "expected_answer": "Altitude ratio = √(49/81) = 7/9. Altitude = 63 × 7/9 = 49 cm."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.triangles10.areas_similar"],
     "question": "In △ABC, DE ∥ BC with AD/DB = 1/2. Find Area(△ADE)/Area(△ABC).",
     "hint": "△ADE ~ △ABC. AD/AB = 1/(1+2) = 1/3.",
     "expected_answer": "AD/AB = 1/3. Area ratio = (1/3)² = 1/9. So Area(△ADE) = (1/9) × Area(△ABC)."},
    {"id": 4, "type": "word_problem", "difficulty": 0.65, "concepts_tested": ["math10.triangles10.areas_similar"],
     "question": "△ABC ~ △DEF. Area(△ABC) = 225 cm², Area(△DEF) = 81 cm². If median BM of △ABC is 15 cm, find the corresponding median EN of △DEF.",
     "hint": "Median ratio = side ratio = √(area ratio).",
     "expected_answer": "Side ratio = √(81/225) = 9/15 = 3/5. Median EN/BM = 3/5. EN = 15 × 3/5 = 9 cm."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.triangles10.areas_similar"],
     "question": "Prove that the area of an equilateral triangle with side 2a is √3 a². Then find the ratio of areas of two equilateral triangles with sides 3 cm and 5 cm.",
     "hint": "Area of equilateral △ = (√3/4)×side². For sides 3 and 5: ratio = (3/5)².",
     "expected_answer": "Area = (√3/4)(2a)² = (√3/4)(4a²) = √3 a². Ratio of areas = (3/5)² = 9/25. (Or: Area₁ = (√3/4)×9 = 9√3/4, Area₂ = (√3/4)×25 = 25√3/4. Ratio = 9/25.)"},
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 4 · Pythagoras Theorem
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.triangles10.pythagoras"] = {
    "title": "📏 Pythagoras Theorem — The Most Famous Theorem in Math",
    "hook": "You're standing at the corner of a rectangular field 30 m × 40 m. Instead of walking along two sides, you cut diagonally. How far do you walk? The answer: √(30² + 40²) = 50 m. This is the Pythagoras Theorem — and it's the most-proved theorem in all of mathematics!",
    "explanation": (
        definition_box("Pythagoras Theorem", "In a right-angled triangle, the square of the hypotenuse equals the sum of squares of the other two sides.")
        + svg_right_triangle("a", "b", "c", "θ")
        + formula_box("c² = a² + b²  (hypotenuse² = base² + height²)", "Pythagoras")
        + "<p><b>Common Pythagorean Triplets:</b></p>"
        + comparison_table(
            ["a", "b", "c", "Check: a²+b²=c²"],
            [["3", "4", "5", "9+16=25 ✓"],
             ["5", "12", "13", "25+144=169 ✓"],
             ["8", "15", "17", "64+225=289 ✓"],
             ["7", "24", "25", "49+576=625 ✓"]]
        )
        + key_point("<b>Converse:</b> If c² = a² + b² in a triangle with sides a, b, c, then the angle opposite to c is 90°.")
        + tip_box("If c² > a²+b² → obtuse angle. If c² < a²+b² → acute angle.")
    ),
    "worked_example": (
        "<b>Example:</b> A ladder 13 m long leans against a wall. Its foot is 5 m from the wall. How high does it reach?<br><br>"
        + step_box([
            ("Identify", "Ladder = hypotenuse = 13, base = 5, height = ?"),
            ("Apply Pythagoras", "13² = 5² + h²"),
            ("Calculate", "169 = 25 + h² → h² = 144 → h = 12 m"),
        ])
    ),
    "try_this": {
        "question": "Is a triangle with sides 6, 8, 10 a right triangle?",
        "hint": "Check if the square of the largest side = sum of squares of the other two.",
        "answer": "10² = 100. 6² + 8² = 36 + 64 = 100. Yes, 100 = 100 → it IS a right triangle (with the right angle opposite the side of length 10)."
    },
    "fun_fact": "There are over 400 different proofs of the Pythagoras Theorem! One was even published by US President James Garfield in 1876."
}

QUESTIONS["math10.triangles10.pythagoras"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.triangles10.pythagoras"],
     "question": "Find the hypotenuse of a right triangle with legs 9 cm and 40 cm.",
     "hint": "c² = 9² + 40² = 81 + 1600.",
     "expected_answer": "c² = 81 + 1600 = 1681. c = √1681 = 41 cm."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.triangles10.pythagoras"],
     "question": "Determine whether a triangle with sides 7, 11, 13 is right-angled, acute, or obtuse.",
     "hint": "Compare 13² with 7² + 11². If equal → right, if less → acute, if more → obtuse.",
     "expected_answer": "13² = 169. 7² + 11² = 49 + 121 = 170. Since 169 < 170, the triangle is acute."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.triangles10.pythagoras"],
     "question": "A 17 m ladder reaches a window 15 m above the ground. How far is the foot of the ladder from the wall?",
     "hint": "17² = 15² + d². Solve for d.",
     "expected_answer": "d² = 17² − 15² = 289 − 225 = 64. d = 8 m."},
    {"id": 4, "type": "word_problem", "difficulty": 0.65, "concepts_tested": ["math10.triangles10.pythagoras"],
     "question": "In an equilateral triangle of side 2a, find the length of the altitude.",
     "hint": "The altitude bisects the base. So you get a right triangle with hypotenuse 2a and base a.",
     "expected_answer": "Altitude² = (2a)² − a² = 4a² − a² = 3a². Altitude = a√3."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.triangles10.pythagoras"],
     "question": "In a right triangle ABC, ∠B = 90°, BD is the altitude from B to AC. If AD = 4, DC = 9, find BD, AB, and BC.",
     "hint": "BD² = AD × DC (geometric mean relation). AB² = AD × AC. BC² = DC × AC.",
     "expected_answer": "AC = 4 + 9 = 13. BD² = AD × DC = 4 × 9 = 36 → BD = 6. AB² = AD × AC = 4 × 13 = 52 → AB = 2√13. BC² = DC × AC = 9 × 13 = 117 → BC = 3√13."},
]
