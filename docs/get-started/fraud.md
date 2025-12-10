---
title: Fraud and Risk
deprecated: false
hidden: false
metadata:
  robots: index
---
Paymentology provides a number of advanced fraud prevention and risk control mechanisms that ensure transactions are secure and trusted. These anti-fraud techniques allow you to build a robust and efficient payment system that protects your customers and ensures business success.

Let’s look at the fraud control measures.

## Transaction Limits

Paymentology Sprint allows you to implement transaction limits per card or program. If the ceiling is reached, no further transactions are permitted.

These are the transaction limits:

* Daily transaction limit : Limits on single-day and multiple-day transaction velocity (number of transactions) & monetary spending (value of transactions).
* Daily POS limit / Daily transaction count POS : Limits on single-day velocity (number of transactions) & monetary spending (value of transactions) for POS transactions.
* Daily ATM limit / Daily transaction count ATM : Limits on single-day velocity (number of transactions) & monetary spending (value of transactions) for ATM transactions.
* Monthly POS limit / Monthly transaction count POS : Limits on monthly velocity (number of transactions) & monetary spending (value of transactions) for POS transactions.
* Monthly ATM limit / Monthly transaction count ATM : Limits on monthly velocity (number of transactions) & monetary spending (value of transactions) for ATM transactions.

## Usage

Paymentology Sprint allows you to specify the payment methods that the card can be used with. If there is an attempted use of the card for an unspecified payment method, the transaction will fail and send a fraud alert.

Here are some of the common methods:

* POS
* ATM
* Tokenization
* Moneysend
* Contactless
* EMV
* E-commerce

## Additional Settings

Paymentology Sprint allows you to implement additional settings to reinforce the security of cards and help with fraud prevention. These are the additional card settings:

* Allow releasing of authorisations
* Max threshold to release funds for unsettled authorisations
* Time period to release authorisations
* Expiry time period
* PIN length

## Notifications

Paymentology Sprint lets you configure real-time notifications that keep customers informed about the state of their cards.

You can configure the following notifications:

* Notifications for declined transactions
* Notifications for successful transactions and reversals

These notifications are sent via the transaction stream: [https://developer.sprint.paymentology.com/notifications/](https://developer.sprint.paymentology.com/notifications/)

## Authorization Checks

Paymentology Sprint allows you to implement the following authorization checks:

Checks on CVC1 and CVC2- card is stopped if incorrect CVV (3-digit code printed on the back of card) is entered incorrectly three times

Checks on magstripe data present

Checks on blacklisted merchants /out of country usage)/high risk merchants

Checks for limits setup on the campaign.

## Alerts

Paymentology has some alerts in place to monitor suspicious/ fraudulent activity

Alert when a merchant has more than 50 transactions that failed with a an error code of 1001 (Expired Crad), 1018 (No card Record/card doesn’t exist) or 1022(security violation eg. incorrect CVV) in the last 15 minutes

Alert for Number of successful transactions from countries of BRA,MEX,RUS,CAN for the BIN compared to total number of successful transactions in the last 30 minutes.

## Merchant Blocking

Paymentology supports various fraud block rule types including :

​BIN equal to and Acceptor Name​/Merchant ID - This refers to blocking a merchant at BIN level using the MID/Merchant name

Paymentology also has rules that can be setup at campaign level and can be validated with the client.
Here are some of the rules

AcquirerCountry, ​TerminalID​, and ​MerchantID​ combinations for more precise merchant blocking

Country-level blocks  - Reject transactions from Specific Countries

Restricting Card Use to Specific Countries in a Region

Terminal Entry Mode blocks

Blocking non-3DS transactions

Blocking Merchant Categories

## Settlement

A Report can be sent to notify the client of any settlement transactions processed without corresponding authorizations that have resulted in a negative balance on a card.
This report enables the client to  review and investigate such occurrences, ensuring resolution and maintaining the accuracy of card balances and settlement records.
