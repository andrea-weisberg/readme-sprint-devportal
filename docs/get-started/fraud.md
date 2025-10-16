---
title: Fraud and Risk
deprecated: false
hidden: false
metadata:
  robots: index
---
<p><span style="font-weight: 400;">Paymentology provides a number of advanced fraud prevention and risk control mechanisms that ensure transactions are secure and trusted. These anti-fraud techniques allow you to build a robust and efficient payment system that protects your customers and ensures business success.  </span></p>
<p><span style="font-weight: 400;">Let’s look at the fraud control measures.</span></p>



\{/* spacing: desktop=20, mobile=10 */\}


<h2>Transaction Limits</h2>
<p><span style="font-weight: 400;">Paymentology Sprint allows you to implement transaction limits per card or program. If the ceiling is reached, no further transactions are permitted. </span></p>
<p><span style="font-weight: 400;">These are the transaction limits:</span></p>
<ul>
<li>Daily transaction limit</li>
<li>Daily POS limit</li>
<li>Daily ATM limit</li>
<li>Daily transaction count POS</li>
<li>Daily transaction count ATM</li>
<li>Monthly POS limit</li>
<li>Monthly ATM limit</li>
<li>Monthly transaction count POS</li>
<li>Monthly transaction count ATM</li>
</ul>
<p> </p>



\{/* unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"\} */}


<h2>Usage</h2>
<p>Paymentology Sprint allows you to specify the payment methods that the card can be used with. If there is an attempted use of the card for an unspecified payment method, the transaction will fail and send a fraud alert.</p>
<ul>
<li>POS</li>
<li>ATM</li>
<li>Tokenization</li>
<li>Moneysend</li>
<li>Contactless</li>
<li>EMV</li>
<li>E-commerce</li>
</ul>



\{/* unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"\} */}


<h2>Additional Settings</h2>
<p><span style="font-weight: 400;">Paymentology Sprint allows you to implement additional settings to reinforce the security of cards and help with fraud prevention. These are the additional card settings:</span></p>
<ul>
<li>Enable multiple currencies linked cards</li>
<li>Allow releasing of authorisations</li>
<li>Max threshold to release funds for unsettled authorisations</li>
<li>Time period to release authorisations</li>
<li>Expiry time period</li>
<li>PIN length</li>
<li>BIN range splitting</li>
<li>Filtering rules</li>
<li>Cards created active or inactive</li>
<li>Is the card readable</li>
<li>Allow batch top ups from administrator portal</li>
<li>Allow card orders from administrator portal</li>
</ul>



\{/* unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"\} */}


<p> </p>
<h2>Notifications</h2>
<p><span style="font-weight: 400;">Paymentology Sprint lets you configure real-time notifications that keep customers informed about the state of their cards. </span></p>
<p><span style="font-weight: 400;">You can configure the following notifications:</span></p>
<ul>
<li>Notifications for declined transactions</li>
<li>Notifications for transactions</li>
<li>Notifications for 3D Secure</li>
</ul>
<p> </p>



\{/* unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"\} */}


<h2>Issuance checks</h2>
<p><span style="font-weight: 400;">Paymentology Sprint allows you to implement the following issuance checks:</span></p>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"Issuance checks","table":{"use_header":true,"header":[{"c":""\}],"caption":false,"body":[[\{"c":"Checks on excessive voucher balances queries, large loads, multiple transactions and other suspicious activity"\}],[\{"c":"Checks on authorizations of cards that are not activated or linked"\}],[\{"c":"Checks on ASI Messages (Account Status Inquiry messages) for new and existing BINs added to production to monitor if\nparty is cycling through card numbers to get valid card numbers with expiry and CVV"\}],[\{"c":"If a card is EMV enabled, we can turn off magstripe fallback and only validate transactions if they come with EMV data as\nthe Paymentology Sprint host system does EMV validation"\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Spend Controls</h2>
<p><span style="font-weight: 400;">Paymentology Sprint allows you to implement the following spend control measures:</span></p>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"Spend controls","table":{"use_header":true,"header":[{"c":""\}],"caption":false,"body":[[\{"c":"Limits on single-day and multiple-day transaction velocity (number of transactions)"\}],[\{"c":"Limits on single-day and multiple-day monetary spending (value of transactions)"\}],[\{"c":"Limits for particular POS entry modes (magnetic stripe-read, PAN key-entry, chip-read, card not present etc.)"\}],[\{"c":"Limits for particular country codes"\}],[\{"c":"Limits on single transaction exceeding a certain amount"\}],[\{"c":"Multiple transactions exceeding a certain amount"\}],[\{"c":"Limits on number of transactions allowed per card based on program rules"\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Authorization Checks</h2>
<p><span style="font-weight: 400;">Paymentology Sprint allows you to implement the following authorization checks:</span></p>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"Authorization checks","table":{"use_header":true,"header":[{"c":""\}],"caption":false,"body":[[\{"c":"Checks on CVC1 and CVC2- card is stopped if incorrect CVV is entered incorrectly three times"\}],[\{"c":"Checks on out of country usage"\}],[\{"c":"Checks on magstripe data present"\}],[\{"c":"Checks on refunds versus original transactions"\}],[\{"c":"Checks on blacklisted merchants"\}],[\{"c":"Checks on spend at single merchants"\}],[\{"c":"Checks on card spend spread across multiple merchants"\}],[\{"c":"Checks on card spend on an individual card at multiple merchants in 1 day"\}],[\{"c":"Checks on card spend at certain merchants identified by merchant category code (high risk MCC)"\}],[\{"c":"Checks on trends on settlements received that have no authorization. Determine if there are multiple/settlement\nitems received for a card that had no authorization, or across cards for a specific merchant"\}],[\{"c":"Check for a high volume of ATM transactions in rapid sequence on a single card number or multiple card numbers"\}],[\{"c":"Alert when a merchant has more than 50 transactions that failed with a an error code of 1001, 1018 or 1022 in the last 15\nminutes"\}],[\{"c":"Alert when the number of ASI transactions is more than 5% of total number of transactions"\}],[\{"c":"Alert when the total number of successful and unsuccessful ATM transactions in the last 5 minutes exceeds the\ntransaction limit"\}],[\{"c":"Alert when the total value of international transactions in the last 5 minutes exceeds the limit"\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}
