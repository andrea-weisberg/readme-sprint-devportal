---
title: Provisioning
deprecated: false
hidden: false
metadata:
  robots: index
original_path: companion-api/tokenization2
---
<p>Provisioning is the process whereby a payment service provider (token requester) asks for a token to be created for a PAN.</p>
<p>Provisioning basically follows these steps:</p>
<p><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-1556" src="https://developer.sprint.paymentology.com/wp-content/uploads/2023/03/Tokenization-Flow_02-v2.png" alt="Provisioning flow" width="4114" height="3200" /></p>



<!-- spacing: desktop=20, mobile=10 -->


<p><b>Step 1: </b>The cardholder initiates the request process via push provisioning or manual provisioning.</p>
<p><b>Step 2: </b>The payment service provider requests a payment token from the card network.</p>
<p><b>Step 3: </b>The card network initiates the token approval process and transfers the requested information to Paymentology(the issuer processor) for verification checks.</p>
<p><b>Step 4: </b>Paymentology makes the provisioning decision and relays the information to the card network. Paymentology will also notify the client via the <b>AdministrativeMessage</b> method of the attempted provisioning.</p>
<p><b>Step 5: </b>If the token activation request is authorized, the card network generates a payment token. After tokenization, MDES will store that information in their secure token vault, while associating the card details to the created token.</p>
<p><b>Step 6: </b>The unique token is sent to the payment service provider for completing the current transaction. The provider may also store the token for future payments. If the provider stores tokenized payment card data on a file in a database, which is used for making repeat purchases, such payments are called card-on-file transactions.</p>



<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<h2><b>Types of Provisioning Methods</b></h2>
<p>Paymentology supports the following two main methods for provisioning a token to incorporate a payment card into a digitized wallet:</p>
<ul>
<li aria-level="1"><b>Push provisioning</b>—this is in-app provisioning where a cardholder pushes the card from their card app directly into a digitized wallet with a click of the button.</li>
<li aria-level="1"><b>Manual provisioning</b>—this is where a cardholder physically enters the card details into the digitized wallet.</li>
</ul>
<p>Here is a table that compares the differences between push provisioning and manual provisioning:</p>



<!-- spacing: desktop=20, mobile=10 -->


<!-- unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"Push Provisioning vs Manual Provisioning ","table":{"use_header":true,"header":[{"c":"PUSH PROVISIONING"},{"c":"MANUAL PROVISIONING"}],"caption":false,"body":[[{"c":"OTP verification not required"},{"c":"OTP verification required. However, some wallets, such as Samsung Pay do not require OTP verification."}],[{"c":"TAV certification required"},{"c":"TAV certification not required"}]]}} -->


<!-- spacing: desktop=20, mobile=10 -->


<h2><b>How Push Provisioning Works</b></h2>
<p><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-2275" src="https://developer.sprint.paymentology.com/wp-content/uploads/2023/03/MDES-Push-provisioning1-v2.png" alt="How push provisioning works flow" width="5069" height="4761" /></p>
<p>Push provisioning is a generic capability that enables cardholders to “push” a token from the issuer experience into a destination wallet or merchant.</p>
<p>There are two main authentication measures implemented during push provisioning:</p>
<ul>
<li aria-level="1">TAV certification</li>
<li aria-level="1">Card data encryption</li>
</ul>
<p>Let’s talk about them in detail.</p>
<p>&nbsp;</p>
<h3>a) TAV certification</h3>
<p>TAV (Token Authentication Value) is an encrypted digital signature that authenticates a push provisioning request from the token requester to the issuer/client. TAV certification is required to ensure the security and authenticity of the push provisioning process.</p>
<p>When a card is pushed on an XPay wallet, the client app will notify Paymentology that a card is being provisioned, and Paymentology needs to calculate its TAV value—based on the card number, expiry date, and CVV. After calculating this value, Paymentology will then pass it to MDES for MDES to tokenize the card. After tokenization, MDES will store that information in their secure token vault, while associating the card details to the generated token.</p>
<p>If a client app relies on Paymentology for TAV calculation, they’ll need to call the <b>CalculateTAV</b> API method, which is part of the Companion API. Paymentology will also need to get the necessary keys from Mastercard.</p>
<p>Note that even if Paymentology assists with TAV calculation, clients will still be responsible for other encryption tasks through the wallet to the MDES.</p>
<p>&nbsp;</p>
<h3>b) Card data encryption</h3>
<p>Other than the TAV, the card information is also structured and encrypted, and passed to the Wallet Provider, and eventually to MDES. MDES actually receives the encrypted card data from the issuer via the Wallet Provider.</p>
<p>The information is encrypted using the PEPK (Play Encrypt Private Key) tool provided by Mastercard. The client does PEPK encryption as part of the direct integration to a digitized wallet.</p>
<p>For most wallet programs, other than Apple Pay, the Wallet Provider offers a simple pass-through mechanism for the encrypted data package. This mechanism ensures the security of sensitive data, without necessarily deploying the technology required to protect card information in conformance with PCI-DSS Standards.</p>
<p>The following steps are an example of a client app communicating with a Wallet Provider’s wallet application to initiate the digitization of the card:</p>
<ol>
<li aria-level="1">The client app uses proprietary APIs that link it to the issuer’s server, where the encryption of the card details is performed.</li>
<li aria-level="1">The Wallet Provider publishes an API for the issuer to use to pass the encrypted card data to the wallet application.</li>
<li aria-level="1">The wallet application uses proprietary APIs to pass the encrypted card data to the Wallet Provider’s server.</li>
<li aria-level="1">The Wallet Provider server calls the MDES API to initiate the digitization request.</li>
<li aria-level="1">MDES identifies the key that was used to encrypt the data from the issuer and decrypts the card details.</li>
</ol>



<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<section id="tutuka-block-21" class="tutuka-block tutuka-block--text-full-width">
<h2><b>How Manual Provisioning Works</b></h2>
<p><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-2273" src="https://developer.sprint.paymentology.com/wp-content/uploads/2023/03/Mdes-Manual-provisioning-v2.png" alt="" width="6300" height="3600" /></p>
<p>&nbsp;</p>
<p>Manual provisioning is where the cardholder physically enters the card details, such as PAN, expiry date, and CVV, into the digitized wallet. It requires the cardholder to enter an OTP via the selected verification method, usually SMS or email, to verify that they indeed own the card.</p>
<p>In manual provisioning, Paymentology will use the<a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/#AdministrativeMessage"><b> AdministrativeMessage </b></a>method to handle various <a href="https://developer.sprint.paymentology.com/administrative-message-values/">digitization</a> tasks.</p>
<p><b>AdministrativeMessage Method</b></p>
<p>The <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/#AdministrativeMessage">AdministrativeMessage method</a>, which is part of the remote Companion API, is used for the following tasks:</p>
<ul>
<li aria-level="1">Notifying the client when a cardholder requests to provision their card, using either the push method or the manual method.</li>
<li aria-level="1">Notifying the client of any token lifecycle events coming from the MDES.</li>
</ul>
<p>&nbsp;</p>
<p>The <b>messageName </b>path parameter, required in the AdministrativeMessage method, specifies the name of the administrative messages sent to the client.</p>
<p>These are the possible values for the <b>messageName </b>data field during manual provisioning:</p>
<ul>
<li aria-level="1"><b><a href="https://developer.sprint.paymentology.com/administrative-message-values/#activationmethods">Digitization.activationmethods</a></b>— sends a notification that a cardholder is requesting provisioning, and the cardholder’s contact method needs to be verified for sending the OTP.</li>
<li aria-level="1"><b><a href="https://developer.sprint.paymentology.com/administrative-message-values/#activation">Digitization.activation</a></b>—sends an activation code that requires the OTP to be sent to the cardholder.</li>
<li aria-level="1"><b><a href="https://developer.sprint.paymentology.com/administrative-message-values/#complete">Digitization.complete</a></b>—sends a notification when MDES has successfully activated the token for the card.</li>
<li aria-level="1"><b><a href="https://developer.sprint.paymentology.com/administrative-message-values/#exception">Digitization.exception</a></b>—sends a notification when there is a problem with the provisioning process.</li>
</ul>
<p>Let’s talk about each of the values in detail.</p>
<p>&nbsp;</p>
<ol>
<li><b><a href="https://developer.sprint.paymentology.com/administrative-message-values/#activationmethods">Digitization.activationmethods</a></b></li>
</ol>
<p>This event happens at the beginning of the manual provisioning process. It signals that token provisioning is being requested, and the cardholder’s contact method needs to be verified for pushing the OTP. The OTP will confirm that the cardholder is the owner of the card.</p>
<p>In this instance, the MDES will send a notification to Paymentology that a cardholder is trying to provision their card on the XPay app, and that Paymentology needs to provide the cardholder’s mobile number and/or email address back to MDES so that they may pass it to the XPay.</p>
<p>Paymentology will then pass the verification request from MDES to the client via <b>Digitization.activationmethods</b> to retrieve the cardholder’s mobile number and/or email address linked to their card.</p>
<p>The client will respond to Paymentology with the required details. Paymentology will pass the data to the MDES to pass to the XPay app. The XPay app will then display the options the cardholder can select for receiving the OTP.</p>
<p><b>Digitization.activationmethods</b>requires the type of contact method as well as the data for the method to be passed to it.</p>
<p>Also, no KLV fields are required to be passed. So, they’ll be no <b>MessageData</b> string included in the AdministrativeMessage request from Paymentology.</p>
<p>&nbsp;</p>
<ol start="2">
<li><b><a href="https://developer.sprint.paymentology.com/administrative-message-values/#activation">Digitization.activation</a></b></li>
</ol>
<p>Once the cardholder selects their preferred method of verification, the XPay wallet will send this information to the MDES, and the MDES will send it to Paymentology.</p>
<p>Paymentology will then send an activation code via <b>Digitization.activation</b> to the client. The client will then pass an OTP to the cardholder, through their preferred contact method, to input it on their XPay wallet app.</p>
<p>&nbsp;</p>
<ol start="3">
<li><b><a href="https://developer.sprint.paymentology.com/administrative-message-values/#complete">Digitization.complete</a></b></li>
</ol>
<p>Once the cardholder enters the OTP, Paymentology will verify the OTP. And MDES will activate the PAN’s token. MDES will also map the token to the full PAN and store this information in its token vault. MDES will then send a notification to Paymentology confirming that the token creation process is complete.</p>
<p>Paymentology will then notify the client via <b>Digitization.complete </b>of the successful provisioning of the cardholder’s card.</p>
<p>&nbsp;</p>
<ol start="4">
<li><b><a href="https://developer.sprint.paymentology.com/administrative-message-values/#exception">Digitization.exception</a></b></li>
</ol>
<p>This occurs when Paymentology informs the XPay wallet that there is an error during the provisioning process.</p>
<p>An exception can be thrown when the OTP activation code retries have been exceeded, an expired activation code was used, an invalid activation code was used, or an incorrect activation code was entered.</p>
</section>
