---
title: Apple Pay monthly declines report
category:
  uri: Reports - Companion API
slug: apple-pay-monthly-declines-report
position: 2
parent:
  uri: reports
---

For clients using Paymentology’s tokenization, Paymentology can issue monthly reports to clients to utilize the report data to compile their Apple report through the Apple Partner Connect platform.

The purpose of the Apple Pay monthly declines report is to provide oversight on Apple Pay transactions that have been declined. It is important to note that failed transactions are NOT considered as declined and therefore not considered for this report.

Declined transactions include those that were declined due to: daily limits exceeded, unable to authorize, no account, card status suspended, over credit line, unavailable funds, invalid PIN, expired card, cardholder authorization file, delinquent account.

The Apple Pay monthly declines report includes the following details:

- **Transaction Size** - is the transaction amount of the reported transaction, denominated in Euros. In cases where the campaign billing currency, is in US Dollars (USD) [This also applies to other currencies], the amount will be converted to Euros using Paymentology's exchange rate applicable at the end of the relevant month. Transaction size is split into: 1000

- **Apple Pay Total POS Transactions** - this is the total number of transactions made using Apple Pay at Point of Sale for the reported month i.e. Apple Pay transactions that were not considered eCommerce.

- **Apple Pay Declined POS Transactions** - this is the total number of declined transactions for the reported month that were attempted using Apple Pay at Point of Sale.

- **Issuer POS Decline Rate (%)** - this is the percentage decline rate for the given month for Apple Pay POS transactions. The calculation is Apple Pay Declined POS Transactions / Apple Pay Total POS Transactions = **Issuer POS Decline Rate.**

- **Apple Pay Total Remote Transactions** - this is the total number of remote transactions made using Apple Pay for the reported month i.e. Apple Pay transactions that were considered eCommerce.

- **Apple Pay Declined Remote Transactions** - this is the total number of declined remote transactions for the reported month that were attempted using Apple Pay.

- **Issuer Remote Decline Rate (%)**- this is the percentage decline rate for the given month for Apple Pay remote transactions. The calculation is Apple Pay Declined Remote Transactions / Apple Pay Total Remote Transactions = **Issuer Remote Decline Rate.**

## Report format

## Report time frame

## Report sample

Note: file will automatically download upon clicking link.

[CampaignName_ApplePay Declines Report MONTH YYYY.xls](https://developer.sprint.paymentology.com/wp-content/uploads/2024/01/CampaignName_ApplePay-Declines-Report-MONTH-YYYY.xls)
