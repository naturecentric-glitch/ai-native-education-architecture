"""Chapter 15 — Probability: 3 concepts, 15 questions."""
from .helpers import formula_box, step_box, tip_box, comparison_table, definition_box, key_point, info_box, warning_box

LESSONS = {}
QUESTIONS = {}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1 · Classical Probability
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.prob.classical"] = {
    "title": "🎲 Classical Probability — Equally Likely Outcomes",
    "hook": "What's the chance of rolling a 6 on a fair die? Getting heads on a coin flip? Drawing an ace from a deck? Probability tells us how likely something is to happen — expressed as a number between 0 and 1!",
    "explanation": (
        formula_box("P(E) = Number of favourable outcomes / Total number of outcomes", "Classical Probability")
        + comparison_table(
            ["Probability", "Meaning", "Example"],
            [["P(E) = 0", "Impossible event", "Rolling a 7 on a standard die"],
             ["0 < P(E) < 1", "Possible but not certain", "Rolling a 6: P = 1/6"],
             ["P(E) = 1", "Certain event", "Rolling a number < 7 on a die"]]
        )
        + formula_box("P(E) + P(not E) = 1  ⟹  P(not E) = 1 − P(E)", "Complementary Events")
        + key_point("All probabilities lie between 0 and 1 (inclusive). The sum of probabilities of all outcomes = 1.")
        + "<p><b>Common sample spaces:</b></p>"
        + comparison_table(
            ["Experiment", "Sample Space", "Total Outcomes"],
            [["1 coin", "{H, T}", "2"],
             ["2 coins", "{HH, HT, TH, TT}", "4"],
             ["1 die", "{1, 2, 3, 4, 5, 6}", "6"],
             ["2 dice", "All (a,b) pairs", "36"],
             ["Deck of cards", "52 cards: 4 suits × 13 values", "52"]]
        )
    ),
    "worked_example": (
        "<b>Example:</b> A bag has 3 red, 5 blue, and 2 green balls. One ball is drawn at random. Find the probability of getting: (a) a red ball, (b) not a green ball.<br><br>"
        + step_box([
            ("Total balls", "3 + 5 + 2 = 10"),
            ("P(red) = 3/10", ""),
            ("P(not green) = 1 − P(green) = 1 − 2/10 = 8/10 = 4/5", ""),
        ])
    ),
    "try_this": {
        "question": "A card is drawn from a well-shuffled deck of 52 cards. Find: (a) P(a king), (b) P(not a face card).",
        "hint": "Kings: 4. Face cards: J, Q, K = 12 total.",
        "answer": "(a) P(king) = 4/52 = 1/13. (b) Face cards = 12. P(not face) = 1 − 12/52 = 40/52 = 10/13."
    },
    "fun_fact": "Probability theory was born from gambling! In 1654, Pascal and Fermat exchanged letters about a dice problem posed by a gambler — and modern probability was born!"
}

QUESTIONS["math10.prob.classical"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.prob.classical"],
     "question": "A die is thrown once. Find the probability of getting: (a) a number greater than 4, (b) a prime number.",
     "hint": "Numbers > 4: {5, 6}. Primes: {2, 3, 5}.",
     "expected_answer": "(a) P(>4) = 2/6 = 1/3. (b) P(prime) = 3/6 = 1/2."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.prob.classical"],
     "question": "A box has 5 red, 4 white, and 6 blue marbles. One is drawn. Find P(red or blue).",
     "hint": "Red or blue = 5 + 6 = 11 out of 15.",
     "expected_answer": "P(red or blue) = 11/15."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.prob.classical"],
     "question": "A card is drawn from a deck of 52 cards. Find: (a) P(red king), (b) P(spade or ace).",
     "hint": "(a) Red kings: ♥K and ♦K = 2. (b) 13 spades + 4 aces − 1 ace of spades = 16.",
     "expected_answer": "(a) P(red king) = 2/52 = 1/26. (b) Spades=13, Aces=4, but Ace of Spades counted twice: 13+4−1=16. P = 16/52 = 4/13."},
    {"id": 4, "type": "word_problem", "difficulty": 0.65, "concepts_tested": ["math10.prob.classical"],
     "question": "A jar has 24 marbles: 8 red, 10 blue, 6 yellow. If P(drawing red) should be 1/2, how many red marbles should be added?",
     "hint": "After adding x red: total = 24+x, red = 8+x. (8+x)/(24+x) = 1/2.",
     "expected_answer": "(8+x)/(24+x) = 1/2 → 2(8+x) = 24+x → 16+2x = 24+x → x = 8. Add 8 red marbles."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.prob.classical"],
     "question": "Two dice are thrown simultaneously. Find: (a) P(sum = 7), (b) P(sum ≥ 10), (c) P(doublet — same number on both).",
     "hint": "Total outcomes = 36. Sum=7: (1,6),(2,5),(3,4),(4,3),(5,2),(6,1). Doublets: (1,1),...,(6,6).",
     "expected_answer": "(a) Sum=7: {(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)} = 6. P = 6/36 = 1/6. (b) Sum≥10: sum=10 has 3, sum=11 has 2, sum=12 has 1 → 6. P = 6/36 = 1/6. (c) Doublets: 6 outcomes. P = 6/36 = 1/6."},
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2 · Types of Events
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.prob.events"] = {
    "title": "🎯 Types of Events — Impossible, Sure, and Complementary",
    "hook": "Can you have a probability of 1.5? Or −0.3? Nope! And some events are guaranteed (certain), while others can never happen (impossible). Understanding event types is key to solving probability problems correctly.",
    "explanation": (
        comparison_table(
            ["Event Type", "Definition", "Probability", "Example (die)"],
            [["<b>Impossible</b>", "Can never occur", "P = 0", "Rolling a 7"],
             ["<b>Sure/Certain</b>", "Always occurs", "P = 1", "Rolling a number 1-6"],
             ["<b>Elementary</b>", "Single outcome", "1/n (if equally likely)", "Rolling exactly 3"],
             ["<b>Complementary</b>", "E and not-E together cover everything", "P(E)+P(E')=1", "Even vs. Odd"]]
        )
        + key_point("For any event E: <b>0 ≤ P(E) ≤ 1</b>")
        + formula_box("P(E) + P(Ē) = 1  ⟹  P(Ē) = 1 − P(E)", "Complement Rule")
        + tip_box("<b>When to use the complement:</b> If finding P(E) directly is hard, try: P(E) = 1 − P(not E). Example: P(at least one head in 3 tosses) = 1 − P(no heads) = 1 − (1/2)³ = 7/8.")
    ),
    "worked_example": (
        "<b>Example:</b> The probability that it rains today is 0.4. What is the probability it does NOT rain?<br><br>"
        + step_box([
            ("P(rain) = 0.4", ""),
            ("P(no rain) = 1 − P(rain) = 1 − 0.4 = 0.6", ""),
        ])
        + "<br><b>Example 2:</b> Is the following a valid probability distribution? Outcomes: A(0.2), B(0.3), C(0.6).<br><br>"
        + step_box([
            ("Sum = 0.2 + 0.3 + 0.6 = 1.1", ""),
            ("1.1 ≠ 1", "NOT valid! Probabilities must sum to exactly 1."),
        ])
    ),
    "try_this": {
        "question": "A bag has only red and blue balls. P(red) = 0.65. Find P(blue). Also, if there are 20 balls in total, how many are blue?",
        "hint": "P(blue) = 1 − P(red). Number of blue = P(blue) × total.",
        "answer": "P(blue) = 1 − 0.65 = 0.35. Number of blue = 0.35 × 20 = 7."
    },
    "fun_fact": "Complementary probability is how weather forecasts work! If there's a 70% chance of rain, there's a 30% chance it stays dry."
}

QUESTIONS["math10.prob.events"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.prob.events"],
     "question": "The probability of an event is 0.75. What is the probability of its complementary event?",
     "hint": "P(complement) = 1 − P(event).",
     "expected_answer": "P(complement) = 1 − 0.75 = 0.25."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.prob.events"],
     "question": "Which of the following can be the probability of an event? (a) −0.3 (b) 1.2 (c) 0 (d) 3/5 (e) 7/6.",
     "hint": "0 ≤ P(E) ≤ 1.",
     "expected_answer": "Valid: (c) 0 and (d) 3/5 = 0.6. Invalid: (a) negative, (b) > 1, (e) 7/6 > 1."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.prob.events"],
     "question": "A game gives you P(winning) = 0.3 and P(losing) = 0.6. What is the probability of a draw?",
     "hint": "P(win) + P(lose) + P(draw) = 1.",
     "expected_answer": "P(draw) = 1 − 0.3 − 0.6 = 0.1."},
    {"id": 4, "type": "word_problem", "difficulty": 0.65, "concepts_tested": ["math10.prob.events"],
     "question": "A box has 100 bulbs, 12 of which are defective. What is P(getting a non-defective bulb)? If 5 more defective bulbs are added, what is the new probability?",
     "hint": "P(non-defective) = 1 − P(defective). After addition, total = 105, defective = 17.",
     "expected_answer": "Original: P(non-defective) = 88/100 = 0.88. After: P(non-defective) = (100−12)/(100+5) = 88/105 ≈ 0.838. Wait — 5 more defective added: defective = 17, total = 105. P(non-defective) = 88/105 ≈ 0.838."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.prob.events"],
     "question": "Three coins are tossed. Using the complement rule, find P(at least one head).",
     "hint": "P(at least 1 head) = 1 − P(no heads) = 1 − P(all tails).",
     "expected_answer": "Total outcomes = 8 (HHH, HHT, HTH, HTT, THH, THT, TTH, TTT). P(all tails) = 1/8. P(at least 1 head) = 1 − 1/8 = 7/8."},
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 3 · Solving Probability Problems
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.prob.problems"] = {
    "title": "🧩 Probability Problem-Solving — Putting It All Together",
    "hook": "Now that you know the formulas, let's tackle the REAL challenge — word problems! From coins to cards to numbered balls, let's develop a systematic approach.",
    "explanation": (
        step_box([
            ("Read carefully — what's the experiment?", "Coin toss? Die roll? Drawing a card? Picking a ball?"),
            ("List the sample space (or at least count outcomes)", ""),
            ("Identify the event — what are 'favourable' outcomes?", ""),
            ("Count favourable outcomes", "Use listing, combination, or logic"),
            ("Apply P(E) = favourable / total", ""),
            ("Check: is your answer between 0 and 1?", "Sanity check!"),
        ], "#E65100")
        + info_box("<b>Common traps:</b><br>• Two dice: (3,4) and (4,3) are DIFFERENT outcomes (total 36, not 21).<br>• Cards: suit matters! King of Hearts ≠ King of Spades.<br>• 'At least one' → use complement method: 1 − P(none).")
        + comparison_table(
            ["Problem Type", "Strategy"],
            [["'At least one'", "Use complement: 1 − P(none)"],
             ["'Both' or 'all'", "Multiply individual probabilities (if independent)"],
             ["'Or' (either/or)", "Add: P(A) + P(B) − P(A and B)"],
             ["With replacement", "Probabilities stay same each draw"],
             ["Without replacement", "Probabilities change after each draw"]]
        )
    ),
    "worked_example": (
        "<b>Example:</b> Numbers 1-20 are written on tickets and put in a box. One ticket is drawn at random. Find: (a) P(multiple of 3 or 5), (b) P(multiple of 3 and 5).<br><br>"
        + step_box([
            ("Multiples of 3: {3,6,9,12,15,18} → 6 numbers", ""),
            ("Multiples of 5: {5,10,15,20} → 4 numbers", ""),
            ("Multiples of both 3 and 5 (i.e., 15): {15} → 1 number", ""),
            ("P(3 or 5) = (6+4−1)/20 = 9/20", "Subtract 15 to avoid double counting"),
            ("P(3 and 5) = 1/20", "Only 15"),
        ])
    ),
    "try_this": {
        "question": "A bag contains 15 white, 25 black, and 10 red balls. One ball is drawn. Find: (a) P(white or red), (b) P(not black), (c) P(neither white nor red).",
        "hint": "Total = 50. (a) and (c) are complements of each other!",
        "answer": "Total = 50. (a) P(white or red) = (15+10)/50 = 25/50 = 1/2. (b) P(not black) = 1 − 25/50 = 1/2. (c) P(neither white nor red) = P(black) = 25/50 = 1/2."
    },
    "fun_fact": "The famous 'Birthday Problem': In a group of just 23 people, there's a greater than 50% chance that two of them share a birthday! Most people guess you'd need hundreds."
}

QUESTIONS["math10.prob.problems"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.prob.problems"],
     "question": "Numbers 1 to 10 are in a bag. One is drawn. Find P(even number).",
     "hint": "Even: {2, 4, 6, 8, 10} = 5 out of 10.",
     "expected_answer": "P(even) = 5/10 = 1/2."},
    {"id": 2, "type": "word_problem", "difficulty": 0.4, "concepts_tested": ["math10.prob.problems"],
     "question": "A two-digit number is formed using digits 1, 2, 3, 4 (repetition allowed). Find P(the number is even).",
     "hint": "Total 2-digit numbers: 4 × 4 = 16. For even: last digit must be 2 or 4 → 4 × 2 = 8.",
     "expected_answer": "Total = 16. Even (last digit 2 or 4): 4 × 2 = 8. P = 8/16 = 1/2."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.prob.problems"],
     "question": "Two dice are rolled. Find P(product of numbers is 12).",
     "hint": "List pairs with product 12: (2,6), (3,4), (4,3), (6,2).",
     "expected_answer": "Pairs: (2,6), (3,4), (4,3), (6,2) = 4 outcomes. P = 4/36 = 1/9."},
    {"id": 4, "type": "word_problem", "difficulty": 0.7, "concepts_tested": ["math10.prob.problems"],
     "question": "A box has 90 discs numbered 1 to 90. One disc is drawn. Find: (a) P(two-digit number), (b) P(perfect square), (c) P(divisible by 5).",
     "hint": "(a) Two-digit: 10-90 = 81 numbers. (b) Squares: 1,4,9,...,81 = 9. (c) Div by 5: 5,10,...,90 = 18.",
     "expected_answer": "(a) Two-digit: 10 to 90 = 81 numbers. P = 81/90 = 9/10. (b) Perfect squares ≤ 90: 1,4,9,16,25,36,49,64,81 = 9. P = 9/90 = 1/10. (c) Divisible by 5: 5,10,...,90 = 18. P = 18/90 = 1/5."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.85, "concepts_tested": ["math10.prob.problems"],
     "question": "A game consists of tossing a coin 3 times. Ravi wins if he gets at least 2 heads. Priya wins if she gets at least 2 tails. Is the game fair? Who has a better chance?",
     "hint": "List all 8 outcomes for 3 coins: HHH, HHT, HTH, THH, HTT, THT, TTH, TTT.",
     "expected_answer": "Outcomes: {HHH, HHT, HTH, THH, HTT, THT, TTH, TTT}. Ravi (≥2 heads): {HHH, HHT, HTH, THH} = 4. P = 4/8 = 1/2. Priya (≥2 tails): {HTT, THT, TTH, TTT} = 4. P = 4/8 = 1/2. The game IS fair — both have equal probability of 1/2!"},
]
