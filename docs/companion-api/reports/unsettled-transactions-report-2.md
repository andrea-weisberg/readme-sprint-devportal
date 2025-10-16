---
title: Unsettled transactions report
deprecated: false
hidden: false
metadata:
  robots: index
---
<p>This report provides client’s with a full list of unsettled transactions, it assists with overall reconciliation.</p>
<p>There are two versions of this report available:</p>
<p><a href="#UTRV1">Version 1.0</a></p>
<p><a href="#UTRV2.0">Version 2.0</a></p>
<h3><a id="UTRV1"></a>Version 1</h3>
<p>This report includes the following details:</p>
<ul>
<li><strong>CampaignName</strong> – name of client’s campaign</li>
<li><strong>TransactionDate </strong>– This is the authorization date of the transaction</li>
<li><strong>TransactionAmount</strong> – the value of the transaction</li>
<li><strong>TransactionNarrative</strong> – it’s the merchant’s description</li>
<li><strong>TransactionDecription </strong>– this describes the transaction type, such as:
<ul>
<li>DEDUCT – deductions or debits</li>
<li>LOAD – refunds or credits</li>
<li>CHARGEBACK</li>
</ul>
</li>
<li><strong>TransactionID</strong> – it’s a reference for the transaction</li>
<li><strong>TransactionType</strong> – it can be marked as any of the following:
<ul>
<li>0 – POS Transaction</li>
<li>1 – ATM Transaction</li>
<li>2 – Adjustment</li>
</ul>
</li>
<li><strong>WalletReference</strong> – this is a unique customer reference for the card (applicable to Companion API). This column will be empty for Card API reporting.</li>
<li><strong>SystemDate</strong> – this is Paymentology’s system date in UTC +2 time zone.</li>
<li><strong>SequenceNumber </strong>– this is a unique sequence card identifier showing a running number for the cards created.</li>
<li><strong>TrackingNumber</strong> – this is a unique 15-digit tracking identifier for the card.</li>
</ul>
<p> </p>

<h3><a id="UTRV2.0"></a>Version 2</h3>
<p>This report includes the following details:</p>
<ul>
<li><strong>CampaignName</strong> – name of client’s campaign</li>
<li><strong>TransactionDate </strong>– This is the authorization date of the transaction</li>
<li><strong>TransactionAmount</strong> – the value of the transaction</li>
<li><strong>TransactionNarrative</strong> – it’s the merchant’s description</li>
<li><strong>TransactionDecription </strong>– this describes the transaction type, such as:
<ul>
<li>DEDUCT – deductions or debits</li>
<li>LOAD – refunds or credits</li>
<li>CHARGEBACK</li>
</ul>
</li>
<li><strong>TransactionID</strong> – it’s a reference for the transaction</li>
<li><strong>TransactionType</strong> – it can be marked as any of the following:
<ul>
<li>0 – POS Transaction</li>
<li>1 – ATM Transaction</li>
<li>2 – Adjustment</li>
</ul>
</li>
<li><strong>WalletReference</strong> – this is a unique customer reference for the card (applicable to Companion API). This column will be empty for Card API reporting.</li>
<li><strong>SystemDate</strong> – this is Paymentology’s system date in UTC +2 time zone.</li>
<li><strong>SequenceNumber </strong>– this is a unique sequence card identifier showing a running number for the cards created.</li>
<li><strong>TrackingNumber</strong> – this is a unique 15-digit tracking identifier for the card.</li>
<li><strong>NetworkTransactionID</strong> – the Transaction id of the transaction, as created by the card network. You can match this against the Transaction id on the <a href="https://developer.sprint.paymentology.com/companion-api/reports/mark-off-file/">Mark-off file</a></li>
</ul>
<p> </p>

<h2>Report format</h2>

<h2>Report time frame</h2>

<h2>Report sample</h2>
<p>**CampaignName_UnsettledTransactionReport_YYYYMMDD-.png IMAGE GOES HERE.**</p>

<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_UnsettledTransactionReport_YYYYMMDD.csv">CampaignName_UnsettledTransactionReport_YYYYMMDD.csv</a></p>
<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2024/01/CampaignName_UnsettledTransactionReport_YYYYMMDD-V2sample.csv">CampaignName_UnsettledTransactionReport_YYYYMMDD.csv V2 sample</a></p>

