---
title: VAU transaction report
deprecated: false
hidden: false
metadata:
  robots: index
original_path: companion-api/reports
---
<p>The purpose of this report is to send to the client the transactions that are still being made to a certain card that was already sent to VISA via the VAU file.</p>
<p data-renderer-start-pos="241">So for example if a card was sent to VISA in a VAU file on the date <span class="date-lozenger-container"><span class="date-node" data-node-type="date" data-timestamp="1694995200000">Sep 18, 2023</span></span> and transactions are still happening after the file was generated the card will be on the report.</p>
<p>The VAU Transaction Report has the following fields:</p>
<ul>
<li><strong>Wallet Reference</strong> – this is the unique identifier of the wallet (12 character string).</li>
<li><strong>Merchant Name</strong> – this is the name of the merchant where the transaction took place (string).</li>
<li><strong>Pre Authorisation Date</strong> – date of the pre-authorisation (MM/DD/YYYY HH:MM:SS).</li>
<li><strong>Vau File System Date</strong> – VAU file generation date (MM/DD/YYYY HH:MM:SS).</li>
<li><strong>Voucher ID</strong> – corresponds to the transaction ID associated with the voucher (integer).</li>
<li><strong>TrackingNumber</strong> – this is the unique identifier linked to the voucher number (15 character string).</li>
<li><strong>Voucher Number</strong> – the voucher number sent to VISA in the VAU file (16 character string).</li>
<li><strong>Expiry Date</strong> – the old expiry date sent to VISA in the VAU file (YYMM).</li>
<li><strong>Service Identifier</strong> – this identifies the type of change that occurred on the card (string).</li>
</ul>



\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report format</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"FORMAT"\},\{"c":"FILE NAME"\},\{"c":"FREQUENCY"\},\{"c":"ACCESSIBILITY"\}],"caption":false,"body":[[\{"c":"CSV"\},\{"c":"VAUTransactionsReport[ClientName]_[report generation date YYYY-MM-DD].csv"\},\{"c":"Monthly"\},\{"c":"Sent via email"\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report time frame</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"UTC +2"\},\{"c":"UTC +7"\},\{"c":"REMARKS"\}],"caption":false,"body":[[\{"c":"10:00"\},\{"c":"15:00"\},\{"c":"The report is generated at the provided times on the 1st of every month and issued to Visa clients via email."\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report sample</h2>



\{/* unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21\}},"text":"<p>Note: file will automatically download upon clicking link.</p>\n"}]} */}


<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2024/02/VAUtransactionsReportClientName_YYYY-MM-DD.csv">VAUtransactionsReportClientName_YYYY-MM-DD.csv</a></p>
