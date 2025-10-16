---
title: Apple Pay quarterly fee billing report
deprecated: false
hidden: false
metadata:
  robots: index
original_path: card-api/reports
---
<p data-pm-slice="1 1 []">For clients using Paymentology’s tokenization, Paymentology can issue a quarterly report to clients to utilize the report data to compile their Apple report through the Apple Partner Connect platform.</p>
<p>The report includes the following details:</p>
<ul>
<li><strong>Total Debit Spend</strong> &#8211; this is the total settled transaction value of Apple Pay transactions for the given quarter. This includes contactless and eCommerce transactions that have been made using Apple Pay.</li>
<li><strong>POS debit spend share</strong> &#8211; this is the percentage of <strong>Total Debit Spend</strong> that was made at Point of Sale (POS) using Apple Pay. This includes the following Capture Mode&#8217;s:
<ul>
<li>EMV &#8211; chip cards</li>
<li>NFC &#8211; Near Field Communication devices</li>
<li>MAG &#8211; Magnetic stripe</li>
<li>MAN &#8211; Manual entry</li>
</ul>
</li>
<li><strong>E-commerce debit spend share</strong> &#8211; this is the percentage of <strong>Total Debit Spend</strong> that was eCommerce using Apple Pay. This includes the following Capture Mode&#8217;s:
<ul>
<li>ECOM &#8211; eCommerce</li>
<li>ECOF &#8211; eCommerce Card on File</li>
</ul>
</li>
<li><strong>Active Debit DPANS</strong> &#8211; this is the total number of cards that made at least one successful spend.</li>
</ul>



<!-- unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21}},"text":"<p>DPAN (Device Primary Account Number) &#8211; A token that acts as a surrogate for the customer’s card number and is used to make contactless and e-commerce transactions using an Apple device.</p>\n"},{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21}},"text":"<p>All amounts reported are in the cardholder billing currency.</p>\n"}]} -->


<!-- spacing: desktop=20, mobile=10 -->


<h2>Report format</h2>



<!-- unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"FORMAT"},{"c":"FILE NAME"},{"c":"FREQUENCY"},{"c":"ACCESSIBILITY"}],"caption":false,"body":[[{"c":"XLS"},{"c":"[CampaignName]_ApplePay Quarterly Fee Billing Report [Month] YYYY.xls"},{"c":"Quarterly"},{"c":"Via email"}]]}} -->


<!-- spacing: desktop=20, mobile=10 -->


<h2>Report time frame</h2>



<!-- unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"UTC +2"},{"c":"UTC +7"},{"c":"REMARKS"}],"caption":false,"body":[[{"c":"02:00, day 2 of month produced"},{"c":"07:00, day 2 of month produced"},{"c":"Quarterly reports are produced as follows:\nQ1 - (January, February, March) produced April\nQ2 - (April, May, June) produced July\nQ3 -  (July, August, September) produced October\nQ4 - (October, November, December)  produced January."}]]}} -->


<!-- spacing: desktop=20, mobile=10 -->


<h2>Report sample</h2>
<p><img loading="lazy" decoding="async" src="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_ApplePay-Quarterly-Fee-Billing-Report-Month-YYYY-003.png" alt="" width="1280" height="297" class="alignleft size-full wp-image-3982" srcset="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_ApplePay-Quarterly-Fee-Billing-Report-Month-YYYY-003.png 1280w, https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_ApplePay-Quarterly-Fee-Billing-Report-Month-YYYY-003-300x70.png 300w, https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_ApplePay-Quarterly-Fee-Billing-Report-Month-YYYY-003-1024x238.png 1024w, https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_ApplePay-Quarterly-Fee-Billing-Report-Month-YYYY-003-768x178.png 768w" sizes="auto, (max-width: 1280px) 100vw, 1280px" /></p>



<!-- unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21}},"text":"<p><strong>Note: file will automatically download upon clicking link</strong></p>\n"}]} -->


<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_ApplePay-Quarterly-Fee-Billing-Report-Month-YYYY.xls">CampaignName_ApplePay Quarterly Fee Billing Report Month YYYY.xls</a></p>



<!-- spacing: desktop=20, mobile=10 -->
