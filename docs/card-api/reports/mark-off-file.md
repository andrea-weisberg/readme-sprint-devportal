---
title: Mark-off file
deprecated: false
hidden: false
metadata:
  robots: index
original_path: card-api/reports
---
<div class="block translation current highlight" data-element="para" data-attr-xinfo-text="10745">
<p><span style="font-weight: 400;">This file contains a record of all successful transactions that Paymentology processes on behalf of a store of value like a wallet or a bank account. It includes the financial transactions between a store of value and Paymentology. </span><span style="font-weight: 400;">Paymentology generates the Mark-off file daily at midnight in your local time zone. The file matches a report from a store of value for all successfully processed transactions. </span></p>
<p>Ideally, the Mark-off file report and the store of value report should be in sync each day as the systems mirror one another. In case of any discrepancy, you should log a ticket via your Zendesk Portal. Select the *<strong data-renderer-mark="true">Report a Service Incident</strong>* form, and then choose *<strong data-renderer-mark="true">Reporting</strong>* and *<strong data-renderer-mark="true">Discrepancy</strong>* under the Request Type, indicate the file’s date and the transaction in question. We’ll promptly address the issue.</p>
<p><span style="font-weight: 400;">The Mark-off file has the following fields:</span></p>
</div>
<ul>
<li><strong>Campaign Name </strong>– the name of the client’s campaign</li>
<li><strong>Paymentology System Date</strong> – <span style="font-weight: 400;">Paymentology’s system date in UTC+7 time zone</span></li>
<li><strong>Time Date Stamp</strong> – t<span style="font-weight: 400;">he merchant’s timestamp, in their time zone</span></li>
<li><strong>Customer Reference </strong>– unique customer reference information</li>
<li><strong>Pocket ID</strong> – the UUID information for the client campaign</li>
<li><strong>Transaction Description </strong>– this described the transaction, such as:<br />
DeductFund – shows deductions/debits<br />
LoadFunds – shows loads/credits</li>
<li><strong>Transaction Type</strong> – the possible values for TransactionTypes are:<br />
0 – POS transaction<br />
1 – ATM transaction<br />
2 – Adjustment</li>
<li><strong>Transaction ID</strong> – <span style="font-weight: 400;">the Transaction ID of the transaction, as created by the card network</span></li>
<li><strong>Sequence Number</strong> – <span style="font-weight: 400;">Paymentology’s unique sequence identifier for the specific card used</span></li>
<li><strong>Tracking Number</strong> – Paymentology’s unique tracking identifier for the specific card used</li>
<li><strong>Amount</strong> – the transaction amount in cents</li>
</ul>



\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report format</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"FORMAT"\},\{"c":"FILE NAME"\},\{"c":"FREQUENCY"\},\{"c":"ACCESSIBILITY"\}],"caption":false,"body":[[\{"c":"CSV"\},\{"c":"[CampaignUUID]/[CampaignName]_CardAPIMarkOffFile_[YYYYMMDD].csv"\},\{"c":"Daily"\},\{"c":"HTTP get request or client SFTP folder"\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report time frame</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"UTC +2"\},\{"c":"UTC +7"\},\{"c":"REMARKS"\}],"caption":false,"body":[[\{"c":"19:00"\},\{"c":"00:00"\},{"c":"When the report is generated at 19:00 UTC+2 2020-09-10 / 00:00: UTC+7 2020-09-11, the timeframe of all the authorized transactions captured in this report is from: <br>\n• 2020-09-09 00:00:00 UTC+2(system time) to 2020-09-09 11:59:59 UTC+2 (system time) <br>\n• 2020-09-10 00:00:00 UTC+7(Asia client time) to 2020-09-10 11:59:59 UTC+7 (Asia client time)"}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report sample</h2>
<p> </p>
<p><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-2326" src="https://developer.sprint.paymentology.com/wp-content/uploads/2021/08/MarkOff-report-final-Card-API.png" alt="Report sample for Mark off file" width="1280" height="720" srcset="https://developer.sprint.paymentology.com/wp-content/uploads/2021/08/MarkOff-report-final-Card-API.png 1280w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/08/MarkOff-report-final-Card-API-300x169.png 300w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/08/MarkOff-report-final-Card-API-1024x576.png 1024w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/08/MarkOff-report-final-Card-API-768x432.png 768w" sizes="auto, (max-width: 1280px) 100vw, 1280px" /></p>



\{/* unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21\}},"text":"<section class=\"tutuka-block tutuka-block--info\">\n<div class=\"block-info-single icon\">\n<div class=\"info-content\">\n<p><strong>Note: file will automatically download upon clicking link</strong></p>\n</div>\n</div>\n</section>\n"}]} */}


<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_MarkOffFile_YYYYMMDD.csv">CampaignName_MarkOffFile_YYYYMMDD.csv</a></p>
