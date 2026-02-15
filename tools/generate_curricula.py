#!/usr/bin/env python3
"""
Course Template Generator
=========================
Generates curriculum JSON files for ALL courses from compact seed data.
Each course is defined as pure DATA — the generator is the TEMPLATE.

Run:  python -m tools.generate_curricula

To add a new course:
  1. Add its seed data to COURSE_SEEDS below
  2. Re-run this script

Each generated curriculum is a SEED — use tools/expand_with_gemini.py
to have Gemini flesh out additional concepts per chapter.
"""

import json
from pathlib import Path

CONTENT_DIR = Path(__file__).resolve().parent.parent / "data" / "content"

# ─────────────────────────────────────────────────────────────────────────────
# COMPACT SEED FORMAT
# ─────────────────────────────────────────────────────────────────────────────
# Each concept tuple:  (id_suffix, title, bloom, difficulty, [prereq_suffixes])
# Full concept_id = "{course_id}.{chapter_short}.{id_suffix}"
# Prereqs reference id_suffixes within the SAME course (auto-prefixed).
#
# Bloom levels: remember, understand, apply, analyze, evaluate, create
# Difficulty: 0.0 (trivial) → 1.0 (very hard)
# ─────────────────────────────────────────────────────────────────────────────


def _c(suffix, title, bloom="understand", diff=0.3, prereqs=None):
    """Shorthand concept constructor."""
    return (suffix, title, bloom, diff, prereqs or [])


# ══════════════════════════════════════════════════════════════════════════════
#  MATHEMATICS  —  Classes 7-12
# ══════════════════════════════════════════════════════════════════════════════

MATH7_CHAPTERS = [
    ("integers", "Integers", [
        _c("properties", "Properties of Integers", "understand", 0.25),
        _c("add_sub", "Addition and Subtraction of Integers", "apply", 0.3, ["integers.properties"]),
        _c("mul_div", "Multiplication and Division of Integers", "apply", 0.35, ["integers.add_sub"]),
    ]),
    ("fractions_decimals", "Fractions and Decimals", [
        _c("mul_fractions", "Multiplication of Fractions", "apply", 0.3),
        _c("div_fractions", "Division of Fractions", "apply", 0.35, ["fractions_decimals.mul_fractions"]),
        _c("mul_decimals", "Multiplication of Decimals", "apply", 0.3),
        _c("div_decimals", "Division of Decimals", "apply", 0.35, ["fractions_decimals.mul_decimals"]),
    ]),
    ("data_handling", "Data Handling", [
        _c("collecting_data", "Collecting and Organizing Data", "understand", 0.2),
        _c("arithmetic_mean", "Arithmetic Mean", "apply", 0.3, ["data_handling.collecting_data"]),
        _c("bar_graphs", "Bar Graphs", "apply", 0.3, ["data_handling.collecting_data"]),
        _c("probability_intro", "Chance and Probability", "understand", 0.35, ["data_handling.bar_graphs"]),
    ]),
    ("simple_equations", "Simple Equations", [
        _c("variable_equation", "Variables and Equations", "understand", 0.25),
        _c("solving_equations", "Solving Simple Equations", "apply", 0.35, ["simple_equations.variable_equation"]),
        _c("word_problems_eq", "Word Problems with Equations", "apply", 0.4, ["simple_equations.solving_equations"]),
    ]),
    ("lines_angles", "Lines and Angles", [
        _c("related_angles", "Complementary and Supplementary Angles", "understand", 0.25),
        _c("adjacent_angles", "Adjacent and Vertically Opposite Angles", "understand", 0.3, ["lines_angles.related_angles"]),
        _c("parallel_transversal", "Parallel Lines and Transversal", "apply", 0.4, ["lines_angles.adjacent_angles"]),
    ]),
    ("triangles", "The Triangle and Its Properties", [
        _c("types_triangles", "Types of Triangles", "remember", 0.2),
        _c("angle_sum", "Angle Sum Property", "understand", 0.3, ["triangles.types_triangles"]),
        _c("exterior_angle", "Exterior Angle Property", "apply", 0.35, ["triangles.angle_sum"]),
        _c("pythagoras_intro", "Pythagoras Property (Introduction)", "understand", 0.4, ["triangles.angle_sum"]),
    ]),
    ("congruence", "Congruence of Triangles", [
        _c("congruent_figures", "Congruent Figures", "understand", 0.25),
        _c("criteria_congruence", "Criteria for Congruence (SSS, SAS, ASA, RHS)", "apply", 0.4, ["congruence.congruent_figures"]),
    ]),
    ("comparing_quantities", "Comparing Quantities", [
        _c("ratios", "Ratios and Equivalent Ratios", "understand", 0.25),
        _c("percentage", "Percentage", "apply", 0.3, ["comparing_quantities.ratios"]),
        _c("profit_loss", "Profit, Loss and Discount", "apply", 0.4, ["comparing_quantities.percentage"]),
        _c("simple_interest", "Simple Interest", "apply", 0.4, ["comparing_quantities.percentage"]),
    ]),
    ("rational_numbers", "Rational Numbers", [
        _c("intro_rationals", "Introduction to Rational Numbers", "understand", 0.3),
        _c("operations_rationals", "Operations on Rational Numbers", "apply", 0.4, ["rational_numbers.intro_rationals"]),
    ]),
    ("practical_geometry", "Practical Geometry", [
        _c("construct_parallel", "Constructing Parallel Lines", "apply", 0.3),
        _c("construct_triangles", "Constructing Triangles (SSS, SAS, ASA)", "apply", 0.4, ["practical_geometry.construct_parallel"]),
    ]),
    ("perimeter_area", "Perimeter and Area", [
        _c("area_rectangle", "Area of Rectangle and Square", "apply", 0.25),
        _c("area_parallelogram", "Area of Parallelogram", "apply", 0.3, ["perimeter_area.area_rectangle"]),
        _c("area_triangle", "Area of Triangle", "apply", 0.35, ["perimeter_area.area_parallelogram"]),
        _c("area_circle", "Circumference and Area of Circle", "apply", 0.4, ["perimeter_area.area_triangle"]),
    ]),
    ("algebraic_expressions", "Algebraic Expressions", [
        _c("terms_coefficients", "Terms, Factors and Coefficients", "understand", 0.25),
        _c("like_unlike_terms", "Like and Unlike Terms", "understand", 0.3, ["algebraic_expressions.terms_coefficients"]),
        _c("add_sub_expressions", "Adding and Subtracting Algebraic Expressions", "apply", 0.35, ["algebraic_expressions.like_unlike_terms"]),
    ]),
    ("exponents", "Exponents and Powers", [
        _c("exponent_intro", "Exponents", "understand", 0.25),
        _c("laws_exponents", "Laws of Exponents", "apply", 0.35, ["exponents.exponent_intro"]),
        _c("standard_form", "Expressing Large Numbers in Standard Form", "apply", 0.3, ["exponents.laws_exponents"]),
    ]),
    ("symmetry", "Symmetry", [
        _c("lines_symmetry", "Lines of Symmetry", "understand", 0.2),
        _c("rotational_symmetry", "Rotational Symmetry", "understand", 0.3, ["symmetry.lines_symmetry"]),
    ]),
    ("solid_shapes", "Visualising Solid Shapes", [
        _c("faces_edges_vertices", "Faces, Edges and Vertices", "remember", 0.2),
        _c("nets_solids", "Nets of 3D Shapes", "understand", 0.3, ["solid_shapes.faces_edges_vertices"]),
        _c("cross_sections", "Cross Sections and Shadows", "analyze", 0.35, ["solid_shapes.nets_solids"]),
    ]),
]

MATH8_CHAPTERS = [
    ("rational_numbers", "Rational Numbers", [
        _c("properties", "Properties of Rational Numbers", "understand", 0.3),
        _c("representation", "Representation on Number Line", "apply", 0.3, ["rational_numbers.properties"]),
        _c("between_rationals", "Rational Numbers Between Two Rationals", "apply", 0.35, ["rational_numbers.representation"]),
    ]),
    ("linear_equations", "Linear Equations in One Variable", [
        _c("solving_linear", "Solving Linear Equations", "apply", 0.3),
        _c("reducible_linear", "Equations Reducible to Linear Form", "apply", 0.4, ["linear_equations.solving_linear"]),
        _c("word_problems", "Applications of Linear Equations", "apply", 0.45, ["linear_equations.reducible_linear"]),
    ]),
    ("quadrilaterals", "Understanding Quadrilaterals", [
        _c("polygons", "Polygons and Classification", "understand", 0.25),
        _c("angle_sum_quad", "Angle Sum Property of Quadrilaterals", "apply", 0.3, ["quadrilaterals.polygons"]),
        _c("special_quads", "Properties of Parallelogram, Rhombus, Trapezium", "analyze", 0.4, ["quadrilaterals.angle_sum_quad"]),
    ]),
    ("practical_geometry", "Practical Geometry", [
        _c("construct_quad", "Constructing Quadrilaterals", "apply", 0.35),
        _c("special_constructions", "Special Cases of Quadrilateral Construction", "apply", 0.4, ["practical_geometry.construct_quad"]),
    ]),
    ("data_handling", "Data Handling", [
        _c("organising_data", "Organising Data and Frequency Distribution", "understand", 0.25),
        _c("pie_charts", "Pie Charts", "apply", 0.35, ["data_handling.organising_data"]),
        _c("probability", "Probability — Equally Likely Outcomes", "apply", 0.4, ["data_handling.organising_data"]),
    ]),
    ("squares_roots", "Squares and Square Roots", [
        _c("perfect_squares", "Perfect Squares and Properties", "understand", 0.3),
        _c("finding_sqrt", "Finding Square Roots", "apply", 0.4, ["squares_roots.perfect_squares"]),
        _c("estimating_sqrt", "Estimating Square Roots", "apply", 0.4, ["squares_roots.finding_sqrt"]),
    ]),
    ("cubes_roots", "Cubes and Cube Roots", [
        _c("perfect_cubes", "Perfect Cubes", "understand", 0.3),
        _c("cube_root", "Finding Cube Roots", "apply", 0.4, ["cubes_roots.perfect_cubes"]),
    ]),
    ("comparing_quantities", "Comparing Quantities", [
        _c("compound_interest", "Compound Interest", "apply", 0.4),
        _c("discount_tax", "Discount, Tax and Sales Tax", "apply", 0.35),
        _c("ci_applications", "Applications of CI (Population, Depreciation)", "apply", 0.45, ["comparing_quantities.compound_interest"]),
    ]),
    ("algebraic_identities", "Algebraic Expressions and Identities", [
        _c("types_expressions", "Types of Algebraic Expressions", "understand", 0.25),
        _c("multiplication", "Multiplication of Polynomials", "apply", 0.35, ["algebraic_identities.types_expressions"]),
        _c("standard_identities", "Standard Algebraic Identities", "apply", 0.4, ["algebraic_identities.multiplication"]),
    ]),
    ("solid_shapes", "Visualising Solid Shapes", [
        _c("views_3d", "Views of 3D Shapes", "understand", 0.3),
        _c("mapping", "Mapping Space Around Us", "apply", 0.35, ["solid_shapes.views_3d"]),
    ]),
    ("mensuration", "Mensuration", [
        _c("area_trapezium", "Area of Trapezium and General Quadrilateral", "apply", 0.35),
        _c("area_polygon", "Area of General Polygon", "apply", 0.4, ["mensuration.area_trapezium"]),
        _c("surface_area_volume", "Surface Area and Volume of Cube, Cuboid, Cylinder", "apply", 0.45, ["mensuration.area_polygon"]),
    ]),
    ("exponents_powers", "Exponents and Powers", [
        _c("negative_exponents", "Negative Exponents", "understand", 0.35),
        _c("laws_review", "Laws of Exponents (Expanded)", "apply", 0.4, ["exponents_powers.negative_exponents"]),
    ]),
    ("proportion", "Direct and Inverse Proportions", [
        _c("direct_proportion", "Direct Proportion", "apply", 0.3),
        _c("inverse_proportion", "Inverse Proportion", "apply", 0.35, ["proportion.direct_proportion"]),
    ]),
    ("factorisation", "Factorisation", [
        _c("common_factors", "Common Factors Method", "apply", 0.3),
        _c("regrouping", "Factorisation by Regrouping", "apply", 0.35, ["factorisation.common_factors"]),
        _c("using_identities", "Factorisation Using Identities", "apply", 0.4, ["factorisation.regrouping"]),
    ]),
    ("graphs", "Introduction to Graphs", [
        _c("reading_graphs", "Reading Bar Graphs and Pie Charts", "understand", 0.2),
        _c("linear_graphs", "Linear Graphs", "apply", 0.35, ["graphs.reading_graphs"]),
        _c("plotting_points", "Plotting Points and Reading Coordinates", "apply", 0.3, ["graphs.reading_graphs"]),
    ]),
]

MATH9_CHAPTERS = [
    ("number_systems", "Number Systems", [
        _c("irrational_numbers", "Irrational Numbers", "understand", 0.35),
        _c("real_number_line", "Real Numbers on Number Line", "apply", 0.4, ["number_systems.irrational_numbers"]),
        _c("laws_radicals", "Laws of Radicals and Exponents for Real Numbers", "apply", 0.45, ["number_systems.real_number_line"]),
    ]),
    ("polynomials", "Polynomials", [
        _c("types_polynomials", "Polynomials in One Variable", "understand", 0.3),
        _c("zeroes_polynomial", "Zeroes of a Polynomial", "apply", 0.4, ["polynomials.types_polynomials"]),
        _c("remainder_theorem", "Remainder Theorem and Factor Theorem", "apply", 0.5, ["polynomials.zeroes_polynomial"]),
        _c("algebraic_identities", "Algebraic Identities", "apply", 0.45, ["polynomials.remainder_theorem"]),
    ]),
    ("coordinate_geometry", "Coordinate Geometry", [
        _c("cartesian_plane", "Cartesian Plane and Coordinates", "understand", 0.3),
        _c("plotting_points", "Plotting Points in All Quadrants", "apply", 0.35, ["coordinate_geometry.cartesian_plane"]),
    ]),
    ("linear_eq_two_var", "Linear Equations in Two Variables", [
        _c("forming_equations", "Forming Linear Equations in Two Variables", "understand", 0.35),
        _c("graphical_solution", "Graphical Representation of Linear Equations", "apply", 0.4, ["linear_eq_two_var.forming_equations"]),
    ]),
    ("euclid_geometry", "Introduction to Euclid's Geometry", [
        _c("axioms_postulates", "Euclid's Axioms and Postulates", "remember", 0.3),
        _c("equivalent_axioms", "Equivalent Versions of Fifth Postulate", "understand", 0.4, ["euclid_geometry.axioms_postulates"]),
    ]),
    ("lines_angles", "Lines and Angles", [
        _c("angle_pairs", "Pairs of Angles", "understand", 0.3),
        _c("parallel_transversal", "Parallel Lines and Transversal", "apply", 0.4, ["lines_angles.angle_pairs"]),
        _c("angle_sum_triangle", "Angle Sum Property of Triangle", "apply", 0.35, ["lines_angles.parallel_transversal"]),
    ]),
    ("triangles", "Triangles", [
        _c("congruence_criteria", "Congruence Criteria (SAS, ASA, SSS, RHS)", "apply", 0.4),
        _c("triangle_inequalities", "Inequalities in Triangles", "analyze", 0.45, ["triangles.congruence_criteria"]),
    ]),
    ("quadrilaterals", "Quadrilaterals", [
        _c("angle_sum_quad", "Angle Sum Property of Quadrilateral", "understand", 0.3),
        _c("properties_parallelogram", "Properties of Parallelogram", "apply", 0.4, ["quadrilaterals.angle_sum_quad"]),
        _c("midpoint_theorem", "Mid-Point Theorem", "apply", 0.45, ["quadrilaterals.properties_parallelogram"]),
    ]),
    ("areas_parallelograms", "Areas of Parallelograms and Triangles", [
        _c("same_base_parallels", "Figures on Same Base and Between Same Parallels", "understand", 0.35),
        _c("area_theorems", "Area Theorems for Parallelograms and Triangles", "apply", 0.45, ["areas_parallelograms.same_base_parallels"]),
    ]),
    ("circles", "Circles", [
        _c("circle_terms", "Chord, Arc, Sector, Segment", "remember", 0.25),
        _c("angle_subtended", "Angle Subtended by a Chord", "apply", 0.4, ["circles.circle_terms"]),
        _c("cyclic_quadrilateral", "Cyclic Quadrilateral", "apply", 0.45, ["circles.angle_subtended"]),
    ]),
    ("constructions", "Constructions", [
        _c("bisect_angle", "Bisecting an Angle and Perpendicular Bisector", "apply", 0.3),
        _c("construct_triangle", "Construction of Triangles (Given Conditions)", "apply", 0.4, ["constructions.bisect_angle"]),
    ]),
    ("herons_formula", "Heron's Formula", [
        _c("herons", "Area Using Heron's Formula", "apply", 0.4),
        _c("applications_herons", "Applications to Quadrilaterals", "apply", 0.45, ["herons_formula.herons"]),
    ]),
    ("surface_area_volume", "Surface Areas and Volumes", [
        _c("cuboid_cylinder", "Surface Area of Cuboid, Cylinder", "apply", 0.35),
        _c("cone_sphere", "Surface Area of Cone, Sphere", "apply", 0.4, ["surface_area_volume.cuboid_cylinder"]),
        _c("volumes", "Volume of Cuboid, Cylinder, Cone, Sphere", "apply", 0.45, ["surface_area_volume.cone_sphere"]),
    ]),
    ("statistics", "Statistics", [
        _c("mean_median_mode", "Mean, Median and Mode", "apply", 0.35),
        _c("grouped_data", "Frequency Distribution and Histograms", "apply", 0.4, ["statistics.mean_median_mode"]),
    ]),
    ("probability", "Probability", [
        _c("experimental_prob", "Experimental Probability", "understand", 0.35),
        _c("applications_prob", "Probability Applications", "apply", 0.4, ["probability.experimental_prob"]),
    ]),
]

MATH10_CHAPTERS = [
    ("real_numbers", "Real Numbers", [
        _c("euclid_division", "Euclid's Division Lemma", "understand", 0.4),
        _c("fundamental_theorem", "Fundamental Theorem of Arithmetic", "apply", 0.45, ["real_numbers.euclid_division"]),
        _c("irrational_proofs", "Proof of Irrationality", "analyze", 0.5, ["real_numbers.fundamental_theorem"]),
    ]),
    ("polynomials", "Polynomials", [
        _c("zeroes_relationship", "Relationship Between Zeroes and Coefficients", "apply", 0.4),
        _c("division_algorithm", "Division Algorithm for Polynomials", "apply", 0.5, ["polynomials.zeroes_relationship"]),
    ]),
    ("linear_eq_pair", "Pair of Linear Equations in Two Variables", [
        _c("graphical_method", "Graphical Method of Solution", "apply", 0.35),
        _c("algebraic_methods", "Substitution, Elimination, Cross-Multiplication", "apply", 0.45, ["linear_eq_pair.graphical_method"]),
        _c("word_problems", "Word Problems on Linear Equation Pairs", "apply", 0.5, ["linear_eq_pair.algebraic_methods"]),
    ]),
    ("quadratic_equations", "Quadratic Equations", [
        _c("standard_form", "Standard Form and Factorisation", "apply", 0.4),
        _c("quadratic_formula", "Quadratic Formula", "apply", 0.45, ["quadratic_equations.standard_form"]),
        _c("nature_of_roots", "Nature of Roots (Discriminant)", "analyze", 0.5, ["quadratic_equations.quadratic_formula"]),
    ]),
    ("arithmetic_progressions", "Arithmetic Progressions", [
        _c("ap_intro", "Introduction to AP — nth Term", "understand", 0.35),
        _c("sum_of_ap", "Sum of First n Terms", "apply", 0.45, ["arithmetic_progressions.ap_intro"]),
        _c("ap_applications", "Applications of AP", "apply", 0.5, ["arithmetic_progressions.sum_of_ap"]),
    ]),
    ("triangles", "Triangles", [
        _c("similarity_criteria", "Similarity of Triangles (AA, SSS, SAS)", "apply", 0.45),
        _c("bpt", "Basic Proportionality Theorem", "apply", 0.5, ["triangles.similarity_criteria"]),
        _c("pythagoras_theorem", "Pythagoras Theorem and Converse", "apply", 0.45, ["triangles.bpt"]),
    ]),
    ("coordinate_geometry", "Coordinate Geometry", [
        _c("distance_formula", "Distance Formula", "apply", 0.4),
        _c("section_formula", "Section Formula", "apply", 0.45, ["coordinate_geometry.distance_formula"]),
        _c("area_triangle_coord", "Area of Triangle (Coordinates)", "apply", 0.5, ["coordinate_geometry.section_formula"]),
    ]),
    ("trigonometry", "Introduction to Trigonometry", [
        _c("trig_ratios", "Trigonometric Ratios", "understand", 0.4),
        _c("trig_specific_angles", "Trig Ratios of Specific Angles", "apply", 0.45, ["trigonometry.trig_ratios"]),
        _c("trig_identities", "Trigonometric Identities", "apply", 0.5, ["trigonometry.trig_specific_angles"]),
    ]),
    ("trig_applications", "Some Applications of Trigonometry", [
        _c("heights_distances", "Heights and Distances", "apply", 0.5, ["trigonometry.trig_ratios"]),
    ]),
    ("circles", "Circles", [
        _c("tangent_circle", "Tangent to a Circle", "understand", 0.4),
        _c("tangent_theorems", "Number of Tangents from a Point", "apply", 0.5, ["circles.tangent_circle"]),
    ]),
    ("constructions", "Constructions", [
        _c("divide_segment", "Division of a Line Segment", "apply", 0.35),
        _c("tangent_construction", "Construction of Tangents to a Circle", "apply", 0.45, ["constructions.divide_segment"]),
    ]),
    ("areas_circles", "Areas Related to Circles", [
        _c("perimeter_area_circle", "Perimeter and Area of Circle", "apply", 0.35),
        _c("sector_segment", "Area of Sector and Segment", "apply", 0.45, ["areas_circles.perimeter_area_circle"]),
    ]),
    ("surface_area_volume", "Surface Areas and Volumes", [
        _c("combination_solids", "Surface Area of Combination of Solids", "apply", 0.45),
        _c("volume_combination", "Volume of Combination of Solids", "apply", 0.5, ["surface_area_volume.combination_solids"]),
        _c("frustum", "Frustum of a Cone", "apply", 0.5, ["surface_area_volume.volume_combination"]),
    ]),
    ("statistics", "Statistics", [
        _c("mean_grouped", "Mean of Grouped Data", "apply", 0.4),
        _c("median_grouped", "Median of Grouped Data", "apply", 0.45, ["statistics.mean_grouped"]),
        _c("mode_grouped", "Mode of Grouped Data", "apply", 0.4, ["statistics.mean_grouped"]),
        _c("ogive", "Cumulative Frequency and Ogives", "apply", 0.45, ["statistics.median_grouped"]),
    ]),
    ("probability", "Probability", [
        _c("theoretical_prob", "Theoretical Probability", "understand", 0.35),
        _c("prob_events", "Probability of Events (Complement, Impossible, Sure)", "apply", 0.4, ["probability.theoretical_prob"]),
    ]),
]

MATH11_CHAPTERS = [
    ("sets", "Sets", [
        _c("set_notation", "Set Notation and Representation", "remember", 0.2),
        _c("types_of_sets", "Types of Sets (Empty, Finite, Infinite, Equal)", "understand", 0.25, ["sets.set_notation"]),
        _c("venn_diagrams", "Venn Diagrams and Set Operations", "apply", 0.35, ["sets.types_of_sets"]),
    ]),
    ("relations_functions", "Relations and Functions", [
        _c("cartesian_product", "Cartesian Product of Sets", "understand", 0.3),
        _c("relations", "Relations — Domain, Codomain, Range", "understand", 0.35, ["relations_functions.cartesian_product"]),
        _c("functions", "Functions — Types and Graphs", "apply", 0.4, ["relations_functions.relations"]),
    ]),
    ("trig_functions", "Trigonometric Functions", [
        _c("angles_measurement", "Angles and Their Measurement (Degrees and Radians)", "understand", 0.3),
        _c("trig_all_angles", "Trigonometric Functions of Any Angle", "apply", 0.4, ["trig_functions.angles_measurement"]),
        _c("trig_identities", "Trigonometric Identities and Equations", "apply", 0.5, ["trig_functions.trig_all_angles"]),
    ]),
    ("induction", "Principle of Mathematical Induction", [
        _c("pmi", "Principle of Mathematical Induction", "apply", 0.5),
        _c("applications_pmi", "Applications of PMI", "apply", 0.55, ["induction.pmi"]),
    ]),
    ("complex_numbers", "Complex Numbers and Quadratic Equations", [
        _c("complex_intro", "Complex Numbers — Definition and Algebra", "understand", 0.4),
        _c("argand_plane", "Argand Plane and Modulus", "apply", 0.45, ["complex_numbers.complex_intro"]),
        _c("quadratic_complex", "Quadratic Equations with Complex Roots", "apply", 0.5, ["complex_numbers.argand_plane"]),
    ]),
    ("linear_inequalities", "Linear Inequalities", [
        _c("solving_inequalities", "Solving Linear Inequalities", "apply", 0.35),
        _c("graphical_solution", "Graphical Solution of Inequalities", "apply", 0.4, ["linear_inequalities.solving_inequalities"]),
        _c("system_inequalities", "System of Linear Inequalities", "apply", 0.45, ["linear_inequalities.graphical_solution"]),
    ]),
    ("permutations", "Permutations and Combinations", [
        _c("counting_principle", "Fundamental Principle of Counting", "understand", 0.35),
        _c("permutations", "Permutations", "apply", 0.45, ["permutations.counting_principle"]),
        _c("combinations", "Combinations", "apply", 0.45, ["permutations.permutations"]),
    ]),
    ("binomial", "Binomial Theorem", [
        _c("binomial_theorem", "Binomial Theorem for Positive Integers", "apply", 0.5),
        _c("general_term", "General and Middle Terms", "apply", 0.55, ["binomial.binomial_theorem"]),
    ]),
    ("sequences", "Sequences and Series", [
        _c("ap_gp", "Arithmetic and Geometric Progressions", "understand", 0.35),
        _c("sum_series", "Sum of n Terms — AP and GP", "apply", 0.45, ["sequences.ap_gp"]),
        _c("special_series", "Sum of Special Series", "apply", 0.5, ["sequences.sum_series"]),
    ]),
    ("straight_lines", "Straight Lines", [
        _c("slope", "Slope of a Line", "understand", 0.3),
        _c("forms_of_line", "Various Forms of Equation of a Line", "apply", 0.4, ["straight_lines.slope"]),
        _c("distance_line", "Distance of a Point from a Line", "apply", 0.45, ["straight_lines.forms_of_line"]),
    ]),
    ("conic_sections", "Conic Sections", [
        _c("circle_eq", "Equation of a Circle", "apply", 0.4),
        _c("parabola", "Parabola — Standard Equations", "apply", 0.45, ["conic_sections.circle_eq"]),
        _c("ellipse_hyperbola", "Ellipse and Hyperbola", "apply", 0.5, ["conic_sections.parabola"]),
    ]),
    ("three_d_intro", "Introduction to Three Dimensional Geometry", [
        _c("coordinate_axes_3d", "Coordinate Axes and Planes in 3D", "understand", 0.35),
        _c("distance_3d", "Distance Between Two Points in 3D", "apply", 0.4, ["three_d_intro.coordinate_axes_3d"]),
    ]),
    ("limits_derivatives", "Limits and Derivatives", [
        _c("limits", "Intuitive Idea of Limits", "understand", 0.4),
        _c("limit_algebra", "Algebra of Limits", "apply", 0.45, ["limits_derivatives.limits"]),
        _c("derivatives", "Derivatives — First Principles", "apply", 0.5, ["limits_derivatives.limit_algebra"]),
    ]),
    ("reasoning", "Mathematical Reasoning", [
        _c("statements", "Statements and Logical Connectives", "understand", 0.3),
        _c("validation", "Validating Statements — Contrapositive, Contradiction", "analyze", 0.45, ["reasoning.statements"]),
    ]),
    ("statistics", "Statistics", [
        _c("dispersion", "Measures of Dispersion", "apply", 0.4),
        _c("mean_deviation", "Mean Deviation", "apply", 0.4, ["statistics.dispersion"]),
        _c("variance_sd", "Variance and Standard Deviation", "apply", 0.5, ["statistics.mean_deviation"]),
    ]),
    ("probability", "Probability", [
        _c("random_experiments", "Random Experiments and Events", "understand", 0.35),
        _c("axiomatic_prob", "Axiomatic Approach to Probability", "apply", 0.45, ["probability.random_experiments"]),
    ]),
]

MATH12_CHAPTERS = [
    ("relations_functions", "Relations and Functions", [
        _c("types_relations", "Types of Relations (Reflexive, Symmetric, Transitive)", "understand", 0.4),
        _c("types_functions", "One-one, Onto and Bijective Functions", "apply", 0.45, ["relations_functions.types_relations"]),
        _c("composition", "Composition of Functions and Inverse", "apply", 0.5, ["relations_functions.types_functions"]),
    ]),
    ("inverse_trig", "Inverse Trigonometric Functions", [
        _c("basic_concepts", "Inverse Trig Functions — Domain and Range", "understand", 0.4),
        _c("properties", "Properties of Inverse Trig Functions", "apply", 0.5, ["inverse_trig.basic_concepts"]),
    ]),
    ("matrices", "Matrices", [
        _c("types_operations", "Types and Operations on Matrices", "understand", 0.35),
        _c("transpose_symmetric", "Transpose, Symmetric and Skew-Symmetric", "apply", 0.4, ["matrices.types_operations"]),
        _c("elementary_operations", "Elementary Operations and Invertible Matrices", "apply", 0.5, ["matrices.transpose_symmetric"]),
    ]),
    ("determinants", "Determinants", [
        _c("determinant_calc", "Determinant Calculation (2x2, 3x3)", "apply", 0.4),
        _c("properties_det", "Properties of Determinants", "apply", 0.45, ["determinants.determinant_calc"]),
        _c("cramers_rule", "Cramer's Rule and Inverse Using Determinants", "apply", 0.55, ["determinants.properties_det"]),
    ]),
    ("continuity", "Continuity and Differentiability", [
        _c("continuity", "Continuity of Functions", "understand", 0.4),
        _c("differentiability", "Differentiability", "apply", 0.45, ["continuity.continuity"]),
        _c("chain_rule", "Chain Rule, Implicit and Logarithmic Differentiation", "apply", 0.55, ["continuity.differentiability"]),
    ]),
    ("derivatives_app", "Application of Derivatives", [
        _c("rate_of_change", "Rate of Change of Quantities", "apply", 0.4),
        _c("tangents_normals", "Tangents and Normals", "apply", 0.45, ["derivatives_app.rate_of_change"]),
        _c("maxima_minima", "Maxima and Minima", "apply", 0.55, ["derivatives_app.tangents_normals"]),
    ]),
    ("integrals", "Integrals", [
        _c("indefinite", "Indefinite Integrals — Methods", "apply", 0.45),
        _c("definite", "Definite Integrals — Fundamental Theorem", "apply", 0.5, ["integrals.indefinite"]),
        _c("integration_methods", "Integration by Substitution, Parts, Partial Fractions", "apply", 0.55, ["integrals.definite"]),
    ]),
    ("integrals_app", "Application of Integrals", [
        _c("area_curves", "Area Under Curves", "apply", 0.5),
        _c("area_between", "Area Between Two Curves", "apply", 0.55, ["integrals_app.area_curves"]),
    ]),
    ("diff_equations", "Differential Equations", [
        _c("order_degree", "Order and Degree of Differential Equations", "understand", 0.4),
        _c("variable_separable", "Variable Separable Method", "apply", 0.5, ["diff_equations.order_degree"]),
        _c("homogeneous_linear", "Homogeneous and Linear Differential Equations", "apply", 0.55, ["diff_equations.variable_separable"]),
    ]),
    ("vectors", "Vector Algebra", [
        _c("vectors_intro", "Vectors — Types and Operations", "understand", 0.35),
        _c("scalar_product", "Scalar (Dot) Product", "apply", 0.4, ["vectors.vectors_intro"]),
        _c("cross_product", "Vector (Cross) Product", "apply", 0.45, ["vectors.scalar_product"]),
    ]),
    ("three_d", "Three Dimensional Geometry", [
        _c("direction_cosines", "Direction Cosines and Ratios", "understand", 0.4),
        _c("line_3d", "Equation of a Line in Space", "apply", 0.45, ["three_d.direction_cosines"]),
        _c("plane_3d", "Equation of a Plane", "apply", 0.5, ["three_d.line_3d"]),
    ]),
    ("linear_programming", "Linear Programming", [
        _c("formulation", "Formulation of LPP", "apply", 0.4),
        _c("graphical_method", "Graphical Method of Solving LPP", "apply", 0.5, ["linear_programming.formulation"]),
    ]),
    ("probability", "Probability", [
        _c("conditional", "Conditional Probability", "understand", 0.4),
        _c("bayes_theorem", "Bayes' Theorem", "apply", 0.5, ["probability.conditional"]),
        _c("random_variable", "Random Variable and Distributions", "apply", 0.55, ["probability.bayes_theorem"]),
    ]),
]

# ══════════════════════════════════════════════════════════════════════════════
#  SCIENCE  —  Classes 6-10
# ══════════════════════════════════════════════════════════════════════════════

SCIENCE6_CHAPTERS = [
    ("food", "Food: Where Does it Come From?", [
        _c("food_sources", "Sources of Food", "remember", 0.15),
        _c("food_materials", "Food Materials and Plant Parts", "understand", 0.2, ["food.food_sources"]),
        _c("herbivore_carnivore", "Herbivores, Carnivores and Omnivores", "understand", 0.2, ["food.food_sources"]),
    ]),
    ("components_food", "Components of Food", [
        _c("nutrients", "Nutrients — Carbohydrates, Proteins, Fats", "understand", 0.25),
        _c("vitamins_minerals", "Vitamins and Minerals", "understand", 0.25, ["components_food.nutrients"]),
        _c("balanced_diet", "Balanced Diet and Deficiency Diseases", "apply", 0.3, ["components_food.vitamins_minerals"]),
    ]),
    ("fibre_fabric", "Fibre to Fabric", [
        _c("fibres", "Plant and Animal Fibres", "understand", 0.2),
        _c("spinning_weaving", "Spinning, Weaving and Knitting", "understand", 0.25, ["fibre_fabric.fibres"]),
    ]),
    ("sorting_materials", "Sorting Materials into Groups", [
        _c("properties_materials", "Properties of Materials", "understand", 0.2),
        _c("grouping", "Grouping Materials by Properties", "apply", 0.25, ["sorting_materials.properties_materials"]),
    ]),
    ("separation", "Separation of Substances", [
        _c("methods", "Methods of Separation — Handpicking, Sieving, Filtration", "understand", 0.25),
        _c("evaporation_condensation", "Evaporation and Condensation", "apply", 0.3, ["separation.methods"]),
        _c("mixture_solution", "Mixtures and Solutions", "understand", 0.3, ["separation.methods"]),
    ]),
    ("changes", "Changes Around Us", [
        _c("reversible", "Reversible and Irreversible Changes", "understand", 0.2),
        _c("expand_contract", "Expansion and Contraction", "understand", 0.25, ["changes.reversible"]),
    ]),
    ("plants", "Getting to Know Plants", [
        _c("plant_parts", "Parts of a Plant — Root, Stem, Leaf, Flower", "remember", 0.15),
        _c("types_plants", "Herbs, Shrubs and Trees", "understand", 0.2),
        _c("flower_parts", "Parts of a Flower and Reproduction", "understand", 0.25, ["plants.plant_parts"]),
    ]),
    ("body_movements", "Body Movements", [
        _c("joints", "Types of Joints — Ball-Socket, Hinge, Pivot", "understand", 0.25),
        _c("movement_animals", "Movement in Different Animals", "understand", 0.25),
    ]),
    ("living_organisms", "The Living Organisms and Their Surroundings", [
        _c("habitat", "Habitat and Adaptation", "understand", 0.2),
        _c("biotic_abiotic", "Biotic and Abiotic Components", "understand", 0.25, ["living_organisms.habitat"]),
    ]),
    ("motion_measurement", "Motion and Measurement of Distances", [
        _c("standard_units", "Standard Units of Measurement", "remember", 0.2),
        _c("types_motion", "Types of Motion — Rectilinear, Circular, Periodic", "understand", 0.25, ["motion_measurement.standard_units"]),
    ]),
    ("light", "Light, Shadows and Reflections", [
        _c("transparent_opaque", "Transparent, Translucent and Opaque Objects", "understand", 0.2),
        _c("shadows", "Formation of Shadows", "apply", 0.25, ["light.transparent_opaque"]),
        _c("reflection_intro", "Introduction to Reflection", "understand", 0.3, ["light.shadows"]),
    ]),
    ("electricity", "Electricity and Circuits", [
        _c("electric_circuit", "Electric Circuit — Open and Closed", "understand", 0.25),
        _c("conductors_insulators", "Conductors and Insulators", "understand", 0.25, ["electricity.electric_circuit"]),
    ]),
    ("magnets", "Fun with Magnets", [
        _c("magnetic_nonmagnetic", "Magnetic and Non-Magnetic Materials", "understand", 0.2),
        _c("poles_attraction", "Poles of Magnet — Attraction and Repulsion", "understand", 0.25, ["magnets.magnetic_nonmagnetic"]),
    ]),
    ("water", "Water", [
        _c("water_cycle", "Water Cycle", "understand", 0.25),
        _c("conservation", "Conservation of Water", "apply", 0.25),
    ]),
    ("air", "Air Around Us", [
        _c("composition", "Composition of Air", "understand", 0.2),
        _c("importance_air", "Importance of Air for Living Organisms", "understand", 0.2),
    ]),
    ("garbage", "Garbage In, Garbage Out", [
        _c("waste_management", "Dealing with Garbage — Reduce, Reuse, Recycle", "understand", 0.2),
        _c("composting", "Composting and Vermicomposting", "apply", 0.25, ["garbage.waste_management"]),
    ]),
]

SCIENCE7_CHAPTERS = [
    ("nutrition_plants", "Nutrition in Plants", [
        _c("photosynthesis", "Photosynthesis", "understand", 0.3),
        _c("modes_nutrition", "Autotrophic and Heterotrophic Nutrition", "understand", 0.3),
        _c("symbiosis", "Symbiotic Relationships", "understand", 0.3, ["nutrition_plants.modes_nutrition"]),
    ]),
    ("nutrition_animals", "Nutrition in Animals", [
        _c("digestion_humans", "Human Digestive System", "understand", 0.3),
        _c("digestion_animals", "Digestion in Grass-Eating Animals", "understand", 0.3),
    ]),
    ("heat", "Heat", [
        _c("temperature", "Temperature and Thermometer", "understand", 0.25),
        _c("conduction_convection", "Conduction, Convection and Radiation", "understand", 0.35, ["heat.temperature"]),
    ]),
    ("acids_bases", "Acids, Bases and Salts", [
        _c("indicators", "Indicators — Litmus, Turmeric", "understand", 0.25),
        _c("neutralisation", "Neutralisation Reaction", "apply", 0.35, ["acids_bases.indicators"]),
    ]),
    ("physical_chemical", "Physical and Chemical Changes", [
        _c("physical_change", "Physical Changes", "understand", 0.2),
        _c("chemical_change", "Chemical Changes", "understand", 0.3, ["physical_chemical.physical_change"]),
        _c("rusting_crystallisation", "Rusting and Crystallisation", "apply", 0.3, ["physical_chemical.chemical_change"]),
    ]),
    ("weather", "Weather, Climate and Adaptations", [
        _c("weather_climate", "Weather vs Climate", "understand", 0.25),
        _c("adaptations", "Adaptations of Animals to Climate", "understand", 0.3, ["weather.weather_climate"]),
    ]),
    ("soil", "Soil", [
        _c("soil_profile", "Soil Profile and Types", "understand", 0.25),
        _c("soil_moisture", "Soil and Moisture Absorption", "apply", 0.3, ["soil.soil_profile"]),
    ]),
    ("respiration", "Respiration in Organisms", [
        _c("breathing", "Breathing and Respiration", "understand", 0.3),
        _c("aerobic_anaerobic", "Aerobic and Anaerobic Respiration", "understand", 0.35, ["respiration.breathing"]),
    ]),
    ("transport_plants_animals", "Transportation in Animals and Plants", [
        _c("circulatory", "Circulatory System — Blood, Heart", "understand", 0.35),
        _c("transport_plants", "Transport of Water and Nutrients in Plants", "understand", 0.3),
    ]),
    ("reproduction_plants", "Reproduction in Plants", [
        _c("asexual", "Vegetative Propagation, Budding, Fragmentation", "understand", 0.25),
        _c("sexual_plants", "Pollination and Fertilisation", "understand", 0.35, ["reproduction_plants.asexual"]),
    ]),
    ("motion_time", "Motion and Time", [
        _c("speed", "Speed and Its Measurement", "apply", 0.3),
        _c("distance_time_graph", "Distance-Time Graph", "apply", 0.35, ["motion_time.speed"]),
    ]),
    ("electric_current", "Electric Current and Its Effects", [
        _c("heating_effect", "Heating Effect of Electric Current", "understand", 0.3),
        _c("magnetic_effect", "Magnetic Effect of Current — Electromagnet", "understand", 0.35, ["electric_current.heating_effect"]),
    ]),
    ("light7", "Light", [
        _c("reflection_light", "Reflection of Light", "understand", 0.3),
        _c("dispersion", "Dispersion of Light — Spectrum", "understand", 0.35, ["light7.reflection_light"]),
    ]),
    ("water7", "Water: A Precious Resource", [
        _c("water_distribution", "Distribution of Water on Earth", "understand", 0.2),
        _c("water_management", "Water Management and Harvesting", "apply", 0.3, ["water7.water_distribution"]),
    ]),
    ("forests", "Forests: Our Lifeline", [
        _c("food_chains", "Food Chains and Food Webs", "understand", 0.3),
        _c("forest_ecosystem", "Forest as an Ecosystem", "understand", 0.3),
    ]),
]

SCIENCE8_CHAPTERS = [
    ("crop_production", "Crop Production and Management", [
        _c("agricultural_practices", "Agricultural Practices", "understand", 0.25),
        _c("crop_types", "Kharif and Rabi Crops", "remember", 0.2),
        _c("irrigation_methods", "Irrigation Methods", "understand", 0.3, ["crop_production.agricultural_practices"]),
    ]),
    ("microorganisms", "Microorganisms: Friend and Foe", [
        _c("types_microorganisms", "Types of Microorganisms", "understand", 0.25),
        _c("useful_harmful", "Useful and Harmful Microorganisms", "understand", 0.3, ["microorganisms.types_microorganisms"]),
        _c("food_preservation", "Food Preservation Methods", "apply", 0.3, ["microorganisms.useful_harmful"]),
    ]),
    ("synthetic_fibres", "Synthetic Fibres and Plastics", [
        _c("types_fibres", "Types of Synthetic Fibres — Rayon, Nylon, Polyester", "understand", 0.25),
        _c("plastics", "Plastics — Thermoplastic and Thermosetting", "understand", 0.3, ["synthetic_fibres.types_fibres"]),
    ]),
    ("metals_nonmetals", "Materials: Metals and Non-Metals", [
        _c("physical_properties", "Physical Properties of Metals and Non-Metals", "understand", 0.3),
        _c("chemical_properties", "Chemical Properties and Reactivity", "apply", 0.4, ["metals_nonmetals.physical_properties"]),
    ]),
    ("coal_petroleum", "Coal and Petroleum", [
        _c("fossil_fuels", "Fossil Fuels — Formation and Types", "understand", 0.25),
        _c("conservation_fuels", "Conservation of Fossil Fuels", "apply", 0.3, ["coal_petroleum.fossil_fuels"]),
    ]),
    ("combustion", "Combustion and Flame", [
        _c("combustion_types", "Types of Combustion", "understand", 0.25),
        _c("flame_structure", "Structure of Flame", "understand", 0.3, ["combustion.combustion_types"]),
    ]),
    ("conservation", "Conservation of Plants and Animals", [
        _c("biodiversity", "Biodiversity and Its Importance", "understand", 0.3),
        _c("endangered_species", "Endangered Species and Conservation", "apply", 0.35, ["conservation.biodiversity"]),
    ]),
    ("cell", "Cell: Structure and Functions", [
        _c("cell_intro", "Cell — Basic Unit of Life", "understand", 0.3),
        _c("plant_animal_cell", "Plant Cell vs Animal Cell", "understand", 0.35, ["cell.cell_intro"]),
        _c("cell_organelles", "Cell Organelles and Their Functions", "understand", 0.4, ["cell.plant_animal_cell"]),
    ]),
    ("reproduction_animals", "Reproduction in Animals", [
        _c("sexual_reproduction", "Sexual Reproduction — Fertilisation", "understand", 0.35),
        _c("asexual_reproduction", "Asexual Reproduction — Binary Fission, Budding", "understand", 0.3),
    ]),
    ("adolescence", "Reaching the Age of Adolescence", [
        _c("puberty", "Puberty and Changes in Body", "understand", 0.25),
        _c("hormones", "Hormones and Reproductive Health", "understand", 0.3, ["adolescence.puberty"]),
    ]),
    ("force_pressure", "Force and Pressure", [
        _c("types_forces", "Contact and Non-Contact Forces", "understand", 0.3),
        _c("pressure", "Pressure — Concept and Applications", "apply", 0.35, ["force_pressure.types_forces"]),
        _c("atmospheric_pressure", "Atmospheric and Liquid Pressure", "apply", 0.35, ["force_pressure.pressure"]),
    ]),
    ("friction", "Friction", [
        _c("types_friction", "Types of Friction — Static, Sliding, Rolling", "understand", 0.3),
        _c("friction_effects", "Increasing and Reducing Friction", "apply", 0.3, ["friction.types_friction"]),
    ]),
    ("sound", "Sound", [
        _c("vibration_sound", "Vibration and Production of Sound", "understand", 0.25),
        _c("propagation", "Propagation of Sound", "understand", 0.3, ["sound.vibration_sound"]),
        _c("loudness_pitch", "Loudness, Pitch and Frequency", "apply", 0.35, ["sound.propagation"]),
    ]),
    ("electric_effects", "Chemical Effects of Electric Current", [
        _c("conductors_liquids", "Conductivity of Liquids", "understand", 0.3),
        _c("electroplating", "Electroplating", "apply", 0.35, ["electric_effects.conductors_liquids"]),
    ]),
    ("natural_phenomena", "Some Natural Phenomena", [
        _c("lightning", "Lightning — Cause and Safety", "understand", 0.3),
        _c("earthquakes", "Earthquakes — Cause and Protection", "understand", 0.3),
    ]),
    ("light8", "Light", [
        _c("reflection_laws", "Laws of Reflection", "understand", 0.3),
        _c("human_eye", "Human Eye and Care", "understand", 0.3, ["light8.reflection_laws"]),
    ]),
    ("stars_solar", "Stars and the Solar System", [
        _c("celestial_bodies", "Moon, Stars, Planets", "understand", 0.2),
        _c("solar_system", "The Solar System", "understand", 0.25, ["stars_solar.celestial_bodies"]),
    ]),
    ("pollution", "Pollution of Air and Water", [
        _c("air_pollution", "Air Pollution — Causes and Effects", "understand", 0.25),
        _c("water_pollution", "Water Pollution and Purification", "apply", 0.3, ["pollution.air_pollution"]),
    ]),
]

SCIENCE9_CHAPTERS = [
    ("matter", "Matter in Our Surroundings", [
        _c("states_of_matter", "States of Matter and Their Properties", "understand", 0.3),
        _c("change_of_state", "Change of State — Melting, Boiling, Evaporation", "apply", 0.35, ["matter.states_of_matter"]),
    ]),
    ("pure_matter", "Is Matter Around Us Pure?", [
        _c("mixtures_solutions", "Mixtures, Solutions, Suspensions, Colloids", "understand", 0.3),
        _c("separation_techniques", "Separation Techniques — Chromatography, Distillation", "apply", 0.4, ["pure_matter.mixtures_solutions"]),
        _c("elements_compounds", "Elements, Compounds and Mixtures", "understand", 0.35, ["pure_matter.mixtures_solutions"]),
    ]),
    ("atoms_molecules", "Atoms and Molecules", [
        _c("laws_chemical", "Laws of Chemical Combination", "understand", 0.35),
        _c("atomic_mass", "Atomic Mass and Molecular Mass", "apply", 0.4, ["atoms_molecules.laws_chemical"]),
        _c("mole_concept", "Mole Concept", "apply", 0.5, ["atoms_molecules.atomic_mass"]),
    ]),
    ("atomic_structure", "Structure of the Atom", [
        _c("subatomic_particles", "Electrons, Protons and Neutrons", "understand", 0.3),
        _c("atomic_models", "Thomson's and Rutherford's Models", "understand", 0.35, ["atomic_structure.subatomic_particles"]),
        _c("bohr_model", "Bohr's Model and Electron Configuration", "apply", 0.4, ["atomic_structure.atomic_models"]),
    ]),
    ("cell_fundamental", "The Fundamental Unit of Life", [
        _c("cell_structure", "Cell Structure and Organelles", "understand", 0.35),
        _c("plant_animal_cell", "Plant and Animal Cell Differences", "understand", 0.3, ["cell_fundamental.cell_structure"]),
    ]),
    ("tissues", "Tissues", [
        _c("plant_tissues", "Plant Tissues — Meristematic and Permanent", "understand", 0.35),
        _c("animal_tissues", "Animal Tissues — Epithelial, Connective, Muscular, Nervous", "understand", 0.35),
    ]),
    ("diversity", "Diversity in Living Organisms", [
        _c("classification", "Basis of Classification", "understand", 0.3),
        _c("five_kingdoms", "Five Kingdom Classification", "understand", 0.35, ["diversity.classification"]),
    ]),
    ("motion", "Motion", [
        _c("distance_displacement", "Distance and Displacement", "understand", 0.3),
        _c("speed_velocity", "Speed, Velocity and Acceleration", "apply", 0.4, ["motion.distance_displacement"]),
        _c("equations_of_motion", "Equations of Motion", "apply", 0.5, ["motion.speed_velocity"]),
        _c("graphical_analysis", "Distance-Time and Velocity-Time Graphs", "analyze", 0.45, ["motion.speed_velocity"]),
    ]),
    ("force_laws", "Force and Laws of Motion", [
        _c("newtons_first", "Newton's First Law — Inertia", "understand", 0.35),
        _c("newtons_second", "Newton's Second Law — F=ma", "apply", 0.45, ["force_laws.newtons_first"]),
        _c("newtons_third", "Newton's Third Law — Action and Reaction", "apply", 0.4, ["force_laws.newtons_second"]),
        _c("momentum", "Momentum and Conservation of Momentum", "apply", 0.5, ["force_laws.newtons_second"]),
    ]),
    ("gravitation", "Gravitation", [
        _c("universal_gravitation", "Universal Law of Gravitation", "understand", 0.4),
        _c("free_fall", "Free Fall and Acceleration Due to Gravity", "apply", 0.45, ["gravitation.universal_gravitation"]),
        _c("mass_weight", "Mass and Weight", "apply", 0.35, ["gravitation.free_fall"]),
    ]),
    ("work_energy", "Work and Energy", [
        _c("work", "Work Done by a Force", "apply", 0.35),
        _c("kinetic_potential", "Kinetic and Potential Energy", "apply", 0.4, ["work_energy.work"]),
        _c("conservation_energy", "Law of Conservation of Energy", "apply", 0.45, ["work_energy.kinetic_potential"]),
    ]),
    ("sound9", "Sound", [
        _c("production_propagation", "Production and Propagation of Sound", "understand", 0.3),
        _c("characteristics", "Characteristics — Frequency, Amplitude, Speed", "apply", 0.35, ["sound9.production_propagation"]),
        _c("echo_resonance", "Echo, Reverberation and Resonance", "apply", 0.4, ["sound9.characteristics"]),
    ]),
    ("health", "Why Do We Fall Ill?", [
        _c("health_disease", "Health and Disease", "understand", 0.25),
        _c("infectious_diseases", "Infectious Diseases — Causes and Prevention", "understand", 0.3, ["health.health_disease"]),
    ]),
    ("natural_resources", "Natural Resources", [
        _c("biogeochemical_cycles", "Biogeochemical Cycles — Water, Carbon, Nitrogen", "understand", 0.35),
        _c("pollution_ozone", "Pollution and Ozone Layer", "understand", 0.3),
    ]),
    ("food_resources", "Improvement in Food Resources", [
        _c("crop_improvement", "Crop Improvement and Management", "understand", 0.3),
        _c("animal_husbandry", "Animal Husbandry", "understand", 0.3),
    ]),
]

SCIENCE10_CHAPTERS = [
    ("chemical_reactions", "Chemical Reactions and Equations", [
        _c("types_reactions", "Types of Chemical Reactions", "understand", 0.35),
        _c("balancing_equations", "Balancing Chemical Equations", "apply", 0.4, ["chemical_reactions.types_reactions"]),
        _c("oxidation_reduction", "Oxidation and Reduction", "apply", 0.45, ["chemical_reactions.balancing_equations"]),
    ]),
    ("acids_bases_salts", "Acids, Bases and Salts", [
        _c("indicators_ph", "Indicators and pH Scale", "understand", 0.35),
        _c("reactions_acids_bases", "Reactions of Acids and Bases", "apply", 0.4, ["acids_bases_salts.indicators_ph"]),
        _c("salts_preparation", "Preparation and Properties of Salts", "apply", 0.4, ["acids_bases_salts.reactions_acids_bases"]),
    ]),
    ("metals_nonmetals10", "Metals and Non-metals", [
        _c("properties10", "Physical and Chemical Properties", "understand", 0.35),
        _c("reactivity_series", "Reactivity Series", "apply", 0.4, ["metals_nonmetals10.properties10"]),
        _c("extraction_metals", "Extraction of Metals", "apply", 0.5, ["metals_nonmetals10.reactivity_series"]),
    ]),
    ("carbon_compounds", "Carbon and its Compounds", [
        _c("bonding_carbon", "Bonding in Carbon — Covalent Bond", "understand", 0.4),
        _c("hydrocarbons", "Saturated and Unsaturated Hydrocarbons", "understand", 0.4, ["carbon_compounds.bonding_carbon"]),
        _c("functional_groups", "Functional Groups and Nomenclature", "apply", 0.5, ["carbon_compounds.hydrocarbons"]),
    ]),
    ("periodic_table", "Periodic Classification of Elements", [
        _c("early_classification", "Early Attempts at Classification", "remember", 0.3),
        _c("modern_periodic", "Modern Periodic Table — Trends", "understand", 0.4, ["periodic_table.early_classification"]),
    ]),
    ("life_processes", "Life Processes", [
        _c("nutrition", "Nutrition — Autotrophic and Heterotrophic", "understand", 0.35),
        _c("respiration10", "Respiration", "understand", 0.35),
        _c("transportation", "Transportation in Animals and Plants", "understand", 0.35),
        _c("excretion", "Excretion in Organisms", "understand", 0.35),
    ]),
    ("control_coordination", "Control and Coordination", [
        _c("nervous_system", "Nervous System", "understand", 0.4),
        _c("hormones10", "Hormones in Animals and Plants", "understand", 0.4),
    ]),
    ("reproduction10", "How Do Organisms Reproduce?", [
        _c("asexual_modes", "Modes of Asexual Reproduction", "understand", 0.3),
        _c("sexual_reproduction10", "Sexual Reproduction in Organisms", "understand", 0.4, ["reproduction10.asexual_modes"]),
        _c("reproductive_health", "Reproductive Health and Contraception", "understand", 0.35, ["reproduction10.sexual_reproduction10"]),
    ]),
    ("heredity_evolution", "Heredity and Evolution", [
        _c("mendels_laws", "Mendel's Laws of Inheritance", "understand", 0.4),
        _c("sex_determination", "Sex Determination", "understand", 0.35, ["heredity_evolution.mendels_laws"]),
        _c("evolution", "Evolution — Evidence and Speciation", "understand", 0.45, ["heredity_evolution.mendels_laws"]),
    ]),
    ("light_reflection", "Light — Reflection and Refraction", [
        _c("reflection_mirrors", "Reflection from Spherical Mirrors", "apply", 0.4),
        _c("refraction", "Refraction of Light through Glass Slab", "apply", 0.4, ["light_reflection.reflection_mirrors"]),
        _c("lenses", "Image Formation by Lenses", "apply", 0.45, ["light_reflection.refraction"]),
    ]),
    ("human_eye", "The Human Eye and the Colourful World", [
        _c("eye_structure", "Structure and Working of Human Eye", "understand", 0.35),
        _c("defects_correction", "Defects of Vision and Correction", "apply", 0.4, ["human_eye.eye_structure"]),
        _c("scattering_dispersion", "Scattering and Dispersion of Light", "understand", 0.35, ["human_eye.eye_structure"]),
    ]),
    ("electricity10", "Electricity", [
        _c("ohms_law", "Ohm's Law", "apply", 0.4),
        _c("resistance", "Resistance — Series and Parallel", "apply", 0.45, ["electricity10.ohms_law"]),
        _c("electric_power", "Electric Power and Energy", "apply", 0.45, ["electricity10.resistance"]),
    ]),
    ("magnetic_effects", "Magnetic Effects of Electric Current", [
        _c("magnetic_field", "Magnetic Field and Field Lines", "understand", 0.35),
        _c("electromagnetic", "Electromagnetic Induction", "apply", 0.45, ["magnetic_effects.magnetic_field"]),
    ]),
    ("sources_energy", "Sources of Energy", [
        _c("conventional", "Conventional Sources — Fossil Fuels, Thermal, Hydro", "understand", 0.3),
        _c("non_conventional", "Non-Conventional — Solar, Wind, Nuclear, Biomass", "understand", 0.3),
    ]),
    ("environment", "Our Environment", [
        _c("ecosystem_components", "Ecosystem Components and Food Chains", "understand", 0.3),
        _c("ozone_depletion", "Ozone Layer Depletion", "understand", 0.3),
    ]),
]

# ══════════════════════════════════════════════════════════════════════════════
#  PHYSICS  —  Classes 11-12
# ══════════════════════════════════════════════════════════════════════════════

PHYSICS11_CHAPTERS = [
    ("units", "Units and Measurements", [
        _c("si_units", "SI Units and Dimensions", "remember", 0.25),
        _c("dimensional_analysis", "Dimensional Analysis", "apply", 0.4, ["units.si_units"]),
        _c("significant_figures", "Significant Figures and Errors", "apply", 0.35, ["units.si_units"]),
    ]),
    ("straight_line_motion", "Motion in a Straight Line", [
        _c("kinematics_1d", "Position, Velocity, Acceleration", "understand", 0.35),
        _c("equations_motion", "Kinematic Equations", "apply", 0.4, ["straight_line_motion.kinematics_1d"]),
        _c("free_fall", "Free Fall", "apply", 0.4, ["straight_line_motion.equations_motion"]),
    ]),
    ("motion_plane", "Motion in a Plane", [
        _c("vectors", "Vectors — Addition, Resolution", "apply", 0.4),
        _c("projectile", "Projectile Motion", "apply", 0.5, ["motion_plane.vectors"]),
        _c("circular_motion", "Uniform Circular Motion", "apply", 0.5, ["motion_plane.vectors"]),
    ]),
    ("laws_motion", "Laws of Motion", [
        _c("newtons_laws", "Newton's Laws of Motion", "apply", 0.4),
        _c("friction", "Friction — Static and Kinetic", "apply", 0.4, ["laws_motion.newtons_laws"]),
        _c("circular_dynamics", "Circular Motion Dynamics", "apply", 0.5, ["laws_motion.newtons_laws", "motion_plane.circular_motion"]),
    ]),
    ("work_energy_power", "Work, Energy and Power", [
        _c("work_ke_theorem", "Work-Energy Theorem", "apply", 0.4),
        _c("conservation_energy", "Conservation of Mechanical Energy", "apply", 0.45, ["work_energy_power.work_ke_theorem"]),
        _c("power_collisions", "Power and Collisions", "apply", 0.5, ["work_energy_power.conservation_energy"]),
    ]),
    ("rotational_motion", "System of Particles and Rotational Motion", [
        _c("centre_of_mass", "Centre of Mass", "apply", 0.45),
        _c("moment_of_inertia", "Moment of Inertia", "apply", 0.5, ["rotational_motion.centre_of_mass"]),
        _c("angular_momentum", "Angular Momentum and Torque", "apply", 0.55, ["rotational_motion.moment_of_inertia"]),
    ]),
    ("gravitation", "Gravitation", [
        _c("gravitational_law", "Newton's Law of Gravitation", "understand", 0.4),
        _c("gravitational_field", "Gravitational Field, Potential Energy", "apply", 0.45, ["gravitation.gravitational_law"]),
        _c("orbital_motion", "Orbital Motion and Satellites", "apply", 0.5, ["gravitation.gravitational_field"]),
    ]),
    ("mech_solids", "Mechanical Properties of Solids", [
        _c("stress_strain", "Stress and Strain", "understand", 0.4),
        _c("elastic_moduli", "Elastic Moduli — Young's, Bulk, Shear", "apply", 0.45, ["mech_solids.stress_strain"]),
    ]),
    ("mech_fluids", "Mechanical Properties of Fluids", [
        _c("pressure_pascals", "Pressure and Pascal's Law", "apply", 0.35),
        _c("bernoulli", "Bernoulli's Principle", "apply", 0.5, ["mech_fluids.pressure_pascals"]),
        _c("viscosity_surface", "Viscosity and Surface Tension", "apply", 0.45, ["mech_fluids.pressure_pascals"]),
    ]),
    ("thermal", "Thermal Properties of Matter", [
        _c("heat_temperature", "Heat, Temperature and Thermal Expansion", "understand", 0.3),
        _c("calorimetry", "Calorimetry and Specific Heat", "apply", 0.4, ["thermal.heat_temperature"]),
        _c("heat_transfer", "Conduction, Convection and Radiation", "apply", 0.4, ["thermal.calorimetry"]),
    ]),
    ("thermodynamics", "Thermodynamics", [
        _c("first_law", "First Law of Thermodynamics", "apply", 0.45),
        _c("second_law", "Second Law and Entropy", "apply", 0.5, ["thermodynamics.first_law"]),
        _c("heat_engines", "Heat Engines and Carnot Cycle", "apply", 0.55, ["thermodynamics.second_law"]),
    ]),
    ("kinetic_theory", "Kinetic Theory", [
        _c("gas_laws", "Ideal Gas Laws", "apply", 0.4),
        _c("kinetic_interpretation", "Kinetic Interpretation of Temperature", "analyze", 0.5, ["kinetic_theory.gas_laws"]),
    ]),
    ("oscillations", "Oscillations", [
        _c("shm", "Simple Harmonic Motion", "apply", 0.45),
        _c("energy_shm", "Energy in SHM", "apply", 0.5, ["oscillations.shm"]),
        _c("damped_forced", "Damped and Forced Oscillations", "analyze", 0.55, ["oscillations.energy_shm"]),
    ]),
    ("waves", "Waves", [
        _c("wave_types", "Transverse and Longitudinal Waves", "understand", 0.35),
        _c("wave_equation", "Wave Equation and Speed", "apply", 0.45, ["waves.wave_types"]),
        _c("superposition", "Superposition, Standing Waves and Beats", "apply", 0.5, ["waves.wave_equation"]),
    ]),
]

PHYSICS12_CHAPTERS = [
    ("electric_charges", "Electric Charges and Fields", [
        _c("coulombs_law", "Coulomb's Law", "apply", 0.4),
        _c("electric_field", "Electric Field and Field Lines", "apply", 0.45, ["electric_charges.coulombs_law"]),
        _c("gauss_law", "Gauss's Law and Applications", "apply", 0.55, ["electric_charges.electric_field"]),
    ]),
    ("electrostatic_potential", "Electrostatic Potential and Capacitance", [
        _c("potential", "Electric Potential and Potential Difference", "apply", 0.4),
        _c("capacitance", "Capacitors and Capacitance", "apply", 0.45, ["electrostatic_potential.potential"]),
        _c("energy_stored", "Energy Stored in Capacitor", "apply", 0.5, ["electrostatic_potential.capacitance"]),
    ]),
    ("current_electricity", "Current Electricity", [
        _c("ohms_law12", "Ohm's Law and Resistivity", "apply", 0.35),
        _c("kirchhoffs", "Kirchhoff's Laws", "apply", 0.5, ["current_electricity.ohms_law12"]),
        _c("wheatstone", "Wheatstone Bridge and Potentiometer", "apply", 0.55, ["current_electricity.kirchhoffs"]),
    ]),
    ("magnetism_current", "Moving Charges and Magnetism", [
        _c("lorentz_force", "Lorentz Force and Motion in Magnetic Field", "apply", 0.45),
        _c("biot_savart", "Biot-Savart Law", "apply", 0.5, ["magnetism_current.lorentz_force"]),
        _c("amperes_law", "Ampere's Circuital Law and Solenoid", "apply", 0.55, ["magnetism_current.biot_savart"]),
    ]),
    ("magnetism_matter", "Magnetism and Matter", [
        _c("bar_magnet", "Bar Magnet as Equivalent Solenoid", "understand", 0.4),
        _c("magnetic_materials", "Dia-, Para- and Ferromagnetic Materials", "understand", 0.4, ["magnetism_matter.bar_magnet"]),
    ]),
    ("em_induction", "Electromagnetic Induction", [
        _c("faradays_law", "Faraday's Law of Electromagnetic Induction", "apply", 0.45),
        _c("lenz_law", "Lenz's Law and Eddy Currents", "apply", 0.5, ["em_induction.faradays_law"]),
        _c("self_mutual", "Self and Mutual Inductance", "apply", 0.55, ["em_induction.lenz_law"]),
    ]),
    ("ac", "Alternating Current", [
        _c("ac_circuits", "AC Voltage and LCR Circuits", "apply", 0.5),
        _c("resonance", "Resonance and Power in AC Circuits", "apply", 0.55, ["ac.ac_circuits"]),
        _c("transformers", "Transformers", "apply", 0.45, ["ac.ac_circuits"]),
    ]),
    ("em_waves", "Electromagnetic Waves", [
        _c("em_spectrum", "Electromagnetic Spectrum", "understand", 0.35),
        _c("properties_em", "Properties of EM Waves", "understand", 0.4, ["em_waves.em_spectrum"]),
    ]),
    ("ray_optics", "Ray Optics and Optical Instruments", [
        _c("reflection_refraction", "Reflection and Refraction at Surfaces", "apply", 0.4),
        _c("prism_tir", "Prism and Total Internal Reflection", "apply", 0.45, ["ray_optics.reflection_refraction"]),
        _c("optical_instruments", "Microscope and Telescope", "apply", 0.5, ["ray_optics.prism_tir"]),
    ]),
    ("wave_optics", "Wave Optics", [
        _c("interference", "Young's Double Slit — Interference", "apply", 0.5),
        _c("diffraction", "Diffraction of Light", "apply", 0.5, ["wave_optics.interference"]),
        _c("polarisation", "Polarisation", "apply", 0.5, ["wave_optics.diffraction"]),
    ]),
    ("dual_nature", "Dual Nature of Radiation and Matter", [
        _c("photoelectric", "Photoelectric Effect", "apply", 0.45),
        _c("de_broglie", "de Broglie Wavelength", "apply", 0.5, ["dual_nature.photoelectric"]),
    ]),
    ("atoms", "Atoms", [
        _c("atomic_models12", "Rutherford and Bohr Models", "understand", 0.4),
        _c("hydrogen_spectrum", "Hydrogen Spectrum and Energy Levels", "apply", 0.5, ["atoms.atomic_models12"]),
    ]),
    ("nuclei", "Nuclei", [
        _c("nuclear_properties", "Nuclear Size, Mass, Binding Energy", "understand", 0.4),
        _c("radioactivity", "Radioactivity — Alpha, Beta, Gamma Decay", "understand", 0.45, ["nuclei.nuclear_properties"]),
        _c("fission_fusion", "Nuclear Fission and Fusion", "apply", 0.5, ["nuclei.radioactivity"]),
    ]),
    ("semiconductors", "Semiconductor Electronics", [
        _c("pn_junction", "p-n Junction Diode", "understand", 0.4),
        _c("transistor", "Transistor as Switch and Amplifier", "apply", 0.5, ["semiconductors.pn_junction"]),
        _c("logic_gates", "Logic Gates — AND, OR, NOT, NAND, NOR", "apply", 0.45, ["semiconductors.transistor"]),
    ]),
]

# ══════════════════════════════════════════════════════════════════════════════
#  CHEMISTRY  —  Classes 11-12
# ══════════════════════════════════════════════════════════════════════════════

CHEMISTRY11_CHAPTERS = [
    ("basic_concepts", "Some Basic Concepts of Chemistry", [
        _c("mole_concept", "Mole Concept and Molar Mass", "apply", 0.4),
        _c("stoichiometry", "Stoichiometry and Limiting Reagent", "apply", 0.45, ["basic_concepts.mole_concept"]),
    ]),
    ("atomic_structure", "Structure of Atom", [
        _c("quantum_numbers", "Quantum Numbers and Orbitals", "understand", 0.4),
        _c("electron_config", "Electron Configuration and Aufbau Principle", "apply", 0.45, ["atomic_structure.quantum_numbers"]),
    ]),
    ("classification", "Classification of Elements and Periodicity", [
        _c("periodic_table", "Modern Periodic Table", "understand", 0.35),
        _c("periodic_trends", "Periodic Trends — Ionization Energy, Electronegativity", "apply", 0.4, ["classification.periodic_table"]),
    ]),
    ("chemical_bonding", "Chemical Bonding and Molecular Structure", [
        _c("ionic_covalent", "Ionic and Covalent Bonding", "understand", 0.35),
        _c("vsepr", "VSEPR Theory and Molecular Geometry", "apply", 0.5, ["chemical_bonding.ionic_covalent"]),
        _c("hybridisation", "Hybridisation and MO Theory", "apply", 0.55, ["chemical_bonding.vsepr"]),
    ]),
    ("states_matter", "States of Matter", [
        _c("gas_laws_chem", "Gas Laws — Boyle's, Charles's, Ideal Gas", "apply", 0.4),
        _c("intermolecular", "Intermolecular Forces and Liquefaction", "understand", 0.4, ["states_matter.gas_laws_chem"]),
    ]),
    ("thermodynamics_chem", "Thermodynamics", [
        _c("enthalpy", "Enthalpy and Hess's Law", "apply", 0.45),
        _c("gibbs_energy", "Gibbs Free Energy and Spontaneity", "apply", 0.55, ["thermodynamics_chem.enthalpy"]),
    ]),
    ("equilibrium", "Equilibrium", [
        _c("chemical_equilibrium", "Chemical Equilibrium and Le Chatelier's Principle", "apply", 0.45),
        _c("ionic_equilibrium", "Ionic Equilibrium — pH, Buffers, Solubility", "apply", 0.5, ["equilibrium.chemical_equilibrium"]),
    ]),
    ("redox", "Redox Reactions", [
        _c("oxidation_numbers", "Oxidation Number Method", "apply", 0.4),
        _c("balancing_redox", "Balancing Redox Reactions", "apply", 0.45, ["redox.oxidation_numbers"]),
    ]),
    ("hydrogen", "Hydrogen", [
        _c("hydrogen_properties", "Properties and Preparation of Hydrogen", "understand", 0.3),
        _c("water_chemistry", "Water — Hard and Soft, Heavy Water", "understand", 0.3),
    ]),
    ("s_block", "The s-Block Elements", [
        _c("alkali_metals", "Alkali Metals — Properties and Compounds", "understand", 0.35),
        _c("alkaline_earth", "Alkaline Earth Metals", "understand", 0.35),
    ]),
    ("p_block_11", "Some p-Block Elements", [
        _c("group_13", "Group 13 Elements — Boron Family", "understand", 0.35),
        _c("group_14", "Group 14 Elements — Carbon Family", "understand", 0.35),
    ]),
    ("organic_basics", "Organic Chemistry — Some Basic Principles", [
        _c("iupac", "IUPAC Nomenclature", "apply", 0.4),
        _c("isomerism", "Isomerism — Structural and Stereoisomerism", "apply", 0.45, ["organic_basics.iupac"]),
        _c("reaction_mechanisms", "Reaction Mechanisms — SN1, SN2, E1, E2", "apply", 0.55, ["organic_basics.isomerism"]),
    ]),
    ("hydrocarbons", "Hydrocarbons", [
        _c("alkanes", "Alkanes — Properties and Reactions", "understand", 0.35),
        _c("alkenes_alkynes", "Alkenes and Alkynes", "understand", 0.4, ["hydrocarbons.alkanes"]),
        _c("aromatic", "Aromatic Hydrocarbons — Benzene", "understand", 0.45, ["hydrocarbons.alkenes_alkynes"]),
    ]),
    ("environmental", "Environmental Chemistry", [
        _c("pollution_chem", "Air, Water and Soil Pollution", "understand", 0.3),
        _c("green_chemistry", "Green Chemistry", "understand", 0.3),
    ]),
]

CHEMISTRY12_CHAPTERS = [
    ("solid_state", "The Solid State", [
        _c("crystal_lattice", "Crystal Lattice and Unit Cell", "understand", 0.4),
        _c("packing_defects", "Packing Efficiency and Crystal Defects", "apply", 0.5, ["solid_state.crystal_lattice"]),
    ]),
    ("solutions", "Solutions", [
        _c("concentration", "Concentration Terms — Molarity, Molality, Mole Fraction", "apply", 0.4),
        _c("colligative", "Colligative Properties", "apply", 0.5, ["solutions.concentration"]),
    ]),
    ("electrochemistry", "Electrochemistry", [
        _c("galvanic_cell", "Galvanic Cells and EMF", "apply", 0.45),
        _c("nernst_equation", "Nernst Equation", "apply", 0.5, ["electrochemistry.galvanic_cell"]),
        _c("electrolysis", "Electrolysis and Faraday's Laws", "apply", 0.5, ["electrochemistry.nernst_equation"]),
    ]),
    ("chemical_kinetics", "Chemical Kinetics", [
        _c("rate_law", "Rate of Reaction and Rate Law", "apply", 0.45),
        _c("order_molecularity", "Order, Molecularity and Integrated Rate Equations", "apply", 0.5, ["chemical_kinetics.rate_law"]),
    ]),
    ("surface_chemistry", "Surface Chemistry", [
        _c("adsorption", "Adsorption — Physical and Chemical", "understand", 0.35),
        _c("colloids", "Colloids — Types and Properties", "understand", 0.4, ["surface_chemistry.adsorption"]),
    ]),
    ("isolation", "General Principles of Isolation of Elements", [
        _c("metallurgy", "Metallurgical Processes", "understand", 0.4),
        _c("refining", "Refining of Metals", "understand", 0.4, ["isolation.metallurgy"]),
    ]),
    ("p_block_12", "The p-Block Elements", [
        _c("group_15", "Group 15 — Nitrogen Family", "understand", 0.4),
        _c("group_16", "Group 16 — Oxygen Family", "understand", 0.4),
        _c("group_17_18", "Group 17 (Halogens) and Group 18 (Noble Gases)", "understand", 0.4),
    ]),
    ("d_f_block", "The d- and f-Block Elements", [
        _c("transition_metals", "Transition Metals — Properties and Trends", "understand", 0.4),
        _c("lanthanoids_actinoids", "Lanthanoids and Actinoids", "understand", 0.4),
    ]),
    ("coordination", "Coordination Compounds", [
        _c("nomenclature_coord", "Nomenclature of Coordination Compounds", "apply", 0.4),
        _c("isomerism_coord", "Isomerism in Coordination Compounds", "apply", 0.45, ["coordination.nomenclature_coord"]),
        _c("bonding_coord", "Bonding — VBT and CFT", "apply", 0.55, ["coordination.isomerism_coord"]),
    ]),
    ("haloalkanes", "Haloalkanes and Haloarenes", [
        _c("preparation_haloalkanes", "Preparation and Properties", "understand", 0.4),
        _c("reactions_haloalkanes", "SN1, SN2, Elimination Reactions", "apply", 0.5, ["haloalkanes.preparation_haloalkanes"]),
    ]),
    ("alcohols", "Alcohols, Phenols and Ethers", [
        _c("preparation_alcohols", "Preparation and Physical Properties", "understand", 0.4),
        _c("reactions_alcohols", "Chemical Reactions of Alcohols and Phenols", "apply", 0.45, ["alcohols.preparation_alcohols"]),
    ]),
    ("aldehydes_ketones", "Aldehydes, Ketones and Carboxylic Acids", [
        _c("preparation_carbonyl", "Preparation of Aldehydes and Ketones", "understand", 0.4),
        _c("nucleophilic_addition", "Nucleophilic Addition Reactions", "apply", 0.5, ["aldehydes_ketones.preparation_carbonyl"]),
        _c("carboxylic_acids", "Carboxylic Acids — Properties and Reactions", "apply", 0.45, ["aldehydes_ketones.nucleophilic_addition"]),
    ]),
    ("amines", "Amines", [
        _c("classification_amines", "Classification and Preparation", "understand", 0.4),
        _c("reactions_amines", "Chemical Reactions of Amines", "apply", 0.45, ["amines.classification_amines"]),
    ]),
    ("biomolecules", "Biomolecules", [
        _c("carbohydrates", "Carbohydrates — Mono, Di, Polysaccharides", "understand", 0.35),
        _c("proteins_nucleic", "Proteins, Enzymes and Nucleic Acids", "understand", 0.4, ["biomolecules.carbohydrates"]),
    ]),
    ("polymers", "Polymers", [
        _c("classification_polymers", "Classification of Polymers", "understand", 0.3),
        _c("important_polymers", "Important Polymers — Nylon, Bakelite, Rubber", "understand", 0.35),
    ]),
]

# ══════════════════════════════════════════════════════════════════════════════
#  BIOLOGY  —  Classes 11-12
# ══════════════════════════════════════════════════════════════════════════════

BIOLOGY11_CHAPTERS = [
    ("living_world", "The Living World", [
        _c("diversity", "Diversity in the Living World", "understand", 0.2),
        _c("taxonomy", "Taxonomical Hierarchy", "remember", 0.25, ["living_world.diversity"]),
    ]),
    ("biological_classification", "Biological Classification", [
        _c("five_kingdoms", "Five Kingdom Classification", "understand", 0.3),
        _c("kingdom_details", "Monera, Protista, Fungi, Plantae, Animalia", "understand", 0.35, ["biological_classification.five_kingdoms"]),
    ]),
    ("plant_kingdom", "Plant Kingdom", [
        _c("algae_bryophytes", "Algae, Bryophytes, Pteridophytes", "understand", 0.3),
        _c("gymnosperms_angiosperms", "Gymnosperms and Angiosperms", "understand", 0.35, ["plant_kingdom.algae_bryophytes"]),
        _c("life_cycles", "Life Cycles and Alternation of Generations", "understand", 0.4, ["plant_kingdom.gymnosperms_angiosperms"]),
    ]),
    ("animal_kingdom", "Animal Kingdom", [
        _c("classification_basis", "Basis of Classification — Symmetry, Germ Layers", "understand", 0.3),
        _c("invertebrates", "Phyla — Porifera to Echinodermata", "understand", 0.35, ["animal_kingdom.classification_basis"]),
        _c("chordates", "Chordata — Fish to Mammals", "understand", 0.35, ["animal_kingdom.invertebrates"]),
    ]),
    ("morphology_plants", "Morphology of Flowering Plants", [
        _c("root_stem_leaf", "Root, Stem and Leaf Modifications", "understand", 0.3),
        _c("flower_fruit_seed", "Flower, Fruit and Seed", "understand", 0.3),
    ]),
    ("anatomy_plants", "Anatomy of Flowering Plants", [
        _c("tissue_system", "Tissue System — Epidermal, Ground, Vascular", "understand", 0.35),
        _c("internal_structure", "Internal Structure of Dicot and Monocot", "understand", 0.4, ["anatomy_plants.tissue_system"]),
    ]),
    ("cell_unit", "Cell: The Unit of Life", [
        _c("cell_theory", "Cell Theory and Cell Types", "understand", 0.3),
        _c("cell_organelles11", "Cell Organelles — Nucleus, Mitochondria, ER", "understand", 0.4, ["cell_unit.cell_theory"]),
    ]),
    ("biomolecules11", "Biomolecules", [
        _c("carbs_proteins", "Carbohydrates, Proteins, Lipids", "understand", 0.35),
        _c("enzymes", "Enzymes — Structure and Mechanism", "apply", 0.45, ["biomolecules11.carbs_proteins"]),
    ]),
    ("cell_cycle", "Cell Cycle and Cell Division", [
        _c("mitosis", "Mitosis — Stages and Significance", "understand", 0.35),
        _c("meiosis", "Meiosis — Stages and Significance", "understand", 0.4, ["cell_cycle.mitosis"]),
    ]),
    ("transport_plants", "Transport in Plants", [
        _c("water_transport", "Water Transport — Root Pressure, Transpiration Pull", "understand", 0.35),
        _c("mineral_transport", "Mineral and Food Transport — Phloem", "understand", 0.35),
    ]),
    ("photosynthesis", "Photosynthesis in Higher Plants", [
        _c("light_reactions", "Light Reactions", "understand", 0.4),
        _c("calvin_cycle", "Calvin Cycle (Dark Reactions)", "understand", 0.45, ["photosynthesis.light_reactions"]),
        _c("c3_c4_cam", "C3, C4 and CAM Pathways", "analyze", 0.5, ["photosynthesis.calvin_cycle"]),
    ]),
    ("respiration_plants", "Respiration in Plants", [
        _c("glycolysis", "Glycolysis", "understand", 0.4),
        _c("krebs_etc", "Krebs Cycle and Electron Transport Chain", "understand", 0.5, ["respiration_plants.glycolysis"]),
    ]),
    ("plant_growth", "Plant Growth and Development", [
        _c("growth_phases", "Phases of Growth", "understand", 0.3),
        _c("plant_hormones", "Plant Hormones — Auxin, Gibberellin, Cytokinin", "understand", 0.4, ["plant_growth.growth_phases"]),
    ]),
    ("digestion", "Digestion and Absorption", [
        _c("digestive_system", "Human Digestive System", "understand", 0.35),
        _c("digestion_absorption", "Digestion and Absorption of Nutrients", "understand", 0.4, ["digestion.digestive_system"]),
    ]),
    ("breathing", "Breathing and Exchange of Gases", [
        _c("respiratory_system", "Human Respiratory System", "understand", 0.35),
        _c("gas_exchange", "Exchange and Transport of Gases", "apply", 0.4, ["breathing.respiratory_system"]),
    ]),
    ("circulation", "Body Fluids and Circulation", [
        _c("blood_composition", "Blood — Components and Functions", "understand", 0.35),
        _c("heart_circulation", "Heart and Circulatory System", "understand", 0.4, ["circulation.blood_composition"]),
    ]),
    ("excretion", "Excretory Products and Their Elimination", [
        _c("nephron", "Nephron — Structure and Urine Formation", "understand", 0.4),
        _c("regulation", "Regulation of Kidney Function", "apply", 0.45, ["excretion.nephron"]),
    ]),
    ("locomotion", "Locomotion and Movement", [
        _c("skeletal_system", "Skeletal System — Types of Joints", "understand", 0.3),
        _c("muscular_system", "Muscular System — Mechanism of Contraction", "understand", 0.4, ["locomotion.skeletal_system"]),
    ]),
    ("neural_control", "Neural Control and Coordination", [
        _c("neuron_impulse", "Neuron and Nerve Impulse", "understand", 0.4),
        _c("brain_cns", "Central Nervous System — Brain and Spinal Cord", "understand", 0.4, ["neural_control.neuron_impulse"]),
    ]),
    ("chemical_coordination", "Chemical Coordination and Integration", [
        _c("endocrine_glands", "Endocrine Glands and Hormones", "understand", 0.35),
        _c("hormonal_regulation", "Hormonal Regulation and Disorders", "apply", 0.4, ["chemical_coordination.endocrine_glands"]),
    ]),
]

BIOLOGY12_CHAPTERS = [
    ("reproduction_organisms", "Reproduction in Organisms", [
        _c("asexual_types", "Asexual Reproduction — Types", "understand", 0.25),
        _c("sexual_events", "Sexual Reproduction — Events", "understand", 0.35, ["reproduction_organisms.asexual_types"]),
    ]),
    ("sexual_reproduction_plants", "Sexual Reproduction in Flowering Plants", [
        _c("flower_structure", "Flower Structure and Microsporogenesis", "understand", 0.35),
        _c("pollination_fertilisation", "Pollination and Fertilisation", "understand", 0.4, ["sexual_reproduction_plants.flower_structure"]),
        _c("endosperm_embryo", "Endosperm and Embryo Development", "understand", 0.4, ["sexual_reproduction_plants.pollination_fertilisation"]),
    ]),
    ("human_reproduction", "Human Reproduction", [
        _c("reproductive_system", "Male and Female Reproductive System", "understand", 0.35),
        _c("gametogenesis", "Gametogenesis and Menstrual Cycle", "understand", 0.4, ["human_reproduction.reproductive_system"]),
        _c("fertilisation_dev", "Fertilisation, Implantation and Embryonic Development", "understand", 0.45, ["human_reproduction.gametogenesis"]),
    ]),
    ("reproductive_health", "Reproductive Health", [
        _c("rh_problems", "Reproductive Health Problems", "understand", 0.3),
        _c("contraception", "Contraception and ART", "understand", 0.35, ["reproductive_health.rh_problems"]),
    ]),
    ("inheritance", "Principles of Inheritance and Variation", [
        _c("mendels_laws12", "Mendel's Laws of Inheritance", "understand", 0.35),
        _c("linkage_crossing", "Linkage and Crossing Over", "apply", 0.45, ["inheritance.mendels_laws12"]),
        _c("sex_linked", "Sex-Linked Inheritance and Genetic Disorders", "apply", 0.45, ["inheritance.linkage_crossing"]),
    ]),
    ("molecular_inheritance", "Molecular Basis of Inheritance", [
        _c("dna_structure", "DNA Structure and Replication", "understand", 0.4),
        _c("transcription_translation", "Transcription and Translation", "apply", 0.5, ["molecular_inheritance.dna_structure"]),
        _c("regulation_expression", "Regulation of Gene Expression", "analyze", 0.55, ["molecular_inheritance.transcription_translation"]),
    ]),
    ("evolution", "Evolution", [
        _c("origin_life", "Origin of Life — Theories", "understand", 0.3),
        _c("mechanisms_evolution", "Mechanisms of Evolution — Natural Selection, Drift", "understand", 0.4, ["evolution.origin_life"]),
        _c("human_evolution", "Human Evolution", "understand", 0.4, ["evolution.mechanisms_evolution"]),
    ]),
    ("human_health", "Human Health and Disease", [
        _c("common_diseases", "Common Diseases — Typhoid, Malaria, Cancer", "understand", 0.3),
        _c("immunity", "Immunity — Innate and Acquired", "understand", 0.4, ["human_health.common_diseases"]),
    ]),
    ("food_production", "Strategies for Enhancement in Food Production", [
        _c("plant_breeding", "Plant Breeding and Tissue Culture", "understand", 0.35),
        _c("animal_husbandry12", "Animal Husbandry and Fisheries", "understand", 0.3),
    ]),
    ("microbes_welfare", "Microbes in Human Welfare", [
        _c("industrial_microbes", "Microbes in Industrial Production", "understand", 0.3),
        _c("biogas_sewage", "Biogas Production and Sewage Treatment", "understand", 0.3),
    ]),
    ("biotech_principles", "Biotechnology: Principles and Processes", [
        _c("rdna_technology", "Recombinant DNA Technology", "understand", 0.45),
        _c("pcr_gel", "PCR and Gel Electrophoresis", "apply", 0.5, ["biotech_principles.rdna_technology"]),
    ]),
    ("biotech_applications", "Biotechnology and its Applications", [
        _c("bt_crops", "Bt Crops and GM Organisms", "understand", 0.4),
        _c("gene_therapy", "Gene Therapy and Molecular Diagnostics", "understand", 0.45, ["biotech_applications.bt_crops"]),
    ]),
    ("ecology_organisms", "Organisms and Populations", [
        _c("habitat_niche", "Habitat, Niche and Adaptations", "understand", 0.3),
        _c("population_dynamics", "Population Growth and Interactions", "apply", 0.4, ["ecology_organisms.habitat_niche"]),
    ]),
    ("ecosystem", "Ecosystem", [
        _c("energy_flow", "Energy Flow and Productivity", "understand", 0.35),
        _c("nutrient_cycling", "Nutrient Cycling — Carbon and Phosphorus", "understand", 0.4, ["ecosystem.energy_flow"]),
    ]),
    ("biodiversity", "Biodiversity and Conservation", [
        _c("biodiversity_levels", "Levels of Biodiversity", "understand", 0.3),
        _c("conservation_strategies", "Conservation Strategies — In Situ and Ex Situ", "apply", 0.35, ["biodiversity.biodiversity_levels"]),
    ]),
    ("environmental_issues", "Environmental Issues", [
        _c("pollution_env", "Air and Water Pollution", "understand", 0.3),
        _c("deforestation_waste", "Deforestation and Solid Waste Management", "understand", 0.3),
    ]),
]

# ══════════════════════════════════════════════════════════════════════════════
#  SOCIAL SCIENCE  —  History, Geography, Civics
# ══════════════════════════════════════════════════════════════════════════════

HISTORY8_CHAPTERS = [
    ("modern_period", "How, When and Where", [
        _c("periodisation", "Periodisation of Indian History", "understand", 0.25),
        _c("sources", "Sources — Official Records, Surveys, Newspapers", "understand", 0.25),
    ]),
    ("trade_to_territory", "From Trade to Territory", [
        _c("east_india_company", "East India Company and Trade", "understand", 0.3),
        _c("battles_expansion", "Battles and Territorial Expansion", "understand", 0.35, ["trade_to_territory.east_india_company"]),
    ]),
    ("ruling_countryside", "Ruling the Countryside", [
        _c("revenue_systems", "Revenue Systems — Permanent Settlement, Mahalwari, Ryotwari", "understand", 0.35),
        _c("indigo_cultivation", "Indigo Cultivation and Blue Rebellion", "understand", 0.3),
    ]),
    ("tribals_dikus", "Tribals, Dikus and the Vision of a Golden Age", [
        _c("tribal_society", "Tribal Societies in India", "understand", 0.3),
        _c("tribal_revolts", "Tribal Revolts — Birsa Munda", "understand", 0.35, ["tribals_dikus.tribal_society"]),
    ]),
    ("revolt_1857", "When People Rebel — 1857", [
        _c("causes_1857", "Causes of the Revolt", "understand", 0.3),
        _c("spread_aftermath", "Spread and Aftermath of 1857", "understand", 0.35, ["revolt_1857.causes_1857"]),
    ]),
    ("civilising_mission", "Civilising the 'Native', Educating the Nation", [
        _c("colonial_education", "Colonial Education Policies", "understand", 0.3),
        _c("national_education", "National Education Movement", "understand", 0.3),
    ]),
    ("women_reform", "Women, Caste and Reform", [
        _c("social_reformers", "Social Reformers — Raja Ram Mohan Roy, Jyotirao Phule", "understand", 0.3),
        _c("women_movements", "Women's Rights and Reform Movements", "understand", 0.3),
    ]),
    ("national_movement", "The Making of the National Movement: 1870s–1947", [
        _c("congress_formation", "Formation of Indian National Congress", "understand", 0.3),
        _c("gandhian_era", "Gandhian Era — NCM, CDM, Quit India", "understand", 0.4, ["national_movement.congress_formation"]),
        _c("independence", "Towards Independence and Partition", "understand", 0.35, ["national_movement.gandhian_era"]),
    ]),
    ("india_after_independence", "India After Independence", [
        _c("constitution_making", "Making of the Constitution", "understand", 0.3),
        _c("integration_states", "Integration of States and Planning", "understand", 0.3, ["india_after_independence.constitution_making"]),
    ]),
]

GEOGRAPHY8_CHAPTERS = [
    ("resources", "Resources", [
        _c("types_resources", "Types of Resources — Natural, Human-Made, Human", "understand", 0.25),
        _c("conservation_resources", "Conservation and Sustainable Development", "apply", 0.3, ["resources.types_resources"]),
    ]),
    ("land_resources", "Land, Soil, Water, Natural Vegetation and Wildlife", [
        _c("land_use", "Land Use Patterns", "understand", 0.25),
        _c("soil_conservation", "Soil Types and Conservation", "understand", 0.3),
    ]),
    ("mineral_power", "Mineral and Power Resources", [
        _c("minerals", "Types and Distribution of Minerals", "understand", 0.3),
        _c("power_resources", "Conventional and Non-Conventional Energy", "understand", 0.3),
    ]),
    ("agriculture", "Agriculture", [
        _c("farming_types", "Types of Farming", "understand", 0.25),
        _c("major_crops", "Major Crops — Food Grains, Fibre Crops", "understand", 0.3, ["agriculture.farming_types"]),
    ]),
    ("industries", "Industries", [
        _c("classification_industries", "Classification of Industries", "understand", 0.25),
        _c("industrial_regions", "Major Industrial Regions", "understand", 0.3, ["industries.classification_industries"]),
    ]),
    ("human_resources", "Human Resources", [
        _c("population_distribution", "Population Distribution and Density", "understand", 0.25),
        _c("population_change", "Population Change and Composition", "understand", 0.3, ["human_resources.population_distribution"]),
    ]),
]

CIVICS8_CHAPTERS = [
    ("constitution", "The Indian Constitution", [
        _c("need_constitution", "Why Do We Need a Constitution?", "understand", 0.25),
        _c("key_features", "Key Features of the Indian Constitution", "understand", 0.3, ["constitution.need_constitution"]),
    ]),
    ("secularism", "Understanding Secularism", [
        _c("secularism_india", "Secularism in India", "understand", 0.3),
        _c("state_religion", "Separation of State and Religion", "understand", 0.3),
    ]),
    ("parliament", "Why Do We Need a Parliament?", [
        _c("role_parliament", "Role of Parliament in Democracy", "understand", 0.25),
        _c("law_making", "How Laws Are Made", "understand", 0.3, ["parliament.role_parliament"]),
    ]),
    ("judiciary", "Understanding Laws and the Judiciary", [
        _c("judicial_system", "Structure of Indian Judiciary", "understand", 0.3),
        _c("access_to_justice", "Access to Justice and PIL", "understand", 0.3),
    ]),
    ("marginalisation", "Understanding Marginalisation", [
        _c("who_marginalised", "Who Are Marginalised?", "understand", 0.25),
        _c("rights_marginalised", "Rights of Marginalised Communities", "understand", 0.3),
    ]),
    ("public_facilities", "Public Facilities", [
        _c("water_facility", "Water as a Public Facility", "understand", 0.25),
        _c("role_government", "Role of Government in Public Facilities", "understand", 0.3),
    ]),
]

# ══════════════════════════════════════════════════════════════════════════════
#  ENGLISH  —  Grammar & Language Skills (Class 6-10)
# ══════════════════════════════════════════════════════════════════════════════

ENGLISH_GRAMMAR_CHAPTERS = [
    ("parts_of_speech", "Parts of Speech", [
        _c("nouns_pronouns", "Nouns and Pronouns", "understand", 0.2),
        _c("verbs_tenses", "Verbs and Tenses", "apply", 0.3, ["parts_of_speech.nouns_pronouns"]),
        _c("adjectives_adverbs", "Adjectives and Adverbs", "understand", 0.25, ["parts_of_speech.nouns_pronouns"]),
        _c("prepositions_conjunctions", "Prepositions and Conjunctions", "apply", 0.3, ["parts_of_speech.adjectives_adverbs"]),
    ]),
    ("sentence_structure", "Sentence Structure", [
        _c("subject_predicate", "Subject and Predicate", "understand", 0.2),
        _c("types_sentences", "Types of Sentences — Assertive, Interrogative, Imperative, Exclamatory", "understand", 0.25, ["sentence_structure.subject_predicate"]),
        _c("simple_compound_complex", "Simple, Compound and Complex Sentences", "apply", 0.35, ["sentence_structure.types_sentences"]),
    ]),
    ("tenses", "Tenses", [
        _c("present_tenses", "Present Tense — Simple, Continuous, Perfect", "apply", 0.3),
        _c("past_tenses", "Past Tense — Simple, Continuous, Perfect", "apply", 0.3),
        _c("future_tenses", "Future Tense — Simple, Continuous, Perfect", "apply", 0.3),
    ]),
    ("voice_speech", "Active-Passive Voice and Direct-Indirect Speech", [
        _c("active_passive", "Active and Passive Voice", "apply", 0.35),
        _c("direct_indirect", "Direct and Indirect Speech", "apply", 0.4, ["voice_speech.active_passive"]),
    ]),
    ("comprehension", "Reading Comprehension", [
        _c("unseen_passages", "Unseen Passages — Factual and Discursive", "apply", 0.35),
        _c("note_making", "Note Making and Summarising", "apply", 0.4, ["comprehension.unseen_passages"]),
    ]),
    ("writing", "Writing Skills", [
        _c("paragraph_writing", "Paragraph Writing", "apply", 0.3),
        _c("letter_writing", "Letter Writing — Formal and Informal", "apply", 0.35, ["writing.paragraph_writing"]),
        _c("essay_writing", "Essay and Article Writing", "create", 0.4, ["writing.letter_writing"]),
    ]),
]

# ══════════════════════════════════════════════════════════════════════════════
#  COMPUTER SCIENCE  —  Python & CS
# ══════════════════════════════════════════════════════════════════════════════

PYTHON_INTRO_CHAPTERS = [
    ("getting_started", "Getting Started with Python", [
        _c("install_run", "Installing Python and Running Programs", "remember", 0.1),
        _c("variables_types", "Variables and Data Types", "understand", 0.2, ["getting_started.install_run"]),
        _c("input_output", "Input/Output — print() and input()", "apply", 0.2, ["getting_started.variables_types"]),
    ]),
    ("operators", "Operators and Expressions", [
        _c("arithmetic_operators", "Arithmetic and Assignment Operators", "apply", 0.2),
        _c("comparison_logical", "Comparison and Logical Operators", "apply", 0.25, ["operators.arithmetic_operators"]),
    ]),
    ("control_flow", "Control Flow", [
        _c("if_elif_else", "if, elif, else Statements", "apply", 0.25),
        _c("for_loop", "for Loop and range()", "apply", 0.3, ["control_flow.if_elif_else"]),
        _c("while_loop", "while Loop", "apply", 0.3, ["control_flow.for_loop"]),
        _c("nested_loops", "Nested Loops and Loop Control", "apply", 0.35, ["control_flow.while_loop"]),
    ]),
    ("strings", "Strings", [
        _c("string_basics", "String Creation and Indexing", "understand", 0.2),
        _c("string_methods", "String Methods — split, join, replace, find", "apply", 0.3, ["strings.string_basics"]),
        _c("string_formatting", "String Formatting — f-strings", "apply", 0.3, ["strings.string_methods"]),
    ]),
    ("lists_tuples", "Lists and Tuples", [
        _c("list_basics", "Creating and Accessing Lists", "understand", 0.25),
        _c("list_operations", "List Operations — append, insert, remove, sort", "apply", 0.3, ["lists_tuples.list_basics"]),
        _c("list_comprehension", "List Comprehension", "apply", 0.4, ["lists_tuples.list_operations"]),
        _c("tuples", "Tuples — Immutable Sequences", "understand", 0.25),
    ]),
    ("dictionaries_sets", "Dictionaries and Sets", [
        _c("dict_basics", "Creating and Accessing Dictionaries", "understand", 0.25),
        _c("dict_methods", "Dictionary Methods and Iteration", "apply", 0.3, ["dictionaries_sets.dict_basics"]),
        _c("sets", "Sets — Operations and Methods", "apply", 0.3),
    ]),
    ("functions", "Functions", [
        _c("defining_functions", "Defining and Calling Functions", "apply", 0.3),
        _c("parameters_return", "Parameters, Arguments and Return Values", "apply", 0.35, ["functions.defining_functions"]),
        _c("scope", "Scope — Local and Global Variables", "understand", 0.35, ["functions.parameters_return"]),
        _c("lambda", "Lambda Functions", "apply", 0.4, ["functions.scope"]),
    ]),
    ("file_handling", "File Handling", [
        _c("reading_files", "Reading Files — open, read, readlines", "apply", 0.3),
        _c("writing_files", "Writing Files — write, writelines", "apply", 0.3, ["file_handling.reading_files"]),
        _c("csv_json", "Working with CSV and JSON", "apply", 0.4, ["file_handling.writing_files"]),
    ]),
    ("error_handling", "Error Handling", [
        _c("try_except", "try, except, finally", "apply", 0.35),
        _c("custom_exceptions", "Custom Exceptions", "apply", 0.4, ["error_handling.try_except"]),
    ]),
    ("oop", "Object-Oriented Programming", [
        _c("classes_objects", "Classes and Objects", "understand", 0.35),
        _c("init_methods", "__init__ and Instance Methods", "apply", 0.4, ["oop.classes_objects"]),
        _c("inheritance_poly", "Inheritance and Polymorphism", "apply", 0.5, ["oop.init_methods"]),
    ]),
]

# ══════════════════════════════════════════════════════════════════════════════
#  COMPETITIVE EXAMS  —  JEE & NEET
# ══════════════════════════════════════════════════════════════════════════════

JEE_MATH_CHAPTERS = [
    ("algebra", "Algebra", [
        _c("quadratic_theory", "Quadratic Equations — Theory of Equations", "apply", 0.5),
        _c("sequences_series", "Sequences, Series and Summation", "apply", 0.5),
        _c("matrices_determinants", "Matrices and Determinants (JEE Level)", "apply", 0.55, ["algebra.quadratic_theory"]),
        _c("pnc_binomial", "Permutations, Combinations, Binomial Theorem", "apply", 0.5),
    ]),
    ("calculus", "Calculus", [
        _c("limits_continuity", "Limits and Continuity (JEE Level)", "apply", 0.55),
        _c("differentiation_jee", "Differentiation Techniques", "apply", 0.55, ["calculus.limits_continuity"]),
        _c("application_derivatives_jee", "Application of Derivatives — Maxima, Minima, Tangents", "apply", 0.6, ["calculus.differentiation_jee"]),
        _c("integration_jee", "Definite and Indefinite Integration", "apply", 0.6, ["calculus.differentiation_jee"]),
        _c("differential_equations_jee", "Differential Equations", "apply", 0.6, ["calculus.integration_jee"]),
    ]),
    ("coordinate_geometry_jee", "Coordinate Geometry", [
        _c("straight_lines_jee", "Straight Lines (JEE Level)", "apply", 0.5),
        _c("circles_jee", "Circles", "apply", 0.55, ["coordinate_geometry_jee.straight_lines_jee"]),
        _c("conics_jee", "Parabola, Ellipse, Hyperbola (JEE Level)", "apply", 0.6, ["coordinate_geometry_jee.circles_jee"]),
    ]),
    ("vectors_3d_jee", "Vectors and 3D Geometry", [
        _c("vectors_jee", "Vectors — Dot, Cross Product (JEE Level)", "apply", 0.5),
        _c("3d_geometry_jee", "3D Geometry — Lines, Planes", "apply", 0.55, ["vectors_3d_jee.vectors_jee"]),
    ]),
    ("trigonometry_jee", "Trigonometry", [
        _c("trig_equations_jee", "Trigonometric Equations", "apply", 0.5),
        _c("inverse_trig_jee", "Inverse Trigonometric Functions (JEE Level)", "apply", 0.55, ["trigonometry_jee.trig_equations_jee"]),
    ]),
    ("probability_jee", "Probability and Statistics", [
        _c("probability_jee", "Probability (JEE Level)", "apply", 0.5),
        _c("distributions_jee", "Probability Distributions — Binomial", "apply", 0.55, ["probability_jee.probability_jee"]),
    ]),
]

NEET_BIOLOGY_CHAPTERS = [
    ("diversity_living", "Diversity in Living World", [
        _c("taxonomy_neet", "Taxonomy and Systematics", "understand", 0.35),
        _c("five_kingdoms_neet", "Five Kingdom Classification (NEET Level)", "apply", 0.4, ["diversity_living.taxonomy_neet"]),
        _c("plant_animal_kingdom_neet", "Plant and Animal Kingdom", "apply", 0.45, ["diversity_living.five_kingdoms_neet"]),
    ]),
    ("cell_biology", "Cell Biology", [
        _c("cell_structure_neet", "Cell Structure and Functions (NEET Level)", "apply", 0.4),
        _c("cell_division_neet", "Cell Division — Mitosis and Meiosis", "apply", 0.45, ["cell_biology.cell_structure_neet"]),
        _c("biomolecules_neet", "Biomolecules and Enzymes", "apply", 0.45, ["cell_biology.cell_structure_neet"]),
    ]),
    ("plant_physiology", "Plant Physiology", [
        _c("photosynthesis_neet", "Photosynthesis (NEET Level)", "apply", 0.5),
        _c("respiration_neet", "Plant Respiration", "apply", 0.45, ["plant_physiology.photosynthesis_neet"]),
        _c("plant_growth_neet", "Plant Growth and Hormones", "apply", 0.4),
    ]),
    ("human_physiology", "Human Physiology", [
        _c("digestion_neet", "Digestion and Absorption (NEET Level)", "apply", 0.4),
        _c("circulation_neet", "Circulation — Heart and Blood", "apply", 0.45, ["human_physiology.digestion_neet"]),
        _c("excretion_neet", "Excretion and Kidney Function", "apply", 0.45),
        _c("neural_neet", "Neural Control and Coordination", "apply", 0.5, ["human_physiology.circulation_neet"]),
    ]),
    ("reproduction_neet", "Reproduction", [
        _c("plant_reproduction_neet", "Plant Reproduction (NEET Level)", "apply", 0.4),
        _c("human_reproduction_neet", "Human Reproduction and RH", "apply", 0.4),
    ]),
    ("genetics_neet", "Genetics and Evolution", [
        _c("mendelian_genetics_neet", "Mendelian Genetics (NEET Level)", "apply", 0.45),
        _c("molecular_genetics_neet", "Molecular Genetics — DNA, RNA, Protein Synthesis", "apply", 0.55, ["genetics_neet.mendelian_genetics_neet"]),
        _c("evolution_neet", "Evolution — Evidence and Mechanisms", "apply", 0.45, ["genetics_neet.molecular_genetics_neet"]),
    ]),
    ("biotechnology_neet", "Biotechnology", [
        _c("rdna_neet", "rDNA Technology (NEET Level)", "apply", 0.5),
        _c("applications_neet", "Biotechnology Applications — GM Crops, Gene Therapy", "apply", 0.45, ["biotechnology_neet.rdna_neet"]),
    ]),
    ("ecology_neet", "Ecology and Environment", [
        _c("ecosystem_neet", "Ecosystems — Energy Flow, Nutrient Cycling", "apply", 0.4),
        _c("biodiversity_neet", "Biodiversity and Conservation", "apply", 0.4),
        _c("environmental_issues_neet", "Environmental Issues", "understand", 0.35),
    ]),
]

# ══════════════════════════════════════════════════════════════════════════════
#  ACCOUNTANCY & BUSINESS STUDIES — Classes 11-12
# ══════════════════════════════════════════════════════════════════════════════

ACCOUNTANCY11_CHAPTERS = [
    ("accounting_intro", "Introduction to Accounting", [
        _c("meaning_objectives", "Meaning and Objectives of Accounting", "understand", 0.2),
        _c("accounting_terms", "Basic Accounting Terms", "remember", 0.25, ["accounting_intro.meaning_objectives"]),
    ]),
    ("accounting_theory", "Theory Base of Accounting", [
        _c("gaap", "Accounting Principles — GAAP", "understand", 0.3),
        _c("concepts_conventions", "Accounting Concepts and Conventions", "understand", 0.35, ["accounting_theory.gaap"]),
    ]),
    ("journal_ledger", "Recording of Transactions", [
        _c("journal", "Journal Entries — Rules of Debit and Credit", "apply", 0.35),
        _c("ledger", "Ledger — Posting and Balancing", "apply", 0.4, ["journal_ledger.journal"]),
    ]),
    ("trial_balance", "Trial Balance and Rectification", [
        _c("trial_balance", "Preparation of Trial Balance", "apply", 0.4),
        _c("rectification", "Rectification of Errors", "apply", 0.45, ["trial_balance.trial_balance"]),
    ]),
    ("financial_statements", "Financial Statements", [
        _c("trading_account", "Trading and Profit & Loss Account", "apply", 0.4),
        _c("balance_sheet", "Balance Sheet", "apply", 0.45, ["financial_statements.trading_account"]),
    ]),
]

ECONOMICS9_CHAPTERS = [
    ("village_economy", "The Story of Village Palampur", [
        _c("factors_production", "Factors of Production — Land, Labour, Capital, Enterprise", "understand", 0.25),
        _c("farming_palampur", "Farming and Non-Farm Activities", "understand", 0.25),
    ]),
    ("people_as_resource", "People as Resource", [
        _c("human_capital", "Human Capital Formation", "understand", 0.3),
        _c("unemployment", "Types of Unemployment", "understand", 0.3, ["people_as_resource.human_capital"]),
    ]),
    ("poverty", "Poverty as a Challenge", [
        _c("poverty_line", "Poverty Line and Measurement", "understand", 0.3),
        _c("poverty_alleviation", "Poverty Alleviation Programmes", "understand", 0.3, ["poverty.poverty_line"]),
    ]),
    ("food_security", "Food Security in India", [
        _c("food_security_concept", "What Is Food Security?", "understand", 0.25),
        _c("pds", "Public Distribution System", "understand", 0.3, ["food_security.food_security_concept"]),
    ]),
]

ECONOMICS10_CHAPTERS = [
    ("development", "Development", [
        _c("development_concept", "What Is Development? Different Perspectives", "understand", 0.25),
        _c("hdi", "Human Development Index", "apply", 0.3, ["development.development_concept"]),
    ]),
    ("sectors_economy", "Sectors of the Indian Economy", [
        _c("primary_secondary_tertiary", "Primary, Secondary and Tertiary Sectors", "understand", 0.25),
        _c("organised_unorganised", "Organised and Unorganised Sectors", "understand", 0.3, ["sectors_economy.primary_secondary_tertiary"]),
    ]),
    ("money_credit", "Money and Credit", [
        _c("money_functions", "Functions of Money", "understand", 0.25),
        _c("credit_banking", "Credit and Banking System", "understand", 0.3, ["money_credit.money_functions"]),
    ]),
    ("globalisation", "Globalisation and the Indian Economy", [
        _c("globalisation_intro", "What Is Globalisation?", "understand", 0.25),
        _c("mncs_trade", "MNCs, Trade and Foreign Investment", "understand", 0.3, ["globalisation.globalisation_intro"]),
        _c("impact_india", "Impact of Globalisation on India", "analyze", 0.35, ["globalisation.mncs_trade"]),
    ]),
    ("consumer_rights", "Consumer Rights", [
        _c("consumer_awareness", "Consumer Awareness and Rights", "understand", 0.25),
        _c("consumer_protection", "Consumer Protection Act", "understand", 0.3, ["consumer_rights.consumer_awareness"]),
    ]),
]


# ══════════════════════════════════════════════════════════════════════════════
#  MASTER COURSE DEFINITIONS
# ══════════════════════════════════════════════════════════════════════════════

COURSES = [
    # ── Mathematics ─────────────────────────────────────────────────────────
    # math6 already exists — not regenerated
    {"course_id": "math7", "title": "Class 7 Mathematics", "subject": "mathematics",
     "grade": 7, "board": "NCERT", "icon": "🔢", "color": "#4A90D9",
     "description": "NCERT Class 7 Mathematics — integers, fractions, algebra, geometry, data handling and more.",
     "chapters": MATH7_CHAPTERS},
    {"course_id": "math8", "title": "Class 8 Mathematics", "subject": "mathematics",
     "grade": 8, "board": "NCERT", "icon": "🔢", "color": "#4A90D9",
     "description": "NCERT Class 8 Mathematics — rational numbers, quadrilaterals, algebraic identities, mensuration and more.",
     "chapters": MATH8_CHAPTERS},
    {"course_id": "math9", "title": "Class 9 Mathematics", "subject": "mathematics",
     "grade": 9, "board": "NCERT", "icon": "📐", "color": "#3B7DD8",
     "description": "NCERT Class 9 Mathematics — number systems, polynomials, geometry, statistics and probability.",
     "chapters": MATH9_CHAPTERS},
    {"course_id": "math10", "title": "Class 10 Mathematics", "subject": "mathematics",
     "grade": 10, "board": "NCERT", "icon": "📐", "color": "#3B7DD8",
     "description": "NCERT Class 10 Mathematics — real numbers, quadratic equations, trigonometry, coordinate geometry and more.",
     "chapters": MATH10_CHAPTERS},
    {"course_id": "math11", "title": "Class 11 Mathematics", "subject": "mathematics",
     "grade": 11, "board": "NCERT", "icon": "∑", "color": "#2E6EC7",
     "description": "NCERT Class 11 Mathematics — sets, trigonometry, complex numbers, calculus introduction, conic sections.",
     "chapters": MATH11_CHAPTERS},
    {"course_id": "math12", "title": "Class 12 Mathematics", "subject": "mathematics",
     "grade": 12, "board": "NCERT", "icon": "∫", "color": "#2E6EC7",
     "description": "NCERT Class 12 Mathematics — relations, matrices, calculus, vectors, 3D geometry, probability.",
     "chapters": MATH12_CHAPTERS},

    # ── Science ─────────────────────────────────────────────────────────────
    {"course_id": "science6", "title": "Class 6 Science", "subject": "science",
     "grade": 6, "board": "NCERT", "icon": "🔬", "color": "#27AE60",
     "description": "NCERT Class 6 Science — food, materials, living world, motion, light, electricity, magnets.",
     "chapters": SCIENCE6_CHAPTERS},
    {"course_id": "science7", "title": "Class 7 Science", "subject": "science",
     "grade": 7, "board": "NCERT", "icon": "🔬", "color": "#27AE60",
     "description": "NCERT Class 7 Science — nutrition, heat, acids and bases, respiration, motion, light.",
     "chapters": SCIENCE7_CHAPTERS},
    {"course_id": "science8", "title": "Class 8 Science", "subject": "science",
     "grade": 8, "board": "NCERT", "icon": "🔬", "color": "#27AE60",
     "description": "NCERT Class 8 Science — microorganisms, metals, cell structure, force, sound, stars.",
     "chapters": SCIENCE8_CHAPTERS},
    {"course_id": "science9", "title": "Class 9 Science", "subject": "science",
     "grade": 9, "board": "NCERT", "icon": "⚗️", "color": "#229954",
     "description": "NCERT Class 9 Science — matter, atoms, cells, motion, force, gravitation, work and energy.",
     "chapters": SCIENCE9_CHAPTERS},
    {"course_id": "science10", "title": "Class 10 Science", "subject": "science",
     "grade": 10, "board": "NCERT", "icon": "⚗️", "color": "#229954",
     "description": "NCERT Class 10 Science — chemical reactions, life processes, electricity, light, environment.",
     "chapters": SCIENCE10_CHAPTERS},

    # ── Physics ─────────────────────────────────────────────────────────────
    {"course_id": "physics11", "title": "Class 11 Physics", "subject": "physics",
     "grade": 11, "board": "NCERT", "icon": "⚛️", "color": "#8E44AD",
     "description": "NCERT Class 11 Physics — mechanics, thermodynamics, oscillations and waves.",
     "chapters": PHYSICS11_CHAPTERS},
    {"course_id": "physics12", "title": "Class 12 Physics", "subject": "physics",
     "grade": 12, "board": "NCERT", "icon": "⚛️", "color": "#8E44AD",
     "description": "NCERT Class 12 Physics — electrostatics, current electricity, optics, modern physics.",
     "chapters": PHYSICS12_CHAPTERS},

    # ── Chemistry ───────────────────────────────────────────────────────────
    {"course_id": "chemistry11", "title": "Class 11 Chemistry", "subject": "chemistry",
     "grade": 11, "board": "NCERT", "icon": "🧪", "color": "#E67E22",
     "description": "NCERT Class 11 Chemistry — atomic structure, bonding, thermodynamics, organic basics.",
     "chapters": CHEMISTRY11_CHAPTERS},
    {"course_id": "chemistry12", "title": "Class 12 Chemistry", "subject": "chemistry",
     "grade": 12, "board": "NCERT", "icon": "🧪", "color": "#E67E22",
     "description": "NCERT Class 12 Chemistry — solutions, electrochemistry, kinetics, coordination, organic reactions.",
     "chapters": CHEMISTRY12_CHAPTERS},

    # ── Biology ─────────────────────────────────────────────────────────────
    {"course_id": "biology11", "title": "Class 11 Biology", "subject": "biology",
     "grade": 11, "board": "NCERT", "icon": "🧬", "color": "#16A085",
     "description": "NCERT Class 11 Biology — diversity, cell biology, plant and human physiology.",
     "chapters": BIOLOGY11_CHAPTERS},
    {"course_id": "biology12", "title": "Class 12 Biology", "subject": "biology",
     "grade": 12, "board": "NCERT", "icon": "🧬", "color": "#16A085",
     "description": "NCERT Class 12 Biology — reproduction, genetics, evolution, biotechnology, ecology.",
     "chapters": BIOLOGY12_CHAPTERS},

    # ── Social Science ──────────────────────────────────────────────────────
    {"course_id": "history8", "title": "Class 8 History — Our Pasts III", "subject": "history",
     "grade": 8, "board": "NCERT", "icon": "📜", "color": "#C0392B",
     "description": "NCERT Class 8 History — British rule, 1857 revolt, nationalism, independence.",
     "chapters": HISTORY8_CHAPTERS},
    {"course_id": "geography8", "title": "Class 8 Geography — Resources and Development", "subject": "geography",
     "grade": 8, "board": "NCERT", "icon": "🌍", "color": "#2980B9",
     "description": "NCERT Class 8 Geography — resources, agriculture, industries, human resources.",
     "chapters": GEOGRAPHY8_CHAPTERS},
    {"course_id": "civics8", "title": "Class 8 Civics — Social and Political Life III", "subject": "civics",
     "grade": 8, "board": "NCERT", "icon": "⚖️", "color": "#D35400",
     "description": "NCERT Class 8 Civics — constitution, secularism, parliament, judiciary, marginalisation.",
     "chapters": CIVICS8_CHAPTERS},
    {"course_id": "economics9", "title": "Class 9 Economics", "subject": "economics",
     "grade": 9, "board": "NCERT", "icon": "💰", "color": "#F39C12",
     "description": "NCERT Class 9 Economics — village economy, human capital, poverty, food security.",
     "chapters": ECONOMICS9_CHAPTERS},
    {"course_id": "economics10", "title": "Class 10 Economics", "subject": "economics",
     "grade": 10, "board": "NCERT", "icon": "💰", "color": "#F39C12",
     "description": "NCERT Class 10 Economics — development, sectors, money and credit, globalisation.",
     "chapters": ECONOMICS10_CHAPTERS},

    # ── English ─────────────────────────────────────────────────────────────
    {"course_id": "english_grammar", "title": "English Grammar & Writing Skills", "subject": "english",
     "grade": 0, "board": "General", "icon": "📝", "color": "#34495E",
     "description": "English grammar, reading comprehension and writing skills — suitable for classes 6-10.",
     "chapters": ENGLISH_GRAMMAR_CHAPTERS},

    # ── Computer Science ────────────────────────────────────────────────────
    {"course_id": "python_intro", "title": "Introduction to Python Programming", "subject": "computer_science",
     "grade": 0, "board": "General", "icon": "🐍", "color": "#3776AB",
     "description": "Python programming from scratch — variables, loops, functions, OOP, file handling.",
     "chapters": PYTHON_INTRO_CHAPTERS},

    # ── Accountancy ─────────────────────────────────────────────────────────
    {"course_id": "accountancy11", "title": "Class 11 Accountancy", "subject": "accountancy",
     "grade": 11, "board": "NCERT", "icon": "📊", "color": "#1ABC9C",
     "description": "NCERT Class 11 Accountancy — accounting principles, journal, ledger, financial statements.",
     "chapters": ACCOUNTANCY11_CHAPTERS},

    # ── Competitive Exams ───────────────────────────────────────────────────
    {"course_id": "jee_math", "title": "JEE Mathematics", "subject": "mathematics",
     "grade": 0, "board": "JEE", "icon": "🎯", "color": "#E74C3C",
     "description": "JEE Main + Advanced Mathematics — algebra, calculus, coordinate geometry, vectors.",
     "chapters": JEE_MATH_CHAPTERS},
    {"course_id": "neet_biology", "title": "NEET Biology", "subject": "biology",
     "grade": 0, "board": "NEET", "icon": "🎯", "color": "#27AE60",
     "description": "NEET Biology — diversity, cell biology, physiology, genetics, biotechnology, ecology.",
     "chapters": NEET_BIOLOGY_CHAPTERS},
]


# ══════════════════════════════════════════════════════════════════════════════
#  GENERATOR LOGIC — Pure template, course data above is pure DATA
# ══════════════════════════════════════════════════════════════════════════════

def _auto_description(title: str, chapter_title: str) -> str:
    """Generate a description from concept title and chapter."""
    return f"{title} — part of the chapter on {chapter_title}."


def _auto_key_ideas(title: str) -> list[str]:
    """Generate seed key ideas from concept title."""
    words = title.split("—")[0].strip() if "—" in title else title
    return [
        f"Core principles of {words.lower()}",
        f"Step-by-step problem solving for {words.lower()}",
        f"Real-world applications of {words.lower()}",
    ]


def build_curriculum(course_def: dict) -> dict:
    """Build a full curriculum JSON from compact seed data."""
    course_id = course_def["course_id"]
    chapters_out = []

    # Global concept map for resolving cross-chapter prereqs
    concept_full_ids = set()

    for ch_idx, (ch_key, ch_title, concepts) in enumerate(course_def["chapters"], 1):
        ch_id = f"ch{ch_idx:02d}"
        concepts_out = []

        for suffix, title, bloom, diff, prereqs in concepts:
            full_id = f"{course_id}.{ch_key}.{suffix}"
            concept_full_ids.add(full_id)

            # Resolve prereq suffixes to full IDs
            resolved_prereqs = []
            for p in prereqs:
                # prereqs are "chapter_key.suffix" format
                full_prereq = f"{course_id}.{p}"
                resolved_prereqs.append(full_prereq)

            concepts_out.append({
                "concept_id": full_id,
                "title": title,
                "bloom_level": bloom,
                "difficulty": round(diff, 2),
                "prerequisites": resolved_prereqs,
                "description": _auto_description(title, ch_title),
                "key_ideas": _auto_key_ideas(title),
            })

        chapters_out.append({
            "chapter_id": ch_id,
            "title": ch_title,
            "concepts": concepts_out,
        })

    return {
        "course_id": course_id,
        "title": course_def["title"],
        "chapters": chapters_out,
    }


def build_registry_entry(course_def: dict) -> dict:
    """Build a courses.json registry entry."""
    return {
        "course_id": course_def["course_id"],
        "title": course_def["title"],
        "subject": course_def["subject"],
        "grade": course_def["grade"],
        "board": course_def["board"],
        "language": "english",
        "icon": course_def["icon"],
        "color": course_def["color"],
        "description": course_def["description"],
        "curriculum_file": f"{course_def['course_id']}/curriculum.json",
        "status": "active",
    }


def generate_all():
    """Generate all curriculum JSON files and update courses.json."""
    print("🏗️  Generating course curricula...")

    # Load existing courses.json to preserve math6
    registry_path = CONTENT_DIR / "courses.json"
    existing_registry = {"courses": []}
    if registry_path.exists():
        with open(registry_path) as f:
            existing_registry = json.load(f)

    existing_ids = {c["course_id"] for c in existing_registry["courses"]}
    total_concepts = 0

    for course_def in COURSES:
        cid = course_def["course_id"]

        # Generate curriculum
        curriculum = build_curriculum(course_def)
        n_chapters = len(curriculum["chapters"])
        n_concepts = sum(len(ch["concepts"]) for ch in curriculum["chapters"])
        total_concepts += n_concepts

        # Write curriculum file
        course_dir = CONTENT_DIR / cid
        course_dir.mkdir(parents=True, exist_ok=True)
        out_path = course_dir / "curriculum.json"
        with open(out_path, "w") as f:
            json.dump(curriculum, f, indent=2, ensure_ascii=False)

        # Add to registry if not already there
        if cid not in existing_ids:
            existing_registry["courses"].append(build_registry_entry(course_def))
            existing_ids.add(cid)
            status = "NEW"
        else:
            # Update existing entry
            for i, c in enumerate(existing_registry["courses"]):
                if c["course_id"] == cid:
                    existing_registry["courses"][i] = build_registry_entry(course_def)
                    break
            status = "UPDATED"

        print(f"   {course_def['icon']} {cid:20s} — {n_chapters:2d} chapters, {n_concepts:3d} concepts  [{status}]")

    # Sort registry by grade then course_id
    existing_registry["courses"].sort(key=lambda c: (c["grade"], c["course_id"]))

    # Write courses.json
    with open(registry_path, "w") as f:
        json.dump(existing_registry, f, indent=2, ensure_ascii=False)

    n_courses = len(existing_registry["courses"])
    print(f"\n✅ Done! {n_courses} courses registered, {total_concepts} seed concepts generated.")
    print(f"📁 Registry: {registry_path}")
    print(f"\n💡 Run 'python -m tools.expand_with_gemini <course_id>' to expand any course with AI.")


if __name__ == "__main__":
    generate_all()
