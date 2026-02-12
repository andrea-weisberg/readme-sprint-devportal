---
title: 3D Secure
deprecated: false
hidden: false
metadata:
  robots: index
---
**3D Secure (Three-Domain Secure) is an additional authentication step which provides an added layer of security for online card transactions by reducing the risk of unauthorized card use due to the card not being physically present.**

The three domains involved in the 3D Secure protocol are:

* The Acquirer domain (the Merchant)
* The Issuer domain (Paymentology)
* The Interoperability domain (the Card scheme)
  _Verified by Visa_
  _MasterCard SecureCode_

***

The primary benefit of using 3D Secure is _to reduce the risk of fraud._ 3D Secure allows the Issuer to verify the cardholder’s identity by requesting supplementary information before completing an online transaction.
The cardholder can choose between the following options when using 3D Secure:

* **Static 3D Secure –** when enabling the 3D Secure functionality, the cardholder sets a password which remains unchanged. This password will be requested as the cardholder authentication when the card is used in an online transaction. For Static 3D Secure code, use the [`Set3dSecureCode`](https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/set3dsecurecode/) call.

* **Dynamic 3D Secure –** this uses an OTP (one-time password) that is generated before a payment is processed after a cardholder has entered their card details online. The OTP is sent to the cardholder via text or email and is valid for a limited time. For Dynamic 3D Secure code, use the [`AdministrativeMessage3DSecureOTP`](https://developer.sprint.paymentology.com/companion-api/api-reference/remote/administrativemessage/#3DSecure) call.

<Image border={false} src="https://files.readme.io/ff55b4e05aa3f9a82f1612594f43ee2a177c0128ae682ccd23d64bc9cc5223e8-image.png" />

These are the steps involved in the Dynamic 3D Secure validation and transaction authorization:

1. The Cardholder captures the card details on the checkout screen on the merchant web store
2. To check if the BIN is registered, the merchant sends a message to the card scheme directory server
3. The card scheme directory server confirms with ACS that the BIN is registered for 3D Secure
4. The ACS provider confirms if the BIN is registered and the card range is loaded on the card scheme directory server
5. The card scheme then directs the merchant to the URL for the pop up screen where the cardholder will enter the 3D Secure code. The pop up screen then appears on the web store interface. The pop up screen is set up by the ACS provider on a specific URL as the process is now handed over to the ACS provider for the rest of the 3D Secure steps
6. The ACS provider will send Paymentology the request to generate an OTP
7. Paymentology generates and sends the OTP on to the ACS provider and the wallet
8. The cardholder receives the Dynamic 3D Secure code (OTP) via a text message or through the app
9. The cardholder inputs the Dynamic 3D Secure code and clicks the “Submit” button. The Dynamic 3D Secure code goes to the ACS system and is validated
10. The ACS provider confirms the validation back to the web store page visible to the cardholder
11. The ACS provider then sends the result and UCAF (**MasterCard:** Universal Cardholder Authentication Field) / CAVV (**Visa:** Cardholder Authentication Value Verification) information to the merchant
12. The ACS provider sends a message to the card scheme’s AHS server to confirm that validation took place so that there is a history of the validation

The merchant then sends the transaction (with the UCAF/CAVV information in the transaction message) to the card scheme for authorization like any other transaction. The card scheme then sends the information to Paymentology.
Paymentology validates the UCAF/CAVV information and then perform all other relevant checks on the card for an authorization request.
