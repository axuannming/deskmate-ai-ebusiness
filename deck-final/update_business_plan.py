from pathlib import Path
from copy import deepcopy
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn

SRC = Path(r"./submission\Business_Plan_Updated.docx")
BACKUP = Path(r"./submission\Business_Plan_Updated_prev_backup.docx")
SHOTS = Path(r"./submission\wix-screenshots")
NEW_URL = "https://deskmate-ai-demo.example.com"

doc = docx.Document(str(BACKUP))

def set_para_text(para, new_text):
    if not para.runs:
        para.add_run(new_text)
        return
    r0 = para.runs[0]
    fname = r0.font.name
    fsize = r0.font.size
    fbold = r0.font.bold
    fital = r0.font.italic
    fcolor = r0.font.color.rgb if r0.font.color else None
    for r in para.runs[1:]:
        r.text = ""
    r0.text = new_text
    if fname: r0.font.name = fname
    if fsize: r0.font.size = fsize
    r0.font.bold = fbold
    r0.font.italic = fital
    if fcolor: r0.font.color.rgb = fcolor

def set_cell_text(cell, new_text):
    p = cell.paragraphs[0]
    set_para_text(p, new_text)
    for extra in cell.paragraphs[1:]:
        set_para_text(extra, "")

# 1. Cover page URL update — cleanly update the <w:hyperlink> XML AND its relationship target!
for rel in doc.part.rels.values():
    if "<wix-handle>.wixsite.com" in str(rel._target):
        rel._target = NEW_URL

for p in doc.paragraphs:
    for hl in p._element.findall(qn("w:hyperlink")):
        t_nodes = hl.findall(".//" + qn("w:t"))
        if t_nodes:
            t_nodes[0].text = NEW_URL
            for extra_t in t_nodes[1:]:
                extra_t.text = ""

# 2. Update §2.3 Revenue model
for p in doc.paragraphs:
    if p.text.startswith("We use the Fee-for-Service revenue model"):
        set_para_text(
            p,
            "We use the Fee-for-Service revenue model, charging a predictable monthly fee based on the value of the 24/7 reception service rather than a per-booking Fee-for-Transaction commission (Schneider, 2017). Salons select one of three monthly tiers (Table 2). Each plan includes a time-limited 14-day free trial (HK$0 due today) as a low-friction onboarding pathway — distinct from a permanent freemium tier — allowing owners to verify the bilingual booking workflow before paid billing begins, tracked by trial-to-paid conversion rate."
        )

# 3. Update §3 Market Analysis
for p in doc.paragraphs:
    if p.text.startswith("Clinics and tutorial centres are secondary segments"):
        set_para_text(
            p,
            "Clinics and tutorial centres form Year 2 expansion segments. Applying online market segmentation and virtual space design (Schneider, 2017), the live Wix prototype's Industries switcher gives each segment a dedicated entry point while serving browsers, shoppers and buyers on one site."
        )

# 4. Update §4 Customer Analysis
for p in doc.paragraphs:
    if p.text.startswith("An AI receptionist is a fairly complex product"):
        set_para_text(
            p,
            "An AI receptionist is a complex B2B service, and buyer trust increases as communication shifts from mass media to the Web (many-to-one) to personal contact (one-to-one) (Schneider, 2017). We use targeted social and search ads to control acquisition cost, the interactive Wix booking demo and one-to-one Book a Demo form to lower conversion cost, and touchpoint consistency across WhatsApp, Instagram and the website to reinforce trust. After sign-up, opt-in performance reports (permission marketing, avoiding unsolicited commercial e-mail) lower retention cost and move salons toward familiarity and commitment under Hong Kong's Personal Data (Privacy) Ordinance (PDPO) with clear opt-out."
        )

# 5. Update §5.2 Technology infrastructure
for p in doc.paragraphs:
    if p.text.startswith("At 60 salons on Pro, the plan allows"):
        set_para_text(
            p,
            "At 60 salons on Pro, the platform handles up to 60,000 monthly conversations, peaking in evenings and before holidays. Following a three-tier client–Web–database architecture, managed cloud (PaaS), serverless functions, and a Content Delivery Network (CDN) meet key hosting criteria — functionality, reliability, scalability, security, backup and cost efficiency — while minimising latency across Hong Kong mobile and Wi-Fi networks (Schneider, 2017; Table 6)."
        )

# 6. Update §5.3 Payment systems
for p in doc.paragraphs:
    if p.text.startswith("The proposed service uses Visa and Mastercard"):
        set_para_text(
            p,
            "Recurring monthly subscriptions use Visa and Mastercard, while Apple Pay and Google Pay provide express checkout for decisive buyers (Schneider, 2017). Hong Kong's Faster Payment System (FPS) supports annual invoices without card fees. Stripe notes cards and digital wallets are core Hong Kong online payment methods (Stripe, n.d.). Card processing is outsourced to certified gateways. Our live Wix prototype includes a safe Simulated Checkout Mock-up demonstrating plan switching, HK$0 trial activation and payment method selection without real billing."
        )

# 7. Update §6 Financial Plan
for p in doc.paragraphs:
    if p.text.startswith("The HK$400,000 request covers the first year"):
        set_para_text(
            p,
            "The HK$400,000 seed request — suited to angel or early seed funding given falling cloud start-up costs — funds Year 1 build and operations. Ongoing costs (HK$220,000) equal 122% of initial development (HK$180,000), squarely within Schneider's (2017) 50%–200% TCO operating range. At 60 active Pro salons, projected monthly revenue reaches HK$47,280 against HK$18,333 average ongoing monthly cost (2.6x coverage), depending on plan mix. Beyond quantitative ROI, DeskMate AI reduces owners' opportunity cost of missed treatment hours and builds intangible loyalty benefits."
        )

# Update Tables 3, 5, 6
t3 = doc.tables[3]
set_cell_text(
    t3.rows[4].cells[1],
    "Serves browsers (interactive bilingual booking demo, '14-Day Free Trial' trigger words), shoppers (3-tier plan comparison, minimum-wage savings slider, FAQ) and buyers (direct 'Start 14-Day Trial' button into simulated express checkout)."
)

t5 = doc.tables[5]
set_cell_text(t5.rows[1].cells[1], "Sticky header with 6 clear links (Home, How It Works, Industries, Pricing, FAQ, Contact) plus direct trial and demo CTAs.")
set_cell_text(t5.rows[2].cells[1], "Verified responsive layout across 1440x900 desktop and 375x812 mobile with slide-down mobile navigation and zero horizontal overflow.")
set_cell_text(t5.rows[3].cells[1], "Lightweight static assets (<40 KB code) with salon photography served via Wix Media CDN edge servers.")
set_cell_text(t5.rows[4].cells[1], "Interactive Cantonese/English booking simulator plus a validated one-to-one 'Book a Demo' contact form (Schneider, 2017 accessibility goals).")
set_cell_text(t5.rows[5].cells[1], "Clear hierarchy presenting pricing, live booking example, savings calculator, Industries tabs and expandable FAQ.")
set_cell_text(t5.rows[6].cells[1], "Transparent HK$ pricing, clearly labeled 'Sample testimonial', safe 'Simulated Checkout' notice and PDPO privacy statement; higher trust supports loyalty (a 5% loyalty lift can raise profit 25%–80%; Schneider, 2017).")

t6 = doc.tables[6]
set_cell_text(t6.rows[1].cells[1], "Cost efficiency (no servers to buy or maintain) and dynamic resource allocation as salon count scales from 1 to 60+ (Wix Headless + managed cloud).")
set_cell_text(t6.rows[2].cells[1], "Pay-per-use event execution for incoming messages and checkout flows: near-zero idle cost overnight and automatic scaling during evening booking peaks.")
set_cell_text(t6.rows[3].cells[1], "Low-latency mobile commerce and instant checkout over Hong Kong 5G networks, while remaining fast over 4G and salon Wi-Fi.")
# Clone row 3 XML so borders, padding, and fonts match 100%!
new_tr = deepcopy(t6.rows[3]._tr)
t6._tbl.append(new_tr)
cdn_row = t6.rows[-1]
set_cell_text(cdn_row.cells[0], "Content Delivery Network (CDN)")
set_cell_text(cdn_row.cells[1], "Caches salon photography on edge servers (Wix Media CDN) close to Hong Kong visitors, reducing network latency and supporting fast loading times.")

# Remove blank page-break paragraph right before References so Page 4 does NOT spill a blank Page 5
for idx, p in enumerate(list(doc.paragraphs)):
    if p.text.strip() == "References":
        p.paragraph_format.page_break_before = True
        if idx > 0:
            prev = doc.paragraphs[idx - 1]
            if not prev.text.strip() and prev._element.findall(".//" + qn("w:br")):
                prev._element.getparent().remove(prev._element)
        break

# 8. Add clean Appendix page after References
h1_style = next((p.style for p in doc.paragraphs if p.text.startswith("1. Executive")), None)
h_app = doc.add_paragraph("Appendix: Live Wix Prototype Screenshots")
if h1_style is not None:
    h_app.style = h1_style
h_app.paragraph_format.page_break_before = True

p_app_intro = doc.add_paragraph(
    f"Live prototype URL: {NEW_URL}  |  All screenshots below were captured directly from the live Wix Headless deployment (verified across 1440×900 desktop and 375×812 mobile viewports)."
)
for r in p_app_intro.runs:
    r.font.size = Pt(9.5)
    r.font.color.rgb = RGBColor(0x4A, 0x46, 0x40)

def add_figure_pair(img1, cap1, img2, cap2, width_in=3.15):
    tbl = doc.add_table(rows=2, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    for ci, (im, cap) in enumerate([(img1, cap1), (img2, cap2)]):
        p_img = tbl.rows[0].cells[ci].paragraphs[0]
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(4)
        p_img.paragraph_format.space_after = Pt(2)
        p_img.add_run().add_picture(str(im), width=Inches(width_in))
        p_cap = tbl.rows[1].cells[ci].paragraphs[0]
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(6)
        rc = p_cap.add_run(cap)
        rc.font.size = Pt(8.5)
        rc.font.italic = True
        rc.font.color.rgb = RGBColor(0x4A, 0x46, 0x40)

add_figure_pair(
    SHOTS / "wix-home.png",
    "Figure A1. Live Wix Homepage & Clear 6-Link Navigation (Desktop 1440×900)",
    SHOTS / "wix-demo.png",
    "Figure A2. Interactive Cantonese/English Booking Simulator & Synced Shared Calendar"
)
add_figure_pair(
    SHOTS / "wix-pricing.png",
    "Figure A3. B2B Fee-for-Service Pricing Tiers (Starter / Pro / Premium, 14-Day Trial)",
    SHOTS / "wix-checkout.png",
    "Figure A4. Safe Interactive Checkout Mock-up (HK$0 Today, Cards / Wallets / FPS)"
)

tbl2 = doc.add_table(rows=2, cols=2)
tbl2.alignment = WD_TABLE_ALIGNMENT.CENTER
tbl2.autofit = False
p_c1 = tbl2.rows[0].cells[0].paragraphs[0]
p_c1.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_c1.add_run().add_picture(str(SHOTS / "wix-contact.png"), width=Inches(3.15))
rc1 = tbl2.rows[1].cells[0].paragraphs[0].add_run("Figure A5. One-to-One 'Book a Demo' Contact Form with PDPO Privacy Notice")
rc1.font.size = Pt(8.5); rc1.font.italic = True; rc1.font.color.rgb = RGBColor(0x4A, 0x46, 0x40)
tbl2.rows[1].cells[0].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER

p_c2 = tbl2.rows[0].cells[1].paragraphs[0]
p_c2.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_c2.add_run().add_picture(str(SHOTS / "wix-mobile.png"), height=Inches(2.1))
rc2 = tbl2.rows[1].cells[1].paragraphs[0].add_run("Figure A6. Verified Mobile Responsive Layout (375×812, Zero Overflow)")
rc2.font.size = Pt(8.5); rc2.font.italic = True; rc2.font.color.rgb = RGBColor(0x4A, 0x46, 0x40)
tbl2.rows[1].cells[1].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.save(str(SRC))
print("SAVED CLEAN DOCX:", SRC)
