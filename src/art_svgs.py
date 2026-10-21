# Original illustrative panels for the tools cards. Generic sample shapes, no real product UI, no real data.
F = "font-family:Figtree,sans-serif"
def t(x, y, s, size=9, w=600, c="#201814", anchor="start"):
    return f'<text x="{x}" y="{y}" style="{F};font-size:{size}px;font-weight:{w};fill:{c}" text-anchor="{anchor}">{s}</text>'
def panel(x, y, w, h, rot=0, extra=""):
    return (f'<g transform="rotate({rot} {x+w/2} {y+h/2})"><rect x="{x+3}" y="{y+4}" width="{w}" height="{h}" fill="#201814" opacity=".12"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#fff"/>{extra}</g>')
def bar(x, y, w, c, h=6): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}"/>'
def dot(x, y, r, c): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>'

def hris():
    e = ""
    e += t(128, 42, "Org chart", 10, 700)
    e += f'<rect x="215" y="52" width="60" height="22" fill="#6b3f12"/>' + dot(227, 63, 5, "#fff") + bar(236, 60, 30, "#fff", 3) + bar(236, 66, 22, "#ffffffaa", 3)
    e += '<path d="M245 74 V86 M170 86 H320 M170 86 V96 M245 86 V96 M320 86 V96" stroke="#201814" stroke-width="1.2" fill="none"/>'
    for x, c in ((140, "#c4701f"), (215, "#f0b66e"), (290, "#e6d2bc")):
        e += f'<rect x="{x}" y="96" width="60" height="22" fill="{c}"/>' + dot(x+12, 107, 5, "#fff") + bar(x+21, 104, 30, "#fff", 3) + bar(x+21, 110, 22, "#ffffffaa", 3)
    for x in (140, 215, 290):
        e += f'<path d="M{x+30} 118 V128" stroke="#201814" stroke-width="1.2"/><rect x="{x+8}" y="128" width="44" height="16" fill="#f1e7dc"/>' + bar(x+14, 134, 30, "#20181455", 3)
    return ("#f3e9de", '<path d="M0 0 L190 0 Q150 100 210 200 L0 200Z" fill="#e6d2bc"/><path d="M300 120 L400 100 L400 200 L280 200Z" fill="#6b3f12"/>' + panel(118, 22, 262, 140, -2, e))

def ats():
    e = t(124, 40, "Hiring pipeline", 10, 700)
    cols = [("Applied", "#c4701f", 3), ("Screen", "#e8892b", 2), ("Interview", "#d9a35a", 2), ("Offer", "#6b3f12", 1)]
    x = 124
    for n, c, k in cols:
        e += f'<rect x="{x}" y="50" width="58" height="4" fill="{c}"/>' + t(x, 66, n, 8, 600)
        for i in range(k):
            y = 72 + i * 28
            e += f'<rect x="{x}" y="{y}" width="58" height="24" fill="#f7f3ef"/>' + dot(x+9, y+12, 4.5, c) + bar(x+18, y+8, 34, "#20181466", 3) + bar(x+18, y+14, 22, "#20181433", 3)
        x += 66
    return ("#f6e1c0", '<path d="M0 60 Q90 10 150 70 L170 200 L0 200Z" fill="#d9a35a"/><path d="M300 0 L400 0 L400 90 Q340 70 300 0Z" fill="#f0b66e"/>' + panel(112, 22, 272, 150, 2, e))

def perf():
    e = t(128, 42, "Review cycle", 10, 700)
    rows = [("Self reviews", 0.9, "#c4701f"), ("Manager reviews", 0.65, "#e8892b"), ("Calibration", 0.35, "#6b3f12"), ("Goals set", 0.8, "#e6d2bc")]
    for i, (n, v, c) in enumerate(rows):
        y = 58 + i * 26
        e += t(128, y + 8, n, 8.5, 600) + f'<rect x="215" y="{y}" width="150" height="9" fill="#f1e7dc"/>' + f'<rect x="215" y="{y}" width="{150*v}" height="9" fill="{c}"/>'
    return ("#f3e9de", '<path d="M120 0 L400 0 L400 200 L0 200Z" fill="#e6d2bc"/><path d="M20 40 L100 30 L120 150 L30 165Z" fill="#6b3f12"/>' + panel(118, 24, 262, 140, 0, e))

def comp():
    e = t(128, 42, "Audit readiness", 10, 700)
    items = ["SOPs reviewed and owned", "Access reviews complete", "Evidence collected", "Policies acknowledged"]
    for i, n in enumerate(items):
        y = 56 + i * 26
        e += f'<rect x="128" y="{y}" width="16" height="16" fill="#6b3f12"/><path d="M132 {y+8} l4 4 l6 -8" stroke="#fff" stroke-width="2" fill="none"/>' + t(152, y + 12, n, 9.5, 600)
    e += '<path d="M335 62 l24 8 v20 q0 18 -24 28 q-24 -10 -24 -28 v-20z" fill="#f0b66e"/><path d="M325 92 l8 8 l14 -16" stroke="#201814" stroke-width="3" fill="none"/>'
    return ("#f8dcc0", '<path d="M0 0 L200 0 Q160 100 230 200 L0 200Z" fill="#e8892b"/><path d="M290 110 L400 90 L400 200 L280 200Z" fill="#8a6a4a"/>' + panel(116, 22, 268, 140, -2, e))

def ai():
    e = t(124, 42, "Employee action flow", 10, 700)
    nodes = [("Request", "#c4701f"), ("Approve", "#e8892b"), ("Update HRIS", "#d9a35a"), ("Audit trail", "#6b3f12")]
    for i, (n, c) in enumerate(nodes):
        x = 124 + i * 66
        tc = "#fff" if c in ("#6b3f12",) else "#201814"
        e += f'<rect x="{x}" y="72" width="56" height="34" fill="{c}"/>' + t(x + 28, 93, n, 8.5, 700, tc, "middle")
        if i < 3: e += f'<path d="M{x+56} 89 h10" stroke="#201814" stroke-width="1.5"/><path d="M{x+62} 85 l4 4 l-4 4" stroke="#201814" stroke-width="1.5" fill="none"/>'
    e += f'<rect x="124" y="124" width="250" height="26" fill="#f7f3ef"/>' + t(136, 141, "Documented, approved, recorded", 9, 600)
    return ("#f1e7da", '<path d="M0 150 Q100 20 220 90 T400 60 L400 200 L0 200Z" fill="#8a6a4a"/><path d="M40 20 L100 10 L112 70 L50 80Z" fill="#d9a35a"/>' + panel(112, 22, 272, 150, 1.5, e))

def rep():
    e = t(128, 42, "People metrics", 10, 700)
    hs = [38, 54, 46, 70, 62, 84]
    cs = ["#c4701f", "#e8892b", "#c4701f", "#e8892b", "#c4701f", "#e8892b"]
    for i, h in enumerate(hs):
        e += f'<rect x="{132+i*24}" y="{150-h}" width="16" height="{h}" fill="{cs[i]}"/>'
    e += '<path d="M132 120 L160 104 L190 112 L220 86 L250 92 L280 70" stroke="#201814" stroke-width="2" fill="none"/>'
    e += f'<rect x="300" y="56" width="70" height="36" fill="#f7f3ef"/>' + bar(308, 66, 40, "#20181466", 4) + bar(308, 76, 28, "#20181433", 4)
    e += f'<rect x="300" y="100" width="70" height="36" fill="#f7f3ef"/>' + bar(308, 110, 34, "#20181466", 4) + bar(308, 120, 46, "#20181433", 4)
    return ("#f5e2d0", '<path d="M200 0 L400 0 L400 140 Q300 120 200 200Z" fill="#f0b66e"/><path d="M0 90 L100 60 L120 200 L0 200Z" fill="#6b3f12"/>' + panel(116, 22, 268, 146, -1.5, e))

def hub():
    # wide art, viewBox 1000 x 150
    c = "".join(dot(x, y, r, col) for x, y, r, col in [(500, 75, 38, "#e8892b"), (380, 60, 26, "#f0b66e"), (620, 62, 28, "#6b3f12"), (300, 100, 20, "#d9a35a"), (700, 98, 22, "#e6d2bc"), (560, 122, 16, "#8a6a4a"), (440, 118, 14, "#f7f3ef")])
    lines = '<path d="M500 75 L380 60 M500 75 L620 62 M380 60 L300 100 M620 62 L700 98 M500 75 L560 122 M500 75 L440 118" stroke="#201814" stroke-width="1.5"/>'
    return ("#c4701f", '<path d="M0 100 Q250 40 520 100 T1000 70 L1000 150 L0 150Z" fill="#f7f3ef"/><path d="M780 20 L940 10 L960 140 L790 150Z" fill="#e8892b" opacity=".9"/><path d="M40 60 L200 40 L220 150 L50 150Z" fill="#e6d2bc"/>' + lines + c, "0 0 1000 150")

ARTS = [hris, ats, perf, comp, ai, rep]



PLAN_ART = [
    '<svg viewBox="0 0 120 100" aria-hidden="true"><path d="M8 18 L92 8 L100 70 L18 88Z" fill="#f0b66e"/><rect x="24" y="22" width="56" height="30" rx="6" fill="#201814"/><path d="M36 52 l-4 12 l14 -12z" fill="#201814"/><rect x="50" y="44" width="52" height="28" rx="6" fill="#f7f3ef" stroke="#201814" stroke-width="2"/><path d="M84 72 l6 12 l2 -12z" fill="#f7f3ef" stroke="#201814" stroke-width="2"/><path d="M34 34h36M34 42h22M60 54h32M60 62h20" stroke="#f7f3ef" stroke-width="3" opacity=".9"/></svg>',
    '<svg viewBox="0 0 120 100" aria-hidden="true"><path d="M6 30 Q30 4 70 12 L108 26 L96 84 L14 90Z" fill="#6b3f12"/><path d="M22 70 Q40 40 62 56 T98 34" stroke="#f7f3ef" stroke-width="3" fill="none" stroke-dasharray="5 5"/><circle cx="22" cy="70" r="6" fill="#f7f3ef"/><circle cx="62" cy="56" r="6" fill="#e8892b"/><circle cx="98" cy="34" r="6" fill="#f7f3ef"/><rect x="50" y="14" width="34" height="22" fill="#201814"/><path d="M56 22h22M56 29h14" stroke="#f7f3ef" stroke-width="3"/></svg>',
    '<svg viewBox="0 0 120 100" aria-hidden="true"><circle cx="54" cy="44" r="38" fill="#d9a35a"/><path d="M8 92 L70 78 L112 92Z" fill="#c4701f"/><rect x="30" y="50" width="14" height="30" fill="#201814"/><rect x="50" y="36" width="14" height="44" fill="#e8892b"/><rect x="70" y="20" width="14" height="60" fill="#201814"/><path d="M28 40 L56 26 L90 10" stroke="#f7f3ef" stroke-width="3" fill="none"/></svg>',
    '<svg viewBox="0 0 120 100" aria-hidden="true"><circle cx="62" cy="48" r="40" fill="#e8892b"/><circle cx="20" cy="20" r="5" fill="#201814"/><circle cx="32" cy="10" r="3" fill="#201814"/><path d="M50 84 V22" stroke="#201814" stroke-width="4"/><path d="M52 22 L92 34 L52 48Z" fill="#f7f3ef" stroke="#201814" stroke-width="3" stroke-linejoin="round"/></svg>',
]

