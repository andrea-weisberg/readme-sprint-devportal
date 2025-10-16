---
title: Detailed settlement report
deprecated: false
hidden: false
metadata:
  robots: index
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

<h2>Report format</h2>

<h2>Report time frame</h2>

<h2>Report sample</h2>
<p> </p>
<p>**Detailed-Settlement-report-1.png IMAGE GOES HERE.**</p>

<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignNameDailySettlementsYYYYMMDD-1.csv">CampaignNameDailySettlementsYYYYMMDD.csv</a></p>
<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignNameDailySettlementsYYYYMMDD-2.csv">CampaignNameDailySettlementsYYYYMMDDsample.csv</a></p>
</a></p></a></p></p></p></h2></h2></h2></span></b></li></span></b></li></span></b></li></span></b></li></span></b></li></span></b></li></span></b></li></span></b></li></span></li></span></li></span></li></ul></span></b></li></li></li></ul></strong></li></span></b></li></span></b></li></span></b></li></span></b></li></ul></span></p></a></h3></span></b></li></span></b></li></span></b></li></span></b></li></span></b></li></span></b></li></span></b></li></span></b></li></span></li></span></li></span></li></ul></span></b></li></li></li></ul></strong></li></span></b></li></span></b></li></span></b></li></span></b></li></ul></p></a></h3></span></b></li></span></b></li></span></b></li></span></b></li></span></b></li></span></b></li></span></b></li></span></b></li></span></li></span></li></span></li></ul></span></b></li></li></li></li></ul></strong></li></span></b></li></span></b></li></span></b></li></span></b></li></ul></p></a></h3></span></p></a></p></a></p></a></p></span></span></p></div>
