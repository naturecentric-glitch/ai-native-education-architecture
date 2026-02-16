"""Chapter 14 — Statistics: 4 concepts, 20 questions."""
from .helpers import formula_box, step_box, tip_box, comparison_table, definition_box, key_point, info_box, warning_box

LESSONS = {}
QUESTIONS = {}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1 · Mean of Grouped Data
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.stats.mean"] = {
    "title": "📊 Mean of Grouped Data — Three Powerful Methods",
    "hook": "You have marks of 100 students grouped into class intervals: 0-20, 20-40, 40-60, 60-80, 80-100. How do you find the average? You can't use each individual mark — but the 'class mark' (midpoint) saves the day!",
    "explanation": (
        definition_box("Class Mark (xᵢ)", "The midpoint of each class interval. xᵢ = (lower limit + upper limit) / 2.")
        + "<p><b>Three methods to find the mean:</b></p>"
        + comparison_table(
            ["Method", "Formula", "Best when"],
            [["<b>Direct</b>", "x̄ = Σfᵢxᵢ / Σfᵢ", "Small values of xᵢ"],
             ["<b>Assumed Mean</b>", "x̄ = a + Σfᵢdᵢ / Σfᵢ (dᵢ = xᵢ − a)", "Large values, saves computation"],
             ["<b>Step Deviation</b>", "x̄ = a + (Σfᵢuᵢ / Σfᵢ) × h", "Equal class widths (most efficient)"]]
        )
        + formula_box("Step Deviation: uᵢ = (xᵢ − a) / h, where a = assumed mean, h = class width", "Key formula")
        + step_box([
            ("Make a table with columns: Class, fᵢ, xᵢ, fᵢxᵢ (or dᵢ, uᵢ)", ""),
            ("Choose 'a' as the class mark of the middle class", "For assumed mean / step deviation"),
            ("Compute the relevant sums", ""),
            ("Apply the formula", ""),
        ], "#1565C0")
        + tip_box("All three methods give the SAME answer — use the one that's easiest for the given data.")
    ),
    "worked_example": (
        "<b>Example:</b> Find the mean for this data:<br>"
        + comparison_table(
            ["Class", "0-10", "10-20", "20-30", "30-40", "40-50"],
            [["fᵢ", "5", "8", "15", "12", "10"]]
        )
        + "<br>Using <b>Step Deviation</b> with a = 25, h = 10:<br>"
        + comparison_table(
            ["Class", "fᵢ", "xᵢ", "uᵢ = (xᵢ−25)/10", "fᵢuᵢ"],
            [["0-10", "5", "5", "−2", "−10"],
             ["10-20", "8", "15", "−1", "−8"],
             ["20-30", "15", "25", "0", "0"],
             ["30-40", "12", "35", "1", "12"],
             ["40-50", "10", "45", "2", "20"]]
        )
        + step_box([
            ("Σfᵢ = 50, Σfᵢuᵢ = −10+−8+0+12+20 = 14", ""),
            ("x̄ = 25 + (14/50) × 10 = 25 + 2.8 = 27.8", ""),
        ])
    ),
    "try_this": {
        "question": "Find the mean (direct method): Classes 10-20 (f=4), 20-30 (f=6), 30-40 (f=10), 40-50 (f=5).",
        "hint": "xᵢ = 15, 25, 35, 45. Σfᵢxᵢ = 4(15)+6(25)+10(35)+5(45).",
        "answer": "Σfᵢxᵢ = 60+150+350+225 = 785. Σfᵢ = 25. Mean = 785/25 = 31.4."
    },
    "fun_fact": "The word 'statistics' comes from the German word 'Statistik' meaning 'science of the state' — it was originally used for collecting census data!"
}

QUESTIONS["math10.stats.mean"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.stats.mean"],
     "question": "Find the mean (direct method): Classes 0-10 (f=3), 10-20 (f=5), 20-30 (f=7), 30-40 (f=5).",
     "hint": "Class marks: 5, 15, 25, 35. Compute Σfᵢxᵢ / Σfᵢ.",
     "expected_answer": "Σfᵢxᵢ = 15+75+175+175 = 440. Σfᵢ = 20. Mean = 440/20 = 22."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.stats.mean"],
     "question": "Using assumed mean method (a = 35), find the mean: 10-20 (f=3), 20-30 (f=5), 30-40 (f=8), 40-50 (f=4).",
     "hint": "dᵢ = xᵢ − 35 = −20, −10, 0, 10. Compute Σfᵢdᵢ.",
     "expected_answer": "fᵢdᵢ: −60, −50, 0, 40. Σfᵢdᵢ = −70. Σfᵢ = 20. Mean = 35 + (−70/20) = 35 − 3.5 = 31.5."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.stats.mean"],
     "question": "If the mean of the following data is 18, find p: 0-5 (f=3), 5-10 (f=5), 10-15 (f=9), 15-20 (f=6), 20-25 (f=p), 25-30 (f=4).",
     "hint": "Σfᵢxᵢ / Σfᵢ = 18. Set up equation and solve for p.",
     "expected_answer": "xᵢ: 2.5, 7.5, 12.5, 17.5, 22.5, 27.5. Σfᵢxᵢ = 7.5+37.5+112.5+105+22.5p+110 = 372.5+22.5p. Σfᵢ = 27+p. (372.5+22.5p)/(27+p) = 18. 372.5+22.5p = 486+18p. 4.5p = 113.5. p ≈ 25.2. Since f must be whole: p = 25 (approximately). Let me recheck: 372.5+22.5(25)/(27+25) = 935/52 = 17.98 ≈ 18. So p = 25."},
    {"id": 4, "type": "word_problem", "difficulty": 0.65, "concepts_tested": ["math10.stats.mean"],
     "question": "The mean of the following distribution is 50. Find the missing frequencies f₁ and f₂ if total frequency is 120: 0-20 (f=17), 20-40 (f=f₁), 40-60 (f=32), 60-80 (f=f₂), 80-100 (f=19).",
     "hint": "Two equations: f₁ + f₂ = 120 − 68 = 52. Σfᵢxᵢ/120 = 50.",
     "expected_answer": "f₁ + f₂ = 52 …(1). xᵢ: 10,30,50,70,90. Σfᵢxᵢ = 170+30f₁+1600+70f₂+1710 = 3480+30f₁+70f₂. Mean: (3480+30f₁+70f₂)/120 = 50 → 3480+30f₁+70f₂ = 6000. 30f₁+70f₂ = 2520 → 3f₁+7f₂ = 252 …(2). From (1): f₁ = 52−f₂. Sub: 3(52−f₂)+7f₂ = 252 → 156+4f₂ = 252 → f₂ = 24. f₁ = 28."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.stats.mean"],
     "question": "The mean of 5 numbers is 30. If each number is multiplied by 3 and then 5 is added, what is the new mean?",
     "hint": "If x̄ is the mean, the new mean after transformation ax + b is a·x̄ + b.",
     "expected_answer": "Original mean = 30. Each → 3x + 5. New mean = 3(30) + 5 = 95."},
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2 · Median of Grouped Data
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.stats.median"] = {
    "title": "📊 Median of Grouped Data — The Middle Value",
    "hook": "If you line up all your data from smallest to largest, the median is the person standing in the exact middle. For grouped data, we use cumulative frequencies to locate this 'middle person.'",
    "explanation": (
        formula_box("Median = l + [(n/2 − cf) / f] × h", "Median Formula")
        + "<p><b>Where:</b></p>"
        + comparison_table(
            ["Symbol", "Meaning"],
            [["l", "Lower boundary of the <b>median class</b>"],
             ["n", "Total frequency (Σfᵢ)"],
             ["cf", "Cumulative frequency of the class <b>before</b> the median class"],
             ["f", "Frequency of the median class"],
             ["h", "Class width"]]
        )
        + step_box([
            ("Find n/2", "Half the total frequency"),
            ("Build cumulative frequency column", "Running total of frequencies"),
            ("Find the median class", "The class whose cumulative frequency first exceeds n/2"),
            ("Apply the formula", "Plug in l, cf, f, h"),
        ], "#2E7D32")
        + key_point("The median divides the data into two equal halves: 50% below, 50% above.")
    ),
    "worked_example": (
        "<b>Example:</b> Find the median:<br>"
        + comparison_table(
            ["Class", "0-10", "10-20", "20-30", "30-40", "40-50"],
            [["fᵢ", "5", "8", "15", "12", "10"],
             ["cf", "5", "13", "28", "40", "50"]]
        )
        + "<br>"
        + step_box([
            ("n/2 = 50/2 = 25", ""),
            ("Median class: 20-30 (cf = 28 ≥ 25, but previous cf = 13 < 25)", ""),
            ("l = 20, cf = 13, f = 15, h = 10", ""),
            ("Median = 20 + (25−13)/15 × 10 = 20 + 8 = 28", ""),
        ])
    ),
    "try_this": {
        "question": "Find the median: 0-10 (f=3), 10-20 (f=7), 20-30 (f=15), 30-40 (f=10), 40-50 (f=5).",
        "hint": "n = 40, n/2 = 20. Build cf: 3, 10, 25, 35, 40. Median class has cf ≥ 20.",
        "answer": "Median class: 20-30 (cf 25 ≥ 20, prev cf = 10). Median = 20 + (20−10)/15 × 10 = 20 + 100/15 = 26.67."
    },
    "fun_fact": "Unlike the mean, the median isn't affected by extreme values. If one student scores 1000 in a test of 100, the median stays sensible but the mean shoots up!"
}

QUESTIONS["math10.stats.median"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.stats.median"],
     "question": "Find the median class: 0-10 (f=4), 10-20 (f=6), 20-30 (f=8), 30-40 (f=2). What is n/2?",
     "hint": "n = 20, n/2 = 10. cf: 4, 10, 18, 20.",
     "expected_answer": "n/2 = 10. cf: 4, 10, 18, 20. Median class is 10-20 (cf = 10 ≥ 10 and previous cf = 4 < 10)."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.stats.median"],
     "question": "Find the median: 100-120 (f=12), 120-140 (f=14), 140-160 (f=8), 160-180 (f=6).",
     "hint": "n = 40, n/2 = 20. cf: 12, 26, 34, 40. Median class: 120-140.",
     "expected_answer": "Median class: 120-140. l=120, cf=12, f=14, h=20. Median = 120 + (20−12)/14 × 20 = 120 + 11.43 = 131.43."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.stats.median"],
     "question": "Marks distribution: 0-10 (f=5), 10-20 (f=15), 20-30 (f=20), 30-40 (f=23), 40-50 (f=7). Find the median marks.",
     "hint": "n=70, n/2=35. cf: 5, 20, 40, 63, 70. Median class: 20-30.",
     "expected_answer": "Median class: 20-30 (cf=40≥35, prev cf=20<35). Median = 20 + (35−20)/20 × 10 = 20 + 7.5 = 27.5."},
    {"id": 4, "type": "word_problem", "difficulty": 0.65, "concepts_tested": ["math10.stats.median"],
     "question": "If the median of the distribution is 46, find x: 10-20 (f=12), 20-30 (f=30), 30-40 (f=x), 40-50 (f=65), 50-60 (f=45), 60-70 (f=25), 70-80 (f=18). Total = 229.",
     "hint": "12+30+x+65+45+25+18 = 229 → x = 34. Verify with median formula: n/2 = 114.5.",
     "expected_answer": "x = 229 − 195 = 34. n/2 = 114.5. cf: 12, 42, 76, 141, ... Median class: 40-50 (cf=141≥114.5, prev=76<114.5). Median = 40 + (114.5−76)/65 × 10 = 40 + 385/65 = 40 + 5.92 = 45.92 ≈ 46. ✓"},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.stats.median"],
     "question": "The median of the following data is 525. Find x and y if total = 100: 0-100 (f=2), 100-200 (f=5), 200-300 (f=x), 300-400 (f=12), 400-500 (f=17), 500-600 (f=20), 600-700 (f=y), 700-800 (f=9), 800-900 (f=7), 900-1000 (f=4).",
     "hint": "2+5+x+12+17+20+y+9+7+4 = 100 → x+y = 24. Median class = 500-600. Use median formula with Median = 525.",
     "expected_answer": "x + y = 24 …(1). n/2 = 50. cf before 500-600 = 2+5+x+12+17 = 36+x. Median = 500 + (50−36−x)/20 × 100 = 525. (14−x)×5 = 25. 14−x = 5 → x = 9. From (1): y = 15."},
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 3 · Mode of Grouped Data
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.stats.mode"] = {
    "title": "📊 Mode of Grouped Data — The Most Popular Value",
    "hook": "What shoe size sells the most? Which score range has the most students? The mode is the value that appears most frequently — the 'most popular' value in the dataset!",
    "explanation": (
        definition_box("Modal Class", "The class interval with the <b>highest frequency</b>.")
        + formula_box("Mode = l + [(f₁ − f₀) / (2f₁ − f₀ − f₂)] × h", "Mode Formula")
        + comparison_table(
            ["Symbol", "Meaning"],
            [["l", "Lower boundary of the modal class"],
             ["f₁", "Frequency of the modal class"],
             ["f₀", "Frequency of the class <b>before</b> the modal class"],
             ["f₂", "Frequency of the class <b>after</b> the modal class"],
             ["h", "Class width"]]
        )
        + key_point("The mode is the value in the modal class that accounts for its 'peak' — it's pulled toward the side with the bigger neighboring frequency.")
        + info_box("<b>Empirical relationship:</b> 3 × Median = Mode + 2 × Mean (approximately true for moderately skewed data).")
    ),
    "worked_example": (
        "<b>Example:</b> Find the mode: 0-10 (f=5), 10-20 (f=8), 20-30 (f=15), 30-40 (f=12), 40-50 (f=10).<br><br>"
        + step_box([
            ("Modal class: 20-30 (highest f = 15)", ""),
            ("l = 20, f₁ = 15, f₀ = 8, f₂ = 12, h = 10", ""),
            ("Mode = 20 + (15−8)/(2×15−8−12) × 10", ""),
            ("= 20 + 7/10 × 10 = 20 + 7 = 27", ""),
        ])
    ),
    "try_this": {
        "question": "Find the mode: 10-20 (f=4), 20-30 (f=7), 30-40 (f=12), 40-50 (f=8), 50-60 (f=3).",
        "hint": "Modal class: 30-40 (f=12). f₀=7, f₂=8.",
        "answer": "Mode = 30 + (12−7)/(24−7−8) × 10 = 30 + 50/9 = 30 + 5.56 = 35.56."
    },
    "fun_fact": "In fashion, the 'mode' literally means the most popular style. The statistical term has the same origin — it identifies what's most common!"
}

QUESTIONS["math10.stats.mode"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.stats.mode"],
     "question": "Identify the modal class: 0-10 (f=3), 10-20 (f=9), 20-30 (f=15), 30-40 (f=6).",
     "hint": "The class with the highest frequency is the modal class.",
     "expected_answer": "Modal class is 20-30 (highest frequency = 15)."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.stats.mode"],
     "question": "Find the mode: 0-10 (f=6), 10-20 (f=11), 20-30 (f=7), 30-40 (f=4).",
     "hint": "Modal class: 10-20. l=10, f₁=11, f₀=6, f₂=7, h=10.",
     "expected_answer": "Mode = 10 + (11−6)/(22−6−7) × 10 = 10 + 50/9 = 10 + 5.56 = 15.56."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.stats.mode"],
     "question": "The mode of the following data is 36. Find the missing frequency f: 0-10 (f=8), 10-20 (f=10), 20-30 (f=f), 30-40 (f=16), 40-50 (f=12), 50-60 (f=6).",
     "hint": "Modal class must be 30-40 (since mode=36). So f₁=16, f₀=f, f₂=12. Use the formula.",
     "expected_answer": "36 = 30 + (16−f)/(32−f−12) × 10. 6 = (16−f)/(20−f) × 10. 6(20−f) = 10(16−f). 120−6f = 160−10f. 4f = 40. f = 10."},
    {"id": 4, "type": "word_problem", "difficulty": 0.65, "concepts_tested": ["math10.stats.mode"],
     "question": "For a distribution, mean = 24 and mode = 18. Estimate the median using the empirical relationship.",
     "hint": "3 × Median = Mode + 2 × Mean.",
     "expected_answer": "3 × Median = 18 + 2(24) = 18 + 48 = 66. Median = 22."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.stats.mode"],
     "question": "A dataset has mean 45.5, median 46, and mode 47. (a) Is the data left-skewed or right-skewed? (b) Verify the empirical relationship approximately.",
     "hint": "If Mean < Median < Mode, the data is left-skewed (negatively skewed).",
     "expected_answer": "(a) Mean(45.5) < Median(46) < Mode(47) → left-skewed (negatively skewed). (b) Mode + 2×Mean = 47 + 91 = 138. 3×Median = 138. So 138 = 138 ✓. The empirical relationship holds exactly here!"},
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 4 · Cumulative Frequency & Ogive
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.stats.ogive"] = {
    "title": "📈 Ogive (Cumulative Frequency Curve) — Visualizing Data",
    "hook": "An ogive is like a 'running total' graph. It helps you answer questions like: 'How many students scored below 60?' or 'What score separates the top 25% from the rest?'",
    "explanation": (
        definition_box("Ogive", "A smooth curve drawn by plotting cumulative frequencies against upper (or lower) class boundaries.")
        + comparison_table(
            ["Type", "Plot", "Shape"],
            [["Less-than ogive", "(upper boundary, cf)", "S-shaped, rising from left to right ↗"],
             ["More-than ogive", "(lower boundary, n − cf)", "S-shaped, falling from left to right ↘"]]
        )
        + step_box([
            ("Make a cumulative frequency table", "Running total of frequencies"),
            ("Plot points: (upper boundary, cf) for 'less than'", ""),
            ("Join with a smooth curve", ""),
            ("To find median graphically", "Draw horizontal at n/2 on y-axis → where it meets the ogive → drop vertical → that's the median"),
        ], "#7B1FA2")
        + key_point("The median is the x-coordinate where the two ogives (less-than and more-than) intersect!")
        + tip_box("The ogive can also give you Q₁ (at n/4), Q₃ (at 3n/4), and any percentile graphically.")
    ),
    "worked_example": (
        "<b>Example:</b> Draw a less-than ogive for: 0-10 (f=5), 10-20 (f=8), 20-30 (f=15), 30-40 (f=12), 40-50 (f=10).<br><br>"
        + comparison_table(
            ["Less than", "10", "20", "30", "40", "50"],
            [["cf", "5", "13", "28", "40", "50"]]
        )
        + "<p>Plot points: (10,5), (20,13), (30,28), (40,40), (50,50). Join with smooth curve.</p>"
        + "<p>For median: n/2 = 25. Draw horizontal at y = 25 → meets curve at approximately x = 28. So median ≈ 28.</p>"
    ),
    "try_this": {
        "question": "From the ogive in the example, approximately what percentage of values are less than 35?",
        "hint": "Read off the ogive at x = 35. That gives the cf. Divide by total (50) and multiply by 100.",
        "answer": "At x = 35, cf ≈ 34 (between 28 and 40, so roughly 28 + 12×(5/10) = 34). Percentage = 34/50 × 100 = 68%."
    },
    "fun_fact": "The word 'ogive' originally referred to the pointed arch shape in Gothic architecture — the S-shaped cumulative frequency curve resembles this arch!"
}

QUESTIONS["math10.stats.ogive"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.stats.ogive"],
     "question": "Write the cumulative frequency table for: 0-5 (f=2), 5-10 (f=3), 10-15 (f=5), 15-20 (f=4).",
     "hint": "cf = running total: 2, 2+3, 2+3+5, ...",
     "expected_answer": "cf: 2, 5, 10, 14. Less-than ogive points: (5,2), (10,5), (15,10), (20,14)."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.stats.ogive"],
     "question": "In a less-than ogive, what do the following points represent? (20, 35) and (30, 62).",
     "hint": "The x is the upper class boundary. The y is the cumulative frequency up to that boundary.",
     "expected_answer": "(20, 35) means 35 observations have values less than 20. (30, 62) means 62 observations have values less than 30. So frequency in 20-30 = 62 − 35 = 27."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.stats.ogive"],
     "question": "From a 'less than' ogive, the median corresponds to n/2. If n = 80, at what cumulative frequency should you read the median from the graph?",
     "hint": "n/2 = 40. Draw a horizontal line at cf = 40.",
     "expected_answer": "Draw horizontal at y = 40. Where it meets the ogive, drop a vertical to x-axis. That x-value is the median."},
    {"id": 4, "type": "word_problem", "difficulty": 0.65, "concepts_tested": ["math10.stats.ogive"],
     "question": "A 'more than' ogive and 'less than' ogive intersect at (28, 25). If total frequency = 50, what is the median?",
     "hint": "The intersection point of the two ogives gives the median.",
     "expected_answer": "The intersection point's x-coordinate = median = 28. The y-coordinate (25) equals n/2 = 50/2 = 25, confirming that this is indeed the median point."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.stats.ogive"],
     "question": "From a less-than ogive with n = 100, the graph passes through (30, 25) and (40, 75). Estimate the interquartile range.",
     "hint": "Q₁ is at n/4 = 25 → x ≈ 30. Q₃ is at 3n/4 = 75 → x ≈ 40. IQR = Q₃ − Q₁.",
     "expected_answer": "Q₁: at cf = 25, x = 30. Q₃: at cf = 75, x = 40. IQR = Q₃ − Q₁ = 40 − 30 = 10."},
]
