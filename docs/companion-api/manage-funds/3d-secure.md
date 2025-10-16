---
title: 3D Secure
deprecated: false
hidden: false
metadata:
  robots: index
original_path: companion-api/manage-funds
---
<p><strong>3D Secure (Three-Domain Secure) is an additional authentication step which provides an added layer of security for online card transactions by reducing the risk of unauthorized card use due to the card not being physically present.</strong></p>
<p>The three domains involved in the 3D Secure protocol are:</p>
<ul>
<li>The Acquirer domain (the Merchant)</li>
<li>The Issuer domain (Paymentology)</li>
<li>The Interoperability domain (the Card scheme)<br />
<em>Verified by Visa</em><br />
<em>MasterCard SecureCode</em></li>
</ul>



\{/* unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"\} */}


<p>The primary benefit of using 3D Secure is <em>to reduce the risk of fraud. </em>3D Secure allows the Issuer to verify the cardholder’s identity by requesting supplementary information before completing an online transaction. The cardholder can choose between the following options when using 3D Secure:</p>
<ul>
<li><strong>Static 3D Secure –</strong> when enabling the 3D Secure functionality, the cardholder sets a password which remains unchanged. This password will be requested as the cardholder authentication when the card is used in an online transaction. For Static 3D Secure code, use the <span class="xml-highlight"><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/set3dsecurecode/">Set3dSecureCode</a></span> call.</li>
<li><strong>Dynamic 3D Secure – </strong>this uses an OTP (one-time password) that is generated before a payment is processed after a cardholder has entered their card details online. The OTP is sent to the cardholder via text or email and is valid for a limited time. For Dynamic 3D Secure code, use the <span class="xml-highlight"><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/administrativemessage/#3DSecure">AdministrativeMessage3DSecureOTP</a></span> call.</li>
</ul>



\{/* spacing: desktop=20, mobile=10 */\}


<p><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-2020" src="https://developer.sprint.paymentology.com/wp-content/uploads/2023/03/image-35-v2.png" alt="Tutuka Dynamic 3DS flow" width="1704" height="1200" /></p>



\{/* spacing: desktop=20, mobile=10 */\}


<p>These are the steps involved in the Dynamic 3D Secure validation and transaction authorization:</p>
<ol>
<li>The Cardholder captures the card details on the checkout screen on the merchant web store</li>
<li>To check if the BIN is registered, the merchant sends a message to the card scheme directory server</li>
<li>The card scheme directory server confirms with ACS that the BIN is registered for 3D Secure</li>
<li>The ACS provider confirms if the BIN is registered and the card range is loaded on the card scheme directory server</li>
<li>The card scheme then directs the merchant to the URL for the pop up screen where the cardholder will enter the 3D Secure code. The pop up screen then appears on the web store interface. The pop up screen is set up by the ACS provider on a specific URL as the process is now handed over to the ACS provider for the rest of the 3D Secure steps</li>
<li>The ACS provider will send Paymentology the request to generate an OTP</li>
<li>Paymentology generates and sends the OTP on to the ACS provider and the wallet</li>
<li>The cardholder receives the Dynamic 3D Secure code (OTP) via a text message or through the app</li>
<li>The cardholder inputs the Dynamic 3D Secure code and clicks the “Submit” button. The Dynamic 3D Secure code goes to the ACS system and is validated</li>
<li>The ACS provider confirms the validation back to the web store page visible to the cardholder</li>
<li>The ACS provider then sends the result and UCAF (<strong>MasterCard:</strong> Universal Cardholder Authentication Field) / CAVV (<strong>Visa: </strong>Cardholder Authentication Value Verification) information to the merchant</li>
<li>The ACS provider sends a message to the card scheme’s AHS server to confirm that validation took place so that there is a history of the validation</li>
</ol>
<p>The merchant then sends the transaction (with he UCAF/CAVV information in the transaction message) to the card scheme for authorization like any other transaction. The card scheme then sends the information to Paymentology. Paymentology validates the UCAF/CAVV information and then perform all other relevant checks on the card for an authorization request.</p>
