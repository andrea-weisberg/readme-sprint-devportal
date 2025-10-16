---
title: Daily sales and redemption report
deprecated: false
hidden: false
metadata:
  robots: index
---
<p>A report which includes all Loads, Redemptions, Authorization, Fees that takes place on a voucher/card.</p>
<p>The report includes the following details:</p>
<ul>
<li><strong>VoucherEngineRef</strong> – this is the vouchers table reference (integer).</li>
<li><strong>VoucherNumber</strong> – this is the actual card number (10 character string).</li>
<li><strong>ControlVoucherNumber</strong> – this is the main card number for a pocket campaign, where one plastic card is linked to multiple cards i.e. the pockets. Note: <strong>ControlVoucherNumber</strong> is only included in PocketCampaigns (16 character string).</li>
<li><strong>TrackingNumber</strong> – this is the public card number that we share with clients (15 character string).</li>
<li><strong>MerchantName</strong> – this is the name of the merchant (string).</li>
<li><strong>Date</strong> – this is the date of the transaction (YYYY/MM/DD HH:MM:SS).</li>
<li><strong>Type</strong> – this is the transaction type, which include (string):
<ul>
<li><strong>Issued</strong> – a card allocated to a cardholder and loaded.</li>
<li><strong>Redeemed</strong> – spend.</li>
<li><strong>Cancelled</strong> – removing a load from a cardholders account.</li>
<li><strong>Authorised</strong> – an authorisation, the first level of a transaction.</li>
</ul>
</li>
<li><strong>Method</strong> – this is how the transaction was initiated or processed, which include (string):
<ul>
<li><strong>Web</strong></li>
<li><strong>SMS</strong></li>
<li><strong>Batch</strong></li>
<li><strong>Terminal</strong></li>
<li><strong>Application</strong></li>
<li><strong>IVR</strong></li>
<li><strong>n/a</strong></li>
</ul>
</li>
<li><strong>Value</strong> – this is the amount of the transaction (decimal).</li>
<li><strong>Description</strong> – this describes the transaction (string).</li>
<li><strong>SequenceNumber</strong> – A sequence number is essentially another card identifier which tells you the actual sequence number of the card/voucher (string).</li>
</ul>

<h2>Report format</h2>

<h2>Report time frame</h2>

<h2>Report sample</h2>

<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2024/02/CampaignName_DailySalesRedmeptionStatement-YYYY-MM-DD.csv">CampaignName_DailySalesRedmeptionStatement YYYY-MM-DD.csv</a></p>
</a></p></h2></h2></h2></strong></li></strong></li></strong></li></strong></li></strong></li></strong></li></strong></li></strong></li></strong></li></strong></li></ul></strong></li></strong></li></strong></li></strong></li></strong></li></ul></strong></li></strong></li></strong></li></strong></li></strong></strong></li></strong></li></strong></li></ul></p></p>
