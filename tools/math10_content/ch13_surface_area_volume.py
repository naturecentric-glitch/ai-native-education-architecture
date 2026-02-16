"""Chapter 13 — Surface Areas and Volumes: 3 concepts, 15 questions."""
from .helpers import formula_box, step_box, tip_box, comparison_table, definition_box, key_point, info_box, warning_box

LESSONS = {}
QUESTIONS = {}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1 · Conversion of Solids
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.sa_vol.conversion"] = {
    "title": "🔄 Converting One Solid to Another — Volume Stays Constant!",
    "hook": "A metallic sphere is melted and recast into a cylinder. A cone-shaped clay model is reshaped into a sphere. In both cases, the VOLUME doesn't change — only the shape! This is the key insight.",
    "explanation": (
        key_point("<b>Fundamental Rule:</b> When a solid is melted/reshaped into another solid, the <b>volume remains the same</b>.")
        + "<p><b>Volume formulas you need:</b></p>"
        + comparison_table(
            ["Solid", "Volume", "Surface Area"],
            [["Cube (side a)", "a³", "6a²"],
             ["Cuboid (l×b×h)", "lbh", "2(lb + bh + hl)"],
             ["Cylinder (r, h)", "πr²h", "2πr(r + h)"],
             ["Cone (r, h, l)", "⅓πr²h", "πr(r + l)"],
             ["Sphere (r)", "⁴⁄₃πr³", "4πr²"],
             ["Hemisphere (r)", "⅔πr³", "3πr²"]]
        )
        + step_box([
            ("Write volume of original solid", ""),
            ("Write volume of new solid (in terms of unknowns)", ""),
            ("Set them equal", "Volume₁ = Volume₂"),
            ("Solve for the unknown dimension", ""),
        ], "#1565C0")
        + tip_box("If the original is split into many smaller solids: Volume of original = n × Volume of each small solid.")
    ),
    "worked_example": (
        "<b>Example:</b> A metallic sphere of radius 6 cm is melted and recast into a cylinder of radius 4 cm. Find the height.<br><br>"
        + step_box([
            ("Volume of sphere", "V = (4/3)π(6)³ = (4/3)π(216) = 288π cm³"),
            ("Volume of cylinder", "V = π(4)²h = 16πh cm³"),
            ("Set equal", "16πh = 288π → h = 18 cm"),
        ])
    ),
    "try_this": {
        "question": "A cone of radius 3 cm and height 8 cm is melted into a sphere. Find the radius of the sphere.",
        "hint": "Volume of cone = ⅓πr²h. Volume of sphere = ⁴⁄₃πR³. Set equal and solve.",
        "answer": "(1/3)π(9)(8) = (4/3)πR³. 24π = (4/3)πR³. R³ = 18. R = ∛18 ≈ 2.62 cm."
    },
    "fun_fact": "Archimedes discovered that a sphere fits perfectly inside a cylinder of the same height and diameter — and the sphere's volume is exactly 2/3 of the cylinder's!"
}

QUESTIONS["math10.sa_vol.conversion"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.sa_vol.conversion"],
     "question": "A solid sphere of radius 3 cm is melted and recast into small spheres of radius 1 cm each. How many small spheres are formed?",
     "hint": "n × Volume of small = Volume of big. n × (4/3)π(1)³ = (4/3)π(3)³.",
     "expected_answer": "n = (3)³/(1)³ = 27 small spheres."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.sa_vol.conversion"],
     "question": "A cylinder of radius 7 cm and height 10 cm is melted into a cone of radius 7 cm. Find the height of the cone.",
     "hint": "πr²h = ⅓πr²H → H = 3h.",
     "expected_answer": "π(49)(10) = (1/3)π(49)H → H = 30 cm."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.sa_vol.conversion"],
     "question": "How many coins of diameter 1.75 cm and thickness 2 mm must be melted to form a cuboid of dimensions 5.5 cm × 10 cm × 3.5 cm?",
     "hint": "Volume of cuboid / Volume of one coin. Coin is a cylinder: r = 0.875 cm, h = 0.2 cm.",
     "expected_answer": "Cuboid: 5.5 × 10 × 3.5 = 192.5 cm³. Coin: π(0.875)²(0.2) = 22/7 × 0.765625 × 0.2 = 0.48125 cm³. n = 192.5/0.48125 = 400 coins."},
    {"id": 4, "type": "word_problem", "difficulty": 0.65, "concepts_tested": ["math10.sa_vol.conversion"],
     "question": "Water is flowing through a cylindrical pipe of internal radius 1 cm at 7 m/s. How much water (in litres) flows out in 30 minutes?",
     "hint": "In 1 second, a 'cylinder' of water 700 cm long flows out. Volume per second = πr²(700). 1 litre = 1000 cm³.",
     "expected_answer": "Rate = π(1)²(700) = 700π cm³/s = 700 × 22/7 = 2200 cm³/s. In 30 min = 1800 s: Volume = 2200 × 1800 = 3,960,000 cm³ = 3960 litres."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.sa_vol.conversion"],
     "question": "A well of diameter 3 m is dug 14 m deep. The earth taken out is spread evenly around the well, forming a ring-shaped embankment 4 m wide. Find the height of the embankment.",
     "hint": "Volume of earth = π(1.5)²(14). Embankment is a ring: outer radius = 1.5+4 = 5.5. Area of ring = π(5.5²−1.5²).",
     "expected_answer": "Volume dug = π(1.5)²(14) = π(2.25)(14) = 31.5π m³. Ring area = π(5.5² − 1.5²) = π(30.25 − 2.25) = 28π m². Height = Volume/Area = 31.5π/(28π) = 1.125 m = 1.125 m."},
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2 · Combination of Solids
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.sa_vol.combination"] = {
    "title": "🏗️ Combination of Solids — Building Complex Shapes",
    "hook": "A medicine capsule is a cylinder with two hemispherical ends. An ice cream cone is a cone topped with a hemisphere. A toy is a cone on top of a hemisphere. These 'combined solids' are everywhere!",
    "explanation": (
        key_point("<b>Volume of combined solid = Sum of volumes of each part.</b>")
        + warning_box("<b>Surface area ≠ Sum of surface areas!</b> You must <b>subtract the areas that are hidden</b> (joined surfaces).")
        + "<p><b>Common combinations:</b></p>"
        + comparison_table(
            ["Shape", "Volume", "Surface Area"],
            [["Cylinder + 2 hemispheres (capsule)", "πr²h + (4/3)πr³", "2πrh + 4πr² (no flat ends!)"],
             ["Cone + hemisphere (ice cream)", "(1/3)πr²h + (2/3)πr³", "πrl + 2πr² (no base!)"],
             ["Cylinder + cone on top", "πr²h + (1/3)πr²H", "2πrh + πrl + πr² (one base only)"]]
        )
        + tip_box("When two solids are joined, the touching surfaces are <b>inside</b> the combined shape and don't count toward the total surface area.")
    ),
    "worked_example": (
        "<b>Example:</b> A toy is shaped as a cone on top of a hemisphere. Cone: height = 4 cm, radius = 3 cm. Find total surface area.<br><br>"
        + step_box([
            ("Slant height of cone", "l = √(r² + h²) = √(9 + 16) = 5 cm"),
            ("CSA of cone", "πrl = π(3)(5) = 15π cm²"),
            ("CSA of hemisphere", "2πr² = 2π(9) = 18π cm²"),
            ("Total surface area", "15π + 18π = 33π ≈ 103.67 cm² (no base circle counted!)"),
        ])
    ),
    "try_this": {
        "question": "A medicine capsule is a cylinder (length 10 mm, radius 3.5 mm) with hemispherical ends. Find its total volume and surface area.",
        "hint": "Cylinder height = 10 mm (the straight part). Two hemispheres = one sphere.",
        "answer": "Volume = πr²h + (4/3)πr³ = π(3.5)²(10) + (4/3)π(3.5)³ = 122.5π + (171.5/3)π = 122.5π + 57.17π = 179.67π ≈ 564.35 mm³. Surface area = 2πrh + 4πr² = 2π(3.5)(10) + 4π(3.5)² = 70π + 49π = 119π ≈ 373.85 mm²."
    },
    "fun_fact": "A rocket is typically a combination of a cone (nose), cylinder (body), and possibly a frustum (engine section) — the exact shapes we study here!"
}

QUESTIONS["math10.sa_vol.combination"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.sa_vol.combination"],
     "question": "A solid is made of a cone (r = 7, h = 24) mounted on a hemisphere (r = 7). Find the total volume.",
     "hint": "V = (1/3)πr²h + (2/3)πr³.",
     "expected_answer": "Cone: (1/3)π(49)(24) = 392π. Hemisphere: (2/3)π(343) = 686π/3. Total = 392π + 686π/3 = (1176π + 686π)/3 = 1862π/3 ≈ 1950.67 cm³."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.sa_vol.combination"],
     "question": "A cylinder (r = 5, h = 13) has hemispheres attached at both ends. Find the total surface area.",
     "hint": "SA = CSA of cylinder + SA of two hemispheres = 2πrh + 4πr². No flat circles!",
     "expected_answer": "2π(5)(13) + 4π(25) = 130π + 100π = 230π ≈ 722.57 cm²."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.sa_vol.combination"],
     "question": "A tent is a cylinder of radius 7 m and height 3 m, topped with a cone of height 4 m. Find the volume of air inside and the canvas needed (only the lateral surfaces and the conical top).",
     "hint": "Slant height l = √(49+16) = √65. Canvas = CSA cylinder + CSA cone (no floor).",
     "expected_answer": "Volume = π(49)(3) + (1/3)π(49)(4) = 147π + 196π/3 = (441π + 196π)/3 = 637π/3 ≈ 667.05 m³. l = √65 ≈ 8.06. Canvas = 2π(7)(3) + π(7)(√65) = 42π + 7√65 π = π(42 + 7√65) ≈ π(42 + 56.4) ≈ 308.9 m²."},
    {"id": 4, "type": "word_problem", "difficulty": 0.65, "concepts_tested": ["math10.sa_vol.combination"],
     "question": "A wooden article is made by scooping out a hemisphere of radius 3.5 cm from each end of a cylinder of radius 3.5 cm and height 10 cm. Find the total surface area of the article.",
     "hint": "Inner curved surface of two hemispheres replaces the flat ends. SA = CSA cylinder + 2 × CSA hemisphere.",
     "expected_answer": "CSA cylinder = 2π(3.5)(10) = 70π. 2 hemispheres' CSA = 2 × 2π(3.5)² = 4π(12.25) = 49π. Total = 70π + 49π = 119π ≈ 374 cm². (Flat circular ends are removed and replaced by curved hemispherical surfaces.)"},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.sa_vol.combination"],
     "question": "A gulab jamun is modelled as a cylinder (length 5 cm, radius 1.4 cm) with hemispherical ends. If 45 gulab jamuns absorb 30% of their volume in sugar syrup, find the total volume of syrup consumed. (Use π = 22/7.)",
     "hint": "Volume of 1 gulab jamun = πr²h + (4/3)πr³ where h = 5 cm (cylindrical part). Syrup = 30% of total volume.",
     "expected_answer": "V₁ = π(1.4)²(5) + (4/3)π(1.4)³ = π(1.96)(5) + (4/3)π(2.744) = 9.8π + 3.659π = 13.459π. With π = 22/7: V₁ = 13.459 × 22/7 = 42.3 cm³. Total for 45: 45 × 42.3 = 1903.5 cm³. Syrup = 30% of 1903.5 = 571.05 cm³ ≈ 571 cm³."},
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 3 · Frustum of a Cone
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS["math10.sa_vol.frustum"] = {
    "title": "🪣 Frustum of a Cone — The Bucket Shape",
    "hook": "Cut off the top of a cone with a slice parallel to the base — the piece left at the bottom is called a 'frustum.' It's the shape of a bucket, a lampshade, or a drinking glass!",
    "explanation": (
        definition_box("Frustum", "The portion of a cone between the base and a plane parallel to the base that cuts the cone.")
        + '<div style="text-align:center;margin:10px 0"><svg width="200" height="160">'
        + '<polygon points="50,20 150,20 180,140 20,140" fill="#FFF3E0" stroke="#E65100" stroke-width="2"/>'
        + '<ellipse cx="100" cy="20" rx="50" ry="8" fill="none" stroke="#E65100" stroke-width="1.5"/>'
        + '<ellipse cx="100" cy="140" rx="80" ry="12" fill="none" stroke="#E65100" stroke-width="1.5"/>'
        + '<text x="100" y="85" text-anchor="middle" font-size="11" font-weight="bold">h</text>'
        + '<text x="100" y="15" text-anchor="middle" font-size="10">r</text>'
        + '<text x="100" y="158" text-anchor="middle" font-size="10">R</text>'
        + '<line x1="150" y1="20" x2="180" y2="140" stroke="#1565C0" stroke-width="1.5" stroke-dasharray="4"/>'
        + '<text x="175" y="80" font-size="10" fill="#1565C0">l</text>'
        + '</svg></div>'
        + formula_box("Slant height: l = √[h² + (R − r)²]", "Frustum slant height")
        + formula_box("Volume = (πh/3)(R² + r² + Rr)", "Frustum volume")
        + formula_box("CSA = π(R + r)l", "Frustum curved surface")
        + formula_box("TSA = π(R + r)l + πR² + πr²", "Frustum total surface area")
        + tip_box("Memory trick: Frustum volume formula has R² + r² + Rr — it's like the 'average' of all possible pairs of the two radii.")
    ),
    "worked_example": (
        "<b>Example:</b> A bucket is in the form of a frustum with top radius 20 cm, bottom radius 10 cm, and height 30 cm. Find its capacity (volume).<br><br>"
        + step_box([
            ("Use frustum volume formula", "V = (πh/3)(R² + r² + Rr)"),
            ("Substitute", "= (π × 30/3)(400 + 100 + 200)"),
            ("Compute", "= 10π × 700 = 7000π ≈ 21,991 cm³ ≈ 22 litres"),
        ])
    ),
    "try_this": {
        "question": "A flower pot is a frustum with top radius 14 cm, bottom radius 7 cm, height 24 cm. Find the slant height and curved surface area.",
        "hint": "l = √(h² + (R−r)²) = √(576 + 49). CSA = π(R+r)l.",
        "answer": "l = √(576 + 49) = √625 = 25 cm. CSA = π(14+7)(25) = 22/7 × 21 × 25 = 1650 cm²."
    },
    "fun_fact": "The word 'frustum' comes from Latin 'frustum' meaning 'a morsel cut off.' Mathematically, it's always about cutting a cone!"
}

QUESTIONS["math10.sa_vol.frustum"] = [
    {"id": 1, "type": "direct", "difficulty": 0.3, "concepts_tested": ["math10.sa_vol.frustum"],
     "question": "Find the slant height of a frustum with height 12, top radius 3, and bottom radius 8.",
     "hint": "l = √(h² + (R−r)²).",
     "expected_answer": "l = √(144 + 25) = √169 = 13 cm."},
    {"id": 2, "type": "direct", "difficulty": 0.4, "concepts_tested": ["math10.sa_vol.frustum"],
     "question": "Find the curved surface area of a frustum with radii 5 cm and 8 cm, slant height 10 cm.",
     "hint": "CSA = π(R + r)l.",
     "expected_answer": "CSA = π(8 + 5)(10) = 130π ≈ 408.41 cm²."},
    {"id": 3, "type": "word_problem", "difficulty": 0.5, "concepts_tested": ["math10.sa_vol.frustum"],
     "question": "A bucket has top diameter 40 cm, bottom diameter 20 cm, and depth 21 cm. Find its capacity in litres.",
     "hint": "R = 20, r = 10, h = 21. V = (πh/3)(R² + r² + Rr). 1 litre = 1000 cm³.",
     "expected_answer": "V = (π × 21/3)(400 + 100 + 200) = 7π × 700 = 4900π = 4900 × 22/7 = 15400 cm³ = 15.4 litres."},
    {"id": 4, "type": "word_problem", "difficulty": 0.65, "concepts_tested": ["math10.sa_vol.frustum"],
     "question": "A solid cone of height 40 cm has its top cut off by a plane parallel to the base at a height of 16 cm from the base. If the radius of the base is 10 cm, find the volume of the frustum.",
     "hint": "By similarity: if the full cone has height 40 and base r=10, the cut cone at top has height 24 (=40−16) and radius r' = 10 × 24/40 = 6.",
     "expected_answer": "Top cone: h = 24, r = 6. Frustum: h = 16, R = 10, r = 6. V = (π×16/3)(100+36+60) = (16π/3)(196) = 3136π/3 ≈ 3285 cm³."},
    {"id": 5, "type": "transfer_task", "difficulty": 0.8, "concepts_tested": ["math10.sa_vol.frustum"],
     "question": "A container shaped as a frustum (R=21, r=14, h=24) is filled with water. The water is poured into a cylindrical container of radius 21 cm. Find the height of water in the cylinder.",
     "hint": "Volume of frustum = Volume of cylinder. (πh/3)(R²+r²+Rr) = πr²H.",
     "expected_answer": "Frustum V = (π×24/3)(441+196+294) = 8π(931) = 7448π. Cylinder: π(21)²H = 441πH. 441πH = 7448π → H = 7448/441 = 16.89 cm ≈ 16.9 cm."},
]
