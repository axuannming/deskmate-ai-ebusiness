# DeskMate AI (SEHS2265) — 超級大 Review 報告、Handoff Plan 與驗收標準

> **審查時間**：2026-11-20 21:20 HKT（距離 Blackboard 截止 `23:59 HKT` 剩餘約 **2 小時 39 分鐘**）
> **審查對象**：Live Wix Prototype (`https://deskmate-ai-demo.example.com`)、[Author_[Student ID].pdf](file:///./READY_TO_UPLOAD/Author_[Student ID].pdf)、[Author_[Student ID].pptx](file:///./READY_TO_UPLOAD/Author_[Student ID].pptx)、[Presentation_Script.md](file:///./submission/Presentation_Script.md)
> **對照準則**：[SEHS2265 Individual Assignment Two Instruction.pdf](file:///./SEHS2265%20Individual%20Assignment%20Two%20Instruction.pdf) + 用戶先前指出的所有 UX 雷區

---

## 第一部分：超級大 Review 發現清單（實測證據）

### ✅ 已 100% 達標、禁止破壞的項目（DO NOT REGRESS）
1. **Business Plan PDF 純白紙黑字與頁數**：XML 實測 `word/document.xml`、`header1.xml`、`footer1.xml` 文字色**僅有 `000000`**，表格表頭填色僅 `F2F2F2`，邊框僅 `000000` / `BFBFBF`，全篇 `Calibri`，零彩色字體；總頁數嚴格 **6 頁**（封面 p1、正文 p2–p4 共 3 頁、APA 7 參考文獻 p5、截圖附錄 p6），零 em-dash（`—`）。
2. **PPTX 結構與熱區**：嚴格 **6 頁**、6 組 Alt Text、Slide 5 內建 **6 個可點擊 Wix 連結熱區**，全數通過視覺無裁切檢查。
3. **Wix 網站三渠道視覺與三店名獨立菜單**：WhatsApp / Instagram / Website 介面已有顯著區隔；三間預設沙龍各自對應美甲 / 美髮 / 美容服務與日曆；手機 `375×812` 零橫向卷軸，所有按鈕高度 ≥ `44px`，0 個 JS 錯誤。
4. **數字與課本理論一致性**：`HK$388 / 788 / 1,488`、`HK$43.10/hr → HK$4,482/mo (-82%)`、`HK$400,000` TCO（`180k / 120k / 60k / 40k`，122% 持續成本比，10/10/80）、`24 Pro salons (Month 5)`、`60 Pro salons = HK$47,280/mo (2.6×)`、`25%` 試用轉化、`<5%` 月流失、18 個月 `10` 間診所/補習社、Schneider (2017) 5 階段 CRLC 與 PDPO opt-in 全部跨檔一致。

---

### 🔴 P0 必須修正（實測抓出的真實邏輯／互動破綻）

| 編號 | 嚴重度 | 檔案與位置 | 實測發現的問題 | 為什麼會被老師／用戶扣分 |
|---|---|---|---|---|
| **BUG-1** | **P0** | [app.js](file:///./wix-site/app.js#L128-L193) | **`HK mixed (中英)` 根本沒有英文！** 實測 `book`、`price`、`reschedule` 的 `mixed` 提問全是純中文（除店名與數字外 `latin_in = False`），且 `handoff` 情景下 `mixed` 與 `zh` **共用同一個 `handoff.request.zh`，逐字 100% 相同**！ | 重蹈「兩個按鈕點下去沒區別」的覆轍；名義上寫 `HK mixed (中英)`，實際卻是純中文。 |
| **BUG-2** | **P0** | [app.js](file:///./wix-site/app.js#L140-L191) & [Presentation_Script.md](file:///./submission/Presentation_Script.md#L11) | **AI 回覆泡泡沒有提到沙龍店名，與 3 分鐘講稿衝突！** 講稿第 5 頁明說 *"DeskMate AI replies in that salon's name and books six-thirty"*，但目前 `app.js` 的 4 個情景 AI 回覆裡全都**沒有插入 `salonName`**；切到 Instagram / Website 時，客人與 AI 兩則泡泡甚至完全沒出現自訂店名。 | 上台 Live Demo 唸講稿時若老師盯著手機畫面看，會發現「你說 AI 用店名回覆，畫面上卻沒出現店名」。 |
| **BUG-3** | **P0** | [app.js](file:///./wix-site/app.js#L403-L407) | **輸入自訂店名後，舊的預設店名按鈕依然亮黑（`is-active`）！** 實測輸入 `Velvet Brow Studio` 後，上方 `Mong Kok Hair Lab` 仍維持黑色選中狀態。 | UI 狀態說謊，讓使用者誤以為畫面還停在舊店鋪。 |
| **BUG-4** | **P0** | [app.js](file:///./wix-site/app.js#L426-L428) | **Checkout 的店名與 Email 不同步！** 點選 `Mong Kok Hair Lab` 後，Checkout 的 `#coSalon` 變成 `Mong Kok Hair Lab`，但隔壁 `#coEmail` 依然寫死 `owner@lumierenail.example.com`。 | Demo 捲到 Checkout 時，美髮店卻掛著美甲店 Email，細節穿幫。 |
| **BUG-5** | **P0** | [app.js](file:///./wix-site/app.js#L750-L763) | **Checkout 付款方式與月繳／年繳週期自相矛盾！** 選 `Annual invoice via FPS` 會切到 `FPS Bank Transfer`，但切回 `Monthly recurring` 時仍卡在 `FPS Bank Transfer`；甚至月繳狀態也能手動點 FPS，直接違背下方提示句（`FPS is supported for annual subscription invoices`）與 Business Plan §5.3。 | 模擬結帳邏輯自打嘴巴，與計畫書 Payment Systems 敘述衝突。 |

### 🟠 P1 建議同步升級（讓 Demo、PPT、PDF 與講稿 100% 咬合）

| 編號 | 優先度 | 檔案與位置 | 實測發現的問題 |
|---|---|---|---|
| **SYNC-1** | **P1** | [index.html](file:///./wix-site/index.html#L135-L138) | 無 JS 時的靜態 fallback 對話泡泡仍為舊版純中文句子，應與修正後的 `HK mixed (中英)` 預設狀態同步。 |
| **SYNC-2** | **P1** | [05-prototype.html](file:///./deck-final/slides/05-prototype.html#L163-L169) | Slide 5 的 Step 2 副標仍只寫 `Personalised salon chat simulation (18:30, HK$280)`，未體現升級後的「3 業態預設＋3 渠道介面＋中英單語自動對應」亮點（可選擇保留 Checkout 截圖，或把副標改精準）。 |
| **SYNC-3** | **P1** | [Presentation_Script.md](file:///./submission/Presentation_Script.md#L1-L21) & [build_retina_pptx.py](file:///./deck-final/build_retina_pptx.py#L21-L28) | 講稿標題寫 `376 字`，PPTX Speaker Notes 含時間戳記 `0:00-0:10 \|` 共 388 tokens（不含時間戳記為 376 字）；另 Step 2 操作指南應補上一句「切換 WhatsApp / Instagram 渠道與語言分頁」，讓 60 秒 Live Demo 更亮眼。 |
| **SYNC-4** | **P1** | [build_business_plan_v2.py](file:///./deck-final/build_business_plan_v2.py#L521) & Page 6 `Figure A2` | 修改 Wix 後須重新抓取線上 `wix-demo.png`（顯示修正後的真實中英夾雜提問＋含店名廣東話回覆），並同步 Table 5 的線上總 KB 數，重編 PDF 與 `READY_TO_UPLOAD`。 |

---

## 第二部分：Handoff Plan（可直接交給下一個模型執行）

> **給接手模型的指令（Copy-Paste Prompt）**：請嚴格依照下方 `<scope>`、`<fixes>`、`<deployment>` 與 `<acceptance_rubric>` 依序執行，**不可破壞任何已通過的紅線規則**（6 頁純黑白 PDF、6 頁 PPTX、0 em-dash、0 AI 禁用詞、所有 Schneider 2017 課本數據）。

### 1. 嚴格檔案邊界（`<scope>`）
- **允許修改的檔案**：
  1. `./wix-site\app.js`
  2. `./wix-site\index.html`（僅限 `#transcriptBody` fallback 對話文字，勿動結構與 ID）
  3. `./deck-final\slides\05-prototype.html`（僅微調 Step 2 說明文字，不動版面尺寸或超連結結構）
  4. `./deck-final\build_retina_pptx.py`（若微調 Slide 5 Speaker Notes，總英文朗讀字數須維持 `≤ 390 words`）
  5. `./submission\Presentation_Script.md`（與 `build_retina_pptx.py` 逐字 100% 同步）
  6. `./deck-final\build_business_plan_v2.py`（**僅允許**同步 Table 5 的 `about {N} KB` 數字，嚴禁改動純黑白配色、字體、頁邊距或任何學術正文）
- **禁止修改**：`styles.css`（除非發現排版回歸）、Slides `01`/`02`/`03`/`04`/`06`、Business Plan 的任何章節內容與 APA 7 參考文獻、`./other-coursework/`（完全不同的課程，嚴禁碰觸）。

### 2. 逐項修復規格（`<fixes>`）

#### Fix 1：修復 `HK mixed (中英)` 與 `中文` 的真實區隔（`app.js`）
- **核心規則（不可妥協）**：
  - `HK mixed (中英)`：客人訊息**必須是真實香港中英夾雜**（包含英文服務名稱或港式英文詞彙，如 `Gel Manicure`、`Cut & Colour`、`Hydra Facial`、`Thu 6:30 PM`、`price list`、`reschedule`、`Friday`、`bridal package`、`balayage`、`laser`），AI **純廣東話回覆**。
  - `中文`：客人訊息**必須 100% 純中文**（不含 `IG story` 等英文詞，統一用 `限時動態`、中文服務名與中文時間），AI **純廣東話回覆**。
  - `English`：客人訊息 **100% 純英文**，AI **純英文回覆**。
  - **任何泡泡內嚴禁出現中英雙語重複翻譯**。
- **具體替換文案建議**（`scenarios` 內 `client.mixed` 與 `presets.*.handoff.request.mixed`）：
  - `book.mixed`：`Thu 6:30 PM 有冇位做 ${primary.en}？`
  - `price.mixed`：`想問 ${primary.en} 同 ${secondary.en} price list 係幾錢？`
  - `reschedule.mixed`：`星期四 6:30 PM 個 ${primary.en} booking 趕唔切，可唔可以 reschedule 去 Friday 同一時間？`
  - `handoff.mixed`（三店各自獨立）：
    - `nail`：`我有 sensitive skin，想問 4 位姊妹嘅 bridal nail & makeup package 幾錢？`
    - `hair`：`想問 senior stylist 做 balayage 漂染同 bridal hair styling 幾錢？`
    - `skin`：`我做完 laser 有啲 sensitive skin，可唔可以約 therapist 做個 assessment 先 book facial？`
  - `channels.instagram.opening`：`mixed` 用 `啱啱睇到你哋 IG story，`，`zh` 用 `啱啱睇到你哋嘅限時動態，`，`en` 用 `Just saw your IG story. `。

#### Fix 2：讓 AI 回覆自然帶出目前沙龍店名（`app.js` + `index.html` fallback）
- 在 `scenarios.*.reply` 傳入 `salonName`（或 `{ ...preset, salonName }`）：
  - `book.reply.zh`：`多謝聯絡 ${salonName}！幫你訂咗星期四 18:30 嘅${primary.zh}，${primary.price}，需時 ${primary.mins} 分鐘。當日 10:00 會提你。`
  - `book.reply.en`：`Thanks for messaging ${salonName}. You're booked for ${primary.en} on Thursday at 6:30 PM, ${primary.price} for ${primary.mins} mins. We'll remind you at 10 AM that day.`
  - `price` / `reschedule` / `handoff` 的 AI 回覆亦簡潔自然提及 `${salonName}`（例如 `handoff.reply.zh`：`我已經將你${handoff.summary.zh}交畀 ${salonName} ${handoff.role.zh}，佢得閒就會覆你。`），確保 **所有 3 渠道 × 自訂店名** 都能在回覆泡泡看到店名，100% 符合 Slide 5 講稿。
- 同步更新 `index.html` line `136–137` 的初始靜態 HTML 泡泡為最新預設對話（`Lumière Nail Studio` + `WhatsApp` + `HK mixed (中英)`）。

#### Fix 3：修復自訂店名時的 `.salon-pill.is-active` 狀態（`app.js`）
- 修改 `syncActivePill()`：
  ```js
  function syncActivePill() {
    const current = customSalonInput.value.trim();
    salonPills.forEach((pill) => {
      pill.classList.toggle('is-active', current === pill.dataset.salon);
    });
  }
  ```
- 當用戶輸入自訂店名時，三顆預設按鈕全部取消黑色選中態（不說謊），底層仍保留原本業態服務菜單（可選擇依關鍵字 `hair/salon/cut` → `hair`、`skin/facial/derma` → `skin`、`nail/lash/brow` → `nail` 智慧匹配，若無匹配則保持目前 `activePreset`）。

#### Fix 4：同步 Checkout 的 `#coEmail` 與店名（`app.js`）
- 新增 `coEmailDirty` 狀態並監聽 `#coEmail` 的 `input` 事件。
- 在 `runDemo()` 中，當 `!coEmailDirty` 時同步 `#coEmail.value = 'owner@' + slug + '.example.com'`（若為預設 `Lumière Nail Studio` 可為 `owner@lumierenailstudio.example.com` 或 `owner@lumierenail.example.com`；同時確保 `index.html` 初始值一致）。

#### Fix 5：修復 Checkout 月繳／年繳與 FPS 付款方式一致性（`app.js`）
- 當切換 `billingCycle === 'monthly'` 且目前 `payMethod === 'fps'` 時，自動切回 `payMethod = 'card'`。
- 當用戶手動點擊 `payMethod === 'fps'` 按鈕且目前 `billingCycle === 'monthly'` 時，自動切換 `billingCycle = 'annual'` 並勾選 `input[name="billingCycle"][value="annual"]`（讓左側單選鈕、付款按鈕與右側 Order Summary 永遠 100% 邏輯一致，絕不出現「Monthly recurring + FPS」矛盾狀態）。

#### Fix 6：同步 Slide 5 文案、講稿、線上部署與最終檔案
1. 微調 `05-prototype.html` Step 2 副標為：`3 salon presets, 3 channels & Cantonese/English auto-match`。
2. 確認 `Presentation_Script.md` 與 `build_retina_pptx.py` 逐字一致，更新 `Presentation_Script.md` 頂部說明註明「純講稿 376 字（不含時間標籤）」，並在「60 秒實機操作步驟」補充點擊切換 `Instagram` 渠道與 `English` 語言分頁。
3. **依序單檔上傳 Wix Headless**（`siteId: "6d4c08aa-a4d9-4b20-a564-05fb40bf04af"`，每次 `UploadHeadlessWebsiteFiles` **只傳一個檔案**：先 `index.html`，再 `app.js`；若單次呼叫串流中斷，改用快速子代理單檔上傳）。
4. 執行線上 Playwright 驗收腳本，重抓最新 `wix-demo.png`（寫入 `submission\wix-screenshots\`、`deck-final\assets\` 與 artifact 目錄），記下最新線上 `LIVE_ROUNDED_KB`。
5. 若 `LIVE_ROUNDED_KB` 與 `105` 不同，更新 `build_business_plan_v2.py` Table 5 的 `about {N} KB`，重跑 `build_business_plan_v2.py` + `./ Files\LibreOffice\program\soffice.com --headless --convert-to pdf` + `pdftoppm -png -r 140`。
6. 重跑 `uv run --with playwright --with python-pptx --with pillow --with pypdf python ./deck-final\build_retina_pptx.py`。
7. 複製最終產物覆蓋至：
   - `./READY_TO_UPLOAD\Author_[Student ID].pdf`
   - `./READY_TO_UPLOAD\Author_[Student ID].pptx`

---

## 第三部分：客觀驗收標準（Acceptance Rubric — 必須 100% PASS）

接手模型在回報「完成」前，**必須實際跑完下列 12 項 Gate 並貼出實測輸出**，缺一不可：

| Gate | 驗收項目 | 客觀通過條件（PASS Criteria） | 驗證方法 |
|---|---|---|---|
| **G1** | **三種語言真區隔** | 全部 3 店 × 3 渠道 × 4 情景下：`mixed` 客人訊息均含英文詞且含中文（`has_latin=True && has_cjk=True`），AI 回覆純廣東話（`has_cjk=True`、無英文整句翻譯）；`zh` 客人訊息純中文（除店名與金額/時間外零英文詞），AI 純廣東話；`en` 客/AI 均純英文（`has_cjk=False`）。**`mixed` 與 `zh` 零完全相同對話**。 | Playwright 遍歷 108 組組合輸出斷言 `0 failures` |
| **G2** | **AI 回覆含目前店名** | 全部 3 渠道 × 4 情景 × 3 語言下，輸入自訂店名 `Velvet Brow Studio` 後，AI 回覆泡泡（`.bubble--out`）均包含 `Velvet Brow Studio`，且 `textContent`-only 測試輸入 `<img src=x onerror=alert(1)>` 時 DOM 新增元素數 `=== 0`。 | Playwright 斷言 |
| **G3** | **自訂店名按鈕狀態誠實** | 輸入自訂店名後，`.salon-pill.is-active` 數量 `=== 0`；點回任一預設按鈕後，該按鈕 `.is-active` 數量 `=== 1` 且三間店對應服務價格各異（`HK$280` / `HK$680` / `HK$520`）。 | Playwright 斷言 |
| **G4** | **三渠道外觀與日曆一致** | `WhatsApp` 顯示 `WA`＋綠點＋`✓✓`＋`Confirmed via WhatsApp`；`Instagram` 顯示 `@slug`＋`DM`＋`.story-reply-card`＋深炭黑回覆框＋`Confirmed via Instagram`；`Website` 顯示 `.web-url-bar` (`<slug>.hk/services`)＋`.web-context-banner`＋`Confirmed via Website`。 | Playwright 斷言 + 視覺檢視 3 張截圖 |
| **G5** | **Checkout 零邏輯矛盾** | (1) 切換店名時 `#coSalon` 與 `#coEmail` 同步更新（未手動編輯前）；(2) 選 `Annual` 自動切 `FPS`，切回 `Monthly` 自動切回 `Visa / Mastercard`；(3) 月繳狀態下點 `FPS` 會同步切為 `Annual`（絕不出現 `Monthly + FPS`）；(4) 按下啟動顯示 `HK$0` 確認畫面。 | Playwright 斷言 |
| **G6** | **線上網站零錯誤與響應式** | 針對**線上網址** `https://deskmate-ai-demo.example.com`：`index.html` / `styles.css` / `app.js` 全數 HTTP `200`；`0` console errors、`0` page errors；`375×812`、`768×1024`、`1440×900` 均滿足 `scrollWidth === innerWidth`；全部互動按鈕高 `≥ 44px`。 | Live Playwright 測試 |
| **G7** | **文案純淨度（無 AI 味）** | `wix-site/`、`Business_Plan_Updated.pdf`、`slides/*.html`、`Presentation_Script.md` 中 em-dash (`—`) 出現次數 `=== 0`，禁用詞（`delve`, `tapestry`, `seamless`, `streamline`, `leverage`, `elevate`, `game-changer`, `revolutionize`, `quiet luxury`, `whisper-soft`）出現次數 `=== 0`。 | Python regex 掃描 |
| **G8** | **Business Plan 嚴格 6 頁** | `READY_TO_UPLOAD\Author_[Student ID].pdf` 總頁數 `=== 6`：Page 1 = 封面（含 `[Author]` 與 `[Student ID]`）、Pages 2–4 = 正文 §1–§6（**嚴格 3 頁，零溢出**）、Page 5 = `References`（6 筆按字母排序 APA 7）、Page 6 = `Appendix`（含更新後 `Figure A2`）。 | `pypdf` 逐頁檢查 + 視覺讀圖 `page-1..6.png` |
| **G9** | **Business Plan 100% 純黑白** | `Business_Plan_Updated.docx` 之 `word/document.xml`、`header1.xml`、`footer1.xml` 中文字顏色集合 `=== ['000000']`，填色集合 `=== ['F2F2F2']`，邊框集合 `⊆ {'000000', 'BFBFBF'}`，字體為 `Calibri`。 | Python XML 稽核 |
| **G10** | **PPTX 嚴格 6 頁與互動熱區** | `READY_TO_UPLOAD\Author_[Student ID].pptx` 共 `6` 張投影片、6 組 Alt Text、Slide 5 共 `6` 個指向 live Wix 網址之點擊熱區；Speaker Notes 與 `Presentation_Script.md` 逐字一致，朗讀字數 `≤ 390 words`。 | `python-pptx` 稽核 + 視覺讀圖 `05-prototype.png` |
| **G11** | **跨檔數字 100% 一致** | PDF、PPTX、講稿與 Wix 網站的 `HK$388/788/1,488`、`HK$43.10`、`HK$4,482`、`82%`、`HK$400,000`、`122%`、`24 Pro salons / Month 5`、`60 salons / HK$47,280 / 2.6×` 與 Table 5 檔案 KB 數完全吻合。 | 交叉稽核腳本 |
| **G12** | **Blackboard 檔名與雜湊確認** | `./READY_TO_UPLOAD\` 內僅包含最新且 SHA-256 與 `submission\` 一致的 `Author_[Student ID].pdf` 與 `Author_[Student ID].pptx`，且回覆末尾單獨列出 Live Wix URL 與 Dashboard URL。 | `Get-FileHash` 比對 |
