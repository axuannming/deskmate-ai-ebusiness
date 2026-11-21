# DeskMate AI — E-Business Start-up Plan & Wix Headless Prototype

An e-business start-up project (`SEHS2265` E-Business Individual Assignment Two) proposing **DeskMate AI**, a 24/7 bilingual (Cantonese & English) AI receptionist SaaS for independent Hong Kong beauty and hair salons across WhatsApp, Instagram DM, and website chat. The deliverables include an interactive Wix Headless prototype, a business plan with a 3-page main body, and a 6-slide pitch deck.

Student identifiers and personal Wix hosting details have been redacted from the portfolio copies, including screenshots and review evidence. The checkout and contact flows in the prototype are simulations. Example email addresses use reserved domains.

## Tech Stack
- **Web Prototype (`wix-site/`):** Semantic HTML5, CSS3, Vanilla JavaScript (designed for Wix Headless + Wix Media CDN)
- **Deck & Document Pipeline (`deck-final/`):** HTML/CSS slide templates, Python (`python-docx`, `python-pptx`, `pypdf`, Playwright)
- **Deliverables (`submission/`):** 6-page Business Plan (`.docx`/`.pdf`), 6-slide Pitch Deck (`.pptx`/`.pdf`), 3-minute Presentation Script & Q&A, Audit & Taste Specs, Manual Review Guide

## Directory Structure
```text
.
├── wix-site/                         # Responsive prototype (Hero, interactive salon iPhone demo, 3-tier pricing, HK$0 checkout, PDPO opt-in form)
├── deck-final/                       # HTML slide sources, salon photography/screenshots, & Python DOCX/PPTX generators
├── submission/                       # Sanitized Business Plan, Presentation Deck, Script, Audit & Taste QA reports
├── docs/                             # Engineering handoff notes, delivery review suggestions, & QA checklist dashboard
├── .gitignore
└── README.md
```

## How to Run Locally
Open the interactive web prototype directly in any browser (or serve via a static server):
```bash
python -m http.server 8000 --directory wix-site
```
Then visit `http://localhost:8000` to test:
- Interactive Cantonese/English booking demo with custom salon name input (`#demo`)
- 3-tier monthly/annual Fee-for-Service pricing (`Starter HK$388`, `Pro HK$788`, `Premium HK$1,488`) (`#pricing`)
- Simulated `HK$0` 14-day free trial checkout flow (`#checkout`)
- 1-to-1 demo contact form with unchecked permission-marketing opt-in & HK PDPO notice (`#contact`)

## Authorship & Attribution
- Individual coursework project (`SEHS2265` E-Business).

## Development Difficulties, AI Prompting & Solutions
Summarized directly from `docs/HANDOFF.md`, `docs/DeskMate_交付修改建議.md`, `submission/Audit_Report_Opus55.md`, `submission/Taste_Spec_Opus55.md`, and `deck-final/polish-log.md`:
1. **Wix Native Checkout Constraints vs. Simulated Front-End Flow:**
   - *Difficulty:* Separate Wix site publication attempts failed or triggered automated review blocks, and the free Wix Harmony plan lacked native checkout flows without activating real payments (`HANDOFF.md`).
   - *Solution:* Built an interactive custom front-end simulation inside `wix-site/` (`HK$0` today, 14-day trial, Visa/Mastercard/Apple Pay/Google Pay/FPS options) and explicitly disclosed its simulated nature across the UI, business plan, and Q&A (`DeskMate_交付修改建議.md`).
2. **Enforcing Strict Page Budgets & Cross-Deliverable Consistency:**
   - *Difficulty:* Maintaining a strict 3-page business plan body (`pp. 2–4`) without orphaned table rows alongside synchronized pricing/cost benchmarks (`82%` comparison vs. HK$4,482 part-time benchmark, `24` Pro salons break-even, `HK$400k` TCO) across the website, PDF, and 6-slide PPTX (`DeskMate_交付修改建議.md`, `Audit_Report_Opus55.md`).
   - *Solution:* Automated DOCX/PPTX generation (`deck-final/*.py`) paired with a multi-gate Taste & Humanizer QA rubric (`T1–T15` in `Taste_Spec_Opus55.md` and `docs/review-dashboard.html`) verifying typography, mobile (`375px`) vs. desktop (`1440px`) layout, XSS-safe `textContent` rendering, and zero AI cliché phrasing.
