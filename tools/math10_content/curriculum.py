"""Class 10 Mathematics — NCERT Curriculum Definition (15 chapters, 53 concepts)."""

CURRICULUM = {
    "course_id": "math10",
    "title": "Class 10 Mathematics",
    "chapters": [
        {
            "chapter_id": "ch01",
            "title": "Real Numbers",
            "concepts": [
                {"concept_id": "math10.real_numbers.euclid_division", "title": "Euclid's Division Lemma", "bloom_level": "understand", "difficulty": 0.35, "prerequisites": [],
                 "description": "For any two positive integers a and b, there exist unique integers q and r such that a = bq + r, where 0 ≤ r < b.",
                 "key_ideas": ["Statement: a = bq + r where 0 ≤ r < b", "Used to find HCF of two numbers", "Algorithm terminates when remainder becomes 0", "The last non-zero remainder is the HCF"]},
                {"concept_id": "math10.real_numbers.euclid_hcf", "title": "Finding HCF Using Euclid's Algorithm", "bloom_level": "apply", "difficulty": 0.4, "prerequisites": ["math10.real_numbers.euclid_division"],
                 "description": "Apply Euclid's division lemma repeatedly to find the HCF of two or more numbers.",
                 "key_ideas": ["Apply a = bq + r repeatedly", "HCF(a,b) = HCF(b,r)", "Process stops when remainder = 0", "Can extend to three or more numbers"]},
                {"concept_id": "math10.real_numbers.fundamental_theorem", "title": "Fundamental Theorem of Arithmetic", "bloom_level": "understand", "difficulty": 0.4, "prerequisites": ["math10.real_numbers.euclid_hcf"],
                 "description": "Every composite number can be expressed as a product of primes uniquely (apart from order). Used to find HCF and LCM.",
                 "key_ideas": ["Every composite = unique product of primes", "HCF = common primes with lowest powers", "LCM = all primes with highest powers", "HCF × LCM = Product of two numbers"]},
                {"concept_id": "math10.real_numbers.irrational_proofs", "title": "Proving Irrationality", "bloom_level": "analyze", "difficulty": 0.55, "prerequisites": ["math10.real_numbers.fundamental_theorem"],
                 "description": "Use proof by contradiction to show √2, √3, √5 etc. are irrational.",
                 "key_ideas": ["Assume √p = a/b in lowest terms", "Square both sides → a² = pb²", "Show both a and b divisible by p → contradiction", "Extends to expressions like 3+2√5"]},
                {"concept_id": "math10.real_numbers.decimal_expansions", "title": "Decimal Expansions of Rationals", "bloom_level": "understand", "difficulty": 0.35, "prerequisites": ["math10.real_numbers.fundamental_theorem"],
                 "description": "p/q terminates iff q = 2ⁿ × 5ᵐ. Otherwise it is non-terminating repeating.",
                 "key_ideas": ["Terminating ⟺ q = 2ⁿ × 5ᵐ", "Non-terminating repeating if q has other prime factors", "Every rational is either terminating or repeating", "Irrational = non-terminating, non-repeating"]},
            ]
        },
        {
            "chapter_id": "ch02",
            "title": "Polynomials",
            "concepts": [
                {"concept_id": "math10.polynomials10.types_and_zeroes", "title": "Geometrical Meaning of Zeroes", "bloom_level": "understand", "difficulty": 0.3, "prerequisites": [],
                 "description": "Zeroes of a polynomial are x-coordinates where its graph crosses the x-axis. Linear has 1, quadratic at most 2, cubic at most 3.",
                 "key_ideas": ["Zero of p(x): value of x where p(x) = 0", "Geometrically = x-intercepts of the graph", "Linear → 1 zero, Quadratic → at most 2, Cubic → at most 3", "Number of zeroes = number of times graph meets x-axis"]},
                {"concept_id": "math10.polynomials10.zeroes_relationship", "title": "Relationship Between Zeroes and Coefficients", "bloom_level": "apply", "difficulty": 0.4, "prerequisites": ["math10.polynomials10.types_and_zeroes"],
                 "description": "For ax²+bx+c: sum of zeroes α+β = −b/a, product αβ = c/a. Can form polynomial from zeroes.",
                 "key_ideas": ["α + β = −b/a (sum of zeroes)", "αβ = c/a (product of zeroes)", "For cubic: α+β+γ = −b/a, αβ+βγ+γα = c/a, αβγ = −d/a", "Form polynomial: k[x² − (sum)x + (product)]"]},
                {"concept_id": "math10.polynomials10.division_algorithm", "title": "Division Algorithm for Polynomials", "bloom_level": "apply", "difficulty": 0.5, "prerequisites": ["math10.polynomials10.zeroes_relationship"],
                 "description": "p(x) = g(x)×q(x) + r(x) where deg(r) < deg(g). Used to find remaining zeroes when some are known.",
                 "key_ideas": ["Long division: divide, multiply, subtract, bring down", "p(x) = g(x)×q(x) + r(x)", "If two zeroes known → divide to find the rest", "Verify: deg(q) = deg(p) − deg(g)"]},
            ]
        },
        {
            "chapter_id": "ch03",
            "title": "Pair of Linear Equations in Two Variables",
            "concepts": [
                {"concept_id": "math10.linear_eq_pair.graphical_method", "title": "Graphical Method and Consistency", "bloom_level": "understand", "difficulty": 0.35, "prerequisites": [],
                 "description": "Two lines can intersect (unique solution), be parallel (no solution), or coincide (infinite solutions).",
                 "key_ideas": ["Intersecting: a₁/a₂ ≠ b₁/b₂ → unique solution", "Parallel: a₁/a₂ = b₁/b₂ ≠ c₁/c₂ → no solution", "Coincident: a₁/a₂ = b₁/b₂ = c₁/c₂ → infinite solutions", "Solution = point of intersection"]},
                {"concept_id": "math10.linear_eq_pair.substitution", "title": "Substitution Method", "bloom_level": "apply", "difficulty": 0.4, "prerequisites": ["math10.linear_eq_pair.graphical_method"],
                 "description": "Express one variable from one equation, substitute into the other, solve the single-variable equation.",
                 "key_ideas": ["Express y in terms of x from one equation", "Substitute into the other equation", "Solve the single-variable equation", "Back-substitute to find the other variable"]},
                {"concept_id": "math10.linear_eq_pair.elimination", "title": "Elimination Method", "bloom_level": "apply", "difficulty": 0.4, "prerequisites": ["math10.linear_eq_pair.substitution"],
                 "description": "Multiply equations to equalize one variable's coefficient, then add/subtract to eliminate it.",
                 "key_ideas": ["Multiply to equalize coefficients", "Add if signs opposite; subtract if same", "Solve resulting single-variable equation", "Back-substitute for the other variable"]},
                {"concept_id": "math10.linear_eq_pair.cross_multiplication", "title": "Cross-Multiplication Method", "bloom_level": "apply", "difficulty": 0.5, "prerequisites": ["math10.linear_eq_pair.elimination"],
                 "description": "Formula: x/(b₁c₂−b₂c₁) = y/(c₁a₂−c₂a₁) = 1/(a₁b₂−a₂b₁) for equations in standard form.",
                 "key_ideas": ["Write equations as a₁x + b₁y + c₁ = 0", "x/(b₁c₂−b₂c₁) = y/(c₁a₂−c₂a₁) = 1/(a₁b₂−a₂b₁)", "Works when a₁b₂ − a₂b₁ ≠ 0", "Gets both x and y in one step"]},
                {"concept_id": "math10.linear_eq_pair.word_problems10", "title": "Word Problems on Linear Equations", "bloom_level": "apply", "difficulty": 0.55, "prerequisites": ["math10.linear_eq_pair.elimination"],
                 "description": "Translate real-life situations into pairs of linear equations and solve.",
                 "key_ideas": ["Identify unknowns → assign variables", "Form two equations from conditions", "Solve using any algebraic method", "Common types: age, speed-time, fraction, digit problems"]},
            ]
        },
        {
            "chapter_id": "ch04",
            "title": "Quadratic Equations",
            "concepts": [
                {"concept_id": "math10.quadratic_equations.standard_form", "title": "Standard Form and Factorization", "bloom_level": "apply", "difficulty": 0.4, "prerequisites": [],
                 "description": "ax² + bx + c = 0 (a≠0). Solve by splitting the middle term: find two numbers with sum=b and product=ac.",
                 "key_ideas": ["Standard form: ax² + bx + c = 0, a ≠ 0", "Find two numbers: sum = b, product = ac", "Split middle term and factor by grouping", "Set each factor = 0 to find roots"]},
                {"concept_id": "math10.quadratic_equations.completing_square", "title": "Completing the Square", "bloom_level": "apply", "difficulty": 0.45, "prerequisites": ["math10.quadratic_equations.standard_form"],
                 "description": "Convert to (x+p)²=q form by adding (half of x-coefficient)² to both sides.",
                 "key_ideas": ["Divide by a to make x² coefficient = 1", "Move constant to RHS", "Add (b/2a)² to both sides", "LHS becomes perfect square → take square root"]},
                {"concept_id": "math10.quadratic_equations.quadratic_formula", "title": "Quadratic Formula", "bloom_level": "apply", "difficulty": 0.45, "prerequisites": ["math10.quadratic_equations.completing_square"],
                 "description": "x = (−b ± √(b²−4ac)) / 2a — the universal formula for all quadratic equations.",
                 "key_ideas": ["x = (−b ± √(b²−4ac)) / 2a", "Derived from completing the square", "The ± gives two roots", "Also called Shreedharacharya's formula"]},
                {"concept_id": "math10.quadratic_equations.nature_of_roots", "title": "Discriminant and Nature of Roots", "bloom_level": "analyze", "difficulty": 0.5, "prerequisites": ["math10.quadratic_equations.quadratic_formula"],
                 "description": "D = b²−4ac: D>0 → two distinct roots, D=0 → equal roots, D<0 → no real roots.",
                 "key_ideas": ["D = b² − 4ac", "D > 0: two distinct real roots", "D = 0: two equal roots (x = −b/2a)", "D < 0: no real roots"]},
                {"concept_id": "math10.quadratic_equations.word_problems_quad", "title": "Word Problems Leading to Quadratics", "bloom_level": "apply", "difficulty": 0.55, "prerequisites": ["math10.quadratic_equations.quadratic_formula"],
                 "description": "Formulate quadratic equations from area, speed, consecutive number, and age problems.",
                 "key_ideas": ["Identify variable and form equation", "Common: area, products, speed-distance", "Reject negative/non-sensical roots", "Always verify by substituting back"]},
            ]
        },
        {
            "chapter_id": "ch05",
            "title": "Arithmetic Progressions",
            "concepts": [
                {"concept_id": "math10.ap.intro", "title": "AP and Common Difference", "bloom_level": "understand", "difficulty": 0.3, "prerequisites": [],
                 "description": "An AP is a sequence where each term differs from the previous by a constant d (common difference).",
                 "key_ideas": ["AP: a, a+d, a+2d, a+3d, ...", "d = any term − previous term", "d can be positive, negative, or zero", "Check AP: verify constant difference"]},
                {"concept_id": "math10.ap.nth_term", "title": "The nth Term of an AP", "bloom_level": "apply", "difficulty": 0.4, "prerequisites": ["math10.ap.intro"],
                 "description": "aₙ = a + (n−1)d. Find any term directly, or find which term has a given value.",
                 "key_ideas": ["aₙ = a + (n−1)d", "Find n: solve a + (n−1)d = given value", "Last term l = a + (n−1)d", "If aₙ < 0 for some n, AP goes negative"]},
                {"concept_id": "math10.ap.sum_n_terms", "title": "Sum of First n Terms", "bloom_level": "apply", "difficulty": 0.45, "prerequisites": ["math10.ap.nth_term"],
                 "description": "Sₙ = n/2 × [2a + (n−1)d] or Sₙ = n/2 × (a + l). Gauss's trick: pair first+last.",
                 "key_ideas": ["Sₙ = n/2 × [2a + (n−1)d]", "Sₙ = n/2 × (a + l) when l is known", "aₙ = Sₙ − Sₙ₋₁", "Gauss: S = n/2 × (first + last)"]},
                {"concept_id": "math10.ap.applications", "title": "AP Applications and Problem Solving", "bloom_level": "apply", "difficulty": 0.5, "prerequisites": ["math10.ap.sum_n_terms"],
                 "description": "Use AP formulas to solve real-world problems: savings, stacking, salary increments, etc.",
                 "key_ideas": ["Check membership: solve a+(n−1)d = k for positive integer n", "Find a or d from given conditions", "Real-life: savings, depreciation, patterns", "If Sₙ = An²+Bn then d=2A, a=A+B"]},
            ]
        },
        {
            "chapter_id": "ch06",
            "title": "Triangles",
            "concepts": [
                {"concept_id": "math10.triangles10.bpt", "title": "Basic Proportionality Theorem (BPT)", "bloom_level": "understand", "difficulty": 0.4, "prerequisites": [],
                 "description": "If a line is drawn parallel to one side of a triangle, it divides the other two sides proportionally: AD/DB = AE/EC.",
                 "key_ideas": ["DE ∥ BC in △ABC ⇒ AD/DB = AE/EC", "Converse: if AD/DB = AE/EC then DE ∥ BC", "Also called Thales' theorem", "Foundation for similarity"]},
                {"concept_id": "math10.triangles10.similarity_criteria", "title": "Criteria for Similarity (AA, SSS, SAS)", "bloom_level": "apply", "difficulty": 0.45, "prerequisites": ["math10.triangles10.bpt"],
                 "description": "AA: two equal angles. SSS: all sides proportional. SAS: one equal angle between proportional sides.",
                 "key_ideas": ["AA: two angle pairs equal → similar", "SSS: all three side ratios equal → similar", "SAS: one equal angle between proportional sides → similar", "△ABC ~ △DEF ⇒ AB/DE = BC/EF = CA/FD"]},
                {"concept_id": "math10.triangles10.areas_similar", "title": "Areas of Similar Triangles", "bloom_level": "apply", "difficulty": 0.5, "prerequisites": ["math10.triangles10.similarity_criteria"],
                 "description": "Ratio of areas = square of ratio of corresponding sides: Area₁/Area₂ = (side₁/side₂)².",
                 "key_ideas": ["Area ratio = (side ratio)²", "Also = (altitude ratio)² = (median ratio)²", "If sides in ratio k:1, areas in ratio k²:1", "Useful when only side ratios are known"]},
                {"concept_id": "math10.triangles10.pythagoras", "title": "Pythagoras Theorem and Converse", "bloom_level": "apply", "difficulty": 0.45, "prerequisites": ["math10.triangles10.similarity_criteria"],
                 "description": "In a right triangle with hypotenuse c: c² = a² + b². Converse: if c² = a² + b², the triangle is right-angled.",
                 "key_ideas": ["AC² = AB² + BC² (right angle at B)", "Hypotenuse is the longest side", "Converse: if AC² = AB² + BC² then ∠B = 90°", "Triplets: (3,4,5), (5,12,13), (8,15,17)"]},
            ]
        },
        {
            "chapter_id": "ch07",
            "title": "Coordinate Geometry",
            "concepts": [
                {"concept_id": "math10.coord_geom.distance", "title": "Distance Formula", "bloom_level": "apply", "difficulty": 0.4, "prerequisites": [],
                 "description": "Distance between (x₁,y₁) and (x₂,y₂) = √[(x₂−x₁)² + (y₂−y₁)²].",
                 "key_ideas": ["d = √[(x₂−x₁)² + (y₂−y₁)²]", "From origin: √(x² + y²)", "d = 0 means same point", "Collinearity check: AB + BC = AC"]},
                {"concept_id": "math10.coord_geom.section", "title": "Section Formula and Midpoint", "bloom_level": "apply", "difficulty": 0.45, "prerequisites": ["math10.coord_geom.distance"],
                 "description": "Point dividing segment in ratio m:n = ((mx₂+nx₁)/(m+n), (my₂+ny₁)/(m+n)). Midpoint when m=n.",
                 "key_ideas": ["Section: ((mx₂+nx₁)/(m+n), (my₂+ny₁)/(m+n))", "Midpoint: ((x₁+x₂)/2, (y₁+y₂)/2)", "Centroid: ((x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3)", "Used to find medians and division points"]},
                {"concept_id": "math10.coord_geom.area_triangle", "title": "Area of Triangle (Coordinate)", "bloom_level": "apply", "difficulty": 0.5, "prerequisites": ["math10.coord_geom.section"],
                 "description": "Area = ½|x₁(y₂−y₃) + x₂(y₃−y₁) + x₃(y₁−y₂)|. If area = 0, points are collinear.",
                 "key_ideas": ["Area = ½|x₁(y₂−y₃) + x₂(y₃−y₁) + x₃(y₁−y₂)|", "Always take absolute value", "Area = 0 ⟹ collinear", "Extend to quadrilateral by splitting"]},
            ]
        },
        {
            "chapter_id": "ch08",
            "title": "Introduction to Trigonometry",
            "concepts": [
                {"concept_id": "math10.trig.ratios", "title": "Trigonometric Ratios", "bloom_level": "understand", "difficulty": 0.4, "prerequisites": [],
                 "description": "sin θ = O/H, cos θ = A/H, tan θ = O/A and their reciprocals cosec, sec, cot.",
                 "key_ideas": ["sin = Opposite/Hypotenuse", "cos = Adjacent/Hypotenuse", "tan = Opposite/Adjacent", "Reciprocals: cosec=1/sin, sec=1/cos, cot=1/tan"]},
                {"concept_id": "math10.trig.standard_angles", "title": "Trig Values of Standard Angles", "bloom_level": "remember", "difficulty": 0.35, "prerequisites": ["math10.trig.ratios"],
                 "description": "Exact values of sin, cos, tan for 0°, 30°, 45°, 60°, 90°.",
                 "key_ideas": ["sin: 0, ½, 1/√2, √3/2, 1 for 0°,30°,45°,60°,90°", "cos is sin reversed", "tan: 0, 1/√3, 1, √3, undefined", "Trick: sin θ = √n/2 for n=0,1,2,3,4"]},
                {"concept_id": "math10.trig.complementary", "title": "Complementary Angle Identities", "bloom_level": "apply", "difficulty": 0.4, "prerequisites": ["math10.trig.standard_angles"],
                 "description": "sin(90°−θ) = cos θ, tan(90°−θ) = cot θ, sec(90°−θ) = cosec θ.",
                 "key_ideas": ["sin(90°−θ) = cos θ", "cos(90°−θ) = sin θ", "tan(90°−θ) = cot θ", "Useful: sin 72° = cos 18°"]},
                {"concept_id": "math10.trig.identities", "title": "Trigonometric Identities", "bloom_level": "apply", "difficulty": 0.5, "prerequisites": ["math10.trig.complementary"],
                 "description": "sin²θ+cos²θ=1, 1+tan²θ=sec²θ, 1+cot²θ=cosec²θ. Proving identities.",
                 "key_ideas": ["sin²θ + cos²θ = 1", "1 + tan²θ = sec²θ", "1 + cot²θ = cosec²θ", "To prove: work on one side to reach the other"]},
            ]
        },
        {
            "chapter_id": "ch09",
            "title": "Some Applications of Trigonometry",
            "concepts": [
                {"concept_id": "math10.trig_app.elevation_depression", "title": "Angle of Elevation and Depression", "bloom_level": "understand", "difficulty": 0.4, "prerequisites": ["math10.trig.ratios"],
                 "description": "Elevation = looking up from horizontal. Depression = looking down. Both form right triangles.",
                 "key_ideas": ["Elevation: angle above horizontal (looking up)", "Depression: angle below horizontal (looking down)", "Elevation from A = Depression from B (alternate angles)", "Always draw a right triangle"]},
                {"concept_id": "math10.trig_app.heights_distances", "title": "Heights and Distances Problems", "bloom_level": "apply", "difficulty": 0.55, "prerequisites": ["math10.trig_app.elevation_depression"],
                 "description": "Apply trig ratios to find heights of towers, widths of rivers, etc. using known angles and distances.",
                 "key_ideas": ["Draw figure → identify right triangle", "tan θ = height/distance (most common)", "Two-triangle problems: set up simultaneous equations", "Common: tower on cliff, moving observer"]},
            ]
        },
        {
            "chapter_id": "ch10",
            "title": "Circles",
            "concepts": [
                {"concept_id": "math10.circles10.tangent_properties", "title": "Tangent to a Circle — Properties", "bloom_level": "understand", "difficulty": 0.4, "prerequisites": [],
                 "description": "A tangent touches a circle at exactly one point and is perpendicular to the radius at that point.",
                 "key_ideas": ["Tangent touches at exactly one point", "Tangent ⊥ Radius at point of contact", "No tangent from inside the circle", "Exactly one tangent at each point on circle"]},
                {"concept_id": "math10.circles10.tangent_theorems", "title": "Tangent Theorems and Problems", "bloom_level": "apply", "difficulty": 0.5, "prerequisites": ["math10.circles10.tangent_properties"],
                 "description": "Tangents from an external point are equal: PA = PB. Many elegant geometric results follow.",
                 "key_ideas": ["PA = PB (tangents from external point)", "OP bisects angle between tangents", "In △OAP: OA² + AP² = OP²", "Used in incircle and circumscribed polygon problems"]},
            ]
        },
        {
            "chapter_id": "ch11",
            "title": "Constructions",
            "concepts": [
                {"concept_id": "math10.constructions10.divide_segment", "title": "Dividing a Line Segment in a Ratio", "bloom_level": "apply", "difficulty": 0.4, "prerequisites": [],
                 "description": "Construct a point dividing a segment in ratio m:n using BPT.",
                 "key_ideas": ["Draw ray at acute angle, mark m+n arcs", "Join last mark to endpoint", "Draw parallel through mth mark", "Based on Basic Proportionality Theorem"]},
                {"concept_id": "math10.constructions10.similar_triangle", "title": "Construction of Similar Triangles", "bloom_level": "apply", "difficulty": 0.45, "prerequisites": ["math10.constructions10.divide_segment"],
                 "description": "Construct a triangle similar to a given triangle with a given scale factor.",
                 "key_ideas": ["Scale factor < 1: smaller triangle", "Scale factor > 1: larger triangle", "Use segment division technique", "All angles equal to original"]},
                {"concept_id": "math10.constructions10.tangent_to_circle", "title": "Construction of Tangents to a Circle", "bloom_level": "apply", "difficulty": 0.5, "prerequisites": ["math10.constructions10.similar_triangle"],
                 "description": "Construct tangents from an external point using the property that angle in semicircle = 90°.",
                 "key_ideas": ["Join OP, find midpoint M", "Draw circle with centre M, radius MO", "Intersection points = points of tangency", "Two tangents from external point are equal"]},
            ]
        },
        {
            "chapter_id": "ch12",
            "title": "Areas Related to Circles",
            "concepts": [
                {"concept_id": "math10.areas_circles.basics", "title": "Circumference and Area of a Circle", "bloom_level": "apply", "difficulty": 0.35, "prerequisites": [],
                 "description": "Circumference = 2πr, Area = πr². Foundation for sectors and segments.",
                 "key_ideas": ["Circumference = 2πr = πd", "Area = πr²", "π ≈ 22/7 or 3.14159...", "Ring area = π(R² − r²)"]},
                {"concept_id": "math10.areas_circles.sector_segment", "title": "Sector and Segment Areas", "bloom_level": "apply", "difficulty": 0.45, "prerequisites": ["math10.areas_circles.basics"],
                 "description": "Sector area = (θ/360)×πr². Segment area = Sector area − Triangle area.",
                 "key_ideas": ["Arc length = (θ/360) × 2πr", "Sector area = (θ/360) × πr²", "Segment area = Sector − Triangle", "Major + Minor = Full circle"]},
                {"concept_id": "math10.areas_circles.combined_figures", "title": "Areas of Combined Plane Figures", "bloom_level": "apply", "difficulty": 0.5, "prerequisites": ["math10.areas_circles.sector_segment"],
                 "description": "Find shaded areas in figures combining circles, squares, triangles by adding/subtracting individual areas.",
                 "key_ideas": ["Identify shapes involved", "Add or subtract areas", "Shaded = Total − Unshaded (often easier)", "Draw auxiliary lines to simplify"]},
            ]
        },
        {
            "chapter_id": "ch13",
            "title": "Surface Areas and Volumes",
            "concepts": [
                {"concept_id": "math10.sa_vol.conversion", "title": "Conversion of Solids", "bloom_level": "apply", "difficulty": 0.45, "prerequisites": [],
                 "description": "When a solid is melted and recast, volume is conserved. Set V₁ = V₂ to find unknowns.",
                 "key_ideas": ["Volume conserved when melted/recast", "V(old) = n × V(new) for n objects", "Common: sphere ↔ cylinder ↔ cone", "n = V(original) / V(one new)"]},
                {"concept_id": "math10.sa_vol.combination", "title": "Combined Solids", "bloom_level": "apply", "difficulty": 0.5, "prerequisites": ["math10.sa_vol.conversion"],
                 "description": "Real objects are combinations of basic solids. Volume = sum of parts. TSA = sum of visible surfaces.",
                 "key_ideas": ["Volume = sum of individual volumes", "TSA ≠ sum of all surfaces (subtract joined faces)", "Common: cylinder+cone, hemisphere+cylinder", "CSA of combined = sum of visible CSAs"]},
                {"concept_id": "math10.sa_vol.frustum", "title": "Frustum of a Cone", "bloom_level": "apply", "difficulty": 0.5, "prerequisites": ["math10.sa_vol.combination"],
                 "description": "Frustum = cone with top sliced off. V = πh/3(R²+r²+Rr), l = √[h²+(R−r)²].",
                 "key_ideas": ["V = (πh/3)(R² + r² + Rr)", "Slant height l = √[h² + (R−r)²]", "CSA = π(R+r)l", "TSA = π(R+r)l + πR² + πr²"]},
            ]
        },
        {
            "chapter_id": "ch14",
            "title": "Statistics",
            "concepts": [
                {"concept_id": "math10.stats.mean", "title": "Mean of Grouped Data", "bloom_level": "apply", "difficulty": 0.4, "prerequisites": [],
                 "description": "Three methods: Direct (Σfᵢxᵢ/Σfᵢ), Assumed Mean, and Step Deviation.",
                 "key_ideas": ["Direct: Mean = Σfᵢxᵢ / Σfᵢ", "Assumed mean: Mean = a + Σfᵢdᵢ/Σfᵢ", "Step deviation: Mean = a + (Σfᵢuᵢ/Σfᵢ)×h", "Class mark xᵢ = (upper + lower)/2"]},
                {"concept_id": "math10.stats.median", "title": "Median of Grouped Data", "bloom_level": "apply", "difficulty": 0.45, "prerequisites": ["math10.stats.mean"],
                 "description": "Median = l + [(n/2 − cf)/f] × h. Find median class using cumulative frequency.",
                 "key_ideas": ["Find n/2, locate median class via cf", "Median = l + [(n/2 − cf)/f] × h", "cf = cumulative frequency BEFORE median class", "l = lower boundary, h = class width"]},
                {"concept_id": "math10.stats.mode", "title": "Mode of Grouped Data", "bloom_level": "apply", "difficulty": 0.4, "prerequisites": ["math10.stats.mean"],
                 "description": "Mode = l + [(f₁−f₀)/(2f₁−f₀−f₂)] × h. Modal class has the highest frequency.",
                 "key_ideas": ["Modal class = highest frequency class", "Mode = l + [(f₁−f₀)/(2f₁−f₀−f₂)] × h", "f₁ = modal frequency, f₀ = before, f₂ = after", "Empirical: 3 Median ≈ Mode + 2 Mean"]},
                {"concept_id": "math10.stats.ogive", "title": "Ogives and Graphical Median", "bloom_level": "apply", "difficulty": 0.45, "prerequisites": ["math10.stats.median"],
                 "description": "Ogive = cumulative frequency curve. Intersection of 'less than' and 'more than' ogives gives the median.",
                 "key_ideas": ["Less-than ogive: upper limits vs cf (rising)", "More-than ogive: lower limits vs cf (falling)", "Median = x-coordinate of intersection", "Can also find median from n/2 line on single ogive"]},
            ]
        },
        {
            "chapter_id": "ch15",
            "title": "Probability",
            "concepts": [
                {"concept_id": "math10.prob.classical", "title": "Classical Probability", "bloom_level": "understand", "difficulty": 0.35, "prerequisites": [],
                 "description": "P(E) = Favourable outcomes / Total equally likely outcomes. 0 ≤ P(E) ≤ 1.",
                 "key_ideas": ["P(E) = Favourable / Total", "0 ≤ P(E) ≤ 1", "P(sure event) = 1, P(impossible) = 0", "P(E) + P(not E) = 1"]},
                {"concept_id": "math10.prob.events", "title": "Events and Sample Space", "bloom_level": "understand", "difficulty": 0.35, "prerequisites": ["math10.prob.classical"],
                 "description": "Sample space = all possible outcomes. Elementary event has one outcome. Complement: P(Ē) = 1−P(E).",
                 "key_ideas": ["Sample space = set of all outcomes", "Elementary event = single outcome", "Compound event = multiple outcomes", "Sum of all elementary event probabilities = 1"]},
                {"concept_id": "math10.prob.problems", "title": "Probability — Coins, Dice, Cards", "bloom_level": "apply", "difficulty": 0.45, "prerequisites": ["math10.prob.events"],
                 "description": "Apply probability to coins (2 outcomes), dice (6 outcomes), cards (52 cards, 4 suits × 13 ranks).",
                 "key_ideas": ["Coin: P(H)=P(T)=½; two coins: 4 outcomes", "Die: 6 outcomes; two dice: 36 outcomes", "Cards: 52 total, 4 suits × 13 ranks", "Strategy: list sample space, count favourable"]},
            ]
        },
    ]
}
