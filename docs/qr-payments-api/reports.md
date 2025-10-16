---
title: Reports
deprecated: false
hidden: false
metadata:
  robots: index
---
<p><strong>Paymentology provides end-to-end reporting and reconciliation capabilities to allow you to track all the financial movements, revenues collected, failed transactions, and more.</strong></p>



\{/* spacing: desktop=20, mobile=10 */\}


<p>These are some of the reports you can generate:</p>
<ul>
<li><a href="#Markoff">Mark-off file</a></li>
<li><a href="#summary">Summary settlement report</a></li>
</ul>
<p>Let’s look at each of them.</p>



\{/* unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"\} */}


<h2>1. <a id="Markoff"></a>Mark-off file</h2>
<p>This file contains a record of all successful transactions that Paymentology processes on behalf of a store of value like a wallet or a bank account. It includes the financial transactions between a store of value and Paymentology.</p>
<p>Paymentology generates the Mark-off file daily at midnight in your local time zone. The file matches a report from a store of value for all successfully processed transactions.</p>
<p>Ideally, the Mark-off file report and the store of value report should be in sync each day as the systems mirror one another. In case of any discrepancy, you should send a query to <a href="mailto:support@tutuka.com">support@paymentology.com</a>, indicating the file’s date and the transaction in question. We’ll promptly address the issue.</p>
<p>You can generate the Mark-off file by sending an HTTP GET request and download the report as a CSV file.</p>
<p>The Mark-off file has the following fields:</p>
<ul>
<li><b>Time date </b>– the merchant’s timestamp, in their time zone.</li>
<li><b>Amount </b>– the transaction amount in cents.</li>
<li><b>Merchant description</b> – the merchant’s name, city and country.</li>
<li><b>Transaction description</b> – the API’s naming convention, such as card deduct, card reversal and card load.</li>
<li><b>Transaction ID</b> – the Transaction ID of the transaction, as created by the card network<b>. </b></li>
<li><b>Transaction type </b>– it can be marked as 00 (for POS transactions), 01 (for ATM transactions), 02 (for adjustments), 09 (for cashback at POS), or 21 (for deposits).</li>
<li><b>Wallet / unique reference</b> – your unique customer reference information.</li>
<li><b>System date</b> – Paymentology’s system date in UTC +7 time zone.</li>
<li><b>Sequence number</b> – Paymentology’s unique sequence identifier for the specific card used.</li>
<li><b>Tracking number</b> – Paymentology’s unique tracking identifier for the specific card used.</li>
</ul>



\{/* spacing: desktop=20, mobile=10 */\}


\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"Report Time Frames","table":{"use_header":true,"header":[{"c":"UTC+2"\},\{"c":"UTC+7"\},\{"c":"REMARKS"\}],"caption":false,"body":[[\{"c":"19:00"\},\{"c":"00:00"\},{"c":"When the report is generated at 19:00 UTC+2 2020-09-10 / 00:00: UTC+7 2020-09-11, the timeframe of all the authorized transactions captured in this report is from: <br>\n• 2020-09-09 00:00:00 UTC+2(system time) to 2020-09-09 11:59:59 UTC+2(system time)<br>\n• 2020-09-10 00:00:00 UTC+7(Asia client time) to 2020-09-10 11:59:59 UTC+7(Asia client time)"}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report Sample</h2>
<p> </p>
<p><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-1547" src="https://developer.sprint.paymentology.com/wp-content/uploads/2021/01/Mark-Off-report-Companion-final.png" alt="" width="1272" height="324" srcset="https://developer.sprint.paymentology.com/wp-content/uploads/2021/01/Mark-Off-report-Companion-final.png 1272w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/01/Mark-Off-report-Companion-final-300x76.png 300w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/01/Mark-Off-report-Companion-final-1024x261.png 1024w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/01/Mark-Off-report-Companion-final-768x196.png 768w" sizes="auto, (max-width: 1272px) 100vw, 1272px" /></p>



\{/* unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"\} */}


<h2>2. <a id="summary"></a>Summary settlement report</h2>
<p>This gives a daily summary of all the transactions settled by the card association. Paymentology gathers the information from the card association file and packages it into a summary report.</p>
<p>It is a report where you can find a summary of transaction types, the number of transactions that have been settled for the day, fees and interchanges earned.</p>
<p>The Summary Settlement Report includes a separate tab for each currency you decide to settle in.</p>
<p><b>Note:</b> If the client chooses to settle in one currency, then both domestic and international settlements will fall under one tab.</p>
<p>The report includes a combination of debits and credits that the network processes daily.</p>
<ul>
<li><strong>Credits</strong> – include refunds, chargebacks and interchanges.</li>
<li><strong>Debits</strong> – include POS and ATM settlements, fees and unique transactions.</li>
</ul>
<p>The network NETTs off the credits from the debits. So, only a single transfer will need to be made when settling with the network daily.</p>
<p>You can generate the Summary Settlement Report by sending an HTTP GET request and download it in Excel format. The report is available daily from 2.00 a.m. (UTC+7).</p>
<p>Here is a description of the transactions you can find in the report:</p>
<ul>
<li><b>Unique Transactions </b>– consist of transactions from merchants, such as casinos, gambling sites and pharmacies.</li>
<li><b>ATM Interchange</b> – it’s a debit fee that the card issuer sends to a card network to pay the bank agent where the ATM transaction took place.</li>
<li><b>Card Association Fee</b> – this can be either a debit or a credit transaction. As a debit transaction, there is a fee paid to a card network for a specific service rendered. As a credit transaction, there can be some discounts applied to the paid services. There is a difference between Card Association Fee Credit and Card Association Fee Reversal. The latter refers to a reversal provided back to the issuer via an incorrect charge, whereas the former is a discount given off the fees.</li>
<li><strong>Payment transaction</strong> – shows the settlements for MoneySend transactions</li>
</ul>



\{/* spacing: desktop=20, mobile=10 */\}


\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"Report Time Frames","table":{"use_header":true,"header":[{"c":"UTC+2"\},\{"c":"UTC+7"\},\{"c":"REMARKS"\}],"caption":false,"body":[[\{"c":"08:00"\},\{"c":"13:00"\},{"c":"When the report is generated at 08:00 UTC+2 / 13:00 UTC+7 2020-09-10, the timeframe of all settled transactions captured in this report is from 2020-09-09 00:00:00 to 2020-09-09 11:59:59 in:<br>\n• System time zone UTC+2 <br>\n• Asia client time zone UTC+7 <br>\n• Merchant time zone"}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report Sample</h2>
<p><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-1541" src="https://developer.sprint.paymentology.com/wp-content/uploads/2021/01/Summary-Settlement-report-final.png" alt="" width="932" height="718" srcset="https://developer.sprint.paymentology.com/wp-content/uploads/2021/01/Summary-Settlement-report-final.png 932w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/01/Summary-Settlement-report-final-300x231.png 300w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/01/Summary-Settlement-report-final-768x592.png 768w" sizes="auto, (max-width: 932px) 100vw, 932px" /></p>
