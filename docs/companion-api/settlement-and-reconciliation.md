---
title: Reconciliation
deprecated: false
hidden: false
metadata:
  robots: index
original_path: companion-api
---
<p><strong>Reconciliation is the process of matching transactions reported by Paymentology to the transactions recorded on the wallet platform to ensure that the amount settled by the card scheme is accurate.</strong></p>



\{/* spacing: desktop=20, mobile=10 */\}


\{/* unsupported_acf_block: columns_with_icons_and_text {"acf_fc_layout":"columns_with_icons_and_text","title":"Reconciliation Process","block_variant":"Variant 1","columns":[{"column_width":"Full","icon":{"ID":2187,"id":2187,"title":"authorize","filename":"authorize.svg","filesize":1719,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/authorize.svg","link":"https://developer.sprint.paymentology.com/companion-api/settlement-and-reconciliation/authorize/","alt":"","author":"29","description":"","caption":"","name":"authorize","status":"inherit","uploaded_to":2096,"date":"2021-06-25 13:49:10","modified":"2021-06-25 14:44:11","menu_order":0,"mime_type":"image/svg+xml","type":"image","subtype":"svg+xml","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":48,"height":48,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/authorize.svg","thumbnail-width":48,"thumbnail-height":48,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/authorize.svg","medium-width":48,"medium-height":48,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/authorize.svg","medium_large-width":48,"medium_large-height":48,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/authorize.svg","large-width":48,"large-height":48,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/authorize.svg","1536x1536-width":48,"1536x1536-height":48,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/authorize.svg","2048x2048-width":48,"2048x2048-height":48\}},"title":"","text":"<h1><a href=\"#authorization\">Authorizations</a></h1>\n<p>Paymentology provides a daily mark-off file</p>\n<p>The mark-off file shows successful transactions that Paymentology has processed on behalf of the Issuer</p>\n<p>The Issuer/client will compare Paymentology’s transactions to the wallet platform</p>\n","link":""},\{"column_width":"Full","icon":{"ID":2201,"id":2201,"title":"settlement","filename":"settlement.svg","filesize":3279,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/settlement.svg","link":"https://developer.sprint.paymentology.com/companion-api/settlement-and-reconciliation/settlement-3/","alt":"","author":"29","description":"","caption":"","name":"settlement-3","status":"inherit","uploaded_to":2096,"date":"2021-06-25 13:49:37","modified":"2021-06-25 14:44:11","menu_order":0,"mime_type":"image/svg+xml","type":"image","subtype":"svg+xml","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":48,"height":48,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/settlement.svg","thumbnail-width":48,"thumbnail-height":48,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/settlement.svg","medium-width":48,"medium-height":48,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/settlement.svg","medium_large-width":48,"medium_large-height":48,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/settlement.svg","large-width":48,"large-height":48,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/settlement.svg","1536x1536-width":48,"1536x1536-height":48,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/settlement.svg","2048x2048-width":48,"2048x2048-height":48\}},"title":"","text":"<h1><a href=\"#settlements\">Settlements</a></h1>\n<p>Paymentology provides a daily summary settlement report as well as a daily detailed settlement report</p>\n<p>The Issuer/client will compare the net settlement amount with the amount that the card scheme has debited from the Issuer/client pool account</p>\n","link":""},\{"column_width":"Full","icon":{"ID":2185,"id":2185,"title":"money","filename":"money.svg","filesize":1037,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/money.svg","link":"https://developer.sprint.paymentology.com/companion-api/settlement-and-reconciliation/money/","alt":"","author":"29","description":"","caption":"","name":"money","status":"inherit","uploaded_to":2096,"date":"2021-06-25 13:49:07","modified":"2021-06-25 14:44:11","menu_order":0,"mime_type":"image/svg+xml","type":"image","subtype":"svg+xml","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":48,"height":48,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/money.svg","thumbnail-width":48,"thumbnail-height":48,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/money.svg","medium-width":48,"medium-height":48,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/money.svg","medium_large-width":48,"medium_large-height":48,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/money.svg","large-width":48,"large-height":48,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/money.svg","1536x1536-width":48,"1536x1536-height":48,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/money.svg","2048x2048-width":48,"2048x2048-height":48\}},"title":"","text":"<h1><a href=\"#revenue\">Revenue</a></h1>\n<p>Paymentology provides a daily forex gains report showing all revenue earned by the Issuer/client</p>\n<p>The Issuer/client also has sight of the daily interchange earned from the summary settlement report</p>\n","link":""},\{"column_width":"Full","icon":{"ID":2213,"id":2213,"title":"secure","filename":"secure.svg","filesize":1449,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/secure.svg","link":"https://developer.sprint.paymentology.com/companion-api/settlement-and-reconciliation/secure/","alt":"","author":"29","description":"","caption":"","name":"secure","status":"inherit","uploaded_to":2096,"date":"2021-06-25 13:49:50","modified":"2021-06-25 14:44:11","menu_order":0,"mime_type":"image/svg+xml","type":"image","subtype":"svg+xml","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":48,"height":48,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/secure.svg","thumbnail-width":48,"thumbnail-height":48,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/secure.svg","medium-width":48,"medium-height":48,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/secure.svg","medium_large-width":48,"medium_large-height":48,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/secure.svg","large-width":48,"large-height":48,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/secure.svg","1536x1536-width":48,"1536x1536-height":48,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/secure.svg","2048x2048-width":48,"2048x2048-height":48\}},"title":"","text":"<h1><a href=\"#fraud\">Fraud</a></h1>\n<p>Paymentology will report on all fraud cases via the card scheme’s online portal</p>\n","link":""}]} */}


\{/* unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"\} */}


<h1><a id="authorization"></a>Authorization reconciliation process</h1>
<p><b>What is Authorization?</b></p>
<p>Authorization is the process of checking the available funds on a card in order to reserve funds when the card is used for a purchase.</p>



\{/* spacing: desktop=20, mobile=10 */\}


\{/* unsupported_acf_block: columns_with_icons_and_text {"acf_fc_layout":"columns_with_icons_and_text","title":"","block_variant":"Variant 1","columns":[{"column_width":"1/3","icon":{"ID":2681,"id":2681,"title":"Paymentology_square","filename":"Paymentology_square.png","filesize":11203,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2022/09/Paymentology_square.png","link":"https://developer.sprint.paymentology.com/companion-api/settlement-and-reconciliation/paymentology_square/","alt":"Paymentology logo","author":"29","description":"","caption":"","name":"paymentology_square","status":"inherit","uploaded_to":2096,"date":"2022-09-06 22:41:12","modified":"2022-09-06 22:41:23","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":860,"height":860,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2022/09/Paymentology_square-150x150.png","thumbnail-width":150,"thumbnail-height":150,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2022/09/Paymentology_square-300x300.png","medium-width":300,"medium-height":300,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2022/09/Paymentology_square-768x768.png","medium_large-width":768,"medium_large-height":768,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2022/09/Paymentology_square.png","large-width":860,"large-height":860,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2022/09/Paymentology_square.png","1536x1536-width":860,"1536x1536-height":860,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2022/09/Paymentology_square.png","2048x2048-width":860,"2048x2048-height":860\}},"title":"","text":"<h1>Paymentology</h1>\n<p>Paymentology will daily generate a mark-off file showing all transactions successfully processed on behalf of the Issuer/client</p>\n","link":""},\{"column_width":"1/3","icon":{"ID":2216,"id":2216,"title":"customer portal","filename":"customer-portal.svg","filesize":1603,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/customer-portal.svg","link":"https://developer.sprint.paymentology.com/companion-api/settlement-and-reconciliation/customer-portal/","alt":"","author":"29","description":"","caption":"","name":"customer-portal","status":"inherit","uploaded_to":2096,"date":"2021-06-25 14:24:15","modified":"2021-06-25 14:24:15","menu_order":0,"mime_type":"image/svg+xml","type":"image","subtype":"svg+xml","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":48,"height":48,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/customer-portal.svg","thumbnail-width":48,"thumbnail-height":48,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/customer-portal.svg","medium-width":48,"medium-height":48,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/customer-portal.svg","medium_large-width":48,"medium_large-height":48,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/customer-portal.svg","large-width":48,"large-height":48,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/customer-portal.svg","1536x1536-width":48,"1536x1536-height":48,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/customer-portal.svg","2048x2048-width":48,"2048x2048-height":48\}},"title":"","text":"<h1>Issuer/Client</h1>\n<p>The Issuer/client will daily generate a similar mark-off file</p>\n<p>The Issuer/client will compare Paymentology’s transaction list to their list</p>\n","link":""},\{"column_width":"1/3","icon":{"ID":2221,"id":2221,"title":"support png","filename":"support-png.png","filesize":2515,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/support-png.png","link":"https://developer.sprint.paymentology.com/companion-api/settlement-and-reconciliation/support-png/","alt":"","author":"29","description":"","caption":"","name":"support-png","status":"inherit","uploaded_to":2096,"date":"2021-06-25 14:48:30","modified":"2021-06-25 14:49:09","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":197,"height":197,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/support-png-150x150.png","thumbnail-width":150,"thumbnail-height":150,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/support-png.png","medium-width":197,"medium-height":197,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/support-png.png","medium_large-width":197,"medium_large-height":197,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/support-png.png","large-width":197,"large-height":197,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/support-png.png","1536x1536-width":197,"1536x1536-height":197,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/support-png.png","2048x2048-width":197,"2048x2048-height":197\}},"title":"","text":"<h1>Support</h1>\n<p>If there are any discrepancies, the Issuer/client will raise these with the Paymentology support team to investigate by logging a ticket via your Zendesk Portal, selecting the *<strong data-renderer-mark=\"true\">Report a Service Incident</strong>* form, and then choosing *<strong data-renderer-mark=\"true\">Reporting</strong>* and *<strong data-renderer-mark=\"true\">Discrepancy</strong>* under the Request Type.</p>\n","link":""}]} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Authorization reports</h2>
<p>The report linked below assists client’s with authorization reconciliation.</p>
<ul>
<li><a href="https://developer.sprint.paymentology.com/companion-api/reports/mark-off-file/">Mark-off file</a></li>
</ul>
<p> </p>



\{/* unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"\} */}


<h1><a id="settlements"></a>Settlements</h1>
<section id="tutuka-block-1" class="tutuka-block tutuka-block--text-full-width"><strong>What is a settlement?</strong></section>
<section class="tutuka-block tutuka-block--text-full-width">A settlement is when funds are deducted from the Issuer/client’s bank account and deposited in to a merchants bank account to settle a card transaction.</section>
<section></section>
<p><img loading="lazy" decoding="async" class="alignleft size-full wp-image-4819" src="https://developer.sprint.paymentology.com/wp-content/uploads/2024/07/Dual-message-settlement-process.png" alt="" width="3918" height="2243" srcset="https://developer.sprint.paymentology.com/wp-content/uploads/2024/07/Dual-message-settlement-process.png 3918w, https://developer.sprint.paymentology.com/wp-content/uploads/2024/07/Dual-message-settlement-process-300x172.png 300w, https://developer.sprint.paymentology.com/wp-content/uploads/2024/07/Dual-message-settlement-process-1024x586.png 1024w, https://developer.sprint.paymentology.com/wp-content/uploads/2024/07/Dual-message-settlement-process-768x440.png 768w, https://developer.sprint.paymentology.com/wp-content/uploads/2024/07/Dual-message-settlement-process-1536x879.png 1536w, https://developer.sprint.paymentology.com/wp-content/uploads/2024/07/Dual-message-settlement-process-2048x1172.png 2048w" sizes="auto, (max-width: 3918px) 100vw, 3918px" /></p>



\{/* spacing: desktop=20, mobile=10 */\}


<h2>Settlement process:</h2>
<p><strong>Step 1:</strong> 1 – 7 days after the successful authorization, merchants will request payments from the card association</p>
<p><strong>Step 2:</strong> The card association debits the Issuing bank (the pool account that the card belongs to) and moves the funds to the Acquiring bank of the Merchant. The Acquiring bank then moves the funds to the merchants account.</p>
<p><strong>Step 3:</strong> The card scheme sends Paymentology clearing files, containing each individual settled transaction. New forex conversion rates will be calculated for all international transactions and interchange is calculated and applied.</p>
<p>Different card schemes have different clearing cycles depending on the region/country and there can be up to 8 clearing cycles per day. All clearing cycles are included in our settlement reports. <strong>NOTE:</strong> Visa’s settlements are online.</p>
<p><strong>Step 4:</strong> Paymentology will compare all settled transactions to previously authorized transactions and match these together. Paymentology creates a summary settlement report and calculates the net settlement amount that will be debited by the card association. Forex currency gains are calculated based on settlement amounts.</p>
<p><strong>Step 5:</strong> The client will compare Paymentology’s settlement amounts to the amount debited by the card scheme and the amount that is debited from their bank accounts.</p>



<h2>Settlement reports</h2>
<p>The reports linked below assist client’s with settlement reconciliation.</p>
<ul>
<li><a href="https://developer.sprint.paymentology.com/companion-api/reports/summary-settlement-report/">Summary settlement report</a></li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/reports/detailed-settlement-report/">Detailed settlement report</a></li>
</ul>



\{/* unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"\} */}


<h1><a id="revenue"></a>Revenue</h1>
<p><strong>What is Revenue?</strong></p>
<p>Revenue is the income earned from Forex gains and interchange.</p>
<h2>Forex Fluctuation</h2>
<p><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-1769" src="https://developer.sprint.paymentology.com/wp-content/uploads/2023/03/Forex-fluctuation-v2.png" alt="Forex fluctuation flow" width="3300" height="1800" /></p>



\{/* spacing: desktop=20, mobile=10 */\}


<h2><b>Revenue reports</b></h2>
<p>The report linked below assists client’s with revenue reconciliation and reporting:</p>
<ul>
<li><a href="https://developer.sprint.paymentology.com/companion-api/reports/forex-gains-report/">Forex gains report</a></li>
</ul>



\{/* spacing: desktop=20, mobile=10 */\}


<h1>Adjustment Handling</h1>
<h2>Deduct Adjustments</h2>
<ul>
<li>Negative forex fluctuation -> Issuer/client to absorb</li>
<li>Settlement with no authorizations -> Issuer/client to debit customer’s account</li>
</ul>
<h2>Load Adjustments</h2>
<ul>
<li>Positive forex fluctuation -> Issuer/client to absorb</li>
<li>Refunds -> Issuer/client credit customer’s account</li>
</ul>



\{/* unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21\}},"text":"<p>All adjustments are recorded in the mark-off file</p>\n"}]} */}


\{/* unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"\} */}


<h1><a id="fraud"></a>Fraud</h1>
<p><strong>What is Fraud?</strong></p>
<p>Fraud is a false or illegal transaction which results in a loss of funds. Paymentology provides the following Risk Management features:</p>
<ul>
<li>Transaction Limits – Paymentology allows you to implement transaction limits per card or program. If the ceiling is reached, no further transactions are permitted.</li>
<li>Usage – Paymentology allows you to specify the payment methods that the card can be used with. If there is an attempted use of the card for an unspecified payment method, the transaction will fail and send a fraud alert.</li>
<li>Additional settings – Paymentology allows you to implement additional settings to reinforce the security of cards and help with fraud prevention.</li>
<li>Notifications – Paymentology lets you configure real-time notifications that keep customers informed about the state of their cards.</li>
<li>Checks and controls – Paymentology allows you to implement a variety of Issuance checks, Spend controls and Authorization checks</li>
</ul>
<p>Read more about Fraud and Risk <a href="https://developer.sprint.paymentology.com/get-started/fraud/">here</a></p>
<h2>Dispute Handling</h2>
<p><strong>What is a Dispute?</strong></p>
<p>A dispute is a transaction that a cardholder/customer does not agree with and therefore requests that part of, or the entire transaction be reversed or refunded.</p>
<h3>Types of Disputes:</h3>
<ol>
<li><strong>Reversal </strong>A reversal is essentially a request for a transaction that was not completed and could have failed at a particular step of the transaction process. It is an advisement message to all parties of the transaction and ensures that the card and store of value are put back into their original state if a failed to deduct transaction had been initiated.If you sent a transaction and did not receive a confirmation that the transaction was successful, it could imply that the transaction did not reach the intended destination.</li>
<li><strong><strong>Refund</strong></strong>A refund is when funds are credited back to the customer’s card from a previously debited transaction. A refund is processed when the merchant refunds the customer for returned goods and the funds which were settled to the merchant’s account need to move back to the cardholder’s account.</li>
<li><strong>Chargeback </strong>A chargeback is the return of funds for a deduct transaction that was previously processed from a cardholder’s card balance, due to a successful dispute by the consumer regarding the transaction</li>
</ol>
<p>Read about Chargeback related Dispute handling <a href="https://developer.sprint.paymentology.com/companion-api/disputes/">here</a></p>
