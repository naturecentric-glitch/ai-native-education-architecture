"""
Reusable HTML visual helpers for rich lesson content.

All functions return HTML strings that render inside the course.html
lesson area (which uses innerHTML with white-space:pre-wrap).
"""


def formula_box(formula: str, label: str = "") -> str:
    """Highlighted formula box with gradient background and optional label."""
    lbl = (
        f'<div style="font-size:0.7rem;text-transform:uppercase;font-weight:700;'
        f'color:#1565C0;margin-bottom:4px">{label}</div>'
        if label else ""
    )
    return (
        f'<div style="background:linear-gradient(135deg,#E3F2FD,#BBDEFB);'
        f'border-left:4px solid #1565C0;border-radius:8px;padding:12px 16px;'
        f'margin:12px 0;font-family:\'Courier New\',monospace;font-size:1.05rem;'
        f'text-align:center">{lbl}<strong>{formula}</strong></div>'
    )


def step_box(steps: list[tuple[str, str]], color: str = "#4A90D9") -> str:
    """Numbered step-by-step visual walkthrough with colored circles."""
    html = '<div style="margin:12px 0">'
    for i, (title, detail) in enumerate(steps, 1):
        html += (
            f'<div style="display:flex;gap:12px;margin-bottom:10px;align-items:flex-start">'
            f'<div style="min-width:32px;height:32px;border-radius:50%;background:{color};'
            f'color:white;display:flex;align-items:center;justify-content:center;'
            f'font-weight:700;font-size:0.85rem">{i}</div>'
            f'<div><strong>{title}</strong><br>'
            f'<span style="color:#555;font-size:0.88rem">{detail}</span></div></div>'
        )
    html += '</div>'
    return html


def tip_box(text: str, icon: str = "💡", bg: str = "#FFF8E1",
            border: str = "#FFB300") -> str:
    """Callout tip box with icon and colored left border."""
    return (
        f'<div style="background:{bg};border-left:4px solid {border};'
        f'border-radius:8px;padding:10px 14px;margin:10px 0;font-size:0.88rem">'
        f'{icon} <strong>Tip:</strong> {text}</div>'
    )


def warning_box(text: str) -> str:
    return tip_box(text, "⚠️", "#FFF3E0", "#E65100")


def info_box(text: str) -> str:
    return tip_box(text, "ℹ️", "#E3F2FD", "#1565C0")


def comparison_table(headers: list[str], rows: list[list[str]]) -> str:
    """Styled HTML table with blue header row."""
    html = (
        '<table style="width:100%;border-collapse:collapse;margin:12px 0;'
        'font-size:0.88rem"><tr>'
    )
    for h in headers:
        html += (
            f'<th style="background:#E3F2FD;padding:8px 12px;border:1px solid '
            f'#BBDEFB;text-align:left;font-weight:700">{h}</th>'
        )
    html += '</tr>'
    for row in rows:
        html += '<tr>'
        for cell in row:
            html += f'<td style="padding:8px 12px;border:1px solid #E0E0E0">{cell}</td>'
        html += '</tr>'
    html += '</table>'
    return html


def key_point(text: str, color: str = "#4A90D9") -> str:
    """A single key-point callout with colored left bar."""
    return (
        f'<div style="background:#F5F5F5;border-left:3px solid {color};'
        f'border-radius:6px;padding:8px 12px;margin:6px 0;font-size:0.9rem">'
        f'{text}</div>'
    )


def definition_box(term: str, definition: str) -> str:
    """Styled definition card."""
    return (
        f'<div style="background:#F3E5F5;border-left:4px solid #7B1FA2;'
        f'border-radius:8px;padding:12px 16px;margin:12px 0">'
        f'<strong style="color:#7B1FA2">{term}:</strong> {definition}</div>'
    )


def example_pair(example: str, non_example: str) -> str:
    """Side-by-side example vs non-example."""
    return (
        '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:12px 0">'
        f'<div style="background:#E8F5E9;border:2px solid #4CAF50;border-radius:8px;'
        f'padding:10px;text-align:center">'
        f'<div style="font-weight:700;color:#2E7D32;font-size:0.75rem;margin-bottom:4px">✅ CORRECT</div>'
        f'{example}</div>'
        f'<div style="background:#FFEBEE;border:2px solid #EF5350;border-radius:8px;'
        f'padding:10px;text-align:center">'
        f'<div style="font-weight:700;color:#C62828;font-size:0.75rem;margin-bottom:4px">❌ WRONG</div>'
        f'{non_example}</div></div>'
    )


def svg_coordinate_grid(
    points: list[tuple[float, float, str, str]] | None = None,
    lines: list[tuple[float, float, float, float, str]] | None = None,
    xrange: tuple[int, int] = (-5, 5),
    yrange: tuple[int, int] = (-5, 5),
    width: int = 300, height: int = 300,
) -> str:
    """SVG coordinate plane with optional points and line segments."""
    xmin, xmax = xrange
    ymin, ymax = yrange
    mx, my = 30, 30  # margins
    iw = width - 2 * mx
    ih = height - 2 * my

    def tx(x): return mx + (x - xmin) / (xmax - xmin) * iw
    def ty(y): return my + (ymax - y) / (ymax - ymin) * ih

    svg = f'<svg width="{width}" height="{height}" style="display:block;margin:10px auto;background:#FAFAFA;border-radius:8px">'
    # Grid lines
    for x in range(xmin, xmax + 1):
        xx = tx(x)
        c = "#333" if x == 0 else "#E0E0E0"
        w = "1.5" if x == 0 else "0.5"
        svg += f'<line x1="{xx}" y1="{my}" x2="{xx}" y2="{height-my}" stroke="{c}" stroke-width="{w}"/>'
        if x != 0:
            svg += f'<text x="{xx}" y="{ty(0)+14}" text-anchor="middle" font-size="9" fill="#666">{x}</text>'
    for y in range(ymin, ymax + 1):
        yy = ty(y)
        c = "#333" if y == 0 else "#E0E0E0"
        w = "1.5" if y == 0 else "0.5"
        svg += f'<line x1="{mx}" y1="{yy}" x2="{width-mx}" y2="{yy}" stroke="{c}" stroke-width="{w}"/>'
        if y != 0:
            svg += f'<text x="{tx(0)-8}" y="{yy+4}" text-anchor="end" font-size="9" fill="#666">{y}</text>'
    # Axis arrows
    svg += f'<text x="{width-mx+5}" y="{ty(0)+4}" font-size="10" font-weight="bold">x</text>'
    svg += f'<text x="{tx(0)+5}" y="{my-5}" font-size="10" font-weight="bold">y</text>'
    # Lines
    if lines:
        for x1, y1, x2, y2, color in lines:
            svg += f'<line x1="{tx(x1)}" y1="{ty(y1)}" x2="{tx(x2)}" y2="{ty(y2)}" stroke="{color}" stroke-width="2"/>'
    # Points
    if points:
        for x, y, label, color in points:
            svg += f'<circle cx="{tx(x)}" cy="{ty(y)}" r="4" fill="{color}" stroke="white" stroke-width="1.5"/>'
            svg += f'<text x="{tx(x)+7}" y="{ty(y)-5}" font-size="10" font-weight="bold" fill="{color}">{label}</text>'
    svg += '</svg>'
    return svg


def svg_right_triangle(a: str, b: str, c: str, angle_label: str = "") -> str:
    """SVG right triangle with labeled sides."""
    return (
        f'<svg width="220" height="180" style="display:block;margin:10px auto">'
        f'<polygon points="30,150 180,150 30,30" fill="#E8F5E9" stroke="#2E7D32" stroke-width="2"/>'
        f'<rect x="30" y="138" width="12" height="12" fill="none" stroke="#2E7D32" stroke-width="1"/>'
        f'<text x="100" y="168" text-anchor="middle" font-size="12" font-weight="bold">{b}</text>'
        f'<text x="15" y="95" text-anchor="middle" font-size="12" font-weight="bold" '
        f'transform="rotate(-90,15,95)">{a}</text>'
        f'<text x="118" y="82" text-anchor="middle" font-size="12" font-weight="bold" fill="#C62828" '
        f'transform="rotate(-40,118,82)">{c}</text>'
        + (f'<text x="155" y="145" font-size="13" font-weight="bold" fill="#E65100">{angle_label}</text>'
           if angle_label else '')
        + '</svg>'
    )


def svg_circle(
    radius_label: str = "r",
    center_label: str = "O",
    annotations: list[tuple[int, int, str]] | None = None,
    width: int = 200,
) -> str:
    """SVG circle with center and optional annotations."""
    cx, cy, r = width // 2, width // 2, width // 2 - 30
    svg = f'<svg width="{width}" height="{width}" style="display:block;margin:10px auto">'
    svg += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#E3F2FD" stroke="#1565C0" stroke-width="2"/>'
    svg += f'<circle cx="{cx}" cy="{cy}" r="3" fill="#1565C0"/>'
    svg += f'<text x="{cx+6}" y="{cy+14}" font-size="11" font-weight="bold">{center_label}</text>'
    # radius line
    svg += f'<line x1="{cx}" y1="{cy}" x2="{cx+r}" y2="{cy}" stroke="#1565C0" stroke-width="1.5" stroke-dasharray="4"/>'
    svg += f'<text x="{cx+r//2}" y="{cy-6}" font-size="10" fill="#1565C0">{radius_label}</text>'
    if annotations:
        for ax, ay, text in annotations:
            svg += f'<text x="{ax}" y="{ay}" font-size="10" fill="#E65100">{text}</text>'
    svg += '</svg>'
    return svg


def progress_indicator(items: list[tuple[str, bool]]) -> str:
    """Visual checklist showing progress through sub-steps."""
    html = '<div style="margin:10px 0">'
    for label, done in items:
        icon = "✅" if done else "⬜"
        html += f'<div style="padding:3px 0;font-size:0.88rem">{icon} {label}</div>'
    html += '</div>'
    return html
