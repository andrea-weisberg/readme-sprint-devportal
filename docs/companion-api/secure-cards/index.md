---
title: Secure cards
deprecated: false
hidden: false
metadata:
  robots: index
original_path: companion-api
---
<div class="block translation current highlight" data-element="para" data-attr-xinfo-text="10605">
<p><strong>The Paymentology Sprint Companion API allows you to secure your cards and ensure the safety of transactions.</strong></p>
</div>



\{/* spacing: desktop=20, mobile=10 */\}


<p><span style="font-weight: 400;">You can use the following three main ways to secure your companion cards:</span></p>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">Dynamic secure code on virtual cards</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">PIN on physical cards</span></li>
</ul>



\{/* unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"\} */}


<h2>1. Securing a virtual card with a dynamic secure code</h2>
<p><span style="font-weight: 400;">You can add an extra layer of security to your virtual card using a dynamic secure code. <strong>The secure code is what Mastercard refers to as 3D Secure, and Visa refers to it as Visa Secure (formerly Verified by Visa (VbV)).</strong> Mastercard and Visa created the technical standard to secure Cardholder Not Present (CNP) transactions. </span></p>
<p><span style="font-weight: 400;"><strong>This method provides additional authentication to secure a customer’s virtual card during an online transaction.</strong> It protects consumers against unauthorized use of cards and businesses from potential fraud liabilities. </span></p>
<p><span style="font-weight: 400;">3D Secure enables consumers to verify transactions using a One Time Pin (OTP), which is sent to their mobile device.</span></p>
<p>If your card program is enabled for Dynamic 3D Secure, the cardholder will be sent an OTP to conclude an online transaction. Through the Remote AdminMessage, Paymentology will send the OTP to your platform, which you can then send on to the cardholder.</p>



\{/* unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"\} */}


<h2>2. Securing a physical card with a PIN</h2>
<p><span style="font-weight: 400;">Your customers will require a PIN (personal identification number) for all ATM transactions. A secret PIN assists in verifying your users’ identity and allowing them to perform secure transactions.</span></p>
<p><span style="font-weight: 400;">There are two options for managing your PIN: <strong>Paymentology manages the PIN</strong> or <strong>you manage the PIN</strong></span></p>



{/* unsupported_acf_block: options_block {"acf_fc_layout":"options_block","options_type":"No info","options_columns":[{"column_width":"Full","title":"","text":"<p><strong>OPTION 1</strong> – Paymentology manages the PIN</p>\n<p><span style=\"font-weight: 400;\">If you choose this option, Paymentology will manage the PIN on your behalf. This implies that <strong>Paymentology will validate the PIN before sending it to a store of value for authorizing the transaction.</strong> </span></p>\n<p><span style=\"font-weight: 400;\">When Paymentology manages the PIN, you can choose between these options:</span></p>\n<p style=\"padding-left: 40px;\"><b>a)</b><span style=\"font-weight: 400;\"> The PIN is pre-printed in a tamper-proof package containing the card. This would be the PIN the cardholder would use for making transactions.</span></p>\n<p style=\"padding-left: 40px;\"><b>b)</b><span style=\"font-weight: 400;\"> The PIN is not printed on the package. This implies it would be set when the card is linked or issued.</span></p>\n","info_text":""}]} */}


\{/* unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21\}},"text":"<p>In case the card PIN needs to be set for the first time or changed at a later time, or if the customer forgets it or requests it to be changed, you’ll need to make a call to the <a href=\"https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/changepin/\"><span class=\"xml-highlight\">ChangePIN</span></a> method to do this. Once the API request has been completed, Paymentology will issue a new PIN, which the cardholder can use for making transactions.</p>\n"}]} */}


{/* unsupported_acf_block: options_block {"acf_fc_layout":"options_block","options_type":"No info","options_columns":[{"column_width":"Full","title":"","text":"<p><strong>OPTION 2</strong> – You manage the PIN</p>\n<p><span style=\"font-weight: 400;\">This second option allows the store of value organization to manage the PIN and perform PIN validation based on a PINblock that Paymentology sends. Paymentology will then send a PINblock in the KLV (Key-Length-Value) transaction data based on pre-shared keys, which allow for encryption and decryption to pass the PIN for secure validation.</span></p>\n","info_text":""}]} */}
