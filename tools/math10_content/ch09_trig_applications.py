"""Chapter 9 — Some Applications of Trigonometry: 2 concepts, 10 questions."""
from .helpers import formula_box, step_box, tip_box, comparison_table, definition_box, key_point, info_box, warning_box

LESSONS = {}
QUESTIONS = {}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1 · Angle of Elevation and Depression
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.trig_app.elevation_depression"] = {
    "title": "🏔️ Angles of Elevation & Depression — Looking Up and Down",
    "hook": "You're standing on a cliff, looking down at a boat in the sea. The angle your line of sight makes with the horizontal is called the 'angle of depression.' It's the same concept used by pilots for landing and surveyors for mapping!",
    "explanation": (
        definition_box("Angle of Elevation", "The angle between the horizontal and the line of sight when looking <b>UP</b> at an object.")
        + definition_box("Angle of Depression", "The angle between the horizontal and the line of sight when looking <b>DOWN</b> at an object.")
        + '<div style="text-align:center;margin:15px 0"><svg width="300" height="200">'
        + '<line x1="20" y1="160" x2="280" y2="160" stroke="#999" stroke-width="1" stroke-dasharray="4"/>'  # ground
        + '<line x1="20" y1="160" x2="20" y2="40" stroke="#333" stroke-width="2"/>'  # observer
        + '<circle cx="20" cy="35" r="8" fill="#FFC107"/>'  # head
        + '<line x1="20" y1="40" x2="260" y2="40" stroke="#666" stroke-width="1" stroke-dasharray="4"/>'  # horizontal from observer
        + '<line x1="20" y1="40" x2="260" y2="160" stroke="#E65100" stroke-width="2"/>'  # line of sight down
        + '<text x="80" y="55" font-size="11" fill="#E65100">angle of depression</text>'
        + '<rect x="240" y="140" width="40" height="20" fill="#1565C0"/>'  # boat
        + '<path d="M 30,45 A 40,40 0 0,1 60,60" fill="none" stroke="#E65100" stroke-width="1.5"/>'  # arc
        + '<line x1="240" y1="160" x2="20" y2="40" stroke="#2E7D32" stroke-width="1" stroke-dasharray="3"/>'
        + '<text x="120" y="175" font-size="11" fill="#2E7D32">angle of elevation (same!)</text>'
        + '</svg></div>'
        + key_point("The angle of depression from A to B <b>equals</b> the angle of elevation from B to A (alternate interior angles with horizontal lines).")
        + step_box([
            ("Step 1: Draw the figure", "Mark the observer, object, horizontal, and right angle"),
            ("Step 2: Identify the triangle", "Usually a right triangle"),
            ("Step 3: Choose the right ratio", "tan is most common (you usually know opposite and adjacent)"),
            ("Step 4: Solve", "Use standard angle values"),
        ], "#1565C0")
    ),
    "worked_example": (
        "<b>Example:</b> From the top of a 20 m tower, the angle of depression to a car is 30°. How far is the car from the base?<br><br>"
        + step_box([
            ("Draw figure", "Tower = 20 m (vertical). Angle of depression = 30°. Need: horizontal distance."),
            ("Angle of elevation from car = 30°", "(alternate angles)"),
            ("Use tan", "tan 30° = opposite/adjacent = 20/d"),
            ("Solve", "1/√3 = 20/d → d = 20√3 ≈ 34.64 m"),
        ])
    ),
    "try_this": {
        "question": "A kite's string is 100 m long and makes an angle of 60° with the ground. Find the height of the kite (assume string is straight).",
        "hint": "sin 60° = height / 100.",
        "answer": "sin 60° = h/100. √3/2 = h/100. h = 50√3 ≈ 86.6 m."
    },
    "fun_fact": "Ancient Egyptians used angles of elevation to align the pyramids with the North Star — a form of practical trigonometry over 4000 years ago!"
}

QUESTIONS["math10.trig_app.elevation_depression"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.trig_app.elevation_depression"],
     "question": "The angle of elevation of the top of a tower from a point 50 m away is 45°. Find the height of the tower.",
     "hint": "tan 45° = height/50.",
     "expected_answer": "tan 45° = h/50 → 1 = h/50 → h = 50 m."},
    {"id": 2, "type": "word_problem", "difficulty": 0.4, "concepts_tested": ["math10.trig_app.elevation_depression"],
     "question": "A tree breaks due to storm and the broken part bends so that the top touches the ground at 30° angle, 30 m from the base. Find the original height.",
     "hint": "Let broken part = hypotenuse. Standing part = vertical side. tan 30° = standing/30. cos 30° = 30/broken.",
     "expected_answer": "Let standing part = h, broken part = l. tan 30° = h/30 → h = 30/√3 = 10√3. cos 30° = 30/l → l = 30/(√3/2) = 60/√3 = 20√3. Total height = 10√3 + 20√3 = 30√3 ≈ 51.96 m."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.trig_app.elevation_depression"],
     "question": "From the top of a 7 m building, the angle of elevation of the top of a tower is 60° and the angle of depression of its foot is 45°. Find the height of the tower.",
     "hint": "Draw: building height = 7m. Let tower = h. The horizontal distance d: tan 45° = 7/d. Then tan 60° = (h-7)/d.",
     "expected_answer": "tan 45° = 7/d → d = 7. tan 60° = (h−7)/7 → √3 = (h−7)/7 → h−7 = 7√3 → h = 7 + 7√3 = 7(1+√3) ≈ 19.12 m."},
    {"id": 4, "type": "word_problem", "difficulty": 0.65, "concepts_tested": ["math10.trig_app.elevation_depression"],
     "question": "Two poles of height 6 m and 11 m stand on a plane ground. The distance between their feet is 12 m. Find the distance between their tops.",
     "hint": "The horizontal distance = 12. The vertical difference = 11 - 6 = 5. Use Pythagoras.",
     "expected_answer": "Vertical difference = 11 − 6 = 5 m. Distance = √(12² + 5²) = √(144+25) = √169 = 13 m."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.trig_app.elevation_depression"],
     "question": "From a point on the ground, the angles of elevation of the bottom and top of a transmission tower on a building are 45° and 60° respectively. Find the height of the tower if the building is 20 m high.",
     "hint": "Let d = horizontal distance. tan 45° = 20/d for the building. tan 60° = (20+h)/d for building+tower.",
     "expected_answer": "tan 45° = 20/d → d = 20. tan 60° = (20+h)/20 → √3 = (20+h)/20 → 20+h = 20√3 → h = 20√3 − 20 = 20(√3−1) ≈ 14.64 m."},
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2 · Heights and Distances (Advanced Problems)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.trig_app.heights_distances"] = {
    "title": "🏗️ Heights and Distances — Multi-Step Problems",
    "hook": "A pilot needs to calculate the landing distance. A surveyor measures a mountain's height from two different spots. These real-world problems use TWO right triangles and the magic of trigonometry!",
    "explanation": (
        "<p><b>Two-triangle problems:</b> These are the most common advanced questions. You get two angle measurements from different positions.</p>"
        + '<div style="text-align:center;margin:10px 0"><svg width="340" height="180">'
        + '<line x1="270" y1="160" x2="270" y2="30" stroke="#333" stroke-width="2"/>'  # tower
        + '<line x1="20" y1="160" x2="320" y2="160" stroke="#999" stroke-width="1"/>'  # ground
        + '<line x1="30" y1="160" x2="270" y2="30" stroke="#E65100" stroke-width="1.5"/>'  # sight line 1
        + '<line x1="160" y1="160" x2="270" y2="30" stroke="#1565C0" stroke-width="1.5"/>'  # sight line 2
        + '<text x="273" y="95" font-size="11" font-weight="bold">h</text>'
        + '<text x="30" y="175" font-size="11" font-weight="bold" fill="#E65100">A</text>'
        + '<text x="158" y="175" font-size="11" font-weight="bold" fill="#1565C0">B</text>'
        + '<text x="270" y="175" font-size="11" font-weight="bold">C</text>'
        + '<text x="85" y="175" font-size="10" fill="#E65100">←d→</text>'
        + '<text x="60" y="150" font-size="10" fill="#E65100">α</text>'
        + '<text x="185" y="150" font-size="10" fill="#1565C0">β</text>'
        + '</svg></div>'
        + step_box([
            ("From A", "tan α = h / (d + BC)  … where BC = distance from B to tower base"),
            ("From B", "tan β = h / BC"),
            ("Two equations, two unknowns", "Solve simultaneously for h"),
        ], "#7B1FA2")
        + tip_box("The key trick: express the horizontal distance in terms of h using one equation, then substitute into the other.")
        + warning_box("Always check if the observer is on the same side or opposite sides of the tower — the equations differ!")
    ),
    "worked_example": (
        "<b>Example:</b> The angles of elevation of the top of a tower from two points at distances a and b from the base, in the same straight line, are complementary (sum to 90°). Prove: height = √(ab).<br><br>"
        + step_box([
            ("Let angles be θ and (90°−θ)", "Tower height = h"),
            ("From distance a", "tan θ = h/a → h = a·tan θ  …(1)"),
            ("From distance b", "tan(90°−θ) = h/b → cot θ = h/b → h = b·cot θ  …(2)"),
            ("Multiply (1) and (2)", "h² = ab·tan θ·cot θ = ab·1 = ab"),
            ("Therefore", "h = √(ab) ∎"),
        ])
    ),
    "try_this": {
        "question": "The angle of elevation of a cloud from a point 60 m above a lake is 30° and the angle of depression of its reflection in the lake is 60°. Find the height of the cloud above the lake.",
        "hint": "Let cloud be h above lake. Observer is 60 m above lake. Cloud reflection is h below lake surface. Use tan 30° and tan 60° with the same horizontal distance.",
        "answer": "Let cloud height above lake = H. Observer is 60 m above lake. tan 30° = (H−60)/d → d = (H−60)√3. tan 60° = (H+60)/d → d = (H+60)/√3. So (H−60)√3 = (H+60)/√3. 3(H−60) = H+60. 3H−180 = H+60. 2H = 240. H = 120 m."
    },
    "fun_fact": "The Great Trigonometrical Survey of India (1802-1871) used these exact techniques to measure the height of Mount Everest — getting within 8 meters of the modern measurement using only theodolites and trigonometry!"
}

QUESTIONS["math10.trig_app.heights_distances"] = [
    {"id": 1, "type": "word_problem", "difficulty": 0.4, "concepts_tested": ["math10.trig_app.heights_distances"],
     "question": "A person standing on top of a cliff 80 m high observes a boat at an angle of depression of 30°. Find the distance of the boat from the base of the cliff.",
     "hint": "Angle of depression = 30° = angle of elevation from boat. tan 30° = 80/d.",
     "expected_answer": "tan 30° = 80/d → 1/√3 = 80/d → d = 80√3 ≈ 138.56 m."},
    {"id": 2, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.trig_app.heights_distances"],
     "question": "The shadow of a tower standing on level ground is found to be 40 m longer when the Sun's altitude is 30° than when it is 60°. Find the height of the tower.",
     "hint": "Let h = height. When 60°: shadow = h/tan 60° = h/√3. When 30°: shadow = h/tan 30° = h√3. Difference = 40.",
     "expected_answer": "h√3 − h/√3 = 40 → h(√3 − 1/√3) = 40 → h(3−1)/√3 = 40 → 2h/√3 = 40 → h = 20√3 ≈ 34.64 m."},
    {"id": 3, "type": "word_problem", "difficulty": 0.6, "concepts_tested": ["math10.trig_app.heights_distances"],
     "question": "From the top of a lighthouse 100 m high, two ships are observed on opposite sides. The angles of depression are 30° and 45°. Find the distance between the ships.",
     "hint": "Ship 1: tan 30° = 100/d₁. Ship 2: tan 45° = 100/d₂. Distance = d₁ + d₂.",
     "expected_answer": "d₁ = 100/tan 30° = 100√3. d₂ = 100/tan 45° = 100. Distance = 100√3 + 100 = 100(√3+1) ≈ 273.2 m."},
    {"id": 4, "type": "word_problem", "difficulty": 0.7, "concepts_tested": ["math10.trig_app.heights_distances"],
     "question": "A straight highway leads to the foot of a tower. From a point on the highway, the angle of elevation is 60°. After walking 100 m further towards the tower, it becomes 30°. Wait — that's wrong! The angle should increase. So: initially 30°, after walking 100 m closer it becomes 60°. Find the height of the tower.",
     "hint": "Let h = height, d = remaining distance. tan 60° = h/d and tan 30° = h/(d+100).",
     "expected_answer": "tan 60° = h/d → h = d√3 …(1). tan 30° = h/(d+100) → h = (d+100)/√3 …(2). From (1)&(2): d√3 = (d+100)/√3 → 3d = d+100 → 2d = 100 → d = 50. h = 50√3 ≈ 86.6 m."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.85, "concepts_tested": ["math10.trig_app.heights_distances"],
     "question": "From the top of a building 60 m high, the angles of depression of the top and bottom of a tower are 30° and 60° respectively. Find the height of the tower and the distance between them.",
     "hint": "Let tower height = h, distance between = d. tan 60° = 60/d (bottom). tan 30° = (60−h)/d (top of tower).",
     "expected_answer": "tan 60° = 60/d → d = 60/√3 = 20√3 m. tan 30° = (60−h)/d → 1/√3 = (60−h)/(20√3) → 20√3/√3 = 60−h → 20 = 60−h → h = 40 m. Tower height = 40 m, distance = 20√3 ≈ 34.64 m."},
]
