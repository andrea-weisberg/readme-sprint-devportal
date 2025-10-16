---
title: Forex gains report
deprecated: false
hidden: false
metadata:
  robots: index
original_path: card-api/reports
---
<div class="block translation current highlight" data-element="para" data-attr-xinfo-text="10765">If you’re marking up a transaction with a forex fee, you’ll receive a report each day showing the FX amount that you earned as revenue for the day.</div>
<div data-element="para" data-attr-xinfo-text="10765"></div>
<div class="placeholder">
<div class="block translation" data-element="para" data-attr-xinfo-text="10767">The report includes the following details:</div>
<ul>
<li data-element="para" data-attr-xinfo-text="10767"><strong>Date</strong> – the date of the settlement.</li>
<li data-element="para" data-attr-xinfo-text="10767"><strong>Voucher number</strong> – the masked card number.</li>
<li data-element="para" data-attr-xinfo-text="10767"><strong>Activation data</strong> – the unique customer reference number.</li>
<li data-element="para" data-attr-xinfo-text="10767"><strong>Merchant description</strong> – the merchant name.</li>
<li data-element="para" data-attr-xinfo-text="10767"><strong>Transaction ID</strong> – the unique transaction ID used for the initial deduct.</li>
<li data-element="para" data-attr-xinfo-text="10767"><strong>Reversed</strong> – this shows if a fee was reversed.</li>
<li data-element="para" data-attr-xinfo-text="10767"><strong>Currency </strong>– this shows the currency of the fee.</li>
<li data-element="para" data-attr-xinfo-text="10767"><strong>Fee</strong> – the actual amount earned in forex fees.</li>
</ul>
<p>​</p>
</div>



\{/* unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21\}},"text":"<p>The Forex Gains Report is also known as the Forex Fee Report</p>\n"}]} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report format</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"FORMAT"\},\{"c":"FILE NAME"\},\{"c":"FREQUENCY"\},\{"c":"ACCESSIBILITY"\}],"caption":false,"body":[[\{"c":"XLS or CSV"\},\{"c":"[CampaignUUID]_DailyForexReport_CAMID[CampaignID]_[YYYY_MM_DD] or \n[CampaignUUID]_Forex_Fee_Report_[YYYY]_[MM]_[DD]"\},\{"c":"Daily"\},\{"c":"HTTP get request or client SFTP folder"\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report time frame</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"UTC +2"\},\{"c":"UTC +7"\},\{"c":"REMARKS"\}],"caption":false,"body":[[\{"c":"08:00"\},\{"c":"13:00"\},{"c":"When the report is generated at 08:00 UTC+2 / 13:00 UTC+7 2020-09-10, the timeframe of all Forex Gains transactions captured in this report is from 2020-09-09 00:00:00 to 2020-09-09 11:59:59 in: <br>\n• System time zone UTC+2 <br>\n• Asia client time zone UTC+7 <br>\n• Merchant time zone"}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report sample</h2>
<p><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-2328" src="https://developer.sprint.paymentology.com/wp-content/uploads/2021/08/Forex-gains-report-final-Card-API.png" alt="Forex gains report sample" width="1280" height="720" srcset="https://developer.sprint.paymentology.com/wp-content/uploads/2021/08/Forex-gains-report-final-Card-API.png 1280w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/08/Forex-gains-report-final-Card-API-300x169.png 300w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/08/Forex-gains-report-final-Card-API-1024x576.png 1024w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/08/Forex-gains-report-final-Card-API-768x432.png 768w" sizes="auto, (max-width: 1280px) 100vw, 1280px" /></p>



\{/* unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21\}},"text":"<section class=\"tutuka-block tutuka-block--info\">\n<div class=\"block-info-single icon\">\n<div class=\"info-content\">\n<p><strong>Note: file will automatically download upon clicking link</strong></p>\n</div>\n</div>\n</section>\n"}]} */}


<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/DailyForexReport_CAMIDNNN_YYYY_MM_DD.xls">DailyForexReport_CAMID(NNN)_(YYYY_MM_DD).xls</a></p>
