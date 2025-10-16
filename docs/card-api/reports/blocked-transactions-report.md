---
title: Blocked transactions report
deprecated: false
hidden: false
metadata:
  robots: index
original_path: card-api/reports
---
<p>This report lists detailed information about filtered transactions for a specific set of campaigns, during a specified date range.<br />
The report includes details about vouchers and reasons for transactions being filtered. This reports helps clients to identify if any whitelisted merchants (approved merchants) are blocked.</p>
<p>The report includes the following details:</p>
<ul>
<li><strong>Campaign</strong> – name of client’s card program (string).</li>
<li><strong>Terminal</strong> – terminal information i.e. merchant name, city, country etc (string).</li>
<li><strong>Reason</strong> – filtered transaction reason i.e. unmatched (string).</li>
<li><strong>Keyword</strong> – filtered transaction blacklist keyword i.e. Estate Service Station (string). If there is no specific keyword then field will contain N/A.</li>
<li><strong>Type</strong> – filtered transaction type, such as (string):
<ul>
<li>POS</li>
<li>ATM</li>
</ul>
</li>
<li><strong>Date Blocked</strong> –  date the the transaction was blocked (YYYY/MM/DD HH:MM:SS).</li>
<li><strong>Identifier</strong> – the voucher number (numeric string).</li>
</ul>



\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report format</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"FORMAT"\},\{"c":"FILE NAME"\},\{"c":"FREQUENCY"\},\{"c":"ACCESSIBILITY"\}],"caption":false,"body":[[\{"c":"XLS"\},\{"c":"[CampaignName] Blocked Transactions - [dateBegin:yymmdd] - [dateEnd:yymmdd].xls"\},\{"c":"Weekly"\},\{"c":"Sent via email or SFTP"\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report time frame</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"UTC +2"\},\{"c":"UTC +7"\},\{"c":"REMARKS"\}],"caption":false,"body":[[\{"c":"08:30"\},\{"c":"13:30"\},\{"c":"This report is generated weekly, only on Thursday."\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report sample</h2>



\{/* unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21\}},"text":"<p>Note: file will automatically download upon clicking link</p>\n"}]} */}


<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2024/02/CampaignName-Blocked-Transactions-231015-231022.xls">CampaignName Blocked Transactions – 231015-231022.xls</a></p>
