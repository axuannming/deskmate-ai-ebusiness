# DeskMate AI 品味規格書（Taste Spec, Opus 5.5）

> 角色：獨立 Art & Editorial Taste Director（唯讀審查）。本文件是 Round-2 執行工人的唯一品味標準。
> 已檢查：humanizer SKILL.md、6 張 Wix 截圖、`wix-site/index.html`（標題與文案）、`styles.css` tokens、Slide 1-6、BP page 2 與 4、`build_business_plan_v2.py`、`Presentation_Script.md`。
> 鎖定決策：Direction 2 色票（Warm Stone `#F8F6F1`、Deep Charcoal `#1F1E1C`、Champagne Bronze `#7C5C34`）不變；只提升工藝，不換風格。

---

## 1. 甚麼是 Apple 級暖調奢華品味（What Defines Apple-Tier Warm Luxury Taste）

### 1.1 核心原則（一句話）
**少一個元素，比多一個元素更貴。** 每個畫面只有一個焦點，一個 bronze 重點色，一種動作。品味來自比例、留白、字距、物理感動效，而不是裝飾。

### 1.2 字體層級（保留現有 `Newsreader` + `Inter` + `Noto Sans TC`，只調比例）

| 層級 | 字體 / 字重 | 尺寸 | 行高 / 字距 | 用途 |
|---|---|---|---|---|
| Display H1 | Newsreader 400（不可 bold） | `clamp(48px, 7vw, 88px)` | `1.02` / `-0.025em` | Hero 一句話 |
| H2 | Newsreader 400 | `clamp(34px, 4.4vw, 56px)` | `1.08` / `-0.02em` | Section 標題 |
| H3 | Newsreader 400 | `24px` 至 `30px` | `1.2` / `-0.01em` | 卡片、方案名稱 |
| Eyebrow | Inter 500，全大寫 | `12px` | `1.4` / `0.14em` | 每個 section 最多一個，bronze |
| Body | Inter 400 | `17px`（Apple 標準） | `1.6` / `0` | 段落，`max-width: 62ch` |
| Meta / 註腳 | Inter 400 | `13px` | `1.5` / `0.005em` | "Illustrative"、"Sample" 標籤 |
| 中文 | Noto Sans TC 400 | 同 Body | `1.75` | 廣東話對話 |

必須加入：
```css
.plan-price, .slot-time, .sum-row, .stat-val { font-variant-numeric: tabular-nums; }
h1, h2 { text-wrap: balance; }
p { text-wrap: pretty; }
```
規則：全站最多 2 個 font family（+中文 fallback）。標題一律 sentence case（"How DeskMate AI compares"，不是 "Why Salons Choose DeskMate AI"）。禁止標題 bold serif。

### 1.3 色彩與表面 tokens（加入 `styles.css` `:root`，保留現有 `--bg` 等）
```css
:root {
  /* 既有：--bg #F8F6F1, --ink #1F1E1C, --bronze #7C5C34, --line #E3DED5 */
  --glass-bg: rgba(248, 246, 241, 0.72);
  --glass-bg-solid: rgba(248, 246, 241, 0.96);   /* 無 backdrop-filter 時 fallback */
  --glass-border: rgba(31, 30, 28, 0.08);
  --bronze-tint: rgba(124, 92, 52, 0.08);         /* 鎖定 slot 底色 */
  --bronze-ring: rgba(124, 92, 52, 0.28);         /* pulse 光環起點 */
  --bubble-in: #FFFFFF;                           /* 客人訊息 */
  --bubble-out: #EFE6D8;                          /* DeskMate 回覆：暖香檳，不用 WhatsApp 綠 */
  --chat-wall: #F3EEE6;                           /* 手機聊天背景 */
  --titanium-1: #3A3835;
  --titanium-2: #1F1E1C;
  --titanium-3: #2C2A27;

  --radius-card: 20px;
  --radius-btn: 12px;
  --radius-pill: 999px;

  --shadow-1: 0 1px 2px rgba(31,30,28,.04), 0 8px 24px rgba(31,30,28,.06);
  --shadow-device: 0 48px 96px -32px rgba(31,30,28,.38), 0 16px 32px -16px rgba(31,30,28,.22);

  --ease-out: cubic-bezier(0.22, 1, 0.36, 1);       /* 進場、reveal：快起慢收 */
  --ease-standard: cubic-bezier(0.4, 0, 0.2, 1);    /* hover、顏色 */
  --ease-spring: cubic-bezier(0.34, 1.32, 0.64, 1); /* 只用於 calendar 鎖定一次輕彈 */
  --dur-fast: 160ms;   /* hover */
  --dur-press: 240ms;  /* 按下 */
  --dur-enter: 320ms;  /* 對話氣泡 */
  --dur-reveal: 700ms; /* scroll reveal */
  --dur-pulse: 900ms;  /* calendar pulse */
}
```
對比要求：`--ink-muted #5C564F` on `#F8F6F1` ≈ 6.6:1，`--bronze` 文字 ≈ 5.9:1，都過 WCAG AA。不可再引入更淺的灰字。

### 1.4 間距（8pt grid）
- Section padding：`padding-block: clamp(88px, 11vw, 144px);`
- Container：`max-width: 1200px; padding-inline: clamp(20px, 5vw, 40px);`
- 標題到副標：`16px`；副標到內容：`48px`；卡片內距：`32px`（手機 `24px`）。
- 只用 8 的倍數（4px 只限 icon 與 hairline 微調）。

### 1.5 Frosted glass sticky nav
```css
.site-header {
  position: sticky; top: 0; z-index: 50;
  background: var(--glass-bg);
  -webkit-backdrop-filter: saturate(180%) blur(20px);
  backdrop-filter: saturate(180%) blur(20px);
  border-bottom: 1px solid transparent;
  transition: border-color var(--dur-fast) var(--ease-standard), background-color var(--dur-fast) var(--ease-standard);
}
.site-header.is-scrolled { border-bottom-color: var(--glass-border); }
@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .site-header { background: var(--glass-bg-solid); }
}
```
JS：`window.scrollY > 8` 時加 `.is-scrolled`（用 `passive: true` listener 或 sentinel IntersectionObserver）。

### 1.6 Scroll reveal（克制、只一次）
```css
.js .reveal { opacity: 0; transform: translateY(16px); }
.js .reveal.is-visible {
  opacity: 1; transform: none;
  transition: opacity var(--dur-reveal) var(--ease-out), transform var(--dur-reveal) var(--ease-out);
  transition-delay: calc(var(--i, 0) * 60ms);
}
@media (prefers-reduced-motion: reduce) {
  .js .reveal { opacity: 1; transform: none; transition: none; }
}
```
- `<html>` 先由 JS 加 `class="js"`，**沒有 JS 時內容必須可見**（保證 Wix 截圖、PDF、爬蟲不出空白）。
- IntersectionObserver：`threshold: 0.15, rootMargin: '0px 0px -10% 0px'`，觸發後 `unobserve`。
- 只用在 section head、卡片群組（stagger 最多 4 個）。Hero H1 不做 reveal（首屏要即時）。

### 1.7 觸感（Tactile restraint）
```css
.btn { border-radius: var(--radius-btn); transition: background-color var(--dur-fast) var(--ease-standard), transform var(--dur-press) var(--ease-out); }
.btn:active { transform: scale(0.98); }
.btn:focus-visible, .salon-pill:focus-visible, input:focus-visible { outline: 2px solid var(--bronze); outline-offset: 3px; }
```

### 1.8 反 AI slop 規則（違反任何一條即 fail）
1. 禁止：漸層文字、紫藍漸層、glow orb、玻璃擬態卡片堆疊（glass 只用在 nav）、emoji、✨、🚀、3D 立體 icon、跑數字 counter、自動輪播。
2. 每個 viewport 只有一個 bronze 實心焦點（主 CTA 用 charcoal，bronze 只做重點文字、細線、鎖定狀態）。
3. 每個元素最多一種動畫；不做 parallax、不做 hover 放大圖片。
4. 不用 "AI-powered"、"Revolutionize"、"Seamless"、"Unlock"、"Elevate"、"Empower"、"Next-gen"、"Supercharge"。
5. 陰影只用 `--shadow-1` 與 `--shadow-device` 兩種。
6. Icon 只用 1.5px stroke 的 inline SVG（例如鎖頭），不用 icon font。
7. 所有示範內容保留誠實標籤："Illustrative"、"Sample"、"Prototype simulation"。

---

## 2. 網站工藝與自訂沙龍 iPhone Demo 規格（Website Craft & Custom-Salon iPhone Demo Spec）

### 2.1 架構（只改 `wix-site/index.html`、`styles.css`、`app.js` 三檔）
- **保留所有既有 id**：`#demo`、`#how-it-works`、`#transcriptBody`、`#calendarSlots`、`#calendarDayLabel`、`#syncStatus`、`#about`、`#fOptIn`、`#pricing`、`#checkout`、`#contact`。Slide 5 熱區與講稿依賴這些錨點。
- 保留 channel tabs（WhatsApp / Instagram / Website）與 4 個 scenario 按鈕，改為控制 iPhone 內的對話。
- 新增樣式全部加在 `styles.css` 尾段 `/* === iPhone demo === */` 區塊，不改舊規則以免回歸。
- 用戶輸入一律 `textContent`，**禁止 `innerHTML` 插入用戶字串**（XSS）。

### 2.2 HTML 結構（取代左邊 `.sheet-transcript` 的外殼，內部 id 不變）
```html
<div class="demo-workbench" id="demo">
  <div class="demo-device-col">
    <div class="personalise">
      <label for="customSalonInput" class="personalise-label">Personalise for your salon</label>
      <input id="customSalonInput" type="text" value="Lumière Nail Studio" maxlength="40"
             autocomplete="organization" spellcheck="false" aria-describedby="salonHint">
      <div class="salon-pills" role="group" aria-label="Sample salon names">
        <button type="button" class="salon-pill is-active" data-salon="Lumière Nail Studio">Lumière Nail Studio</button>
        <button type="button" class="salon-pill" data-salon="Mong Kok Hair Lab">Mong Kok Hair Lab</button>
        <button type="button" class="salon-pill" data-salon="Causeway Lash Bar">Causeway Lash Bar</button>
        <button type="button" class="salon-pill" data-salon="TST Skin Atelier">TST Skin Atelier</button>
      </div>
      <p id="salonHint" class="meta">Sample salon names. Replies are scripted examples (prototype simulation), not live AI output.</p>
    </div>

    <div class="iphone" role="img" aria-label="Prototype simulation of a salon chat on a phone">
      <span class="iphone-btn iphone-btn--action"></span>
      <span class="iphone-btn iphone-btn--vol"></span>
      <span class="iphone-btn iphone-btn--power"></span>
      <div class="iphone-screen">
        <div class="dynamic-island" aria-hidden="true"></div>
        <div class="chat-head">
          <span class="chat-avatar" id="phoneSalonInitials">LN</span>
          <div><strong id="phoneSalonName">Lumière Nail Studio</strong><span class="chat-sub" id="phoneChannel">WhatsApp · DeskMate AI</span></div>
        </div>
        <div class="chat-thread" id="transcriptBody" aria-live="polite"></div>
      </div>
    </div>
    <!-- 原有 .segmented channel tabs 與 .prompt-bar scenario 按鈕放在手機下方 -->
  </div>
  <div class="sheet sheet-calendar"> <!-- 既有日曆，保留 --> </div>
</div>
```

### 2.3 iPhone 鈦金屬 / 炭灰外框 CSS（純 CSS，不用圖片）
```css
.iphone {
  position: relative; width: 300px; aspect-ratio: 9 / 19.5;
  padding: 11px; border-radius: 54px;
  background: linear-gradient(145deg, var(--titanium-1) 0%, var(--titanium-2) 45%, var(--titanium-3) 100%);
  box-shadow: inset 0 0 0 1px rgba(255,255,255,.10), inset 0 0 0 3px #121110, var(--shadow-device);
}
.iphone-screen {
  position: relative; height: 100%; overflow: hidden;
  border-radius: 43px; background: var(--chat-wall);
  display: flex; flex-direction: column;
}
.dynamic-island {
  position: absolute; top: 10px; left: 50%; transform: translateX(-50%);
  width: 96px; height: 28px; border-radius: 20px; background: #000; z-index: 2;
}
.iphone-btn { position: absolute; width: 3px; border-radius: 2px; background: var(--titanium-1); }
.iphone-btn--action { left: -3px; top: 104px; height: 28px; }
.iphone-btn--vol    { left: -3px; top: 150px; height: 56px; box-shadow: 0 68px 0 var(--titanium-1); }
.iphone-btn--power  { right: -3px; top: 168px; height: 84px; }
.chat-head {
  display: flex; gap: 10px; align-items: center;
  padding: 52px 16px 12px; background: rgba(255,255,255,.78);
  -webkit-backdrop-filter: blur(12px); backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--glass-border); font-size: 14px;
}
.chat-avatar { width: 32px; height: 32px; border-radius: 50%; display: grid; place-items: center;
  background: var(--ink); color: var(--bg); font: 500 12px/1 var(--sans); letter-spacing: .04em; }
.chat-sub { display: block; font-size: 11px; color: var(--ink-muted); }
.chat-thread { flex: 1; overflow-y: auto; padding: 16px 12px 20px; display: flex; flex-direction: column; gap: 8px; scroll-behavior: smooth; }
.bubble { max-width: 80%; padding: 9px 12px; font-size: 14px; line-height: 1.45; border-radius: 18px;
  box-shadow: 0 1px 1px rgba(31,30,28,.06); animation: bubbleIn var(--dur-enter) var(--ease-out) both; }
.bubble--in  { align-self: flex-start; background: var(--bubble-in); border-bottom-left-radius: 6px; }
.bubble--out { align-self: flex-end;   background: var(--bubble-out); border-bottom-right-radius: 6px; }
.bubble time { display: block; margin-top: 4px; font-size: 10.5px; color: var(--ink-muted); text-align: right; }
@keyframes bubbleIn { from { opacity: 0; transform: translateY(8px) scale(.98); } to { opacity: 1; transform: none; } }
```

### 2.4 輸入框與 pills
```css
.personalise-label { font: 500 12px/1.4 var(--sans); letter-spacing: .14em; text-transform: uppercase; color: var(--bronze); }
#customSalonInput { width: 100%; height: 48px; padding: 0 16px; font-size: 16px; /* 16px 防 iOS zoom */
  border: 1px solid var(--line-strong); border-radius: var(--radius-btn); background: var(--surface); color: var(--ink);
  transition: border-color var(--dur-fast) var(--ease-standard), box-shadow var(--dur-fast) var(--ease-standard); }
#customSalonInput:focus { border-color: var(--bronze); box-shadow: 0 0 0 4px var(--bronze-tint); outline: none; }
.salon-pills { display: flex; gap: 8px; margin-top: 12px; overflow-x: auto; scroll-snap-type: x mandatory; scrollbar-width: none; }
.salon-pill { flex: none; min-height: 44px; padding: 0 16px; border-radius: var(--radius-pill); scroll-snap-align: start;
  border: 1px solid var(--line-strong); background: transparent; color: var(--ink-2); font-size: 14px; }
.salon-pill.is-active { background: var(--ink); border-color: var(--ink); color: var(--bg); }
```

### 2.5 互動時序（app.js；毫秒為準）
| t (ms) | 事件 |
|---|---|
| 0 | 觸發：pill click、Enter、或輸入停止 450ms（debounce）。`name = input.value.trim() \|\| 'Lumière Nail Studio'`；更新 `#phoneSalonName`、`#phoneSalonInitials`（取前兩個單字首字母）。 |
| 0 | 取消上一輪所有 timers（`AbortController` 或存 timeout ids），清空 thread。**連按不可疊出多組氣泡。** |
| 120 | 客人氣泡進場（`bubble--in`）。 |
| 600 | Typing 氣泡進場：三點 + `aria-label="DeskMate AI is typing"`；手機 header `#phoneChannel` 改為 `typing…`。 |
| 600 + T | T = `Math.min(1400, 700 + reply.length * 4)`，約 1.1 至 1.4 秒。Typing 氣泡以 200ms 淡出，回覆氣泡（`bubble--out`）進場。 |
| +200 | 日曆 18:30 slot 加 `.is-locking`：先顯示 "Holding 18:30"，900ms 後轉 `.is-locked`，狀態文字 "Confirmed for {name}"，加鎖頭 SVG。 |
| +200 | `#calendarDayLabel` 文字改為 `Thursday · {name} · synced across 3 channels`；`#syncStatus` 為 `Illustrative: confirmed in 0.8s`（**必須保留 Illustrative**）。 |

Typing dots：
```css
.typing { display: inline-flex; gap: 4px; padding: 12px 14px; }
.typing span { width: 6px; height: 6px; border-radius: 50%; background: var(--ink-muted); animation: dot 1.2s var(--ease-standard) infinite; }
.typing span:nth-child(2) { animation-delay: .15s; } .typing span:nth-child(3) { animation-delay: .3s; }
@keyframes dot { 0%, 60%, 100% { transform: translateY(0); opacity: .35; } 30% { transform: translateY(-3px); opacity: 1; } }
```
Calendar 鎖定回饋：
```css
.slot.is-locking { background: var(--bronze-tint); animation: lockPulse var(--dur-pulse) var(--ease-out) 1; }
.slot.is-locked  { background: var(--bronze-tint); box-shadow: inset 3px 0 0 var(--bronze); }
.slot.is-locked .slot-status { color: var(--bronze); font-weight: 500; }
@keyframes lockPulse { 0% { box-shadow: 0 0 0 0 var(--bronze-ring); } 100% { box-shadow: 0 0 0 10px rgba(124,92,52,0); } }
@media (prefers-reduced-motion: reduce) {
  .bubble, .slot.is-locking { animation: none; }
  .typing span { animation: none; opacity: .6; }
}
```
Reduced motion 時 typing 時間縮為 300ms，其餘流程不變。

### 2.6 對話文案模板（`{name}` = 沙龍名；全部 `textContent`）
**Book（預設）**
- Client（21:14）：`你好 {name}，聽日放工 6 點後有冇位整 Gel 甲？ Hi, can I book a gel manicure tomorrow after 6pm?`
- DeskMate AI（21:14）：`你好！呢度係 {name}。聽日 6:30 PM 有位，已為你預留 Gel Manicure（HK$280，60 分鐘）。Hello from {name}. Your gel manicure is booked for 6:30 PM tomorrow, and we will send a reminder at 10:00 AM.`

**Price**：`{name} 嘅價錢：Gel Manicure HK$280，Classic Facial HK$480。Gel manicure is HK$280 and a classic facial is HK$480 at {name}.`（如現有 app.js 已有其他價錢，沿用現有數字，不可新增未在網站出現的價錢。）
**Reschedule**：`已將你嘅預約改到星期五 6:30 PM。Your {name} booking has moved to Friday at 6:30 PM.`
**Handoff**：`新娘化妝需要店主親自報價，我已將你嘅要求轉交 {name} 店主，佢會盡快回覆。A bridal request needs a quote from the {name} owner, so I have passed it on with a short summary.`

### 2.7 版面與 responsive
- `≥1024px`：`grid-template-columns: minmax(320px, 380px) 1fr; gap: 64px; align-items: center;`，手機在左，日曆在右。
- `640–1023px`：單欄，手機置中 `300px`，日曆在下，`gap: 48px`。
- `<640px`：`.iphone { width: min(84vw, 300px); }`；pills 橫向滑動；channel tabs 與 scenario 按鈕全寬換行，所有 tap target `≥44px`。
- 驗收：375×812 與 1440×900 時 `document.documentElement.scrollWidth === window.innerWidth`。
- "Built on Wix Headless" 浮動徽章不可遮住主 CTA：手機版 `body { padding-bottom: 72px; }`。

### 2.8 網站文案 de-AI 修正（逐句替換）
| 位置 | Before | After |
|---|---|---|
| `<title>` | `DeskMate AI — 24/7 Bilingual AI Receptionist for Hong Kong Beauty Salons` | `DeskMate AI · 24/7 bilingual AI receptionist for Hong Kong beauty salons` |
| `.hero-lead` | `Quiet 24/7 Cantonese and English reception for independent Hong Kong beauty and hair salons — answering WhatsApp, Instagram, and web enquiries onto one shared calendar from HK$388 a month.` | `Cantonese and English reception, 24 hours a day, for independent Hong Kong beauty and hair salons. DeskMate AI answers WhatsApp, Instagram and website enquiries and books them into one shared calendar, from HK$388 a month.` |
| Hero stat | `「聽日六點後有冇位整 Gel 甲？」 — Confirmed Gel Manicure (Thu 18:30, HK$280)` | `「聽日六點後有冇位整 Gel 甲？」 Booked: Gel Manicure, Thu 18:30, HK$280` |
| How it works sub | `Try the interactive booking flow below to see how DeskMate AI handles real Hong Kong Cantonese and English enquiries and locks slots onto one shared salon calendar.` | `Type your salon's name and watch a sample Cantonese and English booking land on the shared salon calendar.` |
| `.sheet-meta` | `Illustrative conversation flow — Cantonese & English` | `Illustrative conversation in Cantonese and English` |
| `#calendarDayLabel` | `Thursday — Auto-synced across 3 channels` | `Thursday · synced across 3 channels` |
| 日曆 slot | `Gel Manicure — HK$280` | `Gel Manicure · HK$280` |
| 舊 AI 回覆 | `…confirmed on our salon calendar — I will send a reminder at 10:00 AM.` | 用 2.6 模板（兩句，無破折號） |
| Pricing sub | `Predictable B2B Fee-for-Service pricing — no per-booking commissions. Every plan starts…` | `Fixed monthly B2B Fee-for-Service pricing with no per-booking commission. Every plan starts with a 14-day free trial and done-for-you onboarding.` |
| Checkout sub | `Interactive Checkout Prototype — demonstrates plan selection, HK$0 trial activation, and Hong Kong payment methods (cards, mobile wallets, FPS) without real billing.` | `Choose a plan, activate the HK$0 trial and see the Hong Kong payment methods (cards, mobile wallets and FPS). No payment is taken.` |
| `.sim-notice` | `Simulated Checkout Mock-up (Hosted on Wix Headless) — Demonstrates plan selection, HK$0 trial activation & payment methods safely on a free plan without real billing.` | `Prototype simulation hosted on Wix Headless. This mock-up takes no payment and stores no card details.` |
| Plan radios | `Starter — HK$388/mo` 等三個 | `Starter · HK$388/mo`、`Pro · HK$788/mo`、`Premium · HK$1,488/mo` |
| `#confirmCheckoutBtn` | `Activate 14-Day Free Trial — Pay HK$0 Today` | `Activate 14-day free trial · HK$0 today`（**講稿第 3 步同步修改**） |
| Testimonial | `Mei-Ling C. — Independent Nail & Facial Studio, Causeway Bay (Sample testimonial — illustrative prototype copy)` | `Mei-Ling C., independent nail and facial studio, Causeway Bay (Sample testimonial, illustrative prototype copy)` |
| FAQ (Meta) | `General tools leave setup to busy salon owners and live inside a single channel. DeskMate AI includes done-for-you onboarding … — and syncs WhatsApp, Instagram D…` | `General tools leave setup to the salon owner and usually cover one channel. We set up your Hong Kong treatment menu, prices and hours for you, and DeskMate AI keeps WhatsApp, Instagram DM and website chat on one calendar.` |
| FAQ (PDPO) | `…data minimisation principles — storing only the booking details needed…` | `…data minimisation principles. We store only the booking details needed to confirm appointments and send reminders, on encrypted managed cloud infrastructure.` |
| Updates rows | `Nov 2026 — Instagram DM shared-calendar sync and …` | 日期放獨立欄（`display:grid; grid-template-columns: 88px 1fr`），文字：`Instagram DM now syncs to the shared calendar; the HK$0 14-day trial checkout prototype is live.` / `Oct 2026` `Cantonese and English menu templates for nail, facial and lash treatments released for Hong Kong salons.` |
| `.pdpo-note` | `…used solely to arrange your walkthrough and — only if ticked above — to send opt-in updates under Hong Kong PDP…` | `Prototype simulation: no data is transmitted. In the live service, we use your details only to arrange your walkthrough and, if you tick the box above, to send updates under Hong Kong's PDPO. You can opt out at any time.` |
| Footer | `SEHS2265 E-Business Prototype (Wix Headless + Wix Media CDN) — Individual Portfolio Author` | `SEHS2265 E-Business prototype (Wix Headless + Wix Media CDN) · Individual Portfolio Author` |

保持不變（已經好）：H1 `Your hands stay with the client.`、`Built for independent salon economics.`、`Starting with Hong Kong beauty salons, built to expand.`、`Transparent monthly plans.`、`Book a 1-to-1 personal demo.`、`#fOptIn` 保持**未勾選**。

---

## 3. 正式 de-AI 文案改寫（Humanizer + Schneider 2017 課本對齊）

原則：只刪 AI 痕跡（§8 破折號、§6 硬湊三件、§15 `-ing` 尾巴、§12 AI 詞、§18 `serves as`/`features`、§20 Title Case），保留正式商業計劃書語氣。**每個課本術語與數字一字不改**。所有 BP 改寫長度相等或更短（page 4 底部尚有約 25% 空白，安全）。

### 3.1 Business Plan（`build_business_plan_v2.py`）
| # | 行 | Before | After | 依據 |
|---|---|---|---|---|
| B1 | L49 header | `DeskMate AI — E-Business Start-up Plan (SEHS2265)   \|   Individual Portfolio Author` | `DeskMate AI: E-Business Start-up Plan (SEHS2265)   \|   Individual Portfolio Author` | §8 |
| B2 | L317 cover lead | `An E-Business Start-up Plan presenting DeskMate AI's B2B Fee-for-Service model, …` | `This e-business start-up plan sets out DeskMate AI's B2B Fee-for-Service model, …`（其餘照舊） | §25 |
| B3 | L332 | `SEHS2265 E-Business  —  Miss Janice Au (Sem 1, 2026/27)` | `SEHS2265 E-Business, Miss Janice Au (Semester 1, 2026/27)` | §8 |
| B4 | L370 | `Document Structure: Main body strictly 3 pages (Pages 2–4), excluding this Cover Page, APA 7 References (Page 5), and Live Wix Prototype Screenshots Appendix (Page 6).` | `Main body: pages 2 to 4. The cover, APA 7 references (page 5) and the appendix of live Wix prototype screenshots (page 6) are excluded.` | §8, §20 |
| B5 | L393 | `DeskMate AI serves owner-operated salons that handle enquiries through messaging.` | `DeskMate AI's customers are owner-operated salons that take enquiries through messaging apps.` | §18 |
| B6 | L431-434 | `Each plan includes a time-limited 14-day free trial (HK$0 due today) as a low-friction onboarding pathway — distinct from a permanent freemium tier — allowing owners to verify the bilingual booking workflow before paid billing begins, tracked by trial-to-paid conversion rate.` | `Each plan starts with a time-limited 14-day free trial (HK$0 due today), which is distinct from a permanent freemium tier. Owners test the bilingual booking workflow before billing begins, and we track the trial-to-paid conversion rate.` | §8, §15 |
| B7 | L454 + L457 | 兩個 bullet 同名：`Open a new market:` 與 `Open new markets:` | 第一個改為 `Increase sales:`（60 salons），第四個保留 `Open new markets:`（clinics, tutorial centres）。執行者須對照 Figure 12-1 原文標籤；若課本標籤為 "Increase sales in existing markets" 則用原文。 | 邏輯重複，評分者會扣分 |
| B8 | L455 | `Enhance marketing:` | 若是 Figure 12-1 原文標籤則**保留**（課本術語優先於 humanizer 詞表）；否則改 `Improve marketing:` | §12 例外 |
| B9 | L522 Mobile | `…with slide-down mobile menu and zero horizontal overflow (Figure A6).` | `…with a slide-down mobile menu and no horizontal scrolling (Figure A6).` | 去技術腔 |
| B10 | L523 Fast loading | `Hand-coded static pages (~63 KB HTML/CSS/JS, no page-builder bloat) with salon photography served via Wix Media CDN edge servers.` | `Hand-coded static pages (about {N} KB of HTML, CSS and JS) with salon photographs served from Wix Media CDN edge servers.` **{N} 必須用重建後三檔實際大小重算**（目前三檔合計 ≈ 70.5 KB，與 "63 KB" 已不符）。 | 數字誠實、去口語 "bloat" |
| B11 | L524 Two-way | `Interactive Cantonese/English booking simulator plus a validated one-to-one 'Book a Demo' form, meeting Schneider's (2017) two-way communication accessibility goal (Figures A2, A5).` | `A Cantonese and English booking simulation that uses the visitor's salon name, and a validated one-to-one 'Book a Demo' form, provide two-way communication (Schneider, 2017) (Figures A2, A5).` | §15 |
| B12 | L526 Trust | `…honest 'Simulated Checkout' notice, opt-in only updates and PDPO opt-out; higher trust builds loyalty (a 5% loyalty lift can raise profit 25%–80%; Schneider, 2017, Chapter 3).` | `…a 'Prototype simulation' checkout notice, opt-in updates and PDPO opt-out. Trust supports loyalty: a 5% rise in loyalty can raise profit by 25% to 80% (Schneider, 2017, Chapter 3).` | 數字保留 |
| B13 | L533-535 | `…a three-tier client–Web–database design on managed cloud (PaaS), serverless functions and a Content Delivery Network (CDN) meets Schneider's (2017, Chapter 12) six hosting criteria — functionality, reliability, scalability, security, backup and cost (Table 6).` | `…a three-tier design (client, Web server and database) on managed cloud (PaaS), with serverless functions and a Content Delivery Network (CDN), meets the six hosting criteria in Schneider (2017, Chapter 12): functionality, reliability, scalability, security, backup and cost (Table 6).` | §8 |
| B14 | L509 | `opt-in performance reports (permission marketing, avoiding unsolicited commercial e-mail)` | `opt-in performance reports (permission marketing, with no unsolicited commercial e-mail)` | §15 |
| B15 | L581 | `within the 50%–200% TCO range` | `within the 50% to 200% TCO range`（表格內數字範圍可保留 en dash） | §8 |
| B16 | L678-692 captions | `Figure A1. Live Wix Homepage & Clear 6-Link Navigation (Desktop 1440×900)` 等 | A1 `Figure A1. Live Wix homepage with six-link navigation (desktop, 1440×900)`；A2 `Figure A2. Booking simulation in a phone frame, personalised with a salon name, and the shared calendar`；A3 `Figure A3. B2B Fee-for-Service plans (Starter, Pro, Premium) with a 14-day trial`；A4 `Figure A4. Simulated checkout (HK$0 today; cards, wallets and FPS)`；A5 `Figure A5. One-to-one demo form, About facts, opt-in checkbox and PDPO notice`；A6 `Figure A6. Mobile layout (375×812)` | §20, §16 去 "Safe"/"Verified"/"Zero Overflow" |

BP 不需修改（已達標，保留）：Executive Summary 全段、2.2 `Our customers are salons, not consumers` 這個對比更正了真實誤解（B2B vs B2C），符合 §1 例外、Table 3 behavioural 行的 browsers/shoppers/buyers、Section 4 CRLC 全段、Financial Plan 最後一段（opportunity cost、ROI 限制、10/10/80、24 salons、HK$47,280、2.6×）。

### 3.2 Slides（`DeskMate_AI_Presentation.pptx`）
| Slide | Before | After |
|---|---|---|
| 1 標題 | `Quiet reception while your hands stay with the client.` | `Your hands stay with the client.`（與網站 H1 一致；去 "Quiet"） |
| 1 副標 | `24/7 Cantonese and English AI receptionist for independent Hong Kong beauty and hair salons — unifying WhatsApp, Instagram, and website bookings into one calm schedule.` | `A 24/7 Cantonese and English AI receptionist for independent Hong Kong beauty and hair salons. It books WhatsApp, Instagram and website enquiries into one shared calendar.` |
| 1 頁首 | `SEHS2265 E-Business — Live Prototype: headless-…` | `SEHS2265 E-Business · Live prototype: headless-…` |
| 2 標題 | `Missed bookings, solved at 82% lower cost.` | `Missed enquiries answered for 82% less than part-time reception.` |
| 2 小標 | `The Salon Owner's Dilemma` | `The problem` |
| 2 內文 | `Salons pay a predictable monthly subscription with zero per-booking commission — plus a time-limited 14-day trial (not a permanent freemium tier) and done-for-you menu onboarding.`（含 bold 裝飾） | `Salons pay a predictable monthly subscription with no per-booking commission. A time-limited 14-day trial, distinct from a permanent freemium tier, comes with done-for-you menu onboarding.`（移除內文 bold） |
| 2 版面 | 標題下方空白過大，內容偏下 | 內容區垂直置中，上下留白相等 |
| 3 右上 | `CRLC — Target: Awareness & Exploration` | `CRLC · Target: Awareness & Exploration` |
| 3 小標 | `Why Salons Choose DeskMate AI` | `How DeskMate AI compares` |
| 3 註腳 | `Framework: Schneider (2017) — Launch focus: Awareness & Exploration` | `Framework: Schneider (2017) · Launch focus: Awareness & Exploration` |
| 3 Stage 5 | `Separation` + `No ads targeted; exit check & PDPO opt-out honoured.` | **不改**（rubric gate） |
| 4 標題 | `Three channels, one cloud engine, no double-bookings by design.`（§6 硬湊三件） | `WhatsApp, Instagram and web chat share one engine and one calendar.` |
| 4 左欄 | `WhatsApp Business — primary HK booking channel` 等三行 | `WhatsApp Business: main HK booking channel`、`Instagram DM: salon discovery traffic`、`Salon website chat: direct search enquiries` |
| 4 左欄小標 | `Omnichannel Intake` | `Enquiries in` |
| 4 中欄 | `CDN & 5G Connectivity fast real-time mobile replies (6 hosting criteria)`（文法斷裂） | `CDN and 5G give fast mobile replies; the stack meets the six hosting criteria.` |
| 5 Step 2 | `Gel Manicure (18:30, HK$280) live chat`（"live chat" 不誠實） | `Personalised salon chat simulation (18:30, HK$280)` |
| 5 截圖 | 舊版 demo | 網站重建後重截 desktop、mobile 縮圖（可選，若時間允許） |
| 6 右下 | `Thank You — Questions Welcome` | `Thank you. Questions welcome.` |
| 6 底部 | `…(Schneider 50%–200%); labour-led (10/10/80 pattern).` | `…(Schneider: 50% to 200%); mostly labour (10/10/80 pattern).` |

### 3.3 `Presentation_Script.md`（並同步 PPTX Speaker Notes）
| 位置 | Before | After |
|---|---|---|
| Row 2 尾句 | `This is B2B e-commerce on a Fee-for-Service model: a predictable monthly fee, no per-booking commission, and a 14-day trial rather than a freemium tier.` | `This is B2B e-commerce on a Fee-for-Service model. Salons pay a predictable monthly fee with no per-booking commission, and the 14-day trial is time limited, so it is not a freemium tier.` |
| Row 5（配合新 demo） | `In the booking example, a client asks in Cantonese for a gel manicure after six; the assistant confirms six-thirty and the shared calendar updates.` | `In the booking demo, I type a salon name, Lumière Nail Studio. A client asks in Cantonese for a gel manicure after six, DeskMate AI replies in that salon's name and books six-thirty, and the shared calendar marks the slot.` |
| Row 5 尾句 | `…the Book a Demo form is our one-to-one touchpoint, with a PDPO notice.` | `…the Book a Demo form is our one-to-one touchpoint, with an unticked opt-in box and a PDPO notice.` |
| 點擊步驟 3 | `按 Activate 14-Day Free Trial — Pay HK$0 Today` | `按 Activate 14-day free trial · HK$0 today`（與網站按鈕一致） |
| 點擊步驟 2 | `展示廣東話／英文 Gel Manicure…模擬與右側共享行事曆即時更新` | `輸入沙龍名（或點 preset pill），展示 typing 動畫、以該沙龍名回覆的廣東話／英文訊息，以及共享行事曆鎖定 18:30` |
| Q1 | `Meta's tool is WhatsApp-centric and self-configured by the merchant (and public coverage does not confirm Cantonese salon readiness in Hong Kong).` | `Meta's tool centres on WhatsApp and the merchant configures it. Meta's announcement does not say whether it is set up for Cantonese salon bookings in Hong Kong.` |
| Q2 標題 | `…on Wix Headless — why not live billing?` | `…on Wix Headless. Why not live billing?` |
| Q2 | `…demonstrate the entire workflow safely on a free Wix plan without real billing.` | `…show the whole workflow on a free Wix plan without real billing.` |
| Q6 | `That is our key external threat in our SWOT analysis.` | `It is the main external threat in our SWOT analysis.` |

講稿總字數須維持 ≤ 400 字（現 347 字；Row 5 約 +20 字，仍在 60 秒 demo 內）。

---

## 4. 客觀 Pass/Fail 品味與品質驗收表（目標 ≥ 96/100）

任何一項 Fail 即扣該項全部分數。T12、T13、T14 是**硬門檻**：任一 Fail，總分不論多少都視為不合格。

| # | 範疇 | 驗收條件（可客觀檢查） | 分數 |
|---|---|---|---|
| T1 | Website Craft | Nav `position: sticky` + `backdrop-filter: saturate(180%) blur(20px)` + `@supports` fallback；捲動 >8px 後出現 hairline border。 | 5 |
| T2 | Website Craft | 字級符合 1.2 表；H1/H2 為 Newsreader 400；價錢與時間 `tabular-nums`；全站 ≤2 個 font family；標題全為 sentence case。 | 5 |
| T3 | Website Craft | 動效只用 1.3 的三條 cubic-bezier；reveal 只觸發一次；`prefers-reduced-motion` 生效；停用 JS 時所有內容可見（`.js` gating）。 | 6 |
| T4 | Website Craft | 375×812、768×1024、1440×900 下 `scrollWidth === innerWidth`；tap target ≥44px；`#customSalonInput` font-size 16px；Wix 徽章不遮主 CTA。 | 7 |
| T5 | Interactive Wow | iPhone 純 CSS 外框：鈦金屬漸層、dynamic island、3 個側鍵、`--shadow-device`；圓角 54/43px；無外部圖片。 | 7 |
| T6 | Interactive Wow | `id="customSalonInput"` 存在，預設 `Lumière Nail Studio`，`maxlength="40"`，≥4 個 preset pills 並有 "Sample salon names" 標註；空白輸入回退預設；以 `textContent` 插入（輸入 `<b>x</b>` 顯示為純文字）。 | 8 |
| T7 | Interactive Wow | 時序：客人氣泡 120ms、typing 600ms、回覆在 1.1 至 1.4 秒後出現；三點動畫 1.2s；快速連點 5 個 pills 後 thread 只剩一組對話。 | 8 |
| T8 | Interactive Wow | 回覆後 18:30 slot 出現 bronze pulse（900ms、一次）與鎖頭，狀態 `Confirmed for {name}`；`#calendarDayLabel` 含沙龍名；`#syncStatus` 保留 "Illustrative"；`aria-live` 宣讀回覆。 | 7 |
| T9 | Humanizer | 所有可見文字（網站、BP、Slides、講稿英文）`—` 數量 = 0；`–` 只在表格數字範圍或專有名詞內；code/URL 除外。 | 8 |
| T10 | Humanizer | 可見文字 grep 為 0：`quietly`、`Quiet`（形容服務時）、`seamless`、`showcase`、`elevate`、`unlock`、`empower`、`robust`、`crucial`、`delve`、`leverage`、`cutting-edge`、`serves as`、`boasts`、`low-friction`、`bloat`、`key`（形容詞）；`Enhance` 只可作為 Figure 12-1 原文標籤。 | 6 |
| T11 | Humanizer | BP 正式語氣：無縮寫（don't、we're）、無口語、無 "Let's"、無一句收尾金句；講稿口語縮寫（I'm、I'll）可保留。 | 4 |
| T12 | Slide & BP Editorial（硬門檻） | BP 由 DOCX 轉 PDF 後正文只在第 2 至 4 頁（References 第 5 頁、Appendix 第 6 頁）；PPTX 正好 6 張；講稿 ≤400 字且 ≤3:00；Business objectives 無重複標籤（B7）；Slide 4 標題無三件套。 | 8 |
| T13 | Rubric Integrity（硬門檻） | `#about`（Fig 3-7 goal 1）、"Latest Platform Updates"（Fig 3-5）、`#fOptIn` 未預勾、PDPO opt-out 句、"Sample"、"Illustrative"、"Prototype simulation" 標籤全部存在；Slide 3 Stage 5 = Separation，Awareness 與 Exploration 標 "Target"；Slide 5 不再稱 "live chat"。 | 8 |
| T14 | Textbook Integrity（硬門檻） | 下列術語與數字全部仍在（見清單），數值逐一比對無變動。 | 8 |
| T15 | 跨交付物一致 | 網站按鈕文字 = 講稿點擊步驟；Slide 5 步驟名稱 = 網站錨點；BP Figure A2 caption 描述新 iPhone demo；BP "{N} KB" = 重建後 `index.html + styles.css + app.js` 實際大小（四捨五入）；附錄截圖為重建後重新擷取。 | 5 |
| | | **合計** | **100** |

### T14 課本術語清單（必須全部保留）
B2B e-commerce；Fee-for-Service vs Fee-for-Transaction；freemium（"free for many, fee for a few"）；market segmentation：geographic、demographic、psychographic、behavioural；browsers、shoppers、buyers；virtual space；customer relationship life cycle 五階段（awareness、exploration、familiarity、commitment、separation）；mass media → Web (many-to-one) → one-to-one；acquisition / conversion / retention cost；touchpoint consistency；permission marketing；unsolicited commercial e-mail；PDPO；downstream strategy；Figure 12-1；intangible benefits；conversion-to-buyer rate；Web site usability；two-way communication；three-tier；cloud computing (PaaS)；serverless computing；CDN；5G；IoT 與 microservers（不採用的理由）；six hosting criteria；Visa / Mastercard；Apple Pay / Google Pay；FPS；PCI DSS；tokenise；total cost of ownership (TCO)；50% 至 200%；10% hardware / 10% software / 80% labour；angel investors；opportunity cost；ROI 的限制（全部換算為金錢、偏重短期）；loyalty 5% → profit 25% 至 80%；APA 7 references（6 條，字母排序）。

### T14 數字清單（逐一比對）
HK$388 / HK$788 / HK$1,488；HK$43.10；HK$4,482；82%；300 / 1,000 conversations；60 salons in 12 months；25% trial-to-paid；<5% monthly churn；10 clinics or tutorial centres by month 18；US$109；60,000 conversations；FPS annual 10% off；HK$400,000 = 180,000 + 60,000 + 120,000 + 40,000；HK$220,000；122%；24 Pro salons；HK$18,333；month 5；5 new salons a month；HK$47,280；2.6×；14-day trial；HK$0 today；18:30；HK$280；10:00 AM reminder。

### 評分方法
1. Round-3 審查者逐項打 Pass/Fail，Fail 項分數為 0。
2. 合計 ≥96 且 T12、T13、T14 全 Pass，才可提交。
3. 自動檢查建議（唯讀）：
```powershell
Select-String -Path wix-site\index.html,wix-site\app.js -Pattern '—' | Measure-Object   # T9 期望 0（註解內除外）
Select-String -Path wix-site\index.html -Pattern 'id="customSalonInput"','id="fOptIn"','id="about"','Latest Platform Updates','Prototype simulation' # T6/T13
(Get-Item wix-site\index.html,wix-site\styles.css,wix-site\app.js | Measure-Object Length -Sum).Sum / 1KB  # T15 KB
```
`#fOptIn` 標籤內不可出現 `checked` 屬性。
