"""Chapter 3 — Pair of Linear Equations in Two Variables: 5 concepts, 25 questions."""
from .helpers import formula_box, step_box, tip_box, comparison_table, definition_box, key_point, info_box, warning_box, svg_coordinate_grid

LESSONS = {}
QUESTIONS = {}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1 · Graphical Method and Consistency
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.linear_eq_pair.graphical_method"] = {
    "title": "📊 Graphical Method — When Lines Meet (or Don't!)",
    "hook": "Imagine two friends walking on straight paths on a football field. Will they bump into each other? It depends on their paths! If the paths cross, there's one meeting point. If the paths are parallel, they'll never meet. And if they're on the same path — they'll always be together. This is exactly how pairs of linear equations work!",
    "explanation": (
        "<p>Each linear equation <b>a₁x + b₁y = c₁</b> represents a straight line. A <em>pair</em> of such equations gives two lines. Three possibilities:</p>"
        + comparison_table(
            ["Type", "Lines", "Condition", "Solutions", "Consistency"],
            [["Intersecting", "Cross at one point", "a₁/a₂ ≠ b₁/b₂", "Exactly 1", "Consistent"],
             ["Parallel", "Never meet", "a₁/a₂ = b₁/b₂ ≠ c₁/c₂", "0", "Inconsistent"],
             ["Coincident", "Same line", "a₁/a₂ = b₁/b₂ = c₁/c₂", "Infinite", "Dependent"]]
        )
        + "<br><b>Checking without graphing:</b> For a₁x + b₁y = c₁ and a₂x + b₂y = c₂, compare the ratios:"
        + formula_box("Compare a₁/a₂, b₁/b₂, and c₁/c₂", "Consistency Test")
        + svg_coordinate_grid(
            lines=[(-3, 4, 5, -2, "#E65100"), (-3, -1, 5, 3, "#1565C0")],
            points=[(2, 0.5, "Solution", "#2E7D32")],
            xrange=(-4, 6), yrange=(-3, 5), width=260, height=200
        )
        + '<div style="text-align:center;font-size:0.8rem;color:#666">Two intersecting lines → unique solution at the crossing point</div>'
    ),
    "worked_example": (
        "<b>Example:</b> Check the consistency of: 2x + 3y = 7 and 4x + 6y = 10.<br><br>"
        + step_box([
            ("Identify coefficients", "a₁=2, b₁=3, c₁=7 and a₂=4, b₂=6, c₂=10"),
            ("Compute ratios", "a₁/a₂ = 2/4 = 1/2, b₁/b₂ = 3/6 = 1/2, c₁/c₂ = 7/10"),
            ("Compare", "a₁/a₂ = b₁/b₂ = 1/2, but c₁/c₂ = 7/10 ≠ 1/2"),
            ("Conclude", "Since a₁/a₂ = b₁/b₂ ≠ c₁/c₂ → Parallel lines → No solution (Inconsistent)"),
        ])
    ),
    "try_this": {
        "question": "Check the consistency of: x + 2y = 4 and 3x + 6y = 12. How many solutions?",
        "hint": "Compare a₁/a₂, b₁/b₂, c₁/c₂.",
        "answer": "a₁/a₂ = 1/3, b₁/b₂ = 2/6 = 1/3, c₁/c₂ = 4/12 = 1/3. All ratios equal → coincident lines → infinitely many solutions."
    },
    "fun_fact": "In 3D, instead of two lines, you'd have two planes — they can intersect in a line, be parallel, or be the same plane!"
}

QUESTIONS["math10.linear_eq_pair.graphical_method"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.linear_eq_pair.graphical_method"],
     "question": "Check whether the pair x − y = 2 and 3x − 3y = 6 is consistent or inconsistent.",
     "hint": "Compare a₁/a₂, b₁/b₂, c₁/c₂ for equations x − y − 2 = 0 and 3x − 3y − 6 = 0.",
     "expected_answer": "a₁/a₂ = 1/3, b₁/b₂ = (−1)/(−3) = 1/3, c₁/c₂ = (−2)/(−6) = 1/3. All equal → Coincident → Infinitely many solutions (Dependent & Consistent)."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.linear_eq_pair.graphical_method"],
     "question": "For what value of k will 2x + ky = 6 and 6x + 9y = 18 have infinitely many solutions?",
     "hint": "For coincident lines: a₁/a₂ = b₁/b₂ = c₁/c₂. So 2/6 = k/9 = 6/18.",
     "expected_answer": "2/6 = 1/3, c₁/c₂ = 6/18 = 1/3. For b₁/b₂ = 1/3: k/9 = 1/3 → k = 3."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.linear_eq_pair.graphical_method"],
     "question": "For what value of p does px + 3y = p − 3 and 12x + py = p have no solution?",
     "hint": "No solution → parallel → a₁/a₂ = b₁/b₂ ≠ c₁/c₂. So p/12 = 3/p.",
     "expected_answer": "p/12 = 3/p → p² = 36 → p = ±6. Check c₁/c₂: For p=6: (6−3)/6 = 1/2 and a₁/a₂ = 6/12 = 1/2 → all equal → coincident, not parallel. For p=−6: (−6−3)/(−6) = 9/6 = 3/2 and a₁/a₂ = −6/12 = −1/2. Since −1/2 ≠ 3/2 → parallel → no solution. So p = −6."},
    {"id": 4, "type": "word_problem", "difficulty": 0.6, "concepts_tested": ["math10.linear_eq_pair.graphical_method"],
     "question": "Solve graphically: x + y = 5 and x − y = 1. Plot at least 3 points for each line and find where they intersect.",
     "hint": "For x + y = 5: try x = 0,2,5. For x − y = 1: try x = 0,1,3.",
     "expected_answer": "x + y = 5: points (0,5), (2,3), (5,0). x − y = 1: points (0,−1), (1,0), (3,2). The lines intersect at (3, 2). Verify: 3+2=5 ✓, 3−2=1 ✓."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.75, "concepts_tested": ["math10.linear_eq_pair.graphical_method"],
     "question": "Two lines ax + by = c and bx + ay = c (where a ≠ b) always intersect. Find the coordinates of their intersection point in terms of a, b, c.",
     "hint": "Add and subtract the two equations to simplify.",
     "expected_answer": "Add: (a+b)x + (a+b)y = 2c → x + y = 2c/(a+b). Subtract: (a−b)x − (a−b)y = 0 → x = y. From x = y and x + y = 2c/(a+b): 2x = 2c/(a+b) → x = c/(a+b). So the intersection is (c/(a+b), c/(a+b))."},
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2 · Substitution Method
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.linear_eq_pair.substitution"] = {
    "title": "🔄 Substitution Method — Replace and Solve",
    "hook": "Imagine you know that a banana costs twice as much as an apple. If someone tells you a banana and apple together cost ₹30, you can replace 'banana' with '2 × apple' and solve! That's the substitution method.",
    "explanation": (
        "<p>The <b>substitution method</b> solves a pair of equations in three steps:</p>"
        + step_box([
            ("Express one variable", "From one equation, write y in terms of x (or x in terms of y)"),
            ("Substitute", "Replace that variable in the OTHER equation → single-variable equation"),
            ("Back-substitute", "Solve for one variable, then plug back to find the other"),
        ], "#E65100")
        + tip_box("Choose the variable that's easiest to isolate — look for coefficient ±1!")
        + warning_box("Common mistake: substituting back into the SAME equation instead of the other one. This gives a tautology like 0 = 0, not a useful answer.")
    ),
    "worked_example": (
        "<b>Example:</b> Solve: x + 2y = 8 … (1),  3x + y = 9 … (2)<br><br>"
        + step_box([
            ("From (1): x = 8 − 2y", "Equation (1) has coefficient 1 for x, easy to isolate"),
            ("Substitute in (2)", "3(8 − 2y) + y = 9 → 24 − 6y + y = 9 → −5y = −15 → y = 3"),
            ("Back-substitute in (1)", "x = 8 − 2(3) = 8 − 6 = 2"),
            ("Verify in both equations", "(1): 2 + 6 = 8 ✓. (2): 6 + 3 = 9 ✓"),
        ])
        + formula_box("Solution: x = 2, y = 3")
    ),
    "try_this": {
        "question": "Solve: 2x + y = 7 and x − y = 2 using substitution.",
        "hint": "From the second equation: x = y + 2. Substitute into the first.",
        "answer": "x = y + 2. Substitute: 2(y+2) + y = 7 → 2y + 4 + y = 7 → 3y = 3 → y = 1. Then x = 1 + 2 = 3. Solution: x = 3, y = 1."
    },
    "fun_fact": "The substitution method is the basis of 'variable elimination' in computer algebra systems — programs like Wolfram Alpha use a sophisticated version of this same idea!"
}

QUESTIONS["math10.linear_eq_pair.substitution"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.linear_eq_pair.substitution"],
     "question": "Solve by substitution: y = 2x − 1 and 3x + y = 9.",
     "hint": "y is already expressed! Substitute 2x − 1 for y in the second equation.",
     "expected_answer": "3x + (2x − 1) = 9 → 5x = 10 → x = 2. y = 2(2) − 1 = 3. Solution: (2, 3)."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.linear_eq_pair.substitution"],
     "question": "Solve by substitution: x + 3y = 14 and 4x − y = 5.",
     "hint": "From first equation: x = 14 − 3y. Substitute into second.",
     "expected_answer": "x = 14 − 3y. 4(14−3y) − y = 5 → 56 − 12y − y = 5 → −13y = −51 → y = 51/13. Hmm, let me recalculate: −13y = 5−56 = −51 → y = 51/13. Simplify: that doesn't simplify nicely. Actually, let me retry: 56 − 13y = 5 → 13y = 51 → y = 51/13. Let me use integers: try from eq 2: y = 4x−5. Sub in eq 1: x + 3(4x−5) = 14 → x + 12x − 15 = 14 → 13x = 29 → x = 29/13. Solution: x = 29/13, y = 51/13. Verify: 29/13 + 3(51/13) = 29/13 + 153/13 = 182/13 = 14 ✓."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.linear_eq_pair.substitution"],
     "question": "Solve: 2x + 3y = 11 and 2x − 4y = −24 using substitution.",
     "hint": "From equation 1: 2x = 11 − 3y, so x = (11−3y)/2. Or subtract equations first.",
     "expected_answer": "From eq 1: 2x = 11 − 3y. Substitute in eq 2: (11 − 3y) − 4y = −24 → 11 − 7y = −24 → 7y = 35 → y = 5. Then 2x = 11 − 15 = −4 → x = −2. Solution: (−2, 5). Verify: 2(−2)+3(5) = −4+15 = 11 ✓, 2(−2)−4(5) = −4−20 = −24 ✓."},
    {"id": 4, "type": "word_problem", "difficulty": 0.6, "concepts_tested": ["math10.linear_eq_pair.substitution"],
     "question": "The sum of two numbers is 74. The larger exceeds the smaller by 12. Find the numbers using substitution.",
     "hint": "Let the numbers be x (larger) and y (smaller). x + y = 74 and x − y = 12.",
     "expected_answer": "x + y = 74 … (1), x − y = 12 … (2). From (2): x = y + 12. Substitute in (1): (y + 12) + y = 74 → 2y = 62 → y = 31. Then x = 43. The numbers are 43 and 31."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.linear_eq_pair.substitution"],
     "question": "Solve: x/2 + 2y/3 = −1 and x − y/3 = 3.",
     "hint": "Clear fractions first. Multiply first eq by 6 and second by 3.",
     "expected_answer": "Multiply eq 1 by 6: 3x + 4y = −6. Multiply eq 2 by 3: 3x − y = 9. From eq 2 modified: y = 3x − 9. Sub in eq 1 modified: 3x + 4(3x−9) = −6 → 3x + 12x − 36 = −6 → 15x = 30 → x = 2. y = 6 − 9 = −3. Solution: (2, −3)."},
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 3 · Elimination Method
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.linear_eq_pair.elimination"] = {
    "title": "✂️ Elimination Method — Make a Variable Disappear!",
    "hook": "What if, instead of substituting, you could magically make one variable vanish from the equations? That's the elimination method — multiply the equations by the right numbers, then add or subtract to 'eliminate' one variable!",
    "explanation": (
        "<p>The <b>elimination method</b> works by making coefficients of one variable equal, then adding or subtracting:</p>"
        + step_box([
            ("Choose a variable to eliminate", "Pick the one whose coefficients are easier to equalize"),
            ("Multiply equations", "Make coefficients of the chosen variable equal (or opposite)"),
            ("Add or subtract", "Same signs → subtract. Opposite signs → add."),
            ("Solve and back-substitute", "Get one variable, plug into either equation for the other"),
        ], "#2E7D32")
        + tip_box("If coefficients are already equal, just subtract right away! e.g., 2x + 3y = 7 and 2x − y = 3 → subtract to get 4y = 4.")
    ),
    "worked_example": (
        "<b>Example:</b> Solve: 3x + 4y = 25 … (1),  2x − 3y = 6 … (2)<br><br>"
        + step_box([
            ("Eliminate x", "Multiply (1) by 2 and (2) by 3 to make x-coefficients equal"),
            ("Eq (1) × 2:", "6x + 8y = 50"),
            ("Eq (2) × 3:", "6x − 9y = 18"),
            ("Subtract", "(6x + 8y) − (6x − 9y) = 50 − 18 → 17y = 32 → y = 32/17"),
        ])
        + info_box("Hmm, fractions. Let me try eliminating y instead.")
        + step_box([
            ("Eliminate y", "Multiply (1) by 3 and (2) by 4 to make y-coefficients 12 and −12"),
            ("Eq (1) × 3:", "9x + 12y = 75"),
            ("Eq (2) × 4:", "8x − 12y = 24"),
            ("Add (signs are opposite!)", "17x = 99 → x = 99/17"),
        ])
        + key_point("So x = 99/17 and y = 32/17. Sometimes answers are fractions — that's perfectly fine!")
        + "<p>Let's try a cleaner example: <b>3x + 2y = 11, 5x − 2y = 13</b>. Since y-coefficients are +2 and −2, just add: 8x = 24 → x = 3, then y = (11−9)/2 = 1.</p>"
    ),
    "try_this": {
        "question": "Solve: 5x − 3y = 1 and 3x + 2y = 7 using elimination.",
        "hint": "To eliminate y: multiply first eq by 2 and second by 3, then add.",
        "answer": "5x−3y=1 ×2 → 10x−6y=2. 3x+2y=7 ×3 → 9x+6y=21. Add: 19x = 23 → x = 23/19. Hmm. Alternative: eliminate x: multiply first by 3, second by 5: 15x−9y=3 and 15x+10y=35. Subtract: −19y = −32 → y = 32/19, x = 23/19."
    },
    "fun_fact": "The elimination method is the precursor to Gaussian Elimination — a technique used to solve systems with hundreds of variables in engineering and physics!"
}

QUESTIONS["math10.linear_eq_pair.elimination"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.linear_eq_pair.elimination"],
     "question": "Solve by elimination: x + y = 10 and x − y = 4.",
     "hint": "Just add the two equations directly — y will cancel!",
     "expected_answer": "Add: 2x = 14 → x = 7. Subtract: 2y = 6 → y = 3. Solution: (7, 3). Verify: 7+3=10 ✓, 7−3=4 ✓."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.linear_eq_pair.elimination"],
     "question": "Solve by elimination: 3x + 2y = 12 and x + 2y = 8.",
     "hint": "y-coefficients are already equal. Subtract the equations.",
     "expected_answer": "Subtract: (3x+2y) − (x+2y) = 12−8 → 2x = 4 → x = 2. From eq 2: 2+2y = 8 → y = 3. Solution: (2, 3)."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.linear_eq_pair.elimination"],
     "question": "Solve: 2x + 5y = 31 and 7x + 3y = 36.",
     "hint": "Multiply first by 7 and second by 2 to eliminate x, or first by 3 and second by 5 to eliminate y.",
     "expected_answer": "Eq1×3: 6x+15y=93. Eq2×5: 35x+15y=180. Subtract: 29x=87 → x=3. Then 6+5y=31 → y=5. Solution: (3, 5). Verify: 2(3)+5(5)=31 ✓, 7(3)+3(5)=36 ✓."},
    {"id": 4, "type": "word_problem", "difficulty": 0.6, "concepts_tested": ["math10.linear_eq_pair.elimination"],
     "question": "The sum of two numbers is 50. If the larger is 4 more than twice the smaller, find both numbers using elimination.",
     "hint": "Let numbers be x (larger) and y (smaller). x + y = 50 and x = 2y + 4 → x − 2y = 4.",
     "expected_answer": "x + y = 50 … (1). x − 2y = 4 … (2). Subtract (2) from (1): 3y = 46 → y = 46/3. Hmm that's not an integer. Let me re-read: x + y = 50 and x − 2y = 4. Subtract: 3y = 46 → y = 46/3 ≈ 15.33. If we want integers: from (1)−(2): 3y=46, so y = 46/3 and x = 50−46/3 = 104/3. Actually this is correct. The numbers are 104/3 and 46/3."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.linear_eq_pair.elimination"],
     "question": "Solve: 4/x + 3/y = 14 and 3/x − 4/y = 23. (Hint: let u = 1/x, v = 1/y.)",
     "hint": "Substitute u = 1/x, v = 1/y. Then you get 4u + 3v = 14 and 3u − 4v = 23.",
     "expected_answer": "Let u=1/x, v=1/y. 4u+3v=14 …(1), 3u−4v=23 …(2). (1)×4: 16u+12v=56. (2)×3: 9u−12v=69. Add: 25u=125 → u=5 → x=1/5. From (1): 20+3v=14 → v=−2 → y=−1/2. Solution: x=1/5, y=−1/2."},
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 4 · Cross-Multiplication Method
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.linear_eq_pair.cross_multiplication"] = {
    "title": "✖️ Cross-Multiplication — The Formula Method",
    "hook": "What if there was a single formula that could solve any pair of linear equations instantly? The cross-multiplication method gives you exactly that — plug in the coefficients and out come x and y!",
    "explanation": (
        "<p>For the system <b>a₁x + b₁y + c₁ = 0</b> and <b>a₂x + b₂y + c₂ = 0</b>:</p>"
        + formula_box("x/(b₁c₂ − b₂c₁) = y/(c₁a₂ − c₂a₁) = 1/(a₁b₂ − a₂b₁)", "Cross-Multiplication Formula")
        + "<p><b>Memory Trick — the arrow diagram:</b></p>"
        + comparison_table(
            ["", "x", "y", "1"],
            [["Numerator", "b₁c₂ − b₂c₁", "c₁a₂ − c₂a₁", "a₁b₂ − a₂b₁"]]
        )
        + tip_box("Write coefficients in order: b, c, a, b. Cross-multiply downward-right minus downward-left for each column.")
        + warning_box("Equations MUST be in the form ax + by + c = 0 (everything on one side). Move constants to the left!")
        + key_point("This works when a₁b₂ − a₂b₁ ≠ 0 (the lines are not parallel).")
    ),
    "worked_example": (
        "<b>Example:</b> Solve 2x + 3y − 8 = 0 and 4x + 5y − 14 = 0.<br><br>"
        + step_box([
            ("List coefficients", "a₁=2, b₁=3, c₁=−8; a₂=4, b₂=5, c₂=−14"),
            ("Compute numerators", "For x: b₁c₂ − b₂c₁ = 3(−14) − 5(−8) = −42 + 40 = −2"),
            ("", "For y: c₁a₂ − c₂a₁ = (−8)(4) − (−14)(2) = −32 + 28 = −4"),
            ("Compute denominator", "a₁b₂ − a₂b₁ = 2(5) − 4(3) = 10 − 12 = −2"),
            ("Calculate", "x = −2/(−2) = 1, y = −4/(−2) = 2"),
        ])
        + formula_box("Solution: x = 1, y = 2")
        + "<p>Verify: 2(1) + 3(2) = 8 ✓, 4(1) + 5(2) = 14 ✓</p>"
    ),
    "try_this": {
        "question": "Solve using cross-multiplication: x + 2y − 1 = 0 and 2x − 3y − 12 = 0.",
        "hint": "a₁=1, b₁=2, c₁=−1; a₂=2, b₂=−3, c₂=−12. Apply the formula.",
        "answer": "x-numerator: 2(−12) − (−3)(−1) = −24 − 3 = −27. y-numerator: (−1)(2) − (−12)(1) = −2 + 12 = 10. Denominator: 1(−3) − 2(2) = −3 − 4 = −7. x = −27/(−7) = 27/7, y = 10/(−7) = −10/7."
    },
    "fun_fact": "Cross-multiplication is actually Cramer's Rule in disguise — named after Gabriel Cramer (1704-1752), though the method was known in China centuries earlier!"
}

QUESTIONS["math10.linear_eq_pair.cross_multiplication"] = [
    {"id": 1, "type": "direct", "difficulty": 0.35, "concepts_tested": ["math10.linear_eq_pair.cross_multiplication"],
     "question": "Solve by cross-multiplication: x − 3y − 7 = 0 and 3x − 3y − 15 = 0.",
     "hint": "a₁=1, b₁=−3, c₁=−7; a₂=3, b₂=−3, c₂=−15.",
     "expected_answer": "x: (−3)(−15)−(−3)(−7) = 45−21 = 24. y: (−7)(3)−(−15)(1) = −21+15 = −6. denom: 1(−3)−3(−3) = −3+9 = 6. x = 24/6 = 4, y = −6/6 = −1. Verify: 4−(−3)−7 = 0 ✓."},
    {"id": 2, "type": "direct", "difficulty": 0.45, "concepts_tested": ["math10.linear_eq_pair.cross_multiplication"],
     "question": "Solve: 2x + y = 5 and 3x − 2y = 4 using cross-multiplication.",
     "hint": "Rewrite as 2x + y − 5 = 0 and 3x − 2y − 4 = 0.",
     "expected_answer": "a₁=2, b₁=1, c₁=−5; a₂=3, b₂=−2, c₂=−4. x: (1)(−4)−(−2)(−5) = −4−10 = −14. y: (−5)(3)−(−4)(2) = −15+8 = −7. denom: 2(−2)−3(1) = −4−3 = −7. x = −14/(−7) = 2, y = −7/(−7) = 1. Solution: (2, 1)."},
    {"id": 3, "type": "word_problem", "difficulty": 0.55, "concepts_tested": ["math10.linear_eq_pair.cross_multiplication"],
     "question": "For what value of k does the system kx + 3y − (k+3) = 0 and 12x + ky − k = 0 have a unique solution?",
     "hint": "Unique solution exists when a₁b₂ − a₂b₁ ≠ 0, i.e., k(k) − 12(3) ≠ 0.",
     "expected_answer": "a₁b₂ − a₂b₁ ≠ 0: k·k − 12·3 ≠ 0 → k² − 36 ≠ 0 → k ≠ ±6. For all values of k except 6 and −6, the system has a unique solution."},
    {"id": 4, "type": "word_problem", "difficulty": 0.65, "concepts_tested": ["math10.linear_eq_pair.cross_multiplication"],
     "question": "Solve: 5/(x−1) + 1/(y−2) = 2 and 6/(x−1) − 3/(y−2) = 1.",
     "hint": "Let u = 1/(x−1) and v = 1/(y−2). Solve 5u + v = 2 and 6u − 3v = 1.",
     "expected_answer": "Let u = 1/(x−1), v = 1/(y−2). 5u + v = 2 and 6u − 3v = 1. Cross-multiply or eliminate: 15u + 3v = 6 and 6u − 3v = 1. Add: 21u = 7 → u = 1/3. v = 2 − 5/3 = 1/3. So 1/(x−1) = 1/3 → x = 4. 1/(y−2) = 1/3 → y = 5. Solution: (4, 5)."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.linear_eq_pair.cross_multiplication"],
     "question": "The system ax + by = a − b and bx − ay = a + b has a specific solution regardless of a, b (provided a² + b² ≠ 0). Find it.",
     "hint": "Rewrite as ax + by − (a−b) = 0 and bx − ay − (a+b) = 0. Try x = 1, y = −1 directly.",
     "expected_answer": "Test x = 1, y = −1: Eq1: a(1) + b(−1) = a − b ✓. Eq2: b(1) − a(−1) = b + a = a + b ✓. So x = 1, y = −1 works for ALL values of a, b (as long as a² + b² ≠ 0 so the system is non-trivial)."},
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 5 · Word Problems on Linear Equations
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.linear_eq_pair.word_problems10"] = {
    "title": "📝 Word Problems — From Real Life to Equations",
    "hook": "A father is 30 years older than his son. In 5 years, his age will be three times his son's age. How old are they now? Problems like these appear everywhere — from planning finances to mixing chemicals. The trick is translating words into equations!",
    "explanation": (
        "<p><b>Strategy for word problems:</b></p>"
        + step_box([
            ("Read and identify unknowns", "Assign variables: let x = ..., y = ..."),
            ("Translate conditions into equations", "Each condition gives one equation"),
            ("Solve the system", "Use substitution, elimination, or cross-multiplication"),
            ("Verify and interpret", "Check answer makes sense; reject negative ages, etc."),
        ], "#7B1FA2")
        + "<br><b>Common Types:</b>"
        + comparison_table(
            ["Problem Type", "Example Setup", "Key Relationship"],
            [["Age problems", "Father-son ages", "Present + years = future"],
             ["Speed-distance", "Boat in river", "Downstream speed = boat + current"],
             ["Number problems", "Two-digit number", "Number = 10(tens) + units"],
             ["Fraction problems", "Numerator/Denominator", "If 2 added to num, fraction = ..."],
             ["Cost/quantity", "Pens and pencils", "Total cost = unit price × quantity"]]
        )
        + tip_box("Always double-check by substituting back into the original WORDS, not just the equations!")
    ),
    "worked_example": (
        "<b>Example:</b> A fraction becomes 4/5 if 1 is added to both numerator and denominator. If 5 is subtracted from both, it becomes 1/2. Find the fraction.<br><br>"
        + step_box([
            ("Let numerator = x, denominator = y", "The fraction is x/y"),
            ("Condition 1: (x+1)/(y+1) = 4/5", "Cross-multiply: 5(x+1) = 4(y+1) → 5x − 4y = −1 … (1)"),
            ("Condition 2: (x−5)/(y−5) = 1/2", "Cross-multiply: 2(x−5) = 1(y−5) → 2x − y = 5 … (2)"),
            ("Solve: from (2), y = 2x − 5", "Sub in (1): 5x − 4(2x−5) = −1 → 5x − 8x + 20 = −1 → −3x = −21 → x = 7"),
            ("Find y", "y = 2(7) − 5 = 9"),
        ])
        + formula_box("The fraction is 7/9")
        + "<p>Verify: (7+1)/(9+1) = 8/10 = 4/5 ✓. (7−5)/(9−5) = 2/4 = 1/2 ✓.</p>"
    ),
    "try_this": {
        "question": "The sum of a two-digit number and the number obtained by reversing its digits is 121. If the digits differ by 3, find the number (assume tens digit > units digit).",
        "hint": "Let tens digit = x, units digit = y. Number = 10x + y. Reversed = 10y + x. Sum = 121. Difference = 3.",
        "answer": "10x+y + 10y+x = 121 → 11(x+y) = 121 → x+y = 11. And x−y = 3. Adding: 2x = 14 → x = 7, y = 4. Number = 74. Check: 74 + 47 = 121 ✓, 7−4 = 3 ✓."
    },
    "fun_fact": "The earliest word problems in recorded history come from ancient Egyptian papyri and Babylonian clay tablets from about 1800 BC. The famous 'aha' problems of the Rhind Papyrus are essentially linear equations!"
}

QUESTIONS["math10.linear_eq_pair.word_problems10"] = [
    {"id": 1, "type": "word_problem", "difficulty": 0.35, "concepts_tested": ["math10.linear_eq_pair.word_problems10"],
     "question": "5 pencils and 3 pens together cost ₹34, while 3 pencils and 5 pens cost ₹46. Find the cost of each.",
     "hint": "Let pencil = ₹x, pen = ₹y. 5x + 3y = 34 and 3x + 5y = 46.",
     "expected_answer": "5x+3y=34 …(1), 3x+5y=46 …(2). (1)×5: 25x+15y=170. (2)×3: 9x+15y=138. Subtract: 16x=32 → x=2. From (1): 10+3y=34 → y=8. Pencil=₹2, Pen=₹8."},
    {"id": 2, "type": "word_problem", "difficulty": 0.45, "concepts_tested": ["math10.linear_eq_pair.word_problems10"],
     "question": "A father is 24 years older than his daughter. In 6 years, the father's age will be twice his daughter's age. Find their present ages.",
     "hint": "Let daughter's age = x, father's = x + 24. In 6 years: (x+24+6) = 2(x+6).",
     "expected_answer": "Father = x + 24. After 6 years: x+30 = 2(x+6) → x+30 = 2x+12 → x = 18. Daughter = 18 years, Father = 42 years. Check in 6 years: 48 = 2×24 ✓."},
    {"id": 3, "type": "word_problem", "difficulty": 0.55, "concepts_tested": ["math10.linear_eq_pair.word_problems10"],
     "question": "A boat goes 30 km upstream and 44 km downstream in 10 hours. It goes 40 km upstream and 55 km downstream in 13 hours. Find the speed of the boat in still water and the speed of the current.",
     "hint": "Let boat speed = x, current = y. Upstream speed = x−y, downstream = x+y. Let u=1/(x−y), v=1/(x+y).",
     "expected_answer": "Let u=1/(x−y), v=1/(x+y). 30u+44v=10 …(1). 40u+55v=13 …(2). (1)×4: 120u+176v=40. (2)×3: 120u+165v=39. Subtract: 11v=1 → v=1/11 → x+y=11. From (1): 30u+4=10 → u=1/5 → x−y=5. So x=8, y=3. Boat=8 km/h, Current=3 km/h."},
    {"id": 4, "type": "word_problem", "difficulty": 0.65, "concepts_tested": ["math10.linear_eq_pair.word_problems10"],
     "question": "A two-digit number is 4 more than 6 times the sum of its digits. If 18 is subtracted from the number, the digits are reversed. Find the number.",
     "hint": "Let tens=x, units=y. Number=10x+y. Conditions: 10x+y = 6(x+y)+4 and 10x+y−18 = 10y+x.",
     "expected_answer": "10x+y = 6x+6y+4 → 4x−5y=4 …(1). 10x+y−18 = 10y+x → 9x−9y=18 → x−y=2 …(2). From (2): x=y+2. Sub: 4(y+2)−5y=4 → 4y+8−5y=4 → y=4. x=6. Number=64. Check: 6(6+4)+4=64 ✓, 64−18=46 ✓."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.linear_eq_pair.word_problems10"],
     "question": "Places A and B are 100 km apart. One car starts from A and another from B at the same time. If they travel in the same direction, they meet in 5 hours. If they travel towards each other, they meet in 1 hour. Find their speeds.",
     "hint": "Same direction: (faster − slower)×5 = 100. Opposite: (sum)×1 = 100.",
     "expected_answer": "Let speeds be x (from A) and y (from B), x > y. Same direction: 5(x−y) = 100 → x−y = 20. Opposite: 1(x+y) = 100. Adding: 2x = 120 → x = 60. y = 40. Speeds: 60 km/h and 40 km/h."},
]
