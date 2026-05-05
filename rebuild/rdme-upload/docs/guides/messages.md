---
title: Messages
category:
  uri: Guides
slug: messages
position: 25
parent:
  uri: companion-api-guide
---

**These are two types of messages that Paymentology Sprint can send to a client:**

## 1. Administrative Messages

These messages are **sent to the client to complete certain actions**.

### Use cases:

- [3DS OTP authentication](https://developer.sprint.paymentology.com/companion-api/api-reference/remote/#AdminsitrativeMessage3DSecureOTP) - Paymentology will send OTP messages to the fintech this will be sent on to the card holder to input during checkout

- [Token digitization](https://developer.sprint.paymentology.com/companion-api/api-reference/remote/#AdministrativeMessage) - During digitization, if authentication is required Paymentology will pass the authentication OTP to the fintech, the OTP will be passed to the card holder to complete digitization

- [Token management notifications](https://developer.sprint.paymentology.com/administrative-message-values/) - Paymentology will send token update notifications to the fintech if the status of the token changes

## 2. Stop Messages

These messages are **sent to notify you if Paymentology stopped the companion card.** For example, if a validation process has failed to pass, Paymentology would stop the card for security reasons and send a notification to that effect. This requires making a call to the [StopCard](/api-reference/companion-api/stopcard) method.
