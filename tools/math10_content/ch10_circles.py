"""Chapter 10 — Circles: 2 concepts, 10 questions."""
from .helpers import formula_box, step_box, tip_box, comparison_table, definition_box, key_point, info_box, warning_box

LESSONS = {}
QUESTIONS = {}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1 · Tangent Properties
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.circles10.tangent_properties"] = {
    "title": "⭕ Tangent to a Circle — Just Touching",
    "hook": "A tangent line barely 'kisses' a circle at exactly one point. It's like a ball rolling on a flat surface — the floor is tangent to the ball at the point of contact. This one-point touch leads to powerful geometric properties!",
    "explanation": (
        definition_box("Tangent", "A line that touches a circle at exactly <b>one point</b>. That point is called the <b>point of contact</b> or point of tangency.")
        + '<svg width="220" height="220" style="display:block;margin:10px auto">'
          '<circle cx="110" cy="110" r="60" fill="#E3F2FD" stroke="#1565C0" stroke-width="2"/>'
          '<circle cx="110" cy="110" r="3" fill="#1565C0"/><text x="116" y="124" font-size="11" font-weight="bold">O</text>'
          '<line x1="110" y1="110" x2="170" y2="110" stroke="#1565C0" stroke-width="1.5" stroke-dasharray="4"/>'
          '<text x="135" y="105" font-size="10" fill="#1565C0">r</text>'
          '<circle cx="170" cy="110" r="3" fill="#E65100"/><text x="174" y="106" font-size="10" fill="#E65100">A</text>'
          '<line x1="170" y1="40" x2="170" y2="180" stroke="#E65100" stroke-width="2"/>'
          '<text x="176" y="78" font-size="10" fill="#E65100">Tangent</text>'
          '<rect x="164" y="110" width="6" height="6" fill="none" stroke="#1565C0" stroke-width="1"/>'
          '</svg>'
        + '<div style="text-align:center;font-size:0.8rem;color:#555;margin:-5px 0 10px">A tangent at any point is perpendicular to the radius at that point</div>'
        + key_point("<b>Theorem 1:</b> The tangent at any point of a circle is <b>perpendicular</b> to the radius through the point of contact.")
        + formula_box("If OA is radius and PA is tangent at A, then OA ⊥ PA (∠OAP = 90°)", "Key Property")
        + comparison_table(
            ["Term", "Definition", "# Points in common"],
            [["<b>Secant</b>", "Line intersecting circle at 2 points", "2"],
             ["<b>Tangent</b>", "Line touching circle at 1 point", "1"],
             ["<b>Non-intersecting</b>", "Line that misses the circle", "0"]]
        )
        + info_box("How many tangents can you draw from a point? <b>On the circle:</b> exactly 1. <b>Outside:</b> exactly 2. <b>Inside:</b> 0.")
    ),
    "worked_example": (
        "<b>Example:</b> A tangent PQ at point P of a circle of radius 5 cm meets a line through centre O at Q such that OQ = 13 cm. Find PQ.<br><br>"
        + step_box([
            ("OP ⊥ PQ (radius ⊥ tangent)", "Triangle OPQ is right-angled at P"),
            ("By Pythagoras", "OQ² = OP² + PQ²"),
            ("Substitute", "13² = 5² + PQ²"),
            ("Solve", "169 = 25 + PQ² → PQ² = 144 → PQ = 12 cm"),
        ])
    ),
    "try_this": {
        "question": "Two concentric circles have radii 5 cm and 3 cm. Find the length of a chord of the larger circle that is tangent to the smaller circle.",
        "hint": "The chord is tangent to the smaller circle, so the radius (3 cm) to the tangent point is perpendicular to the chord. This creates a right triangle.",
        "answer": "Let half-chord = x. By Pythagoras: 5² = 3² + x² → x² = 16 → x = 4 cm. Full chord = 2 × 4 = 8 cm."
    },
    "fun_fact": "The word 'tangent' comes from Latin 'tangere' meaning 'to touch.' A tangential conversation is one that barely 'touches' on the topic before going off in another direction!"
}

QUESTIONS["math10.circles10.tangent_properties"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.circles10.tangent_properties"],
     "question": "A tangent to a circle of radius 7 cm from an external point is 24 cm long. Find the distance of the point from the centre.",
     "hint": "Tangent ⊥ radius. Use Pythagoras: d² = 7² + 24².",
     "expected_answer": "d² = 49 + 576 = 625. d = 25 cm."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.circles10.tangent_properties"],
     "question": "If two tangents are drawn to a circle of radius 3 cm from a point 5 cm from the centre, find the tangent length and angle between the two tangents.",
     "hint": "Tangent length = √(d²−r²). For the angle: in right △OAP, sin(∠OPA) = r/d.",
     "expected_answer": "Tangent = √(25−9) = 4 cm. In right △OAP: ∠OAP=90°, OA=3, OP=5, PA=4. sin(∠OPA) = OA/OP = 3/5 → ∠OPA ≈ 36.87°. Angle between tangents = 2 × 36.87° ≈ 73.74°."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.circles10.tangent_properties"],
     "question": "PQ is a chord of length 16 cm of a circle with radius 10 cm. Find the distance of the midpoint of the chord from the centre.",
     "hint": "Perpendicular from centre bisects the chord. Half-chord = 8 cm. Use Pythagoras.",
     "expected_answer": "Half-chord = 8. d² + 8² = 10² → d² = 100 - 64 = 36 → d = 6 cm."},
    {"id": 4, "type": "word_problem", "difficulty": 0.65, "concepts_tested": ["math10.circles10.tangent_properties"],
     "question": "Prove that the tangent drawn at the mid-point of an arc of a circle is parallel to the chord joining the end points of the arc.",
     "hint": "Let M be the midpoint of arc AB. OM bisects the chord AB perpendicularly. The tangent at M is ⊥ to OM.",
     "expected_answer": "Let M be midpoint of arc AB, O the centre. OM ⊥ tangent at M (radius ⊥ tangent). Also, since M is midpoint of arc AB, OM is the perpendicular bisector of chord AB, so OM ⊥ AB. Since tangent at M ⊥ OM and AB ⊥ OM, the tangent at M ∥ AB. ∎"},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.circles10.tangent_properties"],
     "question": "A circle is inscribed in a triangle with sides 5 cm, 12 cm, and 13 cm. Find the radius of the inscribed circle.",
     "hint": "For a right triangle (check: 5²+12²=13²), the inradius = (a+b−c)/2 where c is the hypotenuse. Or use Area = r × s where s is the semi-perimeter.",
     "expected_answer": "5² + 12² = 25 + 144 = 169 = 13² → right triangle. Area = ½ × 5 × 12 = 30. Semi-perimeter s = (5+12+13)/2 = 15. Area = r × s → 30 = r × 15 → r = 2 cm."},
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2 · Tangent Theorems (Two Tangents from an External Point)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.circles10.tangent_theorems"] = {
    "title": "✌️ Two Tangents from an External Point — Equal Lengths!",
    "hook": "Hold a ball between your thumb and index finger. Both fingertips are tangent points, and here's the magic: the distances from your knuckle to each fingertip are exactly equal! This is the Two Tangent Theorem.",
    "explanation": (
        definition_box("Two Tangent Theorem", "The lengths of the two tangent segments drawn from an <b>external point</b> to a circle are <b>equal</b>.")
        + '<div style="text-align:center;margin:10px 0"><svg width="240" height="200">'
        + '<circle cx="120" cy="110" r="50" fill="#E8F5E9" stroke="#2E7D32" stroke-width="2"/>'
        + '<circle cx="120" cy="110" r="2" fill="#333"/>'
        + '<text x="125" y="108" font-size="11" font-weight="bold">O</text>'
        + '<line x1="30" y1="30" x2="79" y2="72" stroke="#E65100" stroke-width="2"/>'
        + '<line x1="30" y1="30" x2="88" y2="155" stroke="#E65100" stroke-width="2"/>'
        + '<text x="15" y="28" font-weight="bold" fill="#E65100">P</text>'
        + '<text x="68" y="66" font-size="11" font-weight="bold">A</text>'
        + '<text x="75" y="165" font-size="11" font-weight="bold">B</text>'
        + '<text x="30" y="80" font-size="11" fill="#E65100">PA = PB</text>'
        + '</svg></div>'
        + formula_box("PA = PB (tangent lengths from external point P)", "Two Tangent Theorem")
        + key_point("Also: OP bisects ∠APB and OP bisects AB at right angles.")
        + "<p><b>Tangent-Incircle Property:</b> If a circle is inscribed in a quadrilateral ABCD (touching all 4 sides), then:</p>"
        + formula_box("AB + CD = BC + DA", "Tangent Property for Circumscribed Quadrilateral")
    ),
    "worked_example": (
        "<b>Example:</b> From point P outside a circle, two tangents PA and PB are drawn. If PA = 8 cm and ∠APB = 60°, find the length of chord AB.<br><br>"
        + step_box([
            ("PA = PB = 8 (two tangent theorem)", "△PAB is isosceles"),
            ("∠APB = 60°", "Since PA = PB, the triangle is isosceles with apex 60° — it's equilateral!"),
            ("∠PAB = ∠PBA = (180°−60°)/2 = 60°", "All angles 60° confirms equilateral"),
            ("Therefore", "AB = PA = PB = 8 cm"),
        ])
    ),
    "try_this": {
        "question": "A circle is inscribed in a △ABC with AB = 8, BC = 7, CA = 5. If the tangent from A touches the circle at P on AB and Q on AC, find AP and AQ.",
        "hint": "Let AP = AQ = x (two tangents from A). Let BP = BR = y, CQ = CR = z. Then x+y = 8, y+z = 7, x+z = 5. Solve.",
        "answer": "x + y = 8, y + z = 7, z + x = 5. Add all: 2(x+y+z) = 20 → x+y+z = 10. From x+y = 8: z = 2. From y+z = 7: x = 3. From z+x = 5: y = 5. AP = AQ = x = 3 cm."
    },
    "fun_fact": "This equal-tangent property is why a soap bubble sitting on a flat surface forms a perfect hemisphere — the tangent line (the table) touches the spherical bubble at one point, and every point of contact is equidistant from the centre!"
}

QUESTIONS["math10.circles10.tangent_theorems"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.circles10.tangent_theorems"],
     "question": "From a point P, two tangents PA and PB are drawn to a circle with centre O. If ∠APB = 80°, find ∠AOB.",
     "hint": "∠OAP = ∠OBP = 90° (radius ⊥ tangent). In quadrilateral OAPB, sum of angles = 360°.",
     "expected_answer": "∠OAP + ∠OBP + ∠APB + ∠AOB = 360°. 90° + 90° + 80° + ∠AOB = 360°. ∠AOB = 100°."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.circles10.tangent_theorems"],
     "question": "Two tangents TP and TQ are drawn from external point T to a circle with centre O. If TP = 12 cm and OT = 13 cm, find the radius.",
     "hint": "OP ⊥ TP. OT² = OP² + TP². So OP² = 169 − 144.",
     "expected_answer": "r² = OT² − TP² = 169 − 144 = 25. r = 5 cm."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.circles10.tangent_theorems"],
     "question": "Prove that the tangents drawn at the ends of a diameter of a circle are parallel.",
     "hint": "Each tangent is ⊥ to the radius. The two radii form a diameter (straight line). So both tangents are ⊥ to the same line.",
     "expected_answer": "Let AB be a diameter. Tangent at A is ⊥ to OA. Tangent at B is ⊥ to OB. Since OA and OB are along the same line (diameter), both tangents are perpendicular to the same line → they are parallel. ∎"},
    {"id": 4, "type": "word_problem", "difficulty": 0.65, "concepts_tested": ["math10.circles10.tangent_theorems"],
     "question": "A quadrilateral ABCD is circumscribed about a circle. If AB = 6 cm, BC = 7 cm, CD = 4 cm, find DA.",
     "hint": "For a circumscribed quadrilateral: AB + CD = BC + DA.",
     "expected_answer": "AB + CD = BC + DA → 6 + 4 = 7 + DA → DA = 3 cm."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.circles10.tangent_theorems"],
     "question": "PA and PB are tangents from P to a circle with centre O and radius r. If OP = 2r, find ∠APB.",
     "hint": "In right △OAP: sin(∠OPA) = OA/OP = r/2r = 1/2.",
     "expected_answer": "sin(∠OPA) = r/(2r) = 1/2 → ∠OPA = 30°. Similarly ∠OPB = 30°. ∠APB = ∠OPA + ∠OPB = 60°."},
]
