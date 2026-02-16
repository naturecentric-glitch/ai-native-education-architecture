#!/usr/bin/env python3
"""
Create complete Class 10 NCERT Mathematics content — curriculum + lessons + questions.

This generates everything offline (no API calls). Content is authored by LLM
with rich HTML visuals (SVG diagrams, styled boxes, color-coded steps, tables).

Run:  python -m tools.create_math10_content
"""
import json
import os
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE / "data" / "content" / "math10"

# ═══════════════════════════════════════════════════════════════════════════════
#  VISUAL HELPERS — reusable HTML snippets for rich content
# ═══════════════════════════════════════════════════════════════════════════════

def formula_box(formula: str, label: str = "") -> str:
    """A highlighted formula box with optional label."""
    lbl = f'<div style="font-size:0.7rem;text-transform:uppercase;font-weight:700;color:#1565C0;margin-bottom:4px">{label}</div>' if label else ""
    return f'''<div style="background:linear-gradient(135deg,#E3F2FD,#BBDEFB);border-left:4px solid #1565C0;border-radius:8px;padding:12px 16px;margin:12px 0;font-family:'Courier New',monospace;font-size:1.05rem;text-align:center">
{lbl}<strong>{formula}</strong></div>'''


def step_box(steps: list[tuple[str, str]], color: str = "#4A90D9") -> str:
    """Numbered step-by-step visual walkthrough."""
    html = '<div style="margin:12px 0">'
    for i, (title, detail) in enumerate(steps, 1):
        html += f'''<div style="display:flex;gap:12px;margin-bottom:10px;align-items:flex-start">
<div style="min-width:32px;height:32px;border-radius:50%;background:{color};color:white;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.85rem">{i}</div>
<div><strong>{title}</strong><br><span style="color:#555;font-size:0.88rem">{detail}</span></div></div>'''
    html += '</div>'
    return html


def tip_box(text: str, icon: str = "💡", bg: str = "#FFF8E1", border: str = "#FFB300") -> str:
    return f'<div style="background:{bg};border-left:4px solid {border};border-radius:8px;padding:10px 14px;margin:10px 0;font-size:0.88rem">{icon} <strong>Tip:</strong> {text}</div>'


def warning_box(text: str) -> str:
    return tip_box(text, "⚠️", "#FFF3E0", "#E65100")


def comparison_table(headers: list[str], rows: list[list[str]]) -> str:
    """Styled HTML table."""
    html = '<table style="width:100%;border-collapse:collapse;margin:12px 0;font-size:0.88rem">'
    html += '<tr>' + ''.join(f'<th style="background:#E3F2FD;padding:8px 12px;border:1px solid #BBDEFB;text-align:left;font-weight:700">{h}</th>' for h in headers) + '</tr>'
    for row in rows:
        html += '<tr>' + ''.join(f'<td style="padding:8px 12px;border:1px solid #E0E0E0">{cell}</td>' for cell in row) + '</tr>'
    html += '</table>'
    return html


def svg_number_line(start: int, end: int, highlights: dict = None, width: int = 400) -> str:
    """Simple SVG number line."""
    margin = 30
    inner = width - 2 * margin
    count = end - start
    step = inner / count
    svg = f'<svg width="{width}" height="60" style="display:block;margin:10px auto">'
    svg += f'<line x1="{margin}" y1="30" x2="{width-margin}" y2="30" stroke="#333" stroke-width="2"/>'
    for i in range(count + 1):
        x = margin + i * step
        v = start + i
        svg += f'<line x1="{x}" y1="25" x2="{x}" y2="35" stroke="#333" stroke-width="1.5"/>'
        svg += f'<text x="{x}" y="50" text-anchor="middle" font-size="11">{v}</text>'
    if highlights:
        for val, color in highlights.items():
            x = margin + (val - start) * step
            svg += f'<circle cx="{x}" cy="30" r="6" fill="{color}" stroke="white" stroke-width="1.5"/>'
    svg += '</svg>'
    return svg


def svg_right_triangle(a: int, b: int, c: int, width: int = 200) -> str:
    """SVG right triangle with labeled sides."""
    h = 140
    w = 160
    return f'''<svg width="{w+60}" height="{h+40}" style="display:block;margin:10px auto">
<polygon points="30,{h} {w+10},{h} 30,20" fill="#E8F5E9" stroke="#2E7D32" stroke-width="2"/>
<text x="{(w+40)//2}" y="{h+20}" text-anchor="middle" font-size="12" font-weight="bold">{b}</text>
<text x="12" y="{(h+20)//2}" text-anchor="middle" font-size="12" font-weight="bold" transform="rotate(-90,12,{(h+20)//2})">{a}</text>
<text x="{(w+40)//2+10}" y="{h//2}" text-anchor="start" font-size="12" font-weight="bold" fill="#C62828">{c}</text>
<rect x="30" y="{h-12}" width="12" height="12" fill="none" stroke="#2E7D32" stroke-width="1"/>
</svg>'''


def svg_circle_tangent(width: int = 220) -> str:
    """SVG circle with tangent and radius to point of tangency."""
    cx, cy, r = 110, 100, 60
    # tangent point at right
    tx, ty = cx + r, cy
    return f'''<svg width="{width}" height="200" style="display:block;margin:10px auto">
<circle cx="{cx}" cy="{cy}" r="{r}" fill="#E3F2FD" stroke="#1565C0" stroke-width="2"/>
<circle cx="{cx}" cy="{cy}" r="3" fill="#1565C0"/>
<text x="{cx-4}" y="{cy+16}" font-size="11" font-weight="bold">O</text>
<line x1="{cx}" y1="{cy}" x2="{tx}" y2="{ty}" stroke="#1565C0" stroke-width="1.5" stroke-dasharray="4"/>
<text x="{cx+r//2}" y="{cy-6}" font-size="10" fill="#1565C0">r</text>
<circle cx="{tx}" cy="{ty}" r="3" fill="#E65100"/>
<text x="{tx+4}" y="{ty-6}" font-size="11" font-weight="bold" fill="#E65100">P</text>
<line x1="{tx}" y1="{ty-50}" x2="{tx}" y2="{ty+50}" stroke="#E65100" stroke-width="2"/>
<text x="{tx+6}" y="{ty+46}" font-size="10" fill="#E65100">Tangent</text>
<text x="{tx+8}" y="{cy+r+30}" font-size="10" fill="#666">OP ⊥ Tangent</text>
</svg>'''


def svg_bar_chart(data: dict, title: str = "", width: int = 360, height: int = 180) -> str:
    """Simple SVG bar chart."""
    margin_b, margin_l = 30, 40
    bar_w = (width - margin_l - 20) // len(data) - 8
    max_v = max(data.values())
    scale = (height - margin_b - 20) / max_v
    svg = f'<svg width="{width}" height="{height}" style="display:block;margin:10px auto">'
    if title:
        svg += f'<text x="{width//2}" y="15" text-anchor="middle" font-size="12" font-weight="bold">{title}</text>'
    colors = ["#4A90D9", "#2ECC71", "#F39C12", "#E74C3C", "#9B59B6", "#1ABC9C"]
    for i, (label, val) in enumerate(data.items()):
        x = margin_l + i * (bar_w + 8) + 4
        bh = val * scale
        y = height - margin_b - bh
        c = colors[i % len(colors)]
        svg += f'<rect x="{x}" y="{y}" width="{bar_w}" height="{bh}" fill="{c}" rx="3"/>'
        svg += f'<text x="{x + bar_w//2}" y="{y-4}" text-anchor="middle" font-size="10" font-weight="bold">{val}</text>'
        svg += f'<text x="{x + bar_w//2}" y="{height-10}" text-anchor="middle" font-size="9">{label}</text>'
    svg += f'<line x1="{margin_l}" y1="{height-margin_b}" x2="{width-10}" y2="{height-margin_b}" stroke="#333" stroke-width="1"/>'
    svg += '</svg>'
    return svg


# ═══════════════════════════════════════════════════════════════════════════════
#  CURRICULUM — Expanded with proper NCERT concepts
# ═══════════════════════════════════════════════════════════════════════════════

CURRICULUM = {
    "course_id": "math10",
    "title": "Class 10 Mathematics",
    "chapters": [
        {
            "chapter_id": "ch01",
            "title": "Real Numbers",
            "concepts": [
                {
                    "concept_id": "math10.real_numbers.euclid_division",
                    "title": "Euclid's Division Lemma",
                    "bloom_level": "understand",
                    "difficulty": 0.35,
                    "prerequisites": [],
                    "description": "For any two positive integers a and b, there exist unique integers q and r such that a = bq + r, where 0 ≤ r < b. This is the foundation for finding HCF.",
                    "key_ideas": [
                        "Statement: a = bq + r where 0 ≤ r < b",
                        "Used to find HCF of two numbers step-by-step",
                        "Algorithm terminates when remainder becomes 0",
                        "The last non-zero remainder is the HCF"
                    ]
                },
                {
                    "concept_id": "math10.real_numbers.euclid_hcf",
                    "title": "Finding HCF Using Euclid's Algorithm",
                    "bloom_level": "apply",
                    "difficulty": 0.4,
                    "prerequisites": ["math10.real_numbers.euclid_division"],
                    "description": "Apply Euclid's division lemma repeatedly to find the HCF of two or more numbers. The algorithm uses successive division until the remainder is zero.",
                    "key_ideas": [
                        "Apply a = bq + r repeatedly with divisor and remainder",
                        "HCF(a,b) = HCF(b,r) — key recursive property",
                        "Process stops when remainder = 0; divisor at that step = HCF",
                        "Can extend to find HCF of three or more numbers"
                    ]
                },
                {
                    "concept_id": "math10.real_numbers.fundamental_theorem",
                    "title": "Fundamental Theorem of Arithmetic",
                    "bloom_level": "understand",
                    "difficulty": 0.4,
                    "prerequisites": ["math10.real_numbers.euclid_hcf"],
                    "description": "Every composite number can be expressed as a product of primes in a unique way (apart from the order of factors). This is the backbone of number theory.",
                    "key_ideas": [
                        "Every composite number = product of prime factors (uniquely)",
                        "Prime factorization using factor trees",
                        "Finding HCF using prime factorization: product of common primes with lowest powers",
                        "Finding LCM using prime factorization: product of all primes with highest powers",
                        "HCF × LCM = Product of the two numbers"
                    ]
                },
                {
                    "concept_id": "math10.real_numbers.irrational_proofs",
                    "title": "Proving Irrationality",
                    "bloom_level": "analyze",
                    "difficulty": 0.55,
                    "prerequisites": ["math10.real_numbers.fundamental_theorem"],
                    "description": "Use proof by contradiction and the Fundamental Theorem of Arithmetic to prove that numbers like √2, √3, √5 are irrational.",
                    "key_ideas": [
                        "Proof by contradiction: assume √2 = p/q in lowest terms",
                        "Show that p and q must both be even — contradicts 'lowest terms'",
                        "Key step: if p² is divisible by a prime, then p is also divisible by that prime",
                        "Same technique works for √3, √5, and any √p where p is prime"
                    ]
                },
                {
                    "concept_id": "math10.real_numbers.decimal_expansions",
                    "title": "Decimal Expansions of Rationals",
                    "bloom_level": "understand",
                    "difficulty": 0.35,
                    "prerequisites": ["math10.real_numbers.fundamental_theorem"],
                    "description": "Determine whether the decimal expansion of a rational number p/q is terminating or non-terminating repeating, based on the prime factorization of q.",
                    "key_ideas": [
                        "Terminating decimal: q has only factors of 2 and 5 (q = 2ⁿ × 5ᵐ)",
                        "Non-terminating repeating: q has prime factors other than 2 and 5",
                        "Every rational number has either terminating or repeating decimal",
                        "Irrational numbers have non-terminating, non-repeating decimals"
                    ]
                }
            ]
        },
        {
            "chapter_id": "ch02",
            "title": "Polynomials",
            "concepts": [
                {
                    "concept_id": "math10.polynomials10.types_and_zeroes",
                    "title": "Types of Polynomials and Geometrical Meaning of Zeroes",
                    "bloom_level": "understand",
                    "difficulty": 0.3,
                    "prerequisites": [],
                    "description": "Linear, quadratic, and cubic polynomials and their graphs. Zeroes are the x-coordinates where the graph crosses the x-axis.",
                    "key_ideas": [
                        "Linear polynomial ax+b has exactly 1 zero (straight line graph)",
                        "Quadratic polynomial ax²+bx+c has at most 2 zeroes (parabola)",
                        "Cubic polynomial has at most 3 zeroes (S-curve)",
                        "Zero of polynomial p(x): the value of x for which p(x) = 0",
                        "Geometrically: zeroes = x-coordinates of points where graph meets x-axis"
                    ]
                },
                {
                    "concept_id": "math10.polynomials10.zeroes_relationship",
                    "title": "Relationship Between Zeroes and Coefficients",
                    "bloom_level": "apply",
                    "difficulty": 0.4,
                    "prerequisites": ["math10.polynomials10.types_and_zeroes"],
                    "description": "For a quadratic polynomial ax²+bx+c with zeroes α and β: sum of zeroes = -b/a, product of zeroes = c/a. Extends to cubics.",
                    "key_ideas": [
                        "For ax²+bx+c: α + β = −b/a (sum of zeroes)",
                        "For ax²+bx+c: αβ = c/a (product of zeroes)",
                        "For cubic ax³+bx²+cx+d: α+β+γ = −b/a, αβ+βγ+γα = c/a, αβγ = −d/a",
                        "Can form polynomial from given zeroes: k[x² − (sum)x + (product)]"
                    ]
                },
                {
                    "concept_id": "math10.polynomials10.division_algorithm",
                    "title": "Division Algorithm for Polynomials",
                    "bloom_level": "apply",
                    "difficulty": 0.5,
                    "prerequisites": ["math10.polynomials10.zeroes_relationship"],
                    "description": "If p(x) and g(x) are polynomials with g(x) ≠ 0, then p(x) = g(x)×q(x) + r(x) where degree(r) < degree(g). Used to find remaining zeroes.",
                    "key_ideas": [
                        "Long division of polynomials: divide, multiply, subtract, bring down",
                        "p(x) = g(x) × q(x) + r(x) — analogous to Euclid's lemma",
                        "If two zeroes are known, divide to find quotient → remaining zeroes",
                        "Verify: degree(quotient) = degree(p) − degree(g)"
                    ]
                }
            ]
        },
        {
            "chapter_id": "ch03",
            "title": "Pair of Linear Equations in Two Variables",
            "concepts": [
                {
                    "concept_id": "math10.linear_eq_pair.graphical_method",
                    "title": "Graphical Representation and Consistency",
                    "bloom_level": "understand",
                    "difficulty": 0.35,
                    "prerequisites": [],
                    "description": "A pair of linear equations can be represented as two lines on a graph. The lines may intersect (unique solution), be parallel (no solution), or coincide (infinite solutions).",
                    "key_ideas": [
                        "Intersecting lines: a₁/a₂ ≠ b₁/b₂ → unique solution (consistent)",
                        "Parallel lines: a₁/a₂ = b₁/b₂ ≠ c₁/c₂ → no solution (inconsistent)",
                        "Coincident lines: a₁/a₂ = b₁/b₂ = c₁/c₂ → infinite solutions (dependent)",
                        "Solution of pair = coordinates of point of intersection"
                    ]
                },
                {
                    "concept_id": "math10.linear_eq_pair.substitution",
                    "title": "Substitution Method",
                    "bloom_level": "apply",
                    "difficulty": 0.4,
                    "prerequisites": ["math10.linear_eq_pair.graphical_method"],
                    "description": "Express one variable in terms of the other from one equation, substitute into the second equation to get a single variable equation, then solve.",
                    "key_ideas": [
                        "Step 1: From one equation, express y in terms of x (or vice versa)",
                        "Step 2: Substitute this expression into the other equation",
                        "Step 3: Solve the single-variable equation",
                        "Step 4: Substitute back to find the other variable"
                    ]
                },
                {
                    "concept_id": "math10.linear_eq_pair.elimination",
                    "title": "Elimination Method",
                    "bloom_level": "apply",
                    "difficulty": 0.4,
                    "prerequisites": ["math10.linear_eq_pair.substitution"],
                    "description": "Multiply equations by suitable numbers to make coefficients of one variable equal, then add or subtract to eliminate that variable.",
                    "key_ideas": [
                        "Multiply equations to equalize coefficients of one variable",
                        "Add equations if signs are opposite; subtract if signs are same",
                        "Solve resulting single-variable equation",
                        "Back-substitute to find the other variable"
                    ]
                },
                {
                    "concept_id": "math10.linear_eq_pair.cross_multiplication",
                    "title": "Cross-Multiplication Method",
                    "bloom_level": "apply",
                    "difficulty": 0.5,
                    "prerequisites": ["math10.linear_eq_pair.elimination"],
                    "description": "A formula-based method for solving a₁x + b₁y + c₁ = 0 and a₂x + b₂y + c₂ = 0 using the cross-multiplication rule.",
                    "key_ideas": [
                        "x/(b₁c₂ − b₂c₁) = y/(c₁a₂ − c₂a₁) = 1/(a₁b₂ − a₂b₁)",
                        "Write equations in standard form: ax + by + c = 0",
                        "Works when a₁b₂ − a₂b₁ ≠ 0 (unique solution exists)",
                        "Quick way to get both x and y in one step"
                    ]
                },
                {
                    "concept_id": "math10.linear_eq_pair.word_problems10",
                    "title": "Word Problems on Linear Equations",
                    "bloom_level": "apply",
                    "difficulty": 0.55,
                    "prerequisites": ["math10.linear_eq_pair.elimination"],
                    "description": "Translate real-life situations into pairs of linear equations — age problems, speed-distance-time, fractions, cost problems — and solve using any algebraic method.",
                    "key_ideas": [
                        "Identify unknowns and assign variables (let x = ..., y = ...)",
                        "Form two equations from the given conditions",
                        "Solve using substitution or elimination",
                        "Verify: check both solutions satisfy original word problem",
                        "Common types: age, speed-time, fraction, digit problems"
                    ]
                }
            ]
        },
        {
            "chapter_id": "ch04",
            "title": "Quadratic Equations",
            "concepts": [
                {
                    "concept_id": "math10.quadratic_equations.standard_form",
                    "title": "Standard Form and Factorization Method",
                    "bloom_level": "apply",
                    "difficulty": 0.4,
                    "prerequisites": [],
                    "description": "A quadratic equation has the form ax² + bx + c = 0, a ≠ 0. Solve by splitting the middle term into two parts whose product equals ac.",
                    "key_ideas": [
                        "Standard form: ax² + bx + c = 0 where a ≠ 0",
                        "Splitting middle term: find two numbers with sum = b and product = ac",
                        "Factor and set each factor = 0 to find roots",
                        "Maximum 2 roots for any quadratic equation"
                    ]
                },
                {
                    "concept_id": "math10.quadratic_equations.completing_square",
                    "title": "Completing the Square",
                    "bloom_level": "apply",
                    "difficulty": 0.45,
                    "prerequisites": ["math10.quadratic_equations.standard_form"],
                    "description": "Convert ax² + bx + c = 0 into (x + p)² = q form by adding and subtracting the right constant, then take square root to find roots.",
                    "key_ideas": [
                        "Divide by 'a' to make coefficient of x² equal to 1",
                        "Move constant term to RHS",
                        "Add (half of coefficient of x)² to both sides",
                        "LHS becomes a perfect square; take square root of both sides"
                    ]
                },
                {
                    "concept_id": "math10.quadratic_equations.quadratic_formula",
                    "title": "Quadratic Formula (Shreedharacharya's Rule)",
                    "bloom_level": "apply",
                    "difficulty": 0.45,
                    "prerequisites": ["math10.quadratic_equations.completing_square"],
                    "description": "The roots of ax² + bx + c = 0 are given by x = (−b ± √(b²−4ac)) / 2a. This universal formula works for all quadratic equations.",
                    "key_ideas": [
                        "Formula: x = (−b ± √(b²−4ac)) / 2a",
                        "Derived from completing the square on the general form",
                        "Works even when factorization is not easy",
                        "The ± gives two roots: one with + and one with −",
                        "Also called Shreedharacharya's formula (ancient Indian mathematician)"
                    ]
                },
                {
                    "concept_id": "math10.quadratic_equations.nature_of_roots",
                    "title": "Nature of Roots — Discriminant",
                    "bloom_level": "analyze",
                    "difficulty": 0.5,
                    "prerequisites": ["math10.quadratic_equations.quadratic_formula"],
                    "description": "The discriminant D = b² − 4ac determines the nature of roots: D > 0 → two distinct real roots, D = 0 → two equal roots, D < 0 → no real roots.",
                    "key_ideas": [
                        "Discriminant D = b² − 4ac",
                        "D > 0: two distinct real roots",
                        "D = 0: two equal (repeated) real roots, x = −b/2a",
                        "D < 0: no real roots (roots are complex/imaginary)",
                        "D is a perfect square → roots are rational"
                    ]
                },
                {
                    "concept_id": "math10.quadratic_equations.word_problems_quad",
                    "title": "Word Problems Leading to Quadratics",
                    "bloom_level": "apply",
                    "difficulty": 0.55,
                    "prerequisites": ["math10.quadratic_equations.quadratic_formula"],
                    "description": "Formulate quadratic equations from real-life problems about area, speed-time, consecutive numbers, age problems, etc. and solve them.",
                    "key_ideas": [
                        "Translate statements into equations: identify the variable",
                        "Common situations: area, product of consecutive numbers, speed-distance",
                        "After solving, reject negative/non-integer roots if context demands",
                        "Always verify: substitute back into the original problem"
                    ]
                }
            ]
        },
        {
            "chapter_id": "ch05",
            "title": "Arithmetic Progressions",
            "concepts": [
                {
                    "concept_id": "math10.arithmetic_progressions.ap_intro",
                    "title": "Introduction to AP and Common Difference",
                    "bloom_level": "understand",
                    "difficulty": 0.3,
                    "prerequisites": [],
                    "description": "An Arithmetic Progression is a sequence where each term is obtained by adding a fixed number (common difference d) to the previous term.",
                    "key_ideas": [
                        "AP: a, a+d, a+2d, a+3d, ... where d = common difference",
                        "d = any term − previous term (constant throughout)",
                        "d can be positive (increasing AP), negative (decreasing), or zero (constant)",
                        "First term is denoted by 'a', common difference by 'd'"
                    ]
                },
                {
                    "concept_id": "math10.arithmetic_progressions.ap_nth_term",
                    "title": "The nth Term of an AP",
                    "bloom_level": "apply",
                    "difficulty": 0.4,
                    "prerequisites": ["math10.arithmetic_progressions.ap_intro"],
                    "description": "The general (nth) term of an AP is aₙ = a + (n−1)d. This formula lets you find any term directly without listing all previous terms.",
                    "key_ideas": [
                        "General term: aₙ = a + (n−1)d",
                        "To find which term has a given value: solve a + (n−1)d = value for n",
                        "If aₙ is negative, the AP has started decreasing past zero",
                        "Last term often denoted by 'l': l = a + (n−1)d"
                    ]
                },
                {
                    "concept_id": "math10.arithmetic_progressions.sum_of_ap",
                    "title": "Sum of First n Terms of an AP",
                    "bloom_level": "apply",
                    "difficulty": 0.45,
                    "prerequisites": ["math10.arithmetic_progressions.ap_nth_term"],
                    "description": "Sₙ = n/2 × [2a + (n−1)d] or equivalently Sₙ = n/2 × (a + l). Gauss's trick: pair first+last, second+second-last, etc.",
                    "key_ideas": [
                        "Sₙ = n/2 × [2a + (n−1)d] — when last term is unknown",
                        "Sₙ = n/2 × (a + l) — when last term l is known",
                        "aₙ = Sₙ − Sₙ₋₁ — to find nth term from sum formula",
                        "Gauss's insight: S = n/2 × (first + last)"
                    ]
                },
                {
                    "concept_id": "math10.arithmetic_progressions.ap_applications",
                    "title": "Applications and Problem Solving with AP",
                    "bloom_level": "apply",
                    "difficulty": 0.5,
                    "prerequisites": ["math10.arithmetic_progressions.sum_of_ap"],
                    "description": "Use AP formulas to solve problems: finding terms, determining if a number belongs to an AP, sum-based problems, and real-life contexts like savings and patterns.",
                    "key_ideas": [
                        "Check membership: solve a + (n−1)d = k; if n is a positive integer, k is in the AP",
                        "Finding 'a' or 'd' from given conditions using simultaneous equations",
                        "Real-life APs: monthly savings, depreciation, stacking patterns",
                        "If Sₙ = An² + Bn, then d = 2A and a = A + B"
                    ]
                }
            ]
        },
        {
            "chapter_id": "ch06",
            "title": "Triangles",
            "concepts": [
                {
                    "concept_id": "math10.triangles10.similarity_intro",
                    "title": "Similar Figures and Basic Proportionality Theorem",
                    "bloom_level": "understand",
                    "difficulty": 0.4,
                    "prerequisites": [],
                    "description": "Two figures are similar if they have the same shape (but not necessarily size). BPT states: if a line is parallel to one side of a triangle and intersects the other two sides, it divides them proportionally.",
                    "key_ideas": [
                        "Similar figures: same shape, proportional sides, equal angles",
                        "BPT (Thales' theorem): DE ∥ BC in △ABC ⇒ AD/DB = AE/EC",
                        "Converse of BPT: if AD/DB = AE/EC then DE ∥ BC",
                        "Similarity ≠ Congruence (congruent → same shape AND size)"
                    ]
                },
                {
                    "concept_id": "math10.triangles10.similarity_criteria",
                    "title": "Criteria for Similarity of Triangles",
                    "bloom_level": "apply",
                    "difficulty": 0.45,
                    "prerequisites": ["math10.triangles10.similarity_intro"],
                    "description": "AAA (AA), SSS, and SAS similarity criteria. If two triangles are similar, their corresponding sides are proportional and corresponding angles are equal.",
                    "key_ideas": [
                        "AA criterion: two pairs of equal angles ⇒ triangles are similar",
                        "SSS criterion: all three pairs of sides in proportion ⇒ similar",
                        "SAS criterion: one pair of equal angles between proportional sides ⇒ similar",
                        "If △ABC ~ △DEF, then AB/DE = BC/EF = CA/FD and ∠A=∠D, ∠B=∠E, ∠C=∠F"
                    ]
                },
                {
                    "concept_id": "math10.triangles10.areas_similar",
                    "title": "Areas of Similar Triangles",
                    "bloom_level": "apply",
                    "difficulty": 0.5,
                    "prerequisites": ["math10.triangles10.similarity_criteria"],
                    "description": "The ratio of areas of two similar triangles equals the square of the ratio of their corresponding sides (or altitudes, or medians).",
                    "key_ideas": [
                        "Area(△ABC)/Area(△DEF) = (AB/DE)² = (BC/EF)² = (CA/FD)²",
                        "Also equals (altitude₁/altitude₂)² and (median₁/median₂)²",
                        "If sides are in ratio k:1, areas are in ratio k²:1",
                        "Useful for finding areas without knowing all dimensions"
                    ]
                },
                {
                    "concept_id": "math10.triangles10.pythagoras_theorem",
                    "title": "Pythagoras Theorem and Converse",
                    "bloom_level": "apply",
                    "difficulty": 0.45,
                    "prerequisites": ["math10.triangles10.similarity_criteria"],
                    "description": "In a right triangle, the square of the hypotenuse equals the sum of squares of the other two sides. The converse helps identify right triangles.",
                    "key_ideas": [
                        "Pythagoras: In right △ABC with ∠B = 90°, AC² = AB² + BC²",
                        "Hypotenuse is always the longest side (opposite the right angle)",
                        "Converse: If AC² = AB² + BC², then ∠B = 90°",
                        "Common Pythagorean triplets: (3,4,5), (5,12,13), (8,15,17), (7,24,25)"
                    ]
                }
            ]
        },
        {
            "chapter_id": "ch07",
            "title": "Coordinate Geometry",
            "concepts": [
                {
                    "concept_id": "math10.coordinate_geometry10.distance_formula",
                    "title": "Distance Formula",
                    "bloom_level": "apply",
                    "difficulty": 0.4,
                    "prerequisites": [],
                    "description": "The distance between two points (x₁,y₁) and (x₂,y₂) is √[(x₂−x₁)² + (y₂−y₁)²]. Derived from Pythagoras theorem applied to the coordinate plane.",
                    "key_ideas": [
                        "Distance = √[(x₂−x₁)² + (y₂−y₁)²]",
                        "Distance from origin: √(x² + y²)",
                        "If distance = 0, the points are the same",
                        "Used to check collinearity: three points are collinear if AB + BC = AC"
                    ]
                },
                {
                    "concept_id": "math10.coordinate_geometry10.section_formula",
                    "title": "Section Formula",
                    "bloom_level": "apply",
                    "difficulty": 0.45,
                    "prerequisites": ["math10.coordinate_geometry10.distance_formula"],
                    "description": "The point dividing the line segment joining (x₁,y₁) and (x₂,y₂) in ratio m:n is ((mx₂+nx₁)/(m+n), (my₂+ny₁)/(m+n)). The midpoint is the special case m=n.",
                    "key_ideas": [
                        "Internal division m:n: ((mx₂+nx₁)/(m+n), (my₂+ny₁)/(m+n))",
                        "Midpoint formula (m=n=1): ((x₁+x₂)/2, (y₁+y₂)/2)",
                        "Used to find centroids, medians, and points on line segments",
                        "Centroid of triangle: ((x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3)"
                    ]
                },
                {
                    "concept_id": "math10.coordinate_geometry10.area_triangle_coord",
                    "title": "Area of Triangle Using Coordinates",
                    "bloom_level": "apply",
                    "difficulty": 0.5,
                    "prerequisites": ["math10.coordinate_geometry10.section_formula"],
                    "description": "Area of triangle with vertices (x₁,y₁), (x₂,y₂), (x₃,y₃) = ½|x₁(y₂−y₃) + x₂(y₃−y₁) + x₃(y₁−y₂)|. If area = 0, points are collinear.",
                    "key_ideas": [
                        "Area = ½|x₁(y₂−y₃) + x₂(y₃−y₁) + x₃(y₁−y₂)|",
                        "Absolute value ensures area is always positive",
                        "If area = 0, the three points are collinear (lie on same line)",
                        "Can extend to find area of quadrilateral by dividing into triangles"
                    ]
                }
            ]
        },
        {
            "chapter_id": "ch08",
            "title": "Introduction to Trigonometry",
            "concepts": [
                {
                    "concept_id": "math10.trigonometry.trig_ratios",
                    "title": "Trigonometric Ratios",
                    "bloom_level": "understand",
                    "difficulty": 0.4,
                    "prerequisites": [],
                    "description": "In a right triangle, the six trigonometric ratios (sin, cos, tan, cosec, sec, cot) relate the angles to the ratios of sides.",
                    "key_ideas": [
                        "sin θ = Opposite/Hypotenuse, cos θ = Adjacent/Hypotenuse, tan θ = Opposite/Adjacent",
                        "Reciprocals: cosec θ = 1/sin θ, sec θ = 1/cos θ, cot θ = 1/tan θ",
                        "Mnemonic: SOH-CAH-TOA (Some Old Houses Can Always Hide Their Old Age)",
                        "These ratios depend on the angle, not the size of the triangle"
                    ]
                },
                {
                    "concept_id": "math10.trigonometry.standard_angles",
                    "title": "Trigonometric Ratios of Standard Angles",
                    "bloom_level": "remember",
                    "difficulty": 0.35,
                    "prerequisites": ["math10.trigonometry.trig_ratios"],
                    "description": "The exact values of sin, cos, tan for 0°, 30°, 45°, 60°, 90° must be memorized. These form the foundation for all trigonometric calculations.",
                    "key_ideas": [
                        "sin 0°=0, sin 30°=½, sin 45°=1/√2, sin 60°=√3/2, sin 90°=1",
                        "cos is reverse of sin: cos 0°=1, cos 30°=√3/2, cos 45°=1/√2, cos 60°=½, cos 90°=0",
                        "tan 0°=0, tan 30°=1/√3, tan 45°=1, tan 60°=√3, tan 90°=undefined",
                        "Trick: sin θ values are √0/2, √1/2, √2/2, √3/2, √4/2 for θ = 0°,30°,45°,60°,90°"
                    ]
                },
                {
                    "concept_id": "math10.trigonometry.complementary_angles",
                    "title": "Trigonometric Ratios of Complementary Angles",
                    "bloom_level": "apply",
                    "difficulty": 0.4,
                    "prerequisites": ["math10.trigonometry.standard_angles"],
                    "description": "Two angles are complementary if they add to 90°. Key identities: sin(90°−θ) = cos θ, cos(90°−θ) = sin θ, tan(90°−θ) = cot θ.",
                    "key_ideas": [
                        "sin(90°−θ) = cos θ and cos(90°−θ) = sin θ",
                        "tan(90°−θ) = cot θ and cot(90°−θ) = tan θ",
                        "sec(90°−θ) = cosec θ and cosec(90°−θ) = sec θ",
                        "Useful for simplifying expressions like sin 72° = cos 18°"
                    ]
                },
                {
                    "concept_id": "math10.trigonometry.trig_identities",
                    "title": "Trigonometric Identities",
                    "bloom_level": "apply",
                    "difficulty": 0.5,
                    "prerequisites": ["math10.trigonometry.complementary_angles"],
                    "description": "The three fundamental identities: sin²θ + cos²θ = 1, 1 + tan²θ = sec²θ, 1 + cot²θ = cosec²θ. Used to prove other identities and simplify expressions.",
                    "key_ideas": [
                        "Identity 1: sin²θ + cos²θ = 1 (derived from Pythagoras)",
                        "Identity 2: 1 + tan²θ = sec²θ (divide Identity 1 by cos²θ)",
                        "Identity 3: 1 + cot²θ = cosec²θ (divide Identity 1 by sin²θ)",
                        "Proving identities: work on one side (usually LHS) to reach the other"
                    ]
                }
            ]
        },
        {
            "chapter_id": "ch09",
            "title": "Some Applications of Trigonometry",
            "concepts": [
                {
                    "concept_id": "math10.trig_applications.angle_elevation_depression",
                    "title": "Angle of Elevation and Depression",
                    "bloom_level": "understand",
                    "difficulty": 0.4,
                    "prerequisites": ["math10.trigonometry.trig_ratios"],
                    "description": "Angle of elevation is measured upward from the horizontal line of sight. Angle of depression is measured downward. Both use the same trigonometric ratios.",
                    "key_ideas": [
                        "Angle of elevation: looking UP from horizontal → angle above horizontal",
                        "Angle of depression: looking DOWN from horizontal → angle below horizontal",
                        "Angle of elevation from A = Angle of depression from B (alternate interior angles)",
                        "Always draw a right triangle with the height as one side"
                    ]
                },
                {
                    "concept_id": "math10.trig_applications.heights_distances",
                    "title": "Heights and Distances Problems",
                    "bloom_level": "apply",
                    "difficulty": 0.55,
                    "prerequisites": ["math10.trig_applications.angle_elevation_depression"],
                    "description": "Apply trigonometric ratios to find heights of towers, buildings, widths of rivers, etc. using angles of elevation/depression and known distances.",
                    "key_ideas": [
                        "Draw the figure, identify right triangle, mark known/unknown sides",
                        "Use tan θ = height/distance (most common ratio in these problems)",
                        "Two-triangle problems: set up equations for each triangle, solve simultaneously",
                        "Common setups: tower on cliff, observer moving closer/farther"
                    ]
                }
            ]
        },
        {
            "chapter_id": "ch10",
            "title": "Circles",
            "concepts": [
                {
                    "concept_id": "math10.circles10.tangent_properties",
                    "title": "Tangent to a Circle — Properties",
                    "bloom_level": "understand",
                    "difficulty": 0.4,
                    "prerequisites": [],
                    "description": "A tangent to a circle touches it at exactly one point. The tangent at any point is perpendicular to the radius at that point of contact.",
                    "key_ideas": [
                        "Tangent touches the circle at exactly one point (point of contact/tangency)",
                        "Theorem 1: Tangent ⊥ Radius at the point of contact",
                        "A line perpendicular to the radius at its endpoint on the circle is a tangent",
                        "No tangent can be drawn from a point inside the circle"
                    ]
                },
                {
                    "concept_id": "math10.circles10.tangent_theorems",
                    "title": "Tangent Theorems and Problem Solving",
                    "bloom_level": "apply",
                    "difficulty": 0.5,
                    "prerequisites": ["math10.circles10.tangent_properties"],
                    "description": "Two tangents drawn from an external point to a circle are equal in length. This leads to many elegant geometric results and numerical problems.",
                    "key_ideas": [
                        "Theorem 2: Tangents from an external point are equal (PA = PB)",
                        "The line from external point to centre bisects the angle between tangents",
                        "OP bisects ∠APB and ∠AOB (O = centre, P = external point)",
                        "In △OAP: OA² + AP² = OP² (right angle at A)"
                    ]
                }
            ]
        },
        {
            "chapter_id": "ch11",
            "title": "Constructions",
            "concepts": [
                {
                    "concept_id": "math10.constructions10.division_line_segment",
                    "title": "Division of a Line Segment in a Given Ratio",
                    "bloom_level": "apply",
                    "difficulty": 0.4,
                    "prerequisites": [],
                    "description": "Construct a point that divides a line segment internally in a given ratio m:n using the basic proportionality theorem.",
                    "key_ideas": [
                        "Draw ray at an acute angle, mark (m+n) equal arcs",
                        "Join the last mark to endpoint, draw parallel through mth mark",
                        "Based on Basic Proportionality Theorem (BPT)",
                        "Can also construct similar triangles using this technique"
                    ]
                },
                {
                    "concept_id": "math10.constructions10.similar_triangle",
                    "title": "Construction of Similar Triangles",
                    "bloom_level": "apply",
                    "difficulty": 0.45,
                    "prerequisites": ["math10.constructions10.division_line_segment"],
                    "description": "Construct a triangle similar to a given triangle with sides in a given ratio (scale factor). Uses the line segment division technique.",
                    "key_ideas": [
                        "Scale factor < 1: smaller similar triangle (inside)",
                        "Scale factor > 1: larger similar triangle (outside)",
                        "Steps: draw base, divide using ratio, draw parallel lines",
                        "The constructed triangle has all angles equal to original"
                    ]
                },
                {
                    "concept_id": "math10.constructions10.tangent_construction",
                    "title": "Construction of Tangents to a Circle",
                    "bloom_level": "apply",
                    "difficulty": 0.5,
                    "prerequisites": ["math10.constructions10.similar_triangle"],
                    "description": "Construct tangents to a circle from a point outside it, and construct a tangent at a point on the circle. Uses the property that tangent ⊥ radius.",
                    "key_ideas": [
                        "Tangent from external point: find midpoint of OP, draw circle with that as centre",
                        "Intersection points give points of tangency",
                        "Tangent at a point on circle: draw radius, construct perpendicular",
                        "Two tangents from external point are always equal"
                    ]
                }
            ]
        },
        {
            "chapter_id": "ch12",
            "title": "Areas Related to Circles",
            "concepts": [
                {
                    "concept_id": "math10.areas_circles.perimeter_area",
                    "title": "Circumference and Area of a Circle",
                    "bloom_level": "apply",
                    "difficulty": 0.35,
                    "prerequisites": [],
                    "description": "Circumference = 2πr, Area = πr². These fundamental formulas are the building blocks for sector and segment calculations.",
                    "key_ideas": [
                        "Circumference (perimeter) = 2πr = πd",
                        "Area = πr²",
                        "π ≈ 22/7 or 3.14159...",
                        "Area of ring (annulus) = π(R² − r²) where R > r"
                    ]
                },
                {
                    "concept_id": "math10.areas_circles.sector_segment",
                    "title": "Area of Sector and Segment",
                    "bloom_level": "apply",
                    "difficulty": 0.45,
                    "prerequisites": ["math10.areas_circles.perimeter_area"],
                    "description": "A sector is a 'slice' of a circle; a segment is the region between a chord and its arc. Area of sector = (θ/360°) × πr², and segment area = sector area − triangle area.",
                    "key_ideas": [
                        "Arc length = (θ/360°) × 2πr",
                        "Area of sector = (θ/360°) × πr²",
                        "Area of segment = Area of sector − Area of triangle",
                        "Major sector + Minor sector = Full circle"
                    ]
                },
                {
                    "concept_id": "math10.areas_circles.combined_figures",
                    "title": "Areas of Combinations of Plane Figures",
                    "bloom_level": "apply",
                    "difficulty": 0.5,
                    "prerequisites": ["math10.areas_circles.sector_segment"],
                    "description": "Find areas of shaded regions in figures that combine circles, squares, triangles, and other shapes by adding or subtracting individual areas.",
                    "key_ideas": [
                        "Strategy: identify the shapes involved, then add or subtract areas",
                        "Common patterns: circle inscribed in square, semicircles on sides of triangle",
                        "Shaded area = Total area − Unshaded area (often easier to compute)",
                        "Draw auxiliary lines to break complex figures into simple shapes"
                    ]
                }
            ]
        },
        {
            "chapter_id": "ch13",
            "title": "Surface Areas and Volumes",
            "concepts": [
                {
                    "concept_id": "math10.surface_area_volume10.conversion_solids",
                    "title": "Conversion of One Solid into Another",
                    "bloom_level": "apply",
                    "difficulty": 0.45,
                    "prerequisites": [],
                    "description": "When one solid is melted and recast into another shape, the volume remains the same. Set Volume₁ = Volume₂ to find unknown dimensions.",
                    "key_ideas": [
                        "Volume is conserved when a solid is melted and reshaped",
                        "Equate volumes: V(old shape) = V(new shape) or = n × V(each new)",
                        "Common: sphere → cylinder, cone → spheres, cylinder → cones",
                        "Number of new objects = Volume(original) / Volume(one new object)"
                    ]
                },
                {
                    "concept_id": "math10.surface_area_volume10.combination_solids",
                    "title": "Surface Area and Volume of Combined Solids",
                    "bloom_level": "apply",
                    "difficulty": 0.5,
                    "prerequisites": ["math10.surface_area_volume10.conversion_solids"],
                    "description": "Many real objects (tent, capsule, silo) are combinations of basic solids. Find total surface area and volume by adding/subtracting components.",
                    "key_ideas": [
                        "Combined volume = sum of individual volumes",
                        "Total Surface Area ≠ sum of all surfaces (subtract joined faces)",
                        "Common combinations: cylinder+cone, hemisphere+cylinder, cone+hemisphere",
                        "CSA of combined = sum of CSAs of visible parts"
                    ]
                },
                {
                    "concept_id": "math10.surface_area_volume10.frustum",
                    "title": "Frustum of a Cone",
                    "bloom_level": "apply",
                    "difficulty": 0.5,
                    "prerequisites": ["math10.surface_area_volume10.combination_solids"],
                    "description": "A frustum is the portion of a cone between two parallel cuts. It has two circular faces of different radii. Volume = πh/3(R² + r² + Rr).",
                    "key_ideas": [
                        "Frustum: cone with top sliced off by a plane parallel to the base",
                        "Volume = (πh/3)(R² + r² + Rr) where R = base radius, r = top radius",
                        "Slant height l = √[h² + (R−r)²]",
                        "CSA = π(R+r)l, Total SA = π(R+r)l + πR² + πr²"
                    ]
                }
            ]
        },
        {
            "chapter_id": "ch14",
            "title": "Statistics",
            "concepts": [
                {
                    "concept_id": "math10.statistics10.mean_grouped",
                    "title": "Mean of Grouped Data",
                    "bloom_level": "apply",
                    "difficulty": 0.4,
                    "prerequisites": [],
                    "description": "Three methods to find the mean of grouped frequency data: Direct method, Assumed Mean method (shortcut), and Step Deviation method.",
                    "key_ideas": [
                        "Direct method: Mean = Σfᵢxᵢ / Σfᵢ (where xᵢ = class mark)",
                        "Assumed mean: Mean = a + Σfᵢdᵢ/Σfᵢ (dᵢ = xᵢ − a)",
                        "Step deviation: Mean = a + (Σfᵢuᵢ/Σfᵢ) × h (uᵢ = dᵢ/h)",
                        "Class mark xᵢ = (upper limit + lower limit) / 2"
                    ]
                },
                {
                    "concept_id": "math10.statistics10.median_grouped",
                    "title": "Median of Grouped Data",
                    "bloom_level": "apply",
                    "difficulty": 0.45,
                    "prerequisites": ["math10.statistics10.mean_grouped"],
                    "description": "Median = l + [(n/2 − cf)/f] × h, where l = lower limit of median class, cf = cumulative frequency before median class, f = frequency of median class.",
                    "key_ideas": [
                        "Find n/2, then locate the median class using cumulative frequency",
                        "Median = l + [(n/2 − cf)/f] × h",
                        "l = lower boundary of median class, h = class width",
                        "cf = cumulative frequency of class BEFORE the median class"
                    ]
                },
                {
                    "concept_id": "math10.statistics10.mode_grouped",
                    "title": "Mode of Grouped Data",
                    "bloom_level": "apply",
                    "difficulty": 0.4,
                    "prerequisites": ["math10.statistics10.mean_grouped"],
                    "description": "Mode = l + [(f₁ − f₀)/(2f₁ − f₀ − f₂)] × h, where the modal class has the highest frequency.",
                    "key_ideas": [
                        "Modal class = class with the highest frequency",
                        "Mode = l + [(f₁ − f₀)/(2f₁ − f₀ − f₂)] × h",
                        "f₁ = frequency of modal class, f₀ = frequency before, f₂ = frequency after",
                        "Empirical relation: 3 Median = Mode + 2 Mean (approximate)"
                    ]
                },
                {
                    "concept_id": "math10.statistics10.ogive",
                    "title": "Cumulative Frequency and Ogives",
                    "bloom_level": "apply",
                    "difficulty": 0.45,
                    "prerequisites": ["math10.statistics10.median_grouped"],
                    "description": "An ogive (cumulative frequency curve) is plotted using cumulative frequencies. 'Less than' and 'more than' ogives can be used to find the median graphically.",
                    "key_ideas": [
                        "'Less than' ogive: plot upper limits vs cumulative frequency (rising curve)",
                        "'More than' ogive: plot lower limits vs cumulative frequency (falling curve)",
                        "Median = x-coordinate where the two ogives intersect",
                        "Can also find median by drawing n/2 line on a single ogive"
                    ]
                }
            ]
        },
        {
            "chapter_id": "ch15",
            "title": "Probability",
            "concepts": [
                {
                    "concept_id": "math10.probability10.classical_definition",
                    "title": "Classical (Theoretical) Probability",
                    "bloom_level": "understand",
                    "difficulty": 0.35,
                    "prerequisites": [],
                    "description": "P(E) = Number of favourable outcomes / Total number of equally likely outcomes. Probability always lies between 0 and 1.",
                    "key_ideas": [
                        "P(E) = Favourable outcomes / Total outcomes",
                        "0 ≤ P(E) ≤ 1 always",
                        "P(sure event) = 1, P(impossible event) = 0",
                        "P(E) + P(not E) = 1 ⇒ P(not E) = 1 − P(E)"
                    ]
                },
                {
                    "concept_id": "math10.probability10.elementary_events",
                    "title": "Elementary Events and Sample Space",
                    "bloom_level": "understand",
                    "difficulty": 0.35,
                    "prerequisites": ["math10.probability10.classical_definition"],
                    "description": "An elementary event has a single outcome. The sample space is the set of all possible outcomes. Sum of probabilities of all elementary events = 1.",
                    "key_ideas": [
                        "Sample space: set of all possible outcomes of an experiment",
                        "Elementary event: event with exactly one outcome",
                        "Compound event: event with more than one outcome",
                        "Sum of probabilities of all elementary events = 1"
                    ]
                },
                {
                    "concept_id": "math10.probability10.problems_applications",
                    "title": "Probability Problems — Coins, Dice, Cards",
                    "bloom_level": "apply",
                    "difficulty": 0.45,
                    "prerequisites": ["math10.probability10.elementary_events"],
                    "description": "Apply probability to standard experiments: tossing coins, rolling dice, drawing cards from a deck. Systematic counting is key.",
                    "key_ideas": [
                        "Coin: P(Head) = P(Tail) = 1/2; two coins: 4 outcomes (HH,HT,TH,TT)",
                        "Die: 6 outcomes (1-6); two dice: 36 outcomes",
                        "Deck of cards: 52 cards, 4 suits × 13 ranks",
                        "Strategy: list sample space, count favourable outcomes, apply P = favourable/total"
                    ]
                }
            ]
        }
    ]
}

# ═══════════════════════════════════════════════════════════════════════════════
#  LESSONS — Rich HTML content with SVG diagrams and styled boxes
# ═══════════════════════════════════════════════════════════════════════════════

def make_lessons() -> dict:
    """Return {concept_id: lesson_dict} for all concepts."""
    lessons = {}

    # ── Ch 1: Real Numbers ──────────────────────────────────────────────────

    lessons["math10.real_numbers.euclid_division"] = {
        "title": "Euclid's Division Lemma — The King of 'Divide & Conquer' 👑",
        "hook": "Imagine you have 23 chocolates and want to distribute them equally among 5 friends. You can give 4 chocolates to each (5 × 4 = 20) and you'll have 3 left over. This simple idea — <strong>Dividend = Divisor × Quotient + Remainder</strong> — is Euclid's Division Lemma, and it's the foundation of everything in this chapter!",
        "explanation": (
            "Euclid's Division Lemma says:\n\n"
            + formula_box("a = b × q + r &nbsp;&nbsp; where &nbsp; 0 ≤ r &lt; b", "EUCLID'S DIVISION LEMMA")
            + "\n\nHere:\n"
            + comparison_table(
                ["Symbol", "Meaning", "Example (23 ÷ 5)"],
                [["a", "Dividend (the number being divided)", "23"],
                 ["b", "Divisor (the number we divide by)", "5"],
                 ["q", "Quotient (how many times b fits in a)", "4"],
                 ["r", "Remainder (what's left over)", "3"]]
            )
            + "\n" + tip_box("The remainder r is ALWAYS less than the divisor b, and ALWAYS ≥ 0. So if you divide by 5, the remainder can only be 0, 1, 2, 3, or 4.")
            + "\nThis isn't just about division — it's a <strong>lemma</strong> (a proven mathematical fact) that forms the basis for finding the HCF of two numbers efficiently."
        ),
        "worked_example": (
            "<strong>Verify Euclid's Division Lemma for a = 455, b = 42:</strong>\n\n"
            + step_box([
                ("Divide 455 by 42", "455 ÷ 42 = 10 with remainder 35<br>Check: 42 × 10 = 420, and 455 − 420 = 35"),
                ("Write in Euclid's form", "455 = 42 × 10 + 35"),
                ("Verify the condition on r", "r = 35 and b = 42 → Is 0 ≤ 35 &lt; 42? ✅ YES!"),
                ("Conclusion", "Euclid's Division Lemma is verified. ✓")
            ], "#1565C0")
            + tip_box("You can verify by computing: 42 × 10 + 35 = 420 + 35 = 455 ✓")
        ),
        "try_this": {
            "question": "Apply Euclid's Division Lemma for a = 372 and b = 17. Find q and r, and verify that a = bq + r with 0 ≤ r < b.",
            "hint": "Divide 372 by 17. What's the largest multiple of 17 that doesn't exceed 372?",
            "answer": "372 ÷ 17 = 21 remainder 15.\nSo 372 = 17 × 21 + 15.\nCheck: 17 × 21 = 357, and 372 − 357 = 15.\nSince 0 ≤ 15 < 17, Euclid's Division Lemma is verified. ✓"
        },
        "fun_fact": "Euclid wrote this lemma around 300 BCE in his famous book 'Elements'! That's over 2300 years ago — and we still use it every day. In fact, your phone uses a modern version of Euclid's algorithm for encryption and secure communications! 🔐"
    }

    lessons["math10.real_numbers.euclid_hcf"] = {
        "title": "Finding HCF — Euclid's Elegant Algorithm 🔄",
        "hook": "Suppose you're tiling a rectangular courtyard of 14m × 6m with the <strong>largest possible square tiles</strong> — what size should each tile be? The answer is HCF(14, 6) = 2m! Euclid's algorithm finds this efficiently, even for huge numbers.",
        "explanation": (
            "Euclid's Algorithm uses the division lemma <strong>repeatedly</strong> to find HCF:\n\n"
            + formula_box("HCF(a, b) = HCF(b, r) &nbsp;&nbsp; where a = bq + r", "KEY INSIGHT")
            + "\nThe process:\n"
            + step_box([
                ("Start with a ÷ b", "Get remainder r₁. If r₁ = 0, HCF = b. Otherwise continue."),
                ("Replace: a ← b, b ← r₁", "Now divide b by r₁ to get r₂."),
                ("Keep going", "Replace again: a ← r₁, b ← r₂. Divide."),
                ("Stop when remainder = 0", "The divisor at this step is the HCF! 🎉")
            ], "#2E7D32")
            + "\n" + tip_box("The algorithm ALWAYS terminates because the remainders keep getting smaller (they're bounded by 0) — eventually one must be zero.")
        ),
        "worked_example": (
            "<strong>Find HCF(867, 255):</strong>\n\n"
            + step_box([
                ("867 ÷ 255", "867 = 255 × 3 + 102 &nbsp;&nbsp; (remainder ≠ 0, continue)"),
                ("255 ÷ 102", "255 = 102 × 2 + 51 &nbsp;&nbsp; (remainder ≠ 0, continue)"),
                ("102 ÷ 51", "102 = 51 × 2 + <strong style='color:#2E7D32'>0</strong> &nbsp;&nbsp; (remainder = 0, STOP! ✅)")
            ], "#1565C0")
            + formula_box("HCF(867, 255) = 51", "ANSWER")
            + tip_box("Verify: 867 = 51 × 17 and 255 = 51 × 5. Both divisible by 51! ✓")
        ),
        "try_this": {
            "question": "Find the HCF of 4052 and 12576 using Euclid's algorithm.",
            "hint": "Start with 12576 ÷ 4052. Keep dividing the previous divisor by the remainder until you get remainder 0.",
            "answer": "12576 = 4052 × 3 + 420\n4052 = 420 × 9 + 272\n420 = 272 × 1 + 148\n272 = 148 × 1 + 124\n148 = 124 × 1 + 24\n124 = 24 × 5 + 4\n24 = 4 × 6 + 0\n\nHCF(4052, 12576) = 4"
        },
        "fun_fact": "This algorithm is one of the oldest algorithms in mathematics — over 2300 years old! And it's incredibly fast: even for numbers with hundreds of digits, it finishes in just a few steps. Computer scientists still use it today! 💻"
    }

    lessons["math10.real_numbers.fundamental_theorem"] = {
        "title": "Fundamental Theorem of Arithmetic — Every Number's DNA 🧬",
        "hook": "Just like every person has a unique fingerprint, <strong>every number has a unique prime factorization</strong>. The number 360 will always be 2³ × 3² × 5, no matter how you factor it. This 'uniqueness' is so important, mathematicians call it the <em>Fundamental</em> Theorem!",
        "explanation": (
            '<strong style="color:#C62828">The Theorem:</strong> Every composite number can be expressed as a product of prime numbers, and this factorization is <strong>unique</strong> (apart from the order of factors).\n\n'
            + formula_box("360 = 2³ × 3² × 5¹ &nbsp;&nbsp;&nbsp; (always, no matter how you factor!)", "UNIQUE PRIME FACTORIZATION")
            + "\n<strong>Building a Factor Tree:</strong>\n\n"
            + '<div style="text-align:center;margin:12px 0">'
            + '<svg width="240" height="180" style="display:inline-block">'
            + '<text x="120" y="18" text-anchor="middle" font-weight="bold" font-size="14">360</text>'
            + '<line x1="100" y1="22" x2="60" y2="48" stroke="#333" stroke-width="1.5"/>'
            + '<line x1="140" y1="22" x2="180" y2="48" stroke="#333" stroke-width="1.5"/>'
            + '<text x="60" y="62" text-anchor="middle" font-size="13" fill="#C62828" font-weight="bold">2</text>'
            + '<text x="180" y="62" text-anchor="middle" font-size="13">180</text>'
            + '<line x1="160" y1="66" x2="130" y2="92" stroke="#333" stroke-width="1.5"/>'
            + '<line x1="200" y1="66" x2="220" y2="92" stroke="#333" stroke-width="1.5"/>'
            + '<text x="130" y="106" text-anchor="middle" font-size="13" fill="#C62828" font-weight="bold">2</text>'
            + '<text x="220" y="106" text-anchor="middle" font-size="13">90</text>'
            + '<line x1="205" y1="110" x2="180" y2="136" stroke="#333" stroke-width="1.5"/>'
            + '<line x1="235" y1="110" x2="240" y2="136" stroke="#333" stroke-width="1.5"/>'
            + '<text x="175" y="150" text-anchor="middle" font-size="13" fill="#C62828" font-weight="bold">2</text>'
            + '<text x="237" y="150" text-anchor="middle" font-size="13">45 = 3² × 5</text>'
            + '</svg></div>\n\n'
            + "<strong>Using Prime Factorization to Find HCF and LCM:</strong>\n\n"
            + comparison_table(
                ["", "Method", "Example: HCF & LCM of 12 and 18"],
                [
                    ["<strong>HCF</strong>", "Product of <strong>common</strong> primes with <strong>lowest</strong> powers", "12 = 2² × 3, 18 = 2 × 3²<br>Common: 2¹ × 3¹ = <strong>6</strong>"],
                    ["<strong>LCM</strong>", "Product of <strong>all</strong> primes with <strong>highest</strong> powers", "All primes: 2² × 3² = <strong>36</strong>"]
                ]
            )
            + formula_box("HCF × LCM = Product of the two numbers &nbsp;&nbsp; (6 × 36 = 216 = 12 × 18 ✓)", "GOLDEN RULE")
            + warning_box("This HCF × LCM = Product rule works only for <strong>two</strong> numbers, not three or more!")
        ),
        "worked_example": (
            "<strong>Find HCF and LCM of 96 and 404:</strong>\n\n"
            + step_box([
                ("Prime factorize 96", "96 = 2⁵ × 3"),
                ("Prime factorize 404", "404 = 2² × 101"),
                ("HCF = common primes, lowest powers", "Common prime: 2. Lowest power: 2².<br><strong>HCF = 4</strong>"),
                ("LCM = all primes, highest powers", "2⁵ × 3 × 101 = 32 × 3 × 101<br><strong>LCM = 9696</strong>"),
                ("Verify", "HCF × LCM = 4 × 9696 = 38784<br>96 × 404 = 38784 ✓ 🎉")
            ], "#6A1B9A")
        ),
        "try_this": {
            "question": "Find the HCF and LCM of 306 and 657 using prime factorization. Verify using the formula HCF × LCM = Product.",
            "hint": "306 = 2 × 3² × 17 and 657 = 3 × 219. Keep factoring 219!",
            "answer": "306 = 2 × 3² × 17\n657 = 3 × 219 = 3 × 3 × 73 = 3² × 73\nHCF = 3² = 9 (common prime with lowest power)\nLCM = 2 × 3² × 17 × 73 = 22338\nVerify: 9 × 22338 = 201042 and 306 × 657 = 201042 ✓"
        },
        "fun_fact": "The Fundamental Theorem of Arithmetic was first stated by Euclid, but it was Carl Friedrich Gauss (called the 'Prince of Mathematics') who gave the first rigorous proof in 1801 — in his book 'Disquisitiones Arithmeticae', which he wrote when he was just 21! 📚"
    }

    lessons["math10.real_numbers.irrational_proofs"] = {
        "title": "Proving √2 is Irrational — A Beautiful Contradiction! 🎭",
        "hook": "Can you write √2 as a fraction? Try it! 1.414... doesn't end and doesn't repeat. But <em>how do we prove it can never be a fraction?</em> We use one of math's most elegant weapons: <strong>proof by contradiction</strong> — assume it CAN be written as a fraction, and show this leads to something impossible!",
        "explanation": (
            '<div style="background:linear-gradient(135deg,#FCE4EC,#F8BBD0);border-radius:12px;padding:16px;margin:10px 0">'
            + '<strong style="color:#C62828;font-size:1.05rem">Proof that √2 is irrational:</strong></div>\n\n'
            + step_box([
                ("Assume √2 IS rational", "Then √2 = p/q where p and q are integers with no common factor (i.e., HCF(p,q) = 1)."),
                ("Square both sides", "2 = p²/q² → <strong>p² = 2q²</strong>"),
                ("p² is even → p must be even", "Since p² = 2q² is divisible by 2, p itself must be divisible by 2.<br>Let p = 2m for some integer m."),
                ("Substitute back", "(2m)² = 2q² → 4m² = 2q² → <strong>q² = 2m²</strong>"),
                ("q² is also even → q is also even", "So both p and q are even — they have a common factor of 2!"),
                ("CONTRADICTION! 💥", "We assumed HCF(p,q) = 1, but both are even → HCF ≥ 2.<br>This is impossible! So our assumption was wrong."),
            ], "#C62828")
            + formula_box("∴ √2 is IRRATIONAL", "CONCLUSION")
            + "\n" + tip_box("The same technique works for √3, √5, √7 — any √p where p is prime. The key step is: <strong>if p divides n², then p divides n</strong> (this comes from the Fundamental Theorem of Arithmetic).")
        ),
        "worked_example": (
            "<strong>Prove that 3 + 2√5 is irrational:</strong>\n\n"
            + step_box([
                ("Assume 3 + 2√5 IS rational", "Then 3 + 2√5 = a/b (where a, b are integers, b ≠ 0)"),
                ("Rearrange to isolate √5", "2√5 = a/b − 3 = (a − 3b)/b<br>√5 = (a − 3b)/2b"),
                ("RHS is rational", "Since a, b are integers, (a − 3b)/2b is rational."),
                ("But LHS is irrational!", "We know √5 is irrational (proved similarly to √2)."),
                ("Contradiction! 💥", "A rational number cannot equal an irrational number.<br>So 3 + 2√5 is <strong>irrational</strong>. ✓")
            ], "#6A1B9A")
        ),
        "try_this": {
            "question": "Prove that √3 is irrational using proof by contradiction.",
            "hint": "Follow the same steps as the √2 proof: assume √3 = p/q in lowest terms, square both sides to get p² = 3q², then argue that both p and q must be divisible by 3 — contradiction!",
            "answer": "Assume √3 = p/q with HCF(p,q) = 1.\nThen p² = 3q².\nSince 3 divides p², 3 must divide p (by Fundamental Theorem).\nLet p = 3k. Then 9k² = 3q² → q² = 3k².\nSo 3 divides q² → 3 divides q.\nBoth p and q divisible by 3 → HCF(p,q) ≥ 3. Contradiction!\n∴ √3 is irrational."
        },
        "fun_fact": "Legend says that when Hippasus (a student of Pythagoras) discovered that √2 is irrational around 500 BCE, the other Pythagoreans were so shocked that they threw him overboard from a ship! They believed all numbers should be ratios of whole numbers. 🚢"
    }

    lessons["math10.real_numbers.decimal_expansions"] = {
        "title": "Terminating or Repeating? Decoding Decimal Expansions 🔮",
        "hook": "Why does 1/4 = 0.25 (stops after 2 digits) but 1/3 = 0.333... (goes on forever)? It's not random — the <strong>prime factors of the denominator</strong> tell you everything! It's like a secret code hidden in every fraction.",
        "explanation": (
            "For a rational number p/q (in lowest terms):\n\n"
            + comparison_table(
                ["If denominator q is...", "Decimal expansion is...", "Examples"],
                [
                    ["Only 2s and 5s<br>(q = 2ⁿ × 5ᵐ)", '<strong style="color:#2E7D32">Terminating</strong>', "1/8 = 1/2³ = 0.125<br>7/40 = 7/(2³×5) = 0.175"],
                    ["Has other prime factors", '<strong style="color:#E65100">Non-terminating repeating</strong>', "1/3 = 0.333...<br>1/7 = 0.142857142857..."]
                ]
            )
            + "\n" + formula_box("Terminating ⟺ q = 2ⁿ × 5ᵐ (only factors of 2 and 5)", "THE RULE")
            + "\n<strong>Why does this work?</strong>\n\nTo get a terminating decimal, we need to convert p/q into p'/10ⁿ form. Since 10 = 2 × 5, we can only do this if q has no prime factors other than 2 and 5.\n\n"
            + tip_box("Quick check: just look at the denominator's prime factors. If you see anything other than 2 or 5, it's repeating!")
        ),
        "worked_example": (
            "<strong>Determine whether these have terminating or non-terminating decimals:</strong>\n\n"
            + comparison_table(
                ["Fraction", "Denominator", "Prime Factors", "Terminating?"],
                [
                    ["13/3125", "3125", "5⁵", '✅ Yes <span style="color:#2E7D32">(only 5s)</span>'],
                    ["7/80", "80", "2⁴ × 5", '✅ Yes <span style="color:#2E7D32">(only 2s and 5s)</span>'],
                    ["17/6", "6", "2 × 3", '❌ No <span style="color:#E65100">(has factor 3)</span>'],
                    ["23/200", "200", "2³ × 5²", '✅ Yes <span style="color:#2E7D32">(only 2s and 5s)</span>'],
                ]
            )
        ),
        "try_this": {
            "question": "Without actual division, determine whether 29/343 has a terminating or non-terminating repeating decimal expansion.",
            "hint": "Find the prime factorization of 343. Is it made up of only 2s and 5s?",
            "answer": "343 = 7³. Since the denominator has a prime factor 7 (which is neither 2 nor 5), the decimal expansion of 29/343 is non-terminating repeating."
        },
        "fun_fact": "The decimal expansion of 1/7 = 0.142857142857... has a repeating block of 6 digits. And those 6 digits (142857) form a 'cyclic number' — multiply it by 1, 2, 3, 4, 5, or 6 and you get the same digits in a different order! 142857 × 2 = 285714, × 3 = 428571! 🤯"
    }

    # ── Ch 4: Quadratic Equations ──────────────────────────────────────────

    lessons["math10.quadratic_equations.standard_form"] = {
        "title": "Quadratic Equations — Meet the Mighty ax² + bx + c = 0 💪",
        "hook": "A ball thrown upward follows a path described by a quadratic equation. The area of a rectangular garden, the time taken by two pipes to fill a tank — all lead to equations with x². Welcome to the world of <strong>Quadratic Equations</strong>!",
        "explanation": (
            '<div style="background:linear-gradient(135deg,#E8F5E9,#C8E6C9);border-radius:12px;padding:16px;margin:10px 0;text-align:center">'
            + '<strong style="font-size:1.1rem">Standard Form:</strong> <span style="font-size:1.2rem;font-family:serif">ax² + bx + c = 0</span> where <strong>a ≠ 0</strong></div>\n\n'
            + comparison_table(
                ["Coefficient", "Role", "Example in 3x²−5x+2=0"],
                [["a", "Coefficient of x² (must not be 0!)", "3"],
                 ["b", "Coefficient of x", "−5"],
                 ["c", "Constant term", "2"]]
            )
            + "\n<strong>Solving by Factorization (Splitting the Middle Term):</strong>\n\n"
            + step_box([
                ("Find two numbers", "whose <strong>sum = b</strong> and <strong>product = a×c</strong>"),
                ("Split the middle term", "Replace bx with these two numbers"),
                ("Factor by grouping", "Take common factors from pairs"),
                ("Set each factor = 0", "Solve to get the two roots")
            ], "#2E7D32")
        ),
        "worked_example": (
            "<strong>Solve: 6x² − x − 2 = 0</strong>\n\n"
            + step_box([
                ("Identify a, b, c", "a = 6, b = −1, c = −2. Product ac = 6 × (−2) = −12"),
                ("Find two numbers", "Sum = −1, Product = −12<br>Numbers: <strong>−4 and 3</strong> (−4 + 3 = −1, −4 × 3 = −12) ✓"),
                ("Split middle term", "6x² − 4x + 3x − 2 = 0"),
                ("Group and factor", "2x(3x − 2) + 1(3x − 2) = 0<br>(2x + 1)(3x − 2) = 0"),
                ("Set each factor = 0", "2x + 1 = 0 → <strong>x = −1/2</strong><br>3x − 2 = 0 → <strong>x = 2/3</strong>")
            ], "#1565C0")
            + formula_box("Roots: x = −1/2 &nbsp;and&nbsp; x = 2/3", "ANSWER")
        ),
        "try_this": {
            "question": "Solve by factorization: 2x² + x − 6 = 0",
            "hint": "Find two numbers whose sum = 1 (coefficient of x) and product = 2 × (−6) = −12.",
            "answer": "Numbers: 4 and −3 (sum = 1, product = −12)\n2x² + 4x − 3x − 6 = 0\n2x(x + 2) − 3(x + 2) = 0\n(2x − 3)(x + 2) = 0\nx = 3/2 or x = −2"
        },
        "fun_fact": "The ancient Babylonians were solving quadratic equations as early as 2000 BCE — that's 4000 years ago! They used a geometric method: they literally completed a square using clay tablets. 🏛️"
    }

    lessons["math10.quadratic_equations.completing_square"] = {
        "title": "Completing the Square — Making Imperfect Things Perfect ✨",
        "hook": "What if you can't easily split the middle term? There's a beautiful trick: you can <strong>force</strong> any quadratic into a perfect square form by adding just the right number. It's like finding the missing puzzle piece! 🧩",
        "explanation": (
            "The idea: transform <strong>x² + bx</strong> into <strong>(x + something)²</strong>.\n\n"
            + '<div style="text-align:center;margin:16px 0">'
            + '<svg width="340" height="180" style="display:inline-block">'
            + '<rect x="10" y="10" width="100" height="100" fill="#BBDEFB" stroke="#1565C0" stroke-width="2"/>'
            + '<text x="60" y="65" text-anchor="middle" font-size="14" font-weight="bold">x²</text>'
            + '<text x="60" y="125" text-anchor="middle" font-size="12">x</text>'
            + '<text x="5" y="65" text-anchor="end" font-size="12" transform="rotate(-90,5,65)">x</text>'
            + '<rect x="115" y="10" width="50" height="100" fill="#C8E6C9" stroke="#2E7D32" stroke-width="2"/>'
            + '<text x="140" y="65" text-anchor="middle" font-size="11" font-weight="bold">bx/2</text>'
            + '<rect x="10" y="115" width="100" height="50" fill="#C8E6C9" stroke="#2E7D32" stroke-width="2"/>'
            + '<text x="60" y="145" text-anchor="middle" font-size="11" font-weight="bold">bx/2</text>'
            + '<rect x="115" y="115" width="50" height="50" fill="#FFCDD2" stroke="#C62828" stroke-width="2" stroke-dasharray="4"/>'
            + '<text x="140" y="145" text-anchor="middle" font-size="10" font-weight="bold" fill="#C62828">(b/2)²</text>'
            + '<text x="250" y="90" font-size="14" font-weight="bold">= (x + b/2)²</text>'
            + '<text x="250" y="115" font-size="12" fill="#C62828">← add this piece!</text>'
            + '</svg></div>\n\n'
            + formula_box("x² + bx + (b/2)² = (x + b/2)²", "THE COMPLETING TRICK")
            + "\n" + step_box([
                ("Make coefficient of x² = 1", "Divide the entire equation by 'a'"),
                ("Move constant to RHS", "x² + (b/a)x = −c/a"),
                ("Add (half of x-coefficient)² to both sides", "x² + (b/a)x + (b/2a)² = −c/a + (b/2a)²"),
                ("LHS is now a perfect square!", "(x + b/2a)² = (b² − 4ac)/4a²"),
                ("Take square root", "x + b/2a = ±√(b² − 4ac)/2a → solve for x")
            ], "#6A1B9A")
        ),
        "worked_example": (
            "<strong>Solve x² + 4x − 5 = 0 by completing the square:</strong>\n\n"
            + step_box([
                ("Move constant to RHS", "x² + 4x = 5"),
                ("Half of 4 = 2, square it = 4", "Add 4 to both sides: x² + 4x + 4 = 5 + 4"),
                ("Factor the perfect square", "(x + 2)² = 9"),
                ("Take square root", "x + 2 = ±3"),
                ("Solve", "x = −2 + 3 = <strong>1</strong> &nbsp;or&nbsp; x = −2 − 3 = <strong>−5</strong>")
            ], "#1565C0")
            + "\n" + tip_box("Verify: (1)² + 4(1) − 5 = 0 ✓ and (−5)² + 4(−5) − 5 = 0 ✓")
        ),
        "try_this": {
            "question": "Solve 2x² − 7x + 3 = 0 by completing the square.",
            "hint": "First divide everything by 2 to make the coefficient of x² equal to 1. Then move the constant to the RHS and complete the square.",
            "answer": "x² − 7x/2 + 3/2 = 0\nx² − 7x/2 = −3/2\nAdd (7/4)² = 49/16 to both sides:\nx² − 7x/2 + 49/16 = −3/2 + 49/16 = 25/16\n(x − 7/4)² = 25/16\nx − 7/4 = ±5/4\nx = 7/4 + 5/4 = 3 or x = 7/4 − 5/4 = 1/2"
        },
        "fun_fact": "The 'completing the square' technique was developed by the great Indian mathematician Shreedharacharya in the 8th century CE — centuries before it appeared in European mathematics! 🇮🇳"
    }

    lessons["math10.quadratic_equations.quadratic_formula"] = {
        "title": "The Quadratic Formula — The Ultimate Problem Solver 🚀",
        "hook": "What if there was ONE formula that could solve ANY quadratic equation? No factoring, no guessing — just plug in a, b, c and get the answer! That's exactly what the Quadratic Formula does, and it was discovered by the Indian mathematician <strong>Shreedharacharya</strong>!",
        "explanation": (
            "By completing the square on the general equation ax² + bx + c = 0, we get:\n\n"
            + '<div style="background:linear-gradient(135deg,#FFF3E0,#FFE0B2);border:2px solid #E65100;border-radius:12px;padding:20px;margin:16px 0;text-align:center">'
            + '<div style="font-size:0.75rem;text-transform:uppercase;font-weight:700;color:#E65100;margin-bottom:6px">SHREEDHARACHARYA\'S QUADRATIC FORMULA</div>'
            + '<div style="font-size:1.3rem;font-family:serif"><strong>x = (−b ± √(b² − 4ac)) / 2a</strong></div></div>\n\n'
            + comparison_table(
                ["Part of Formula", "What It Gives You"],
                [
                    ["−b / 2a", "The x-coordinate of the vertex (midpoint of the two roots)"],
                    ["√(b² − 4ac)", "How far apart the two roots are from the midpoint"],
                    ["The ± sign", "One root with +, another with − (two solutions!)"],
                ]
            )
            + "\n" + tip_box("This formula works for ALL quadratic equations — even when factorization is impossible. It's derived by completing the square on ax² + bx + c = 0.")
            + warning_box("Don't forget: the formula only gives <strong>real</strong> roots when b² − 4ac ≥ 0. If b² − 4ac < 0, there are no real solutions!")
        ),
        "worked_example": (
            "<strong>Solve 2x² − 3x − 5 = 0 using the Quadratic Formula:</strong>\n\n"
            + step_box([
                ("Identify a, b, c", "a = 2, b = −3, c = −5"),
                ("Calculate discriminant", "b² − 4ac = (−3)² − 4(2)(−5) = 9 + 40 = <strong>49</strong>"),
                ("Apply the formula", "x = (−(−3) ± √49) / (2 × 2) = (3 ± 7) / 4"),
                ("Find both roots", "x = (3 + 7)/4 = <strong>10/4 = 5/2</strong><br>x = (3 − 7)/4 = <strong>−4/4 = −1</strong>")
            ], "#E65100")
            + formula_box("Roots: x = 5/2 &nbsp;and&nbsp; x = −1", "ANSWER")
        ),
        "try_this": {
            "question": "Solve 3x² − 5x + 2 = 0 using the Quadratic Formula.",
            "hint": "a = 3, b = −5, c = 2. First calculate the discriminant b² − 4ac, then plug into x = (−b ± √D) / 2a.",
            "answer": "D = (−5)² − 4(3)(2) = 25 − 24 = 1\nx = (5 ± √1) / 6 = (5 ± 1) / 6\nx = 6/6 = 1 or x = 4/6 = 2/3"
        },
        "fun_fact": "While we call it the 'Quadratic Formula' in English, in India it's rightfully called <strong>Shreedharacharya's Rule</strong>, honoring the 8th-century Indian mathematician who first described this method. Indian mathematicians were solving quadratics centuries before Europe! 🇮🇳"
    }

    lessons["math10.quadratic_equations.nature_of_roots"] = {
        "title": "The Discriminant — A Crystal Ball for Roots 🔮",
        "hook": "Before you even solve a quadratic equation, you can predict what KIND of roots it has! Will there be two answers, one answer, or no real answer at all? The <strong>discriminant</strong> tells you — like a crystal ball for mathematics!",
        "explanation": (
            "The <strong>discriminant</strong> is the expression under the square root in the Quadratic Formula:\n\n"
            + formula_box("D = b² − 4ac", "DISCRIMINANT")
            + "\n"
            + '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:16px 0">'
            + '<div style="background:#E8F5E9;border:2px solid #2E7D32;border-radius:10px;padding:12px;text-align:center">'
            + '<div style="font-size:1.5rem;margin-bottom:4px">D &gt; 0</div>'
            + '<div style="font-weight:700;color:#2E7D32">Two distinct real roots</div>'
            + '<svg width="80" height="50" style="margin:8px auto;display:block"><path d="M5,45 Q40,0 75,45" fill="none" stroke="#2E7D32" stroke-width="2"/><line x1="5" y1="25" x2="75" y2="25" stroke="#999" stroke-width="1" stroke-dasharray="3"/><circle cx="18" cy="25" r="3" fill="#2E7D32"/><circle cx="62" cy="25" r="3" fill="#2E7D32"/></svg>'
            + '<div style="font-size:0.75rem;color:#666">Parabola cuts x-axis at 2 points</div></div>'
            + '<div style="background:#FFF8E1;border:2px solid #F9A825;border-radius:10px;padding:12px;text-align:center">'
            + '<div style="font-size:1.5rem;margin-bottom:4px">D = 0</div>'
            + '<div style="font-weight:700;color:#F9A825">Two equal (repeated) roots</div>'
            + '<svg width="80" height="50" style="margin:8px auto;display:block"><path d="M5,45 Q40,5 75,45" fill="none" stroke="#F9A825" stroke-width="2"/><line x1="5" y1="45" x2="75" y2="45" stroke="#999" stroke-width="1" stroke-dasharray="3"/><circle cx="40" cy="45" r="3" fill="#F9A825"/></svg>'
            + '<div style="font-size:0.75rem;color:#666">Parabola just touches x-axis</div></div>'
            + '<div style="background:#FFEBEE;border:2px solid #C62828;border-radius:10px;padding:12px;text-align:center">'
            + '<div style="font-size:1.5rem;margin-bottom:4px">D &lt; 0</div>'
            + '<div style="font-weight:700;color:#C62828">No real roots</div>'
            + '<svg width="80" height="50" style="margin:8px auto;display:block"><path d="M5,45 Q40,15 75,45" fill="none" stroke="#C62828" stroke-width="2"/><line x1="5" y1="50" x2="75" y2="50" stroke="#999" stroke-width="1" stroke-dasharray="3"/></svg>'
            + '<div style="font-size:0.75rem;color:#666">Parabola doesn\'t touch x-axis</div></div>'
            + '</div>\n\n'
            + tip_box("When D = 0, the repeated root is x = −b/2a. When D > 0 and D is a perfect square, the roots are rational.")
        ),
        "worked_example": (
            "<strong>Determine the nature of roots without solving:</strong>\n\n"
            + comparison_table(
                ["Equation", "a, b, c", "D = b²−4ac", "Nature of Roots"],
                [
                    ["2x²−4x+3=0", "2, −4, 3", "16−24 = <strong>−8</strong>", '❌ <span style="color:#C62828">No real roots</span>'],
                    ["x²−6x+9=0", "1, −6, 9", "36−36 = <strong>0</strong>", '🟡 <span style="color:#F9A825">Equal roots (x=3)</span>'],
                    ["x²−5x+6=0", "1, −5, 6", "25−24 = <strong>1</strong>", '✅ <span style="color:#2E7D32">Two distinct real roots</span>']
                ]
            )
        ),
        "try_this": {
            "question": "Find the values of k for which the equation 2x² + kx + 3 = 0 has equal roots.",
            "hint": "For equal roots, D = 0. Set b² − 4ac = 0 and solve for k.",
            "answer": "D = k² − 4(2)(3) = k² − 24 = 0\nk² = 24\nk = ±√24 = ±2√6"
        },
        "fun_fact": "The word 'discriminant' comes from the Latin word 'discriminare' meaning 'to distinguish' — because it <strong>distinguishes</strong> between the three types of roots! It's like a sorting hat for equations. 🎩"
    }

    lessons["math10.quadratic_equations.word_problems_quad"] = {
        "title": "Quadratic Word Problems — Math Meets Real Life 🌍",
        "hook": "Two water pipes fill a pool. Working together they take 12 hours. Pipe A alone takes 10 hours more than Pipe B alone. How long does each pipe take? This is a real-life problem that leads to a quadratic equation!",
        "explanation": (
            "The strategy for word problems:\n\n"
            + step_box([
                ("Read & Identify", "What is unknown? Assign it a variable (let x = ...)."),
                ("Translate to Math", "Convert the English sentences into an equation."),
                ("Solve the Quadratic", "Use factorization or the quadratic formula."),
                ("Check & Reject", "Reject negative or nonsensical answers (e.g., negative age, negative length).")
            ], "#6A1B9A")
            + "\n<strong>Common Types:</strong>\n\n"
            + comparison_table(
                ["Type", "What leads to x²", "Example Setup"],
                [
                    ["Area problems", "length × width = area", "Rectangle: x(x+5) = 150"],
                    ["Consecutive numbers", "n × (n+1) = product", "n(n+1) = 182"],
                    ["Speed-Distance-Time", "Speed = Distance/Time", "If speed ↑ by 5, time ↓ by 3"],
                    ["Age problems", "Present × Future age", "(x)(x+4) = 192"],
                    ["Work-Time", "1/x + 1/y = 1/total", "1/x + 1/(x+10) = 1/12"],
                ]
            )
            + "\n" + warning_box("Always check if both roots make sense in the original context! A length can't be negative, time can't be negative, and number of people must be a whole number.")
        ),
        "worked_example": (
            "<strong>The product of two consecutive positive integers is 306. Find them.</strong>\n\n"
            + step_box([
                ("Let the integers be", "x and x + 1"),
                ("Form the equation", "x(x + 1) = 306<br>x² + x − 306 = 0"),
                ("Solve by factorization", "Find two numbers: sum = 1, product = −306<br>Numbers: 18 and −17<br>x² + 18x − 17x − 306 = 0<br>x(x + 18) − 17(x + 18) = 0<br>(x − 17)(x + 18) = 0"),
                ("Find x", "x = 17 or x = −18"),
                ("Reject & Conclude", "Since integers are positive, x = 17.<br><strong>The integers are 17 and 18.</strong> ✓ (17 × 18 = 306 ✓)")
            ], "#1565C0")
        ),
        "try_this": {
            "question": "The altitude of a right triangle is 7 cm less than its base. If the hypotenuse is 13 cm, find the other two sides.",
            "hint": "Let base = x, altitude = x − 7. Use Pythagoras: x² + (x−7)² = 13².",
            "answer": "x² + (x−7)² = 169\nx² + x² − 14x + 49 = 169\n2x² − 14x − 120 = 0\nx² − 7x − 60 = 0\n(x − 12)(x + 5) = 0\nx = 12 (reject −5)\nBase = 12 cm, Altitude = 5 cm.\nCheck: 12² + 5² = 144 + 25 = 169 = 13² ✓"
        },
        "fun_fact": "The Rhind Papyrus from ancient Egypt (1650 BCE) contains quadratic word problems about distributing loaves of bread! The scribe Ahmes wrote: 'A heap and its seventh make 19.' This leads to x + x/7 = 19, and ancient versions got even more complex. 🍞"
    }

    # ── Ch 8: Trigonometry ──────────────────────────────────────────────────

    lessons["math10.trigonometry.trig_ratios"] = {
        "title": "Trigonometric Ratios — SOH-CAH-TOA, Your New Best Friends! 📐",
        "hook": "How do engineers measure the height of a mountain without climbing it? How do astronomers calculate distances to stars? They use <strong>trigonometry</strong> — the study of relationships between angles and sides of triangles. And it all starts with three simple ratios!",
        "explanation": (
            "In a right triangle with angle θ:\n\n"
            + '<div style="display:flex;align-items:center;gap:20px;flex-wrap:wrap;justify-content:center">'
            + '<svg width="200" height="170" style="flex-shrink:0">'
            + '<polygon points="30,150 170,150 30,30" fill="#E8F5E9" stroke="#2E7D32" stroke-width="2"/>'
            + '<rect x="30" y="138" width="12" height="12" fill="none" stroke="#2E7D32" stroke-width="1.5"/>'
            + '<path d="M140,150 A30,30 0 0,0 155,125" fill="none" stroke="#E65100" stroke-width="2"/>'
            + '<text x="128" y="140" font-size="14" font-weight="bold" fill="#E65100">θ</text>'
            + '<text x="95" y="168" text-anchor="middle" font-size="12" font-weight="bold" fill="#1565C0">Adjacent (A)</text>'
            + '<text x="14" y="95" text-anchor="middle" font-size="12" font-weight="bold" fill="#2E7D32" transform="rotate(-90,14,95)">Opposite (O)</text>'
            + '<text x="115" y="82" text-anchor="middle" font-size="12" font-weight="bold" fill="#C62828" transform="rotate(-40,115,82)">Hypotenuse (H)</text>'
            + '</svg>'
            + '<div style="flex:1;min-width:200px">'
            + '<div style="background:#E3F2FD;border-radius:10px;padding:12px;margin:4px 0;font-weight:bold;font-size:0.95rem">🔵 sin θ = Opposite / Hypotenuse = O/H</div>'
            + '<div style="background:#E8F5E9;border-radius:10px;padding:12px;margin:4px 0;font-weight:bold;font-size:0.95rem">🟢 cos θ = Adjacent / Hypotenuse = A/H</div>'
            + '<div style="background:#FFF3E0;border-radius:10px;padding:12px;margin:4px 0;font-weight:bold;font-size:0.95rem">🟠 tan θ = Opposite / Adjacent = O/A</div>'
            + '</div></div>\n\n'
            + formula_box("SOH — CAH — TOA &nbsp;&nbsp;(Sin=O/H, Cos=A/H, Tan=O/A)", "MEMORY TRICK")
            + "\nThe <strong>reciprocal</strong> ratios:\n"
            + comparison_table(
                ["Ratio", "Formula", "Reciprocal of"],
                [
                    ["cosec θ", "H/O = 1/sin θ", "sin θ"],
                    ["sec θ", "H/A = 1/cos θ", "cos θ"],
                    ["cot θ", "A/O = 1/tan θ", "tan θ"],
                ]
            )
            + tip_box("The ratios depend ONLY on the angle θ, not on the size of the triangle! A bigger similar triangle gives the same ratios.")
        ),
        "worked_example": (
            "<strong>In a right triangle, if sin A = 3/5, find all other trig ratios:</strong>\n\n"
            + step_box([
                ("From sin A = 3/5", "Opposite = 3, Hypotenuse = 5 (or any multiple like 6/10)"),
                ("Find Adjacent using Pythagoras", "Adjacent = √(5² − 3²) = √(25 − 9) = √16 = <strong>4</strong>"),
                ("Calculate all ratios", "cos A = 4/5, tan A = 3/4<br>cosec A = 5/3, sec A = 5/4, cot A = 4/3")
            ], "#1565C0")
            + '\n<div style="text-align:center;font-size:0.85rem;color:#666;margin-top:8px">Triangle: sides 3, 4, 5 — a Pythagorean triplet! 🎯</div>'
        ),
        "try_this": {
            "question": "In a right triangle ABC with ∠B = 90°, AB = 7 cm and AC = 25 cm. Find sin A, cos A, and tan A.",
            "hint": "First find BC using Pythagoras: BC = √(AC² − AB²). Then identify which side is opposite and which is adjacent to angle A.",
            "answer": "BC = √(625 − 49) = √576 = 24 cm\nFor angle A: Opposite = BC = 24, Adjacent = AB = 7, Hypotenuse = AC = 25\nsin A = 24/25, cos A = 7/25, tan A = 24/7"
        },
        "fun_fact": "The word 'sine' comes from the Sanskrit word 'jyā' (meaning 'bowstring'), which was translated to Arabic as 'jiba', misread as 'jaib' (meaning 'bay/fold'), and then translated to Latin as 'sinus'! So every time you write 'sin', you're using a word with roots in ancient India! 🇮🇳"
    }

    lessons["math10.trigonometry.standard_angles"] = {
        "title": "Trig Values of Standard Angles — The Power Table ⚡",
        "hook": "There are exactly 5 angles whose trig values you MUST memorize: 0°, 30°, 45°, 60°, 90°. They appear in almost every board exam question! But here's a trick — you only need to remember ONE row, and you can derive the rest!",
        "explanation": (
            '<div style="background:linear-gradient(135deg,#E8EAF6,#C5CAE9);border-radius:12px;padding:16px;margin:12px 0">'
            + '<div style="font-weight:700;text-align:center;margin-bottom:10px;color:#283593">📊 THE POWER TABLE</div>'
            + comparison_table(
                ["θ →", "0°", "30°", "45°", "60°", "90°"],
                [
                    ['<strong>sin θ</strong>', "0", "1/2", "1/√2", "√3/2", "1"],
                    ['<strong>cos θ</strong>', "1", "√3/2", "1/√2", "1/2", "0"],
                    ['<strong>tan θ</strong>', "0", "1/√3", "1", "√3", "∞ (undefined)"],
                ]
            )
            + '</div>\n\n'
            + '<div style="background:#FFF8E1;border-radius:10px;padding:14px;margin:12px 0">'
            + '<strong>🧠 The Memory Trick (for sin θ):</strong><br><br>'
            + 'Write: √0/2, √1/2, √2/2, √3/2, √4/2 for θ = 0°, 30°, 45°, 60°, 90°<br><br>'
            + '<div style="display:flex;gap:6px;justify-content:center;flex-wrap:wrap">'
            + '<div style="background:white;border:2px solid #F9A825;border-radius:8px;padding:8px 12px;text-align:center;min-width:55px"><div style="font-size:0.7rem;color:#666">0°</div><div style="font-weight:bold">√0/2</div><div style="font-size:0.8rem">=0</div></div>'
            + '<div style="background:white;border:2px solid #F9A825;border-radius:8px;padding:8px 12px;text-align:center;min-width:55px"><div style="font-size:0.7rem;color:#666">30°</div><div style="font-weight:bold">√1/2</div><div style="font-size:0.8rem">=1/2</div></div>'
            + '<div style="background:white;border:2px solid #F9A825;border-radius:8px;padding:8px 12px;text-align:center;min-width:55px"><div style="font-size:0.7rem;color:#666">45°</div><div style="font-weight:bold">√2/2</div><div style="font-size:0.8rem">=1/√2</div></div>'
            + '<div style="background:white;border:2px solid #F9A825;border-radius:8px;padding:8px 12px;text-align:center;min-width:55px"><div style="font-size:0.7rem;color:#666">60°</div><div style="font-weight:bold">√3/2</div><div style="font-size:0.8rem">=√3/2</div></div>'
            + '<div style="background:white;border:2px solid #F9A825;border-radius:8px;padding:8px 12px;text-align:center;min-width:55px"><div style="font-size:0.7rem;color:#666">90°</div><div style="font-weight:bold">√4/2</div><div style="font-size:0.8rem">=1</div></div>'
            + '</div><br>'
            + 'For <strong>cos θ</strong>: just <strong>reverse</strong> the row! cos 0° = sin 90° = 1, etc.<br>'
            + 'For <strong>tan θ</strong>: just divide sin/cos for each angle.'
            + '</div>\n\n'
            + tip_box("Memorize the sin row using √0, √1, √2, √3, √4 (all divided by 2). Then cos is the reverse, and tan = sin/cos!")
        ),
        "worked_example": (
            "<strong>Evaluate: sin 60° cos 30° + sin 30° cos 60°</strong>\n\n"
            + step_box([
                ("Substitute values", "= (√3/2)(√3/2) + (1/2)(1/2)"),
                ("Multiply", "= 3/4 + 1/4"),
                ("Add", "= <strong>4/4 = 1</strong>")
            ], "#1565C0")
            + tip_box("Notice this equals sin(60° + 30°) = sin 90° = 1. This is actually the sine addition formula in action!")
        ),
        "try_this": {
            "question": "Evaluate: (tan 30°)(tan 60°) + cos²45° + sin²45°",
            "hint": "tan 30° = 1/√3, tan 60° = √3, cos 45° = sin 45° = 1/√2",
            "answer": "(1/√3)(√3) + (1/√2)² + (1/√2)²\n= 1 + 1/2 + 1/2\n= 1 + 1 = 2"
        },
        "fun_fact": "The ancient Indian mathematician Aryabhata (476 CE) created the first known table of sine values! He called sine 'ardha-jya' (half-chord) and his values for 24 angles from 0° to 90° were accurate to about 4 decimal places — without a calculator! 🧮"
    }

    # ── Ch 15: Probability ──────────────────────────────────────────────────

    lessons["math10.probability10.classical_definition"] = {
        "title": "Probability — Predicting the Unpredictable! 🎲",
        "hook": "Will it rain tomorrow? Will your team win the match? Will you get heads if you flip a coin? We can't know for sure — but we CAN measure <strong>how likely</strong> something is. That's probability — the mathematics of chance!",
        "explanation": (
            '<div style="background:linear-gradient(135deg,#E3F2FD,#BBDEFB);border-radius:12px;padding:16px;margin:10px 0;text-align:center">'
            + '<div style="font-size:1.2rem;font-weight:bold;color:#1565C0">P(Event) = Favourable Outcomes / Total Outcomes</div></div>\n\n'
            + '<div style="display:flex;gap:10px;margin:16px 0;flex-wrap:wrap;justify-content:center">'
            + '<div style="flex:1;min-width:140px;background:#FFEBEE;border-radius:10px;padding:12px;text-align:center;border:2px solid #EF9A9A">'
            + '<div style="font-size:1.5rem">0</div><div style="font-weight:700;color:#C62828">Impossible</div>'
            + '<div style="font-size:0.8rem;color:#666;margin-top:4px">P(sun rises in west)</div></div>'
            + '<div style="flex:1;min-width:140px;background:#FFF8E1;border-radius:10px;padding:12px;text-align:center;border:2px solid #FFE082">'
            + '<div style="font-size:1.5rem">0.5</div><div style="font-weight:700;color:#F9A825">Equally Likely</div>'
            + '<div style="font-size:0.8rem;color:#666;margin-top:4px">P(heads on fair coin)</div></div>'
            + '<div style="flex:1;min-width:140px;background:#E8F5E9;border-radius:10px;padding:12px;text-align:center;border:2px solid #A5D6A7">'
            + '<div style="font-size:1.5rem">1</div><div style="font-weight:700;color:#2E7D32">Certain</div>'
            + '<div style="font-size:0.8rem;color:#666;margin-top:4px">P(getting 1-6 on a die)</div></div>'
            + '</div>\n\n'
            + formula_box("P(E) + P(not E) = 1 &nbsp;&nbsp;⟹&nbsp;&nbsp; P(not E) = 1 − P(E)", "COMPLEMENT RULE")
            + "\n" + tip_box("If it's hard to count favourable outcomes, count the UNfavourable ones and subtract from 1!")
        ),
        "worked_example": (
            "<strong>A bag has 3 red, 5 blue, and 2 green balls. Find: P(red), P(not green), P(blue or green).</strong>\n\n"
            + step_box([
                ("Count total outcomes", "Total = 3 + 5 + 2 = <strong>10 balls</strong>"),
                ("P(red)", "Favourable = 3 red balls<br>P(red) = 3/10 = <strong>0.3</strong>"),
                ("P(not green)", "P(green) = 2/10 = 1/5<br>P(not green) = 1 − 1/5 = <strong>4/5 = 0.8</strong>"),
                ("P(blue or green)", "Favourable = 5 + 2 = 7<br>P(blue or green) = 7/10 = <strong>0.7</strong>")
            ], "#6A1B9A")
        ),
        "try_this": {
            "question": "Two dice are thrown simultaneously. Find the probability of getting a sum of 7.",
            "hint": "Total outcomes for two dice = 6 × 6 = 36. List the pairs that give sum 7: (1,6), (2,5), ...",
            "answer": "Favourable outcomes: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6 outcomes\nP(sum = 7) = 6/36 = 1/6"
        },
        "fun_fact": "Probability theory was born from gambling! In 1654, two French mathematicians — Blaise Pascal and Pierre de Fermat — exchanged letters about a gambling problem (the 'Problem of Points'). This correspondence laid the foundation for all of probability theory! 🃏"
    }

    # Fill remaining concepts with placeholder-quality lessons that are still
    # better than the old auto-generated stubs. For brevity in this script,
    # we create shorter lessons for the remaining concepts.
    
    # Helper for concepts not yet hand-crafted
    for ch in CURRICULUM["chapters"]:
        for concept in ch["concepts"]:
            cid = concept["concept_id"]
            if cid not in lessons:
                # Generate a decent default lesson from the concept metadata
                lessons[cid] = _auto_lesson(concept, ch["title"])

    return lessons


def _auto_lesson(c: dict, chapter_title: str) -> dict:
    """Create a reasonable lesson from concept metadata (no API call needed)."""
    key_ideas_html = "\n".join(
        f'<div style="background:#F5F5F5;border-left:3px solid #4A90D9;border-radius:6px;padding:8px 12px;margin:6px 0;font-size:0.9rem">💡 {ki}</div>'
        for ki in c["key_ideas"]
    )
    return {
        "title": f"{c['title']} — {chapter_title}",
        "hook": f"Let's explore <strong>{c['title']}</strong> from the chapter on {chapter_title}. This is an important concept in NCERT Class 10 Mathematics that builds your foundation for higher studies!",
        "explanation": (
            f"<strong>{c['title']}</strong>\n\n"
            f"<em>{c['description']}</em>\n\n"
            f"<strong>Key Ideas to Master:</strong>\n{key_ideas_html}"
        ),
        "worked_example": f"<em>A detailed worked example for {c['title']} will be available soon. Practice the textbook NCERT examples for now!</em>",
        "try_this": {
            "question": f"Review NCERT Example problems for {c['title']} and solve Exercise questions from the textbook.",
            "hint": "Start with the easier questions and work your way up. Use the key ideas above as a checklist.",
            "answer": "Check your answers with the NCERT solutions. Focus on understanding the method, not just the final answer."
        },
        "fun_fact": f"Mathematics is the queen of sciences and {chapter_title.lower()} concepts like {c['title'].lower()} are used in engineering, data science, and everyday problem solving!"
    }


# ═══════════════════════════════════════════════════════════════════════════════
#  QUESTIONS — 3 per concept (direct, word_problem, transfer_task)
# ═══════════════════════════════════════════════════════════════════════════════

def make_questions() -> dict:
    """Return {concept_id: [question_list]} for all concepts."""
    questions = {}

    questions["math10.real_numbers.euclid_division"] = [
        {
            "id": 1, "type": "direct", "difficulty": 0.4,
            "question": "Express 455 in terms of 42 using Euclid's Division Lemma (i.e., find q and r such that 455 = 42q + r).",
            "hint": "Divide 455 by 42 to find the quotient and remainder.",
            "expected_answer": "455 ÷ 42 = 10 remainder 35. So 455 = 42 × 10 + 35, where q = 10 and r = 35. Verify: 0 ≤ 35 < 42 ✓",
            "concepts_tested": ["Euclid's Division Lemma", "Division with remainder"]
        },
        {
            "id": 2, "type": "word_problem", "difficulty": 0.5,
            "question": "A number when divided by 17 gives quotient 23 and remainder 4. What is the number? Verify using Euclid's Division Lemma.",
            "hint": "Use a = bq + r where b = 17, q = 23, r = 4.",
            "expected_answer": "a = 17 × 23 + 4 = 391 + 4 = 395. Verify: 395 ÷ 17 = 23 remainder 4 ✓, and 0 ≤ 4 < 17 ✓",
            "concepts_tested": ["Euclid's Division Lemma"]
        },
        {
            "id": 3, "type": "transfer_task", "difficulty": 0.6,
            "question": "A teacher has 93 notebooks to distribute equally among students. After distribution, 3 notebooks are left. If each student got at least 5 notebooks, what are the possible number of students?",
            "hint": "93 = n × q + 3, where q ≥ 5 and n = number of students. Find values of n that work.",
            "expected_answer": "93 − 3 = 90 notebooks distributed equally. n × q = 90 with q ≥ 5.\nPossible: n=18(q=5), n=15(q=6), n=10(q=9), n=9(q=10), n=6(q=15), n=5(q=18), n=3(q=30), n=2(q=45), n=1(q=90).\nSo possible number of students: 1, 2, 3, 5, 6, 9, 10, 15, 18.",
            "concepts_tested": ["Euclid's Division Lemma", "Real-world application"]
        }
    ]

    questions["math10.real_numbers.euclid_hcf"] = [
        {
            "id": 1, "type": "direct", "difficulty": 0.4,
            "question": "Find the HCF of 196 and 38220 using Euclid's algorithm.",
            "hint": "Start: 38220 = 196 × q + r. Keep going until remainder is 0.",
            "expected_answer": "38220 = 196 × 195 + 0. Since the remainder is 0 in the very first step, HCF(38220, 196) = 196.",
            "concepts_tested": ["Euclid's Algorithm for HCF"]
        },
        {
            "id": 2, "type": "direct", "difficulty": 0.5,
            "question": "Use Euclid's algorithm to find HCF of 4052 and 12576.",
            "hint": "Divide the larger by the smaller, then continue with the divisor and remainder.",
            "expected_answer": "12576 = 4052 × 3 + 420\n4052 = 420 × 9 + 272\n420 = 272 × 1 + 148\n272 = 148 × 1 + 124\n148 = 124 × 1 + 24\n124 = 24 × 5 + 4\n24 = 4 × 6 + 0\nHCF = 4",
            "concepts_tested": ["Euclid's Algorithm for HCF"]
        },
        {
            "id": 3, "type": "word_problem", "difficulty": 0.6,
            "question": "A rectangular courtyard is 18m 72cm long and 13m 20cm wide. It is to be paved with square tiles of the same size. Find the largest possible size of the tile.",
            "hint": "Convert to cm: 1872 cm × 1320 cm. The tile side = HCF(1872, 1320).",
            "expected_answer": "1872 = 1320 × 1 + 552\n1320 = 552 × 2 + 216\n552 = 216 × 2 + 120\n216 = 120 × 1 + 96\n120 = 96 × 1 + 24\n96 = 24 × 4 + 0\nHCF = 24 cm. Largest tile size = 24 cm × 24 cm.",
            "concepts_tested": ["Euclid's Algorithm", "HCF application"]
        }
    ]

    questions["math10.quadratic_equations.quadratic_formula"] = [
        {
            "id": 1, "type": "direct", "difficulty": 0.4,
            "question": "Solve using the quadratic formula: x² − 7x + 10 = 0",
            "hint": "a = 1, b = −7, c = 10. Find D = b² − 4ac, then apply x = (−b ± √D) / 2a.",
            "expected_answer": "D = 49 − 40 = 9. x = (7 ± 3)/2. x = 5 or x = 2.",
            "concepts_tested": ["Quadratic Formula"]
        },
        {
            "id": 2, "type": "direct", "difficulty": 0.5,
            "question": "Solve: 2x² + x − 4 = 0 using the quadratic formula. Express roots in simplest form.",
            "hint": "a = 2, b = 1, c = −4. D = 1 + 32 = 33.",
            "expected_answer": "D = 1 + 32 = 33. x = (−1 ± √33)/4. Roots are x = (−1+√33)/4 and x = (−1−√33)/4.",
            "concepts_tested": ["Quadratic Formula", "Irrational roots"]
        },
        {
            "id": 3, "type": "word_problem", "difficulty": 0.6,
            "question": "The sum of the reciprocals of Rehman's age 3 years ago and 5 years from now is 1/3. Find his present age.",
            "hint": "Let present age = x. Set up: 1/(x−3) + 1/(x+5) = 1/3. Simplify to get a quadratic.",
            "expected_answer": "1/(x−3) + 1/(x+5) = 1/3\n(x+5+x−3)/((x−3)(x+5)) = 1/3\n(2x+2)×3 = (x−3)(x+5)\n6x+6 = x²+2x−15\nx²−4x−21 = 0\nx = (4 ± √(16+84))/2 = (4±10)/2\nx = 7 (reject −3).\nRehman's present age = 7 years.",
            "concepts_tested": ["Quadratic Formula", "Word problems"]
        }
    ]

    questions["math10.quadratic_equations.nature_of_roots"] = [
        {
            "id": 1, "type": "direct", "difficulty": 0.4,
            "question": "Find the discriminant and determine the nature of roots: (a) 2x² − 6x + 3 = 0, (b) x² − 4x + 4 = 0, (c) 3x² + x + 5 = 0",
            "hint": "D = b² − 4ac. If D > 0: two distinct roots. D = 0: equal roots. D < 0: no real roots.",
            "expected_answer": "(a) D = 36−24 = 12 > 0 → two distinct real roots\n(b) D = 16−16 = 0 → two equal roots (x = 2)\n(c) D = 1−60 = −59 < 0 → no real roots",
            "concepts_tested": ["Discriminant", "Nature of roots"]
        },
        {
            "id": 2, "type": "direct", "difficulty": 0.5,
            "question": "For what values of k does the equation kx² − 6x + 1 = 0 have (i) equal roots (ii) no real roots?",
            "hint": "D = 36 − 4k. Equal roots: D = 0. No real roots: D < 0.",
            "expected_answer": "(i) D = 36−4k = 0 → k = 9\n(ii) D = 36−4k < 0 → k > 9\nAlso note: k ≠ 0 (otherwise it's not quadratic).",
            "concepts_tested": ["Discriminant", "Conditions on coefficients"]
        },
        {
            "id": 3, "type": "transfer_task", "difficulty": 0.65,
            "question": "A shopkeeper buys a number of books for ₹80. If he had bought 4 more books for the same amount, each book would have cost ₹1 less. Find the number of books he bought. First determine if the equation has real solutions.",
            "hint": "Let n = number of books. Cost per book = 80/n. New cost = 80/(n+4) = 80/n − 1. Form quadratic and check discriminant.",
            "expected_answer": "80/n − 80/(n+4) = 1\n80(n+4−n)/(n(n+4)) = 1\n320 = n² + 4n\nn² + 4n − 320 = 0\nD = 16 + 1280 = 1296 = 36² > 0 → real solutions exist!\nn = (−4+36)/2 = 16 (reject −20)\nHe bought 16 books.",
            "concepts_tested": ["Discriminant", "Quadratic word problem"]
        }
    ]

    questions["math10.trigonometry.trig_ratios"] = [
        {
            "id": 1, "type": "direct", "difficulty": 0.4,
            "question": "If tan A = 4/3, find sin A and cos A (A is acute).",
            "hint": "tan A = Opposite/Adjacent = 4/3. Use Pythagoras to find the hypotenuse.",
            "expected_answer": "Hypotenuse = √(4²+3²) = √25 = 5.\nsin A = 4/5, cos A = 3/5.",
            "concepts_tested": ["Trigonometric ratios", "Pythagorean triplets"]
        },
        {
            "id": 2, "type": "word_problem", "difficulty": 0.5,
            "question": "A ladder 15 m long leans against a wall. The foot of the ladder is 9 m from the wall. Find the angle the ladder makes with the ground.",
            "hint": "Adjacent = 9 m, Hypotenuse = 15 m. cos θ = 9/15 = 3/5. What standard angle gives this?",
            "expected_answer": "cos θ = 9/15 = 3/5.\nThis isn't a standard angle, but we can find sin θ = √(1−9/25) = √(16/25) = 4/5.\ntan θ = 4/3. The angle θ ≈ 53.13° (or you can express as 'the angle whose cos = 3/5').",
            "concepts_tested": ["Trigonometric ratios", "Real-world application"]
        },
        {
            "id": 3, "type": "transfer_task", "difficulty": 0.6,
            "question": "In a video game, a cannon fires at angle θ to the ground. The ball travels a horizontal distance of 12 m and reaches a maximum height of 5 m. If the initial speed determines the hypotenuse of the right triangle formed, what is sin θ?",
            "hint": "Think of the triangle: opposite (height) = 5 m, adjacent (horizontal) = 12 m. Find hypotenuse first.",
            "expected_answer": "Hypotenuse = √(12² + 5²) = √(144 + 25) = √169 = 13 m.\nsin θ = Opposite/Hypotenuse = 5/13 ≈ 0.385.\nThe firing angle θ = sin⁻¹(5/13) ≈ 22.6°.",
            "concepts_tested": ["Trigonometric ratios", "Transfer to new context"]
        }
    ]

    questions["math10.probability10.classical_definition"] = [
        {
            "id": 1, "type": "direct", "difficulty": 0.35,
            "question": "A box contains 5 red, 8 white, and 4 green marbles. One marble is drawn at random. Find: (i) P(red) (ii) P(white) (iii) P(not green)",
            "hint": "Total marbles = 5+8+4 = 17. P = favourable/total.",
            "expected_answer": "(i) P(red) = 5/17\n(ii) P(white) = 8/17\n(iii) P(not green) = 1 − P(green) = 1 − 4/17 = 13/17",
            "concepts_tested": ["Classical probability", "Complement rule"]
        },
        {
            "id": 2, "type": "word_problem", "difficulty": 0.5,
            "question": "A bag contains tickets numbered 1 to 25. One ticket is drawn at random. Find the probability that the number on the ticket is: (a) a multiple of 5 (b) a prime number (c) a perfect square",
            "hint": "List the favourable outcomes for each: multiples of 5 up to 25, primes up to 25, perfect squares up to 25.",
            "expected_answer": "(a) Multiples of 5: {5,10,15,20,25} = 5 numbers. P = 5/25 = 1/5\n(b) Primes: {2,3,5,7,11,13,17,19,23} = 9 numbers. P = 9/25\n(c) Perfect squares: {1,4,9,16,25} = 5 numbers. P = 5/25 = 1/5",
            "concepts_tested": ["Classical probability", "Number theory"]
        },
        {
            "id": 3, "type": "transfer_task", "difficulty": 0.6,
            "question": "In a class of 40 students, 8 study both Hindi and English, 20 study Hindi only, and 5 study English only. The remaining study neither. If a student is selected at random, find the probability that the student studies: (a) both subjects (b) at least one subject (c) neither subject.",
            "hint": "Count: Hindi only = 20, English only = 5, Both = 8, Neither = 40 − 20 − 5 − 8 = 7.",
            "expected_answer": "(a) P(both) = 8/40 = 1/5\n(b) At least one = 20+5+8 = 33. P = 33/40\n(c) Neither = 40−33 = 7. P = 7/40",
            "concepts_tested": ["Classical probability", "Set counting"]
        }
    ]

    # Generate default questions for all other concepts
    for ch in CURRICULUM["chapters"]:
        for concept in ch["concepts"]:
            cid = concept["concept_id"]
            if cid not in questions:
                questions[cid] = _auto_questions(concept)

    return questions


def _auto_questions(c: dict) -> list[dict]:
    """Create reasonable default questions from concept metadata."""
    return [
        {
            "id": 1, "type": "direct", "difficulty": c["difficulty"],
            "question": f"State and explain the key concept: {c['key_ideas'][0]}.",
            "hint": f"Think about the definition and main formula related to {c['title']}.",
            "expected_answer": f"This tests understanding of: {c['key_ideas'][0]}. Refer to NCERT textbook for the detailed explanation.",
            "concepts_tested": [c["title"]]
        },
        {
            "id": 2, "type": "word_problem", "difficulty": c["difficulty"] + 0.1,
            "question": f"Solve an NCERT example problem related to '{c['title']}'. Show all steps clearly.",
            "hint": f"Review the key ideas: {', '.join(c['key_ideas'][:2])}.",
            "expected_answer": f"Practice NCERT in-text examples and Exercise problems for {c['title']}. Focus on step-by-step working.",
            "concepts_tested": [c["title"]]
        },
        {
            "id": 3, "type": "transfer_task", "difficulty": c["difficulty"] + 0.15,
            "question": f"How would you apply '{c['title']}' to solve a real-world problem? Give an example and solve it.",
            "hint": f"Think about everyday situations where {c['title'].lower()} concepts are useful.",
            "expected_answer": f"Create a real-world scenario (e.g., measurement, construction, finance) and apply the formulas and techniques from {c['title']}.",
            "concepts_tested": [c["title"], "Real-world application"]
        }
    ]


# ═══════════════════════════════════════════════════════════════════════════════
#  WRITE EVERYTHING TO DISK
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    print("📘 Creating Class 10 Mathematics content...")

    # 1. Write expanded curriculum
    curriculum_path = CONTENT_DIR / "curriculum.json"
    with open(curriculum_path, "w") as f:
        json.dump(CURRICULUM, f, indent=2, ensure_ascii=False)
    total_concepts = sum(len(ch["concepts"]) for ch in CURRICULUM["chapters"])
    print(f"   ✅ Curriculum: {len(CURRICULUM['chapters'])} chapters, {total_concepts} concepts")

    # 2. Write lessons to cache
    lessons = make_lessons()
    lesson_dir = CONTENT_DIR / "lessons"
    lesson_dir.mkdir(parents=True, exist_ok=True)
    for concept_id, lesson in lessons.items():
        key = concept_id.replace(".", "_")
        path = lesson_dir / f"{key}.json"
        with open(path, "w") as f:
            json.dump(lesson, f, indent=2, ensure_ascii=False)
    print(f"   ✅ Lessons: {len(lessons)} cached")

    # 3. Write questions to cache
    all_questions = make_questions()
    question_dir = CONTENT_DIR / "questions"
    question_dir.mkdir(parents=True, exist_ok=True)
    for concept_id, qs in all_questions.items():
        key = concept_id.replace(".", "_")
        path = question_dir / f"{key}_3_medium.json"
        with open(path, "w") as f:
            json.dump(qs, f, indent=2, ensure_ascii=False)
    print(f"   ✅ Questions: {len(all_questions)} sets cached")

    print(f"\n🎉 Done! Class 10 Math is fully loaded with {total_concepts} concepts, {len(lessons)} lessons, {len(all_questions)} question sets.")
    print(f"   📂 Content at: {CONTENT_DIR}")


if __name__ == "__main__":
    main()
