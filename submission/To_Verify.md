# 交件前最終核對清單（2026-11-20 最終品味升級版）

## 最新交件狀態（已完成 Opus 5.5 審核＋品味規格升級＋全面去 AI 化）

- **Business Plan（40%）**：[Business_Plan_Updated.pdf](Business_Plan_Updated.pdf)（與原始檔 [Business_Plan_Updated.docx](Business_Plan_Updated.docx)）採 Direction 2 暖石黑銅編輯排版，共 **6 頁**：封面（p1，含姓名 [Author]、學號 [Student ID] 與可點擊 Live Wix 連結）＋**正文嚴格 3 頁（p2–p4）**＋按字母排序之 APA 7 參考文獻（p5）＋新版 Live Wix 實景截圖附錄 Figures A1–A6（p6）。已移除所有破折號（`—`）與 AI 套話，修正 §2.4 業務目標避免標籤重複（Increase sales / Enhance marketing programs / Serve existing customers better / Open new markets），並將靜態程式碼大小同步為實測 `about 94 KB`。
- **Live Wix Headless 原型（40%）**：`https://deskmate-ai-demo.example.com`（HTTP 200；實測線上未壓縮程式碼 94.46 KB / 96,728 B，約 94 KB；照片託管於 Wix Media CDN；375×812、768×1024 與 1440×900 均零水平捲動、零 JS 錯誤）。升級至 Apple 級暖調奢華工藝：毛玻璃固定導覽列、純 CSS 鈦金屬 iPhone 實機框與自訂沙龍名互動模擬（預設 `Lumière Nail Studio`＋4 個 preset pills＋typing 動畫＋18:30 bronze pulse 日曆鎖定＋`textContent` 防 XSS）、About DeskMate AI（Fig 3-7 goal 1）、Latest Platform Updates（Fig 3-5 return visits）、預設不勾選的 Permission Marketing opt-in 與 PDPO opt-out、以及誠實標示前端模擬的 HK$0 結帳與聯絡表單。
- **6 頁簡報與 3 分鐘講稿（20%）**：[DeskMate_AI_Presentation.pptx](DeskMate_AI_Presentation.pptx)（與 [DeskMate_AI_Presentation.pdf](DeskMate_AI_Presentation.pdf)）共 6 頁；Slide 1 標題與網站一致（`Your hands stay with the client.`）；Slide 2 垂直置中且移除裝飾粗體；Slide 3 保留 Schneider CRLC 第 5 階段 **Separation**、目標階段 **Awareness & Exploration** 與已驗證競品定價 `SleekFlow Pro from US$109/mo annual`；Slide 4 單行標題無強制三件套；Slide 5 換上新版 Wix 實拍縮圖、將 Step 2 誠實標示為 `Personalised salon chat simulation (18:30, HK$280)` 並保留 6 個可點擊即時示範熱區（首頁×2、`#demo`、`#pricing`、`#checkout`、`#contact`）；全部 6 頁具無障礙 Alt Text，並與 [Presentation_Script.md](Presentation_Script.md)（376 字，約 3 分鐘含 60 秒現場操作）100% 逐字同步。
- **目錄清理**：所有舊版草稿均已移至 `./archive\`，避免上傳錯檔。
- **獨立審核與品味規格**：詳見 [Audit_Report_Opus55.md](Audit_Report_Opus55.md) 與 [Taste_Spec_Opus55.md](Taste_Spec_Opus55.md)。

---

## 提交前你本人必須確認的最後 3 件事

- [x] 商業計劃封面填妥姓名（[Author]）、學號（[Student ID]）與可點擊 Live Wix 連結
- [x] PDF 正文嚴格維持 3 頁（封面、References、附錄截圖不計入正文頁數）
- [x] 簡報嚴格 6 頁、講稿 376 字與 PPTX 備忘稿 100% 逐字同步、全部 6 張附錄與 Slide 5 截圖皆為新版 Live Wix 實拍
- [x] 全部交付物零破折號（`—`）、零 AI 禁詞，且所有 Schneider (2017) 課本概念與跨檔數字 100% 一致
- [x] 舊版草稿已移出 `submission/` 資料夾（僅上傳 `Business_Plan_Updated.pdf`、`DeskMate_AI_Presentation.pptx` 與 Wix 連結）
- [ ] **確認課程／PolyU HKCC 對使用 AI 工具的申報規定**：若 Miss Janice 或課程指引要求附上 AI-use declaration，請在上傳前於封面或 References 後補上一行聲明。
- [ ] **親自測試一次 Live Demo 流程**（開 `DeskMate_AI_Presentation.pptx` Slide 5，依序點擊 Home → Booking Example 輸入沙龍名或點 preset pill 展示 iPhone 模擬與日曆鎖定 → Plans / Checkout 點 `Activate 14-day free trial · HK$0 today` → Book a Demo 展示未勾選 opt-in 與 PDPO）。
- [ ] **熟讀 376 字講稿與 Q&A**（特別是：為何採 Fee-for-Service 而非 Fee-for-Transaction、為何限時 14 天試用不等於永久 freemium、TCO 122% 與 24 間店損益兩平、以及為何 Wix 免費方案以誠實模擬呈現結帳）。

---

## 數據與來源速查（已全面核對）

| 項目 | 數值／內容 | 來源／依據 |
|---|---|---|
| 香港法定最低工資 | HK$43.10/hr（2026-05-01 起） | [Labour Department (2026)](https://www.labour.gov.hk/common/public/pdf/smw/Concise_Guide_2026_Eng.pdf) |
| 兼職接待估算基準 | HK$4,482/mo（43.10 × 4 hr × 26 days） | 依最低工資估算；Pro HK$788 節省 82% |
| 競品公開資料 | Meta Business Agent (2026)；SleekFlow Pro from US$109/mo annual；Wati automation | [Meta](https://about.fb.com/news/2026/06/meta-business-agent/) · [SleekFlow](https://sleekflow.io/en-us/pricing) · [Wati](https://www.wati.io/pricing/) |
| 香港線上支付依據 | Cards & digital wallets widely used；FPS 免手續費年繳 9 折 | [Stripe (en-hk)](https://stripe.com/en-hk/resources/more/payments-in-hong-kong) |
| 靜態網站程式碼大小 | 約 94 KB（線上實測 94.46 KB / 96,728 B；本機 94.28 KB / 96,539 B） | `index.html + styles.css + app.js` 未壓縮總和 |
| 財務與損益兩平 | Seed HK$400k（開發 180k＋營運 220k = 122% TCO）；24 間 Pro 店損益兩平（~第 5 個月）；60 間 Pro 店月收 HK$47,280（2.6× 月營運成本 HK$18,333） | 依 Schneider (2017) Ch.12 TCO（50% to 200%、10/10/80 人力結構）推算 |
| 虛構示意資料（已誠實標示） | Gel manicure HK$280 對話、Sample salon names、Sample testimonial、Illustrative 0.8s sync、Prototype simulation HK$0 checkout | 網站、BP 與簡報皆明確標示為示意／模擬 |
