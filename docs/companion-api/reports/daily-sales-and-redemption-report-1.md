---
title: Daily sales and redemption report
deprecated: false
hidden: false
metadata:
  robots: index
original_path: companion-api/reports
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



\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report format</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"FORMAT"\},\{"c":"FILE NAME"\},\{"c":"FREQUENCY"\},\{"c":"ACCESSIBILITY"\}],"caption":false,"body":[[\{"c":"CSV"\},\{"c":"[CampaignName]_DailySalesRedemptionStatement [YYYY-MM-DD].csv"\},\{"c":"Daily"\},\{"c":"Via download link"\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report time frame</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"UTC +2"\},\{"c":"UTC +7"\}],"caption":false,"body":[[\{"c":"08:00"\},\{"c":"13:00"\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report sample</h2>



\{/* unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21\}},"text":"<p>Note: file will automatically download upon clicking link.</p>\n"}]} */}


<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2024/02/CampaignName_DailySalesRedmeptionStatement-YYYY-MM-DD.csv">CampaignName_DailySalesRedmeptionStatement YYYY-MM-DD.csv</a></p>
