---
title: 3D Secure – Out of band Authentication
deprecated: false
hidden: false
metadata:
  robots: index
---

## Overview of Out-of-Band (OOB) Authentication

Out-of-Band (OOB) authentication is a type of two-factor authentication (2FA) that uses a distinct communication channel for verification. It is an optional but recommended Challenge-flow method for 3DS transactions for Paymentology clients.

This applies to both Mastercard and Visa transactions.

### Operational Workflow

OOB is used during the 3DS Challenge flow and directs the process to an Issuer’s mobile application instead of a one-time password (OTP) sent via SMS.

During the Challenge flow, a push notification is sent to the Issuer’s mobile app. The app requests the cardholder to authenticate using biometrics (face or fingerprint) or a one-time password.

After authentication, the issuer communicates the result. If successful, the merchant can send the authorization request to complete the transaction.

### Paymentology's OOB Solution

Participants:

- **Cardholder:** Performs online purchases and authenticates via the Issuer mobile app.
- **ACS provider:** Access Control Server that authenticates the cardholder.
- **Paymentology:** Issuer processor, executing the card transaction for the client.
- **Issuing Client:** Operates the OOB Issuer mobile app and authenticates the client.

### Interaction Sequence

1. **Message reception and forwarding:**  
   Paymentology receives a JSON message from the ACS provider at a defined endpoint with relevant details. This is relayed to clients (Administrative Messages to Companion clients; Remote Messaging to others). The client acknowledges receipt to Paymentology and contacts the cardholder.

2. **Transaction approval/denial:**  
   The client then sends a separate API request to Paymentology’s Card or Companion API to approve or deny the transaction. Paymentology forwards the outcome to the ACS provider.

## Transaction flow

When a 3DS-enrolled cardholder performs an e-commerce transaction, authentication is required.

### Request and initial response

Paymentology is informed of the requested authentication by the ACS provider via an **Authentication Request** message.

- Paymentology checks which product the client uses:
  - **Companion API:** Paymentology sends an Administrative Message  
    MessageType: **[3DSecureAppAuthentication](https://developer.sprint.paymentology.com/companion-api/api-reference/remote/administrativemessage/#3DSAppAuth)**
  - **Card API:** Paymentology sends a RemoteMessaging message  
    MessageType: **[3DSecure.AppAuthentication](https://developer.sprint.paymentology.com/card-api/api-reference/remotemessaging/#appauth)**
- The client validates with the cardholder and acknowledges receipt of **3DSecure.AppAuthentication** to Paymentology.
- Paymentology acknowledges to the ACS provider that it has forwarded the **Authentication Request** to the client.

![Request-and-initial-response-Light](Request-and-initial-response-Light.png)

### Final response and final confirmation

Once the client completes authentication with the cardholder:

- The client calls **ThreeDSAuthenticationOutcome** to report success or failure:
  - **Companion API:** [ThreeDSAuthenticationOutcome](https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/threedsauthenticationoutcome/)
  - **Card API:** [ThreeDSAuthenticationOutcome](https://developer.sprint.paymentology.com/card-api/api-reference/threedsauthenticationoutcome/)
- Paymentology sends the authentication outcome to the ACS provider.
- The ACS provider sends a final confirmation message to Paymentology.
- Paymentology checks which product the client uses:
  - **Companion API:** Administrative Message  
    MessageType: **[3DSecureAppFinalisation](https://developer.sprint.paymentology.com/companion-api/api-reference/remote/administrativemessage/#3DSAppFinal)**
  - **Card API:** RemoteMessaging message  
    MessageType: **[3DSecure.AppFinalisation](https://developer.sprint.paymentology.com/card-api/api-reference/remotemessaging/#appfinal)**

![Final-Response-and-Final-Confirmation-Light](Final-Response-and-Final-Confirmation-Light.png)

### In summary

This method strengthens security by using a separate communication channel for verification. It is recommended for Paymentology clients seeking robust 3DS processing.
