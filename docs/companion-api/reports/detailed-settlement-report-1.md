---
title: Detailed settlement report
deprecated: false
hidden: false
metadata:
  robots: index
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
<li><b>Transactions date</b> – this is the settlement date of the transaction.</li>
<li><b>The amount in the issuing currency (cardholder currency)</b> – the actual amount is a decimal number.</li>
<li><b>The amount in the settlement currency</b> – it’s the amount passed over by the network. It should be multiplied by 100 to include cents. If the settlement currency does not have decimals, you’ll take the value as-is.</li>
<li><b>Transaction narrative</b> – it’s the merchant’s description.</li>
<li><strong data-renderer-mark="true">Transaction description </strong>– this describes the transaction type, such as:
<ul>
<li>Deduct – shows all deductions at the time of settlement.</li>
<li>Load – shows loads/credits at the time of settlement.</li>
<li>Reversal – shows reversals at the time of settlement. In most cases these are reversals of an original deduct transaction.</li>
<li>Load reversal – shows loads that have been reversed at the time of settlement.</li>
<li>2nd presentment – shows 2nd presentments at the time of settlement.</li>
<li>2nd presentment reversal – shows a 2nd presentment that has been reversed at the time of settlement.</li>
</ul>
</li>
<li><b>Transaction ID</b> – it’s a reference for the transaction.
<ul>
<li>In most cases, the provided Transaction ID will be the same Transaction ID as the original authorization. It’s usually 7 to 10 digits.</li>
<li>In case of refunds, there will be a unique Transaction ID for each of them. The ID does not relate to the original authorization. It’s also longer, up to 23 characters.</li>
<li>In case of chargebacks, there will be a unique Transaction ID for each of them. The ID does not relate to the original authorization. It’s also longer, up to 23 characters.</li>
</ul>
</li>
<li><b>Currency code</b> – this is the currency code for the settlement currency.</li>
<li><b>Transaction types</b> – they can be marked as 00 (for POS transactions), 01 (for ATM transactions), or 02 (for adjustment transactions).</li>
<li><b>Wallet reference</b> – this is a unique customer reference for the card.</li>
<li><b>System date</b> – this is Paymentology’s system date in UTC +2 time zone.</li>
<li><b>Sequence number</b> – this is a unique sequence card identifier showing a running number for the cards created.</li>
<li><b>Tracking number</b> – this is a unique 15-digit tracking identifier for the card.</li>
<li><b>Settlement currency</b> – this is the currency code for the settlement currency.</li>
<li><b>Interchange amount</b> – this is the individual amounts earned per transaction.</li>
<li><strong>Network transaction ID</strong> – (Mastercard only) this is the Networks TraceID, it assists clients with matching pre-authorizations and incremental pre-authorizations to the settlements for those transactions.</li>
</ul>
</div>
<div class="block translation" data-element="para" data-attr-xinfo-text="10763"></div>

<h3><a id="DSRV2"></a>Version 2.4</h3>
<p>Version 2.4 includes the following details:</p>
<ul>
<li><b>TransactionDate</b> – this is the settlement date of the transaction.</li>
<li><b>Transaction Amount (SettlementAmount)</b> – it’s the amount passed over by the network. It should be multiplied by 100 to include cents. If the settlement currency does not have decimals, you’ll take the value as-is.</li>
<li><b>TransactionAmount (CardholderCurrency)</b> – the actual amount is a decimal number.</li>
<li><b>TransactionNarrative</b> – it’s the merchant’s description.</li>
<li><strong data-renderer-mark="true">TransactionDescription </strong>– this describes the transaction type, such as:
<ul>
<li>DEDUCT – shows all deductions at the time of settlement.</li>
<li>LOAD – shows loads/credits at the time of settlement.</li>
<li>REVERSAL – shows reversals at the time of settlement. In most cases these are reversals of an original deduct transaction.</li>
<li>LOAD REVERSAL – shows loads that have been reversed at the time of settlement.</li>
<li>2ND PRESENTMENT – shows 2nd presentments at the time of settlement.</li>
<li>2ND PRESENTMENT REVERSAL – shows a 2nd presentment that has been reversed at the time of settlement.</li>
</ul>
</li>
<li><b>TransactionID</b> – it’s a reference for the transaction.
<ul>
<li>In most cases, the provided Transaction ID will be the same Transaction ID as the original authorization. It’s usually 7 to 10 digits.</li>
<li>In case of refunds, there will be a unique Transaction ID for each of them. The ID does not relate to the original authorization. It’s also longer, up to 23 characters.</li>
<li>In case of chargebacks, there will be a unique Transaction ID for each of them. The ID does not relate to the original authorization. It’s also longer, up to 23 characters.</li>
</ul>
</li>
<li><b>TransactionType</b> – they can be marked as 00 (for POS transactions), 01 (for ATM transactions), or 02 (for adjustment transactions).</li>
<li><b>WalletReference</b> – this is a unique customer reference for the card.</li>
<li><b>SystemDate</b> – this is Paymentology’s system date in UTC +2 time zone.</li>
<li><b>SequenceNumber</b> – this is a unique sequence card identifier showing a running number for the cards created.</li>
<li><b>TrackingNumber</b> – this is a unique 15-digit tracking identifier for the card.</li>
<li><b>SettlementCurrency</b> – this is the currency code for the settlement currency and relates to the <strong>Transaction Amount (SettlementAmount)</strong>.</li>
<li><strong>CardholderCurrency</strong> – this is the currency code for the cardholder currency and relares to the <strong>TransactionAmount(CardholderCurrency)</strong>.</li>
<li><strong>Interchange Amount</strong> – this is the individual amounts earned per transaction.</li>
<li><strong>LocalAmount</strong> – this is the local amount of the transaction (DE4).</li>
<li><strong>LocalCurrency</strong> – this is the local currency of the transaction (DE49) and refers to <b>LocalAmount</b></li>
<li><strong>NetworkTransactionID</strong> – (Mastercard only) this is the Networks TraceID, it assists clients with matching pre-authorizations and incremental pre-authorizations to the settlements for those transactions.</li>
<li><strong>AcquirerReferenceNumber</strong> – this is the Acquirer Reference Data (DE31)</li>
<li><strong>TransactionAuthorisationNumber</strong> – this is the Approval Code (DE38) (Authorisation ID Response) provided by the network.</li>
<li><strong>OriginatingMessageFormat</strong> – identifies whether the acquirer was domestic or international (MEXICO ONLY).</li>
</ul>

<h2>Report format</h2>

<h2>Report time frame</h2>

<h2>Report Sample</h2>
<p> </p>
<p>**Detailed-Settlement-report1.png IMAGE GOES HERE.**</p>

<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2024/02/CampaignNameDailySettlementsYYYYMMDD.csv">CampaignNameDailySettlementsYYYYMMDD.csv</a></p>
</a></p></p></p></h2></h2></h2></strong></li></strong></li></strong></li></strong></li></b></strong></li></strong></li></strong></li></strong></strong></li></strong></b></li></b></li></b></li></b></li></b></li></b></li></li></li></li></ul></b></li></li></li></li></li></li></li></ul></strong></li></b></li></b></li></b></li></b></li></ul></p></a></h3></div></strong></li></b></li></b></li></b></li></b></li></b></li></b></li></b></li></b></li></li></li></li></ul></b></li></li></li></li></li></li></li></ul></strong></li></b></li></b></li></b></li></b></li></ul></p></a></h3></a></p></a></p></p></p></p></div>
