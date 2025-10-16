---
title: Apple Pay monthly usage frequency report
deprecated: false
hidden: false
metadata:
  robots: index
original_path: card-api/reports
---
<p>For clients using Paymentology’s tokenization, Paymentology can issue monthly reports to clients to assist in compiling their Apple report through the Apple Partner Connect platform.</p>
<p>This report refers to the number of times a specific account is used to make a transaction in a given month. This includes any type of Apple Pay transaction i.e. POS or eCommerce.</p>
<p>The report includes the following details:</p>
<ul>
<li><strong>Month</strong> – the month the report data is based on.</li>
<li><strong>Not used in current month</strong> – this is the total count of available DPANs that did not make any successful transaction in the given month.</li>
<li><strong>Once(1) in current month</strong> – this is the total count of available DPANs that have successfully transacted exactly one time in the given month.</li>
<li><strong>Twice(2) in current month</strong> – this is the total count of available DPANs that have successfully transacted exactly two times in the given month.</li>
<li><strong>3 times in current month</strong> – this is the total count of available DPANs that have successfully transacted exactly three times in the given month.</li>
<li><strong>4 times in current month</strong> – this is the total count of available DPANs that have successfully transacted exactly four times in the given month.</li>
<li><strong>5 times in current month</strong> – this is the total count of available DPANs that have successfully transacted exactly five times in the given month.</li>
<li><strong>6 times in current month</strong> – this is the total count of available DPANs that have successfully transacted exactly six times in the given month.</li>
<li><strong>7 times in current month</strong> – this is the total count of available DPANs that have successfully transacted exactly seven times in the given month.</li>
<li><strong>8 times in current month</strong> – this is the total count of available DPANs that have successfully transacted exactly eight times in the given month.</li>
<li><strong>9 times in current month</strong> – this is the total count of available DPANs that have successfully transacted exactly nine times in the given month.</li>
<li><strong>>= 10 times in current month</strong> – this is the total count of available DPANs that have successfully transacted at least ten times in the given month.</li>
<li><strong>Total</strong> – this is the total count of available DPANs in the given month.</li>
<li><strong>Active DPAN rate </strong>– this is the percentage of DPANs that have transacted in the given month of the total available DPANs. An available DPAN is defined as a token that is provisioned and available for transacting i.e. it is not temporarily blocked.</li>
</ul>



\{/* unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21\}},"text":"<p>DPAN (Device Primary Account Number) – A token that acts as a surrogate for the customer’s card number and is used to make contactless and eCommerce transactions using an Apple Pay device.</p>\n"},\{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21\}},"text":"<p>Only settled transactions are counted.</p>\n"}]} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report format</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"FORMAT"\},\{"c":"FILE NAME"\},\{"c":"FREQUENCY"\},\{"c":"ACCESSIBILITY"\}],"caption":false,"body":[[\{"c":"XLS"\},\{"c":"[CampaignName]_ApplePay Monthly Frequency Report [Month] YYYY.xls"\},\{"c":"Monthly"\},\{"c":"Via email."\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report time frame</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"UTC +2"\},\{"c":"UTC +7"\},\{"c":"REMARKS"\}],"caption":false,"body":[[\{"c":"02:00"\},\{"c":"07:00"\},\{"c":"Monthly Apple Pay reports are produced on day 2 of the following month."\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report sample</h2>
<p><img loading="lazy" decoding="async" src="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_ApplePay-Monthly-Frequency-Report-Month-YYYY-_.png" alt="" width="1280" height="720" class="alignleft size-full wp-image-3963" srcset="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_ApplePay-Monthly-Frequency-Report-Month-YYYY-_.png 1280w, https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_ApplePay-Monthly-Frequency-Report-Month-YYYY-_-300x169.png 300w, https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_ApplePay-Monthly-Frequency-Report-Month-YYYY-_-1024x576.png 1024w, https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_ApplePay-Monthly-Frequency-Report-Month-YYYY-_-768x432.png 768w" sizes="auto, (max-width: 1280px) 100vw, 1280px" /></p>



\{/* unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21\}},"text":"<p><strong>Note: file will automatically download upon clicking link</strong></p>\n"}]} */}


<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_ApplePay-Monthly-Frequency-Report-Month-YYYY.xls">CampaignName_ApplePay Monthly Frequency Report Month YYYY.xls</a></p>



\{/* spacing: desktop=20, mobile=10 */\}
