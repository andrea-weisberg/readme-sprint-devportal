---
title: Unsettled transactions report
deprecated: false
hidden: false
metadata:
  robots: index
original_path: companion-api/reports
---
<p>This report provides client’s with a full list of unsettled transactions, it assists with overall reconciliation.</p>
<p>There are two versions of this report available:</p>
<p><a href="#UTRV1">Version 1.0</a></p>
<p><a href="#UTRV2.0">Version 2.0</a></p>
<h3><a id="UTRV1"></a>Version 1</h3>
<p>This report includes the following details:</p>
<ul>
<li><strong>CampaignName</strong> – Name of client’s campaign</li>
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



\{/* unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"\} */}


<h3><a id="UTRV2.0"></a>Version 2</h3>
<p>This report includes the following details:</p>
<ul>
<li><strong>CampaignName</strong> – Name of client’s campaign</li>
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
<li><strong>NetworkTransactionID</strong> – the Transaction ID of the transaction, as created by the card network. You can match this against the Transaction ID on the <a href="https://developer.sprint.paymentology.com/companion-api/reports/mark-off-file/">Mark-off file</a></li>
</ul>
<p> </p>



\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report format</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"FORMAT"\},\{"c":"FILE NAME"\},\{"c":"FREQUENCY"\},\{"c":"ACCESSIBILITY"\}],"caption":false,"body":[[\{"c":"CSV"\},\{"c":"[CampaignName]_UnsettledTransactionReport_[YYMMDD].csv"\},\{"c":"Hourly"\},\{"c":"HTTP get request"\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report time frame</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"REMARKS"\}],"caption":false,"body":[[\{"c":"The report is generated once per hour for every campaign."\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report sample</h2>
<p><img loading="lazy" decoding="async" class="alignleft size-full wp-image-4088" src="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_UnsettledTransactionReport_YYYYMMDD-.png" alt="" width="4092" height="1856" srcset="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_UnsettledTransactionReport_YYYYMMDD-.png 4092w, https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_UnsettledTransactionReport_YYYYMMDD--300x136.png 300w, https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_UnsettledTransactionReport_YYYYMMDD--1024x464.png 1024w, https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_UnsettledTransactionReport_YYYYMMDD--768x348.png 768w, https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_UnsettledTransactionReport_YYYYMMDD--1536x697.png 1536w, https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_UnsettledTransactionReport_YYYYMMDD--2048x929.png 2048w" sizes="auto, (max-width: 4092px) 100vw, 4092px" /></p>



\{/* unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21\}},"text":"<p><strong>Note: file will automatically download upon clicking link</strong></p>\n"}]} */}


<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_UnsettledTransactionReport_YYYYMMDD.csv">CampaignName_UnsettledTransactionReport_YYYYMMDD.csv</a></p>
<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2024/01/CampaignName_UnsettledTransactionReport_YYYYMMDD-V2sample.csv">CampaignName_UnsettledTransactionReport_YYYYMMDD.csv V2 sample</a></p>



\{/* spacing: desktop=20, mobile=10 */\}
