---
title: Card order report
deprecated: false
hidden: false
metadata:
  robots: index
original_path: card-api/reports
---
<p><span style="font-weight: 400;">If you choose the option of ordering cards via the </span><span class="xml-highlight">OrderCard</span> method, then a report will be available each day with information of the successful orders that were processed and sent to the card manufacturer.</p>
<p>The report includes the following details:</p>
<ul>
<li><strong>Card number</strong> – the masked card number.</li>
<li><strong>Wallet reference</strong> – <span style="font-weight: 400;">this column will be empty for Card API reporting.</span></li>
<li><strong>Date created</strong> – the date that card was created.</li>
</ul>



\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report format</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"FORMAT"\},\{"c":"FILE NAME"\},\{"c":"FREQUENCY"\},\{"c":"ACCESSIBILITY"\}],"caption":false,"body":[[\{"c":"CSV"\},\{"c":"[CampaignUUID]/[CampaignName]_PanDetails_[YYYYMMDD].csv"\},\{"c":"Daily"\},\{"c":"HTTP get request or client SFTP folder"\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report time frame</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"UTC +2"\},\{"c":"UTC +7"\},\{"c":"REMARKS"\}],"caption":false,"body":[[\{"c":"02:30"\},\{"c":"07:30"\},\{"c":"Paymentology creates batch order and submits to manufacturer for printing physical cards at 19:30 UTC+2, and the Card Order Report itself will be made available by our system for client’s consumption on next day 02:30 UTC+2."\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report sample</h2>
<p><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-1536" src="https://developer.sprint.paymentology.com/wp-content/uploads/2021/01/Card-Order-report-final-Card-API.png" alt="" width="598" height="406" srcset="https://developer.sprint.paymentology.com/wp-content/uploads/2021/01/Card-Order-report-final-Card-API.png 598w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/01/Card-Order-report-final-Card-API-300x204.png 300w" sizes="auto, (max-width: 598px) 100vw, 598px" /></p>



\{/* unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21\}},"text":"<section class=\"tutuka-block tutuka-block--info\">\n<div class=\"block-info-single icon\">\n<div class=\"info-content\">\n<p><strong>Note: file will automatically download upon clicking link</strong></p>\n</div>\n</div>\n</section>\n"}]} */}


<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_PanDetails_YYYYMMDD-card.csv">CampaignName_PanDetails_YYYYMMDD.csv</a></p>
