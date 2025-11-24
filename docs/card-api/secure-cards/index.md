---
title: Secure cards
deprecated: false
hidden: false
metadata:
  robots: index
---


**The Sprint Card API allows you to access a wide range of features to ensure the security of card transactions.**

Here are the main features available to secure your cards:

* Dynamic secure code on virtual cards
* Dynamic CVV on virtual cards
* PIN on physical cards
* Adding pockets to your card

Let’s look at each of them.

## 1. Using a dynamic secure code on virtual cards

A dynamic secure code allows you to increase the security of your virtual cards. If enabled, the secure code is required at the time of making any transaction, enhancing payment security and safeguarding against fraud.

The secure code is what Mastercard refers to as **3D Secure**, and Visa refers to as **Visa Secure** (formerly Verified by Visa / VbV).

To secure your virtual card with a dynamic secure code:

* Call the [`AdministrativeMessage`](https://developer.sprint.paymentology.com/companion/documentation/remote#administrativemessage) method.
* An OTP will be delivered to the cardholder via the [`OTPRequest`](https://developer.sprint.paymentology.com/remote-messaging/documentation#otprequest) method to complete the secure code process and finalize the transaction.

## 2. Using a dynamic CVV on virtual cards

The CVV (Card Verification Value) that comes with every virtual card is a static number used to validate the cardholder's identity.

To strengthen security or replace a compromised CVV:

* Call the `UpdateCVV` method.
  Paymentology will generate a new CVV, which you can then send to the cardholder.

## 3. Using a PIN on physical cards

A **PIN** (Personal Identification Number) is required for all ATM transactions and helps verify the cardholder’s identity.

Paymentology manages the card PIN:

* It can be pre-printed with the card in a tamper-proof package
* Or it can be set when the card is linked or issued

If the card PIN needs to be set or changed (e.g. forgotten or reset requested):

* Call the [`ChangePIN`](https://developer.sprint.paymentology.com/card/documentation/card-api#changepin) method
  Paymentology will issue a new PIN once the request is completed.

## 4. Adding pockets to your card

Multiple pockets allow additional versatility and security. You can maintain a main control card (PAN) and link additional pockets, each with its own balance.

Examples include:

* Multiple currency pockets
* Savings pockets
* Expenditure pockets
* Lifestyle pockets

Each pocket supports its own balance management and improves overall security.

To add pockets:

* Call the [`AddPocket`](https://developer.sprint.paymentology.com/card/documentation/card-api#addpocket) method
