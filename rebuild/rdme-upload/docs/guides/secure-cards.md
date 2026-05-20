---
title: Secure cards
category:
  uri: Guides
slug: secure-cards
position: 14
parent:
  uri: companion-api-guide
---

**The Paymentology Sprint Companion API allows you to secure your cards and ensure the safety of transactions.**

You can use the following three main ways to secure your companion cards:

- Dynamic secure code on virtual cards

- PIN on physical cards

## 1. Securing a virtual card with a dynamic secure code

You can add an extra layer of security to your virtual card using a dynamic secure code. **The secure code is what Mastercard refers to as 3D Secure, and Visa refers to it as Visa Secure (formerly Verified by Visa (VbV)).** Mastercard and Visa created the technical standard to secure Cardholder Not Present (CNP) transactions.

**This method provides additional authentication to secure a customer’s virtual card during an online transaction.** It protects consumers against unauthorized use of cards and businesses from potential fraud liabilities.

3D Secure enables consumers to verify transactions using a One Time Pin (OTP), which is sent to their mobile device.

If your card program is enabled for Dynamic 3D Secure, the cardholder will be sent an OTP to conclude an online transaction. Through the Remote AdminMessage, Paymentology will send the OTP to your platform, which you can then send on to the cardholder.

## 2. Securing a physical card with a PIN

Your customers will require a PIN (personal identification number) for all ATM transactions. A secret PIN assists in verifying your users’ identity and allowing them to perform secure transactions.

There are two options for managing your PIN: **Paymentology manages the PIN** or **you manage the PIN**

**OPTION 1** - Paymentology manages the PIN

If you choose this option, Paymentology will manage the PIN on your behalf. This implies that **Paymentology will validate the PIN before sending it to a store of value for authorizing the transaction.**

When Paymentology manages the PIN, you can choose between these options:

**a)** The PIN is pre-printed in a tamper-proof package containing the card. This would be the PIN the cardholder would use for making transactions.

**b)** The PIN is not printed on the package. This implies it would be set when the card is linked or issued.

In case the card PIN needs to be set for the first time or changed at a later time, or if the customer forgets it or requests it to be changed, you’ll need to make a call to the [ChangePIN](/api-reference/companion-api/changepin) method to do this. Once the API request has been completed, Paymentology will issue a new PIN, which the cardholder can use for making transactions.

**OPTION 2** - You manage the PIN

This second option allows the store of value organization to manage the PIN and perform PIN validation based on a PINblock that Paymentology sends. Paymentology will then send a PINblock in the KLV (Key-Length-Value) transaction data based on pre-shared keys, which allow for encryption and decryption to pass the PIN for secure validation.
