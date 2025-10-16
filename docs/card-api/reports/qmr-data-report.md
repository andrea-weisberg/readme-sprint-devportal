---
title: QMR data report
deprecated: false
hidden: false
metadata:
  robots: index
---
<p>Paymentology’s QMR (Quarterly Mastercard Report) data report contains transaction data and card/account data for the given quarter. The report can be provided to clients using Mastercard, to assist clients with their Mastercard quarterly reporting requirements.</p>
<p>The report includes the following:</p>
<h3>Cardholder activity</h3>
<ul>
<li><strong>Purchases</strong> – transaction count and volume of cleared transactions enacted to purchase goods or services.</li>
<li><strong>Funding MCC 4829</strong> – transaction count and volume of cleared funding transactions under MCC (Merchant Category Code) 4829 (Money Transfer)</li>
<li><strong>Funding MCC 6540</strong> – transaction count and volume of cleared funding transactions under MCC (Merchant Category Code) 6540 (Point of Interaction Funding Transactions)</li>
<li><strong>Funding MCC 6538</strong> – transaction count and volume of cleared funding transactions under MCC (Merchant Category Code) 6538 (MoneySend Funding)</li>
<li><strong>Cash Disbursements</strong> – transaction count and volume of cleared transactions enacted to withdraw cash either at an ATM, Branch, Teller, Balance Transfer or Convenience Check (used to obtain cash).</li>
<li><strong>Breakdown of Cash Disbursements</strong> – transaction count and volume of cleared transactions enacted to withdraw cash at an ATM and Teller.</li>
<li><strong>Refunds/Returns/Credits</strong> – total or partial refund of the amount of a previously cleared transaction for the return of unwanted goods or services. This can also be known as a reversal.</li>
<li><strong>Payment Consumer</strong> – transaction count and volume of cleared Money Send payment transactions identified as consumer initiated.</li>
<li><strong>Payment Government</strong> – transaction count and volume of cleared Money Send payment transactions identified as consumer initiated.</li>
<li><strong>Payment Gaming Gambling</strong> – transaction count and volume of cleared Money Send payment transactions identified as business or government initiated.</li>
</ul>
<p>The Cardholder Activity section is split by the following:</p>
<ul>
<li><strong>Domestic On-us</strong> – a cleared transaction made at a merchant within the issuing country and the Issuing Bank and Acquiring Bank are the same.</li>
<li><strong>Domestic Other Brand/Non-Mastercard Processed</strong> – a cleared transaction made at a merchant within the issuing country where the Issuing Bank and Acquiring Bank differ, Mastercard interchange is not applied, a competing domestic brand/scheme is on the card and present at the POS or ATM and the transaction is intentionally routed through the competing domestic brand/scheme.</li>
<li><strong>Domestic Interchange</strong> – a cleared transaction made at a merchant within the issuing country and the Issuing Bank and Acquiring Bank differ.</li>
<li><strong>International</strong> <strong>Within Region</strong> – a cleared transaction where the Issuing country and Acquiring country differ and both are in the EEA (European Economic Area).</li>
<li><strong>International Outside Region</strong> – a cleared transaction where either the Issuer <strong>or</strong> Acquirer is outside the EEA.</li>
</ul>
<h3>Accounts/Cards</h3>
<ul>
<li><strong>Accounts at beginning of quarter</strong> – number of open and temporarily blocked accounts on the last day of the previous quarter.</li>
<li><strong>New accounts obtained during quarter</strong> – number of accounts added to the card program since the end of the previous quarter.</li>
<li><strong>Accounts terminated during quarter</strong> – number of accounts retired or expired since the end of the previous quarter.</li>
<li><strong>Accounts at end of quarter</strong> – number of open and temporarily blocked accounts on the last day of the reported quarter.</li>
<li><strong>Accounts with at least one transaction during quarter</strong> – number of accounts that made at least one transaction during the reported quarter.</li>
<li><strong>Cards at beginning of quarter</strong> – number of open and temporarily blocked cards on the last day of the previous quarter.</li>
<li><strong>New cards</strong> – number of cards added to the card program since the end of the previous quarter.</li>
<li><strong>Cards at end of quarter</strong> – number of open and temporarily blocked cards on the last day of the reported quarter.</li>
<li><strong>Cards with at least one transaction during quarter</strong> – number of cards that made at least one transaction during the reported quarter.</li>
</ul>
<h3>Charged-Off Losses</h3>
<p>Unless otherwise instructed by Paymentology, this data will be left blank or contain a 0. The data for this section is to be collated and reported by the client.</p>
<h3>Card Feature Details</h3>
<ul>
<li><strong>Breakout of EMV-compliant Chip enabled Cards</strong> – total number of cards at the end of the reported quarter that have the EMV-compliant Chip.</li>
<li><strong>Total Mastercard contactless Cards issued</strong> – total number of physical plastic contactless cards at the end of the reported quarter (both magstripe and EMV compliant contactless cards) and the associated transactions and volume on those cards and devices. Contactless cards use NFC technology.</li>
<li><strong>Total number of Cards enrolled in the Mastercard Biometric Card program</strong> – total number of physical Mastercard biometric cards in market. Biometric refers to fingerprint sensor-enabled payment cards.</li>
<li><strong>Total number of Mastercard Digital Accounts</strong> – total number of Mastercard Digital Accounts at the end of the reported quarter.</li>
<li><strong>Total number of virtual, non-reloadable prepaid and full metal body cards</strong> – total number of virtual, non-reloadable prepaid and full metal body cards at the end of the reported quarter. These types of cards do not have contactless capability.</li>
</ul>



\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report format</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"FORMAT"\},\{"c":"FILE NAME"\},\{"c":"FREQUENCY"\},\{"c":"ACCESSIBILITY"\}],"caption":false,"body":[[\{"c":"XLS"\},\{"c":"QMR_[BIN]_[ClientName]_[YYYYQQ].xls"\},\{"c":"Quarterly"\},\{"c":"Via email"\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report time frame</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"TIME, DATE"\},\{"c":"REMARKS"\}],"caption":false,"body":[[\{"c":"Clients are required to liaise with their client executive to confirm when they will be scheduled to receive this report."\},\{"c":"Quarterly reports are produced as follows: Q1 - (January, February, March) produced April Q2 - (April, May, June) produced July Q3 - (July, August, September) produced October Q4 - (October, November, December) produced January."\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report sample</h2>



\{/* unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21\}},"text":"<p>Note: file will automatically download upon clicking link</p>\n"}]} */}


<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2025/01/QMR_BIN_ClientName_YYYYQQ.xls">QMR_BIN_ClientName_YYYYQQ</a></p>
