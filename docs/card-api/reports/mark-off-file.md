---
title: Mark-off file
deprecated: false
hidden: false
metadata:
  robots: index
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

<h2>Report format</h2>

<h2>Report time frame</h2>

<h2>Report sample</h2>
<p> </p>
<p>**MarkOff-report-final-Card-API.png IMAGE GOES HERE.**</p>

<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_MarkOffFile_YYYYMMDD.csv">CampaignName_MarkOffFile_YYYYMMDD.csv</a></p>
