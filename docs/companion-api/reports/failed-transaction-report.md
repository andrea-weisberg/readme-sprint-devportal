---
title: Failed transaction report
deprecated: false
hidden: false
metadata:
  robots: index
original_path: companion-api/reports
---
<div class="block translation current highlight" data-element="para" data-attr-xinfo-text="10769"><span style="font-weight: 400;">This report gives details of the transactions that were declined daily. </span><span style="font-weight: 400;">It contains a list of transactions that Paymentology or the client declined, and sent a declined response code to the card association. </span><span style="font-weight: 400;">With the failed transaction report file, it becomes easier to find the reasons for failures in transactions and improve the process.</span></div>
<div data-element="para" data-attr-xinfo-text="10769"></div>
<div data-element="para" data-attr-xinfo-text="10769">The report is also generated monthly and contains the same report details as the daily report.</div>
<div data-element="para" data-attr-xinfo-text="10769">
<p>There are two versions of this report available:</p>
<p><a href="#FTRV1">Version 1.0</a></p>
<p><a href="#FTRV2">Version 2.0</a></p>
<h3><a id="FTRV1"></a>Version 1</h3>
<p>Version 1 includes the following details:</p>
</div>
<ul>
<li><strong>Campaign Name </strong>– name of client’s campaign.</li>
<li><strong>Voucher</strong> <strong>Number</strong> – the customer’s card number.</li>
<li><strong>Transaction Amount </strong>– the value of the transaction.</li>
<li><strong>Transaction Date </strong>– this is the settlement date of the transaction.</li>
<li><strong>Transaction Method</strong> – the API method used in sending the transaction to the client.</li>
<li><strong>Transaction Error Code</strong> – the code indicating the reason for the decline.</li>
<li><strong>Acceptor Name</strong> – the name of the merchant.</li>
<li><strong>Merchant No </strong>– the unique number used to identify the merchant.</li>
<li><strong>Voucher Value</strong> – the voucher value at the point the transaction failed. Voucher Value = Voucher Load Value – (Already settled amount + Authorised amount).</li>
<li><strong>Wallet Reference</strong> – this is a unique customer reference for the card.</li>
<li><strong>Transaction ID</strong> – it’s a unique reference for the transaction.
<ul>
<li>In most cases, the provided Transaction ID will be the same Transaction ID as the original authorization. It’s usually 7 to 10 digits.</li>
<li>In case of refunds, there will be a unique Transaction ID for each of them. The ID does not relate to the original authorization. It’s also longer, up to 23 characters.</li>
<li>In case of chargebacks, there will be a unique Transaction ID for each of them. The ID does not relate to the original authorization. It’s also longer, up to 23 characters.</li>
</ul>
</li>
<li><strong>Tracking Number</strong> – this is a unique 15-digit tracking identifier for the card.</li>
<li><strong>MCC </strong>– the merchant category code.</li>
<li><strong>POS Entry mode</strong> – indicates how the transaction was captured (Capture Mode). Possible values include: ECOM (Ecommerce), NFC (Near Field Communication), MAG (Magnetic stripe), MAN (Manually), EMV (EMV chip).</li>
<li><strong>Transaction Internal Code </strong>– this is a code that gives you the reason for transaction declines. List of codes can be downloaded <a href="https://developer.sprint.paymentology.com/wp-content/uploads/2021/04/Failed-transaction-report-code-descriptions.xlsx">here</a></li>
<li><strong>Digitized Wallet ID </strong>– the 3 digit numeric code that identifies the Xpay App. Find a list of the Wallet IDs <a href="https://developer.sprint.paymentology.com/companion-api/tokenization2/token-lifecycle-management/#WID">here</a><em>. </em></li>
</ul>



\{/* unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21\}},"text":"<p><span style=\"font-weight: 400;\"> If the transaction did not reach Paymentology and was declined, this would not appear on the report.</span></p>\n"}]} */}


\{/* unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"\} */}


<h3><a id="FTRV2"></a>Version 2</h3>
<p>Version 2 includes the following details:</p>
<ul>
<li><strong>VoucherNumber</strong> – the customer’s card number</li>
<li><strong>FailedTransactionID</strong> – it’s a unique reference for the transaction.
<ul>
<li>In most cases, the provided Transaction ID will be the same Transaction ID as the original authorization. It’s usually 7 to 10 digits.</li>
<li>In case of refunds, there will be a unique Transaction ID for each of them. The ID does not relate to the original authorization. It’s also longer, up to 23 characters.</li>
<li>In case of chargebacks, there will be a unique Transaction ID for each of them. The ID does not relate to the original authorization. It’s also longer, up to 23 characters.</li>
</ul>
</li>
<li><strong>FailedVoucher</strong><strong>Number</strong> – the customer’s card number.</li>
<li><strong>CampaignName </strong>– name of client’s campaign.</li>
<li><strong>FailedTransactionAmount </strong>– the value of the transaction.</li>
<li><strong>FailedTransactionDate </strong>– this is the settlement date of the transaction.</li>
<li><strong>FailedTransactionMethod</strong> – the API method used in sending the transaction to the client.</li>
<li><strong>FailedTransactionManager</strong> –</li>
<li><strong>FailedTransactionErrorCode</strong> – the code indicating the reason for the decline. List of codes can be downloaded <a href="https://developer.sprint.paymentology.com/wp-content/uploads/2021/04/Failed-transaction-report-code-descriptions.xlsx">here.</a></li>
<li><strong>FailedTransactionInternalCode </strong>– this is a code that gives you the reason for the decline, when the failure was due to an internal reason. In most cases this will be NULL.</li>
<li><strong>FailedTransactionAcquiringInstitution</strong> – the acquiring institution (typically the merchants bank) or its agent.</li>
<li><strong>FailedTransactionDescription</strong> – the name of the merchant.</li>
<li><strong>FailedTransactionErrorDescription</strong> – a textual description on why a transaction failed with more reasons. For example: “Reject With Action Code 1061; ruleID: 6839”.</li>
<li><strong>TrackingNumber</strong> – this is a unique 15-digit tracking identifier for the card.</li>
<li><strong>WalletReference</strong> – this is a unique customer reference for the card.</li>
<li><strong>TransactionID</strong> – it’s a unique reference for the failed transaction record.
<ul>
<li>In most cases, the provided TransactionID will be different from the FailedTransactionID, as it’s a reference to the failed record. It’s usually 12-16 digits.</li>
</ul>
</li>
<li><strong>FailedTransactionVoucherValue</strong> – the voucher value at the point the transaction failed. Voucher Value = Voucher Load Value – (Already settled amount + Authorised amount).</li>
<li><strong>EntryMode</strong> – indicates how the transaction was captured (Capture Mode). Possible values include: ECOM (Ecommerce), NFC (Near Field Communication), MAG (Magnetic stripe), MAN (Manually), EMV (EMV chip).</li>
<li><strong>DigitizedWalletID </strong>– the 3 digit numeric code that identifies the Xpay App. Find a list of the Wallet IDs <a href="https://developer.sprint.paymentology.com/companion-api/tokenization2/token-lifecycle-management/#WID">here</a><em>.</em></li>
<li><strong>MerchantNo </strong>– the unique number used to identify the merchant.</li>
<li><strong>MerchantCategoryCode </strong>– the merchant category code.</li>
<li><strong>PaymentInitiator</strong> – indicates whether a transaction was initiated by the Cardholder (CIT – Cardholder Initiated Transaction) or the Merchant (MIT – Merchant Initiated Transaction)</li>
</ul>



\{/* unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21\}},"text":"<p><span style=\"font-weight: 400;\"> If the transaction did not reach Paymentology and was declined, this would not appear on the report.</span></p>\n"}]} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report format</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"FORMAT"\},\{"c":"FILE NAME"\},\{"c":"FREQUENCY"\},\{"c":"ACCESSIBILITY"\}],"caption":false,"body":[[\{"c":"CSV"\},\{"c":"DAILY REPORT: [CampaignUUID]/[CampaignName]_DailyAuthFailure_[YYYYMMDD].csv\nMONTHLY REPORT: [CampaignUUID]/failedtransactions_[CampaignName]_[YYYY-MM-DD-YYYY-MM-DD].csv"\},\{"c":"Daily & Monthly"\},\{"c":"HTTP get request or client SFTP folder"\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report time frame</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"UTC +2"\},\{"c":"UTC +7"\},\{"c":"REMARKS"\}],"caption":false,"body":[[\{"c":"06:30"\},\{"c":"11:30"\},{"c":"When the report is generated at 06:30 UTC+2 / 11:30 UTC+7 2020-09-10, the timeframe of all failed transactions captured in this report is from 2020-09-09 00:00:00 to 2020-09-09 11:59:59 in: \n<br> \n•\tSystem time zone UTC+2 <br>  \n•\tAsia client time zone UTC+7 <br>\n•\tMerchant time zone  "}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report sample</h2>
<p></p>
<p><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-2401" src="https://developer.sprint.paymentology.com/wp-content/uploads/2021/10/Failed-transaction-report1-1.png" alt="" width="1280" height="720" data-mce-src="https://developer.sprint.paymentology.com/wp-content/uploads/2021/10/Failed-transaction-report1-1.png" srcset="https://developer.sprint.paymentology.com/wp-content/uploads/2021/10/Failed-transaction-report1-1.png 1280w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/10/Failed-transaction-report1-1-300x169.png 300w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/10/Failed-transaction-report1-1-1024x576.png 1024w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/10/Failed-transaction-report1-1-768x432.png 768w" sizes="auto, (max-width: 1280px) 100vw, 1280px" /></p>
<p></p>



\{/* unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21\}},"text":"<p><strong>Note: file will automatically download upon clicking link</strong></p>\n"}]} */}


<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_DailyAuthFailure_YYYYMMDD.csv">CampaignName_DailyAuthFailure_YYYYMMDD.csv</a></p>
<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2025/05/CampaignName_DailyAuthFailure_YYYYMMDD-V2.csv">CampaignName_DailyAuthFailure_YYYYMMDD.csv – V2 sample</a></p>
