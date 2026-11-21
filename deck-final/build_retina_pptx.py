import io
from pathlib import Path
from playwright.sync_api import sync_playwright
from pypdf import PdfWriter, PdfReader
from pptx import Presentation
from pptx.util import Inches
from pptx.enum.shapes import MSO_SHAPE

SLIDES_DIR = Path(r"./deck-final\slides")
RETINA_DIR = Path(r"./deck-final\retina")
SHOTS_DIR = Path(r"./deck-final\shots")
ART_DIR = Path(r"./artifacts/final_deck")
OUT_PPTX = Path(r"./submission\DeskMate_AI_Presentation.pptx")
OUT_PDF = Path(r"./submission\DeskMate_AI_Presentation.pdf")

for d in (RETINA_DIR, SHOTS_DIR, ART_DIR):
    d.mkdir(parents=True, exist_ok=True)

slide_files = sorted(SLIDES_DIR.glob("0*.html"))

SPEAKER_NOTES = [
    "0:00-0:10 | Good morning. DeskMate AI is a bilingual AI receptionist that answers WhatsApp, Instagram and website enquiries for small Hong Kong beauty salons.",
    "0:10-0:40 | Salons with one to ten staff rarely have a receptionist, so enquiries are missed during treatments and after closing. At minimum wage, four hours of reception a day costs about 4,482 Hong Kong dollars a month; our Pro plan costs 788, which is 82% less. This is B2B e-commerce on a Fee-for-Service model. Salons pay a predictable monthly fee with no per-booking commission, and the 14-day trial is time limited, so it is not a freemium tier.",
    "0:40-1:05 | We target owner-run salons in Mong Kok, Causeway Bay and Tsim Sha Tsui. As a new brand, we focus on the awareness and exploration stages of the customer relationship life cycle: social and search ads inform owners, then the web demo, the trial and a one-to-one demo explain the product. Our targets are 25% trial-to-paid conversion and under 5% monthly churn.",
    "1:05-1:30 | All three channels feed one booking engine and one shared calendar. It runs on a three-tier design with managed cloud and serverless functions, so we pay per use and scale for evening peaks, while a CDN keeps pages fast on mobile. Salons pay by recurring card, Apple Pay or Google Pay, or FPS for annual invoices.",
    "1:30-2:30 | Here is the live Wix prototype. The navigation is clear and the layout works on mobile. In the booking demo, I type a salon name, Lumière Nail Studio. A client asks in mixed Cantonese and English for a six-thirty gel manicure. DeskMate AI replies in that salon's name and then confirms it on the shared calendar. On Pricing, each plan starts with a 14-day trial; I'll choose Pro, and the simulated checkout shows HK$0 due today. Finally, the Book a Demo form is our one-to-one touchpoint, with an unticked opt-in box and a PDPO notice.",
    "2:30-3:00 | We are asking for 400,000 Hong Kong dollars in angel or seed funding, estimated with total cost of ownership. Ongoing costs are 122% of the initial build, inside the textbook's 50 to 200% range. We cover monthly operating costs at 24 Pro salons and aim for 60 by month twelve, or 47,280 dollars a month if all choose Pro. Thank you."
]

ALT_TEXTS = [
    "Slide 1: DeskMate AI cover. 24/7 Cantonese and English AI receptionist for independent Hong Kong beauty and hair salons. Pro HK$788/month (82% lower than part-time staff), 14-day free trial and setup. Presented by Individual Portfolio Author.",
    "Slide 2: Problem and Business Model. Missed salon enquiries during treatments and after closing. B2B Fee-for-Service subscriptions: Starter HK$388, Pro HK$788 (-82% vs HK$4,482 part-time minimum wage benchmark), Premium HK$1,488, with a time-limited 14-day trial.",
    "Slide 3: Market and Customer Strategy. Target Hong Kong beauty and hair salons (1 to 10 staff, MK/CWB/TST), Year 2 goal 10 clinics or tutorial centres by Month 18, 25% trial conversion, under 5% churn; Schneider 5-stage CRLC (Awareness, Exploration [Targets], Familiarity, Commitment, Separation).",
    "Slide 4: Operations and Technology. WhatsApp, Instagram DM and website chat share one three-tier PaaS/Serverless/CDN/5G DeskMate AI engine and one shared calendar. Payments: Visa/Mastercard, Apple/Google Pay, Hong Kong FPS (10% off prepaid annual plans), PDPO and permission opt-in.",
    "Slide 5: Live Wix Prototype Walkthrough. Live Wix Headless URL with uncropped Desktop Home, Simulated HK$0 Checkout, and Mobile 375x812 screenshots plus clickable links to Home, personalised salon chat simulation (#demo), Plans (#pricing), Checkout (#checkout), and Book a Demo Form (#contact).",
    "Slide 6: Year 1 Funding and Unit Economics. HK$400,000 angel/seed TCO ask (Development 45% HK$180k, Marketing 30% HK$120k, Infrastructure 15% HK$60k, Maintenance 10% HK$40k; 122% ongoing ratio; mostly labour, 10/10/80 pattern). Break-even at 24 Pro salons (~Month 5); 60 salons = HK$47,280/mo if all choose Pro (2.6x cost coverage)."
]

slide5_links = []
pngs = []
pdf_writer = PdfWriter()

with sync_playwright() as p:
    browser = p.chromium.launch()
    for idx, f in enumerate(slide_files, start=1):
        # 2x Retina PNG for PPTX + 1x PNG for shots/artifact + Vector PDF page
        page = browser.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=2)
        page.goto(f.as_uri(), wait_until="networkidle")
        page.evaluate("() => document.fonts.ready")
        page.wait_for_timeout(350)
        out_png = RETINA_DIR / f"{f.stem}.png"
        page.screenshot(path=str(out_png))
        pngs.append(out_png)
        if idx == 5:
            slide5_links = page.evaluate("""() => {
                return [...document.querySelectorAll('a[href]')].map(a => {
                    const r = a.getBoundingClientRect();
                    return { href: a.href, x: r.left, y: r.top, w: r.width, h: r.height };
                });
            }""")
        pdf_buf = page.pdf(width="1920px", height="1080px", print_background=True, margin={"top":"0","right":"0","bottom":"0","left":"0"}, page_ranges="1")
        pdf_writer.add_page(PdfReader(io.BytesIO(pdf_buf)).pages[0])
        page.close()

        # Also refresh 1x preview PNG in shots/ & art/
        p1 = browser.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=1)
        p1.goto(f.as_uri(), wait_until="networkidle")
        p1.evaluate("() => document.fonts.ready")
        p1.wait_for_timeout(250)
        s_png = SHOTS_DIR / f"{f.stem}.png"
        p1.screenshot(path=str(s_png))
        (ART_DIR / f"{f.stem}.png").write_bytes(s_png.read_bytes())
        p1.close()
        print("RENDER_OK", f.name)
    browser.close()

with open(OUT_PDF, "wb") as fp:
    pdf_writer.write(fp)
print("SAVED_PDF", OUT_PDF, OUT_PDF.stat().st_size)

W_IN, H_IN = 13.333333, 7.5
prs = Presentation()
prs.slide_width = Inches(W_IN)
prs.slide_height = Inches(H_IN)
blank = prs.slide_layouts[6]

for idx, png in enumerate(pngs):
    slide = prs.slides.add_slide(blank)
    pic = slide.shapes.add_picture(str(png), Inches(0), Inches(0), width=Inches(W_IN), height=Inches(H_IN))
    # Embed accessible Alt Text per Opus 5.5 P2-10
    pic._element.nvPicPr.cNvPr.set("descr", ALT_TEXTS[idx])
    slide.notes_slide.notes_text_frame.text = SPEAKER_NOTES[idx]
    if idx == 4:
        for lk in slide5_links:
            left = Inches((lk["x"] / 1920.0) * W_IN)
            top = Inches((lk["y"] / 1080.0) * H_IN)
            width = Inches((lk["w"] / 1920.0) * W_IN)
            height = Inches((lk["h"] / 1080.0) * H_IN)
            sh = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
            sh.fill.background()
            sh.line.fill.background()
            sh.click_action.hyperlink.address = lk["href"]
        print(f"SLIDE5_HOTSPOTS_ADDED={len(slide5_links)}")

prs.save(str(OUT_PPTX))
print("SAVED_PPTX", OUT_PPTX, OUT_PPTX.stat().st_size)
