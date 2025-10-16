---
title: Processing
deprecated: false
hidden: false
metadata:
  robots: index
original_path: companion-api/tokenization2
---
<p>Processing a transaction using a token basically follows these steps:</p>
<p>(We’ll assume that the card’s data has already been provisioned)</p>
<p><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-1555" src="https://developer.sprint.paymentology.com/wp-content/uploads/2021/01/Tokenization-Flow_01.png" alt="Authprization Request flow" width="4113" height="3200" srcset="https://developer.sprint.paymentology.com/wp-content/uploads/2021/01/Tokenization-Flow_01.png 4113w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/01/Tokenization-Flow_01-300x233.png 300w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/01/Tokenization-Flow_01-1024x797.png 1024w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/01/Tokenization-Flow_01-768x598.png 768w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/01/Tokenization-Flow_01-1536x1195.png 1536w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/01/Tokenization-Flow_01-2048x1593.png 2048w" sizes="auto, (max-width: 4113px) 100vw, 4113px" /></p>



\{/* spacing: desktop=20, mobile=10 */\}


<p><b>Step 1: </b>The cardholder initiates the transaction and provides their sensitive credit card details. The transaction can be initiated via a mobile app, at an NFC store, or on an e-commerce site.</p>
<p><b>Step 2: </b>The merchant initiates the payment authorization request by submitting a token, in place of a PAN, to their acquiring bank.</p>
<p><b>Step 3:</b> The acquiring bank passes the token to the credit card network.</p>
<p><b>Step 4:</b> The credit card network maps the token with the original PAN, and verifies the rightful use of the payment token. During provisioning, the card network stores the original PAN in its secure token vault. After the processing, the card network transmits the PAN and token to Paymentology, which is the issuer, for authorization.</p>
<p><b>Step 5: </b>Paymentology authorizes or declines the transaction</p>
<p><b>Step 6: </b>Paymentology sends the authorization response to the card network.</p>
<p><b>Step 7: </b>The card network substitutes the PAN back to the token and sends the response to the acquirer and to the merchant.</p>
<p><b>Step 8</b>: The merchant and the acquiring bank coordinate to finalize the transaction.</p>
