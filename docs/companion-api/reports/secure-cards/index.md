---
title: Secure cards
deprecated: false
hidden: false
metadata:
  robots: index
---
**The Paymentology Sprint Companion API allows you to secure your cards and ensure the safety of transactions.**

You can use the following three main ways to secure your companion cards:

* Dynamic CVV on virtual cards
* PIN on physical cards

## Securing a virtual card with a dynamic secure code

You can add an extra layer of security to your virtual card using a dynamic secure code. **The secure code is what Mastercard refers to as 3D Secure, and Visa refers to it as Visa Secure (formerly Verified by Visa (VbV)).** Mastercard and Visa created the technical standard to secure Cardholder Not Present (CNP) transactions.

**This method provides additional authentication to secure a customer’s virtual card during an online transaction.** It protects consumers against unauthorized use of cards and businesses from potential fraud liabilities.

3D Secure enables consumers to verify transactions using a One Time Pin (OTP), which is sent to their mobile device.

If your card program is enabled for Dynamic 3D Secure, the cardholder will be sent an OTP to conclude an online transaction. Through the Remote AdminMessage, Paymentology will send the OTP to your platform, which you can then send on to the cardholder.

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
