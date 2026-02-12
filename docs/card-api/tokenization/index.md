---
title: Tokenization
deprecated: false
hidden: false
metadata:
  robots: index
---
<!-- MIGRATION_METADATA
Migrated-From: https://developer.sprint.paymentology.com/card-api/tokenization/
Source-Slug: tokenization
Migrated-On: 2026-02-12T20:19:15+00:00
Migrated-By: wp-readme-migration
-->

Tokenization is the process of substituting the card’s sensitive data, such as an account number, with non-sensitive, surrogate data, called a token. The PAN (Primary Account Number) is usually replaced with a unique string of numbers that acts as a secure reference to the card.

Only the token is provided when a payment transaction is initiated, without revealing the original card details. This desensitization greatly improves the security of transactions.

The Sprint platform allows you to take advantage of the tokenization technology—both by facilitating the provisioning of the cards and by providing control over the token lifecycle management process. With an existing virtual or physical card that has been issued by Paymentology, enabling card tokenization becomes easier.

So, tokenization mainly involves two key tasks:

- **Card provisioning** – when a token is created for a full PAN.

- **Token lifecycle management** – when an event occurs on a token.


## **Benefits of Tokenization**

- Tokenizing customers’ private account data greatly enhances the security of transactions. A token has no meaningful value, if breached.

- It drives payment innovation on Paymentology’s Sprint platform, such as the adoption of digital wallet technology—like Apple Pay and Android Pay. These wallets store digital versions of payment cards, avoiding the need to carry physical cards.

- It creates smooth, secure, and fast customer payment experiences when making contactless payments or face-to-face payments.

- It simplifies attaining and maintaining compliance with the payment industry standards, which fosters customer loyalty and trust.


## **Terminology**

Here is a table describing the common phrases used in the tokenization process.


| TERM | DEFINITION |
| --- | --- |
| TSP (Token Service Provider) | The TSP is the custodian of all token. It's responsible for token creation, token suspension, token resumption, token deletion, and token re-digitization. |
| Token Vault | The TSP owned secure vault where tokens are stored along with their full PANs mapped to each token. |
| Card provisioning | The process of a card being tokenized. |
| Push provisioning | The cardholder pushes the card from their card app directly into a digitized wallet with a click of the button. |
| Manual provisioning | The cardholder physically enters the card details into the digitized wallet. |
| TAV (Token Authentication Value) | An encrypted value sent to MDES to verify that the card details exist and are valid. TAV is only used on Push provisioning. |
| TER | Token Eligibility Request |
| Token Suspended | When a token is stopped |
| Token Resumed | When a token is unstopped |
| Token Deleted from Device | When a token has been deleted from a specific digital device. |
| Token Deleted | Token has been deleted in it's entirety. The token cannot be retrieved ever again. |
| Token Requester | An online merchant or digital wallet that requests a token to be provided for a transaction. Examples include M4Ms, Apple Pay, Samsung Pay, Google Pay and Garmin Pay |
| Digitized Wallet or Xpay | These include digital wallets such as M4Ms, Apple Pay, Samsung Pay, Google Pay and Garmin Pay |
| WID | The is the Wallet ID for the above-listed wallets/merchants. It is represented by a 3-digit numeric value |
| KLV (Key Length Value) | Is a string of data that is passed onto clients through the Sprint API. The *key* identifies the data, *length* specifies the data's length, and *value* is the data itself. |
