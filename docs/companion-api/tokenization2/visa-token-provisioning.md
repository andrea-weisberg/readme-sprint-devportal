---
title: VTS
deprecated: false
hidden: false
metadata:
  robots: index
---
The Visa Token Service (VTS) is a Visa-powered security technology that substitutes sensitive account data, such as the 16-digit account number, with a unique token that safeguards the underlying card details from being compromised. This greatly improves the security of digital transactions and provides customers with a seamless purchasing experience.

Paymentology supports Visa’s tokenization technology. We have leveraged VTS to offer our clients simple, fast and secure token management services.

We use VTS to generate and provision the tokens. Token provisioning refers to the process of creating a token and incorporating it on the digital wallet so that it can be used for making payments conveniently.

The process of enabling payments through tokens involves a number of steps.

Let’s talk about them.

**step 1:** The cardholder initiates the request for a token via push provisioning or manual provisioning. You can learn more about the two provisioning methods [here](token-provisioning).  
**step 2:** The payment service provider (such as a digital wallet or an online retailer) requests a token from the card network.  
**step 3:** The card network initiates the token approval process and transfers the requested information to Paymentology for verification checks.  
**step 4:** Paymentology does the preliminary verification checks and decides whether to make the provisioning approval. Paymentology will perform all the base validations and ensure compliance with the recommended VTS compliance rules, such as card number validity, expiry date, CVV validity, or any other specific XPay wallet rules.  
**step 5:** Optionally, Paymentology can involve the Companion API client in the decision to issue the token.

**Note:** This feature can be enabled or disabled on the Campaign configuration settings page by sending a request to your Client Executive.

If the preliminary validations succeed, Paymentology will notify the client via a new **AdministrativeMessage** method of the requested provisioning.

The client will then respond with the following decision codes:

- APPROVED
- DECLINED
- REQUIRE_ADDITIONAL_AUTHENTICATION

**Note:** In case the decisioning data is not received in the request, Paymentology will not call the remote Companion API or Card API and will respond with a REQUIRE_ADDITIONAL_AUTHENTICATION.

**step 6:** Paymentology relays the provisioning decision to the card network.  
**step 7:** If the token approval process succeeds, the card network generates a payment token. The card network then stores the information in their secure token vault, while associating the card details with the created token.  
**step 8:** The card network sends the unique token to the payment service provider to incorporate into its platform and complete the current transaction. The provider may also store the token to ease future repeat purchases.  
**step 9:** Optionally, additional cardholder authentication may be required before the token is activated. In that case, the client will need to call the [**ActivateToken**](https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/activatetoken/) method to activate the token.

The method is used to activate a token that has been approved and provisioned but a cardholder authentication is required before it is activated. It is expected that a cardholder will carry out the authentication process via an issuer’s (wallet / Paymentology’s client) call center or via a backend service called by the issuer’s mobile application.
