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

<h2>Report format</h2>

<h2>Report time frame</h2>

<h2>Report sample</h2>
<p> </p>
<p>**Mark-Off-report-Companion-final.png IMAGE GOES HERE.**</p>

<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2024/02/CampaignName_MarkOffFile_GMT_plus_3_00h00_YYYYMMDD.csv">CampaignName_MarkOffFile_GMT_plus_3_00h00_YYYYMMDD.csv</a></p>
