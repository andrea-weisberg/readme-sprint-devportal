---
title: Google Pay monthly report
deprecated: false
hidden: false
metadata:
  robots: index
original_path: card-api/reports
---
<p>A report which provides detailed information about cards that were tokenised to a Google Pay wallet within a given month. Client’s can use the data from this report to fulfil their Google Pay reporting requirements.</p>
<p>The report includes the following details:</p>
<ul>
<li><strong>FirstLastName </strong>– Customer’s first and last name</li>
<li><strong>BillingPostalCode </strong>– Customer’s postal code</li>
<li><strong>BillingStreetAddress </strong>– Customer’s postal street address</li>
<li><strong>BillingCountryCode</strong> – Customer’s postal country</li>
<li><strong>BillingCity</strong> – Customer’s postal city</li>
<li><strong>BillingAdministrativeArea</strong> – Customer’s postal region or state</li>
<li><strong>FullPhoneNumber </strong>– Customer’s contact number</li>
<li><strong>OpaquePaymentCard</strong> – Google Pay tokenised card number</li>
<li><strong>FundingPrimaryAccountNumber </strong>– Voucher number/Customer’s card number</li>
<li><strong>ExpirationDate </strong>– Expiry date of <strong>OpaquePaymentCard</strong></li>
</ul>
<p> </p>



\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report format</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"FORMAT"\},\{"c":"FILE NAME"\},\{"c":"FREQUENCY"\},\{"c":"ACCESSIBILITY"\}],"caption":false,"body":[[\{"c":"CSV"\},\{"c":"[CampaignName]googlepaymonthlyreport[MMM YYYY].csv"\},\{"c":"Monthly"\},\{"c":"HTTP get request and email."\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report time frame</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"UTC +2"\},\{"c":"UTC +7"\},\{"c":"REMARKS"\}],"caption":false,"body":[[\{"c":"12:00"\},\{"c":"17:00"\},\{"c":"The report is generated on day 1 of every month, the timeframe of all the captured data in this report is from 00:00:00 day 1 of previous month to 11:59:59 of last day of previous month in:\n• System time zone UTC+2\n• Asia client time zone UTC+7."\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report sample</h2>
<p><img loading="lazy" decoding="async" class="alignleft size-full wp-image-4095" src="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_googlepay_monthlyreport_MMM-YYYY-.png" alt="" width="4083" height="976" srcset="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_googlepay_monthlyreport_MMM-YYYY-.png 4083w, https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_googlepay_monthlyreport_MMM-YYYY--300x72.png 300w, https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_googlepay_monthlyreport_MMM-YYYY--1024x245.png 1024w, https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_googlepay_monthlyreport_MMM-YYYY--768x184.png 768w, https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_googlepay_monthlyreport_MMM-YYYY--1536x367.png 1536w, https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_googlepay_monthlyreport_MMM-YYYY--2048x490.png 2048w" sizes="auto, (max-width: 4083px) 100vw, 4083px" /></p>



\{/* unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21\}},"text":"<p>Note: file will automatically download upon clicking link</p>\n"}]} */}


<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignNamegooglepaymonthlyreportMMM-YYYY.csv">CampaignNamegooglepaymonthlyreportMMM YYYY.csv</a></p>



\{/* spacing: desktop=20, mobile=10 */\}
