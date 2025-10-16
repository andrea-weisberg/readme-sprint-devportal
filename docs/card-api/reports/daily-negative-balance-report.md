---
title: Daily negative balance report
deprecated: false
hidden: false
metadata:
  robots: index
---
<p>This report provides clients with detailed information on cards that have entered into a negative balance status. It provides essential, actionable information to trace the transactions and correct the negative balance scenarios.</p>
<ul>
<li data-renderer-start-pos="2632">Clients will receive this report via email daily with the data from the previous day.</li>
<li data-renderer-start-pos="2632">All sensitive information, such as voucher numbers, are masked for security</li>
</ul>
<p>The report includes the following details:</p>
<ul>
<li><strong>VoucherNumber</strong> – The voucher number associated with the card (masked for security purposes, only last four digits visible).</li>
<li><strong>TrackingNumber</strong> – Unique identifier for tracking the transaction.</li>
<li><strong>WalletReference</strong> – The unique wallet identifier associated with the card.</li>
<li><strong>CardStatus</strong> – Current status of the card (e.g. Active, Inactive).</li>
<li><strong>VoucherBalanceAmount</strong> – The balance of the card.</li>
<li><strong>CampaignName</strong> – Name of the campaign to which the card belongs.</li>
<li><strong>AuthorisationID</strong> – The unique authorization ID for the transaction that led to the balance.</li>
<li><strong>AuthorisationAmount</strong> – The authorized amount for the transaction.</li>
<li><strong>AuthorisationDate</strong> – The date when the authorization was made.</li>
<li><strong>TransactionType</strong> – Type of transaction. 0 = POS transaction, 1 = ATM transaction, 2 = Adjustment.</li>
<li><strong>CampaignCurrencySymbol</strong> – The currency of the campaign to which the card belongs in ISO4217 alpha (e.g. USD).</li>
<li><strong>MerchantName</strong> – The name and address of the merchant where the transaction occurred.</li>
</ul>



\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report format</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"FORMAT"\},\{"c":"FILE NAME"\},\{"c":"FREQUENCY"\},\{"c":"ACCESSIBILITY"\}],"caption":false,"body":[[\{"c":"CSV"\},\{"c":"DailyNegativeBalanceReportOnChargebackQueue_[CampignName]_[YYYYMMDD].csv"\},\{"c":"Daily"\},\{"c":"Email (automated)"\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report time frame</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"UTC +2"\},\{"c":"UTC +7"\},\{"c":"REMARKS"\}],"caption":false,"body":[[\{"c":"Defined by client and configured by Paymentology."\},\{"c":"Defined by client and configured by Paymentology."\},\{"c":"The daily scheduled task generates the report for the previous day."\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report sample</h2>



\{/* unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21\}},"text":"<p><strong>Note: sample file will automatically download upon clicking link</strong></p>\n"}]} */}


<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2024/10/DailyNegativeBalanceReportOnChargebackQueue_CampaignName_YYYYMMDD.csv">DailyNegativeBalanceReportOnChargebackQueue_CampaignName_YYYYMMDD.csv</a></p>



\{/* spacing: desktop=20, mobile=10 */\}


\{/* unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"\} */}


<p><a class="btn btn--primary" href="#https://developer.sprint.paymentology.com/card-api/reports/">Back to Card API Reports</a></p>
