---
title: Summary settlement report
deprecated: false
hidden: false
metadata:
  robots: index
---
<div class="block translation current highlight" data-element="para" data-attr-xinfo-text="10752"><span style="font-weight: 400;">This gives a daily summary of all the transactions settled by the card association. Paymentology gathers the information from the card association file and packages it into a summary report. </span><span style="font-weight: 400;">It is a report where you can find a summary of transaction types, the number of transactions that have been settled for the day, fees and interchanges earned. </span></p>
<p><span style="font-weight: 400;">The Summary Settlement Report includes a separate tab for each currency you decide to settle in.</span></p>
<p><b>Note:</b><span style="font-weight: 400;"> If the client chooses to settle in one currency, then both domestic and international settlements will fall under one tab. </span></p>
<p><span style="font-weight: 400;">The report includes a combination of debits and credits that the network processes daily. </span></p>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;"><strong>Credits</strong> – include refunds, chargebacks and interchanges.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;"><strong>Debits</strong> – include POS and ATM settlements, fees and unique transactions. </span></li>
</ul>
<p><span style="font-weight: 400;">The network NETTs off the credits from the debits. So, only a single transfer will need to be made when settling with the network daily.</span></p>
<p><span style="font-weight: 400;">Here is a description of the transactions you can find in the report:</span></p>
<ul>
<li><b>Unique Transactions</b> – <span style="font-weight: 400;">consist of transactions from merchants, such as casinos, gambling sites and pharmacies.</span></li>
<li><b>ATM Interchange</b> – <span style="font-weight: 400;">it’s a debit fee that the card issuer sends to a card network to pay the bank agent where the ATM transaction took place.</span></li>
<li><b>Card Association Fee</b> – <span style="font-weight: 400;">this can be either a debit or a credit transaction. As a debit transaction, there is a fee paid to a card network for a specific service rendered. As a credit transaction, there can be some discounts applied to the paid services. There is a difference between Card Association Fee Credit and Card Association Fee Reversal. The latter refers to a reversal provided back to the issuer via an incorrect charge, whereas the former is a discount given off the fees. </span></li>
</ul>
</div>



\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report format</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"FORMAT"\},\{"c":"FILE NAME"\},\{"c":"FREQUENCY"\},\{"c":"ACCESSIBILITY"\}],"caption":false,"body":[[\{"c":"CSV or XLS"\},\{"c":"[CampaignUUID]/[CampaignName]Daily_Settlement_Report_[ICA]_[YYYY_MM_DD].csv or [CampaignUUID]/[CampaignName]Daily_Settlement_Report_[ICA]_[YYYY_MM_DD].xls"\},\{"c":"Daily"\},\{"c":"HTTP get request or client SFTP folder"\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report time frame</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"UTC +2"\},\{"c":"UTC +7"\},\{"c":"REMARKS"\}],"caption":false,"body":[[\{"c":"08:00"\},\{"c":"13:00"\},{"c":"When the report is generated at 08:00 UTC+2 / 13:00 UTC+7 2020-09-10, the timeframe of all settled transactions captured in this report is from 2020-09-09 00:00:00 to 2020-09-09 11:59:59 in: <br>\n• System time zone UTC+2 <br>\n• Asia client time zone UTC+7 <br>\n• Merchant time zone"}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report sample</h2>
<p><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-1541" src="https://developer.sprint.paymentology.com/wp-content/uploads/2021/01/Summary-Settlement-report-final.png" alt="" width="932" height="718" srcset="https://developer.sprint.paymentology.com/wp-content/uploads/2021/01/Summary-Settlement-report-final.png 932w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/01/Summary-Settlement-report-final-300x231.png 300w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/01/Summary-Settlement-report-final-768x592.png 768w" sizes="auto, (max-width: 932px) 100vw, 932px" /></p>



\{/* unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21\}},"text":"<section class=\"tutuka-block tutuka-block--info\">\n<div class=\"block-info-single icon\">\n<div class=\"info-content\">\n<p><strong>Note: file will automatically download upon clicking link</strong></p>\n</div>\n</div>\n</section>\n"}]} */}


<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/Daily_Settlement_Report_ICA_YYYY_MM_DD-1.xls">Daily_Settlement_Report_ICA_(YYYY_MM_DD).xls</a></p>
