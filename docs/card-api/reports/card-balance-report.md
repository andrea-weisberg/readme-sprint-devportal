---
title: Card balance report
deprecated: false
hidden: false
metadata:
  robots: index
original_path: card-api/reports
---
<p>This report provides clients with card details such as, current available balance, last load and lifetime expenditure. It is available for each Campaign.</p>
<p>The report includes the following details:</p>
<ul>
<li><strong>Campaign Name</strong> &#8211; name of client’s card program.</li>
<li><strong>Voucher Number </strong>&#8211; the customer’s card number.</li>
<li><strong>Sequence Number</strong> &#8211; this is a unique sequence card identifier showing a running number for the cards created.</li>
<li><strong>Tracking Number</strong> &#8211; this is a unique 15-digit tracking identifier for the card.</li>
<li><strong>WalletReference</strong> &#8211; this is a unique customer reference for the card.</li>
<li><strong>Balance</strong> &#8211; this is the amount available on the card.</li>
<li><strong>Last Load Amount</strong> &#8211; this is the value of the most recent load/top-up made to the card.</li>
<li><strong>Last Load Date</strong> &#8211; this is the date the most recent load/top up was received on the card.</li>
<li><strong>Last Load Merchant</strong> &#8211; this is the description of the merchant the <strong>Last Load</strong> was made through.</li>
<li><strong>Load Total</strong> &#8211; this is the total value the card has been loaded since it was first issued.</li>
<li><strong>Authorisation Total </strong>&#8211; this is the total value of all successful transactions the card has made since it was first issued.</li>
<li><strong>Cancelled </strong>&#8211; this advises whether the card is currently in a cancelled state at the time of the report.</li>
<li><strong>Stopped</strong> &#8211; this advises whether the card is currently in a stopped state at the time of the report.</li>
<li><strong>Retired </strong>&#8211; this advises whether the card is in a retired state at the time of the report.</li>
<li><strong>Voucher Expiry Date</strong> &#8211; specifies the date in which the card expires.</li>
</ul>
<p>&nbsp;</p>



<!-- spacing: desktop=20, mobile=10 -->


<h2>Report format</h2>



<!-- unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"FORMAT"},{"c":"FILE NAME"},{"c":"FREQUENCY"},{"c":"ACCESSIBILITY"}],"caption":false,"body":[[{"c":"CSV"},{"c":"[CampaignName]_cardbalance_[YYYY]_[MM]_[DD].csv"},{"c":"Daily"},{"c":"HTTP get request"}]]}} -->


<!-- spacing: desktop=20, mobile=10 -->


<h2>Report time frame</h2>



<!-- unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"UTC +2"},{"c":"UTC +7"},{"c":"REMARKS"}],"caption":false,"body":[[{"c":"08:00"},{"c":"13:00"},{"c":"When the report is generated, the timeframe of all captured data in this report is from 00:00:00   to 11:59:59 of the previous day:\n• System time zone UTC+2\n• Asia client time zone UTC+7"}]]}} -->


<!-- spacing: desktop=20, mobile=10 -->


<h2>Report sample</h2>
<p><img loading="lazy" decoding="async" class="alignleft size-full wp-image-4099" src="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_cardbalances_YYYY_MM_DD-.png" alt="" width="4120" height="1613" srcset="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_cardbalances_YYYY_MM_DD-.png 4120w, https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_cardbalances_YYYY_MM_DD--300x117.png 300w, https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_cardbalances_YYYY_MM_DD--1024x401.png 1024w, https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_cardbalances_YYYY_MM_DD--768x301.png 768w, https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_cardbalances_YYYY_MM_DD--1536x601.png 1536w, https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_cardbalances_YYYY_MM_DD--2048x802.png 2048w" sizes="auto, (max-width: 4120px) 100vw, 4120px" /></p>



<!-- unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21}},"text":"<p>Note: file will automatically download upon clicking link</p>\n"}]} -->


<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_cardbalances_YYYY_MM_DD.csv">CampaignName_cardbalances_YYYY_MM_DD.csv</a></p>



<!-- spacing: desktop=20, mobile=10 -->
