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
<li><strong>CampaignName</strong> – name of the campaign to which the card belongs.</li>
<li><strong>AuthorisationID</strong> – The unique authorization id for the transaction that led to the balance.</li>
<li><strong>AuthorisationAmount</strong> – The authorized amount for the transaction.</li>
<li><strong>AuthorisationDate</strong> – The date when the authorization was made.</li>
<li><strong>TransactionType</strong> – type of transaction. 0 = POS transaction, 1 = ATM transaction, 2 = Adjustment.</li>
<li><strong>CampaignCurrencySymbol</strong> – The currency of the campaign to which the card belongs in ISO4217 alpha (e.g. USD).</li>
<li><strong>MerchantName</strong> – The name and address of the merchant where the transaction occurred.</li>
</ul>

<h2>Report format</h2>

<h2>Report time frame</h2>

<h2>Report sample</h2>

<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2024/10/DailyNegativeBalanceReportOnChargebackQueue_CampaignName_YYYYMMDD.csv">DailyNegativeBalanceReportOnChargebackQueue_CampaignName_YYYYMMDD.csv</a></p>

<p><a className="btn btn--primary" href="#https://developer.sprint.paymentology.com/card-api/reports/">Back to Card API Reports</a></p>
