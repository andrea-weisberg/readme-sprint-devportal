---
title: Fraud and Risk
deprecated: false
hidden: false
metadata:
  robots: index
---
<!-- MIGRATION_METADATA
Migrated-From: https://developer.sprint.paymentology.com/get-started/fraud/
Source-Slug: fraud
Migrated-On: 2026-02-12T19:23:23+00:00
Migrated-By: wp-readme-migration
-->

Paymentology provides a number of advanced fraud prevention and risk control mechanisms that ensure transactions are secure and trusted. These anti-fraud techniques allow you to build a robust and efficient payment system that protects your customers and ensures business success.

Let’s look at the fraud control measures.

## Transaction Limits

Paymentology Sprint allows you to implement transaction limits per card or program. If the ceiling is reached, no further transactions are permitted.

These are the transaction limits:

- Daily transaction limit

- Daily POS limit

- Daily ATM limit

- Daily transaction count POS

- Daily transaction count ATM

- Monthly POS limit

- Monthly ATM limit

- Monthly transaction count POS

- Monthly transaction count ATM


---

## Usage

Paymentology Sprint allows you to specify the payment methods that the card can be used with. If there is an attempted use of the card for an unspecified payment method, the transaction will fail and send a fraud alert.

- POS

- ATM

- Tokenization

- Moneysend

- Contactless

- EMV

- E-commerce


---

## Additional Settings

Paymentology Sprint allows you to implement additional settings to reinforce the security of cards and help with fraud prevention. These are the additional card settings:

- Enable multiple currencies linked cards

- Allow releasing of authorisations

- Max threshold to release funds for unsettled authorisations

- Time period to release authorisations

- Expiry time period

- PIN length

- BIN range splitting

- Filtering rules

- Cards created active or inactive

- Is the card readable

- Allow batch top ups from administrator portal

- Allow card orders from administrator portal


---

## Notifications

Paymentology Sprint lets you configure real-time notifications that keep customers informed about the state of their cards.

You can configure the following notifications:

- Notifications for declined transactions

- Notifications for transactions

- Notifications for 3D Secure


---

## Issuance checks

Paymentology Sprint allows you to implement the following issuance checks:

|  |
| --- |
| Checks on excessive voucher balances queries, large loads, multiple transactions and other suspicious activity |
| Checks on authorizations of cards that are not activated or linked |
| Checks on ASI Messages (Account Status Inquiry messages) for new and existing BINs added to production to monitor if<br>party is cycling through card numbers to get valid card numbers with expiry and CVV |
| If a card is EMV enabled, we can turn off magstripe fallback and only validate transactions if they come with EMV data as<br>the Paymentology Sprint host system does EMV validation |

## Spend Controls

Paymentology Sprint allows you to implement the following spend control measures:

|  |
| --- |
| Limits on single-day and multiple-day transaction velocity (number of transactions) |
| Limits on single-day and multiple-day monetary spending (value of transactions) |
| Limits for particular POS entry modes (magnetic stripe-read, PAN key-entry, chip-read, card not present etc.) |
| Limits for particular country codes |
| Limits on single transaction exceeding a certain amount |
| Multiple transactions exceeding a certain amount |
| Limits on number of transactions allowed per card based on program rules |

## Authorization Checks

Paymentology Sprint allows you to implement the following authorization checks:

|  |
| --- |
| Checks on CVC1 and CVC2- card is stopped if incorrect CVV is entered incorrectly three times |
| Checks on out of country usage |
| Checks on magstripe data present |
| Checks on refunds versus original transactions |
| Checks on blacklisted merchants |
| Checks on spend at single merchants |
| Checks on card spend spread across multiple merchants |
| Checks on card spend on an individual card at multiple merchants in 1 day |
| Checks on card spend at certain merchants identified by merchant category code (high risk MCC) |
| Checks on trends on settlements received that have no authorization. Determine if there are multiple/settlement<br>items received for a card that had no authorization, or across cards for a specific merchant |
| Check for a high volume of ATM transactions in rapid sequence on a single card number or multiple card numbers |
| Alert when a merchant has more than 50 transactions that failed with a an error code of 1001, 1018 or 1022 in the last 15<br>minutes |
| Alert when the number of ASI transactions is more than 5% of total number of transactions |
| Alert when the total number of successful and unsuccessful ATM transactions in the last 5 minutes exceeds the<br>transaction limit |
| Alert when the total value of international transactions in the last 5 minutes exceeds the limit |
