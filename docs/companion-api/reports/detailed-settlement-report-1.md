---
title: Detailed settlement report
deprecated: false
hidden: false
metadata:
  robots: index
original_path: companion-api/reports
---
<div class="block translation current highlight" data-element="para" data-attr-xinfo-text="10760">
<p>Paymentology also provides a detailed version of the Summary Settlement Report.The Detailed Settlement Report shows each settled transaction, which allows you to use the Transaction ID to mark off settled transactions from authorized transactions. This also assists in confirming the values of the amounts in the Summary Settlement Report. The network provides the Transaction ID field during authorization. The same Transaction ID for authorizations is included in the Detailed Settlement Report.</p>
<p>You can generate the Detailed Settlement Report by sending an HTTP GET request and download it as a CSV file.</p>
<p>There are two versions of this report available:</p>
<p><a href="#DSRV1">Version 1.0</a></p>
<p><a href="#DSRV2">Version 2.4</a></p>
<h3><a id="DSRV1"></a>Version 1</h3>
<p>Version 1 includes the following details:</p>
<ul>
<li><b>Transactions date</b> &#8211; this is the settlement date of the transaction.</li>
<li><b>The amount in the issuing currency (cardholder currency)</b> &#8211; the actual amount is a decimal number.</li>
<li><b>The amount in the settlement currency</b> &#8211; it’s the amount passed over by the network. It should be multiplied by 100 to include cents. If the settlement currency does not have decimals, you’ll take the value as-is.</li>
<li><b>Transaction narrative</b> &#8211; it’s the merchant’s description.</li>
<li><strong data-renderer-mark="true">Transaction description </strong>&#8211; this describes the transaction type, such as:
<ul>
<li>Deduct &#8211; shows all deductions at the time of settlement.</li>
<li>Load &#8211; shows loads/credits at the time of settlement.</li>
<li>Reversal &#8211; shows reversals at the time of settlement. In most cases these are reversals of an original deduct transaction.</li>
<li>Load reversal &#8211; shows loads that have been reversed at the time of settlement.</li>
<li>2nd presentment &#8211; shows 2nd presentments at the time of settlement.</li>
<li>2nd presentment reversal &#8211; shows a 2nd presentment that has been reversed at the time of settlement.</li>
</ul>
</li>
<li><b>Transaction ID</b> &#8211; it’s a reference for the transaction.
<ul>
<li>In most cases, the provided Transaction ID will be the same Transaction ID as the original authorization. It’s usually 7 to 10 digits.</li>
<li>In case of refunds, there will be a unique Transaction ID for each of them. The ID does not relate to the original authorization. It’s also longer, up to 23 characters.</li>
<li>In case of chargebacks, there will be a unique Transaction ID for each of them. The ID does not relate to the original authorization. It’s also longer, up to 23 characters.</li>
</ul>
</li>
<li><b>Currency code</b> &#8211; this is the currency code for the settlement currency.</li>
<li><b>Transaction types</b> &#8211; they can be marked as 00 (for POS transactions), 01 (for ATM transactions), or 02 (for adjustment transactions).</li>
<li><b>Wallet reference</b> &#8211; this is a unique customer reference for the card.</li>
<li><b>System date</b> &#8211; this is Paymentology&#8217;s system date in UTC +2 time zone.</li>
<li><b>Sequence number</b> &#8211; this is a unique sequence card identifier showing a running number for the cards created.</li>
<li><b>Tracking number</b> &#8211; this is a unique 15-digit tracking identifier for the card.</li>
<li><b>Settlement currency</b> &#8211; this is the currency code for the settlement currency.</li>
<li><b>Interchange amount</b> &#8211; this is the individual amounts earned per transaction.</li>
<li><strong>Network transaction ID</strong> &#8211; (Mastercard only) this is the Networks TraceID, it assists clients with matching pre-authorizations and incremental pre-authorizations to the settlements for those transactions.</li>
</ul>
</div>
<div class="block translation" data-element="para" data-attr-xinfo-text="10763"></div>



<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<h3><a id="DSRV2"></a>Version 2.4</h3>
<p>Version 2.4 includes the following details:</p>
<ul>
<li><b>TransactionDate</b> &#8211; this is the settlement date of the transaction.</li>
<li><b>Transaction Amount (SettlementAmount)</b> &#8211; it’s the amount passed over by the network. It should be multiplied by 100 to include cents. If the settlement currency does not have decimals, you’ll take the value as-is.</li>
<li><b>TransactionAmount (CardholderCurrency)</b> &#8211; the actual amount is a decimal number.</li>
<li><b>TransactionNarrative</b> &#8211; it’s the merchant’s description.</li>
<li><strong data-renderer-mark="true">TransactionDescription </strong>&#8211; this describes the transaction type, such as:
<ul>
<li>DEDUCT &#8211; shows all deductions at the time of settlement.</li>
<li>LOAD &#8211; shows loads/credits at the time of settlement.</li>
<li>REVERSAL &#8211; shows reversals at the time of settlement. In most cases these are reversals of an original deduct transaction.</li>
<li>LOAD REVERSAL &#8211; shows loads that have been reversed at the time of settlement.</li>
<li>2ND PRESENTMENT &#8211; shows 2nd presentments at the time of settlement.</li>
<li>2ND PRESENTMENT REVERSAL &#8211; shows a 2nd presentment that has been reversed at the time of settlement.</li>
</ul>
</li>
<li><b>TransactionID</b> &#8211; it’s a reference for the transaction.
<ul>
<li>In most cases, the provided Transaction ID will be the same Transaction ID as the original authorization. It’s usually 7 to 10 digits.</li>
<li>In case of refunds, there will be a unique Transaction ID for each of them. The ID does not relate to the original authorization. It’s also longer, up to 23 characters.</li>
<li>In case of chargebacks, there will be a unique Transaction ID for each of them. The ID does not relate to the original authorization. It’s also longer, up to 23 characters.</li>
</ul>
</li>
<li><b>TransactionType</b> &#8211; they can be marked as 00 (for POS transactions), 01 (for ATM transactions), or 02 (for adjustment transactions).</li>
<li><b>WalletReference</b> &#8211; this is a unique customer reference for the card.</li>
<li><b>SystemDate</b> &#8211; this is Paymentology&#8217;s system date in UTC +2 time zone.</li>
<li><b>SequenceNumber</b> &#8211; this is a unique sequence card identifier showing a running number for the cards created.</li>
<li><b>TrackingNumber</b> &#8211; this is a unique 15-digit tracking identifier for the card.</li>
<li><b>SettlementCurrency</b> &#8211; this is the currency code for the settlement currency and relates to the <strong>Transaction Amount (SettlementAmount)</strong>.</li>
<li><strong>CardholderCurrency</strong> &#8211; this is the currency code for the cardholder currency and relares to the <strong>TransactionAmount(CardholderCurrency)</strong>.</li>
<li><strong>Interchange Amount</strong> &#8211; this is the individual amounts earned per transaction.</li>
<li><strong>LocalAmount</strong> &#8211; this is the local amount of the transaction (DE4).</li>
<li><strong>LocalCurrency</strong> &#8211; this is the local currency of the transaction (DE49) and refers to <b>LocalAmount</b></li>
<li><strong>NetworkTransactionID</strong> &#8211; (Mastercard only) this is the Networks TraceID, it assists clients with matching pre-authorizations and incremental pre-authorizations to the settlements for those transactions.</li>
<li><strong>AcquirerReferenceNumber</strong> &#8211; this is the Acquirer Reference Data (DE31)</li>
<li><strong>TransactionAuthorisationNumber</strong> &#8211; this is the Approval Code (DE38) (Authorisation ID Response) provided by the network.</li>
<li><strong>OriginatingMessageFormat</strong> &#8211; identifies whether the acquirer was domestic or international (MEXICO ONLY).</li>
</ul>



<!-- spacing: desktop=20, mobile=10 -->


<h2>Report format</h2>



<!-- unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"FORMAT"},{"c":"FILE NAME"},{"c":"FREQUENCY"},{"c":"ACCESSIBILITY"}],"caption":false,"body":[[{"c":"CSV"},{"c":"[CampaignUUID]/[CampaignName]DailySettlements[YYYYMMDD].csv"},{"c":"Daily"},{"c":"HTTP get request or client SFTP folder"}]]}} -->


<!-- spacing: desktop=20, mobile=10 -->


<h2>Report time frame</h2>



<!-- unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"UTC +2"},{"c":"UTC +7"},{"c":"REMARKS"}],"caption":false,"body":[[{"c":"04:00"},{"c":"09:00"},{"c":"When the report is generated at 04:00 UTC+2 / 09:00 UTC+7 2020-09-10, the timeframe of all the settled transactions captured in this report is from 2020-09-09 00:00:00 to 2020-09-09 11:59:59 in: \n<br> \n•\tSystem time zone UTC+2   <br>\n•\tAsia client time zone UTC+7 <br>\n•\tMerchant time zone  \n"}]]}} -->


<!-- spacing: desktop=20, mobile=10 -->


<h2>Report Sample</h2>
<p>&nbsp;</p>
<p><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-2396" src="https://developer.sprint.paymentology.com/wp-content/uploads/2021/10/Detailed-Settlement-report1.png" alt="" width="1280" height="720" srcset="https://developer.sprint.paymentology.com/wp-content/uploads/2021/10/Detailed-Settlement-report1.png 1280w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/10/Detailed-Settlement-report1-300x169.png 300w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/10/Detailed-Settlement-report1-1024x576.png 1024w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/10/Detailed-Settlement-report1-768x432.png 768w" sizes="auto, (max-width: 1280px) 100vw, 1280px" /></p>



<!-- unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21}},"text":"<p><strong>Note: file will automatically download upon clicking link</strong></p>\n"}]} -->


<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2024/02/CampaignNameDailySettlementsYYYYMMDD.csv">CampaignNameDailySettlementsYYYYMMDD.csv</a></p>
