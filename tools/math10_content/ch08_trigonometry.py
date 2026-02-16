"""Chapter 8 — Introduction to Trigonometry: 4 concepts, 20 questions."""
from .helpers import formula_box, step_box, tip_box, comparison_table, definition_box, key_point, info_box, warning_box, svg_right_triangle

LESSONS = {}
QUESTIONS = {}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1 · Trigonometric Ratios
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.trig.ratios"] = {
    "title": "📐 Trigonometric Ratios — SOH CAH TOA",
    "hook": "You're standing 50 m from a building and looking up at a 60° angle to see the top. How tall is the building? The answer comes from trigonometry — the study of relationships between angles and sides in right triangles!",
    "explanation": (
        "<p>In a right triangle with an acute angle θ, we define six ratios:</p>"
        + svg_right_triangle("Opposite (O)", "Adjacent (A)", "Hypotenuse (H)", "θ")
        + comparison_table(
            ["Ratio", "Formula", "Memory Aid"],
            [["<b>sin θ</b>", "Opposite / Hypotenuse", "<b>S</b>OH"],
             ["<b>cos θ</b>", "Adjacent / Hypotenuse", "<b>C</b>AH"],
             ["<b>tan θ</b>", "Opposite / Adjacent", "<b>T</b>OA"],
             ["cosec θ", "1 / sin θ = H / O", "Reciprocal of sin"],
             ["sec θ", "1 / cos θ = H / A", "Reciprocal of cos"],
             ["cot θ", "1 / tan θ = A / O", "Reciprocal of tan"]]
        )
        + formula_box("SOH CAH TOA — the ultimate memory trick!", "Remember This!")
        + key_point("These ratios depend ONLY on the angle, not the size of the triangle. If the angle is the same, the ratio is the same — even if the triangle is bigger or smaller.")
        + warning_box("sin θ ≠ sin × θ. 'sin' is a function, not a number being multiplied.")
    ),
    "worked_example": (
        "<b>Example:</b> In △ABC, ∠B = 90°, AB = 5, BC = 12, AC = 13. Find all trig ratios of angle A.<br><br>"
        + step_box([
            ("Identify sides relative to ∠A", "Opposite = BC = 12, Adjacent = AB = 5, Hypotenuse = AC = 13"),
            ("sin A = O/H = 12/13", "cos A = A/H = 5/13"),
            ("tan A = O/A = 12/5", "cosec A = 13/12, sec A = 13/5, cot A = 5/12"),
        ])
    ),
    "try_this": {
        "question": "In a right triangle with hypotenuse 10 and one side 6, find sin θ and cos θ for the angle opposite the side of length 6.",
        "hint": "Find the third side using Pythagoras. Then apply SOH CAH TOA.",
        "answer": "Third side = √(100−36) = √64 = 8. sin θ = 6/10 = 3/5. cos θ = 8/10 = 4/5."
    },
    "fun_fact": "The word 'trigonometry' comes from Greek: 'trigonon' (triangle) + 'metron' (measure). It was originally developed by astronomers to calculate distances to stars!"
}

QUESTIONS["math10.trig.ratios"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.trig.ratios"],
     "question": "In a right triangle, the side opposite θ is 8 and hypotenuse is 17. Find sin θ, cos θ, and tan θ.",
     "hint": "Adjacent = √(17² − 8²) = √(289 − 64).",
     "expected_answer": "Adjacent = √225 = 15. sin θ = 8/17, cos θ = 15/17, tan θ = 8/15."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.trig.ratios"],
     "question": "If tan θ = 3/4, find sin θ and cos θ.",
     "hint": "Opposite = 3k, Adjacent = 4k. Hypotenuse = √(9k² + 16k²) = 5k.",
     "expected_answer": "H = √(9+16) = 5 (using k=1). sin θ = 3/5, cos θ = 4/5."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.trig.ratios"],
     "question": "If 3 cos θ = 2, find the value of (sin²θ + cos²θ)/(1 + tan²θ).",
     "hint": "cos θ = 2/3. sin²θ + cos²θ = 1 always. 1 + tan²θ = sec²θ.",
     "expected_answer": "sin²θ + cos²θ = 1. 1 + tan²θ = sec²θ = 1/cos²θ = 9/4. So the expression = 1/(9/4) = 4/9."},
    {"id": 4, "type": "word_problem", "difficulty": 0.65, "concepts_tested": ["math10.trig.ratios"],
     "question": "If sin θ = a/b, find sec θ + tan θ in terms of a and b.",
     "hint": "Draw a right triangle: O = a, H = b, A = √(b²−a²). Then compute sec and tan.",
     "expected_answer": "A = √(b²−a²). sec θ = b/√(b²−a²). tan θ = a/√(b²−a²). sec θ + tan θ = (a+b)/√(b²−a²) = (a+b)/√((b−a)(b+a)) = √((b+a)/(b−a))."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.trig.ratios"],
     "question": "In △PQR, ∠Q = 90°, PQ = 7, QR = 24. Find sin P, cos P, sin R, cos R. Verify that sin P = cos R.",
     "hint": "PR = √(49+576) = √625 = 25.",
     "expected_answer": "PR = 25. For ∠P: sin P = QR/PR = 24/25, cos P = PQ/PR = 7/25. For ∠R: sin R = PQ/PR = 7/25, cos R = QR/PR = 24/25. sin P = 24/25 = cos R? No — sin P = 24/25 and cos R = 24/25. ✓ (P and R are complementary: P + R = 90°.)"},
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2 · Standard Angles
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.trig.standard_angles"] = {
    "title": "📋 Trig Values of Standard Angles — The Must-Know Table",
    "hook": "There are five special angles whose trig values you should know by heart: 0°, 30°, 45°, 60°, and 90°. Memorizing this one table unlocks most trigonometry problems!",
    "explanation": (
        comparison_table(
            ["θ", "0°", "30°", "45°", "60°", "90°"],
            [["<b>sin θ</b>", "0", "1/2", "1/√2", "√3/2", "1"],
             ["<b>cos θ</b>", "1", "√3/2", "1/√2", "1/2", "0"],
             ["<b>tan θ</b>", "0", "1/√3", "1", "√3", "∞ (undefined)"]]
        )
        + tip_box("<b>Pattern for sin:</b> √0/2, √1/2, √2/2, √3/2, √4/2 → 0, 1/2, 1/√2, √3/2, 1. <b>cos is sin reversed!</b>")
        + info_box("1/√2 = √2/2 ≈ 0.707.  1/√3 = √3/3 ≈ 0.577.  √3/2 ≈ 0.866.")
        + key_point("Quick check: sin increases from 0° to 90°. cos decreases from 0° to 90°. tan increases and blows up at 90°.")
    ),
    "worked_example": (
        "<b>Example:</b> Evaluate: 2 sin 30° + 3 cos 60° − tan 45°.<br><br>"
        + step_box([
            ("Substitute values", "2(1/2) + 3(1/2) − 1"),
            ("Compute", "1 + 3/2 − 1 = 3/2 = 1.5"),
        ])
        + "<br><b>Example 2:</b> If sin(A + B) = 1 and cos(A − B) = 1, find A and B.<br><br>"
        + step_box([
            ("sin(A+B) = 1", "A + B = 90°"),
            ("cos(A−B) = 1", "A − B = 0° → A = B"),
            ("Solve", "2A = 90° → A = B = 45°"),
        ])
    ),
    "try_this": {
        "question": "Find the value of: tan²60° + 4cos²45° − 3sec²30° − cot²60°.",
        "hint": "tan 60° = √3, cos 45° = 1/√2, sec 30° = 2/√3, cot 60° = 1/√3.",
        "answer": "(√3)² + 4(1/√2)² − 3(2/√3)² − (1/√3)² = 3 + 4(1/2) − 3(4/3) − 1/3 = 3 + 2 − 4 − 1/3 = 1 − 1/3 = 2/3."
    },
    "fun_fact": "In ancient India, mathematicians used 'jya' (sine) and 'koti-jya' (cosine) — the word 'sine' comes from a mistranslation of the Arabic version of 'jya'!"
}

QUESTIONS["math10.trig.standard_angles"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.trig.standard_angles"],
     "question": "Evaluate: sin²30° + cos²60°.",
     "hint": "sin 30° = 1/2, cos 60° = 1/2.",
     "expected_answer": "(1/2)² + (1/2)² = 1/4 + 1/4 = 1/2."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.trig.standard_angles"],
     "question": "Find the value of: (2 tan 30°)/(1 + tan²30°).",
     "hint": "tan 30° = 1/√3. So tan²30° = 1/3.",
     "expected_answer": "(2/√3)/(1 + 1/3) = (2/√3)/(4/3) = (2/√3)(3/4) = 6/(4√3) = 3/(2√3) = √3/2."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.trig.standard_angles"],
     "question": "If sin(A−B) = 1/2 and cos(A+B) = 1/2, where A > B > 0°, find A and B.",
     "hint": "sin 30° = 1/2 and cos 60° = 1/2. So A−B = 30° and A+B = 60°.",
     "expected_answer": "A − B = 30° …(1). A + B = 60° …(2). Add: 2A = 90° → A = 45°. B = 15°."},
    {"id": 4, "type": "word_problem", "difficulty": 0.65, "concepts_tested": ["math10.trig.standard_angles"],
     "question": "Verify: cos 60° = 1 − 2sin²30° = 2cos²30° − 1.",
     "hint": "Just substitute the values and check both sides.",
     "expected_answer": "cos 60° = 1/2. 1 − 2sin²30° = 1 − 2(1/4) = 1 − 1/2 = 1/2 ✓. 2cos²30° − 1 = 2(3/4) − 1 = 3/2 − 1 = 1/2 ✓."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.trig.standard_angles"],
     "question": "In △ABC, ∠C = 90°. If tan A = 1/√3, find sin A cos B + cos A sin B.",
     "hint": "tan A = 1/√3 → A = 30°. Since C = 90°, B = 60°. Or recognize sin A cos B + cos A sin B = sin(A+B).",
     "expected_answer": "A = 30°, B = 60°. sin A cos B + cos A sin B = sin(30°)cos(60°) + cos(30°)sin(60°) = (1/2)(1/2) + (√3/2)(√3/2) = 1/4 + 3/4 = 1. (This is sin(A+B) = sin 90° = 1.)"},
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 3 · Complementary Angle Identities
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.trig.complementary"] = {
    "title": "🔄 Complementary Angles — sin and cos are Partners!",
    "hook": "Notice how sin 30° = 1/2 = cos 60°? And sin 60° = cos 30°? This isn't coincidence — when two angles add up to 90°, they have a beautiful mirror relationship!",
    "explanation": (
        definition_box("Complementary Angles", "Two angles are complementary if they add up to 90°. In a right triangle, the two acute angles are always complementary.")
        + "<p><b>The six complementary identities:</b></p>"
        + comparison_table(
            ["Identity", "Example"],
            [["sin(90° − θ) = cos θ", "sin 72° = cos 18°"],
             ["cos(90° − θ) = sin θ", "cos 55° = sin 35°"],
             ["tan(90° − θ) = cot θ", "tan 80° = cot 10°"],
             ["cot(90° − θ) = tan θ", "cot 75° = tan 15°"],
             ["sec(90° − θ) = cosec θ", "sec 40° = cosec 50°"],
             ["cosec(90° − θ) = sec θ", "cosec 25° = sec 65°"]]
        )
        + key_point("<b>Why?</b> In a right triangle: the side opposite one acute angle is the side adjacent to the other. So sin of one angle = cos of its complement.")
        + tip_box("If you see sin 72°, think: 'That's the same as cos 18°' (since 72° + 18° = 90°).")
    ),
    "worked_example": (
        "<b>Example:</b> Evaluate: sin 25° cos 65° + cos 25° sin 65°.<br><br>"
        + step_box([
            ("Notice complementary pairs", "25° + 65° = 90°"),
            ("Apply identities", "cos 65° = sin 25° and sin 65° = cos 25°"),
            ("Substitute", "sin 25° · sin 25° + cos 25° · cos 25° = sin²25° + cos²25° = 1"),
        ])
    ),
    "try_this": {
        "question": "Without tables, evaluate: tan 1° · tan 2° · tan 3° · ... · tan 89°.",
        "hint": "Pair: tan 1° with tan 89° = cot 1°. What is tan θ × cot θ?",
        "answer": "tan θ × tan(90°−θ) = tan θ × cot θ = 1 for each pair. Pairs: (1°,89°), (2°,88°), ..., (44°,46°). The middle is tan 45° = 1. Total = 1⁴⁴ × 1 = 1."
    },
    "fun_fact": "The prefix 'co' in cosine literally means 'complement' — cosine is the 'sine of the complement'!"
}

QUESTIONS["math10.trig.complementary"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.trig.complementary"],
     "question": "Evaluate: cos 48° − sin 42°.",
     "hint": "48° + 42° = 90°. So cos 48° = sin 42°.",
     "expected_answer": "cos 48° = sin(90°−48°) = sin 42°. So cos 48° − sin 42° = 0."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.trig.complementary"],
     "question": "If tan 2A = cot(A − 18°), find A (where 2A is acute).",
     "hint": "tan θ = cot(90°−θ). So 2A and (A−18°) are complementary: 2A + (A−18°) = 90°.",
     "expected_answer": "2A + A − 18° = 90° → 3A = 108° → A = 36°."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.trig.complementary"],
     "question": "Express sec 70° + cosec 20° in terms of trigonometric ratios of angles between 0° and 45°.",
     "hint": "sec 70° = cosec(90°−70°) = cosec 20°. But wait — we need angles < 45°.",
     "expected_answer": "sec 70° = cosec 20°. So sec 70° + cosec 20° = 2 cosec 20°. To express in terms of < 45°: cosec 20° = sec 70° = sec 70°. 20° is already < 45°, so: 2 cosec 20°."},
    {"id": 4, "type": "word_problem", "difficulty": 0.65, "concepts_tested": ["math10.trig.complementary"],
     "question": "Prove: (cos 80°)/(sin 10°) + cos 59° · cosec 31° = 2.",
     "hint": "cos 80° = sin 10° (since 80°+10°=90°). cosec 31° = sec 59° (since 31°+59°=90°).",
     "expected_answer": "cos 80° = sin 10° → cos 80°/sin 10° = 1. cos 59° · cosec 31° = cos 59° · sec 59° (since cosec 31° = sec(90°−31°) = sec 59°). Wait: cosec 31° = 1/sin 31° = 1/cos 59°. So cos 59°/cos 59° = 1. Total = 1 + 1 = 2. ∎"},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.trig.complementary"],
     "question": "If sin 3A = cos(A − 26°), find A (where 3A is acute).",
     "hint": "sin θ = cos(90°−θ). So 3A and (A−26°) should sum to 90°.",
     "expected_answer": "sin 3A = cos(90°−3A). So cos(90°−3A) = cos(A−26°). Therefore 90°−3A = A−26° → 116° = 4A → A = 29°. Check: sin 87° = cos 3° ✓ (87°+3° = 90°)."},
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 4 · Trigonometric Identities
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.trig.identities"] = {
    "title": "🔐 Trigonometric Identities — Equations True for ALL Angles",
    "hook": "sin²θ + cos²θ = 1. Always. No matter what θ is — 17°, 42.3°, or even π/7 radians. These 'identities' are universal truths, and they're the key to solving complex trig expressions.",
    "explanation": (
        "<p><b>The Three Fundamental Identities:</b></p>"
        + formula_box("sin²θ + cos²θ = 1", "Identity 1 (Pythagorean)")
        + formula_box("1 + tan²θ = sec²θ", "Identity 2 (divide Identity 1 by cos²θ)")
        + formula_box("1 + cot²θ = cosec²θ", "Identity 3 (divide Identity 1 by sin²θ)")
        + comparison_table(
            ["From Identity 1", "Rearrangement"],
            [["sin²θ = 1 − cos²θ", "Useful to eliminate sin"],
             ["cos²θ = 1 − sin²θ", "Useful to eliminate cos"],
             ["tan²θ = sec²θ − 1", "Useful in sec-tan problems"],
             ["cot²θ = cosec²θ − 1", "Useful in cosec-cot problems"]]
        )
        + "<p><b>Strategy for proving identities:</b></p>"
        + step_box([
            ("Start from one side (usually the more complex one)", ""),
            ("Convert everything to sin and cos", "tan = sin/cos, sec = 1/cos, etc."),
            ("Simplify using algebra", "Factor, combine fractions, use a²−b² = (a+b)(a−b)"),
            ("Reach the other side", "If stuck, try working from BOTH sides toward the middle"),
        ], "#7B1FA2")
    ),
    "worked_example": (
        "<b>Prove:</b> (1 + tan²θ)/(1 + cot²θ) = tan²θ.<br><br>"
        + step_box([
            ("Use identities on top and bottom", "Top: 1 + tan²θ = sec²θ. Bottom: 1 + cot²θ = cosec²θ."),
            ("Simplify", "sec²θ / cosec²θ = (1/cos²θ) / (1/sin²θ)"),
            ("", "= sin²θ / cos²θ = tan²θ ∎"),
        ])
    ),
    "try_this": {
        "question": "Prove: (sin θ − cos θ)² + (sin θ + cos θ)² = 2.",
        "hint": "Expand both squares and use sin²θ + cos²θ = 1.",
        "answer": "LHS = (sin²θ − 2sinθcosθ + cos²θ) + (sin²θ + 2sinθcosθ + cos²θ) = 1 − 2sinθcosθ + 1 + 2sinθcosθ = 2. ∎"
    },
    "fun_fact": "The identity sin²θ + cos²θ = 1 is actually the Pythagoras theorem in disguise — in a unit circle (radius 1), the x-coordinate is cos θ and y-coordinate is sin θ, so x² + y² = 1!"
}

QUESTIONS["math10.trig.identities"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.trig.identities"],
     "question": "If sin θ = 3/5, find cos θ and tan θ using identities.",
     "hint": "cos²θ = 1 − sin²θ = 1 − 9/25.",
     "expected_answer": "cos²θ = 1 − 9/25 = 16/25 → cos θ = 4/5 (θ acute). tan θ = sin θ/cos θ = (3/5)/(4/5) = 3/4."},
    {"id": 2, "type": "direct", "difficulty": 0.45, "concepts_tested": ["math10.trig.identities"],
     "question": "Simplify: (1 − sin²θ) · sec²θ.",
     "hint": "1 − sin²θ = cos²θ. sec²θ = 1/cos²θ.",
     "expected_answer": "cos²θ × (1/cos²θ) = 1."},
    {"id": 3, "type": "word_problem", "difficulty": 0.55, "concepts_tested": ["math10.trig.identities"],
     "question": "Prove: (1 + tan²θ)(1 − sin θ)(1 + sin θ) = 1.",
     "hint": "(1−sinθ)(1+sinθ) = 1−sin²θ = cos²θ. And 1+tan²θ = sec²θ.",
     "expected_answer": "LHS = sec²θ × cos²θ = (1/cos²θ) × cos²θ = 1. ∎"},
    {"id": 4, "type": "word_problem", "difficulty": 0.7, "concepts_tested": ["math10.trig.identities"],
     "question": "Prove: (cosec θ − cot θ)² = (1 − cos θ)/(1 + cos θ).",
     "hint": "Convert LHS to sin/cos: cosec θ − cot θ = (1−cos θ)/sin θ.",
     "expected_answer": "LHS = ((1−cosθ)/sinθ)² = (1−cosθ)²/sin²θ = (1−cosθ)²/(1−cos²θ) = (1−cosθ)²/((1−cosθ)(1+cosθ)) = (1−cosθ)/(1+cosθ) = RHS. ∎"},
    {"id": 5, "type": "transfer_task", "difficulty": 0.85, "concepts_tested": ["math10.trig.identities"],
     "question": "Prove: (sin θ + cosec θ)² + (cos θ + sec θ)² = 7 + tan²θ + cot²θ.",
     "hint": "Expand each square. Use sin θ · cosec θ = 1 and cos θ · sec θ = 1.",
     "expected_answer": "LHS = sin²θ + 2·sin θ·cosecθ + cosec²θ + cos²θ + 2·cosθ·secθ + sec²θ = sin²θ+cos²θ + 2 + 2 + cosec²θ + sec²θ = 1 + 4 + (1+cot²θ) + (1+tan²θ) = 7 + tan²θ + cot²θ = RHS. ∎"},
]
