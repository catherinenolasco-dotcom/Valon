import base64, html, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import content as C
import art_svgs

e = html.escape
FONTS = os.environ.get("FONTS_DIR", "/tmp/valon/node_modules/@fontsource/")


def b64(p):
    return base64.b64encode(open(p, "rb").read()).decode()


def font_css(embed):
    if not embed:
        return ""
    out = ""
    for w in (400, 500, 600, 700):
        out += "@font-face{font-family:'Figtree';font-weight:%d;font-display:swap;src:url(data:font/woff2;base64,%s) format('woff2');}\n" % (w, b64(FONTS + "figtree/files/figtree-latin-%d-normal.woff2" % w))
    for w in (400, 500):
        out += "@font-face{font-family:'Newsreader';font-weight:%d;font-display:swap;src:url(data:font/woff2;base64,%s) format('woff2');}\n" % (w, b64(FONTS + "newsreader/files/newsreader-latin-%d-normal.woff2" % w))
    return out


HEADSHOT = b64(os.path.join(HERE, "headshot.jpg"))

CSS = r"""
:root{--ink:#201814;--ink2:#5b4f46;--orange:#e8892b;--orange-d:#c4701f;--brown:#6b3f12;--deep:#8a4a0f;--amber:#f0b66e;--cream:#f7f3ef;--white:#fff;--line:#ece4dc;--beige:#f1e7dc;--display:'Newsreader',Georgia,serif;--body:'Figtree',system-ui,sans-serif;--mono:'Figtree',system-ui,sans-serif}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--white);color:var(--ink);font-family:var(--body);font-size:17px;line-height:1.55;-webkit-font-smoothing:antialiased}
.pf img{max-width:100%}
.pf a{color:inherit}
.wrap{max-width:1160px;margin:0 auto;padding:0 20px}
.bar{background:var(--amber);color:var(--ink);font-size:14px;font-weight:600;padding:10px 0}
.bar .wrap{display:flex;gap:12px;justify-content:space-between;align-items:center;flex-wrap:wrap}
.bar a{font-size:13px;text-decoration:underline}
header.nav{position:sticky;top:env(safe-area-inset-top,0px);z-index:20;background:rgba(255,255,255,.96);border-bottom:1px solid var(--line);backdrop-filter:blur(6px)}
header.nav .wrap{display:flex;align-items:center;gap:18px;min-height:60px}
.logo{font-family:var(--display);font-size:24px;white-space:nowrap;text-decoration:none}
.logo i{display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--orange);margin-left:3px;vertical-align:top;margin-top:4px}
nav.links{flex:1;min-width:0;display:flex;gap:4px;overflow-x:auto;justify-content:safe flex-end;scrollbar-width:none}
nav.links::-webkit-scrollbar{display:none}
nav.links a{font-size:13.5px;font-weight:500;text-decoration:none;padding:8px 10px;white-space:nowrap;border-radius:8px;color:var(--ink2)}
nav.links a:hover{background:var(--cream);color:var(--ink)}
.btn{display:inline-block;background:var(--ink);color:#fff!important;text-decoration:none;font-weight:600;font-size:15px;padding:12px 20px;border-radius:8px;border:1.5px solid var(--ink)}
.btn.ghost{background:transparent;color:var(--ink)!important}
section{padding:84px 0}
section.alt{background:var(--cream)}
.eyebrow{font-size:12.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--orange-d);font-weight:600;margin:0 0 14px}
h1,h2,h3{font-family:var(--display);font-weight:400;margin:0}
h2{font-size:clamp(32px,4.4vw,52px);line-height:1.08;max-width:20ch}
.lede{font-size:19px;color:var(--ink2);max-width:62ch;margin:18px 0 0}
.hero{padding:64px 0 76px}
.hero .grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,340px);gap:56px;align-items:center}
.hero h1{font-size:clamp(40px,6vw,80px);line-height:1.02;letter-spacing:-.01em}
.hero h1 small{display:block;font-family:var(--body);font-size:15px;font-weight:600;letter-spacing:.02em;color:var(--ink2);margin-top:14px}
.tagline{font-family:var(--display);font-size:clamp(22px,2.6vw,30px);color:var(--orange-d);margin:18px 0 0}
.target{margin:22px 0 0;font-weight:600;font-size:18px}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:22px 0 0;padding:0;list-style:none}
.chips li{background:var(--cream);border:1px solid var(--line);border-radius:999px;padding:6px 14px;font-size:14px;font-weight:500}
.cta{display:flex;gap:12px;flex-wrap:wrap;margin-top:30px}
.photo{position:relative;justify-self:center;width:100%;max-width:340px}
.photo::before{content:"";position:absolute;inset:16px -16px -16px 16px;background:var(--amber);border-radius:22px}
.photo img{position:relative;display:block;width:100%;height:auto;border-radius:22px;border:1px solid var(--line)}
.stats{background:var(--ink);color:var(--cream);padding:0}
.stats .grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr))}
.stat{padding:34px 24px;border-left:1px solid #ffffff22}
.stat:first-child{border-left:0}
.stat b{display:block;font-family:var(--display);font-weight:400;font-size:clamp(40px,5vw,60px);line-height:1;color:var(--amber)}
.stat span{display:block;margin-top:10px;font-size:15px;color:#e9e1da}
.sumlist{margin:30px 0 0;padding:0;list-style:none;display:grid;gap:14px;max-width:880px}
.sumlist li{background:var(--cream);border:1px solid var(--line);border-radius:14px;padding:18px 22px 18px 26px;position:relative}
.sumlist li::before{content:"";position:absolute;left:0;top:18px;bottom:18px;width:4px;background:var(--orange);border-radius:0 4px 4px 0}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,340px),1fr));gap:20px;margin-top:40px}
.fit{border-radius:18px;padding:28px 26px 30px;min-width:0}
.fit .lab{font-size:12px;letter-spacing:.14em;text-transform:uppercase;font-weight:700;opacity:.85;margin:0 0 12px}
.fit h3{font-size:28px;line-height:1.12;margin:0 0 14px}
.fit ul{margin:0;padding-left:18px;display:grid;gap:10px;font-size:15.5px}
.fit.ink{background:var(--ink);color:var(--cream)}.fit.orange{background:var(--orange);color:var(--ink)}
.fit.amber{background:var(--amber);color:var(--ink)}.fit.brown{background:var(--brown);color:#fff}
.fit.cream{background:var(--white);color:var(--ink);border:1.5px solid var(--ink)}.fit.deep{background:var(--deep);color:#fff}
.nums{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));margin-top:40px;border:1px solid var(--line);border-radius:18px;background:var(--white);overflow:hidden}
.num{padding:28px 26px;border-right:1px solid var(--line);border-bottom:1px solid var(--line);margin:0 -1px -1px 0}
.num b{display:block;font-family:var(--display);font-weight:400;font-size:clamp(42px,5vw,60px);line-height:1;color:var(--orange-d)}
.num h3{font-family:var(--body);font-size:16px;font-weight:700;margin:10px 0 6px}
.num p{margin:0;font-size:15px;color:var(--ink2)}
.cases{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,460px),1fr));gap:24px;margin-top:40px}
.case{background:var(--white);border:1px solid var(--line);border-radius:18px;overflow:hidden;min-width:0;display:flex;flex-direction:column}
.case .stripe{height:10px}
.stripe.orange{background:var(--orange)}.stripe.amber{background:var(--amber)}.stripe.ink{background:var(--ink)}.stripe.brown{background:var(--brown)}
.case .cb{padding:26px 26px 28px}
.case h3{font-size:30px;line-height:1.1}
.case .meta{font-size:14px;color:var(--ink2);margin:6px 0 18px;font-weight:600}
.case h4{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--orange-d);margin:16px 0 4px;font-family:var(--body);font-weight:700}
.case p{margin:0;font-size:15.5px}
.case .res{background:var(--cream);border-left:4px solid var(--orange);border-radius:8px;padding:12px 14px;margin-top:16px}
.case .res h4{margin-top:0}
.case .chipsm{display:flex;flex-wrap:wrap;gap:6px;margin:18px 0 0;padding:0;list-style:none}
.case .chipsm li{background:var(--beige);border-radius:999px;padding:4px 11px;font-size:13px;font-weight:500}
.vals{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr));gap:20px;margin-top:40px}
.val{background:var(--white);border:1px solid var(--line);border-radius:16px;overflow:hidden;min-width:0}
.val .vt{background:var(--ink);height:84px;display:flex;align-items:center;padding:0 24px}
.val .vt svg{height:36px;width:auto;display:block}
.val .vb{padding:22px 24px 26px}
.val h3{font-size:26px;line-height:1.12}
.val .def{color:var(--ink2);font-size:15px;margin:8px 0 14px}
.val .did{font-size:15.5px;margin:0;padding-top:14px;border-top:1px solid var(--line)}
.val .did b{display:block;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--orange-d);margin-bottom:4px}
"""

TOOL_CSS = r"""
.tools{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,360px),1fr));gap:24px;margin-top:40px}
.tcard{background:var(--white);border:1px solid var(--line);border-radius:18px;overflow:hidden;min-width:0;display:flex;flex-direction:column}
.tcard.wide{grid-column:1/-1}
.tart{position:relative;aspect-ratio:2/1;overflow:hidden;background:var(--beige)}
.tart svg{position:absolute;inset:0;width:100%;height:100%;display:block}
.tcard.wide .tart{aspect-ratio:auto;height:150px}
.tlabel{position:absolute;top:14px;left:14px;font-size:12.5px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;padding:8px 13px;border-radius:999px}
.tbody{padding:22px 22px 26px;min-width:0}
.tbody h3{font-size:28px;line-height:1.12;margin:0 0 16px}
.tcard ul{display:flex;flex-wrap:wrap;gap:8px;margin:0;padding:0;list-style:none}
.tcard li{font-size:13.5px;font-weight:600;line-height:1.3;padding:8px 13px;border-radius:999px;background:var(--amber);color:var(--ink)}
.tcard li:nth-child(5n+2){background:var(--beige)}
.tcard li:nth-child(5n+3){background:#f6e1c0}
.tcard li:nth-child(5n+4){background:var(--orange)}
.tcard li:nth-child(5n+5){background:#e6d2bc}
.note{font-size:13.5px;color:var(--ink2);margin:20px 0 0}
.exp{margin-top:40px;display:grid;gap:22px}
.job{background:var(--white);border:1px solid var(--line);border-radius:18px;padding:26px 28px}
.job .jh{display:flex;justify-content:space-between;flex-wrap:wrap;gap:6px 18px;align-items:baseline}
.job h3{font-size:30px;line-height:1.1}
.job .jd{font-weight:600;color:var(--orange-d);font-size:15px}
.job .jo{color:var(--ink2);font-size:15px;margin:4px 0 14px;font-weight:500}
.job ul{margin:0;padding-left:20px;display:grid;gap:8px;font-size:15.5px}
.job li::marker{color:var(--orange-d)}
.early{margin-top:22px;background:var(--cream);border-radius:18px;padding:22px 28px;border:1px solid var(--line)}
.early h3{font-size:24px;margin-bottom:10px}
.early ul{margin:0;padding:0;list-style:none;display:grid;gap:6px;font-size:15px}
.early li span{color:var(--ink2)}
.arc{margin-top:40px;background:var(--white);border:1px solid var(--line);border-radius:18px;padding:26px 24px 22px}
.axis{position:relative;height:22px;margin-left:300px;border-bottom:1px solid var(--line)}
.axis span{position:absolute;top:0;font-size:11.5px;color:var(--ink2);transform:translateX(-50%)}
.arow{display:grid;grid-template-columns:300px minmax(0,1fr);gap:0;align-items:center;min-height:44px;border-bottom:1px dashed var(--line)}
.arow:last-child{border-bottom:0}
.alab{padding:6px 14px 6px 0;font-size:13.5px;line-height:1.3}
.alab b{display:block;font-weight:700}
.alab span{color:var(--ink2);font-size:12.5px}
.atrack{position:relative;height:22px}
.abar{position:absolute;top:2px;height:18px;border-radius:5px;min-width:7px}
.abar.ic{background:var(--amber)}.abar.mgr{background:var(--orange)}.abar.dir{background:var(--ink)}
.legend{display:flex;gap:18px;flex-wrap:wrap;margin-top:16px;font-size:13px;color:var(--ink2)}
.legend i{display:inline-block;width:12px;height:12px;border-radius:3px;margin-right:6px;vertical-align:-1px}
.plansec{background:var(--cream)}
.plansec .wrap>h2,.plansec .wrap>.lede,.plansec .wrap>.eyebrow{text-align:center;margin-left:auto;margin-right:auto}
.plansec h2{max-width:22ch}
.plansec .lede{max-width:60ch}
.steps{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;margin-top:40px;position:relative}
.steps::before{content:"";position:absolute;left:6%;right:6%;top:19px;border-top:2px dashed #20181433}
.step{display:flex;flex-direction:column;align-items:center;min-width:0;position:relative}
.stag{background:var(--white);font-size:13px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:11px 18px;margin-bottom:22px;position:relative;white-space:nowrap;border-radius:999px;border:1px solid var(--line)}
.stag.dark{background:var(--ink);color:var(--cream);border-color:var(--ink)}
.pcard{background:var(--white);border-radius:18px;padding:24px 22px 28px;width:100%;flex:1;min-width:0}
.pcard svg{display:block;width:120px;height:auto;margin-bottom:20px}
.pcard h3{font-size:27px;line-height:1.12;margin:0 0 14px}
.pcard ul{margin:0;padding-left:18px;display:grid;gap:9px;font-size:15px;line-height:1.45}
.pcard li::marker{color:var(--orange)}
.pnote{margin:28px auto 0;color:var(--ink2);max-width:70ch;text-align:center;font-size:14px}
.pcta{text-align:center;margin-top:26px}
@media(max-width:980px){.steps{grid-template-columns:repeat(2,minmax(0,1fr))}.steps::before{display:none}}
@media(max-width:600px){.steps{grid-template-columns:minmax(0,1fr)}.step{align-items:flex-start}}
.creds{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:18px;margin-top:36px}
.cred{background:var(--white);border:1px solid var(--line);border-radius:16px;padding:22px 24px}
.cred.hl{background:var(--ink);color:var(--cream);border-color:var(--ink)}
.cred h3{font-size:25px;line-height:1.15}
.cred p{margin:6px 0 0;font-size:15px;color:var(--ink2)}
.cred.hl p{color:#e9e1da}
.quotes{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,340px),1fr));gap:20px;margin-top:36px}
.quote{background:var(--white);border:1px solid var(--line);border-radius:16px;padding:26px 24px;margin:0;display:flex;flex-direction:column;min-width:0}
.quote:before{content:"\201C";font-family:var(--display);font-size:60px;line-height:.6;color:var(--orange);display:block;margin-bottom:10px}
.quote p{margin:0 0 18px;font-size:16.5px;flex:1}
.quote cite{font-style:normal;font-size:14px;color:var(--ink2)}
.quote cite b{display:block;color:var(--ink);font-size:15.5px}
.recs{display:grid;gap:22px;margin-top:40px}
.rec{background:var(--white);border:1px solid var(--line);border-radius:18px;padding:28px 30px}
.rec h3{font-size:28px}
.rec .rm{color:var(--ink2);font-size:14.5px;margin:4px 0 18px}
.rec p{margin:0 0 14px;font-size:16px}
.rec p:last-child{margin-bottom:0}
footer.ft{background:var(--ink);color:var(--cream);border-radius:24px;margin:0 16px 16px;padding:64px 20px;text-align:center}
footer.ft h2{color:#fff;max-width:22ch;margin:0 auto}
footer.ft p{color:#e9e1da;max-width:58ch;margin:16px auto 0}
footer.ft .cta{justify-content:center}
footer.ft .btn{background:#fff;color:var(--ink)!important;border-color:#fff}
footer.ft .btn.ghost{background:transparent;color:#fff!important;border-color:#ffffff88}
.fine{font-size:13px;color:#cdbfb3;margin-top:28px}
.skip{position:absolute;left:-9999px}
@media(max-width:820px){
 section{padding:60px 0}
 .hero .grid{grid-template-columns:minmax(0,1fr)}
 .photo{max-width:300px;order:-1;margin:0 auto 12px}
 .stats .grid{grid-template-columns:repeat(2,minmax(0,1fr))}
 .stat:nth-child(3){border-left:0}
 .axis{margin-left:0}
 .axis span:nth-child(even){display:none}
 .arow{grid-template-columns:minmax(0,1fr);padding:8px 0}
 .alab{padding:0 0 4px}
 .logo{font-size:22px}
}
"""

def tool_card(i, title, items, unit, wide=False):
    if wide:
        bg, shapes, vb = art_svgs.hub()
    else:
        bg, shapes = art_svgs.ARTS[i % len(art_svgs.ARTS)]()
        vb = "0 0 400 200"
    tags = ["#f0b66e", "#e8892b", "#f6e1c0", "#e6d2bc", "#f1e7dc", "#d9a35a"]
    tag = tags[i % len(tags)]
    svg = '<svg viewBox="%s" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="1000" height="200" fill="%s"/>%s</svg>' % (vb, bg, shapes)
    lis = "".join("<li>%s</li>" % e(t) for t in items)
    return ('<article class="tcard%s"><div class="tart">%s<span class="tlabel" style="background:%s;color:#201814">%d %s</span></div>'
            '<div class="tbody"><h3>%s</h3><ul>%s</ul></div></article>') % (" wide" if wide else "", svg, tag, len(items), unit, e(title), lis)


VALUE_ART = [
    '<svg viewBox="0 0 200 40" aria-hidden="true"><text x="0" y="31" font-family="Figtree,sans-serif" font-size="30" font-weight="700" fill="#e8892b">1</text><text x="20" y="31" font-family="Figtree,sans-serif" font-size="30" font-weight="700" fill="#5b4f46">0000000</text></svg>',
    '<svg viewBox="0 0 200 40" aria-hidden="true"><g fill="#5b4f46"><rect y="2" width="140" height="3"/><rect y="9" width="140" height="3"/><rect y="16" width="140" height="3"/></g><g fill="#e8892b"><rect y="23" width="140" height="4"/><rect y="30" width="140" height="4"/></g></svg>',
    '<svg viewBox="0 0 200 40" aria-hidden="true"><path d="M0 12 Q25 2 50 12 T100 12 T150 12" stroke="#5b4f46" stroke-width="2" fill="none"/><path d="M0 28 H150" stroke="#f7f3ef" stroke-width="3"/></svg>',
    '<svg viewBox="0 0 80 40" aria-hidden="true"><circle cx="40" cy="20" r="18" fill="none" stroke="#5b4f46" stroke-width="2"/><circle cx="40" cy="20" r="11" fill="none" stroke="#5b4f46" stroke-width="2"/><circle cx="40" cy="20" r="6" fill="#e8892b"/></svg>',
    '<svg viewBox="0 0 200 40" aria-hidden="true"><g fill="#5b4f46"><circle cx="6" cy="20" r="3"/><circle cx="22" cy="20" r="4"/><circle cx="40" cy="20" r="5"/><circle cx="60" cy="20" r="6"/><circle cx="82" cy="20" r="8"/></g><circle cx="110" cy="20" r="10" fill="#f7f3ef"/><circle cx="140" cy="20" r="13" fill="#e8892b"/></svg>',
]


def sec(id_, cls, eyebrow, title, lede, body):
    return ('<section id="%s" class="%s"><div class="wrap"><p class="eyebrow">%s</p><h2>%s</h2>%s%s</div></section>'
            % (id_, cls, e(eyebrow), e(title), ('<p class="lede">%s</p>' % e(lede)) if lede else "", body))


def build(embed):
    p = []
    p.append('<div class="pf">')
    p.append('<div class="bar"><div class="wrap"><span>A portfolio made for the %s role at %s</span><a href="#summary">Start here</a></div></div>' % (e(C.ROLE), C.COMPANY))
    navs = [("summary", "Summary"), ("fit", "Role fit"), ("results", "Results"), ("cases", "Case studies"), ("values", "Values"),
            ("tools", "Tools"), ("experience", "Experience"), ("arc", "Career arc"), ("plan", "30-60-90"), ("credentials", "Credentials"), ("kind", "Kind words")]
    p.append('<header class="nav"><div class="wrap"><a class="logo" href="#top">Catherine Nolasco<i></i></a><nav class="links" aria-label="Sections">%s</nav></div></header>'
             % "".join('<a href="#%s">%s</a>' % (a, b) for a, b in navs))
    # hero
    p.append('<section id="top" class="hero"><div class="wrap"><div class="grid"><div>'
             '<p class="eyebrow">Portfolio for %s</p><h1>Catherine Nolasco<small>SHRM-CP | %s</small></h1><p class="tagline">%s</p>'
             '<p class="lede">%s</p><p class="target">Applying for: %s at %s</p><ul class="chips">%s</ul>'
             '<div class="cta"><a class="btn" href="mailto:%s">Email me</a><a class="btn ghost" href="https://www.%s">LinkedIn</a></div></div>'
             '<div class="photo"><img src="data:image/jpeg;base64,%s" alt="Catherine Nolasco" width="560" height="704"></div></div></div></section>'
             % (C.COMPANY, e(C.LOCATION), e(C.HERO_TAG), e(C.HERO_LEDE), e(C.ROLE), C.COMPANY,
                "".join("<li>%s</li>" % e(k) for k in C.HERO_KEYWORDS), C.EMAIL, C.LINKEDIN, HEADSHOT))
    p.append('<div class="stats"><div class="wrap"><div class="grid">%s</div></div></div>' % "".join('<div class="stat"><b>%s</b><span>%s</span></div>' % (e(a), e(b)) for a, b in C.STATS))
    p.append(sec("summary", "", "Summary", "Who I am, in five lines", "",
                 '<ul class="sumlist">%s</ul>' % "".join("<li>%s</li>" % e(s) for s in C.summary)))
    fit = "".join('<article class="fit %s"><p class="lab">%s</p><h3>%s</h3><ul>%s</ul></article>' % (cls, e(lab), e(t), "".join("<li>%s</li>" % e(x) for x in bl))
                  for lab, t, cls, bl in C.FIT)
    p.append(sec("fit", "alt", "Role fit", "What you will own, and what I have done", "Each area of the role description, matched to real work from my resume.", '<div class="cards">%s</div>' % fit))
    nums = "".join('<div class="num"><b>%s</b><h3>%s</h3><p>%s</p></div>' % (e(a), e(b), e(c)) for a, b, c in C.RESULTS)
    p.append(sec("results", "", "Results", "Numbers from my own work", "", '<div class="nums">%s</div>' % nums))
    cases = ""
    for c in C.CASES:
        cases += ('<article class="case"><div class="stripe %s"></div><div class="cb"><h3>%s</h3><p class="meta">%s | %s</p>'
                  '<h4>Challenge</h4><p>%s</p><h4>What I did</h4><p>%s</p><div class="res"><h4>Result</h4><p>%s</p></div>'
                  '<h4>What I would do differently</h4><p>%s</p><ul class="chipsm">%s</ul></div></article>'
                  % (c["stripe"], e(c["title"]), e(c["org"]), e(c["dates"]), e(c["challenge"]), e(c["did"]), e(c["result"]), e(c["differently"]),
                     "".join("<li>%s</li>" % e(x) for x in c["chips"])))
    p.append(sec("cases", "alt", "Case studies", "Five projects, in detail", "Ridecell first, then Prezent AI. Each one includes what I would change.", '<div class="cases">%s</div>' % cases))
    vals = "".join('<article class="val"><div class="vt">%s</div><div class="vb"><h3>%s</h3><p class="def">%s</p><p class="did"><b>What I did</b>%s</p></div></article>'
                   % (VALUE_ART[i], e(t), e(d), e(w)) for i, (t, d, w) in enumerate(C.VALUES))
    p.append(sec("values", "", "Values", "How Valon's values show up in my work", "Each of the five values, paired with something I actually did.", '<div class="vals">%s</div>' % vals))
    cards = "".join(tool_card(i, t, items, "tools") for i, (t, items) in enumerate(C.TOOL_CATS))
    compl = [x.strip() for x in C.comp.split(" | ")]
    cards += tool_card(6, "Core competencies", compl, "areas", wide=True)
    p.append(sec("tools", "alt", "Tools and systems", "The systems I know", "Grouped by what they do.",
                 '<div class="tools">%s</div><p class="note">Card illustrations are simplified examples with sample shapes, not screenshots of real systems or data.</p>' % cards))
    # experience
    def job(t, d, o, bl):
        return '<article class="job"><div class="jh"><h3>%s</h3><span class="jd">%s</span></div><p class="jo">%s</p><ul>%s</ul></article>' % (e(t), e(d), e(o), "".join("<li>%s</li>" % e(x) for x in bl))
    exp = (job("Director of People Operations", "Dec 2018 - Jan 2026", "Ridecell Inc. | Remote, San Francisco, CA | Fleet intelligence platform, 300+ employees in US, Canada, Germany, India, and Japan", C.ridecell)
           + job("People Operations Consultant (Director)", "Jan 2026 - Jun 2026", "Ridecell Inc. | Remote, San Francisco, CA", C.consult)
           + job("Head of People Operations", "Feb 2026 - Apr 2026", "Prezent AI | Remote | $70M+ VC-funded AI SaaS, 500+ employees in US and India, reporting to the CEO", C.prezent)
           + job("Manager, People Operations", "Oct 2017 - Dec 2018", "Munchery | San Francisco, CA | Meal delivery, 700+ employees across NY, SF, Seattle, and LA", C.munch)
           + '<div class="early"><h3>Earlier experience</h3><ul>%s</ul></div>' % "".join("<li><b>%s</b>, %s <span>| %s | %s</span></li>" % (e(a), e(b), e(c_), e(d)) for a, b, c_, d in C.earlier))
    p.append(sec("experience", "", "Experience", "Where I have worked", "", '<div class="exp">%s</div>' % exp))
    # arc
    y0, y1 = 2013.0, 2026.6
    span = y1 - y0
    axis = "".join('<span style="left:%.2f%%">%d</span>' % ((y - y0) / span * 100, y) for y in range(2013, 2027))
    rows = ""
    for s, en, t, co, dt, tier in C.ARC:
        rows += ('<div class="arow"><div class="alab"><b>%s</b><span>%s | %s</span></div><div class="atrack"><div class="abar %s" style="left:%.2f%%;width:%.2f%%" title="%s"></div></div></div>'
                 % (e(t), e(co), e(dt), tier, (s - y0) / span * 100, (en - s) / span * 100, e(dt)))
    p.append(sec("arc", "alt", "Career arc", "Thirteen years, drawn to scale", "Bar length shows real start and end dates. The two 2026 roles overlapped.",
                 '<div class="arc"><div class="axis">%s</div>%s<div class="legend"><span><i style="background:var(--amber)"></i>Coordinator to Specialist</span><span><i style="background:var(--orange)"></i>Manager</span><span><i style="background:var(--ink)"></i>Director and Head</span></div></div>' % (axis, rows)))
    # plan
    steps = "".join('<div class="step"><span class="stag%s">%s</span><div class="pcard">%s<h3>%s</h3><ul>%s</ul></div></div>'
                    % (" dark" if i == len(C.PLAN) - 1 else "", e(a), art_svgs.PLAN_ART[i], e(b), "".join("<li>%s</li>" % e(x) for x in c))
                    for i, (a, b, c) in enumerate(C.PLAN))
    p.append('<section id="plan" class="plansec"><div class="wrap"><p class="eyebrow">30-60-90</p><h2>How I would start</h2><p class="lede">A proposed plan built around the responsibilities in the role description.</p>'
             '<div class="steps">%s</div><p class="pnote">This is a starting point. I would adjust it after the first conversations with the People team and partners.</p>'
             '<div class="pcta"><a class="btn" href="mailto:%s">Let\'s talk</a></div></div></section>' % (steps, C.EMAIL))
    # creds
    creds = "".join('<article class="cred%s"><h3>%s</h3><p>%s</p>%s</article>' % (" hl" if i == 0 else "", e(a), e(b), ("<p>%s</p>" % e(c_)) if c_ else "") for i, (a, b, c_) in enumerate(C.CREDS))
    p.append(sec("credentials", "", "Credentials", "Certification and education", "", '<div class="creds">%s</div>' % creds))
    # testimonials + recs (last content)
    quotes = "".join('<figure class="quote"><p>%s</p><cite><b>%s</b>%s | %s</cite></figure>' % (e(q), e(n), e(r), e(s)) for n, r, s, q in C.TESTIMONIALS)
    recs = "".join('<article class="rec"><h3>%s</h3><p class="rm">%s | %s | %s</p>%s</article>'
                   % (e(n), e(t), e(d), e(w), "".join("<p>%s</p>" % e(x) for x in ps)) for n, t, d, w, ps in C.RECS)
    p.append(sec("kind", "alt", "Kind words", "What colleagues have said", "Six messages and four LinkedIn recommendations, shared as written.",
                 '<div class="quotes">%s</div><h3 style="margin-top:56px;font-size:34px">LinkedIn recommendations</h3><div class="recs">%s</div>' % (quotes, recs)))
    p.append('<footer class="ft" id="contact"><h2>Let\'s talk about %s</h2><p>I would love to talk about how a People Operations function that runs on clear playbooks, good systems, and thoughtful automation can free the team for the conversations only people can have.</p>'
             '<div class="cta"><a class="btn" href="mailto:%s">%s</a><a class="btn ghost" href="https://www.%s">%s</a></div>'
             '<p class="fine">%s | San Francisco Bay Area, CA<br>This is an independent portfolio styled after the %s brand. It is not affiliated with %s.</p></footer>'
             % (C.COMPANY, C.EMAIL, C.EMAIL, C.LINKEDIN, C.LINKEDIN, "", C.COMPANY, C.COMPANY))
    p.append("</div>")
    body = "\n".join(p).replace('<p class="fine"> | ', '<p class="fine">')
    body = body.replace('<p class="fine">San Francisco', '<p class="fine">San Francisco')
    css = font_css(embed) + CSS + TOOL_CSS
    if embed:
        return ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
                '<title>Catherine Nolasco | %s portfolio for %s</title><meta name="description" content="Portfolio of Catherine Nolasco, SHRM-CP, for the %s role at %s."><style>%s</style></head><body>%s</body></html>'
                % (e(C.ROLE), C.COMPANY, e(C.ROLE), C.COMPANY, css, body))
    link = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700&family=Newsreader:wght@400;500&display=swap" rel="stylesheet">'
    return link + "<style>" + css + "</style>" + body


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "index.html")
    open(out, "w").write(build(True))
    open(os.path.join(HERE, "artifact_fragment.html"), "w").write(build(False))
    print("ok", os.path.getsize(out))
