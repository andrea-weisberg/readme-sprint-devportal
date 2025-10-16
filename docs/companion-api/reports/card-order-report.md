---
title: Card order
deprecated: false
hidden: false
metadata:
  robots: index
original_path: companion-api/reports
---
\{/* spacing: desktop=40, mobile=20 */\}


<p>A <strong>card order</strong> is a request to print a physical card. With the Companion API, you can optionally issue a physical card to a customer by sending an order for printing to the card manufacturer. To initiate a request to print a physical card, you use the <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/ordercard/"><span class="xml-highlight">OrderCard</span></a> method in the Local API. On a daily basis at 19:30 UTC+2, Paymentology creates a batch order and submits it to the manufacturer for printing. A <strong>card order </strong>report lists all the orders that were processed on the previous day.{/* <strong>Stored in:</strong> Paymentology-hosted <span class="GlossaryItem-trigger">SFTP</span> folder */}</p>
<p>The report includes the following details:</p>
<ul>
<li><strong>Card Number </strong>– this is the issued/created card number. Due to card numbers being sensitive data, the card number is usually presented in the format 1234xxxxxxxx5678.</li>
<li><strong>Wallet Reference</strong> – this is the unique customer reference for the card.</li>
<li><strong>Date Created</strong> – this is the date and time stamp of when the card number was issued. Usually in the format DD/MM/YYYY HH:MM.</li>
</ul>



\{/* spacing: desktop=60, mobile=30 */\}


<h2>Report format</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"FORMAT"\},\{"c":"FILE NAME"\},\{"c":"FREQUENCY"\},\{"c":"ACCESSIBILITY"\}],"caption":false,"body":[[\{"c":"CSV"\},\{"c":"[CampaignUUID]/[CampaignName]_PanDetails_[YYYYMMDD].csv"\},\{"c":"Daily"\},\{"c":"HTTP get request or client SFTP folder"\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report time frame</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"UTC +2"\},\{"c":"UTC +7"\},\{"c":"REMARKS"\}],"caption":false,"body":[[\{"c":"02:45"\},\{"c":"07:45"\},\{"c":"00:00:00 → 00:00:00 day + 1, UTC +2\n\nBased on the time in UTC +2 that the perso was requested."\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report sample</h2>
<p><img loading="lazy" decoding="async" class="size-full wp-image-3152 alignleft" src="https://developer.sprint.paymentology.com/wp-content/uploads/2023/02/Card-Order1-300x195.png" alt="Card order report" width="600" height="390" srcset="https://developer.sprint.paymentology.com/wp-content/uploads/2023/02/Card-Order1-300x195.png 300w, https://developer.sprint.paymentology.com/wp-content/uploads/2023/02/Card-Order1.png 679w" sizes="auto, (max-width: 600px) 100vw, 600px" /></p>



\{/* unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21\}},"text":"<div class=\"info-content\">\n<p><strong>Note: file will automatically download upon clicking link</strong></p>\n</div>\n"}]} */}


<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_PanDetails_YYYYMMDD.csv">CampaignName_PanDetails_YYYYMMDD.csv</a></p>



\{/* spacing: desktop=60, mobile=30 */\}


\{/* spacing: desktop=20, mobile=4 */\}
