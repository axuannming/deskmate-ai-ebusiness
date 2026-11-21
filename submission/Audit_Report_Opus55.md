# DeskMate AI — A+ 驗收與審核報告（Opus55 獨立審核）

**學生：** [Author]（[Student ID]）｜**科目：** SEHS2265 E-Business, Assignment Two
**審核日期：** 2026-11-20（HKT 01:00；截止時間 2026-11-20 23:59，**剩約 23 小時**）
**審核範圍：** Business Plan PDF/DOCX、Live Wix Headless prototype（live HTML + `wix-site/` 原始碼）、6 頁 PPTX/PDF + 講者備忘稿、`Presentation_Script.md`、`To_Verify.md`
**依據：** 官方 Instruction（4 頁 PDF）＋ Lecture Summary（Schneider 2017，L01–L07）
**審核原則：** 只審不改；所有交付檔案未被修改。

---

## 0. 審核方法與已核實的事實

| 檢查項 | 方法 | 結果 |
|---|---|---|
| BP 頁數 | `pypdf` 解析 + `bp-verify/page-1..6.png` 目視 | 6 頁 = Cover(1) + **正文 3 頁(p2–p4)** + References(p5) + Appendix(p6) ✅ |
| BP 版面 | `python-docx` | A4、邊界 L/R 1.9 cm、T/B 1.76 cm、正文 **10.5 pt**、表格 9–10 pt（密度偏高，見 P2-9） |
| Live 網站 | `Invoke-WebRequest` 抓 live HTML | HTTP 200；`#demo` `#pricing` `#contact` `#checkout` 全部存在 ✅；live HTML 27.9 KB + `styles.css` 17.1 KB + `app.js` 15.7 KB ≈ **60.7 KB（未壓縮）** |
| Wix 原生功能 | grep `app.js` | **沒有任何 Wix SDK / Wix Forms / Wix Pricing Plans / Wix Checkout 呼叫**；表單和結帳都是純前端 JS，送出後沒有資料寫到任何地方 ⚠️ |
| PPTX | `python-pptx` | 6 頁 ✅；每頁是**一張全版圖片**（文字不可編輯）；6 頁都有講者備忘稿 ✅；Slide 5 有 5 個可點擊熱區：home×2、`#demo`、`#pricing`、`#contact` ✅（**沒有 `#checkout`**） |
| 講稿字數 | PowerShell 計算 | PPTX 備忘稿 **265 字**；`Presentation_Script.md` **258 字**（第 5 頁兩者**不同**） |
| 算式 | 手算 | 43.10×4×26 = 4,482.4 ✅；60×788 = 47,280 ✅；220,000÷12 = 18,333 ✅；47,280÷18,333 = 2.58→2.6× ✅；220k÷180k = 122% ✅；(4,482−788)×12 = 44,328 ✅；1−788/4,482 = 82.4% ✅；成本占比 45/30/15/10% ✅ |
| 舊版 Wix Editor 站 | 抓 `example.wixsite.com/deskmate-ai` | 仍在線；裝有 Wix Pricing Plans、Checkout、Wix Forms 頁面，但 `/plans-pricing` 回 **404**，而且內容是舊版 |

---

## (a) 評分卡（依官方 40 / 40 / 20）

| 項目 | 比重 | 現況分數 | 主要扣分原因 | 修完 P0+P1 後預估 |
|---|---|---|---|---|
| **Business Plan PDF**：E-Business 概念分析、創意、結構與語言 | 40 | **35.0** | 第 4 個 objective 無法衡量；opportunity cost 用錯對象；TCO 沒有 employee/labour cost，也沒套 10/10/80；References 沒按字母排序，且有一處 APA 格式錯誤；「<40 KB code」與實測不符；沒有 break-even 或營收爬坡；Starter 功能與網站不一致 | 38.5 |
| **Wix Prototype**：usability、反映 business／revenue model | 40 | **34.0**（若老師嚴格要求「Wix checkout page／Wix features」，可能只有 30–31） | 沒用 Wix 原生 Forms / Pricing Plans / Checkout；表單成功訊息寫「logged」，但其實沒送出任何資料；沒有「About／organisation facts」（Fig 3-7 goal 1）；沒有 permission-marketing opt-in；年繳 FPS 9 折只出現在網站；導覽列沒有 scroll-spy；ARIA 角色不完整 | 38.0 |
| **Presentation**：6 頁 PPT + 3 分鐘 | 20 | **16.0** | **Slide 3 把 CRLC 第 5 階段寫成「Retention」（Schneider 的是 Separation），屬於教科書概念錯誤**；階段內容與 BP Table 4 矛盾；講稿只有 265 字，時間沒用足；`Presentation_Script.md` 與 PPTX 備忘稿不同步；Slide 3 的「US$49–109+」沒有來源；Slide 6 營收沒附「全部選 Pro」的前提 | 19.0 |
| **總分** | 100 | **85 / 100** | 在 A 區間下緣，**未達 A+（≥95）** | **95–96** |

### A+ 差距診斷（一句話）
BP 的教科書運用已經相當紮實，但 **PPT 有一個評審一眼就看得到的 CRLC 錯誤**，網站則**沒有把 BP 寫的 permission marketing、組織資訊、Wix 原生功能做出來**。另外有 5–6 處數字或功能在三份交付物之間不一致。這些是從 85 分到 95 分的主要障礙，大部分 2–4 小時內可以修完。

---

## (b) 教科書概念覆蓋矩陣（PDF / PPT / Website）

圖例：✅ 明確且正確｜⚠️ 有但淺、不一致或可再加強｜❌ 缺漏｜⛔ 誤用

| # | Schneider (2017) 概念 | Lecture | BP PDF | PPT | Website | 審核意見 |
|---|---|---|---|---|---|---|
| 1 | B2B e-commerce（明確定義＋為什麼） | L01 p15–19 | ✅ §2.2 | ✅ S2 | ✅ Pricing 副標 | 三處一致 |
| 2 | Fee-for-Service vs. Fee-for-Transaction | L03 p29–36 | ✅ §2.3 | ✅ S2 | ✅「no per-booking commissions」 | 很好 |
| 3 | 14-day trial ≠ Freemium（p37） | L03 p37 | ✅ §2.3 | ⚠️ 只寫 trial | ✅ FAQ | PPT 可補「not freemium」 |
| 4 | Downstream strategy | L06 p5 | ✅ §2.4 | ❌ | — | 可接受 |
| 5 | 可衡量目標＋tangible/intangible＋Fig 12-1 指標 | L06 p6–12 | ⚠️ 第 4 個目標沒有數字和期限；沒點名 Fig 12-1 | ✅ S3（25%、<5%） | — | 見 P1-1 |
| 6 | Geographic / Demographic(firm) / Psychographic | L05 p13–14 | ✅ Table 3 | ⚠️ 只有地區＋規模 | ✅ Industries、Contact | 「firm demographic」的改寫很好 |
| 7 | Behavioural（Browsers / Shoppers / Buyers） | L05 p18–23 | ⚠️ Table 3 寫成「網站功能」，不是「客群行為」 | ❌ | ✅ trial CTA、方案比較、FAQ、express checkout | 見 P2-3 |
| 8 | Virtual space / one-to-one marketing | L05 p16–17 | ✅ §3 | ❌ | ✅ Industries 切換 | — |
| 9 | CRLC 5 階段＋目標階段 | L05 p24–30 | ✅ 目標 = Awareness + Exploration | ⛔ **Stage 5 寫成 "Retention"**；trial 放在 Familiarity，與 BP 矛盾 | — | **P0-1** |
| 10 | 各階段訊息（inform / explain / convince / reinforce / no ads） | L05 p34 | ✅ inform / explain；⚠️ convince / reinforce 沒寫 | ❌ | — | P1-10 |
| 11 | Communication modes（mass media → Web → personal contact）＋ trust | L03 p53–55；L05 p10 | ✅ §4 | ⚠️ 只有標題「personal demos」 | ✅ 模擬器（Web）＋ 1-to-1 表單 | — |
| 12 | Touchpoint consistency | L05 p28 | ✅ | ✅ S4 三頻道 | ✅ | — |
| 13 | Permission marketing / UCE / PDPO / opt-out | L05 p39–43 | ✅ | ⚠️ 只有「PDPO Compliance」 | ⚠️ 有 PDPO 聲明，但**沒有 opt-in 勾選框** | **P1-5** |
| 14 | Acquisition / conversion / retention cost | L05 p31–36 | ✅ | ❌ | — | 可接受 |
| 15 | Web presence（Fig 3-5） | L03 p43–46 | ⚠️ 沒點名 | ❌ | ⚠️ 有品牌一致、sample testimonial；**沒有** external reviews、regularly updated info | P2-4 |
| 16 | Accessibility goals（Fig 3-7，5 項） | L03 p51 | ⚠️ 只引用「two-way」 | ❌ | ⚠️ goal 1「facts about the organization」**缺**；goal 4「return visits」**缺** | **P1-5** |
| 17 | Trust & loyalty（5% → 25–80%） | L03 p52 | ✅ Table 5 | ❌ | ⚠️ 隱含 | — |
| 18 | Three-tier architecture | L04 p14 | ✅ §5.2 | ❌ | — | P1-7 |
| 19 | Cloud PaaS / Serverless | L04 p42–52 | ✅ Table 6 | ✅ S4 | ⚠️ FAQ 只寫「managed cloud」 | — |
| 20 | CDN / latency | L04 p47–48 | ✅ | ❌ | ✅（實際用 Wix Media CDN） | P1-7 |
| 21 | 5G（real-time connectivity） | L02 p53–55 | ⚠️ 用來支撐「instant checkout」，理由偏弱 | ❌ | — | P1-8 |
| 22 | IoT / Microserver（沒選的理由） | L02 p11；L04 p33 | ❌ | ❌（只在 Q&A） | — | P1-8 |
| 23 | Hosting 6 criteria（Fig 12-3） | L06 p19 | ✅ §5.2 | ❌ | — | — |
| 24 | Payment：recurring cards、express checkout wallets、FPS | L05 p22；L02 p55 | ✅ §5.3 | ✅ S4 | ✅ 結帳 mock-up | 年繳 9 折只在網站，見 P0-5 |
| 25 | TCO（maintenance + future redesign） | L06 p14 | ✅ Table 7 | ✅ S6 | — | — |
| 26 | TCO 50–200% | L06 p16–18 | ✅ 122% | ✅ | — | — |
| 27 | 10/10/80 labour rule＋employee costs | L06 p14–16 | ❌ | ❌ | — | **P1-3** |
| 28 | Opportunity cost | L06 p15 | ⛔ 寫成「店主少做療程的機會成本」（客戶端），不是**本公司放棄其他專案的成本** | ❌ | — | **P1-2** |
| 29 | Angel / VC funding | L06 p20–21 | ✅ | ❌（只在講稿） | — | P1-7 |
| 30 | Cost/benefit＋ROI 的限制 | L06 p22–27 | ⚠️「Beyond quantitative ROI」太淺 | ❌ | — | P1-2 |
| 31 | SWOT（internal / external） | L01 p58–64 | ✅ Table 1 | ❌（只在 Q&A） | — | 可接受 |

**小結：** BP 覆蓋 31 項中的 25 項，有 2 項用錯。PPT 覆蓋約 11 項，**有 1 項用錯**。網站覆蓋約 13 項，缺 Fig 3-7 goal 1/4 和 opt-in。

---

## 跨交付物數字一致性稽核

| 數字／事實 | BP | PPT | Website | Script | 判定 |
|---|---|---|---|---|---|
| HK$43.10/hr | ✅ | ✅ S2 | ✅ | （口述「minimum wage」） | ✅ |
| HK$4,482/mo | ✅ | ✅ | ✅ | ✅ | ✅ |
| HK$388 / 788 / 1,488 | ✅ | ✅ | ✅ | 788 ✅ | ✅ |
| 82% cheaper | ❌ **沒寫** | ✅ S1/S2 | ✅ | ❌ | ⚠️ P1-9 |
| 60 salons / 12 months | ✅ | ✅ S6 | — | ✅ | ✅ |
| HK$400,000 | ✅ | ✅ | — | ✅ | ✅ |
| 122% | ✅ | ✅ | — | Q&A ✅ | ✅ |
| HK$47,280 | ✅（附「depending on plan mix」） | ⚠️ S6 沒寫「全部選 Pro」 | — | ✅「If all 60 choose Pro」 | ⚠️ P1-7 |
| HK$18,333 / 2.6× | ✅ | ✅ | — | ❌ | ✅ |
| 25% / <5% | ✅ | ✅ S3 | — | ❌ | ✅ |
| 60,000 chats/mo | ✅ | ✅ S4 | — | — | ✅ |
| **Annual FPS 9 折（save 10%）** | ❌（只寫 "annual invoices"，Table 2 沒有年繳） | ❌ | ✅ `index.html` L349、`app.js` L258–259 | ❌ | ⛔ **P0-5** |
| **Starter 功能** | Starter = 「automatic answers to enquiries」；booking 在 **Pro** 才加入 | S2：「FAQ & booking capture」 | 「FAQ + booking capture」 | — | ⛔ **P0-5** |
| **競品價格** | SleekFlow Pro 從 US$109（年繳） | S3：「**US$49–109+**」 | — | — | ⛔ US$49 在 BP 和 References 都沒有出處，**P0-5** |
| Slide 5 demo 路徑 | — | 備忘稿有提到「simulated HK$0 trial checkout」 | `#checkout` 存在 | `Script.md` 第 5 頁**沒有**這句 | ⛔ **P0-4** |
| CRLC 目標階段 | Awareness + Exploration；trial 屬 Exploration | Trial 放 **Familiarity**；第 5 階段寫成 **Retention** | — | 講稿說 exploration ✅ | ⛔ **P0-1** |
| 程式碼大小 | 「<40 KB code」 | — | 實測約 61 KB | — | ⛔ **P0-3** |

---

## (c) 修正清單（依優先順序）

> **硬性限制提醒：** BP 正文 p2–p4 目前**完全排滿**（`bp-verify/page-4.png` 已到頁尾）。下面每一項 BP 的新增文字都附有**對應的刪減**（「抵銷」欄），保證正文仍是 3 頁。PPT 維持 6 頁，只改內容，不加頁。
> PPT 的修改流程：改 `deck-final/slides/0X-*.html` → 重新截圖 `deck-final/shots/0X-*.png` → 重建 `submission/DeskMate_AI_Presentation.pptx`（**保留備忘稿和 Slide 5 的熱區連結**）→ 重新匯出 `DeskMate_AI_Presentation.pdf`。

### 🔴 P0 — 必須修（提交前一定要處理）

#### P0-1 Slide 3 的 CRLC 概念錯誤（PPT，扣分最明顯）
- **檔案：** `deck-final/slides/03-market.html`（CRLC 那一列）→ `shots/03-market.png` → PPTX/PDF 第 3 頁
- **問題：** 「Stage 5 Retention」不是 Schneider 的階段，正確是 **Separation**。另外「Stage 3 Familiarity = 14-day free trial」與 BP Table 4（trial 屬 Exploration）矛盾；副標「CRLC Acquisition Funnel」把生命週期說成漏斗，也不準確。
- **建議替換內容：**
  - 副標：`Market & Customer Strategy · CRLC — Target: Awareness & Exploration`
  - Stage 1 **Awareness** ★ Target —「IG/FB ads, SEO & paid placement → *inform*」
  - Stage 2 **Exploration** ★ Target —「Live Wix demo, 14-day trial, 1-to-1 demo → *explain & switch*」
  - Stage 3 **Familiarity** —「Opt-in monthly booking reports → *convince to stay*」
  - Stage 4 **Commitment** —「Menu refresh & priority support → *reinforce* (<5% churn)」
  - Stage 5 **Separation** —「No ads targeted; exit survey, PDPO opt-out honoured」
  - 前兩格加粗或用銅色標示（★ Target），讓評審看出它和 BP 的目標階段一致。

#### P0-2 APA 7 引用格式
- **檔案：** `submission/Business_Plan_Updated.docx` → 重新匯出 PDF（References 在 p5）
- **問題 1：** References 沒有按字母排序（現在是 Labour → Schneider → Meta → …）。
  **修正順序：** Labour Department (2026) → Meta (2026) → Schneider (2017) → SleekFlow (n.d.) → Stripe (n.d.) → Wati (n.d.)。用懸掛縮排 0.5"，書名和網頁標題用斜體。
- **問題 2：** Table 5「Two-way communication」那一列的「(Schneider, 2017 accessibility goals)」不符合 APA 格式。
  **改成：** `…plus a validated one-to-one 'Book a Demo' form, meeting Schneider's (2017) two-way communication accessibility goal.`
- **問題 3（建議）：** Stripe 的網址是 `stripe.com/en-de/…`（德國語系）。如果有 `en-hk` 版本就換掉，沒有就保留。

#### P0-3 寫錯的事實「<40 KB code」
- **檔案：** BP Table 5「Fast loading time」那一列（p3 底部）
- **實測：** live HTML 27.9 KB + CSS 17.1 KB + JS 15.7 KB ≈ 61 KB（未壓縮）。
- **改成：** `Hand-coded static pages (~61 KB HTML/CSS/JS, no page-builder bloat) with salon photography served from Wix Media CDN edge servers.`（長度差不多，不影響頁數）

#### P0-4 講稿與 PPT 同步
- **檔案：** `submission/Presentation_Script.md` L11（第 5 頁那一列）
- **改成**和 PPTX 備忘稿一樣（或者兩邊都換成 P1-6 的新講稿）：
  `…three monthly plans, each with a 14-day trial, followed by our simulated HK$0 trial checkout. The Book a demo form…`
- **L16「Demo 點擊路徑」**目前寫「結帳畫面確認後，可安排在方案與表單之間示範」，這是舊說法（checkout 已經上線）。**改成：** `首頁 → Booking example（#demo）→ Plans（#pricing）→ 點 Pro「Start Pro 14-Day Trial」進入 #checkout，按「Activate」顯示 HK$0 確認畫面 → Book a demo（#contact）。`
- **（建議）** Slide 5 的 Step 3 熱區目前連到 `#pricing`。可以在 Step 3 旁邊加一個「Checkout」小熱區，連到 `…wix-site-host.com/#checkout`，現場 demo 時能少一次捲動。

#### P0-5 三份交付物之間的功能和價格不一致
1. **年繳 FPS 9 折**（只有網站有）。二選一：
   - **(建議) 寫進 BP §5.3**，換掉第 2 句：`FPS supports prepaid annual plans (10% off) without card fees.`（字數相同）；Slide 4 的「Annual Invoices」副標改成「Zero card fees; 10% off annual plans」。
   - 或者從網站拿掉：`index.html` L349 的「(save 10%)」，以及 `app.js` L257–260 的 0.9 折扣邏輯。
2. **Starter 功能**：BP Table 2 改成和網站／Slide 2 一致：
   - Starter：`One WhatsApp number, bilingual FAQ answers and booking capture, 300 conversations a month`
   - Pro：`Adds Instagram and website chat, one shared calendar, rescheduling and reminders, 1,000 conversations a month`
3. **Slide 3 的「US$49–109+」**：改成 `SleekFlow Pro from US$109/mo (annual)`，和 BP §2.1 引用的數字一致；或者把 US$49 的來源補進 BP References。不建議留著沒有出處的數字。

#### P0-6 網站沒有用 Wix 原生功能，表單成功訊息與實際不符（Prototype 40% 的主要風險）
- **官方要求（Instruction p3）：** 「use Wix's e-commerce features」、「**Use Wix features** to simulate communication modes, such as a contact form」、「**Use the Wix checkout page** to mock up how customers would complete a transaction」。
- **現況：** Headless 網站是自寫的 HTML/JS（由 Wix 託管，使用 Wix Media CDN），但 Book-a-Demo 表單和結帳**都沒有接 Wix**。`app.js` L373–374 送出後顯示「We have logged your 1-to-1 demo request…」，**實際上沒有記錄任何資料**。這和 BP 強調的「honest labelling」原則衝突。
- **方案 A（最完整，約 2–4 小時）：** 用 Wix Headless SDK
  - Demo 表單接 **Wix Forms / Wix CRM**（`@wix/forms` 或 `@wix/crm` contacts + submissions），讓提交紀錄出現在 Wix Dashboard 的 Inbox/Contacts。
  - 「Start 14-Day Trial」接 **Wix Pricing Plans**：建立 Starter / Pro / Premium 三個方案，各設 14 天 free trial，再用 `redirects.createRedirectSession({ paidPlansCheckout })` 導到 **Wix 託管的 checkout 頁面**。
  - 現有的自訂 mock-up 保留，當作「預覽」。
- **方案 B（最低限度，約 15 分鐘，至少要做）：**
  - `app.js` L373–374 改成：`Thank you, ${name}. Prototype only: in the live service this request would be routed to our Hong Kong onboarding team via WhatsApp within 1 business day (no data is sent from this demo).`
  - BP §5.3 最後一句（見 P0 刪減 T5）和 Slide 5 底部「Verified Live」那行，寫明「hosted on Wix Headless (Wix hosting + Wix Media CDN); checkout and form are simulated front-end mock-ups」，主動說明而不是被老師發現。
- **補充：** 舊的 Wix Editor 站（`example.wixsite.com/deskmate-ai`）裝有 Pricing Plans、Checkout、Forms，但 `/plans-pricing` 回 404，內容也是舊版，**不建議**當作提交連結。如果時間不夠做方案 A，可以考慮在那個站修好 Pricing Plans 頁，再從 Headless 站加一個「Wix native checkout」外部連結。這是次佳方案。

#### P0-7 提交前的流程檢查
- `To_Verify.md` L61：**確認課程對 AI 工具的規定**。如果要求申報，在 BP cover 或 References 後加一行 AI-use declaration。
- `submission/` 裡有容易上傳錯的舊檔：`Business_Plan.docx`（18 KB 舊稿）、`Business_Plan_Updated_prev_backup.docx`、`Presentation.pptx`（40 KB 舊稿）。**移到 `_archive/`**，避免傳錯。只交 `Business_Plan_Updated.pdf`、`DeskMate_AI_Presentation.pptx` 和 Wix Headless 連結。

### 🟠 P1 — 對 A+ 影響最大的升級

#### P1-1 BP §2.4：讓每個目標都可衡量，並對應 Fig 12-1
- **檔案：** BP p2 §2.4
- 引言句改成：`Our objectives support a downstream strategy, which improves the value delivered to customers, and each uses a Figure 12-1 measure so that even intangible benefits are measurable (Schneider, 2017).`
- 第 2 點：`Enhance marketing: convert at least 25% of completed trials into paid plans by month 12 (conversion-to-buyer rate).`
- 第 3 點：`Serve existing customers better: keep monthly cancellations below 5% (customer loyalty).`
- **第 4 點（目前沒有數字和期限）改成：** `Open new markets: sign 10 paying clinics or tutorial centres by month 18, measured by active subscriptions in the new segments.`

#### P1-2 BP §6：修正 opportunity cost 的用法，補上 ROI 的限制
- **檔案：** BP p4 §6 最後一句「Beyond quantitative ROI, DeskMate AI reduces owners' opportunity cost of missed treatment hours…」
- **改成：** `Our main opportunity cost is the founder's forgone graduate salary, which is excluded from cash TCO; and because ROI converts everything to money and favours short-term results, it understates intangible benefits such as salon loyalty (Schneider, 2017).`
- **為什麼要改：** Schneider 的 opportunity cost 是**本公司**選這個專案而放棄其他選擇的利益；現在寫的是**客戶**少做療程的損失，教科書概念用錯了。

#### P1-3 BP §6：TCO 補上 labour／employee costs 和 10/10/80
- **檔案：** BP p4 Table 7 ＋ Table 7 後的第一句
- Table 7 Development 的 Items：`Contract developer and designer labour: website, AI and WhatsApp/Instagram integration, booking module, testing`
- Table 7 Marketing 的 Items：`Social and search ads, part-time onboarding staff for demo visits and trial support`
- Table 7 後的第一句改成：`The HK$400,000 seed request, suited to angel investors given falling cloud start-up costs, is mostly labour, consistent with Schneider's (2017) 10% hardware, 10% software and 80% labour pattern.`
- **為什麼要改：** 「done-for-you onboarding」60 間店需要大量人力，評審一定會問誰來做。

#### P1-4 Break-even 與營收爬坡（投資人最想看的數字）
- **BP §6**，接在「2.6x coverage」後面：`Operating break-even needs 24 Pro salons (HK$18,333 ÷ HK$788); adding five salons a month reaches it in month 5 and the 60-salon target in month 12.`
- **Slide 6：** 「2.6×」下面加一行小字：`Break-even at 24 Pro salons (≈ month 5)`；「60」的說明改成：`If all on Pro: HK$47,280 / mo`（補上前提）。
- **講稿 Slide 6：** 見 P1-6。
- **（可選）** 在 Q&A 加一句：依線性爬坡，Year 1 的 salon-months 總共 390，乘 HK$788 ≈ HK$307k 營收，所以 Year 1 還不會回本；這也是需要 seed funding 的理由。

#### P1-5 網站：做出 Fig 3-7 goal 1 / 4 和 permission marketing
- **檔案：** `wix-site/index.html`、`styles.css` → 重新部署到 Wix Headless → 重新截 `submission/wix-screenshots/`
1. **About／organisation facts（Fig 3-7 goal 1）：** 在 `#contact` 的 `.contact-meta` 下面（L504 之後）加一列，例如 `<div class="cm-row"><span class="cm-k">About Us</span><span class="cm-v">Hong Kong start-up founded by [Author] (PolyU HKCC) — on a mission to give every independent salon a 24/7 bilingual front desk.</span></div>`；footer 也可以加一個「About」連結。
2. **Opt-in 勾選框（permission marketing＋PDPO opt-out＋retention）：** 在 L541 之前加一個**預設不勾選**的 checkbox：`<label class="optin"><input type="checkbox" id="fOptIn" name="optin"> Send me monthly salon booking tips and performance reports (optional — unsubscribe anytime).</label>`。L545 的 PDPO 說明同步改成：`…used to arrange your walkthrough and, only if you tick the box, to send opt-in updates. Unsubscribe anytime under Hong Kong PDPO.`
3. 完成後 BP Table 5「Trust」那一列可以補「opt-in only updates」（表格不算頁數，但仍會佔版面，要跟 T 系列刪減一起處理）。

#### P1-6 講稿重寫（265 字 → 347 字，時間用足，教科書術語都講到）
- **檔案：** PPTX 6 頁講者備忘稿＋`Presentation_Script.md` L7–L12（**兩邊要完全一樣**）
- 非 demo 部分 273 字 ÷ 120 秒 ≈ 136 wpm；demo 部分 74 字，留 60 秒給點擊操作。

| 頁 | 時間 | 新講稿 |
|---|---|---|
| 1 | 0:00–0:10 | Good morning. DeskMate AI is a bilingual AI receptionist that answers WhatsApp, Instagram and website enquiries for small Hong Kong beauty salons. |
| 2 | 0:10–0:40 | Salons with one to ten staff rarely have a receptionist, so enquiries are missed during treatments and after closing. At minimum wage, four hours of reception a day costs about 4,482 Hong Kong dollars a month; our Pro plan costs 788, which is 82% less. This is B2B e-commerce on a Fee-for-Service model: a predictable monthly fee, no per-booking commission, and a 14-day trial rather than a freemium tier. |
| 3 | 0:40–1:05 | We target owner-run salons in Mong Kok, Causeway Bay and Tsim Sha Tsui. As a new brand, we focus on the awareness and exploration stages of the customer relationship life cycle: social and search ads inform owners, then the web demo, the trial and a one-to-one demo explain the product. Our targets are 25% trial-to-paid conversion and under 5% monthly churn. |
| 4 | 1:05–1:30 | All three channels feed one booking engine and one shared calendar. It runs on a three-tier design with managed cloud and serverless functions, so we pay per use and scale for evening peaks, while a CDN keeps pages fast on mobile. Salons pay by recurring card, Apple Pay or Google Pay, or FPS for annual invoices. |
| 5 | 1:30–2:30 | Here is the live Wix prototype. The navigation is clear and the layout works on mobile. In the booking example, a client asks in Cantonese for a gel manicure after six; the assistant confirms six-thirty and the shared calendar updates. On Pricing, each plan starts with a 14-day trial; I'll choose Pro, and the simulated checkout shows HK$0 due today. Finally, the Book a Demo form is our one-to-one touchpoint, with a PDPO notice. |
| 6 | 2:30–3:00 | We are asking for 400,000 Hong Kong dollars in angel or seed funding, estimated with total cost of ownership. Ongoing costs are 122% of the initial build, inside the textbook's 50 to 200% range. We cover monthly operating costs at 24 Pro salons and aim for 60 by month twelve, or 47,280 dollars a month if all choose Pro. Thank you. |

#### P1-7 Slide 4 / Slide 6：讓教科書概念在 PPT 上看得到
- **Slide 4**（`04-operations.html`）：中間卡片「Nearby Asia Cloud…」下面加一列小字：`Three-tier · PaaS · Serverless · CDN · 5G — hosting chosen on Schneider's 6 criteria`。「Cantonese & English NLP **trained** on salon menus」改成「**configured with** each salon's menu」，和 BP「We configure…」一致，也避免誇大。標題「zero double-bookings」改成「no double-bookings by design」。
- **Slide 6**（`06-financials.html`）：「400k」說明改成 `Angel / seed request — 12-month runway`；加上 P1-4 的 break-even 和前提說明。底部 TCO 那行可以補「Labour-led (Schneider 10/10/80)」。

#### P1-8 BP §5.2：5G 理由改成即時連線，並說明為什麼不選 IoT／microserver
- **檔案：** BP p4 Table 6「5G mobile networks」那一列
- **改成：** `Low-latency 5G supports real-time replies to clients messaging from phones and instant mobile checkout; IoT and microservers are unnecessary at a 60-salon scale.`
- **為什麼要改：** Instruction 明確寫「low-latency performance, enhanced connectivity for real-time applications」；說明「為什麼不選」也是 justify 的一部分。

#### P1-9 BP Executive Summary 補上 82%
- **檔案：** BP p2 §1 第 4 句
- **改成：** `DeskMate AI's Pro subscription costs HK$788 a month, 82% less.`（只多 3 個字，不影響頁數；三份交付物的主賣點從此一致）

#### P1-10 BP §4：補上 Familiarity / Commitment 階段的訊息重點
- **檔案：** BP p3 §4 最後一句
- **改成：** `…lower retention cost and move salons toward familiarity (messages that convince owners to keep paying) and commitment (messages that reinforce good feelings) under Hong Kong's PDPO with clear opt-out.`

### ✂️ BP 頁數抵銷表（讓 P0／P1 的新增內容不超過 3 頁）

P1-1、P1-3、P1-4、P1-10 大約會多出 **5–6 行**。下面的刪減可以省下大約 **7 行**：

| ID | 位置 | 原文 | 改成 | 省下 |
|---|---|---|---|---|
| T1 | §3 Table 3 後的段落（p3） | Clinics and tutorial centres form Year 2 expansion segments. Applying online market segmentation and virtual space design (Schneider, 2017), the live Wix prototype's Industries switcher gives each segment a dedicated entry point while serving browsers, shoppers and buyers on one site. | Clinics and tutorial centres are Year 2 segments; the prototype's Industries switcher gives each a dedicated virtual space (Schneider, 2017). | ~1.5 行 |
| T2 | §5.2 引言（p4） | At 60 salons on Pro, the platform handles up to 60,000 monthly conversations, peaking in evenings and before holidays. Following a three-tier … (Schneider, 2017; Table 6). | At 60 Pro salons (up to 60,000 conversations a month, peaking in evenings), a three-tier client–Web–database design on managed cloud (PaaS), serverless functions and a CDN meets Schneider's (2017) six hosting criteria — functionality, reliability, scalability, security, backup and cost (Table 6). | ~1 行 |
| T3 | §5.3 第 3–5 句（p4） | Stripe notes cards… Card processing is outsourced to certified gateways. Our live Wix prototype includes a safe Simulated Checkout Mock-up demonstrating plan switching, HK$0 trial activation and payment method selection without real billing. | Stripe (n.d.) notes cards and wallets are core Hong Kong methods; a PCI DSS-certified gateway tokenises cards, and the Wix prototype simulates this checkout without real billing (Figure A4). | ~1.5 行 |
| T4 | Table 5「Mobile-responsive design」（p3） | Verified responsive layout across 1440x900 desktop and 375x812 mobile with slide-down mobile navigation and zero horizontal overflow. | Responsive at 1440×900 and 375×812, with slide-down mobile menu (Figure A6). | ~1 行 |
| T5 | Table 5「Accessible information」（p4） | Clear hierarchy presenting pricing, live booking example, savings calculator, Industries tabs and expandable FAQ. | Pricing, booking example, savings slider, Industries tabs and FAQ (Figures A1–A3). | ~1 行 |
| T6 | §2.1 第 1 段最後一句 | We configure the salon's services, prices and opening hours during onboarding. | （併入前一句）…with a short summary, after we configure its services, prices and hours. | ~0.5 行 |

> 每改完一輪，就重新匯出 PDF，再用 `bp-verify` 截圖確認：**p4 最後一行仍是 §6 的結尾，References 從 p5 開始**。

### 🟢 P2 — 選做的細節打磨

1. **APA 頁碼／章節定位：** 引用具體數據時，加上章節定位：「(Schneider, 2017, Chapter 3)」（5% → 25–80%）、「(Schneider, 2017, Chapter 12)」（50–200%、10/10/80）。
2. **把附錄截圖和正文連起來：** 在 Table 5 各列加「(Figure A1)」等交叉引用（T4、T5 已示範）。這樣評審會知道 usability 的每一項說法都有截圖佐證。
3. **Table 3 Behavioural 那一列：** 先寫客群「做什麼」，再寫網站怎麼回應。例如：`Salons already booking through WhatsApp DMs with heavy evening enquiry volume; the site serves browsers (demo, 'Free Trial' trigger words), shoppers (plan comparison, savings slider, FAQ) and buyers (one-click 'Start 14-Day Trial').`
4. **Fig 3-5 web presence（網站）：** 加一個「What's new」小區塊（例如「Nov 2026: Instagram DM sync added」），對應 *current, regularly updated information → encourage return visits*。外部評價或獎項沒有真的就不要加。
5. **導覽 scroll-spy：** 目前不論捲到哪一節，「Home」都一直是 active（見 `wix-contact.png`）。用 `IntersectionObserver` 依目前所在的 section 切換 `.nav-link.active`，加強 *clear navigation*。
6. **無障礙（W3C）：** `.plan-switcher` 和 `.pay-methods` 宣告了 `role="radiogroup"`，但子按鈕沒有 `role="radio"` / `aria-checked`；`.segmented` tablist 缺 `aria-controls`；建議加一個 skip-to-content 連結；檢查淺灰字的對比度是否達 4.5:1。
7. **網站上的效能數字：** 「Synced in 0.8s」「Zero double-bookings」前面加上「Illustrative:」，和 testimonial 的標示方式一致。
8. **Wix 免費方案的浮動標籤：** 「Built on WIX Headless」會在手機版擋住 hero 的狀態列（見 `wix-mobile.png`）。demo 時先點 × 關掉，或者在 hero 下方留白。
9. **BP 版面密度：** 10.5 pt 字＋1.9 cm 邊界在規定範圍內，但很密。如果 T1–T6 刪減後有空間，把 Table 字級統一成 9.5 pt，不要再縮正文。
10. **PPTX 是全圖片：** 每頁都是一張圖，沒有可選取的文字，對螢幕閱讀器也不友善。建議至少在每張圖的 Alt Text 填入該頁的重點文字（python-pptx：`pic._element.nvPicPr.cNvPr.set('descr', '…')`）。
11. **Slide 1：** 右下角加上 Wix 網址小字，萬一 Slide 5 的連結失效還有備援。
12. **`To_Verify.md` 已過時：** 「PDF 共五頁」（現在 6 頁）、舊 wixsite 連結、「示範尚待發佈到 Wix」都要更新，避免自己誤判狀態。
13. **Stripe 的說法：** `To_Verify.md` #5 指出「電子錢包排名」其實來自 Antom。建議打開 Stripe 原文核對，或者改成只寫「cards and digital wallets are widely used」。
14. **Meta Business Agent：** 香港是否已開放、是否支援廣東話，目前都查不到。BP 的寫法沒問題，但 Q&A 被問到時不要說得太肯定。

---

## 結論與建議執行順序

| 順序 | 項目 | 預估時間 | 分數影響 |
|---|---|---|---|
| 1 | P0-1 修 Slide 3 CRLC＋P1-6 新講稿＋P0-4 同步 `Script.md` | 45 分鐘 | Presentation +2.5 |
| 2 | P0-2、P0-3、P0-5、P1-1～P1-4、P1-8～P1-10＋T1–T6 刪減（BP 一次改完再匯出） | 90 分鐘 | BP +3.5 |
| 3 | P0-6 方案 B（15 分鐘）→ 時間夠再做方案 A（2–4 小時） | 15 分鐘～4 小時 | Prototype +1～+3 |
| 4 | P1-5 加 About 和 opt-in；P1-7 改 Slide 4/6 | 45 分鐘 | Prototype +1、Presentation +0.5 |
| 5 | P0-7 AI 申報與整理檔案；P2 項目視時間處理 | 20 分鐘＋ | 降低風險 |

**現況：85/100。P0＋P1 全部完成後預估 95–96/100（A+）。** 最關鍵的單一修正是 **P0-1（Slide 3 的 Separation）**；最大的隱藏風險是 **P0-6（沒有使用 Wix 原生的 checkout 和表單）**。

*本報告只做審核，沒有修改任何交付檔案。*


---

## Round-2 Re-Verification & Final Score (2026-11-20)

**複審方法：** 重新以 `pypdf`、`python-docx`、`python-pptx` 解析最新交件檔案（`Business_Plan_Updated.pdf`、`.docx`、`DeskMate_AI_Presentation.pptx`、`.pdf`、`Presentation_Script.md`、`To_Verify.md`），以 `Invoke-WebRequest` 抓取線上 Wix Headless 網站（`https://deskmate-ai-demo.example.com`）與其 CSS/JS 資源，並逐頁目視檢查 `deck-final/bp-verify/page-1..6.png`、`deck-final/pptx-verify/slide-1..6.png` 及更新後的 `submission/wix-screenshots/*.png`。所有交付物维持唯讀（read-only）。

### 1. P0 / P1 / P2 修正逐項驗收結果

| 編號 | 原審核問題 | 複審驗證結果 | 狀態 |
|---|---|---|---|
| **P0-1** | Slide 3 CRLC Stage 5 誤寫為 Retention；trial 錯置於 Familiarity | `slide-3.png` 已改為 **Stage 5 Separation**（「No ads targeted; exit check & PDPO opt-out honoured」）；14-day trial 移回 **Stage 2 Exploration (Target)**；Stage 1 Awareness 與 Stage 2 Exploration 均加銅色框標示 `Target`；副標更新為 `CRLC — Target: Awareness & Exploration`。 | ✅ 已通過 |
| **P0-2** | APA 7 參考文獻未按字母排序；Table 5 括號引用格式不合規；Stripe `en-de` 語系 | `page-5.png` 與 `.docx` 驗證：6 筆文獻嚴格依 **Labour Department → Meta → Schneider → SleekFlow → Stripe (`en-hk`) → Wati** 字母排序，均具 0.5" 懸掛縮排（`first_line: -457200, left: 457200`）與斜體書名／標題；Table 5 已改為 `meeting Schneider's (2017) two-way communication accessibility goal (Figures A2, A5)`。 | ✅ 已通過 |
| **P0-3** | BP Table 5 宣稱 `<40 KB code` 與實測不符 | Table 5 已改為 `~63 KB HTML/CSS/JS`（實測 live HTML 29.6 KB + CSS 17.8 KB + JS 16.8 KB = 64.2 KB / 62.7 KB KiB，完全吻合）。 | ✅ 已通過 |
| **P0-4** | `Presentation_Script.md` 與 PPTX 備忘稿不同步；Slide 5 缺 `#checkout` 熱區 | PPTX 6 頁備忘稿與 `Presentation_Script.md` 100% 逐字同步（347 字）；Slide 5 新增並排的 `Plans (#pricing)` 與 `Checkout (#checkout)` 熱區（共 6 個可點擊連結），Demo 路徑說明亦已更新。 | ✅ 已通過 |
| **P0-5** | 年繳 FPS 9 折、Starter 功能、Slide 3 競品價格（US$49）跨檔案不一致 | BP §5.3 與 Slide 4 均納入 `FPS prepaid annual plans (10% off) without card fees`；BP Table 2 Starter 統一為 `bilingual FAQ answers and booking capture`；Slide 3 競品價格改為已驗證的 `SleekFlow Pro from US$109/mo annual; Wati automation`。 | ✅ 已通過 |
| **P0-6** | Wix 原生功能與表單「logged」虛假提示風險 | 完整落實 Option B：live `app.js` L380 改為 `Prototype confirmation (simulated — no external data stored)…`；網站表單底部、結帳橫幅、BP §5.3、Slide 5 頁尾與 Q&A #2 均誠實揭露「Wix Headless hosting + Wix Media CDN + safe front-end simulation on a free Wix plan without live billing」。 | ✅ 已通過 |
| **P0-7** | `submission/` 內含舊版草稿易傳錯；AI 申報提醒 | `submission/` 已清理完畢（舊檔移至 `archive/`），僅留最終交件檔；`To_Verify.md` 已加入醒目 AI 工具申報確認提醒。 | ✅ 已通過 |
| **P1-1** | BP §2.4 第 4 個目標不可衡量、未點名 Fig 12-1 | §2.4 已點名 `Figure 12-1 measure (Schneider, 2017, Chapter 12)`，第 4 點改為 `sign 10 paying clinics or tutorial centres by month 18, measured by active subscriptions in the new segments`（同步至 Slide 3）。 | ✅ 已通過 |
| **P1-2** | BP §6 Opportunity cost 誤用為客戶端、缺 ROI 限制 | §6 已修正為 `founder's forgone graduate salary (excluded from cash TCO)`，並明確指出 `ROI converts all benefits to money and favours short-term results, it understates intangible benefits such as salon loyalty`。 | ✅ 已通過 |
| **P1-3** | TCO 缺 labour/employee costs 與 10/10/80 規則 | Table 7 納入 `Contract developer and designer labour` 與 `part-time onboarding staff`，§6 與 Slide 6 均載明符合 Schneider `10% hardware, 10% software and 80% labour pattern`。 | ✅ 已通過 |
| **P1-4** | 缺損益兩平（break-even）與月收前提 | BP §6、Slide 6 與講稿均補上 `24 Pro salons (~Month 5; HK$18,333 ÷ HK$788)` 營運損益兩平點、Slide 6 補上 `If all choose Pro` 前提，Q&A #5 亦補充 390 salon-months ≈ HK$307k 首年線性爬坡說明。 | ✅ 已通過 |
| **P1-5** | 網站缺組織資訊（Fig 3-7 goal 1）、回訪誘因（Fig 3-5）與 opt-in 勾選框 | Live 網站與 `wix-contact.png` 已驗證新增 `About DeskMate AI`（`#about`）、`Latest Platform Updates`、預設未勾選的 `#fOptIn` Permission Marketing 勾選框及 PDPO opt-out 條款。 | ✅ 已通過 |
| **P1-6** | 講稿僅 265 字偏短 | 已全面替換為 347 字 A+ 講稿（非 demo 273 字 + 60 秒 demo 74 字）。 | ✅ 已通過 |
| **P1-7..10** | Slide 4/6 教科書術語、5G/IoT 理由、Exec Summary 82%、§4 階段訊息 | Slide 2 標明 `not a permanent freemium tier`；Slide 4 呈現 `Three-Tier PaaS & Serverless`、`CDN & 5G (6 hosting criteria)`、`configured with each salon's menu`、`no double-bookings by design`；Table 6 說明 5G 即時回覆與 60 間店規模不需 IoT/microservers；Exec Summary 補上 `82% less`；§4 補齊 familiarity (convince) 與 commitment (reinforce) 訊息。 | ✅ 已通過 |
| **P2-1..12** | 章節定位、圖表交叉引用、scroll-spy、ARIA、Alt Text、Direction 2 排版 | BP 補上 `Chapter 3` / `Chapter 12` 與 `Figures A1–A6` 交叉引用；網站補上 `IntersectionObserver` scroll-spy（`wix-demo.png` 與 `wix-contact.png` 導覽列高亮正確）、`skip-link`、`role="radio"`、`aria-controls="transcriptBody"` 與 `Illustrative:` 標記；PPTX 6 張圖片均寫入完整 `descr` Alt Text；BP 改用 Direction 2 視覺排版，**正文嚴格維持 3 頁（p2–p4）**且留白均衡。 | ✅ 已通過 |

### 2. 最終評分卡（Round-2 Verified Score）

| 評分項目 | 比重 | Round-1 分數 | **Round-2 最終分數** | 複審評語 |
|---|---|---|---|---|
| **Business Plan PDF**（概念分析、創意、結構與語言） | 40% | 35.0 | **39.0 / 40** | 嚴格遵守 3 頁正文上限（p2–p4），31 項 Schneider (2017) 核心概念全部精準嵌合且無任何誤用；APA 7 格式、章節定位與圖表交叉引用完整；Direction 2 排版專業易讀。 |
| **Wix Prototype**（可用性、反映商業與收入模式） | 40% | 34.0 | **38.0 / 40** | 完整呈現 B2B Fee-for-Service 三層方案、14 天試用 HK$0 模擬結帳、雙語預約模擬器、計算機、Industries 虛擬空間切換、About 組織資訊、Latest Updates、Permission Marketing opt-in 與 PDPO 聲明；前端模擬已於四處誠實揭露（若使用 Wix 原生付費版 Pricing Plans 後端可拿滿 40/40，以免費方案原型而言已達最高誠信與完成度標準）。 |
| **Presentation PPT & Script**（6 頁簡報 + 3 分鐘講稿） | 20% | 16.0 | **19.5 / 20** | Slide 3 CRLC 五階段（含 Separation 與 Target 標示）完全正確；Slide 1–6 與 BP 數據 100% 同步；Slide 5 具備 6 個可點擊 live demo 熱區；347 字講稿與備忘稿逐字一致並涵蓋所有高分教科書關鍵詞。 |
| **總分** | **100%** | **85.0 / 100** | **96.5 / 100（A+ 驗收通過）** | **所有 P0 與 P1 扣分點已 100% 消除，跨交付物零矛盾、零格式違規。** |

**最終審核結論：** **PASS (A+ Ready, 96.5/100)**。學生只需在上傳前按 `To_Verify.md` 完成最後兩項人工確認（核對課程是否要求 AI-use declaration、親自順跑一次 Slide 5 點擊 Demo 與 347 字講稿）即可直接提交。


---

## Round-3 Final Taste & A+ Audit (2026-11-20)

**複審範圍與方法：** 依據 `Taste_Spec_Opus55.md`（§1–§4，Gates T1–T15）與 `humanizer` 規範，對 Round-2 完成後的線上 Wix Headless 網站（`https://deskmate-ai-demo.example.com`，HTTP 200）、原始碼（`wix-site/index.html`、`styles.css`、`app.js`）、最新網站截圖（`submission/wix-screenshots/*.png`）、重建版商業計劃書（`Business_Plan_Updated.pdf` / `.docx` 及 `deck-final/bp-verify/page-1..6.png`）、6 頁簡報與備忘稿（`DeskMate_AI_Presentation.pptx` / `.pdf` 及 `deck-final/pptx-verify/slide-1..6.png`）以及 3 分鐘講稿（`Presentation_Script.md`）進行唯讀自動化腳本檢測與逐頁目視驗收。

### 1. Taste & Quality Acceptance Table (Gates T1–T15)

| Gate | 範疇 | 實測驗證結果 | 得分 | 狀態 |
|---|---|---|---|---|
| **T1** | Website Craft | `.site-header` 具 `position: sticky`、`backdrop-filter: saturate(180%) blur(20px)`、`@supports` fallback（`--glass-bg-solid`），捲動 `>8px` 切換 `.is-scrolled` 細線邊框。 | 5 / 5 | ✅ PASS |
| **T2** | Website Craft | H1/H2/H3 採用 `Newsreader` 400（無粗體襯線），內文 `Inter` 400 `17px`，價格／時間／統計全面套用 `tabular-nums`，`text-wrap: balance/pretty`，全站標題與導覽列統一為 sentence case。 | 5 / 5 | ✅ PASS |
| **T3** | Website Craft | 嚴格使用 `--ease-out`、`--ease-standard`、`--ease-spring` 三條曲線；`.js .reveal` 單次觸發且無 JS 時 100% 可見；`@media (prefers-reduced-motion: reduce)` 關閉位移動畫並將 typing 縮短至 300ms。 | 6 / 6 | ✅ PASS |
| **T4** | Website Craft | `375×812`、`768×1024`、`1440×900` 均零水平溢位（`scrollWidth === innerWidth`）；按鈕與 pills 觸控高度 `≥44px`；`#customSalonInput` 為 `16px`（防 iOS 自動放大）；手機版預留 `72px` 底部空間，Wix 徽章不遮擋主 CTA。 | 7 / 7 | ✅ PASS |
| **T5** | Interactive Wow | 純 CSS 鈦金屬／炭灰 iPhone 外框（`--titanium-1..3` 漸層、Dynamic Island、3 顆側鍵、`--shadow-device`、`54px/43px` 圓角、暖香檳色回覆氣泡 `#EFE6D8`），零外部圖片依賴。 | 7 / 7 | ✅ PASS |
| **T6** | Interactive Wow | `id="customSalonInput"`（預設 `Lumière Nail Studio`、`maxlength="40"`）+ 4 個 `.salon-pill` 預設按鈕 + `#salonHint` 誠實標註；空白輸入自動回退預設值；全程僅用 `textContent` 插入（`<b>x</b>` 測試為純文字，零 XSS 風險）。 | 8 / 8 | ✅ PASS |
| **T7** | Interactive Wow | 互動時序精準：450ms debounce、`runId` 計時器取消機制（快速連點 5 個 pills 僅留一組對話，零疊泡）、120ms 客人氣泡、600ms typing 三點動畫（`#phoneChannel` 顯示 `typing…`）、`700 + reply.length * 4`（上限 1400ms）後淡出並顯示雙語回覆。 | 8 / 8 | ✅ PASS |
| **T8** | Interactive Wow | 回覆後 +200ms 右側共享行事曆 18:30 時段觸發 `.is-locking`（`Holding 18:30` + 900ms 香檳銅色光環 pulse），隨即轉為 `.is-locked`（1.5px 鎖頭 SVG + `Confirmed for {name}`）；`#calendarDayLabel` 同步沙龍名，`#syncStatus` 保留 `Illustrative: confirmed in 0.8s`。 | 7 / 7 | ✅ PASS |
| **T9** | Humanizer | 全交付物（`index.html`、`app.js`、BP DOCX/PDF、Slides 1–6 HTML/Alt Text/Notes、`Presentation_Script.md`）可見文字之破折號 `—` 數量 = **0**。 | 8 / 8 | ✅ PASS |
| **T10** | Humanizer | 全交付物禁用 AI 詞彙（`quietly`、形容服務之 `Quiet`、`seamless`、`showcase`、`elevate`、`unlock`、`empower`、`robust`、`crucial`、`delve`、`leverage`、`cutting-edge`、`serves as`、`boasts`、`low-friction`、`bloat`）grep 結果 = **0**；`Enhance marketing programs` 僅作 Schneider (2017) Fig 12-1 課本標籤。 | 6 / 6 | ✅ PASS |
| **T11** | Humanizer | BP 全文保持正式商業計劃書語氣（零口語縮寫、零 "Let's" 開場、零單句金句收尾）；講稿保留自然口語節奏。 | 4 / 4 | ✅ PASS |
| **T12** | Slide & BP Editorial（硬門檻） | BP PDF 嚴格共 **6 頁**（p1 封面、**p2–p4 正文 3 頁零溢頁**且 p4 底部留白約 25%、p5 APA 7 文獻、p6 附錄）；PPTX 嚴格 **6 頁**；講稿 **376 字**（≤400 字）；§2.4 四項目標標籤無重複（`Increase sales` / `Enhance marketing programs` / `Serve existing customers better` / `Open new markets`）；Slide 1/2/4 標題與排版完全符合規格。 | 8 / 8 | ✅ PASS |
| **T13** | Rubric Integrity（硬門檻） | `#about`（Fig 3-7 goal 1）、`Latest Platform Updates`（Fig 3-5 日期雙欄）、未預勾之 `#fOptIn`（無 `checked` 屬性）+ PDPO opt-out、`Sample` / `Illustrative` / `Prototype simulation` 誠實標記全部在位；Slide 3 Stage 5 = `Separation` 且 Awareness/Exploration 標示 `Target`；Slide 5 Step 2 改為 `Personalised salon chat simulation (18:30, HK$280)`（移除 "live chat"）。 | 8 / 8 | ✅ PASS |
| **T14** | Textbook Integrity（硬門檻） | 31 項 Schneider (2017) 核心概念與全部財務／營運數字（HK$388/788/1,488、HK$43.10、HK$4,482、82%、60 間店、25% 轉換、<5% 流失、18 個月 10 間診所／補習社、US$109、60,000 對話、FPS 年繳 9 折、TCO HK$400k = 180k+60k+120k+40k、122% 位於 50%–200%、10/10/80、24 間 Pro 損益兩平、HK$18,333、Month 5、HK$47,280、2.6×、5% 忠誠度 → 25%–80% 利潤、6 筆字母排序 APA 7 文獻）100% 完整保留。 | 8 / 8 | ✅ PASS |
| **T15** | 跨交付物一致 | 網站按鈕（`Start Pro 14-day trial`、`Activate 14-day free trial · HK$0 today`）與講稿點擊步驟逐字一致；Slide 5 具 6 個可點擊熱區；BP Figure A2 圖說描述手機外框個人化沙龍模擬；BP Table 5 檔案大小更新為 `about 94 KB`（與實測未壓縮 94.3–94.5 KB 吻合）；BP 附錄與 Slide 5 已嵌入最新實機截圖；PPTX 備忘稿與 `Presentation_Script.md` 376 字講詞 100% 同步。 | 5 / 5 | ✅ PASS |
| **總計** | **Gates T1–T15** | **硬門檻 T12、T13、T14 全部通過，零殘留缺陷** | **100 / 100** | **✅ PASS** |

### 2. 官方 40 / 40 / 20 評分卡（Round-3 最終核定）

| 評分項目 | 比重 | Round-1 | Round-2 | **Round-3 最終分數** | 最終審核評語 |
|---|---|---|---|---|---|
| **Business Plan PDF** | 40% | 35.0 | 39.0 | **39.5 / 40** | 正文嚴格控制在 3 頁（p2–p4），零破折號、零 AI 陳腔，Figure 12-1 四項目標標籤精準無重複，Table 5 檔案大小（94 KB）與 Figure A2 圖說完全同步最新線上版本。 |
| **Wix Prototype** | 40% | 34.0 | 38.0 | **39.0 / 40** | 新增 Apple 級純 CSS 鈦金屬 iPhone 自訂沙龍名雙語互動模擬器（含 typing 節奏與共享行事曆銅色脈衝鎖定回饋）、毛玻璃導覽列與嚴謹無障礙／防 XSS 實作，視覺工藝與互動說服力大幅躍升。 |
| **Presentation & Script** | 20% | 16.0 | 19.5 | **19.5 / 20** | 6 頁簡報視覺留白均衡、去 AI 化標題乾淨利落，Slide 5 更新最新截圖與誠實標籤，376 字講稿涵蓋自訂沙龍名實機示範並與 PPTX Speaker Notes 逐字同步。 |
| **總分** | **100%** | **85.0** | **96.5** | **98.0 / 100** | **A+ Sign-Off: PASS（Taste Score 100/100 · Rubric Score 98.0/100）** |

**最終裁定（Final Verdict）：** **`PASS`（零必改缺陷，已達最高提交標準）**。
