"""Chapter 2 — Polynomials: 3 concepts, 15 questions."""
from .helpers import formula_box, step_box, tip_box, comparison_table, definition_box, key_point, info_box, warning_box, svg_coordinate_grid

LESSONS = {}
QUESTIONS = {}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1 · Geometrical Meaning of Zeroes
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.polynomials10.types_and_zeroes"] = {
    "title": "📈 Geometrical Meaning of Zeroes — Where Graphs Meet the X-axis",
    "hook": "When you throw a ball, its height follows a parabola (a quadratic). The ball starts on the ground, rises, then comes back down. The two points where it touches the ground? Those are the 'zeroes' of the quadratic equation for its height!",
    "explanation": (
        definition_box("Zero of a Polynomial", "A number c is a zero of polynomial p(x) if p(c) = 0. Graphically, the zeroes are the x-coordinates where the graph of y = p(x) crosses or touches the x-axis.")
        + "<br><b>Types by Degree:</b>"
        + comparison_table(
            ["Type", "Degree", "General Form", "Max Zeroes", "Graph Shape"],
            [["Linear", "1", "ax + b", "1", "Straight line"],
             ["Quadratic", "2", "ax² + bx + c", "2", "Parabola (U-shape)"],
             ["Cubic", "3", "ax³ + bx² + cx + d", "3", "S-curve"]]
        )
        + "<br><b>Quadratic graph cases:</b>"
        + comparison_table(
            ["Case", "Graph crosses x-axis", "Number of zeroes", "Example"],
            [["Two distinct zeroes", "At 2 points", "2", "x² − 5x + 6 → zeroes 2, 3"],
             ["One repeated zero", "Touches at 1 point", "1 (repeated)", "x² − 4x + 4 → zero 2 (twice)"],
             ["No real zeroes", "Doesn't cross x-axis", "0", "x² + 1 → no real zeroes"]]
        )
        + tip_box("A polynomial of degree n has <b>at most n</b> zeroes. It can have fewer!")
        + svg_coordinate_grid(
            points=[(2, 0, "(2,0)", "#E65100"), (3, 0, "(3,0)", "#E65100"), (2.5, -0.25, "min", "#1565C0")],
            lines=[(-1, 12, 0, 6, "#4A90D9"), (0, 6, 1, 2, "#4A90D9"), (1, 2, 2, 0, "#4A90D9"),
                   (2, 0, 3, 0, "#4A90D9"), (3, 0, 4, 2, "#4A90D9"), (4, 2, 5, 6, "#4A90D9")],
            xrange=(-1, 5), yrange=(-1, 8), width=260, height=200
        )
        + '<div style="text-align:center;font-size:0.8rem;color:#666">Graph of x² − 5x + 6: crosses x-axis at x = 2 and x = 3</div>'
    ),
    "worked_example": (
        "<b>Example:</b> Find the zeroes of p(x) = x² − 3x − 10 and verify.<br><br>"
        + step_box([
            ("Factor the polynomial", "x² − 3x − 10 = (x − 5)(x + 2) [since −5 × 2 = −10, −5 + 2 = −3]"),
            ("Set each factor = 0", "x − 5 = 0 → x = 5;  x + 2 = 0 → x = −2"),
            ("Verify x = 5", "p(5) = 25 − 15 − 10 = 0 ✓"),
            ("Verify x = −2", "p(−2) = 4 + 6 − 10 = 0 ✓"),
        ])
        + key_point("Zeroes are <b>x = 5</b> and <b>x = −2</b>. The graph crosses the x-axis at these two points.")
    ),
    "try_this": {
        "question": "Find the zeroes of p(x) = x² − 7x + 12.",
        "hint": "Find two numbers that multiply to 12 and add to −7.",
        "answer": "x² − 7x + 12 = (x − 3)(x − 4). Zeroes: x = 3, x = 4. Verify: p(3) = 9 − 21 + 12 = 0 ✓, p(4) = 16 − 28 + 12 = 0 ✓."
    },
    "fun_fact": "The word 'polynomial' comes from Greek: 'poly' (many) + 'nomos' (term). So it literally means 'many terms'!"
}

QUESTIONS["math10.polynomials10.types_and_zeroes"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.polynomials10.types_and_zeroes"],
     "question": "Find the zeroes of p(x) = x² − 2x − 8.",
     "hint": "Factor: find two numbers that multiply to −8 and add to −2.",
     "expected_answer": "x² − 2x − 8 = (x − 4)(x + 2). Zeroes: x = 4 and x = −2. Verify: p(4) = 16 − 8 − 8 = 0 ✓, p(−2) = 4 + 4 − 8 = 0 ✓."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.polynomials10.types_and_zeroes"],
     "question": "Find the zeroes of p(x) = 6x² − 7x − 3.",
     "hint": "Product = 6×(−3) = −18. Find two numbers with product −18 and sum −7.",
     "expected_answer": "6x² − 7x − 3: ac = −18, numbers: −9 and 2. Rewrite: 6x² − 9x + 2x − 3 = 3x(2x−3) + 1(2x−3) = (3x+1)(2x−3). Zeroes: x = −1/3 and x = 3/2."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.polynomials10.types_and_zeroes"],
     "question": "The graph of a quadratic polynomial touches the x-axis at x = 4 and opens upward. Write one such polynomial.",
     "hint": "If it only touches (doesn't cross), x = 4 is a repeated zero. So p(x) = a(x − 4)².",
     "expected_answer": "Since x = 4 is a repeated zero (touches, doesn't cross), p(x) = (x − 4)² = x² − 8x + 16. Opens upward since coefficient of x² is positive."},
    {"id": 4, "type": "word_problem", "difficulty": 0.6, "concepts_tested": ["math10.polynomials10.types_and_zeroes"],
     "question": "A quadratic polynomial has zeroes at x = −3 and x = 2. If p(1) = 8, find the polynomial.",
     "hint": "p(x) = a(x + 3)(x − 2). Use p(1) = 8 to find a.",
     "expected_answer": "p(x) = a(x + 3)(x − 2). p(1) = a(4)(−1) = −4a = 8 → a = −2. So p(x) = −2(x + 3)(x − 2) = −2(x² + x − 6) = −2x² − 2x + 12."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.polynomials10.types_and_zeroes"],
     "question": "A cubic polynomial has zeroes at −2, 1, and 3 and passes through (0, 12). Find the polynomial.",
     "hint": "p(x) = a(x + 2)(x − 1)(x − 3). Use p(0) = 12 to find a.",
     "expected_answer": "p(x) = a(x + 2)(x − 1)(x − 3). p(0) = a(2)(−1)(−3) = 6a = 12 → a = 2. So p(x) = 2(x + 2)(x − 1)(x − 3). Expanding: 2(x³ − 2x² − 5x + 6) = 2x³ − 4x² − 10x + 12."},
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2 · Relationship Between Zeroes and Coefficients
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.polynomials10.zeroes_relationship"] = {
    "title": "🔗 Zeroes and Coefficients — A Hidden Connection",
    "hook": "What if I told you that without finding the actual zeroes, you can know their sum and product just by looking at the coefficients? For x² − 5x + 6, the zeroes are 2 and 3 — and notice: 2 + 3 = 5 (the coefficient of x, but with a minus sign), and 2 × 3 = 6 (the constant term). Coincidence? Not at all!",
    "explanation": (
        "<p>For a quadratic polynomial <b>ax² + bx + c</b> with zeroes α and β:</p>"
        + formula_box("α + β = −b/a  (Sum of zeroes)", "Sum")
        + formula_box("αβ = c/a  (Product of zeroes)", "Product")
        + "<br><p>To <b>form a quadratic</b> when zeroes are given:</p>"
        + formula_box("p(x) = k[x² − (α + β)x + αβ]  for any non-zero constant k", "Formation")
        + comparison_table(
            ["Polynomial", "a, b, c", "Sum α+β = −b/a", "Product αβ = c/a", "Verify"],
            [["x² − 5x + 6", "1, −5, 6", "−(−5)/1 = 5", "6/1 = 6", "Zeroes 2,3: 2+3=5 ✓ 2×3=6 ✓"],
             ["2x² + 7x + 3", "2, 7, 3", "−7/2", "3/2", "Zeroes −3, −½: sum = −7/2 ✓ prod = 3/2 ✓"],
             ["3x² − 11x − 4", "3, −11, −4", "11/3", "−4/3", "Zeroes 4, −⅓: sum = 11/3 ✓ prod = −4/3 ✓"]]
        )
        + tip_box("For a <b>cubic</b> ax³ + bx² + cx + d with zeroes α, β, γ: α+β+γ = −b/a, αβ+βγ+γα = c/a, αβγ = −d/a.")
    ),
    "worked_example": (
        "<b>Example:</b> Find a quadratic polynomial whose zeroes are 3 + √2 and 3 − √2.<br><br>"
        + step_box([
            ("Find sum", "α + β = (3 + √2) + (3 − √2) = 6"),
            ("Find product", "αβ = (3 + √2)(3 − √2) = 9 − 2 = 7  [difference of squares!]"),
            ("Form polynomial", "p(x) = x² − (sum)x + (product) = x² − 6x + 7"),
        ])
        + key_point("Answer: <b>p(x) = x² − 6x + 7</b>. Any scalar multiple k(x² − 6x + 7) is also valid.")
    ),
    "try_this": {
        "question": "Find a quadratic polynomial whose sum of zeroes is 1/4 and product of zeroes is −1.",
        "hint": "p(x) = x² − (sum)x + (product). You may multiply through to clear fractions.",
        "answer": "p(x) = x² − (1/4)x + (−1) = x² − x/4 − 1. Multiply by 4: 4x² − x − 4."
    },
    "fun_fact": "These relationships are named after François Viète (1540–1603), a French mathematician. They're called 'Vieta's formulas' and work for polynomials of any degree!"
}

QUESTIONS["math10.polynomials10.zeroes_relationship"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.polynomials10.zeroes_relationship"],
     "question": "Find the sum and product of zeroes of p(x) = 3x² − 12x + 9 without actually finding the zeroes.",
     "hint": "Sum = −b/a, Product = c/a. Here a=3, b=−12, c=9.",
     "expected_answer": "Sum = −(−12)/3 = 4. Product = 9/3 = 3. (Actual zeroes: 1 and 3. Check: 1+3=4 ✓, 1×3=3 ✓.)"},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.polynomials10.zeroes_relationship"],
     "question": "Find a quadratic polynomial with zeroes 5 and −3.",
     "hint": "Sum = 5 + (−3), Product = 5 × (−3). Then p(x) = x² − (sum)x + (product).",
     "expected_answer": "Sum = 2, Product = −15. p(x) = x² − 2x − 15. Verify: (x−5)(x+3) = x² − 2x − 15 ✓."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.polynomials10.zeroes_relationship"],
     "question": "If one zero of 2x² − 8x + k is twice the other, find the value of k.",
     "hint": "Let zeroes be α and 2α. Use sum = −b/a and product = c/a.",
     "expected_answer": "Let zeroes be α and 2α. Sum: α + 2α = 3α = 8/2 = 4, so α = 4/3. Product: α × 2α = 2α² = k/2. So k = 4α² = 4 × 16/9 = 64/9."},
    {"id": 4, "type": "word_problem", "difficulty": 0.65, "concepts_tested": ["math10.polynomials10.zeroes_relationship"],
     "question": "If α and β are zeroes of x² − 6x + k and 3α + 2β = 20, find k.",
     "hint": "You know α + β = 6 and 3α + 2β = 20. Solve these two equations for α and β.",
     "expected_answer": "α + β = 6 … (1). 3α + 2β = 20 … (2). From (1): β = 6 − α. Substitute: 3α + 2(6−α) = 20 → 3α + 12 − 2α = 20 → α = 8. Then β = 6 − 8 = −2. k = αβ = 8 × (−2) = −16."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.polynomials10.zeroes_relationship"],
     "question": "If α, β are zeroes of p(x) = x² − 5x + 6, find the value of (1/α) + (1/β) and α² + β².",
     "hint": "1/α + 1/β = (α+β)/(αβ). For α²+β², use (α+β)² = α²+2αβ+β².",
     "expected_answer": "α + β = 5, αβ = 6. (1/α + 1/β) = (α+β)/(αβ) = 5/6. α² + β² = (α+β)² − 2αβ = 25 − 12 = 13."},
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 3 · Division Algorithm for Polynomials
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.polynomials10.division_algorithm"] = {
    "title": "➗ Division Algorithm — Polynomial Long Division",
    "hook": "You know how to divide numbers: 23 ÷ 5 = 4 remainder 3. Polynomials work the same way! When you divide x³ + 2x² − 5x + 1 by x − 2, you get a quotient and a remainder, just like numbers.",
    "explanation": (
        definition_box("Division Algorithm for Polynomials",
                       "If p(x) and g(x) are polynomials with g(x) ≠ 0, then there exist polynomials q(x) and r(x) such that: p(x) = g(x) × q(x) + r(x), where deg(r) < deg(g) or r(x) = 0.")
        + formula_box("p(x) = g(x) × q(x) + r(x),  deg(r) &lt; deg(g)", "Division Algorithm")
        + "<br><p><b>How to do Polynomial Long Division:</b></p>"
        + step_box([
            ("Divide leading terms", "Divide the first term of dividend by first term of divisor → first term of quotient"),
            ("Multiply", "Multiply entire divisor by this term"),
            ("Subtract", "Subtract from dividend to get new polynomial"),
            ("Repeat", "Bring down next term, repeat until degree of remainder < degree of divisor"),
        ], "#7B1FA2")
        + tip_box("This is useful when you know one or two zeroes and want to find the rest — divide out the known factors!")
    ),
    "worked_example": (
        "<b>Example:</b> Divide 3x³ + x² + 2x + 5 by x² + 2x + 1.<br><br>"
        + step_box([
            ("Divide leading terms", "3x³ ÷ x² = 3x. So first term of q(x) = 3x"),
            ("Multiply", "3x × (x² + 2x + 1) = 3x³ + 6x² + 3x"),
            ("Subtract", "(3x³ + x² + 2x + 5) − (3x³ + 6x² + 3x) = −5x² − x + 5"),
            ("Divide leading terms again", "−5x² ÷ x² = −5. So next term = −5"),
            ("Multiply", "−5 × (x² + 2x + 1) = −5x² − 10x − 5"),
            ("Subtract", "(−5x² − x + 5) − (−5x² − 10x − 5) = 9x + 10"),
        ])
        + key_point("<b>Quotient q(x) = 3x − 5, Remainder r(x) = 9x + 10</b>")
        + "<p>Verify: (x² + 2x + 1)(3x − 5) + (9x + 10) = 3x³ + x² + 2x + 5 ✓</p>"
    ),
    "try_this": {
        "question": "Divide 2x³ − 3x² + x + 1 by x − 1. What is the quotient and remainder?",
        "hint": "Divide leading terms: 2x³ ÷ x = 2x². Multiply, subtract, repeat.",
        "answer": "2x³ − 3x² + x + 1 ÷ (x − 1): q(x) = 2x² − x, r = 1. Verify: (x−1)(2x²−x) + 1 = 2x³ − x² − 2x² + x + 1 = 2x³ − 3x² + x + 1 ✓."
    },
    "fun_fact": "Polynomial division is the basis of synthetic division and the Remainder Theorem: the remainder when dividing p(x) by (x − a) is simply p(a)!"
}

QUESTIONS["math10.polynomials10.division_algorithm"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.polynomials10.division_algorithm"],
     "question": "Divide x² + 3x + 2 by x + 1. Find quotient and remainder.",
     "hint": "x² ÷ x = x. Multiply (x+1) by x, subtract, continue.",
     "expected_answer": "x² + 3x + 2 ÷ (x+1): First term: x. x(x+1) = x² + x. Subtract: 2x + 2. Next term: 2. 2(x+1) = 2x + 2. Subtract: 0. Quotient = x + 2, Remainder = 0. (It factors exactly!)"},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.polynomials10.division_algorithm"],
     "question": "Divide 3x³ − 5x² + 10 by x² − 3. Find q(x) and r(x), and verify p(x) = g(x)·q(x) + r(x).",
     "hint": "3x³ ÷ x² = 3x. Multiply (x²−3) by 3x, subtract. Then continue.",
     "expected_answer": "3x³ − 5x² + 10 ÷ (x²−3): Step 1: 3x. 3x(x²−3) = 3x³−9x. Subtract: −5x² + 9x + 10. Step 2: −5. −5(x²−3) = −5x² + 15. Subtract: 9x − 5. q(x) = 3x − 5, r(x) = 9x − 5. Verify: (x²−3)(3x−5) + 9x−5 = 3x³−5x²−9x+15+9x−5 = 3x³−5x²+10 ✓."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.polynomials10.division_algorithm"],
     "question": "One zero of x³ − 6x² + 11x − 6 is x = 1. Find all zeroes.",
     "hint": "Since x = 1 is a zero, (x − 1) is a factor. Divide to find the quadratic factor.",
     "expected_answer": "Divide x³ − 6x² + 11x − 6 by (x−1): q(x) = x² − 5x + 6. Factor: (x−2)(x−3). All zeroes: x = 1, 2, 3. Verify: (x−1)(x−2)(x−3) = x³ − 6x² + 11x − 6 ✓."},
    {"id": 4, "type": "word_problem", "difficulty": 0.65, "concepts_tested": ["math10.polynomials10.division_algorithm"],
     "question": "If x² − 3x + 2 is a factor of x⁴ − 5x³ + 9x² − 7x + 2, find the other factor.",
     "hint": "Divide x⁴ − 5x³ + 9x² − 7x + 2 by x² − 3x + 2.",
     "expected_answer": "Long division: x⁴ − 5x³ + 9x² − 7x + 2 ÷ (x² − 3x + 2). Step 1: x². x²(x²−3x+2) = x⁴−3x³+2x². Subtract: −2x³+7x²−7x+2. Step 2: −2x. −2x(x²−3x+2) = −2x³+6x²−4x. Subtract: x²−3x+2. Step 3: 1. 1(x²−3x+2) = x²−3x+2. Subtract: 0. Other factor: x² − 2x + 1 = (x−1)²."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.polynomials10.division_algorithm"],
     "question": "What value of k makes (x − 3) a factor of x³ − kx² + x + 6?",
     "hint": "If (x−3) is a factor, then x = 3 is a zero. So p(3) = 0.",
     "expected_answer": "p(3) = 0: 27 − 9k + 3 + 6 = 0 → 36 − 9k = 0 → k = 4. Verify: x³ − 4x² + x + 6 at x=3: 27 − 36 + 3 + 6 = 0 ✓. The polynomial is x³ − 4x² + x + 6 = (x−3)(x²−x−2) = (x−3)(x−2)(x+1)."},
]
