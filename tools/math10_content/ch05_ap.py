"""Chapter 5 — Arithmetic Progressions: 4 concepts, 20 questions."""
from .helpers import formula_box, step_box, tip_box, comparison_table, definition_box, key_point, info_box, warning_box

LESSONS = {}
QUESTIONS = {}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1 · AP and Common Difference
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.ap.intro"] = {
    "title": "📊 Arithmetic Progressions — Patterns in Numbers",
    "hook": "You're saving money: ₹100 in week 1, ₹150 in week 2, ₹200 in week 3... Each week you save ₹50 more. This is an Arithmetic Progression — a sequence where you add the same number each time!",
    "explanation": (
        definition_box("Arithmetic Progression (AP)", "A sequence a₁, a₂, a₃, ... where each term differs from the previous by a constant <b>d</b> (common difference).")
        + formula_box("d = a₂ − a₁ = a₃ − a₂ = ... = aₙ − aₙ₋₁", "Common Difference")
        + comparison_table(
            ["Sequence", "a (first term)", "d", "Is it AP?"],
            [["2, 5, 8, 11, ...", "2", "+3", "Yes ✓"],
             ["10, 7, 4, 1, −2, ...", "10", "−3", "Yes ✓ (d can be negative!)"],
             ["5, 5, 5, 5, ...", "5", "0", "Yes ✓ (d can be zero!)"],
             ["1, 4, 9, 16, ...", "1", "varies", "No ✗ (differences: 3,5,7 — not constant)"]]
        )
        + key_point("An AP is fully described by just two things: the <b>first term a</b> and the <b>common difference d</b>.")
        + tip_box("To check if a sequence is an AP: compute all consecutive differences. If they're all the same → it's an AP!")
    ),
    "worked_example": (
        "<b>Example:</b> Is −3, −1, 1, 3, 5 an AP? If so, find the common difference.<br><br>"
        + step_box([
            ("Find differences", "−1 − (−3) = 2, 1 − (−1) = 2, 3 − 1 = 2, 5 − 3 = 2"),
            ("All differences equal?", "Yes, all are 2"),
            ("Conclusion", "It's an AP with a = −3 and d = 2"),
        ])
    ),
    "try_this": {
        "question": "Check if 1, 3, 6, 10, 15 is an AP.",
        "hint": "Find differences: 3−1, 6−3, 10−6, 15−10.",
        "answer": "Differences: 2, 3, 4, 5. Not constant! This is NOT an AP. (It's actually the sequence of triangular numbers.)"
    },
    "fun_fact": "The concept of AP was known to ancient Babylonians around 1700 BC! They used it to predict astronomical events like eclipses."
}

QUESTIONS["math10.ap.intro"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.ap.intro"],
     "question": "Which of the following are APs? For those that are, find d. (a) 2, 4, 8, 16  (b) −10, −6, −2, 2  (c) 1, 1, 1, 1",
     "hint": "Check if consecutive differences are constant.",
     "expected_answer": "(a) Differences: 2, 4, 8 — not constant → Not AP. (b) Differences: 4, 4, 4 → AP, d = 4. (c) Differences: 0, 0, 0 → AP, d = 0."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.ap.intro"],
     "question": "Write the first 5 terms of the AP with a = 7 and d = −3.",
     "hint": "Start with 7, subtract 3 each time.",
     "expected_answer": "7, 4, 1, −2, −5."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.ap.intro"],
     "question": "The first term of an AP is 5 and the common difference is −2. Which term is the first negative term?",
     "hint": "aₙ = 5 + (n−1)(−2) = 7 − 2n. Find smallest n where aₙ < 0.",
     "expected_answer": "aₙ = 7 − 2n < 0 → n > 3.5. So n = 4 is the first negative term. a₄ = 7 − 8 = −1. Verify: 5, 3, 1, −1 ✓."},
    {"id": 4, "type": "word_problem", "difficulty": 0.6, "concepts_tested": ["math10.ap.intro"],
     "question": "If a, a+d, a+2d are the angles of a triangle, find the value of d and the angles (given that angles sum to 180°).",
     "hint": "Sum of angles = 180°. So a + (a+d) + (a+2d) = 180.",
     "expected_answer": "3a + 3d = 180 → a + d = 60. The middle term = 60°. Since we need a > 0 and a + 2d > 0, and the angles must be positive: any d where a = 60−d > 0 (d < 60) and 60+d > 0 (d > −60). E.g., d = 20 → angles 40°, 60°, 80°. The middle angle is always 60°."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.75, "concepts_tested": ["math10.ap.intro"],
     "question": "If 2x, x+10, 3x+2 are in AP, find x.",
     "hint": "In AP, middle term = average of first and third: (x+10) = (2x + 3x+2)/2.",
     "expected_answer": "For AP: 2(x+10) = 2x + (3x+2). 2x + 20 = 5x + 2. 18 = 3x. x = 6. Check: 12, 16, 20 → differences 4, 4 ✓."},
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2 · The nth Term
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.ap.nth_term"] = {
    "title": "🎯 The nth Term — Jump Straight to Any Position",
    "hook": "Your AP is 3, 7, 11, 15, ... What's the 100th term? You don't need to write out all 100 terms — there's a formula that takes you directly to any term!",
    "explanation": (
        "<p>The <b>nth term</b> of an AP with first term <b>a</b> and common difference <b>d</b>:</p>"
        + formula_box("aₙ = a + (n − 1)d", "nth Term Formula")
        + "<p>Think of it: start at a, then take (n−1) steps of size d.</p>"
        + comparison_table(
            ["n", "Formula", "Value for AP: 3, 7, 11, ..."],
            [["1", "3 + 0(4) = 3", "3"],
             ["2", "3 + 1(4) = 7", "7"],
             ["5", "3 + 4(4) = 19", "19"],
             ["100", "3 + 99(4) = 399", "399"]]
        )
        + tip_box("You can also use this backwards: if you know a term's value, solve for n to find its position!")
        + key_point("The nth term formula is <b>linear in n</b>: aₙ = dn + (a−d). If you plot term vs position, you get a straight line!")
    ),
    "worked_example": (
        "<b>Example:</b> Find the 20th term of the AP: 2, 7, 12, 17, ...<br><br>"
        + step_box([
            ("Identify a and d", "a = 2, d = 7 − 2 = 5"),
            ("Apply formula", "a₂₀ = 2 + (20 − 1) × 5 = 2 + 95 = 97"),
        ])
        + "<br><b>Example 2:</b> Which term of the AP 5, 13, 21, ... is 181?<br><br>"
        + step_box([
            ("Set up", "181 = 5 + (n−1) × 8"),
            ("Solve", "176 = 8(n−1) → n−1 = 22 → n = 23"),
        ])
        + key_point("181 is the <b>23rd term</b> of this AP.")
    ),
    "try_this": {
        "question": "Find the 15th term of the AP: 10, 6, 2, −2, ...",
        "hint": "a = 10, d = 6 − 10 = −4. Use aₙ = a + (n−1)d.",
        "answer": "a₁₅ = 10 + 14 × (−4) = 10 − 56 = −46."
    },
    "fun_fact": "The concept of going 'straight to the nth term' is the heart of random access in computers — just like how a computer can jump to any memory address, you can jump to any term in an AP!"
}

QUESTIONS["math10.ap.nth_term"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.ap.nth_term"],
     "question": "Find the 30th term of the AP: 7, 10, 13, 16, ...",
     "hint": "a = 7, d = 3. Use aₙ = a + (n−1)d with n = 30.",
     "expected_answer": "a₃₀ = 7 + 29 × 3 = 7 + 87 = 94."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.ap.nth_term"],
     "question": "Which term of the AP 3, 8, 13, 18, ... is 78?",
     "hint": "78 = 3 + (n−1)×5. Solve for n.",
     "expected_answer": "78 = 3 + 5(n−1) → 75 = 5(n−1) → n−1 = 15 → n = 16. So 78 is the 16th term."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.ap.nth_term"],
     "question": "The 7th term of an AP is 34 and the 13th term is 64. Find the AP (first term and common difference).",
     "hint": "a₇ = a + 6d = 34 and a₁₃ = a + 12d = 64. Solve these simultaneous equations.",
     "expected_answer": "Subtract: 6d = 30 → d = 5. Then a = 34 − 30 = 4. AP: 4, 9, 14, 19, 24, 29, 34, ..."},
    {"id": 4, "type": "word_problem", "difficulty": 0.6, "concepts_tested": ["math10.ap.nth_term"],
     "question": "How many two-digit numbers are divisible by 7?",
     "hint": "The two-digit multiples of 7 form an AP: 14, 21, 28, ..., 98. Use aₙ = a + (n−1)d with last term = 98.",
     "expected_answer": "AP: 14, 21, 28, ..., 98. a = 14, d = 7, aₙ = 98. 98 = 14 + (n−1)7 → 84 = 7(n−1) → n = 13. There are 13 two-digit multiples of 7."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.ap.nth_term"],
     "question": "The 4th term of an AP is equal to 3 times the 1st term, and the 7th term exceeds twice the 3rd term by 1. Find the AP.",
     "hint": "a₄ = 3a₁ → a+3d = 3a. a₇ = 2a₃ + 1 → a+6d = 2(a+2d)+1.",
     "expected_answer": "From a+3d = 3a: 3d = 2a → a = 3d/2. From a+6d = 2a+4d+1: 2d = a+1. Substitute: 2d = 3d/2 + 1 → 4d = 3d + 2 → d = 2. Then a = 3. AP: 3, 5, 7, 9, 11, 13, ..."},
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 3 · Sum of First n Terms
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.ap.sum_n_terms"] = {
    "title": "∑ Sum of an AP — Gauss's Brilliant Trick",
    "hook": "Legend says young Carl Friedrich Gauss amazed his teacher by instantly summing 1+2+3+...+100 = 5050. His trick? Pair the first with the last: 1+100=101, 2+99=101, ... That's 50 pairs of 101 = 5050!",
    "explanation": (
        formula_box("Sₙ = n/2 × [2a + (n−1)d]", "Sum Formula (using a and d)")
        + formula_box("Sₙ = n/2 × (a + l)", "Sum Formula (using first and last term)")
        + "<p><b>Gauss's Trick Illustrated:</b> Sum of 1 + 2 + 3 + ... + 100:</p>"
        + comparison_table(
            ["Pairing", "Sum of pair"],
            [["1 + 100", "101"],
             ["2 + 99", "101"],
             ["3 + 98", "101"],
             ["...", "..."],
             ["50 + 51", "101"]]
        )
        + key_point("50 pairs × 101 = 5050. In general: n/2 × (first + last).")
        + tip_box("To find the nth term from partial sums: <b>aₙ = Sₙ − Sₙ₋₁</b> (for n ≥ 2).")
    ),
    "worked_example": (
        "<b>Example:</b> Find the sum of first 20 terms of the AP: 3, 7, 11, 15, ...<br><br>"
        + step_box([
            ("Identify a, d, n", "a = 3, d = 4, n = 20"),
            ("Use Sₙ = n/2 × [2a + (n−1)d]", "S₂₀ = 20/2 × [6 + 19×4] = 10 × [6 + 76] = 10 × 82 = 820"),
        ])
        + "<br><b>Alternative:</b> Find last term first: a₂₀ = 3 + 19(4) = 79. S₂₀ = 20/2 × (3 + 79) = 10 × 82 = 820. Same answer!"
    ),
    "try_this": {
        "question": "Find the sum of first 15 terms of the AP: 10, 7, 4, 1, ...",
        "hint": "a = 10, d = −3, n = 15.",
        "answer": "S₁₅ = 15/2 × [2(10) + 14(−3)] = 15/2 × [20 − 42] = 15/2 × (−22) = −165."
    },
    "fun_fact": "Gauss reportedly did this calculation at age 7! His teacher, J.G. Büttner, was so impressed that he got the young Gauss special math books to study."
}

QUESTIONS["math10.ap.sum_n_terms"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.ap.sum_n_terms"],
     "question": "Find the sum: 1 + 2 + 3 + ... + 50.",
     "hint": "AP with a=1, d=1, n=50. Use Sₙ = n/2 × (a + l).",
     "expected_answer": "S₅₀ = 50/2 × (1 + 50) = 25 × 51 = 1275."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.ap.sum_n_terms"],
     "question": "Find the sum of the first 24 terms of the AP: 5, 8, 11, 14, ...",
     "hint": "a=5, d=3, n=24.",
     "expected_answer": "S₂₄ = 24/2 × [2(5) + 23(3)] = 12 × [10 + 69] = 12 × 79 = 948."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.ap.sum_n_terms"],
     "question": "The first term of an AP is 5 and the last term is 45. The sum is 400. Find the number of terms and the common difference.",
     "hint": "Use S = n/2(a+l): 400 = n/2(5+45). Then find d from a + (n−1)d = 45.",
     "expected_answer": "400 = n/2 × 50 → n = 16. Then 45 = 5 + 15d → d = 40/15 = 8/3."},
    {"id": 4, "type": "word_problem", "difficulty": 0.65, "concepts_tested": ["math10.ap.sum_n_terms"],
     "question": "Find the sum of all multiples of 3 between 1 and 200.",
     "hint": "Multiples of 3: 3, 6, 9, ..., 198. This is an AP. Find n first: 198 = 3 + (n−1)×3.",
     "expected_answer": "AP: 3, 6, ..., 198. n: 198 = 3n → n = 66. S = 66/2 × (3 + 198) = 33 × 201 = 6633."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.ap.sum_n_terms"],
     "question": "If Sₙ = 3n² + 5n for an AP, find the common difference d and the 15th term.",
     "hint": "a₁ = S₁ = 8. a₂ = S₂ − S₁ = 22 − 8 = 14. d = a₂ − a₁ = 6. For aₙ: aₙ = Sₙ − Sₙ₋₁.",
     "expected_answer": "S₁ = 8, S₂ = 22, a₁ = 8, a₂ = 14, d = 6. a₁₅ = 8 + 14(6) = 92. Or: aₙ = Sₙ − Sₙ₋₁ = 3n²+5n − 3(n−1)²−5(n−1) = 6n+2. a₁₅ = 92. d = 6 (coefficient of n in 6n+2 times 1, since aₙ−aₙ₋₁ = 6)."},
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 4 · AP Applications
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.ap.applications"] = {
    "title": "🌎 AP Applications — From Savings Plans to Stacking Logs",
    "hook": "A man saves ₹1000 in January, ₹1200 in February, ₹1400 in March, and so on — increasing by ₹200 each month. How much does he save in the entire year? Real life is full of AP patterns!",
    "explanation": (
        "<p><b>Common Application Patterns:</b></p>"
        + comparison_table(
            ["Scenario", "What forms the AP?", "What to find?"],
            [["Salary with annual raise", "Monthly salaries", "Total earnings over n years"],
             ["Stacking objects", "Rows with decreasing count", "Total objects"],
             ["Regular savings", "Monthly savings amounts", "Total saved"],
             ["Depreciation", "Value each year", "When value drops below threshold"]]
        )
        + "<br><p><b>Strategy for AP word problems:</b></p>"
        + step_box([
            ("Identify the AP pattern", "What changes by a constant amount?"),
            ("Find a and d", "First term and common difference"),
            ("Decide: nth term or sum?", "Finding one value → aₙ. Finding total → Sₙ."),
            ("Apply the formula", "And check the answer makes sense!"),
        ], "#7B1FA2")
        + tip_box("If 3 numbers are in AP, take them as <b>a−d, a, a+d</b> — their sum is 3a, which simplifies many problems!")
    ),
    "worked_example": (
        "<b>Example:</b> A man starts saving ₹1000 in month 1 and increases by ₹200 each month. In which month does his total savings exceed ₹40,000?<br><br>"
        + step_box([
            ("AP terms", "1000, 1200, 1400, ... → a = 1000, d = 200"),
            ("Total = Sₙ > 40000", "n/2 × [2(1000) + (n−1)200] > 40000"),
            ("Simplify", "n/2 × [2000 + 200n − 200] > 40000 → n(1800 + 200n)/2 > 40000"),
            ("", "n(900 + 100n) > 40000 → 100n² + 900n − 40000 > 0"),
            ("Solve equality", "n² + 9n − 400 = 0 → n = (−9 + √1681)/2 = (−9 + 41)/2 = 16"),
            ("Check", "S₁₆ = 16/2 × [2000 + 3000] = 8 × 5000 = 40000. So total exceeds 40000 in month 17."),
        ])
    ),
    "try_this": {
        "question": "Logs are stacked: 20 in the bottom row, 19 in the next, 18 in the next, and so on, with 1 log on top. How many logs are there in total?",
        "hint": "AP: 20, 19, 18, ..., 1 with n = 20 terms. Find the sum.",
        "answer": "S₂₀ = 20/2 × (20 + 1) = 10 × 21 = 210 logs."
    },
    "fun_fact": "The famous Fibonacci sequence (1, 1, 2, 3, 5, 8, ...) is NOT an AP, but if you take the differences of consecutive Fibonacci numbers, you get... the Fibonacci sequence back!"
}

QUESTIONS["math10.ap.applications"] = [
    {"id": 1, "type": "word_problem", "difficulty": 0.35, "concepts_tested": ["math10.ap.applications"],
     "question": "A factory produced 500 units in its first year and increases production by 100 units each year. What will the production be in the 8th year?",
     "hint": "AP: a = 500, d = 100. Find a₈.",
     "expected_answer": "a₈ = 500 + 7(100) = 1200 units."},
    {"id": 2, "type": "word_problem", "difficulty": 0.45, "concepts_tested": ["math10.ap.applications"],
     "question": "In a flower bed, there are 23 rose plants in the first row, 21 in the second, 19 in the third, and so on. If the last row has 5 plants, how many rows are there and what's the total number of plants?",
     "hint": "AP: 23, 21, 19, ..., 5. a=23, d=−2, aₙ=5.",
     "expected_answer": "5 = 23 + (n−1)(−2) → −18 = −2(n−1) → n = 10 rows. Total = 10/2 × (23+5) = 5 × 28 = 140 plants."},
    {"id": 3, "type": "word_problem", "difficulty": 0.55, "concepts_tested": ["math10.ap.applications"],
     "question": "The sum of three numbers in AP is 27 and their product is 648. Find the numbers.",
     "hint": "Let them be a−d, a, a+d. Sum = 3a = 27 → a = 9. Product: (9−d)(9)(9+d) = 648.",
     "expected_answer": "3a = 27 → a = 9. Product: 9(81−d²) = 648 → 81−d² = 72 → d² = 9 → d = ±3. Numbers: 6, 9, 12 or 12, 9, 6."},
    {"id": 4, "type": "word_problem", "difficulty": 0.65, "concepts_tested": ["math10.ap.applications"],
     "question": "A person deposits ₹500 the first month and increases by ₹40 every month. After how many months will total savings reach ₹33,000?",
     "hint": "Sₙ = n/2[2(500)+(n−1)(40)] = 33000. Simplify to get a quadratic.",
     "expected_answer": "n/2[1000+40n−40] = 33000 → n(960+40n)/2 = 33000 → n(480+20n) = 33000 → 20n² + 480n − 33000 = 0 → n² + 24n − 1650 = 0. (n+54)(n−30) = 0. n = 30 months. Verify: S₃₀ = 15[1000+1160] = 15×2160... let me recalculate. S₃₀ = 30/2 × [1000+29(40)] = 15 × [1000+1160] = 15 × 2160 = 32400. Hmm not exactly 33000. Let me re-solve: 20n²+480n=33000, n²+24n−1650=0. D=576+6600=7176. √7176≈84.7. n = (−24+84.7)/2 ≈ 30.35. So after 31 months (total crosses 33000 in month 31)."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.ap.applications"],
     "question": "Find the sum of all two-digit odd numbers.",
     "hint": "Two-digit odd numbers: 11, 13, 15, ..., 99. This is an AP with a=11, d=2, last=99.",
     "expected_answer": "AP: 11, 13, ..., 99. n: 99 = 11 + (n−1)×2 → 88 = 2(n−1) → n = 45. S₄₅ = 45/2 × (11+99) = 45/2 × 110 = 45 × 55 = 2475."},
]
