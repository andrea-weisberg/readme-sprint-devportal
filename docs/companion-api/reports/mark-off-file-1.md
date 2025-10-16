---
title: Mark-off file
deprecated: false
hidden: false
metadata:
  robots: index
---
<div class="block translation current highlight" data-element="para" data-attr-xinfo-text="10745">
<p>This file contains a record of all successful transactions that Paymentology processes on behalf of a store of value like a wallet or a bank account. It includes the financial transactions between a store of value and Paymentology.Paymentology generates the Mark-off file daily at midnight in your local time zone. The file matches a report from a store of value for all successfully processed transactions.</p>
<p>Ideally, the Mark-off file report and the store of value report should be in sync each day as the systems mirror one another. In case of any discrepancy, you should log a ticket via your Zendesk Portal. Select the *<strong data-renderer-mark="true">Report a Service Incident</strong>* form, and then choose *<strong data-renderer-mark="true">Reporting</strong>* and *<strong data-renderer-mark="true">Discrepancy</strong>* under the Request Type, indicate the file’s date and the transaction in question. We’ll promptly address the issue.</p>
<p>You can generate the Mark-off file by sending an HTTP GET request and downloading the report as a CSV file.</p>
<p>The Mark-off file has the following fields:</p>
<ul>
<li><strong>CampaignName</strong> – name of client’s card program.</li>
<li><b>TransactionDate </b>– the merchant’s timestamp in their time zone.</li>
<li><b>TransactionAmount </b>– the transaction value in cents. For example, a value of 4215 will mean 42.15. Amount is in the card campaign’s billing currency. ‘-‘ states the value is a debit and ‘+’ or no symbol states the value is a credit.</li>
<li><b>TransactionNarrative</b> – it’s the merchant’s description. Usually, the merchant’s name, city and country.</li>
<li><b>TransactionDescription</b> – this describes the transactions purpose such as:
<ul>
<li data-renderer-start-pos="639">Deduct – a deduction/debit.</li>
<li data-renderer-start-pos="699">Load – a refund/credit.</li>
</ul>
</li>
<li><b>TransactionID</b> – the Transaction ID of the transaction, as created by the card network<b>. </b></li>
<li><b>TransactionType </b>– it can be marked as any of the following:
<ul>
<li>0 – POS transaction</li>
<li>1 – ATM transaction</li>
<li>2 – Adjustment</li>
<li>20 – Refund</li>
<li>28 – Money Send</li>
</ul>
</li>
<li><b>WalletReference</b> – the customer reference associated to the card that transacted.</li>
<li><b>SystemDate</b> – Paymentology’s system date in UTC +2 time zone.</li>
<li><b>SequenceNumber</b> – Paymentology’s unique sequence identifier for the specific card used.</li>
<li><b>TrackingNumber</b> – Paymentology’s unique tracking identifier for the specific card used.</li>
<li><strong>NetworkTransactionID</strong> – (Mastercard only) this is the Networks TraceID, it assists clients with matching pre-authorizations and incremental pre-authorizations to the settlements for those transactions.</li>
</ul>
</div>



\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report format</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"FORMAT"\},\{"c":"FILE NAME"\},\{"c":"FREQUENCY"\},\{"c":"ACCESSIBILITY"\}],"caption":false,"body":[[\{"c":"CSV"\},\{"c":"[CampaignUUID]/[CampaignName]_MarkOffFile_[YYYYMMDD].csv"\},\{"c":"Daily"\},\{"c":"HTTP get request or client SFTP folder"\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report time frame</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"UTC+2"\},\{"c":"UTC+7"\},\{"c":"REMARKS"\}],"caption":false,"body":[[\{"c":"19:00"\},\{"c":"00:00"\},{"c":"When the report is generated at 19:00 UTC+2 2020-09-10 / 00:00: UTC+7 2020-09-11, the timeframe of all the authorized transactions captured in this report is from: <br> \n \n•\t2020-09-09 00:00:00 UTC+7(system time) to 2020-09-09 11:59:59 UTC+2(system time) <br>\n\n  \n•\t2020-09-10 00:00:00 UTC+7(Asia client time) to 2020-09-10 11:59:59 UTC+2(Asia client time)\n"}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report sample</h2>
<p> </p>
<p><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-2394" src="https://developer.sprint.paymentology.com/wp-content/uploads/2021/10/Mark-Off-report-Companion-final.png" alt="MarkOff sample" width="1280" height="720" srcset="https://developer.sprint.paymentology.com/wp-content/uploads/2021/10/Mark-Off-report-Companion-final.png 1280w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/10/Mark-Off-report-Companion-final-300x169.png 300w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/10/Mark-Off-report-Companion-final-1024x576.png 1024w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/10/Mark-Off-report-Companion-final-768x432.png 768w" sizes="auto, (max-width: 1280px) 100vw, 1280px" /></p>



\{/* unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21\}},"text":"<p><strong>Note: file will automatically download upon clicking link</strong></p>\n"}]} */}


<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2024/02/CampaignName_MarkOffFile_GMT_plus_3_00h00_YYYYMMDD.csv">CampaignName_MarkOffFile_GMT_plus_3_00h00_YYYYMMDD.csv</a></p>
