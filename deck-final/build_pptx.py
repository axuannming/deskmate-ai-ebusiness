import re, subprocess, sys
from pathlib import Path
from pptx import Presentation

SLIDES_DIR = Path(r"./deck-final\slides")
COMBINED = Path(r"./deck-final\slides\deck-combined.html")
OUT_PPTX = Path(r"./submission\DeskMate_AI_Presentation.pptx")
HD_SCRIPT = Path(r"~\.gemini\config\skills\huashu-design\scripts\pptx_from_rendered.py")

slide_files = sorted([f for f in SLIDES_DIR.glob("0*.html")])

styles_all = []
sections_all = []

for idx, sf in enumerate(slide_files, start=1):
    html = sf.read_text(encoding="utf-8")
    css_m = re.search(r"<style>(.*?)</style>", html, re.S)
    body_m = re.search(r"<body>(.*?)</body>", html, re.S)
    css = css_m.group(1) if css_m else ""
    body = body_m.group(1) if body_m else ""
    scope = f".s{idx}"
    # Prefix selectors with .sN cleanly
    scoped_rules = []
    for block in re.split(r"(?<=\})", css):
        block = block.strip()
        if not block or block.startswith("/*") and "}" not in block:
            continue
        if "{" not in block:
            continue
        sel_part, rest = block.split("{", 1)
        sel_part = re.sub(r"/\*.*?\*/", "", sel_part, flags=re.S).strip()
        if sel_part in ("*", "html, body", "html", "body"):
            continue
        new_sels = []
        for s in sel_part.split(","):
            s = s.strip()
            if not s:
                continue
            new_sels.append(f"{scope} {s}")
        scoped_rules.append(", ".join(new_sels) + " {" + rest)
    styles_all.append("\n".join(scoped_rules))
    sections_all.append(f'<div class="slide s{idx}">\n{body}\n</div>')

combined_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>DeskMate AI — Combined 6-Slide Deck</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400&family=Noto+Sans+TC:wght@300;400;500&display=swap" rel="stylesheet">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ background: #EAE6DE; font-family: 'Inter', 'Noto Sans TC', sans-serif; color: #1F1E1C; }}
  .slide {{
    width: 1920px; height: 1080px; overflow: hidden;
    background: #F8F6F1; color: #1F1E1C;
    position: relative; margin: 0 auto 24px;
    font-family: 'Inter', 'Noto Sans TC', sans-serif;
  }}
  {"".join(styles_all)}
</style>
</head>
<body>
{"".join(sections_all)}
</body>
</html>
"""
COMBINED.write_text(combined_html, encoding="utf-8")
print("WROTE", COMBINED)

cmd = [
    sys.executable, str(HD_SCRIPT),
    str(COMBINED),
    "-o", str(OUT_PPTX),
    "--selector", ".slide",
    "--bg", "F8F6F1",
    "--font-latin", "Calibri",
    "--font-ea", "Microsoft JhengHei"
]
subprocess.run(cmd, check=True)

# Post-process: inject synced 3-minute English Speaker Notes + clickable live Wix hyperlinks on Slide 5
SPEAKER_NOTES = [
    "0:00–0:10 | Good morning. I’m [Author]. DeskMate AI is an AI receptionist for small beauty salons in Hong Kong.",
    "0:10–0:35 | A salon owner can miss booking enquiries while serving customers. At minimum wage, four hours of reception work a day for 26 days costs about 4,482 Hong Kong dollars. Our Pro plan costs 788 Hong Kong dollars per month. Salons pay us a monthly fee under a B2B Fee-for-Service model.",
    "0:35–1:05 | We start with independent Hong Kong beauty and hair salons with one to ten staff. Search and social ads build awareness. During exploration, a personal demo and a 14-day trial let owners try the booking workflow. We set up each salon’s services and opening hours, and the assistant handles Cantonese and English enquiries.",
    "1:05–1:35 | Enquiries from WhatsApp, Instagram and the salon website go through the same booking workflow. It checks one shared calendar before confirming a time. Managed cloud capacity can scale with busy periods. We plan to use cards for recurring payments, wallets where supported and FPS for annual invoices.",
    "1:35–2:35 | Here is the live Wix prototype. I’ll open the booking demo. The example shows a gel manicure booking at six-thirty. Next, the pricing page shows three monthly plans, each with a 14-day trial, followed by our simulated HK$0 trial checkout. The Book a demo form gives a salon owner a direct way to contact us.",
    "2:35–3:00 | We’re asking for 400,000 Hong Kong dollars for the first year. Development takes the largest share. We aim for 60 paying salons by month twelve. If all 60 choose Pro, that’s 47,280 Hong Kong dollars in monthly subscription revenue. Thank you."
]

BASE_URL = "https://deskmate-ai-demo.example.com"
LINK_MAP = {
    "headless-tthgaiftzjw": BASE_URL + "/",
    "Open Wix Home": BASE_URL + "/",
    "Booking Example": BASE_URL + "/#demo",
    "Plans & Checkout": BASE_URL + "/#pricing",
    "Book a Demo Form": BASE_URL + "/#contact",
}

prs = Presentation(str(OUT_PPTX))
for idx, slide in enumerate(prs.slides):
    if idx < len(SPEAKER_NOTES):
        notes_slide = slide.notes_slide
        notes_slide.notes_text_frame.text = SPEAKER_NOTES[idx]
    if idx == 4:  # Slide 5: attach real clickable hyperlinks
        linked = 0
        for sh in slide.shapes:
            if sh.has_text_frame:
                txt = sh.text_frame.text.strip()
                for key, url in LINK_MAP.items():
                    if key in txt:
                        for p in sh.text_frame.paragraphs:
                            for r in p.runs:
                                r.hyperlink.address = url
                        sh.click_action.hyperlink.address = url
                        linked += 1
        print(f"SLIDE 5 HYPERLINKS ATTACHED: {linked}")

prs.save(str(OUT_PPTX))
print("FINAL PPTX SAVED:", OUT_PPTX)
