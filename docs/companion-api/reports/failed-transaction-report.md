---
title: Failed transaction report
deprecated: false
hidden: false
metadata:
  robots: index
---
<div className="block translation current highlight" data-element="para" data-attr-xinfo-text="10769"><span style={{fontWeight: "400"}}>This report gives details of the transactions that were declined daily. </span><span style={{fontWeight: "400"}}>It contains a list of transactions that Paymentology or the client declined, and sent a declined response code to the card association. </span><span style={{fontWeight: "400"}}>With the failed transaction report file, it becomes easier to find the reasons for failures in transactions and improve the process.</span></div>
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
<li><strong>Campaign name </strong>– name of client’s campaign.</li>
<li><strong>Voucher</strong> <strong>Number</strong> – the customer’s card number.</li>
<li><strong>Transaction Amount </strong>– the value of the transaction.</li>
<li><strong>Transaction Date </strong>– this is the settlement date of the transaction.</li>
<li><strong>Transaction method</strong> – the API method used in sending the transaction to the client.</li>
<li><strong>Transaction Error Code</strong> – the code indicating the reason for the decline.</li>
<li><strong>Acceptor name</strong> – the name of the merchant.</li>
<li><strong>Merchant No </strong>– the unique number used to identify the merchant.</li>
<li><strong>Voucher value</strong> – the voucher value at the point the transaction failed. Voucher value = Voucher Load value – (Already settled amount + Authorised amount).</li>
<li><strong>Wallet Reference</strong> – this is a unique customer reference for the card.</li>
<li><strong>Transaction id</strong> – it’s a unique reference for the transaction.
<ul>
<li>In most cases, the provided Transaction id will be the same Transaction id as the original authorization. It’s usually 7 to 10 digits.</li>
<li>In case of refunds, there will be a unique Transaction id for each of them. The id does not relate to the original authorization. It’s also longer, up to 23 characters.</li>
<li>In case of chargebacks, there will be a unique Transaction id for each of them. The id does not relate to the original authorization. It’s also longer, up to 23 characters.</li>
</ul>
</li>
<li><strong>Tracking Number</strong> – this is a unique 15-digit tracking identifier for the card.</li>
<li><strong>MCC </strong>– the merchant category code.</li>
<li><strong>POS Entry mode</strong> – indicates how the transaction was captured (capture Mode). Possible values include: ECOM (Ecommerce), NFC (Near Field Communication), MAG (Magnetic stripe), MAN (Manually), EMV (EMV chip).</li>
<li><strong>Transaction Internal Code </strong>– this is a code that gives you the reason for transaction declines. List of codes can be downloaded <a href="https:developer.sprint.paymentology.com/wp-content/uploads/2021/04/Failed-transaction-report-code-descriptions.xlsx">here</a></li>
<li><strong>Digitized Wallet id </strong>– the 3 digit numeric code that identifies the Xpay App. Find a list of the Wallet IDs <a href="https:developer.sprint.paymentology.com/companion-api/tokenization2/token-lifecycle-management/#WID">here</a><em>. </em></li>
</ul>

<h3><a id="FTRV2"></a>Version 2</h3>
<p>Version 2 includes the following details:</p>
<ul>
<li><strong>VoucherNumber</strong> – the customer’s card number</li>
<li><strong>FailedTransactionID</strong> – it’s a unique reference for the transaction.
<ul>
<li>In most cases, the provided Transaction id will be the same Transaction id as the original authorization. It’s usually 7 to 10 digits.</li>
<li>In case of refunds, there will be a unique Transaction id for each of them. The id does not relate to the original authorization. It’s also longer, up to 23 characters.</li>
<li>In case of chargebacks, there will be a unique Transaction id for each of them. The id does not relate to the original authorization. It’s also longer, up to 23 characters.</li>
</ul>
</li>
<li><strong>FailedVoucher</strong><strong>Number</strong> – the customer’s card number.</li>
<li><strong>CampaignName </strong>– name of client’s campaign.</li>
<li><strong>FailedTransactionAmount </strong>– the value of the transaction.</li>
<li><strong>FailedTransactionDate </strong>– this is the settlement date of the transaction.</li>
<li><strong>FailedTransactionMethod</strong> – the API method used in sending the transaction to the client.</li>
<li><strong>FailedTransactionManager</strong> –</li>
<li><strong>FailedTransactionErrorCode</strong> – the code indicating the reason for the decline. List of codes can be downloaded <a href="https:developer.sprint.paymentology.com/wp-content/uploads/2021/04/Failed-transaction-report-code-descriptions.xlsx">here.</a></li>
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
<li><strong>FailedTransactionVoucherValue</strong> – the voucher value at the point the transaction failed. Voucher value = Voucher Load value – (Already settled amount + Authorised amount).</li>
<li><strong>EntryMode</strong> – indicates how the transaction was captured (capture Mode). Possible values include: ECOM (Ecommerce), NFC (Near Field Communication), MAG (Magnetic stripe), MAN (Manually), EMV (EMV chip).</li>
<li><strong>DigitizedWalletID </strong>– the 3 digit numeric code that identifies the Xpay App. Find a list of the Wallet IDs <a href="https:developer.sprint.paymentology.com/companion-api/tokenization2/token-lifecycle-management/#WID">here</a><em>.</em></li>
<li><strong>MerchantNo </strong>– the unique number used to identify the merchant.</li>
<li><strong>MerchantCategoryCode </strong>– the merchant category code.</li>
<li><strong>PaymentInitiator</strong> – indicates whether a transaction was initiated by the Cardholder (CIT – Cardholder Initiated Transaction) or the Merchant (MIT – Merchant Initiated Transaction)</li>
</ul>

<h2>Report format</h2>

<h2>Report time frame</h2>

<h2>Report sample</h2>
<p></p>
<p>**Failed-transaction-report1-1.png IMAGE GOES HERE.**</p>
<p></p>

<p><a href="https:developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_DailyAuthFailure_YYYYMMDD.csv">CampaignName_DailyAuthFailure_YYYYMMDD.csv</a></p>
<p><a href="https:developer.sprint.paymentology.com/wp-content/uploads/2025/05/CampaignName_DailyAuthFailure_YYYYMMDD-V2.csv">CampaignName_DailyAuthFailure_YYYYMMDD.csv – V2 sample</a></p>
</a></p></a></p></p></p></p></h2></h2></h2></strong></li></strong></li></strong></li></em></a></strong></li></strong></li></strong></li></li></ul></strong></li></strong></li></strong></li></strong></li></strong></li></strong></li></strong></li></a></strong></li></strong></li></strong></li></strong></li></strong></li></strong></li></strong></strong></li></li></li></li></ul></strong></li></strong></li></ul></p></a></h3></em></a></strong></li></a></strong></li></strong></li></strong></li></strong></li></li></li></li></ul></strong></li></strong></li></strong></li></strong></li></strong></li></strong></li></strong></li></strong></li></strong></li></strong></strong></li></strong></li></ul></p></a></h3></a></p></a></p></p></div></div></div></span></span></span></div>
