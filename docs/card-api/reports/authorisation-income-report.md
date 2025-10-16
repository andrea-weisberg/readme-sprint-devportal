---
title: Authorisation income report
deprecated: false
hidden: false
metadata:
  robots: index
---
<p data-pm-slice="1 1 []">This daily report provides client’s with transaction markup data to support their internal reporting and P & L reconciliation. The report includes the following details:</p>
<ul>
<li><strong>CampaignID</strong> – ID number of client’s campaign.</li>
<li><strong>CampaignName </strong>– name of client’s campaign.</li>
<li><strong>TransactionDate</strong> – this is the date the transaction was authorised.</li>
<li><strong>AccumulatedTransactionOriginalAmount</strong> – this is the total value of all the original amounts of the transactions without any markup.</li>
<li><strong>AccumulatedMarkupAmount</strong> – this is the total value of all the markup amounts of the transactions.</li>
<li><strong>AccumulatedTransactionAuthorisedAmount</strong> – this is the total value of all the transaction authorised amounts.</li>
<li><strong>TransactionOriginalAmount</strong> – this is the value of the transaction without any markup.</li>
<li><strong>TransactionMarkupAmount </strong>– this is the value of the markup amount.</li>
<li><strong>TransactionAuthorisedAmount</strong> – this is the value of the full transaction including markup.</li>
<li><strong>TransactionDescription</strong> – it’s the merchant’s description.</li>
<li><strong>TransactionID</strong> – it’s a reference for the transaction.</li>
<li><strong>TransactionType</strong> –  ch2aracter string identifying the type of transaction:
<ul>
<li>0 = POS</li>
<li>1 = ATM</li>
<li>2 = Adjustments</li>
</ul>
</li>
<li><strong>WalletReference </strong>– this is a unique customer reference for the card.</li>
<li><strong>SystemDate</strong> – this is Paymentology’s system date in UTC +2 time zone.</li>
<li><strong>SequenceNumber</strong> – this is a unique sequence card identifier showing a running number for the cards created.</li>
<li><strong>TrackingNumber</strong> – this is a unique 15-digit tracking identifier for the card.</li>
</ul>
<p> </p>



\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report format</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"FORMAT"\},\{"c":"FILE NAME"\},\{"c":"FREQUENCY"\},\{"c":"ACCESSIBILITY"\}],"caption":false,"body":[[\{"c":"CSV"\},\{"c":"[CampaignName]_authorisationincomereport_[YYYY_MM_DD].csv"\},\{"c":"Daily"\},\{"c":"HTTP get request"\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report time frame</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"UTC +2"\},\{"c":"UTC +7"\},\{"c":"REMARKS"\}],"caption":false,"body":[[\{"c":"09:45"\},\{"c":"14:45"\},\{"c":"When the report is generated, the timeframe of all data captured in this report is from 00:00:00 to \n 11:59:59 the previous day in:\n• System time zone UTC+2\n• Asia client time zone UTC+7"\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report sample</h2>
<p><img loading="lazy" decoding="async" class="alignleft size-full wp-image-4102" src="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_authorisationincomereport_YYYY_MM_DD-.png" alt="" width="4092" height="2025" srcset="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_authorisationincomereport_YYYY_MM_DD-.png 4092w, https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_authorisationincomereport_YYYY_MM_DD--300x148.png 300w, https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_authorisationincomereport_YYYY_MM_DD--1024x507.png 1024w, https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_authorisationincomereport_YYYY_MM_DD--768x380.png 768w, https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_authorisationincomereport_YYYY_MM_DD--1536x760.png 1536w, https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_authorisationincomereport_YYYY_MM_DD--2048x1013.png 2048w" sizes="auto, (max-width: 4092px) 100vw, 4092px" /></p>



\{/* unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21\}},"text":"<p>Note: file will automatically download upon clicking link</p>\n"}]} */}


<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_authorisationincomereport_YYYY_MM_DD.csv">CampaignName_authorisationincomereport_YYYY_MM_DD.csv</a></p>



\{/* spacing: desktop=20, mobile=10 */\}
