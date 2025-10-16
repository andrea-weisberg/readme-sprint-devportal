---
title: Apple Pay monthly declines report
deprecated: false
hidden: false
metadata:
  robots: index
---
<p>For clients using Paymentology’s tokenization, Paymentology can issue monthly reports to clients to utilize the report data to compile their Apple report through the Apple Partner Connect platform.</p>
<p>The purpose of the Apple Pay monthly declines report is to provide oversight on Apple Pay transactions that have been declined. It is important to note that failed transactions are NOT considered as declined and therefore not considered for this report.</p>
<p>Declined transactions include those that were declined due to: daily limits exceeded, unable to authorize, no account, card status suspended, over credit line, unavailable funds, invalid PIN, expired card, cardholder authorization file, delinquent account.</p>
<p>The Apple Pay monthly declines report includes the following details:</p>
<ul>
<li><strong>Transaction Size</strong> – is the transaction amount of the reported transaction, denominated in Euros. In cases where the campaign billing currency, is in US Dollars (USD) [This also applies to other currencies], the amount will be converted to Euros using Paymentology’s exchange rate applicable at the end of the relevant month. Transaction size is split into:
<ul>
<li><10</li>
<li>10 – 25</li>
<li>25 – 50</li>
<li>50 – 100</li>
<li>100 – 250</li>
<li>250 – 1000</li>
<li>>1000</li>
</ul>
</li>
<li><strong>Apple Pay Total POS Transactions</strong> – this is the total number of transactions made using Apple Pay at Point of Sale for the reported month i.e. Apple Pay transactions that were not considered eCommerce.</li>
<li><strong>Apple Pay Declined POS Transactions</strong> – this is the total number of declined transactions for the reported month that were attempted using Apple Pay at Point of Sale.</li>
<li><strong>Issuer POS Decline Rate (%)</strong> – this is the percentage decline rate for the given month for Apple Pay POS transactions. The calculation is <em>Apple Pay Declined POS Transactions</em> / <em>Apple Pay Total POS Transactions</em> = <strong><em>Issuer POS Decline Rate.</em></strong></li>
<li><strong>Apple Pay Total Remote Transactions</strong> – this is the total number of remote transactions made using Apple Pay for the reported month i.e. Apple Pay transactions that were considered eCommerce.</li>
<li><strong>Apple Pay Declined Remote Transactions</strong> – this is the total number of declined remote transactions for the reported month that were attempted using Apple Pay.</li>
<li><strong>Issuer Remote Decline Rate (%) </strong>– this is the percentage decline rate for the given month for Apple Pay remote transactions. The calculation is <em>Apple Pay Declined Remote Transactions</em> / <em>Apple Pay Total Remote Transactions</em> = <strong><em>Issuer Remote Decline Rate.</em></strong></li>
</ul>



\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report format</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"FORMAT"\},\{"c":"FILE NAME"\},\{"c":"FREQUENCY"\},\{"c":"ACCESSIBILITY"\}],"caption":false,"body":[[\{"c":"XLS"\},\{"c":"[CampaignName]_ApplePay Declines Report [Month YYYY].xls"\},\{"c":"Monthly"\},\{"c":"Via email"\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report time frame</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"UTC +2"\},\{"c":"UTC +7"\},\{"c":"REMARKS"\}],"caption":false,"body":[[\{"c":"02:00"\},\{"c":"07:00"\},\{"c":"Monthly Apple Pay reports are produced on day 2 of the following month."\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Report sample</h2>



\{/* unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21\}},"text":"<p>Note: file will automatically download upon clicking link.</p>\n"}]} */}


<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2024/01/CampaignName_ApplePay-Declines-Report-MONTH-YYYY.xls">CampaignName_ApplePay Declines Report MONTH YYYY.xls</a></p>
