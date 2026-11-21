import base64, io, json, re
from pathlib import Path
from PIL import Image

GUIDE = Path(r"./submission\Manual_Review_Guide.html")
BP_DIR = Path(r"./deck-final\bp-verify")
SLIDE_DIR = Path(r"./deck-final\pptx-verify")
WIX_DIR = Path(r"./submission\wix-screenshots")
SCRIPT_MD = Path(r"./submission\Presentation_Script.md")

def to_data_uri(path: Path, max_w=1280, quality=82):
    im = Image.open(path).convert("RGB")
    if im.width > max_w:
        h = int(im.height * max_w / im.width)
        im = im.resize((max_w, h), Image.Resampling.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, format="JPEG", quality=quality, optimize=True)
    b64 = base64.b64encode(buf.getvalue()).decode("ascii")
    return f"data:image/jpeg;base64,{b64}"

bp_pages = [
    {"title": "第 1 頁：封面（姓名、學號與可點擊 Live Wix 連結）", "src": to_data_uri(BP_DIR / "page-1.png", 1100, 82)},
    {"title": "第 2 頁：正文 1/3（Executive Summary、SWOT、B2B、Fee-for-Service、Objectives）", "src": to_data_uri(BP_DIR / "page-2.png", 1100, 82)},
    {"title": "第 3 頁：正文 2/3（Market Segmentation、CRLC 溝通策略、Website Usability）", "src": to_data_uri(BP_DIR / "page-3.png", 1100, 82)},
    {"title": "第 4 頁：正文 3/3（Three-Tier Cloud/CDN/5G、Payment Systems、TCO 財務計畫）", "src": to_data_uri(BP_DIR / "page-4.png", 1100, 82)},
    {"title": "第 5 頁：APA 7 參考文獻（嚴格字母排序＋0.5 吋懸掛縮排）", "src": to_data_uri(BP_DIR / "page-5.png", 1100, 82)},
    {"title": "第 6 頁：附錄（Live Wix 原型實景截圖 Figures A1–A6）", "src": to_data_uri(BP_DIR / "page-6.png", 1100, 82)},
]

slides = [
    {"title": "Slide 1：封面與備援 Live Wix 網址", "src": to_data_uri(SLIDE_DIR / "slide-1.png", 1280, 82)},
    {"title": "Slide 2：痛點與 B2B Fee-for-Service（省 82%、14 天試用 ≠ freemium）", "src": to_data_uri(SLIDE_DIR / "slide-2.png", 1280, 82)},
    {"title": "Slide 3：市場定位與 CRLC 5 階段（Target: Awareness & Exploration；Stage 5: Separation）", "src": to_data_uri(SLIDE_DIR / "slide-3.png", 1280, 82)},
    {"title": "Slide 4：三管道合一、Three-Tier PaaS/Serverless/CDN/5G 與香港支付", "src": to_data_uri(SLIDE_DIR / "slide-4.png", 1280, 82)},
    {"title": "Slide 5：Live Wix 1 分鐘示範頁（含 6 個可點擊熱區：Home / Demo / Plans / Checkout / Contact）", "src": to_data_uri(SLIDE_DIR / "slide-5.png", 1280, 82)},
    {"title": "Slide 6：Year 1 HK$400k 種子募資、TCO 122%、10/10/80 與 24 店損益兩平", "src": to_data_uri(SLIDE_DIR / "slide-6.png", 1280, 82)},
]

wix_shots = [
    {"title": "Wix 1/6：桌機首頁與 6 連結清楚導覽（1440×900）", "src": to_data_uri(WIX_DIR / "wix-home.png", 1200, 80)},
    {"title": "Wix 2/6：iPhone 實機框自訂沙龍名廣東話／英文預約模擬與共享行事曆", "src": to_data_uri(WIX_DIR / "wix-demo.png", 1200, 80)},
    {"title": "Wix 3/6：B2B Fee-for-Service 三層方案（Starter / Pro / Premium）", "src": to_data_uri(WIX_DIR / "wix-pricing.png", 1200, 80)},
    {"title": "Wix 4/6：模擬 HK$0 14 天試用結帳（卡片 / 電子錢包 / FPS 年繳 9 折）", "src": to_data_uri(WIX_DIR / "wix-checkout.png", 1200, 80)},
    {"title": "Wix 5/6：一對一預約表單＋About 組織資訊＋Latest Updates＋Opt-in 與 PDPO", "src": to_data_uri(WIX_DIR / "wix-contact.png", 1200, 80)},
    {"title": "Wix 6/6：手機響應式版面（375×812，零水平捲動）", "src": to_data_uri(WIX_DIR / "wix-mobile.png", 600, 82)},
]

viewer_block = f'''const VIEWER_DATA = {{
    bp: {{
      eyebrow: 'DELIVERABLE 1 · BUSINESS PLAN PDF (40%)',
      path: './submission/Business_Plan_Updated.pdf',
      extUrl: '',
      items: {json.dumps(bp_pages, ensure_ascii=False)}
    }},
    slides: {{
      eyebrow: 'DELIVERABLE 2 · 6-SLIDE PRESENTATION PPTX (20%)',
      path: './submission/DeskMate_AI_Presentation.pptx',
      extUrl: '',
      items: {json.dumps(slides, ensure_ascii=False)}
    }},
    wix: {{
      eyebrow: 'DELIVERABLE 3 · LIVE WIX HEADLESS PROTOTYPE (40%)',
      path: 'https://deskmate-ai-demo.example.com',
      extUrl: 'https://deskmate-ai-demo.example.com/#checkout',
      items: {json.dumps(wix_shots, ensure_ascii=False)}
    }}
  }};'''

html = GUIDE.read_text(encoding="utf-8")

# 1. Refresh VIEWER_DATA cleanly (idempotent)
pattern_vd = re.compile(r'const VIEWER_DATA = \{.*?\n  \};', re.S)
assert pattern_vd.search(html), "Could not find VIEWER_DATA block in Manual_Review_Guide.html"
html = pattern_vd.sub(lambda _: viewer_block, html, count=1)

# 2. Sync Section 5 script prompt cards and word count from Presentation_Script.md
if SCRIPT_MD.exists():
    script_text = SCRIPT_MD.read_text(encoding="utf-8")
    rows = re.findall(r'^\| [1-6] [^|]+\| [^|]+\| ([^|]+) \|$', script_text, re.M)
    if len(rows) == 6:
        counts = [len(r.strip().split()) for r in rows]
        total_w = sum(counts)
        non_demo_w = total_w - counts[4]
        demo_w = counts[4]
        html = re.sub(
            r'<div class="sec-note">全文共 \d+ 字（[^<]+</div>',
            f'<div class="sec-note">全文共 {total_w} 字（非 Demo {non_demo_w} 字 ≈ 2 分鐘＋Live Demo {demo_w} 字與操作 ≈ 1 分鐘），與 PPTX 備忘稿 100% 同步。</div>',
            html,
            count=1,
        )
        en_divs = list(re.finditer(r'<div class="sr-en">.*?</div>', html, re.S))
        if len(en_divs) == 6:
            # Replace in reverse order to preserve offsets
            for m, new_en in reversed(list(zip(en_divs, rows))):
                html = html[:m.start()] + f'<div class="sr-en">{new_en.strip()}</div>' + html[m.end():]
        html = re.sub(
            r'(<div class="sr-zh">)操作順序：[^<]+(</div>)',
            r'\1操作順序：點 Home → Booking Example（#demo 輸入自訂沙龍名展示 iPhone 廣東話 Gel 甲模擬＋日曆鎖定）→ Pricing/Checkout（點 Pro 顯示 HK$0 模擬結帳）→ Book a Demo（#contact 展示一對一表單＋未勾選 opt-in＋PDPO）。\2',
            html,
            count=1,
        )

GUIDE.write_text(html, encoding="utf-8")
print("EMBEDDED_GUIDE_OK:", GUIDE, GUIDE.stat().st_size, "bytes")
