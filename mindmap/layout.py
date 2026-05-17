"""
layout.py — adaptive mind map coordinate engine v7

Strategy:
- Even spoke angles, -90 offset (first branch points up)
- Children placed into angular gaps between spokes
- GAP_FRAC scales with branch count
- scale-to-fit pass: whole layout scales to fit W with MARGIN
- font_scale included in output so SVG text scales with nodes
- Overlap checker included in warnings

All coordinates: screen space. y=0 top, y increases downward. Never flip.
"""
import json, math, sys

W        = 680
MARGIN   = 48

R_BRANCH  = 165
R_CHILD_A = 285
R_CHILD_B = 335

NODE_ROOT   = (164, 60)
NODE_BRANCH = (140, 48)
NODE_CHILD  = (120, 40)

# Base font sizes (at scale=1.0)
FONT_TITLE = 14
FONT_SUB   = 11

def gap_frac(n):
    """Tighter angular spread with more branches."""
    return max(0.22, 0.50 - n * 0.035)

def angular_gap(a, b):
    return (b - a) % (2 * math.pi)

def _place_raw(tree, cx, cy):
    branches = tree["branches"]
    n = len(branches)
    bw, bh = NODE_BRANCH
    cw, ch = NODE_CHILD
    rw, rh = NODE_ROOT
    angles = [math.radians((360/n)*i - 90) for i in range(n)]
    GF = gap_frac(n)
    nodes = {}
    nodes["root"] = dict(cx=cx, cy=cy, w=rw, h=rh)

    for i, branch in enumerate(branches):
        a      = angles[i]
        a_prev = angles[(i-1) % n]
        a_next = angles[(i+1) % n]
        bx = cx + R_BRANCH * math.cos(a)
        by = cy + R_BRANCH * math.sin(a)
        nodes[branch["id"]] = dict(cx=bx, cy=by, w=bw, h=bh, angle=a)

        children = branch.get("children", [])
        nc = len(children)
        if nc == 0:
            continue

        gap_ccw = angular_gap(a_prev, a)
        gap_cw  = angular_gap(a, a_next)

        if nc == 1:
            ccx = cx + R_CHILD_A * math.cos(a)
            ccy = cy + R_CHILD_A * math.sin(a)
            nodes[children[0]["id"]] = dict(cx=ccx, cy=ccy, w=cw, h=ch)
        else:
            if gap_cw >= gap_ccw:
                a0 = a + gap_cw  * GF
                a1 = a - gap_ccw * GF
            else:
                a0 = a - gap_ccw * GF
                a1 = a + gap_cw  * GF
            for child, angle, r in zip(children, [a0, a1], [R_CHILD_A, R_CHILD_B]):
                ccx = cx + r * math.cos(angle)
                ccy = cy + r * math.sin(angle)
                nodes[child["id"]] = dict(cx=ccx, cy=ccy, w=cw, h=ch)
            for k in range(2, nc):
                child = children[k]
                side  = k % 2
                tier  = k // 2
                r     = R_CHILD_B + tier * 55
                angle = (a + gap_cw * GF * 0.8) if side == 0 else (a - gap_ccw * GF * 0.8)
                ccx   = cx + r * math.cos(angle)
                ccy   = cy + r * math.sin(angle)
                nodes[child["id"]] = dict(cx=ccx, cy=ccy, w=cw, h=ch)

    return nodes

def _scale_to_fit(raw_nodes):
    min_x = min(v["cx"] - v["w"]/2 for v in raw_nodes.values())
    max_x = max(v["cx"] + v["w"]/2 for v in raw_nodes.values())
    min_y = min(v["cy"] - v["h"]/2 for v in raw_nodes.values())
    max_y = max(v["cy"] + v["h"]/2 for v in raw_nodes.values())

    content_w = max_x - min_x
    content_h = max_y - min_y
    avail = W - 2 * MARGIN
    scale = min(avail / content_w, avail / content_h, 1.0)

    tx = MARGIN + (avail - content_w * scale) / 2 - min_x * scale
    ty = MARGIN - min_y * scale

    result = {}
    for k, v in raw_nodes.items():
        scx = v["cx"] * scale + tx
        scy = v["cy"] * scale + ty
        sw  = v["w"]  * scale
        sh  = v["h"]  * scale
        result[k] = dict(
            x=round(scx - sw/2), y=round(scy - sh/2),
            w=round(sw), h=round(sh),
            cx=round(scx), cy=round(scy)
        )
    return result, round((max_y - min_y) * scale + 2 * MARGIN), scale

def layout(tree):
    raw = _place_raw(tree, 0, 0)
    coords, viewbox_h, scale = _scale_to_fit(raw)

    # Scale font sizes with layout, but clamp to readable range
    font_title = round(max(10, min(FONT_TITLE, FONT_TITLE * scale)), 1)
    font_sub   = round(max(9,  min(FONT_SUB,   FONT_SUB   * scale)), 1)

    min_y = min(v["y"] for v in coords.values())
    max_y = max(v["y"] + v["h"] for v in coords.values())
    min_x = min(v["x"] for v in coords.values())
    max_x = max(v["x"] + v["w"] for v in coords.values())

    items = list(coords.items())
    overlaps = []
    for i, (ka, a) in enumerate(items):
        for kb, b in items[i+1:]:
            if (a['x']+a['w'] > b['x'] and b['x']+b['w'] > a['x'] and
                a['y']+a['h'] > b['y'] and b['y']+b['h'] > a['y']):
                overlaps.append(f"{ka}+{kb}")

    warnings = []
    if min_x < 0:    warnings.append(f"left clip: {min_x}")
    if max_x > W:    warnings.append(f"right clip: {max_x}")
    if overlaps:     warnings.append(f"overlaps: {overlaps}")

    return {
        "coords": coords,
        "viewbox_height": viewbox_h,
        "font_title": font_title,
        "font_sub": font_sub,
        "scale": round(scale, 3),
        "bounds": dict(min_x=min_x, max_x=max_x, min_y=min_y, max_y=max_y),
        "warnings": warnings
    }

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "/home/claude/session.json"
    with open(path) as f:
        tree = json.load(f)
    print(json.dumps(layout(tree), indent=2))
