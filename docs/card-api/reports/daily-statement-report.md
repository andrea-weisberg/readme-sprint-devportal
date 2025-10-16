---
title: Daily statement report
deprecated: false
hidden: false
metadata:
  robots: index
original_path: card-api/reports
---
<p>The daily statement report can be used by client&#8217;s to assist with their reconciliation and program activity reporting.</p>
<p>The report includes the following details:</p>
<ul>
<li><strong>TransactionID</strong> &#8211; it&#8217;s a unique reference for the transaction.</li>
<li><strong>TransactionDate</strong> &#8211; this is the date and time of the transaction.</li>
<li><strong>TerminalTransactionDate</strong> &#8211; this is the data and time of the initial transaction if the transaction has settled.</li>
<li><strong>VoucherNumber</strong> &#8211; the customer&#8217;s card number.</li>
<li><strong>VoucherSequenceNumber</strong> -this is a unique sequence card identifier showing a running number for the cards created.</li>
<li><strong>VoucherTrackingNumber</strong> &#8211; this is a unique 15-digit tracking identifier for the card.</li>
<li><strong>TransactionAmount</strong> &#8211; the transaction value in cents. For example, a value of 4215 will mean 42.15. Amount is in the card campaign’s billing currency.</li>
<li><strong>TransactionType</strong> &#8211; it can be marked as any of the following:
<ul>
<li>0 – POS transaction</li>
<li>1 – ATM transaction</li>
<li>2 – Adjustment</li>
</ul>
</li>
<li><strong>MerchantCode</strong> &#8211; this is the identifier code of the merchant.</li>
<li><strong>MerchantName</strong> &#8211; it&#8217;s the merchant&#8217;s name.</li>
<li><strong>TransactionInfo</strong> &#8211; it’s the merchant’s or adjustment description.</li>
<li><strong>TransactionOperator</strong> &#8211; it&#8217;s the identifier of the operator if manually processed and provided.</li>
</ul>



<!-- spacing: desktop=20, mobile=10 -->


<h2>Report format</h2>



<!-- unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"FORMAT"},{"c":"FILE NAME"},{"c":"FREQUENCY"},{"c":"ACCESSIBILITY"}],"caption":false,"body":[[{"c":"CSV"},{"c":"[CampaignName]_Statement_[YYYYMMDD].csv"},{"c":"Daily"},{"c":"HTTP get request"}]]}} -->


<!-- spacing: desktop=20, mobile=10 -->


<h2>Report time frame</h2>



<!-- unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"UTC +2"},{"c":"UTC +7"},{"c":"REMARKS"}],"caption":false,"body":[[{"c":"08:05"},{"c":"08:05"},{"c":"Generated daily in the client's campaign timezone."}]]}} -->


<!-- spacing: desktop=20, mobile=10 -->


<h2>Report sample</h2>



<!-- unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21}},"text":"<p>Note: file will automatically download upon clicking link</p>\n"}]} -->


<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_Statement_YYYYMMDD.csv">CampaignName_Statement_YYYYMMDD.csv</a></p>
