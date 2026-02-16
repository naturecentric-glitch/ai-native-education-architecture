"""Chapter 1 — Real Numbers: 5 concepts, 25 questions."""
from .helpers import formula_box, step_box, tip_box, comparison_table, definition_box, key_point, info_box, warning_box

LESSONS = {}
QUESTIONS = {}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1 · Euclid's Division Lemma
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.real_numbers.euclid_division"] = {
    "title": "🔢 Euclid's Division Lemma — The Foundation of Number Theory",
    "hook": "When you divide 17 chocolates among 5 friends, each friend gets 3 and 2 are left over. This simple idea — that every division has a quotient and remainder — is the basis of one of the oldest and most powerful results in mathematics.",
    "explanation": (
        "<b>Euclid's Division Lemma</b> states:<br><br>"
        + formula_box("a = bq + r,  where 0 ≤ r &lt; b", "Euclid's Division Lemma")
        + "<p>For any two positive integers <b>a</b> (dividend) and <b>b</b> (divisor), there exist "
        "unique non-negative integers <b>q</b> (quotient) and <b>r</b> (remainder) such that the above holds.</p>"
        + comparison_table(
            ["Part", "Meaning", "Example (a=17, b=5)"],
            [["a (dividend)", "The number being divided", "17"],
             ["b (divisor)", "The number we divide by", "5"],
             ["q (quotient)", "How many times b fits in a", "3"],
             ["r (remainder)", "What's left over", "2"]]
        )
        + key_point("The remainder r is always ≥ 0 and strictly less than b. This is what makes the result unique.")
        + "<p><b>Why does this matter?</b> This lemma is the engine behind <em>Euclid's Algorithm</em> — a 2300-year-old method "
        "for finding the HCF of two numbers. We'll explore that next.</p>"
    ),
    "worked_example": (
        "<b>Example:</b> Express the relationship between 455 and 42 using Euclid's Division Lemma.<br><br>"
        + step_box([
            ("Divide 455 by 42", "455 ÷ 42 = 10 remainder 35"),
            ("Write in Lemma form", "455 = 42 × 10 + 35"),
            ("Verify remainder condition", "0 ≤ 35 &lt; 42 ✓"),
            ("Verify the equation", "42 × 10 + 35 = 420 + 35 = 455 ✓"),
        ])
        + tip_box("To find q, think: what is the largest multiple of b that doesn't exceed a?")
    ),
    "try_this": {
        "question": "Express 272 = 12 × q + r using Euclid's Division Lemma. Find q and r.",
        "hint": "Divide 272 by 12. What is the quotient and remainder?",
        "answer": "272 ÷ 12 = 22 remainder 8. So 272 = 12 × 22 + 8. Here q = 22, r = 8. Check: 12 × 22 + 8 = 264 + 8 = 272 ✓, and 0 ≤ 8 < 12 ✓."
    },
    "fun_fact": "Euclid wrote this in his book 'Elements' around 300 BC — making it over 2300 years old! It's one of the oldest algorithms still taught in schools today."
}

QUESTIONS["math10.real_numbers.euclid_division"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.real_numbers.euclid_division"],
     "question": "Use Euclid's Division Lemma to express the relationship between 135 and 12. Find q and r.",
     "hint": "Divide 135 by 12. Remember: a = bq + r where 0 ≤ r < b.",
     "expected_answer": "135 = 12 × 11 + 3. So q = 11 and r = 3. Check: 12 × 11 + 3 = 132 + 3 = 135 ✓, and 0 ≤ 3 < 12 ✓."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.real_numbers.euclid_division"],
     "question": "If a = 3q + r, a = 28, and r must satisfy Euclid's Division Lemma conditions for divisor 3, what are the possible values of r? Which one is correct?",
     "hint": "For divisor b = 3, the remainder r must satisfy 0 ≤ r < 3. Now find what 28 ÷ 3 gives.",
     "expected_answer": "Possible values of r: 0, 1, or 2 (since 0 ≤ r < 3). Now 28 ÷ 3 = 9 remainder 1. So 28 = 3 × 9 + 1, meaning r = 1."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.real_numbers.euclid_division"],
     "question": "A teacher has 170 notebooks. She wants to distribute them equally among 8 students. How many will each student get, and how many will be left? Express this using Euclid's Division Lemma.",
     "hint": "Let a = 170, b = 8. Find q and r such that 170 = 8q + r.",
     "expected_answer": "170 = 8 × 21 + 2. Each student gets 21 notebooks and 2 are left over. Check: 8 × 21 + 2 = 168 + 2 = 170 ✓."},
    {"id": 4, "type": "word_problem", "difficulty": 0.6, "concepts_tested": ["math10.real_numbers.euclid_division"],
     "question": "Show that any positive integer is of the form 3q, 3q + 1, or 3q + 2 for some integer q ≥ 0.",
     "hint": "Apply Euclid's Division Lemma with b = 3. What are the possible remainders?",
     "expected_answer": "By Euclid's Division Lemma, for any positive integer a and b = 3: a = 3q + r where 0 ≤ r < 3. So r can be 0, 1, or 2. Therefore a = 3q (when r=0), a = 3q+1 (when r=1), or a = 3q+2 (when r=2). These cover all positive integers."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.75, "concepts_tested": ["math10.real_numbers.euclid_division"],
     "question": "Show that the square of any positive integer is of the form 3m or 3m + 1 (but never 3m + 2).",
     "hint": "Start by writing any integer as 3q, 3q+1, or 3q+2. Then square each form and simplify.",
     "expected_answer": "Any integer n = 3q, 3q+1, or 3q+2. Case 1: (3q)² = 9q² = 3(3q²) = 3m where m = 3q². Case 2: (3q+1)² = 9q²+6q+1 = 3(3q²+2q)+1 = 3m+1. Case 3: (3q+2)² = 9q²+12q+4 = 3(3q²+4q+1)+1 = 3m+1. So n² is always 3m or 3m+1, never 3m+2."},
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2 · Finding HCF Using Euclid's Algorithm
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.real_numbers.euclid_hcf"] = {
    "title": "🔄 Euclid's Algorithm — Finding HCF the Smart Way",
    "hook": "You have two ropes of lengths 240 cm and 180 cm. You want to cut them into pieces of the same length, with no waste. What's the longest piece you can cut? This is finding the HCF — and Euclid showed us how over 2000 years ago.",
    "explanation": (
        "<b>Euclid's Algorithm</b> finds the HCF (Highest Common Factor) of two numbers by repeatedly applying the Division Lemma:<br><br>"
        + definition_box("Key Insight", "HCF(a, b) = HCF(b, r), where a = bq + r. Replace the bigger number with the remainder and repeat until remainder = 0.")
        + step_box([
            ("Start with two numbers a, b (a > b)", "Apply: a = bq + r"),
            ("Replace (a, b) with (b, r)", "Now find HCF(b, r)"),
            ("Repeat until remainder = 0", "The divisor at this step is the HCF"),
        ], "#2E7D32")
        + info_box("Think of it as a chain: HCF(a,b) → HCF(b,r₁) → HCF(r₁,r₂) → ... → HCF(rₙ,0) = rₙ")
        + "<p>The algorithm always terminates because the remainders keep getting smaller (r₁ > r₂ > r₃ > ... ≥ 0).</p>"
    ),
    "worked_example": (
        "<b>Example:</b> Find HCF(867, 255) using Euclid's Algorithm.<br><br>"
        + step_box([
            ("867 = 255 × 3 + 102", "Divide 867 by 255 → remainder 102"),
            ("255 = 102 × 2 + 51", "Divide 255 by 102 → remainder 51"),
            ("102 = 51 × 2 + 0", "Divide 102 by 51 → remainder 0 ✅"),
        ], "#1565C0")
        + key_point("<b>HCF(867, 255) = 51</b> — the last non-zero remainder.")
        + tip_box("Verify: 867 = 51 × 17 and 255 = 51 × 5 ✓")
    ),
    "try_this": {
        "question": "Find HCF(196, 38846) using Euclid's Algorithm.",
        "hint": "Start with 38846 = 196 × q + r. Keep applying until remainder = 0.",
        "answer": "38846 = 196 × 198 + 38. 196 = 38 × 5 + 6. 38 = 6 × 6 + 2. 6 = 2 × 3 + 0. HCF = 2."
    },
    "fun_fact": "Euclid's Algorithm is one of the most efficient algorithms ever invented. It can find the HCF of two 100-digit numbers in under a second on a modern computer!"
}

QUESTIONS["math10.real_numbers.euclid_hcf"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.real_numbers.euclid_hcf"],
     "question": "Find the HCF of 56 and 88 using Euclid's Algorithm.",
     "hint": "Start: 88 = 56 × q + r. Then continue with 56 and r.",
     "expected_answer": "88 = 56 × 1 + 32. 56 = 32 × 1 + 24. 32 = 24 × 1 + 8. 24 = 8 × 3 + 0. HCF(56, 88) = 8."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.real_numbers.euclid_hcf"],
     "question": "Find the HCF of 420 and 130 using Euclid's Algorithm.",
     "hint": "420 = 130 × q + r. Keep going until remainder is 0.",
     "expected_answer": "420 = 130 × 3 + 30. 130 = 30 × 4 + 10. 30 = 10 × 3 + 0. HCF(420, 130) = 10."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.real_numbers.euclid_hcf"],
     "question": "A rectangular courtyard is 18 m by 12 m. Find the minimum number of identical square tiles needed to pave it completely.",
     "hint": "Side of tile = HCF(18, 12). Then count = area of court ÷ area of one tile.",
     "expected_answer": "HCF(18, 12): 18 = 12×1 + 6, 12 = 6×2 + 0. HCF = 6. Tile side = 6 m. Number of tiles = (18×12)/(6×6) = 216/36 = 6 tiles."},
    {"id": 4, "type": "word_problem", "difficulty": 0.6, "concepts_tested": ["math10.real_numbers.euclid_hcf"],
     "question": "Find the HCF of 135 and 225. Then express it as 135x + 225y for some integers x, y.",
     "hint": "First find HCF, then work Euclid's steps backwards to express the HCF as a combination of 135 and 225.",
     "expected_answer": "225 = 135×1 + 90. 135 = 90×1 + 45. 90 = 45×2 + 0. HCF = 45. Back-substitute: 45 = 135 − 90×1 = 135 − (225−135)×1 = 135×2 − 225×1. So x = 2, y = −1. Check: 135×2 + 225×(−1) = 270−225 = 45 ✓."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.real_numbers.euclid_hcf"],
     "question": "An army contingent of 616 members is to march behind an army band of 32 members in a parade. Both groups must march in the same number of columns. What is the maximum number of columns?",
     "hint": "Maximum columns = HCF(616, 32). Apply Euclid's Algorithm.",
     "expected_answer": "616 = 32×19 + 8. 32 = 8×4 + 0. HCF(616, 32) = 8. Maximum number of columns = 8."},
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 3 · Fundamental Theorem of Arithmetic
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.real_numbers.fundamental_theorem"] = {
    "title": "🧱 Fundamental Theorem of Arithmetic — Every Number's DNA",
    "hook": "Just like every molecule is made of atoms, every number bigger than 1 is built from prime numbers. And just like a molecule has a unique atomic formula, every number has a unique prime factorization. This is the 'DNA' of numbers!",
    "explanation": (
        definition_box("Fundamental Theorem of Arithmetic",
                       "Every composite number can be expressed as a product of primes, and this factorization is unique (apart from the order of factors).")
        + "<p><b>Examples of Prime Factorization:</b></p>"
        + comparison_table(
            ["Number", "Prime Factorization", "Shorthand"],
            [["12", "2 × 2 × 3", "2² × 3"],
             ["36", "2 × 2 × 3 × 3", "2² × 3²"],
             ["180", "2 × 2 × 3 × 3 × 5", "2² × 3² × 5"],
             ["1001", "7 × 11 × 13", "7 × 11 × 13"]]
        )
        + "<p><b>Using FTA to find HCF and LCM:</b></p>"
        + formula_box("HCF = product of common primes with <u>lowest</u> powers", "HCF Rule")
        + formula_box("LCM = product of all primes with <u>highest</u> powers", "LCM Rule")
        + formula_box("HCF(a,b) × LCM(a,b) = a × b", "Relationship")
        + tip_box("The HCF × LCM property only works for exactly two numbers, not three or more!")
    ),
    "worked_example": (
        "<b>Example:</b> Find HCF and LCM of 96 and 404.<br><br>"
        + step_box([
            ("Factorise 96", "96 = 2 × 48 = 2 × 2 × 24 = 2 × 2 × 2 × 12 = 2 × 2 × 2 × 2 × 6 = 2⁵ × 3"),
            ("Factorise 404", "404 = 2 × 202 = 2 × 2 × 101 = 2² × 101"),
            ("Find HCF", "Common primes with lowest powers: 2² = 4. So HCF = 4"),
            ("Find LCM", "All primes with highest powers: 2⁵ × 3 × 101 = 32 × 3 × 101 = 9696"),
            ("Verify", "HCF × LCM = 4 × 9696 = 38784 = 96 × 404 ✓"),
        ])
    ),
    "try_this": {
        "question": "Find the LCM and HCF of 510 and 92 using prime factorization. Verify that LCM × HCF = 510 × 92.",
        "hint": "510 = 2 × 3 × 5 × 17.  92 = 2² × 23. Now apply the rules.",
        "answer": "510 = 2 × 3 × 5 × 17. 92 = 2² × 23. HCF = 2 (common prime, lowest power). LCM = 2² × 3 × 5 × 17 × 23 = 4 × 3 × 5 × 17 × 23 = 23460. Verify: 2 × 23460 = 46920 = 510 × 92 ✓."
    },
    "fun_fact": "The Fundamental Theorem of Arithmetic was first proved rigorously by Carl Friedrich Gauss in his 1801 book 'Disquisitiones Arithmeticae' — though Euclid had essentially stated it 2000 years earlier!"
}

QUESTIONS["math10.real_numbers.fundamental_theorem"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.real_numbers.fundamental_theorem"],
     "question": "Find the prime factorization of 3825.",
     "hint": "Start dividing by the smallest prime. Is 3825 divisible by 3? By 5?",
     "expected_answer": "3825 ÷ 3 = 1275. 1275 ÷ 3 = 425. 425 ÷ 5 = 85. 85 ÷ 5 = 17 (prime). So 3825 = 3² × 5² × 17."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.real_numbers.fundamental_theorem"],
     "question": "Find HCF and LCM of 12, 15 and 21 using prime factorization.",
     "hint": "12 = 2² × 3, 15 = 3 × 5, 21 = 3 × 7. HCF = common primes with lowest powers. LCM = all primes with highest powers.",
     "expected_answer": "12 = 2² × 3. 15 = 3 × 5. 21 = 3 × 7. HCF = 3 (the only common prime). LCM = 2² × 3 × 5 × 7 = 420."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.real_numbers.fundamental_theorem"],
     "question": "Two tankers contain 850 litres and 680 litres of fuel. Find the maximum capacity of a container that can measure the fuel of either tanker an exact number of times.",
     "hint": "You need the HCF of 850 and 680. Use prime factorization.",
     "expected_answer": "850 = 2 × 5² × 17. 680 = 2³ × 5 × 17. HCF = 2 × 5 × 17 = 170. Maximum capacity = 170 litres."},
    {"id": 4, "type": "word_problem", "difficulty": 0.6, "concepts_tested": ["math10.real_numbers.fundamental_theorem"],
     "question": "Given HCF(306, 657) = 9, find LCM(306, 657).",
     "hint": "Use the relationship: HCF × LCM = Product of the two numbers.",
     "expected_answer": "HCF × LCM = 306 × 657. So LCM = (306 × 657) / 9 = 201042 / 9 = 22338."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.real_numbers.fundamental_theorem"],
     "question": "Explain why 7 × 11 × 13 + 13 is a composite number. Is 7 × 6 × 5 × 4 × 3 × 2 × 1 + 5 composite?",
     "hint": "Factor out a common factor from each expression.",
     "expected_answer": "7 × 11 × 13 + 13 = 13(7 × 11 + 1) = 13 × 78 = 13 × 78. Since it has a factor of 13 (and 78), it's composite. 7 × 6 × 5 × 4 × 3 × 2 × 1 + 5 = 5(7 × 6 × 4 × 3 × 2 × 1 + 1) = 5 × (1008 + 1) = 5 × 1009. Since 1009 is prime, the number = 5 × 1009, which is composite."},
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 4 · Proving Irrationality
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.real_numbers.irrational_proofs"] = {
    "title": "🔍 Proving Irrationality — The Art of Contradiction",
    "hook": "Can you write √2 as a fraction? The ancient Greeks were shocked to discover you can't! The proof is one of the most beautiful in all of mathematics — and it uses a clever trick called 'proof by contradiction'.",
    "explanation": (
        definition_box("Proof by Contradiction",
                       "Assume the opposite of what you want to prove. Show this leads to a logical impossibility. Therefore the original statement must be true.")
        + "<p><b>Key Tool:</b> If p is a prime and p divides a², then p divides a.</p>"
        + "<p><b>The Classic Proof: √2 is irrational</b></p>"
        + step_box([
            ("Assume √2 is rational", "Then √2 = a/b where a, b are coprime integers (no common factor)"),
            ("Square both sides", "2 = a²/b², so a² = 2b²"),
            ("Conclude a is even", "Since a² = 2b², a² is divisible by 2, so a must be even. Write a = 2k."),
            ("Substitute and simplify", "(2k)² = 2b² → 4k² = 2b² → b² = 2k² → b is also even"),
            ("Reach contradiction", "Both a and b are even → they share factor 2. But we said a/b is in lowest terms! Contradiction ⚡"),
        ])
        + formula_box("∴ √2 is irrational ∎")
        + info_box("The same technique works for √3, √5, √7 — any square root of a prime number is irrational.")
        + "<p><b>Extending:</b> Expressions like 3 + 2√5 and 1/√3 are also irrational (assuming √5, √3 are irrational).</p>"
    ),
    "worked_example": (
        "<b>Example:</b> Prove that 3 + 2√5 is irrational.<br><br>"
        + step_box([
            ("Assume rational", "Suppose 3 + 2√5 = a/b (a, b integers, b ≠ 0)"),
            ("Isolate √5", "2√5 = a/b − 3 = (a − 3b)/b, so √5 = (a − 3b)/(2b)"),
            ("Check RHS", "(a − 3b)/(2b) is rational (ratio of integers)"),
            ("Contradiction", "But √5 is irrational! A rational number cannot equal an irrational number."),
        ])
        + formula_box("∴ 3 + 2√5 is irrational ∎")
    ),
    "try_this": {
        "question": "Prove that √3 is irrational.",
        "hint": "Follow the same method as the √2 proof but use the fact: if 3 divides a², then 3 divides a.",
        "answer": "Assume √3 = a/b (coprime). Then 3 = a²/b², so a² = 3b². Since 3|a², we get 3|a, so a = 3k. Then 9k² = 3b², so b² = 3k², meaning 3|b. Both a and b divisible by 3 — contradicts coprime assumption. ∴ √3 is irrational."
    },
    "fun_fact": "Legend says Hippasus of Metapontum discovered irrational numbers around 500 BC while studying the diagonal of a unit square (which is √2). The Pythagoreans were reportedly so disturbed by this discovery that they drowned him at sea!"
}

QUESTIONS["math10.real_numbers.irrational_proofs"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.real_numbers.irrational_proofs"],
     "question": "Classify each as rational or irrational: (a) √4  (b) √7  (c) 2 + √3  (d) π − π",
     "hint": "√4 = 2, which is rational. √7 cannot be simplified to a fraction. For (d), what is π − π?",
     "expected_answer": "(a) Rational — √4 = 2 (integer). (b) Irrational — 7 is prime, so √7 is irrational. (c) Irrational — sum of rational (2) and irrational (√3) is irrational. (d) Rational — π − π = 0."},
    {"id": 2, "type": "direct", "difficulty": 0.45, "concepts_tested": ["math10.real_numbers.irrational_proofs"],
     "question": "Prove that √5 is irrational.",
     "hint": "Use proof by contradiction. If 5 divides a², then 5 divides a.",
     "expected_answer": "Assume √5 = a/b (coprime). Then a² = 5b². Since 5|a², 5|a, so a = 5k. Then 25k² = 5b², so b² = 5k², hence 5|b. Contradiction: a, b share factor 5. ∴ √5 is irrational."},
    {"id": 3, "type": "word_problem", "difficulty": 0.55, "concepts_tested": ["math10.real_numbers.irrational_proofs"],
     "question": "Prove that 5 − 3√2 is irrational.",
     "hint": "Assume it equals a/b. Isolate √2 and show a contradiction.",
     "expected_answer": "Assume 5 − 3√2 = a/b (rational). Then 3√2 = 5 − a/b = (5b−a)/b. So √2 = (5b−a)/(3b), which is rational. But √2 is irrational — contradiction. ∴ 5 − 3√2 is irrational."},
    {"id": 4, "type": "word_problem", "difficulty": 0.65, "concepts_tested": ["math10.real_numbers.irrational_proofs"],
     "question": "Prove that 1/√2 is irrational.",
     "hint": "Rationalize or use contradiction directly.",
     "expected_answer": "Assume 1/√2 = a/b (rational). Then √2 = b/a, which is rational. But √2 is irrational — contradiction. ∴ 1/√2 is irrational. (Alternatively: 1/√2 = √2/2 — a non-zero rational times an irrational is irrational.)"},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.real_numbers.irrational_proofs"],
     "question": "Show that √2 + √3 is irrational.",
     "hint": "Assume √2 + √3 = r (rational). Square both sides: 2 + 2√6 + 3 = r². Isolate √6.",
     "expected_answer": "Assume √2 + √3 = r (rational). Squaring: 2 + 2√6 + 3 = r², so 2√6 = r² − 5, hence √6 = (r²−5)/2. RHS is rational. But √6 is irrational (since 6 has prime factor 2 or 3 not a perfect square). Contradiction. ∴ √2 + √3 is irrational."},
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 5 · Decimal Expansions of Rationals
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.real_numbers.decimal_expansions"] = {
    "title": "🔢 Decimal Expansions — Terminating or Repeating?",
    "hook": "1/4 = 0.25 (it stops!), but 1/3 = 0.333... (it repeats forever). Why? The secret lies in the prime factors of the denominator.",
    "explanation": (
        "<b>Key Theorem:</b><br>"
        + formula_box("p/q terminates ⟺ q = 2ⁿ × 5ᵐ (after simplifying to lowest terms)", "Termination Test")
        + comparison_table(
            ["Fraction", "Denominator", "Prime factors of q", "Decimal", "Type"],
            [["13/80", "80 = 2⁴ × 5", "Only 2 and 5", "0.1625", "Terminating"],
             ["7/25", "25 = 5²", "Only 5", "0.28", "Terminating"],
             ["1/6", "6 = 2 × 3", "Has 3 ← not just 2,5", "0.1666…", "Non-terminating repeating"],
             ["1/7", "7", "Has 7 ← not just 2,5", "0.142857…", "Non-terminating repeating"]]
        )
        + key_point("<b>Why 2 and 5?</b> Our decimal system is base 10 = 2 × 5. A fraction terminates only if the denominator divides some power of 10 = 2ⁿ × 5ⁿ.")
        + warning_box("Always reduce the fraction to lowest terms first! 6/15 = 2/5, and 5 = 5¹ (only 5), so it terminates: 0.4.")
    ),
    "worked_example": (
        "<b>Example:</b> Without actually dividing, state whether each decimal expansion terminates or not:<br>"
        "(a) 13/3125  (b) 17/8  (c) 64/455<br><br>"
        + step_box([
            ("(a) 3125 = 5⁵", "Only prime factor is 5 → Terminates"),
            ("(b) 8 = 2³", "Only prime factor is 2 → Terminates"),
            ("(c) 455 = 5 × 91 = 5 × 7 × 13", "Has primes 7 and 13 besides 5 → Non-terminating repeating"),
        ])
    ),
    "try_this": {
        "question": "Without dividing, determine if 29/343 has a terminating decimal. If 77/210 is simplified, does it terminate?",
        "hint": "Factorise each denominator. For 77/210, simplify first.",
        "answer": "343 = 7³ → has prime 7 (not just 2,5) → Non-terminating repeating. 77/210: GCD(77,210)=7, so 77/210 = 11/30. 30 = 2×3×5 → has prime 3 → Non-terminating repeating."
    },
    "fun_fact": "The decimal expansion of 1/97 has a repeating block of 96 digits! The maximum repeating block length for 1/p is always p−1."
}

QUESTIONS["math10.real_numbers.decimal_expansions"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.real_numbers.decimal_expansions"],
     "question": "Without dividing, determine which of the following has a terminating decimal: (a) 7/16  (b) 3/11  (c) 9/40",
     "hint": "Factor each denominator. Terminating ⟺ only 2s and 5s.",
     "expected_answer": "(a) 16 = 2⁴ → only 2s → Terminating. (b) 11 is prime (not 2 or 5) → Non-terminating repeating. (c) 40 = 2³ × 5 → only 2s and 5s → Terminating."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.real_numbers.decimal_expansions"],
     "question": "Express 13/3125 in decimal form without long division.",
     "hint": "3125 = 5⁵. Multiply top and bottom to make denominator a power of 10.",
     "expected_answer": "3125 = 5⁵. Multiply by 2⁵/2⁵: 13 × 32 / (5⁵ × 2⁵) = 416 / 10⁵ = 416/100000 = 0.00416."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.real_numbers.decimal_expansions"],
     "question": "Simplify 14/350 and determine if its decimal expansion terminates.",
     "hint": "Find GCD(14, 350) first, reduce, then check the denominator.",
     "expected_answer": "GCD(14, 350) = 14. So 14/350 = 1/25. 25 = 5² → only 5s → Terminates. In fact, 1/25 = 4/100 = 0.04."},
    {"id": 4, "type": "word_problem", "difficulty": 0.6, "concepts_tested": ["math10.real_numbers.decimal_expansions"],
     "question": "After how many decimal places will 23/(2³ × 5²) terminate?",
     "hint": "Make the denominator a power of 10. Which exponent is larger, the 2 or the 5?",
     "expected_answer": "Denominator = 2³ × 5² = 8 × 25 = 200. To make 10ⁿ, we need 2³ × 5³ = 1000. Multiply top and bottom by 5: 23×5/1000 = 115/1000 = 0.115. Terminates after 3 decimal places."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.75, "concepts_tested": ["math10.real_numbers.decimal_expansions"],
     "question": "The decimal expansion of p/q (in lowest terms) terminates after exactly 4 decimal places. What conditions must q satisfy? Give an example.",
     "hint": "Terminating after 4 places means p/q = m/10⁴ for some integer m. So q must divide 10⁴.",
     "expected_answer": "If it terminates after exactly 4 places, q must divide 10⁴ = 2⁴ × 5⁴. So q = 2ᵃ × 5ᵇ where max(a,b) = 4. Example: q = 625 = 5⁴. Then 1/625 = 16/10000 = 0.0016 (exactly 4 places)."},
]
