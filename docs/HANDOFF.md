# DeskMate AI｜SEHS2265 作業交接

**更新日期：2026 年 11 月 19 日。** 使用者已要求暫停 Wix 和交件成品的修改。這份交接只記錄進度。等使用者交代恢復後，先處理 **Wix 結帳示範**。

**交件截止：2026 年 11 月 20 日 23:59（香港時間）。** 繳交英文商業計劃 PDF、PPT 和可展示的 Wix 網址。個人報告在 11 月 23 日或 30 日的 tutorial 進行，限 3 分鐘，包含網站示範。確切場次以課堂安排為準。[作業原文](SEHS2265%20Individual%20Assignment%20Two%20Instruction.pdf)

## 目前做到哪裡

| 交付物 | 已完成及驗證 | 仍待完成 |
| --- | --- | --- |
| 商業計劃 | PDF 共 5 頁，包含封面、3 頁英文正文和參考資料。已核對封面姓名、學號及作業要求的主要章節。封面已有 Wix 網址。 | 修正 §2.3 的試用描述。按本專案標準補網站截圖，再匯出並核對 PDF。 |
| Wix 原型 | DeskMate AI 主站已發布。先前已開啟首頁、預約示範、定價頁和聯絡表單。手機首頁的選單及主要按鈕已在編輯器檢查。定價顯示 Starter HK$388、Pro HK$788、Premium HK$1,488，均為月費及 14 天試用。 | 官網缺可展示的結帳路徑。其他重點頁的手機畫面、訪客可達性和表單送出結果仍待驗證。 |
| 結帳設計 | 用 huashu-design 3.3.0 做出三個可點擊 HTML 初稿。已在 1440 × 900 和 375 × 812 測過三個方案、更新月費、模擬確認及返回。Wixel 配圖已存入原站的 Wix 媒體庫。 | 初稿待選，結帳示範尚未加入原站或發布。 |
| 簡報 | 最新版為 6 頁可編輯 PPTX。已核對封面姓名、學號和 6 頁講者備忘稿。第 5 頁有首頁、預約示範、定價和聯絡表單四個 Wix 連結。 | 加入結帳展示步驟和可用連結，更新講稿，另存截圖作現場備案。實際計時排練尚待完成。 |

目前有 **3 項收尾工作**（Wix、商業計劃、簡報），另有正式繳交及口頭報告準備。尚無已繳交的紀錄。

## 從哪一步接手

1. **處理 Wix 結帳。** 先確認使用者要用哪個方向：[A 美容院現場](design-demos/checkout/a.html)、[B 商戶結帳](design-demos/checkout/b.html) 或 [C 試用時間線](design-demos/checkout/c.html)。簡報之前已選 A「美容院現場」，這次的結帳方向仍待選。作業第 3 頁明訂用 Wix checkout page 模擬交易。優先查現有站的原生結帳是否可在預覽中安全展示。如果改做自訂模擬頁，交接驗收時要標明其性質，並保留老師對要求的判斷。演示應看得到所選方案、14 天試用、今天 HK$0、試用後月費和確認畫面。實作限於模擬，避免啟動真實訂閱、收款或啟用付款設定。
2. **驗收網站及擷取證據。** 從公開網站的訪客視角跑一次首頁 → 預約示範 → 定價 → 結帳 → 聯絡表單，桌面與手機都看一遍。核對三個價格、試用條件及表單的成功提示。擷取首頁、定價、結帳、聯絡表單四張圖，供 PDF 附圖及口頭報告備案使用。
3. **完成 PDF 與 PPTX。** 在新版 Word 修正 §2.3，保留 Fee-for-Service 月費訂閱，寫明試用是限時體驗，以試用後的付費轉換率衡量。補上網站附圖、重新匯出 PDF，確認正文仍為 3 頁以內。PPTX 第 5 頁及講者備忘稿同步結帳路徑，維持總共 6 頁。用完整 demo 計時排練至 3 分鐘。
4. **繳交與核對。** 繳交前打開最終 PDF、PPTX 和 Wix 網址。繳交後確認上傳版本與網址正確。

## Wix 接手資訊

- [DeskMate AI 公開網站](https://example.wixsite.com/deskmate-ai) · [現有 Wix 編輯器](https://editor.wix.com/<redacted-site-editor>)
- [預約示範](https://example.wixsite.com/deskmate-ai/how-it-works) · [定價](https://example.wixsite.com/deskmate-ai/pricing-plans/plans-pricing) · [聯絡表單](https://example.wixsite.com/deskmate-ai/contact)
- Wix 插件曾成功讀取主站資料，確認為 Wix Harmony 免費站。新增頁面和 HTML 嵌入的入口在原站編輯器。Wixel 已完成配圖並透過 Wix 插件上傳，媒體庫名稱為 `DeskMate AI – Checkout Demo (Wixel).png`。[Wix HTML 嵌入說明](https://support.wix.com/en/article/wix-harmony-editor-embedding-a-link-or-html-code)
- 先前另站部署失敗，留下的空白站已移到 Wix 垃圾桶。第二次另站發布被自動審查擋下，目前也未收到使用者同意建立及公開獨立站點。原站是現有交件網址。若使用者同意另站發布，仍需核對它與作業所要求的原生結帳演示有何差別。

## 檔案入口

- [商業計劃 PDF](submission/Business_Plan_Updated.pdf) · [可編輯 Word](submission/Business_Plan_Updated.docx)
- [最新六頁 PPTX](submission/DeskMate_AI_Presentation.pptx) · [三分鐘英文講稿與問答](submission/Presentation_Script.md)
- [結帳三版總覽](design-demos/checkout/index.html) · [本機舊版結帳](submission/checkout-demo/index.html) · [新版桌面及手機驗證紀錄](design-demos/checkout/polish-log.md)
- [專案計劃](Assignment_Plan.md) · [待驗證紀錄](submission/To_Verify.md)

較早的 `Business_Plan.docx` 和 `Presentation.pptx` 是草稿。續改時從上述最新版開始。
