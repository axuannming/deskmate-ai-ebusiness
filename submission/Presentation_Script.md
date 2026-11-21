# 3 分鐘 Presentation 講稿（純講稿 376 字（不含時間標籤））

> 英文講稿與 PPTX 生成腳本中的 6 頁講者備忘稿（Speaker Notes）逐字同步。非 demo 段落共 281 字（120 秒 ≈ 140 wpm），第 5 頁保留 60 秒進行 Wix Headless 實機點擊示範（95 字）。

| 頁 | 時間 | 英文講稿（同步至 PPTX Speaker Notes） |
|---|---|---|
| 1 Title | 0:00–0:10 | Good morning. DeskMate AI is a bilingual AI receptionist that answers WhatsApp, Instagram and website enquiries for small Hong Kong beauty salons. |
| 2 Problem & Model | 0:10–0:40 | Salons with one to ten staff rarely have a receptionist, so enquiries are missed during treatments and after closing. At minimum wage, four hours of reception a day costs about 4,482 Hong Kong dollars a month; our Pro plan costs 788, which is 82% less. This is B2B e-commerce on a Fee-for-Service model. Salons pay a predictable monthly fee with no per-booking commission, and the 14-day trial is time limited, so it is not a freemium tier. |
| 3 Market & CRLC | 0:40–1:05 | We target owner-run salons in Mong Kok, Causeway Bay and Tsim Sha Tsui. As a new brand, we focus on the awareness and exploration stages of the customer relationship life cycle: social and search ads inform owners, then the web demo, the trial and a one-to-one demo explain the product. Our targets are 25% trial-to-paid conversion and under 5% monthly churn. |
| 4 Operations & Tech | 1:05–1:30 | All three channels feed one booking engine and one shared calendar. It runs on a three-tier design with managed cloud and serverless functions, so we pay per use and scale for evening peaks, while a CDN keeps pages fast on mobile. Salons pay by recurring card, Apple Pay or Google Pay, or FPS for annual invoices. |
| 5 Prototype Demo | 1:30–2:30 | Here is the live Wix prototype. The navigation is clear and the layout works on mobile. In the booking demo, I type a salon name, Lumière Nail Studio. A client asks in mixed Cantonese and English for a six-thirty gel manicure. DeskMate AI replies in that salon's name and then confirms it on the shared calendar. On Pricing, each plan starts with a 14-day trial; I'll choose Pro, and the simulated checkout shows HK$0 due today. Finally, the Book a Demo form is our one-to-one touchpoint, with an unticked opt-in box and a PDPO notice. |
| 6 Financials & Ask | 2:30–3:00 | We are asking for 400,000 Hong Kong dollars in angel or seed funding, estimated with total cost of ownership. Ongoing costs are 122% of the initial build, inside the textbook's 50 to 200% range. We cover monthly operating costs at 24 Pro salons and aim for 60 by month twelve, or 47,280 dollars a month if all choose Pro. Thank you. |

## Live Wix Demo 點擊路徑（Slide 5 熱區皆可直接點擊）

- **Live URL**：`https://deskmate-ai-demo.example.com`
- **60 秒實機操作步驟**：
  1. 點 **Step 1 Open Wix Home**（`/`）→ 展示清晰 6 欄導覽與極簡首屏；
  2. 點 **Step 2 Booking Example**（`/#demo`）→ 輸入沙龍名（或點預設店名），展示 WhatsApp 中英夾雜提問、帶店名的廣東話回覆和行事曆確認 18:30。再點 **Instagram** 渠道及 **English** 語言分頁，展示英文回覆；
  3. 點 **Step 3 Plans**（`/#pricing`）→ 展示 Starter / Pro / Premium 三個月費方案，點擊 Pro 的 **Start Pro 14-day trial**（或直接點 Slide 5 的 **Checkout** 熱區 `/#checkout`）→ 按 **Activate 14-day free trial · HK$0 today** 展示 HK$0 模擬確認畫面；
  4. 點 **Step 4 Book a Demo Form**（`/#contact`）→ 展示一對一聯絡表單、未預勾的 Permission Marketing opt-in 勾選框與香港 PDPO 隱私聲明。

## Q&A 預備回答（緊扣 Schneider, 2017 課本概念）

**1. Meta Business Agent can already take bookings. Why would a salon pay for DeskMate AI?**
Meta's tool centres on WhatsApp and the merchant configures it. Meta's announcement does not say whether it is set up for Cantonese salon bookings in Hong Kong. We configure each salon's exact services, prices and opening hours during onboarding, keep one shared calendar across WhatsApp, Instagram and the salon website, and handle Cantonese and English enquiries.

**2. Your prototype uses simulated chat, checkout and form on Wix Headless. Why not live billing?**
As noted in the assignment, a prototype demonstrates the concept without live payment processing. Our site is hosted on Wix Headless using Wix hosting and Wix Media CDN, and our interactive booking simulator, HK$0 simulated checkout and one-to-one demo form show the whole workflow on a free Wix plan without real billing. The production AI engine would be built on managed cloud language models, which is why development is our largest TCO cost item.

**3. Why Fee-for-Service and not Fee-for-Transaction, and isn't a 14-day trial "freemium"?**
A fixed monthly Fee-for-Service subscription is predictable for small salons and does not penalise them for taking more bookings. Our 14-day free trial is a time-limited Exploration-stage onboarding pathway measured by trial-to-paid conversion (25% target), distinct from a permanent "free for many, fee for a few" freemium tier (Schneider, 2017).

**4. Why did you not use IoT or microservers?**
At a 60-salon scale (up to 60,000 monthly conversations peaking in evenings), managed cloud (PaaS), serverless functions and a CDN satisfy Schneider's six hosting criteria with pay-per-use efficiency and dynamic scaling. Physical IoT sensors and microservers are unnecessary overhead for a messaging-first SaaS workflow.

**5. How did you estimate the costs, and when do you break even?**
Using Schneider's Total Cost of Ownership (TCO) framework covering contract development/design labour, cloud infrastructure, marketing/onboarding staff, plus site maintenance and a future redesign reserve. Ongoing costs (HK$220,000) are 122% of initial development (HK$180,000), inside the textbook's 50% to 200% range, and primarily labour-driven (consistent with the 10/10/80 pattern). Monthly operating break-even is 24 Pro salons (~Month 5 at 5 new salons/month). On a linear ramp from 5 to 60 salons (390 salon-months × HK$788 ≈ HK$307k Year 1 revenue), Year 1 still needs the HK$400,000 angel/seed runway to fund initial build and ramp-up.

**6. What happens if Meta changes its WhatsApp policy or fees?**
It is the main external threat in our SWOT analysis. We mitigate single-platform dependence by integrating Instagram DM and the salon's own website chat into the same shared calendar.
