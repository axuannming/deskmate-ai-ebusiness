from pathlib import Path
import docx
from docx.shared import Cm, Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

OUT_DOCX = Path(r"./submission\Business_Plan_Updated.docx")
SHOTS = Path(r"./submission\wix-screenshots")
LIVE_URL = "https://deskmate-ai-demo.example.com"

# Classic Pure Black-and-White Business Format (Calibri monochrome)
C_INK = RGBColor(0x00, 0x00, 0x00)       # Pure black
C_BODY = RGBColor(0x00, 0x00, 0x00)      # Pure black
C_MUTED = RGBColor(0x00, 0x00, 0x00)     # Pure black
C_BRONZE = RGBColor(0x00, 0x00, 0x00)    # Pure black
HEX_HDR = "F2F2F2"                       # Classic neutral light gray header & total fill
HEX_BORDER = "BFBFBF"                    # Crisp monochrome inner divider
HEX_BLACK = "000000"                     # Pure black rules & hyperlinks
HEX_BRONZE = "000000"                    # Pure black

doc = docx.Document()

# A4 Page Setup with clean academic margins
sec = doc.sections[0]
sec.page_width = Cm(21.0)
sec.page_height = Cm(29.7)
sec.left_margin = Cm(1.80)
sec.right_margin = Cm(1.80)
sec.top_margin = Cm(1.75)
sec.bottom_margin = Cm(1.45)
sec.header_distance = Cm(0.75)
sec.footer_distance = Cm(0.70)
sec.different_first_page_header_footer = True

# Base Normal style
normal = doc.styles["Normal"]
normal.font.name = "Calibri"
normal.font.size = Pt(10.0)
normal.font.color.rgb = C_BODY
normal.paragraph_format.space_before = Pt(0)
normal.paragraph_format.space_after = Pt(3.5)
normal.paragraph_format.line_spacing = 1.12

# Running header & footer on pages 2+
hdr_p = sec.header.paragraphs[0]
hdr_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
r_h = hdr_p.add_run("DeskMate AI: E-Business Start-up Plan (SEHS2265)   |   Individual Portfolio Author")
r_h.font.name = "Calibri"
r_h.font.size = Pt(8.5)
r_h.font.color.rgb = C_MUTED

ftr_p = sec.footer.paragraphs[0]
ftr_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_f = ftr_p.add_run("Page ")
r_f.font.name = "Calibri"; r_f.font.size = Pt(8.5); r_f.font.color.rgb = C_MUTED
fld = OxmlElement("w:fldSimple")
fld.set(qn("w:instr"), "PAGE")
ftr_p._p.append(fld)

def set_p_bottom_border(para, color_hex=HEX_BORDER, sz="6", space="3"):
    pPr = para._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bot = OxmlElement("w:bottom")
    bot.set(qn("w:val"), "single")
    bot.set(qn("w:sz"), sz)
    bot.set(qn("w:space"), space)
    bot.set(qn("w:color"), color_hex)
    pBdr.append(bot)
    pPr.append(pBdr)

def add_hyperlink(para, url, text=None, color_hex=HEX_BRONZE, size_pt=10.5, bold=False):
    part = para.part
    r_id = part.relate_to(url, docx.opc.constants.RELATIONSHIP_TYPE.HYPERLINK, is_external=True)
    hl = OxmlElement("w:hyperlink")
    hl.set(qn("r:id"), r_id)
    new_run = OxmlElement("w:r")
    rPr = OxmlElement("w:rPr")
    rFonts = OxmlElement("w:rFonts")
    rFonts.set(qn("w:ascii"), "Calibri"); rFonts.set(qn("w:hAnsi"), "Calibri")
    rPr.append(rFonts)
    sz = OxmlElement("w:sz"); sz.set(qn("w:val"), str(int(size_pt * 2)))
    rPr.append(sz)
    c = OxmlElement("w:color"); c.set(qn("w:val"), color_hex)
    rPr.append(c)
    u = OxmlElement("w:u"); u.set(qn("w:val"), "single")
    rPr.append(u)
    if bold:
        rPr.append(OxmlElement("w:b"))
    new_run.append(rPr)
    t = OxmlElement("w:t")
    t.text = text or url
    new_run.append(t)
    hl.append(new_run)
    para._p.append(hl)

def set_cell_shading(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill_hex)
    tcPr.append(shd)

def set_cell_margins(cell, top=42, bottom=42, left=95, right=95):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement("w:tcMar")
    for side, val in [("top", top), ("bottom", bottom), ("left", left), ("right", right)]:
        node = OxmlElement(f"w:{side}")
        node.set(qn("w:w"), str(val))
        node.set(qn("w:type"), "dxa")
        tcMar.append(node)
    tcPr.append(tcMar)

def cm_to_dxa(cm_val):
    return int(round(cm_val / 2.54 * 1440))

def apply_fixed_col_widths(tbl, col_widths_cm):
    total_dxa = sum(cm_to_dxa(w) for w in col_widths_cm)
    tblPr = tbl._tbl.tblPr
    for tag in ("w:tblW", "w:tblLayout"):
        old = tblPr.find(qn(tag))
        if old is not None:
            tblPr.remove(old)
    tblW = OxmlElement("w:tblW")
    tblW.set(qn("w:w"), str(total_dxa))
    tblW.set(qn("w:type"), "dxa")
    tblPr.append(tblW)
    layout = OxmlElement("w:tblLayout")
    layout.set(qn("w:type"), "fixed")
    tblPr.append(layout)

    old_grid = tbl._tbl.find(qn("w:tblGrid"))
    if old_grid is not None:
        tbl._tbl.remove(old_grid)
    grid = OxmlElement("w:tblGrid")
    for w in col_widths_cm:
        gc = OxmlElement("w:gridCol")
        gc.set(qn("w:w"), str(cm_to_dxa(w)))
        grid.append(gc)
    tblPr.addnext(grid)

    for row in tbl.rows:
        for ci, cell in enumerate(row.cells):
            tcPr = cell._tc.get_or_add_tcPr()
            old_w = tcPr.find(qn("w:tcW"))
            if old_w is not None:
                tcPr.remove(old_w)
            tcW = OxmlElement("w:tcW")
            tcW.set(qn("w:w"), str(cm_to_dxa(col_widths_cm[ci])))
            tcW.set(qn("w:type"), "dxa")
            tcPr.append(tcW)

def style_table(tbl, col_widths_cm, header_rows=1, right_align_cols=()):
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    apply_fixed_col_widths(tbl, col_widths_cm)
    tblPr = tbl._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for side, val, sz, col in [
        ("top", "single", "8", HEX_BLACK),
        ("bottom", "single", "6", HEX_BLACK),
        ("insideH", "single", "4", HEX_BORDER),
        ("left", "none", "0", "auto"),
        ("right", "none", "0", "auto"),
        ("insideV", "none", "0", "auto"),
    ]:
        b = OxmlElement(f"w:{side}")
        b.set(qn("w:val"), val); b.set(qn("w:sz"), sz); b.set(qn("w:color"), col)
        borders.append(b)
    tblPr.append(borders)

    for ri, row in enumerate(tbl.rows):
        trPr = row._tr.get_or_add_trPr()
        trPr.append(OxmlElement("w:cantSplit"))
        is_hdr = ri < header_rows
        if is_hdr:
            trPr.append(OxmlElement("w:tblHeader"))
        for ci, cell in enumerate(row.cells):
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            set_cell_margins(cell, top=32 if not is_hdr else 44, bottom=32 if not is_hdr else 44, left=85, right=85)
            if is_hdr:
                set_cell_shading(cell, HEX_HDR)
                tcPr = cell._tc.get_or_add_tcPr()
                tcBdr = OxmlElement("w:tcBorders")
                bot = OxmlElement("w:bottom")
                bot.set(qn("w:val"), "single"); bot.set(qn("w:sz"), "8"); bot.set(qn("w:color"), HEX_BLACK)
                tcBdr.append(bot)
                tcPr.append(tcBdr)
            for p in cell.paragraphs:
                p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.space_after = Pt(0)
                p.paragraph_format.line_spacing = 1.06
                if ci in right_align_cols:
                    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
                for r in p.runs:
                    r.font.name = "Calibri"
                    r.font.size = Pt(9.3)
                    if is_hdr:
                        r.font.bold = True
                        r.font.color.rgb = C_INK
                    else:
                        r.font.color.rgb = C_BODY

def add_h1(text, page_break=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(7 if not page_break else 0)
    p.paragraph_format.space_after = Pt(3.5)
    p.paragraph_format.keep_with_next = True
    if page_break:
        p.paragraph_format.page_break_before = True
    r = p.add_run(text)
    r.font.name = "Calibri"
    r.font.size = Pt(11.5)
    r.font.bold = True
    r.font.color.rgb = C_INK
    set_p_bottom_border(p, HEX_BLACK, sz="6", space="2")
    return p

def add_h2(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(5)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = "Calibri"
    r.font.size = Pt(10.5)
    r.font.bold = True
    r.font.color.rgb = C_INK
    return p

def add_caption(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(3)
    p.paragraph_format.space_after = Pt(1.5)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = "Calibri"
    r.font.size = Pt(9.2)
    r.font.bold = True
    r.font.italic = True
    r.font.color.rgb = C_MUTED
    return p

def add_body(text, space_after=3.5):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.12
    r = p.add_run(text)
    r.font.name = "Calibri"
    r.font.size = Pt(10.0)
    r.font.color.rgb = C_BODY
    return p

def add_bullet(lead, text):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(0.55)
    p.paragraph_format.first_line_indent = Cm(-0.3)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2.0)
    p.paragraph_format.line_spacing = 1.10
    r0 = p.add_run("•  " + lead)
    r0.font.name = "Calibri"; r0.font.size = Pt(9.8); r0.font.bold = True; r0.font.color.rgb = C_INK
    r1 = p.add_run(text)
    r1.font.name = "Calibri"; r1.font.size = Pt(9.8); r1.font.color.rgb = C_BODY
    return p

def make_table(headers, rows, widths_cm, right_cols=(), bold_last_row=False, bold_first_col=True):
    tbl = doc.add_table(rows=1 + len(rows), cols=len(headers))
    for ci, h in enumerate(headers):
        tbl.rows[0].cells[ci].paragraphs[0].add_run(h)
    for ri, row_data in enumerate(rows):
        for ci, val in enumerate(row_data):
            run = tbl.rows[ri + 1].cells[ci].paragraphs[0].add_run(val)
            if (bold_first_col and ci == 0) or (bold_last_row and ri == len(rows) - 1):
                run.font.bold = True
    style_table(tbl, widths_cm, header_rows=1, right_align_cols=right_cols)
    if bold_last_row:
        for cell in tbl.rows[-1].cells:
            set_cell_shading(cell, HEX_HDR)
            for p in cell.paragraphs:
                for r in p.runs:
                    r.font.bold = True
                    r.font.color.rgb = C_INK
    return tbl

# ================= PAGE 1: EDITORIAL COVER PAGE =================
p_sp = doc.add_paragraph()
p_sp.paragraph_format.space_before = Pt(64)
p_sp.paragraph_format.space_after = Pt(0)

p_eye = doc.add_paragraph()
p_eye.paragraph_format.space_after = Pt(14)
re = p_eye.add_run("POLYU HKCC   ·   SEHS2265 E-BUSINESS   ·   INDIVIDUAL ASSIGNMENT TWO")
re.font.name = "Calibri"; re.font.size = Pt(9.5); re.font.bold = True; re.font.color.rgb = C_BRONZE

p_title = doc.add_paragraph()
p_title.paragraph_format.space_after = Pt(8)
rt = p_title.add_run("DeskMate AI")
rt.font.name = "Calibri"; rt.font.size = Pt(28); rt.font.bold = True; rt.font.color.rgb = C_INK

p_sub = doc.add_paragraph()
p_sub.paragraph_format.space_after = Pt(24)
rs = p_sub.add_run("The 24/7 Bilingual AI Receptionist for Independent Hong Kong Beauty & Hair Salons")
rs.font.name = "Calibri"; rs.font.size = Pt(12.5); rs.font.italic = True; rs.font.color.rgb = C_INK
set_p_bottom_border(p_sub, HEX_BLACK, sz="12", space="14")

p_lead = doc.add_paragraph()
p_lead.paragraph_format.space_before = Pt(10)
p_lead.paragraph_format.space_after = Pt(36)
p_lead.paragraph_format.line_spacing = 1.35
rl = p_lead.add_run(
    "This e-business start-up plan sets out DeskMate AI's B2B Fee-for-Service model, Hong Kong salon "
    "market segmentation, Customer Relationship Life Cycle communication strategy, three-tier cloud "
    "and payment architecture, Total Cost of Ownership financial plan, and live Wix Headless prototype."
)
rl.font.name = "Calibri"; rl.font.size = Pt(11); rl.font.color.rgb = C_BODY

# Editorial metadata block
meta_tbl = doc.add_table(rows=6, cols=2)
meta_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
meta_tbl.autofit = False
apply_fixed_col_widths(meta_tbl, [4.2, 13.2])
meta_rows = [
    ("Submission Title", "Assignment Two (Individual): E-Business Start-up Plan"),
    ("Student Full Name", "[Author]"),
    ("Student ID", "[Student ID]"),
    ("Subject & Lecturer", "SEHS2265 E-Business, Miss Janice Au (Semester 1, 2026/27)"),
    ("Live Wix Prototype", "HYPERLINK_PLACEHOLDER"),
    ("Submission Date", "20 November 2026"),
]
for ri, (k, v) in enumerate(meta_rows):
    c0, c1 = meta_tbl.rows[ri].cells
    c0.width = Cm(4.8); c1.width = Cm(12.5)
    set_cell_margins(c0, top=70, bottom=70, left=60, right=60)
    set_cell_margins(c1, top=70, bottom=70, left=60, right=60)
    p0 = c0.paragraphs[0]; p0.paragraph_format.space_after = Pt(0)
    rk = p0.add_run(k)
    rk.font.name = "Calibri"; rk.font.size = Pt(10.0); rk.font.bold = True; rk.font.color.rgb = C_BRONZE
    p1 = c1.paragraphs[0]; p1.paragraph_format.space_after = Pt(0)
    if v == "HYPERLINK_PLACEHOLDER":
        add_hyperlink(p1, LIVE_URL, LIVE_URL, color_hex=HEX_BRONZE, size_pt=10.0, bold=True)
    else:
        rv = p1.add_run(v)
        rv.font.name = "Calibri"; rv.font.size = Pt(10.0); rv.font.color.rgb = C_INK
        if ri in (1, 2):
            rv.font.bold = True

# Subtle horizontal rules on cover metadata table
m_bdr = OxmlElement("w:tblBorders")
for side, val, sz, col in [
    ("top", "single", "6", HEX_BRONZE),
    ("bottom", "single", "6", HEX_BRONZE),
    ("insideH", "single", "4", HEX_BORDER),
    ("left", "none", "0", "auto"),
    ("right", "none", "0", "auto"),
    ("insideV", "none", "0", "auto"),
]:
    b = OxmlElement(f"w:{side}"); b.set(qn("w:val"), val); b.set(qn("w:sz"), sz); b.set(qn("w:color"), col)
    m_bdr.append(b)
meta_tbl._tbl.tblPr.append(m_bdr)

p_cov_note = doc.add_paragraph()
p_cov_note.paragraph_format.space_before = Pt(42)
rn = p_cov_note.add_run(
    "Main body: pages 2 to 4. The cover, APA 7 references (page 5) and the appendix of live Wix "
    "prototype screenshots (page 6) are excluded."
)
rn.font.name = "Calibri"; rn.font.size = Pt(9.0); rn.font.italic = True; rn.font.color.rgb = C_MUTED

# ================= BODY PAGES (STRICTLY PAGES 2-4) =================

# 1. Executive Summary
add_h1("1. Executive Summary", page_break=True)
add_body(
    "DeskMate AI is a business-to-business (B2B) AI receptionist for small beauty and hair salons in Hong Kong. "
    "It responds to enquiries and handles bookings, rescheduling and reminders on WhatsApp, Instagram and the salon "
    "website in Cantonese and English. Salons pay a monthly fee from HK$388. At the statutory minimum wage of "
    "HK$43.10 per hour, a receptionist working four hours a day for 26 days would cost about HK$4,482 a month "
    "(Labour Department, 2026). DeskMate AI's Pro subscription costs HK$788 a month, 82% less. We aim to reach "
    "60 paying salons within 12 months and seek HK$400,000 to fund first-year development, infrastructure, "
    "marketing and maintenance."
)

# 2. Company and Idea
add_h1("2. Company and Idea")
add_h2("2.1 Business description")
add_body(
    "DeskMate AI's customers are owner-operated salons that take enquiries through messaging apps. A message can go unanswered "
    "while the owner is with a customer or after closing. DeskMate AI checks the salon's calendar, confirms or "
    "reschedules the appointment, sends reminders and hands complex enquiries to the owner with a short summary, "
    "after we configure its services, prices and hours."
)
add_body(
    "Meta Business Agent can book appointments and hand enquiries to staff (Meta, 2026). SleekFlow offers AI agents "
    "on its Pro plan, advertised from US$109 per month when billed annually (SleekFlow, n.d.). Wati offers messaging "
    "automation and an AI agent builder (Wati, n.d.). DeskMate AI focuses on Hong Kong salons: we set up a shared "
    "booking calendar across messaging and the salon website, with Cantonese and English conversations (Table 1)."
)

add_caption("Table 1. SWOT analysis")
make_table(
    ["Strengths (internal)", "Weaknesses (internal)"],
    [["Salon booking workflow, done-for-you setup for each salon, Cantonese and English replies, shared calendar",
      "New brand with a small team and a dependency on third-party messaging platforms"]],
    [8.7, 8.7],
    bold_first_col=False
)
p_gap = doc.add_paragraph(); p_gap.paragraph_format.space_before = Pt(0); p_gap.paragraph_format.space_after = Pt(2)
make_table(
    ["Opportunities (external)", "Threats (external)"],
    [["Owner-operated salons need to handle enquiries during treatments and after closing",
      "Meta's booking tools, established automation providers and changes to platform fees or rules"]],
    [8.7, 8.7],
    bold_first_col=False
)

add_h2("2.2 E-commerce model")
add_body(
    "DeskMate AI is B2B e-commerce: one business sells a service to another business online (Schneider, 2017). "
    "Our customers are salons, not consumers; consumers only talk to the AI on behalf of the salon."
)

add_h2("2.3 Revenue model")
add_body(
    "We use the Fee-for-Service revenue model, charging a predictable monthly fee based on the value of the 24/7 "
    "reception service rather than a per-booking Fee-for-Transaction commission (Schneider, 2017). Salons select "
    "one of three monthly tiers (Table 2). Each plan starts with a time-limited 14-day free trial (HK$0 due today), "
    "which is distinct from a permanent freemium tier. Owners test the bilingual booking workflow before billing "
    "begins, and we track the trial-to-paid conversion rate."
)

add_caption("Table 2. Subscription plans")
make_table(
    ["Plan", "Monthly fee", "What the salon gets"],
    [
        ["Starter", "HK$388", "One WhatsApp number, bilingual FAQ answers and booking capture, 300 conversations a month"],
        ["Pro", "HK$788", "Adds Instagram and website chat, one shared calendar, rescheduling and reminders, 1,000 conversations a month"],
        ["Premium", "HK$1,488", "Adds deposit collection, no-show follow-up, multiple branches and priority support"],
    ],
    [2.6, 2.6, 12.1]
)

add_h2("2.4 Business objectives")
add_body(
    "Our objectives support a downstream strategy, which improves the value delivered to customers, and each uses "
    "a Figure 12-1 measure so that even intangible benefits are measurable (Schneider, 2017, Chapter 12):",
    space_after=2.0
)
add_bullet("Increase sales: ", "reach 60 paying salons within 12 months, measured by active subscriptions.")
add_bullet("Enhance marketing programs: ", "convert at least 25% of completed trials into paid plans by month 12 (conversion-to-buyer rate).")
add_bullet("Serve existing customers better: ", "keep monthly cancellations below 5% of subscriptions active at the start of each month (customer loyalty).")
add_bullet("Open new markets: ", "sign 10 paying clinics or tutorial centres by month 18, measured by active subscriptions in the new segments.")

# 3. Market Analysis
add_h1("3. Market Analysis")
add_body(
    "Market segmentation divides potential customers into groups with similar characteristics so that the right "
    "product is promoted to the right group (Schneider, 2017). Because our customers are businesses, we replace "
    "personal demographic variables such as age and income with firm characteristics such as industry and size (Table 3)."
)

add_caption("Table 3. Primary target segment")
make_table(
    ["Segmentation basis", "DeskMate AI target segment"],
    [
        ["Geographic", "Hong Kong, starting with dense retail districts such as Mong Kok, Causeway Bay and Tsim Sha Tsui"],
        ["Demographic (firm)", "Beauty salons and hair salons with 1 to 10 staff and no full-time receptionist"],
        ["Psychographic", "Owner-operators who reply to customers personally, feel short of staff and already rely on WhatsApp and Instagram for bookings"],
        ["Behavioural", "Salons already booking through WhatsApp DMs with heavy evening enquiry volume; the site serves browsers (booking demo, '14-Day Free Trial' trigger words), shoppers (plan comparison, savings slider, FAQ) and buyers (direct 'Start 14-Day Trial' button)"],
    ],
    [3.8, 13.5]
)
add_body(
    "Clinics and tutorial centres are Year 2 segments; the prototype's Industries switcher gives each a dedicated "
    "virtual space (Schneider, 2017)."
)

# 4. Customer Analysis
add_h1("4. Customer Analysis")
add_body(
    "The customer relationship life cycle (CRLC) has five stages: awareness, exploration, familiarity, commitment "
    "and separation (Schneider, 2017). As a new brand with no existing customers, DeskMate AI targets awareness "
    "and exploration (Table 4)."
)

add_caption("Table 4. Communication strategy by stage")
make_table(
    ["Stage", "Salon owner's state", "Communication", "Measure"],
    [
        ["Awareness", "Has not heard of DeskMate AI",
         "Targeted Instagram and Facebook ads, SEO and paid placement. Message: informs owners that an AI receptionist for salons exists",
         "Impressions, cost per click, website visits"],
        ["Exploration", "Learns how it works and compares it with manual replies or Meta's tool",
         "Demo conversation on the website, 14-day free trial, and one-to-one contact through the 'Book a Demo' form. Message: explains how it works and encourages switching",
         "Demo requests, trial sign-ups, trial-to-paid conversion rate"],
    ],
    [2.3, 3.6, 8.0, 3.4]
)
add_body(
    "An AI receptionist is a complex B2B service, and buyer trust rises as communication shifts from mass media to "
    "the Web (many-to-one) to personal contact (one-to-one) (Schneider, 2017). We use targeted social and search ads "
    "to control acquisition cost, the interactive Wix booking demo and one-to-one Book a Demo form to lower conversion "
    "cost, and touchpoint consistency across WhatsApp, Instagram and the website to reinforce trust. After sign-up, "
    "opt-in performance reports (permission marketing, with no unsolicited commercial e-mail) lower retention cost "
    "and move salons toward familiarity (messages that convince owners to keep paying) and commitment (messages that "
    "reinforce good feelings) under Hong Kong's Personal Data (Privacy) Ordinance (PDPO) with clear opt-out."
)

# 5. Operations and Technology
add_h1("5. Operations and Technology")
add_h2("5.1 Web site usability")
add_caption("Table 5. Usability factors")
make_table(
    ["Factor", "How the DeskMate AI site applies it"],
    [
        ["Clear navigation", "Sticky header with 6 clear links (Home, How It Works, Industries, Pricing, FAQ, Contact), scroll-spy active state, and direct trial/demo CTAs (Figure A1)."],
        ["Mobile-responsive design", "Responsive at 1440×900 and 375×812, with a slide-down mobile menu and no horizontal scrolling (Figure A6)."],
        ["Fast loading time", "Hand-coded static pages (about 110 KB of HTML, CSS and JS) with salon photographs served from Wix Media CDN edge servers."],
        ["Two-way communication", "A Cantonese and English booking simulation that uses the visitor's salon name, and a validated one-to-one 'Book a Demo' form, provide two-way communication (Schneider, 2017) (Figures A2, A5)."],
        ["Accessible information", "Pricing, booking example, savings slider, Industries tabs, About facts, Latest Platform Updates and FAQ (Figures A1 to A3, A5)."],
        ["Trust", "Transparent HK$ fees, 'Sample' and 'Illustrative' labels, a 'Prototype simulation' checkout notice, opt-in updates and PDPO opt-out. Trust supports loyalty: a 5% rise in loyalty can raise profit by 25% to 80% (Schneider, 2017, Chapter 3)."],
    ],
    [4.0, 13.3]
)

add_h2("5.2 Technology infrastructure")
add_body(
    "At 60 Pro salons (up to 60,000 conversations a month, peaking in evenings), a three-tier design (client, Web "
    "server and database) on managed cloud (PaaS), with serverless functions and a Content Delivery Network (CDN), "
    "meets the six hosting criteria in Schneider (2017, Chapter 12): functionality, reliability, scalability, "
    "security, backup and cost (Table 6)."
)
add_caption("Table 6. Infrastructure choices")
make_table(
    ["Technology", "Justification for our scale"],
    [
        ["Cloud computing (PaaS)", "Cost efficiency (no servers to buy or maintain) and dynamic resource allocation as salon count scales from 1 to 60+ (Wix Headless + managed cloud)."],
        ["Serverless computing", "Pay-per-use event execution for incoming messages and checkout flows: near-zero idle cost overnight and automatic scaling during evening booking peaks."],
        ["5G mobile networks", "Low-latency 5G supports real-time replies to clients messaging from phones and instant mobile checkout; IoT and microservers are unnecessary at a 60-salon scale."],
        ["Content Delivery Network (CDN)", "Caches salon photography on edge servers (Wix Media CDN) close to Hong Kong visitors, reducing network latency and supporting fast loading."],
    ],
    [4.6, 12.7]
)

add_h2("5.3 Payment systems")
add_body(
    "Recurring monthly subscriptions use Visa and Mastercard, while Apple Pay and Google Pay provide express checkout "
    "for decisive buyers (Schneider, 2017). Hong Kong's Faster Payment System (FPS) supports prepaid annual plans "
    "(10% off) without card fees. Stripe (n.d.) notes cards and digital wallets are widely used in Hong Kong; a PCI "
    "DSS-certified gateway tokenises cards, and our Wix Headless prototype (Wix hosting + Wix Media CDN) simulates "
    "this checkout and demo form on the front end without real billing (Figure A4)."
)

# 6. Financial Plan
add_h1("6. Financial Plan")
add_body(
    "Costs are estimated with the total cost of ownership (TCO) approach, which includes maintenance and future "
    "redesign as well as initial build (Schneider, 2017, Chapter 12; Table 7)."
)
add_caption("Table 7. Year 1 cost estimate")
make_table(
    ["Category", "Items", "Year 1 (HK$)"],
    [
        ["Development", "Contract developer and designer labour: website, AI and WhatsApp/Instagram integration, booking module, testing", "180,000"],
        ["Infrastructure", "Cloud hosting, AI model usage, WhatsApp Business API fees, domain", "60,000"],
        ["Marketing", "Social and search ads, part-time onboarding staff for demo visits and trial support", "120,000"],
        ["Maintenance and redesign", "Site maintenance and a reserve for future redesign", "40,000"],
        ["Total", "", "400,000"],
    ],
    [4.0, 10.7, 2.6],
    right_cols=(2,),
    bold_last_row=True
)
add_body(
    "The HK$400,000 seed request, suited to angel investors given falling cloud start-up costs, is mostly labour, "
    "consistent with Schneider's (2017, Chapter 12) 10% hardware, 10% software and 80% labour pattern. Ongoing costs "
    "(HK$220,000) equal 122% of initial build (HK$180,000), within the 50% to 200% TCO range. Operating break-even needs "
    "24 Pro salons (HK$18,333 ÷ HK$788), reached in month 5 at five new salons a month; 60 Pro salons generate "
    "HK$47,280 a month (2.6× ongoing cost), depending on plan mix. Our main opportunity cost is the founder's forgone "
    "graduate salary (excluded from cash TCO); because ROI converts all benefits to money and favours short-term "
    "results, it understates intangible benefits such as salon loyalty (Schneider, 2017, Chapter 12).",
    space_after=0
)

# ================= PAGE 5: ALPHABETICAL APA 7 REFERENCES =================
add_h1("References", page_break=True)

def add_apa_ref(parts):
    """parts is a list of (text, is_italic, url_or_none)"""
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.5)
    p.paragraph_format.first_line_indent = Inches(-0.5)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(8)
    p.paragraph_format.line_spacing = 1.25
    for txt, ital, url in parts:
        if url:
            add_hyperlink(p, url, txt, color_hex=HEX_BRONZE, size_pt=10.0, bold=False)
        else:
            r = p.add_run(txt)
            r.font.name = "Calibri"
            r.font.size = Pt(10.0)
            r.font.italic = ital
            r.font.color.rgb = C_BODY

refs = [
    [("Labour Department. (2026). ", False, None),
     ("Statutory minimum wage: Concise guide.", True, None),
     (" ", False, None),
     ("https://www.labour.gov.hk/common/public/pdf/smw/Concise_Guide_2026_Eng.pdf", False,
      "https://www.labour.gov.hk/common/public/pdf/smw/Concise_Guide_2026_Eng.pdf")],
    [("Meta. (2026, June 3). ", False, None),
     ("Be there for every customer with Meta Business Agent.", True, None),
     (" ", False, None),
     ("https://about.fb.com/news/2026/06/meta-business-agent/", False,
      "https://about.fb.com/news/2026/06/meta-business-agent/")],
    [("Schneider, G. P. (2017). ", False, None),
     ("Electronic commerce", True, None),
     (" (12th ed.). Cengage Learning.", False, None)],
    [("SleekFlow. (n.d.). ", False, None),
     ("Pricing and plans.", True, None),
     (" ", False, None),
     ("https://sleekflow.io/en-us/pricing", False, "https://sleekflow.io/en-us/pricing")],
    [("Stripe. (n.d.). ", False, None),
     ("Payments in Hong Kong: An in-depth guide.", True, None),
     (" ", False, None),
     ("https://stripe.com/en-hk/resources/more/payments-in-hong-kong", False,
      "https://stripe.com/en-hk/resources/more/payments-in-hong-kong")],
    [("Wati. (n.d.). ", False, None),
     ("Pricing.", True, None),
     (" ", False, None),
     ("https://www.wati.io/pricing/", False, "https://www.wati.io/pricing/")],
]
for ref in refs:
    add_apa_ref(ref)

# ================= PAGE 6: APPENDIX (FRESH LIVE WIX SCREENSHOTS) =================
add_h1("Appendix: Live Wix Prototype Screenshots", page_break=True)

p_app = doc.add_paragraph()
p_app.paragraph_format.space_after = Pt(6)
ra1 = p_app.add_run("Live prototype URL: ")
ra1.font.name = "Calibri"; ra1.font.size = Pt(9.2); ra1.font.bold = True; ra1.font.color.rgb = C_INK
add_hyperlink(p_app, LIVE_URL, LIVE_URL, color_hex=HEX_BRONZE, size_pt=9.2, bold=False)
ra2 = p_app.add_run("  |  Captured directly from live Wix Headless hosting (1440×900 desktop & 375×812 mobile).")
ra2.font.name = "Calibri"; ra2.font.size = Pt(9.2); ra2.font.color.rgb = C_MUTED

def add_fig_pair(im1, cap1, im2, cap2, w1=3.15, w2=3.15, h2=None):
    tbl = doc.add_table(rows=2, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    for ci, (im, cap, w, h) in enumerate([(im1, cap1, w1, None), (im2, cap2, w2, h2)]):
        cell_i = tbl.rows[0].cells[ci]
        cell_i.width = Cm(8.65)
        set_cell_margins(cell_i, top=24, bottom=20, left=40, right=40)
        pi = cell_i.paragraphs[0]
        pi.alignment = WD_ALIGN_PARAGRAPH.CENTER
        pi.paragraph_format.space_after = Pt(0)
        if h is not None:
            pi.add_run().add_picture(str(im), height=Inches(h))
        else:
            pi.add_run().add_picture(str(im), width=Inches(w))
        cell_c = tbl.rows[1].cells[ci]
        cell_c.width = Cm(8.65)
        set_cell_margins(cell_c, top=15, bottom=50, left=40, right=40)
        pc = cell_c.paragraphs[0]
        pc.alignment = WD_ALIGN_PARAGRAPH.CENTER
        pc.paragraph_format.space_after = Pt(0)
        rc = pc.add_run(cap)
        rc.font.name = "Calibri"; rc.font.size = Pt(8.5); rc.font.italic = True; rc.font.color.rgb = C_MUTED

add_fig_pair(
    SHOTS / "wix-home.png",
    "Figure A1. Live Wix homepage with six-link navigation (desktop, 1440×900)",
    SHOTS / "wix-demo.png",
    "Figure A2. Booking simulation in a phone frame, personalised with a salon name, and the shared calendar"
)
add_fig_pair(
    SHOTS / "wix-pricing.png",
    "Figure A3. B2B Fee-for-Service plans (Starter, Pro, Premium) with a 14-day trial",
    SHOTS / "wix-checkout.png",
    "Figure A4. Simulated checkout (HK$0 today; cards, wallets and FPS)"
)
add_fig_pair(
    SHOTS / "wix-contact.png",
    "Figure A5. One-to-one demo form, About facts, opt-in checkbox and PDPO notice",
    SHOTS / "wix-mobile.png",
    "Figure A6. Mobile layout (375×812)",
    w1=3.15, w2=None, h2=2.08
)

doc.save(str(OUT_DOCX))
print("BUILT_V2_DOCX:", OUT_DOCX, OUT_DOCX.stat().st_size)
