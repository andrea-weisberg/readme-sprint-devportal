---
title: Detailed settlement report
deprecated: false
hidden: false
metadata:
  robots: index
original_path: card-api/reports
---
<div class="block translation current highlight" data-element="para" data-attr-xinfo-text="10760">
<p><span style="font-weight: 400;">Paymentology also provides a detailed version of the Summary Settlement Report. </span><span style="font-weight: 400;">The Detailed Settlement Report shows each settled transaction, which allows you to use the Transaction ID to mark off settled transactions from authorized transactions. This also assists in confirming the values of the amounts in the Summary Settlement Report. The network provides the Transaction ID field during authorization. The same Transaction ID for authorizations is included in the Detailed Settlement Report.</span></p>
<p>There are 3 versions of this report available:<br />
<a href="#DSRV1">Version 1.0</a></p>
<p><a href="#DSRV2.0">Version 2.0</a></p>
<p><a href="#DSRV2.1">Version 2.1</a></p>
<p><span style="font-weight: 400;">The report includes the following details:</span></p>
<h3><a id="DSRV1"></a>Version 1</h3>
<p>Contains the Chargeback report</p>
<ul>
<li style="font-weight: 400;"><b>Transactions date</b> – <span style="font-weight: 400;">this is the settlement date of the transaction.</span></li>
<li style="font-weight: 400;"><b>The amount in the issuing currency (cardholder currency)</b> – <span style="font-weight: 400;">the actual amount is a decimal number.</span></li>
<li style="font-weight: 400;"><b>The amount in the settlement currency</b> – <span style="font-weight: 400;">it’s the amount passed over by the network. It should be multiplied by 100 to include cents. If the settlement currency does not have decimals, you’ll take the value as-is. </span></li>
<li style="font-weight: 400;"><b>Transaction narrative</b> – <span style="font-weight: 400;">it’s the merchant’s description.</span></li>
<li><strong data-renderer-mark="true">Transaction description </strong>– this describes the transaction type, such as:
<ul>
<li>Deduct – shows all deductions at the time of settlement.</li>
<li>Load – shows refunds.</li>
<li>Chargeback – gives positive or negative amounts for chargebacks.</li>
</ul>
</li>
<li style="font-weight: 400;"><b>Transaction ID</b> – <span style="font-weight: 400;">it’s a reference for the transaction. </span>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">In most cases, the provided Transaction ID will be the same Transaction ID as the original authorization. It’s usually 7 to 10 digits. </span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">In case of refunds, there will be a unique Transaction ID for each of them. The ID does not relate to the original authorization. It’s also longer, up to 23 characters.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">In case of chargebacks, there will be a unique Transaction ID for each of them. The ID does not relate to the original authorization. It’s also longer, up to 23 characters.</span></li>
</ul>
</li>
<li style="font-weight: 400;"><b>Currency code</b> – <span style="font-weight: 400;">this is the currency code for the settlement currency.</span></li>
<li style="font-weight: 400;"><b>Transaction types</b> – <span style="font-weight: 400;">they can be marked as 00 (for POS transactions), 01 (for ATM transactions), or 02 (for adjustment transactions).</span></li>
<li style="font-weight: 400;"><b>Wallet reference</b> – <span style="font-weight: 400;">this column will be empty for Card API reporting.</span></li>
<li style="font-weight: 400;"><b>System date</b> – <span style="font-weight: 400;">this is Paymentology’s system date in UTC +2 time zone. </span></li>
<li style="font-weight: 400;"><b>Sequence number</b> – <span style="font-weight: 400;">this is a unique sequence card identifier showing a running number for the cards created.</span></li>
<li style="font-weight: 400;"><b>Tracking number</b> – <span style="font-weight: 400;">this is a unique 15-digit tracking identifier for the card. </span></li>
<li style="font-weight: 400;"><b>Settlement currency</b> – <span style="font-weight: 400;">this is the currency code for the settlement currency.</span></li>
<li style="font-weight: 400;"><b>Interchange amount</b> – <span style="font-weight: 400;">this is the individual amounts earned per transaction.</span></li>
</ul>
</div>



\{/* unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"\} */}


<h3><a id="DSRV2.0"></a>Version 2.0</h3>
<p>Does not contain the Chargeback record (see Transaction Description column).</p>
<ul>
<li style="font-weight: 400;"><b>Transactions date</b> – <span style="font-weight: 400;">this is the settlement date of the transaction.</span></li>
<li style="font-weight: 400;"><b>The amount in the issuing currency (cardholder currency)</b> – <span style="font-weight: 400;">the actual amount is a decimal number.</span></li>
<li style="font-weight: 400;"><b>The amount in the settlement currency</b> – <span style="font-weight: 400;">it’s the amount passed over by the network. It should be multiplied by 100 to include cents. If the settlement currency does not have decimals, you’ll take the value as-is. </span></li>
<li style="font-weight: 400;"><b>Transaction narrative</b> – <span style="font-weight: 400;">it’s the merchant’s description.</span></li>
<li><strong data-renderer-mark="true">Transaction description </strong>– this describes the transaction type, such as:
<ul>
<li>Deduct – shows all deductions at the time of settlement.</li>
<li>Load – shows refunds.</li>
</ul>
</li>
<li style="font-weight: 400;"><b>Transaction ID</b> – <span style="font-weight: 400;">it’s a reference for the transaction. </span>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">In most cases, the provided Transaction ID will be the same Transaction ID as the original authorization. It’s usually 7 to 10 digits. </span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">In case of refunds, there will be a unique Transaction ID for each of them. The ID does not relate to the original authorization. It’s also longer, up to 23 characters.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">In case of chargebacks, there will be a unique Transaction ID for each of them. The ID does not relate to the original authorization. It’s also longer, up to 23 characters.</span></li>
</ul>
</li>
<li style="font-weight: 400;"><b>Currency code</b> – <span style="font-weight: 400;">this is the currency code for the settlement currency.</span></li>
<li style="font-weight: 400;"><b>Transaction types</b> – <span style="font-weight: 400;">they can be marked as 00 (for POS transactions), 01 (for ATM transactions), or 02 (for adjustment transactions).</span></li>
<li style="font-weight: 400;"><b>Wallet reference</b> – <span style="font-weight: 400;">this column will be empty for Card API reporting.</span></li>
<li style="font-weight: 400;"><b>System date</b> – <span style="font-weight: 400;">this is Paymentology’s system date in UTC +2 time zone. </span></li>
<li style="font-weight: 400;"><b>Sequence number</b> – <span style="font-weight: 400;">this is a unique sequence card identifier showing a running number for the cards created.</span></li>
<li style="font-weight: 400;"><b>Tracking number</b> – <span style="font-weight: 400;">this is a unique 15-digit tracking identifier for the card. </span></li>
<li style="font-weight: 400;"><b>Settlement currency</b> – <span style="font-weight: 400;">this is the currency code for the settlement currency.</span></li>
<li style="font-weight: 400;"><b>Interchange amount</b> – <span style="font-weight: 400;">this is the individual amounts earned per transaction.</span></li>
</ul>



\{/* unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"\} */}


<h3><a id="DSRV2.1"></a>Version 2.1</h3>
<p>Builds off of V2.0 and does not contain the Chargeback record. Changes include additional information to <span style="text-decoration: underline;">TransactionNarrative</span> column delimited by pipes eg. TransactionNarrative|AdditionalTraceRef|CustomIdentifier</p>
<ul>
<li style="font-weight: 400;"><b>Transactions date</b> – <span style="font-weight: 400;">this is the settlement date of the transaction.</span></li>
<li style="font-weight: 400;"><b>The amount in the issuing currency (cardholder currency)</b> – <span style="font-weight: 400;">the actual amount is a decimal number.</span></li>
<li style="font-weight: 400;"><b>The amount in the settlement currency</b> – <span style="font-weight: 400;">it’s the amount passed over by the network. It should be multiplied by 100 to include cents. If the settlement currency does not have decimals, you’ll take the value as-is. </span></li>
<li style="font-weight: 400;"><b>Transaction narrative|AdditionalTraceRef|CustomIdentifier</b> – <span style="font-weight: 400;">it’s the merchant’s description.</span></li>
<li><strong data-renderer-mark="true">Transaction description </strong>– this describes the transaction type, such as:
<ul>
<li>Deduct – shows all deductions at the time of settlement.</li>
<li>Load – shows refunds.</li>
</ul>
</li>
<li style="font-weight: 400;"><b>Transaction ID</b> – <span style="font-weight: 400;">it’s a reference for the transaction. </span>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">In most cases, the provided Transaction ID will be the same Transaction ID as the original authorization. It’s usually 7 to 10 digits. </span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">In case of refunds, there will be a unique Transaction ID for each of them. The ID does not relate to the original authorization. It’s also longer, up to 23 characters.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">In case of chargebacks, there will be a unique Transaction ID for each of them. The ID does not relate to the original authorization. It’s also longer, up to 23 characters.</span></li>
</ul>
</li>
<li style="font-weight: 400;"><b>Currency code</b> – <span style="font-weight: 400;">this is the currency code for the settlement currency.</span></li>
<li style="font-weight: 400;"><b>Transaction types</b> – <span style="font-weight: 400;">they can be marked as 00 (for POS transactions), 01 (for ATM transactions), or 02 (for adjustment transactions).</span></li>
<li style="font-weight: 400;"><b>Wallet reference</b> – <span style="font-weight: 400;">this column will be empty for Card API reporting.</span></li>
<li style="font-weight: 400;"><b>System date</b> – <span style="font-weight: 400;">this is Paymentology’s system date in UTC +2 time zone. </span></li>
<li style="font-weight: 400;"><b>Sequence number</b> – <span style="font-weight: 400;">this is a unique sequence card identifier showing a running number for the cards created.</span></li>
<li style="font-weight: 400;"><b>Tracking number</b> – <span style="font-weight: 400;">this is a unique 15-digit tracking identifier for the card. </span></li>
<li style="font-weight: 400;"><b>Settlement currency</b> – <span style="font-weight: 400;">this is the currency code for the settlement currency.</span></li>
<li style="font-weight: 400;"><b>Interchange amount</b> – <span style="font-weight: 400;">this is the individual amounts earned per transaction.</span></li>
</ul>



\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report format</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"FORMAT"\},\{"c":"FILE NAME"\},\{"c":"FREQUENCY"\},\{"c":"ACCESSIBILITY"\}],"caption":false,"body":[[\{"c":"CSV"\},\{"c":"[CampaignUUID]/[CampaignName]DailySettlements[YYYYMMDD].csv"\},\{"c":"Daily"\},\{"c":"HTTP get request or client SFTP folder"\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report time frame</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"UTC +2"\},\{"c":"UTC +7"\},\{"c":"REMARKS"\}],"caption":false,"body":[[\{"c":"04:00"\},\{"c":"09:00"\},{"c":"When the report is generated at 04:00 UTC+2 / 09:00 UTC+7 2020-09-10, the timeframe of all the settled transactions captured in this report is from 2020-09-09 00:00:00 to 2020-09-09 11:59:59 in: <br>\n• System time zone UTC+2 <br>\n• Asia client time zone UTC+7 <br>\n• Merchant time zone"}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report sample</h2>
<p> </p>
<p><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-2129" src="https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/Detailed-Settlement-report-1.png" alt="" width="1280" height="720" srcset="https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/Detailed-Settlement-report-1.png 1280w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/Detailed-Settlement-report-1-300x169.png 300w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/Detailed-Settlement-report-1-1024x576.png 1024w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/Detailed-Settlement-report-1-768x432.png 768w" sizes="auto, (max-width: 1280px) 100vw, 1280px" /></p>



\{/* unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21\}},"text":"<section class=\"tutuka-block tutuka-block--info\">\n<div class=\"block-info-single icon\">\n<div class=\"info-content\">\n<p><strong>Note: file will automatically download upon clicking link</strong></p>\n</div>\n</div>\n</section>\n"}]} */}


<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignNameDailySettlementsYYYYMMDD-1.csv">CampaignNameDailySettlementsYYYYMMDD.csv</a></p>
<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignNameDailySettlementsYYYYMMDD-2.csv">CampaignNameDailySettlementsYYYYMMDDsample.csv</a></p>
