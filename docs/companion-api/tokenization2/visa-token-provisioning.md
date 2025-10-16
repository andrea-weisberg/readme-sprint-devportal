---
title: VTS
deprecated: false
hidden: false
metadata:
  robots: index
---
<p><span style="font-weight: 400;">The Visa Token Service (VTS) is a Visa-powered security technology that substitutes sensitive account data, such as the 16-digit account number, with a unique token that safeguards the underlying card details from being compromised. This greatly improves the security of digital transactions and provides customers with a seamless purchasing experience.  </span></p>
<p><span style="font-weight: 400;">Paymentology supports the Visa’s tokenization technology. We have leveraged VTS to offer our clients with simple, fast and secure token management services.</span></p>
<p><span style="font-weight: 400;">We use VTS to generate and provision the tokens. Token provisioning refers to the process of creating a token and incorporating it on the digital wallet so that it can be used for making payments conveniently.</span></p>
<p><span style="font-weight: 400;">The process of enabling payments through tokens involves a number of steps. </span></p>
<p><span style="font-weight: 400;">Let’s talk about them. </span></p>

<p><b>Step 1</b><span style="font-weight: 400;">: The cardholder initiates the request for a token via push provisioning or manual provisioning. You can learn more about the two provisioning methods <a href="https://developer.sprint.paymentology.com/companion-api/tokenization2/token-provisioning/">here</a>.</span></p>
<p><b>Step 2: </b><span style="font-weight: 400;">The payment service provider (such as a digital wallet or an online retailer) requests a token from the card network. </span></p>
<p><b>Step 3: </b><span style="font-weight: 400;">The card network initiates the token approval process and transfers the requested information to Paymentology for verification checks.</span></p>
<p><b>Step 4: </b><span style="font-weight: 400;">Paymentology does the preliminary verification checks and decides whether to make the provisioning approval. Paymentology will perform all the base validations and ensure compliance with the recommended VTS compliance rules, such as card number validity, expiry date, CVV validity, or any other specific XPay wallet rules.</span></p>
<p><b>Step 5: </b><span style="font-weight: 400;">Optionally, Paymentology can involve the Companion API client in the decision to issue the token. </span></p>
<p><b>Note: </b><span style="font-weight: 400;">This feature can be enabled or disabled on the Campaign configuration settings page by sending a request to your Client Executive.</span></p>
<p><span style="font-weight: 400;">If the preliminary validations succeed, Paymentology will notify the client via a new </span><b>AdministrativeMessage</b><span style="font-weight: 400;"> method of the requested provisioning. </span></p>
<p><span style="font-weight: 400;">The client will then respond with the following decision codes:</span></p>
<ul>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">APPROVED</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">DECLINED</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">REQUIRE_ADDITIONAL_AUTHENTICATION</span></li>
</ul>
<p><b>Note:</b><span style="font-weight: 400;"> In case the decisioning data is not received in the request, Paymentology will not call the remote Companion API or Card API and will respond with a REQUIRE_ADDITIONAL_AUTHENTICATION.</span></p>
<p><b>Step 6: </b><span style="font-weight: 400;">Paymentology relays the provisioning decision to the card network.</span></p>
<p><b>Step 7: </b><span style="font-weight: 400;">If the token approval process succeeds, the card network generates a payment token. The card network then stores the information in their secure token vault, while associating the card details with the created token.</span></p>
<p><b>Step 8: </b><span style="font-weight: 400;">The card network sends the unique token to the payment service provider to incorporate into its platform and complete the current transaction. The provider may also store the token to ease future repeat purchases.</span></p>
<p><b>Step 9: </b><span style="font-weight: 400;">Optionally, additional cardholder authentication may be required before the token is activated. In that case, the client will need to call the </span><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/activatetoken/"><b>ActivateToken</b></a><span style="font-weight: 400;"> method to activate the token.</span></p>
<p><span style="font-weight: 400;">The method is used to activate a token that has been approved and provisioned but a cardholder authentication is required before it is activated. It is expected that a cardholder will carry out the authentication process via an issuer’s </span><span style="font-weight: 400;"> </span><span style="font-weight: 400;">(wallet / Paymentology’s client) call center or via a backend service called by the issuer’s mobile application. </span></p>
</span></span></span></p></span></b></a></span></b></p></span></b></p></span></b></p></span></b></p></span></b></p></span></li></span></li></span></li></ul></span></p></span></b></span></p></span></b></p></span></b></p></span></b></p></span></b></p></span></b></p></a></span></b></p></span></p></span></p></span></p></span></p></span></p>
