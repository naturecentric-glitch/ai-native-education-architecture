"""Chapter 11 — Constructions: 3 concepts, 15 questions."""
from .helpers import formula_box, step_box, tip_box, comparison_table, definition_box, key_point, info_box, warning_box

LESSONS = {}
QUESTIONS = {}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1 · Division of a Line Segment
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.constructions10.divide_segment"] = {
    "title": "✏️ Dividing a Line Segment in a Given Ratio",
    "hook": "You have a line segment AB and you need to find the point that divides it in ratio 3:2 — but you can only use a compass and straightedge! This classical construction has been used since Euclid's time.",
    "explanation": (
        definition_box("Problem", "Divide a given line segment AB in a given ratio m:n using only compass and straightedge.")
        + "<p><b>Construction Steps (to divide AB in ratio m:n):</b></p>"
        + step_box([
            ("Draw ray AX at any acute angle to AB", "AX should not overlap AB"),
            ("Mark (m+n) equal arcs on AX", f"Using compass, mark points A₁, A₂, ..., A_(m+n) on AX"),
            ("Join the last point to B", "Join A_(m+n) to B"),
            ("Through A_m, draw line parallel to A_(m+n)B", "This line meets AB at point P"),
            ("P divides AB in ratio m:n", "AP:PB = m:n"),
        ], "#1565C0")
        + key_point("<b>Why it works:</b> By BPT (Basic Proportionality Theorem), a line parallel to one side of a triangle divides the other two sides proportionally.")
        + tip_box("Alternative: You can also use the section formula to verify: if A=(0,0) and B=(a,0), then P = (ma/(m+n), 0).")
    ),
    "worked_example": (
        "<b>Example:</b> Divide a line segment of 7 cm in ratio 2:3.<br><br>"
        + step_box([
            ("Draw AB = 7 cm", ""),
            ("Draw ray AX at acute angle to AB", "Any angle works, ~30° is convenient"),
            ("Mark 5 (=2+3) equal arcs on AX", "A₁, A₂, A₃, A₄, A₅"),
            ("Join A₅ to B", ""),
            ("Through A₂, draw A₂P ∥ A₅B", "P is on AB"),
            ("Result: AP = 2.8 cm, PB = 4.2 cm", "AP/PB = 2.8/4.2 = 2/3 ✓"),
        ])
    ),
    "try_this": {
        "question": "Describe the steps to divide a 10 cm segment in ratio 3:7. What will be the lengths of the two parts?",
        "hint": "Total ratio parts = 3+7 = 10. Mark 10 equal arcs.",
        "answer": "Mark 10 arcs on AX. Join A₁₀ to B. Draw A₃P ∥ A₁₀B. AP = 10×3/10 = 3 cm. PB = 10×7/10 = 7 cm."
    },
    "fun_fact": "The ancient Greeks could divide segments in any rational ratio, but they struggled with irrational ratios. Dividing a segment in ratio √2 : 1 requires a slightly different technique!"
}

QUESTIONS["math10.constructions10.divide_segment"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.constructions10.divide_segment"],
     "question": "To divide a line segment AB in ratio 4:5, how many equal arcs should you mark on the ray AX?",
     "hint": "Total parts = m + n.",
     "expected_answer": "4 + 5 = 9 equal arcs."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.constructions10.divide_segment"],
     "question": "A line segment of 9 cm is divided in ratio 1:2. What are the lengths of the two parts? Describe the construction steps.",
     "hint": "Total parts = 3. Shorter part = 9×1/3 = 3 cm.",
     "expected_answer": "Parts: 3 cm and 6 cm. Steps: Draw AB = 9 cm. Draw ray AX. Mark 3 equal arcs A₁A₂A₃. Join A₃B. Draw A₁P ∥ A₃B meeting AB at P. AP = 3 cm, PB = 6 cm."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.constructions10.divide_segment"],
     "question": "In dividing AB in ratio 3:4, you draw A₃P parallel to A₇B. Which theorem justifies that AP/PB = 3/4?",
     "hint": "Think of △AA₇B. The line A₃P is parallel to A₇B.",
     "expected_answer": "By BPT (Basic Proportionality Theorem / Thales' Theorem): If A₃P ∥ A₇B in △AA₇B, then AA₃/A₃A₇ = AP/PB = 3/4."},
    {"id": 4, "type": "word_problem", "difficulty": 0.65, "concepts_tested": ["math10.constructions10.divide_segment"],
     "question": "Point P divides segment AB of length 12 cm such that AP/AB = 3/4. What is the ratio AP:PB? What length is AP?",
     "hint": "AP/AB = 3/4 means AP = 3k and AB = 4k for some k. PB = AB − AP.",
     "expected_answer": "AP/AB = 3/4. So AP = 12×3/4 = 9 cm. PB = 12−9 = 3 cm. AP:PB = 9:3 = 3:1."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.constructions10.divide_segment"],
     "question": "Describe how you would divide a segment AB in ratio √3 : 1 (approximately 1.732 : 1). You may use constructions involving equilateral triangles.",
     "hint": "Construct an equilateral triangle on AB. The altitude = (√3/2)AB. Use this length.",
     "expected_answer": "One method: (1) On AB, construct equilateral △ABQ externally. The altitude from Q to AB has length h = (√3/2)AB. (2) On ray AX, mark A₁ such that AA₁ = h and A₂ such that A₁A₂ = AB/2 (half of AB). Then AA₁/A₁A₂ = h/(AB/2) = √3. (3) Now join A₂B and draw A₁P ∥ A₂B. Then AP/PB = √3/1. Length AP = AB×√3/(√3+1) = AB×√3(√3−1)/2."},
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2 · Construction of Similar Triangles
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.constructions10.similar_triangle"] = {
    "title": "📐 Constructing Similar Triangles — Scaling Up or Down",
    "hook": "Want to build an exact scale model of a triangle — say 3/4 the size? Or enlarge it to 5/3 the size? These constructions show you how to create a triangle similar to a given one with any scale factor.",
    "explanation": (
        definition_box("Scale Factor", "The ratio of sides of the new triangle to the corresponding sides of the original. Scale factor < 1 means smaller. Scale factor > 1 means larger.")
        + "<p><b>Construction (scale factor m/n):</b></p>"
        + step_box([
            ("Draw the given triangle ABC", ""),
            ("Draw ray BX at acute angle to BC (on side opposite A)", ""),
            ("Mark max(m,n) arcs on BX", "Points B₁, B₂, ..., B_max(m,n)"),
            ("Join Bₙ to C", "n-th point to vertex C"),
            ("Through Bₘ, draw Bₘ C' ∥ BₙC", "C' is on BC (or extension)"),
            ("Through C', draw C'A' ∥ CA", "A' is on BA (or extension)"),
            ("△A'BC' is similar to △ABC with scale m/n", "A'B/AB = BC'/BC = m/n"),
        ], "#7B1FA2")
        + comparison_table(
            ["Scale factor", "Triangle size", "Where C' falls"],
            [["m/n < 1 (e.g., 2/3)", "Smaller", "Between B and C"],
             ["m/n > 1 (e.g., 5/3)", "Larger", "Beyond C on ray BC"]]
        )
    ),
    "worked_example": (
        "<b>Example:</b> Construct a triangle similar to △ABC (BC = 6 cm, AB = 5 cm, ∠B = 60°) with scale factor 3/4.<br><br>"
        + step_box([
            ("Draw △ABC: BC=6, AB=5, ∠B=60°", ""),
            ("Draw ray BX below BC at acute angle", ""),
            ("Mark 4 arcs (max(3,4)=4) on BX", "B₁B₂B₃B₄"),
            ("Join B₄ to C", ""),
            ("Draw B₃C' ∥ B₄C (C' on BC)", "BC' = 6×3/4 = 4.5 cm"),
            ("Draw C'A' ∥ CA (A' on BA)", "BA' = 5×3/4 = 3.75 cm"),
            ("△A'BC' ~ △ABC, scale 3/4", ""),
        ])
    ),
    "try_this": {
        "question": "To construct a triangle similar to △PQR with scale factor 5/3, how many arcs do you mark? Where does the new vertex Q' fall — between P and Q, or beyond Q?",
        "hint": "max(5,3) = 5 arcs. Scale > 1 means larger triangle.",
        "answer": "Mark 5 arcs. Since scale 5/3 > 1, the new triangle is LARGER, so Q' falls beyond Q (on the extension of PQ)."
    },
    "fun_fact": "Architects have been using similar triangle constructions to create scale blueprints for thousands of years — the principle behind every building plan!"
}

QUESTIONS["math10.constructions10.similar_triangle"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.constructions10.similar_triangle"],
     "question": "To construct a triangle similar to a given triangle with scale factor 3/5, the minimum number of arcs to mark is:",
     "hint": "You need max(m, n) = max(3, 5).",
     "expected_answer": "max(3, 5) = 5 arcs."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.constructions10.similar_triangle"],
     "question": "△ABC has sides AB = 8, BC = 6, AC = 10. A similar triangle with scale factor 3/4 is constructed. What are the sides of the new triangle?",
     "hint": "Multiply each side by 3/4.",
     "expected_answer": "A'B' = 8×3/4 = 6, B'C' = 6×3/4 = 4.5, A'C' = 10×3/4 = 7.5."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.constructions10.similar_triangle"],
     "question": "Describe the steps to construct a triangle with sides 3/5 times the corresponding sides of △PQR (PQ = 5, QR = 6, PR = 7).",
     "hint": "Scale factor = 3/5. Draw △PQR first, then scale it.",
     "expected_answer": "1) Draw △PQR with given sides. 2) From Q, draw ray QX at acute angle to QR (opposite side of P). 3) Mark 5 arcs on QX. 4) Join Q₅ to R. 5) Draw Q₃R' ∥ Q₅R → R' is on QR with QR' = 6×3/5 = 3.6. 6) Draw R'P' ∥ RP → P' on QP with QP' = 5×3/5 = 3. New triangle P'QR' has sides 3, 3.6, 4.2."},
    {"id": 4, "type": "word_problem", "difficulty": 0.65, "concepts_tested": ["math10.constructions10.similar_triangle"],
     "question": "In the construction of a similar triangle with scale factor 7/4, you need to extend a side. Why? Where does the new vertex lie?",
     "hint": "7/4 > 1, so the new triangle is larger than the original.",
     "expected_answer": "Since 7/4 > 1, the new triangle is larger. The new vertex C' lies on the extension of BC beyond C (not between B and C). We join B₄ to C, then draw B₇C' ∥ B₄C, and C' falls beyond C. Similarly, A' lies on the extension of BA beyond A."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.constructions10.similar_triangle"],
     "question": "Construct two similar triangles with the same base BC = 6 cm, one with scale factor 3/5 and another with 7/5 relative to a given △ABC (AB = 5, AC = 7, BC = 6). What are the areas of the two new triangles if the area of △ABC is 14.7 cm²?",
     "hint": "Area ratio = (scale factor)².",
     "expected_answer": "Scale 3/5: Area = 14.7 × (3/5)² = 14.7 × 9/25 = 5.292 cm². Scale 7/5: Area = 14.7 × (7/5)² = 14.7 × 49/25 = 28.812 cm²."},
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 3 · Construction of Tangent to a Circle
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.constructions10.tangent_to_circle"] = {
    "title": "⭕ Constructing Tangents to a Circle",
    "hook": "Given a circle and a point outside it, can you draw the lines that 'just touch' the circle? This classical construction uses a beautiful property: the angle in a semicircle is 90°!",
    "explanation": (
        "<p><b>Two types of tangent constructions:</b></p>"
        + comparison_table(
            ["Situation", "Method", "# Tangents"],
            [["Point ON the circle", "Draw radius, then perpendicular", "1"],
             ["Point OUTSIDE the circle", "Use semicircle construction", "2"]]
        )
        + "<p><b>Construction: Tangent from an external point P to circle with centre O, radius r:</b></p>"
        + step_box([
            ("Join OP", ""),
            ("Find midpoint M of OP", "Use perpendicular bisector"),
            ("Draw circle with centre M, radius MO = MP", "This circle passes through both O and P"),
            ("Let this circle intersect the given circle at A and B", ""),
            ("PA and PB are the required tangents!", ""),
        ], "#2E7D32")
        + key_point("<b>Why?</b> ∠OAP = 90° (angle in semicircle of the new circle). Since OA is radius and ∠OAP = 90°, PA must be tangent to the original circle!")
        + tip_box("For a tangent at a point ON the circle: just draw the radius to that point, then construct a perpendicular to the radius at that point.")
    ),
    "worked_example": (
        "<b>Example:</b> Draw a circle of radius 3 cm. From point P at 7 cm from centre, construct tangents. Find the tangent length.<br><br>"
        + step_box([
            ("Draw circle, centre O, r = 3 cm. Mark P at 7 cm from O", ""),
            ("Find midpoint M of OP (at 3.5 cm from each)", ""),
            ("Draw circle with centre M, radius 3.5 cm", ""),
            ("Mark intersection points A, B with original circle", ""),
            ("Join PA, PB — these are tangents", ""),
            ("Tangent length = √(OP² − r²) = √(49−9) = √40 = 2√10 ≈ 6.32 cm", ""),
        ])
    ),
    "try_this": {
        "question": "Draw a circle of radius 4 cm. Mark a point P at 10 cm from centre. If you construct tangents PA and PB, what is the length PA? What angle does OP make with PA?",
        "hint": "PA = √(OP²−r²). ∠OAP = 90°. Find ∠OPA using trigonometry.",
        "answer": "PA = √(100−16) = √84 = 2√21 ≈ 9.17 cm. sin(∠OPA) = OA/OP = 4/10 = 2/5. ∠OPA = arcsin(0.4) ≈ 23.6°."
    },
    "fun_fact": "This construction is over 2300 years old — Euclid described it in Book III of his Elements!"
}

QUESTIONS["math10.constructions10.tangent_to_circle"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.constructions10.tangent_to_circle"],
     "question": "To construct a tangent at point A on a circle with centre O, what is the first step?",
     "hint": "The tangent is perpendicular to the radius at the point of contact.",
     "expected_answer": "Join OA (draw the radius to point A). Then construct a line perpendicular to OA at point A. This perpendicular is the tangent."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.constructions10.tangent_to_circle"],
     "question": "In the tangent construction from external point P, why do we draw a circle with diameter OP?",
     "hint": "Think about the angle in a semicircle.",
     "expected_answer": "Any angle inscribed in a semicircle is 90°. If A is the intersection of this new circle with the original circle, then ∠OAP = 90° (angle in semicircle of OP). Since OA is radius and ∠OAP = 90°, PA ⊥ OA, making PA a tangent."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.constructions10.tangent_to_circle"],
     "question": "A circle has radius 5 cm. From a point 13 cm from the centre, tangents are drawn. Find: (a) tangent length, (b) angle between the two tangents.",
     "hint": "Tangent length = √(13²−5²). For the angle: sin(half-angle) = 5/13.",
     "expected_answer": "(a) Tangent = √(169−25) = √144 = 12 cm. (b) sin(∠OPA) = 5/13 → ∠OPA = arcsin(5/13) ≈ 22.6°. Angle between tangents = 2 × 22.6° ≈ 45.2°. (More precisely: 2 arcsin(5/13).)"},
    {"id": 4, "type": "word_problem", "difficulty": 0.65, "concepts_tested": ["math10.constructions10.tangent_to_circle"],
     "question": "Describe how to construct a tangent to a circle of radius 4 cm from a point P at distance 6 cm from the centre. Can you draw more than 2 tangents from P?",
     "hint": "Follow the standard steps. From any external point, exactly 2 tangents exist.",
     "expected_answer": "Steps: Draw circle (r=4). Mark P at 6 cm from O. Find midpoint M of OP. Draw circle with centre M, radius 3 cm (=OP/2). This intersects original circle at A and B. Join PA, PB. Tangent length = √(36−16) = √20 = 2√5 cm. No, exactly 2 tangents can be drawn from any external point."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.constructions10.tangent_to_circle"],
     "question": "Two circles with centres O₁ and O₂ have radii 3 cm and 5 cm. The distance O₁O₂ = 10 cm. Describe how to construct a common external tangent.",
     "hint": "Draw a circle with centre O₂ and radius (5−3)=2 cm. From O₁, draw a tangent to this auxiliary circle. Then shift this tangent outward by 3 cm.",
     "expected_answer": "Method: (1) Draw auxiliary circle with centre O₂ radius |r₂−r₁| = 2 cm. (2) From O₁, construct tangent to this auxiliary circle (tangent length = √(10²−2²) = √96 = 4√6). (3) Let this tangent touch the auxiliary circle at T. (4) Draw O₂T and extend to meet the larger circle at Q. (5) Draw O₁P parallel to O₂Q with P on smaller circle. (6) PQ is the common external tangent. (Two such tangents exist, on opposite sides.)"},
]
