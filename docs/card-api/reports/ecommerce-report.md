---
title: eCommerce report
deprecated: false
hidden: false
metadata:
  robots: index
---
<p data-renderer-start-pos="25">A report that shows successful and failed Ecommerce transactions along with associated eCommerce fees.</p>
<p data-renderer-start-pos="25">The report includes the following details:</p>
<ul>
<li data-renderer-start-pos="71"><strong data-renderer-mark="true">TransactionID – </strong>it’s a reference for the transaction</li>
<li data-renderer-start-pos="127"><strong data-renderer-mark="true">TrackingNumber</strong> – this is a unique 15-digit tracking identifier for the card.</li>
<li data-renderer-start-pos="207"><strong data-renderer-mark="true">TransactionDescription </strong>– this is a description of the merchant.</li>
<li data-renderer-start-pos="274"><strong data-renderer-mark="true">TransactionAmount</strong> – the value of the transaction</li>
<li data-renderer-start-pos="326"><strong data-renderer-mark="true">TransactionDate </strong>– This is the authorization date of the transaction</li>
<li data-renderer-start-pos="397"><strong data-renderer-mark="true">MerchantIdentitifer</strong> – this is numeric identifier of the merchant. Usually 15 digits.</li>
<li data-renderer-start-pos="485"><strong data-renderer-mark="true">Fee</strong> – this is the value of a fee the card has incurred for the transaction. Fee type must be one of the below:
<ul>
<li data-renderer-start-pos="592">51 – Ecommerce Fee</li>
<li data-renderer-start-pos="614">52 – Online Fee</li>
<li data-renderer-start-pos="633">6 – POS Purchase Fee</li>
</ul>
</li>
<li data-renderer-start-pos="702"><strong data-renderer-mark="true">3DS </strong>– specifies whether 3DS authentication occurred prior to the authorisation.</li>
<li data-renderer-start-pos="785"><strong data-renderer-mark="true">SuccessfulTransaction</strong> – specifies whether the transaction was approved or declined.</li>
<li data-renderer-start-pos="872"><strong data-renderer-mark="true">TransactionFeeID</strong> – the identifier of the transaction fee incurred.</li>
<li data-renderer-start-pos="942"><strong data-renderer-mark="true">TransactionFeeDescription</strong> – describes the transaction fee.</li>
<li data-renderer-start-pos="1004"><strong data-renderer-mark="true">TransactionFeeDate</strong> – the date in which the transaction fee was applied.</li>
<li data-renderer-start-pos="1079"><strong data-renderer-mark="true">DeclineReason</strong> – describes why the transaction was declined. If the transaction was successful then this filed is left blank.</li>
<li data-renderer-start-pos="1207"><strong data-renderer-mark="true">CaptureType</strong><em data-renderer-mark="true"> – </em>Capture type must be one of the below:
<ul>
<li data-renderer-start-pos="1256">ECOM – Transaction captured online</li>
<li data-renderer-start-pos="1294">MAG – Magnetic Stripe captured transaction</li>
<li data-renderer-start-pos="1340">MAN – Manually captured transaction</li>
<li data-renderer-start-pos="1379">ECOF – Online Card On File transaction</li>
</ul>
</li>
<li data-renderer-start-pos="1425"><strong data-renderer-mark="true">CaptureMode</strong> – this is the respective capture mode of the card’s transaction. Capture Mode must be one of the below:
<ul>
<li data-renderer-start-pos="1537">MAG – Magnetic Stripe captured transaction</li>
<li data-renderer-start-pos="1583">EMV – Electronic chip captured transaction</li>
<li data-renderer-start-pos="1629">ECOM – Transaction captured online (with no 3DS authentication)</li>
<li data-renderer-start-pos="1696">3DS – Transaction captured online using 3DS authentication</li>
<li data-renderer-start-pos="1758">MAN – Manually captured transaction</li>
<li data-renderer-start-pos="1797">NFC – Transaction captured via a Near Field Communication device</li>
</ul>
</li>
<li data-renderer-start-pos="1869"><strong data-renderer-mark="true">Recurring</strong> – specifies whether the transactions is a once off or recurring through COF method.</li>
</ul>
<p> </p>



\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report format</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"FORMAT"\},\{"c":"FILE NAME"\},\{"c":"FREQUENCY"\},\{"c":"ACCESSIBILITY"\}],"caption":false,"body":[[\{"c":"CSV"\},\{"c":"EcommerceTransactions_[CampaignName]_[YYYYMMDD].csv"\},\{"c":"Daily"\},\{"c":"HTTP get request"\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report time frame</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"UTC +2"\},\{"c":"UTC +7"\},\{"c":"REMARKS"\}],"caption":false,"body":[[\{"c":"09:00"\},\{"c":"14:00"\},\{"c":"When the report is generated, the timeframe of all captured data in this report is from 00:00:00   to 11:59:59 of the previous day:\n• System time zone UTC+2\n• Asia client time zone UTC+7"\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report sample</h2>
<p><img loading="lazy" decoding="async" class="alignleft size-full wp-image-4083" src="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/EcommerceTransactions_CampaignName_YYYYMMDD-.png" alt="" width="4115" height="1636" srcset="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/EcommerceTransactions_CampaignName_YYYYMMDD-.png 4115w, https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/EcommerceTransactions_CampaignName_YYYYMMDD--300x119.png 300w, https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/EcommerceTransactions_CampaignName_YYYYMMDD--1024x407.png 1024w, https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/EcommerceTransactions_CampaignName_YYYYMMDD--768x305.png 768w, https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/EcommerceTransactions_CampaignName_YYYYMMDD--1536x611.png 1536w, https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/EcommerceTransactions_CampaignName_YYYYMMDD--2048x814.png 2048w" sizes="auto, (max-width: 4115px) 100vw, 4115px" /></p>



\{/* unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21\}},"text":"<p>Note: file will automatically download upon clicking link</p>\n"}]} */}


<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/EcommerceTransactions_CampaignName_YYYYMMDD.csv">EcommerceTransactions_CampaignName_YYYYMMDD.csv</a></p>



\{/* spacing: desktop=20, mobile=10 */\}
