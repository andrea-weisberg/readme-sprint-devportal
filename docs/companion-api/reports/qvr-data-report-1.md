---
title: QVR data report
deprecated: false
hidden: false
metadata:
  robots: index
original_path: companion-api/reports
---
<p>The QVR data report can be provided to clients using Visa. It contains data to assist clients with their Visa quarterly reporting requirements. The report includes the following:</p>
<h3>Category definitions</h3>
<ul>
<li><strong>On Us</strong> &#8211; is when the issuer and acquirer of the transaction is the same member and the transaction was made at a merchant within the issuing country/region.</li>
<li><strong>National</strong> &#8211; is when the transaction was made at a merchant within the issuing country/region and the issuer and acquirer are different.</li>
<li><strong>International</strong> &#8211; is when the transaction was made at a merchant outside of the issuing country/region.</li>
<li><strong>Debit Classic</strong> &#8211; only applicable for debit classic campaigns.</li>
</ul>
<h3>Cardholder activity</h3>
<p>The report includes the Cardholder Activity data for <strong>On Us</strong>, <strong>National</strong>, <strong>International</strong> and <strong>Debit Classic</strong><em>. </em>This data includes:</p>
<ul>
<li><strong>Payments &#8211; Card Present </strong>&#8211; this is the count and volume of successful payments/purchase transactions within the period where the card was considered as present.</li>
<li><strong>Payments &#8211; Card Not Present</strong> &#8211; this is the count and volume of successful payments/purchase transactions within the period where the card was considered as not present.</li>
<li><strong>ATM Cash Advances</strong> &#8211; this is the count and volume of successful cash withdrawal transactions made at an ATM within the period.</li>
<li><strong>Manual Cash</strong> &#8211; this is the count and volume of successful cash withdrawal transactions made via a teller or not at an ATM within the period.</li>
<li><strong>Account funding transaction </strong>&#8211; this is the count and volume of successful transactions considered as an account funding transaction within the period.</li>
<li><strong>Original Credits</strong> &#8211; this is the count and volume of successful transactions considered as an original credit transaction within the period.</li>
<li><strong>Cashback </strong>&#8211; this is the count and volume of successful transactions considered as a cashback transaction within the period.</li>
</ul>
<h3>Card/account data:</h3>
<p>In addition to the above the following Card/Account data is provided:</p>
<ul>
<li><strong>Total Number of Cards</strong> &#8211; this is the total number of cards that are issued on the program. This includes cards that are temporarily blocked and excludes those that have been terminated/retired or closed (i.e. the card cannot return to an active state).</li>
<li><strong>Number of Cards &#8211; Magnetic Stripe</strong> &#8211; this is the number of cards that are issued with magnetic stripe <em>only</em> functionality. This includes cards that are temporarily blocked and excludes those that have been terminated/retired or closed (i.e. the card cannot return to an active state).</li>
<li><strong>Number of Cards &#8211; Magnetic Stripe, Chip</strong> &#8211; this is the number of cards that are issued with magnetic stripe &amp; chip functionality <em>only</em>. This includes cards that are temporarily blocked and excludes those that have been terminated/retired or closed (i.e. the card cannot return to an active state).</li>
<li><strong>Number of Cards &#8211; Magnetic Stripe, Contactless</strong> &#8211; this is the number of cards that are issued with magnetic stripe &amp; contactless functionality <em>only</em>. This includes cards that are temporarily blocked and excludes those that have been terminated/retired or closed (i.e. the card cannot return to an active state).</li>
<li><strong>Number of Cards &#8211; Magnetic Stripe, Chip, Contactless</strong> &#8211; this is the number of cards that are issued with magnetic stripe, chip &amp; contactless functionality. This includes cards that are temporarily blocked and excludes those that have been terminated/retired or closed (i.e. the card cannot return to an active state).</li>
<li><strong>Total Number of Active Cards</strong> &#8211; this is the number of cards that have made at least 1 transaction during the time period.</li>
<li><strong>Total Number of Active Cards &#8211; used at Contactless device</strong> &#8211; this is the number of cards that have made at least 1 transaction via a contactless device during the time period.</li>
<li><strong>Number of Accounts &#8211; Domestic use Only</strong> &#8211; this is the number of accounts that are <em>only</em> capable of transacting within the issuing country.</li>
<li><strong>Number of Accounts &#8211; International enabled</strong> &#8211; this is the number of accounts that are capable of transacting outside the issuing country.</li>
<li><strong>Payments Transactions Declined for Insufficient Funds &#8211; Count</strong> &#8211; this is the number of payments transactions that were attempted but declined due to insufficient funds.</li>
<li><strong>Cash Transactions Declined for Insufficient Fund &#8211; Count</strong> &#8211; this is the number of cash transactions that were attempted but declined due to insufficient funds.</li>
</ul>



<!-- spacing: desktop=20, mobile=10 -->


<h2>Report format</h2>



<!-- unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"FORMAT"},{"c":"FILE NAME"},{"c":"FREQUENCY"},{"c":"ACCESSIBILITY"}],"caption":false,"body":[[{"c":"XLS"},{"c":"QVR_SRE[SRE]_YYYYMMDD-YYYYMMDD.xls"},{"c":"Quarterly"},{"c":"Via email"}]]}} -->


<!-- spacing: desktop=20, mobile=10 -->


<h2>Report time frame</h2>



<!-- unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"TIME, DATE"},{"c":"REMARKS"}],"caption":false,"body":[[{"c":"Clients are required to liaise with their client executive to confirm when they will be scheduled to receive this report."},{"c":"Quarterly reports are produced as follows: Q1 - (January, February, March) produced April Q2 - (April, May, June) produced July Q3 - (July, August, September) produced October Q4 - (October, November, December) produced January."}]]}} -->


<!-- spacing: desktop=20, mobile=10 -->


<h2>Report sample</h2>



<!-- unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21}},"text":"<p>Note: file will automatically download upon clicking link</p>\n"}]} -->


<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/QVR_SRE-SRE_YYYYMMDD-YYYYMMDD.xls">QVR_SRE[SRE]_[YYYYMMDD]-[YYYYMMDD].xls</a></p>
