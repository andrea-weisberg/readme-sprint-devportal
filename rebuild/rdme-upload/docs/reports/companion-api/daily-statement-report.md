---
title: Daily statement report
category:
  uri: Reports
slug: companion-api-daily-statement-report
position: 41
parent:
  uri: card-api-reports
---

The daily statement report can be used by client's to assist with their reconciliation and program activity reporting.

The report includes the following details:

- **TransactionID** - it's a unique reference for the transaction.

- **TransactionDate** - this is the date and time of the transaction.

- **TerminalTransactionDate** - this is the data and time of the initial transaction if the transaction has settled.

- **VoucherNumber** - the customer's card number.

- **VoucherSequenceNumber** -this is a unique sequence card identifier showing a running number for the cards created.

- **VoucherTrackingNumber** - this is a unique 15-digit tracking identifier for the card.

- **TransactionAmount** - the transaction value in cents. For example, a value of 4215 will mean 42.15. Amount is in the card campaign’s billing currency.

- **TransactionType** - it can be marked as any of the following: 0 – POS transaction

- 1 – ATM transaction

- 2 – Adjustment

- **MerchantCode** - this is the identifier code of the merchant.

- **MerchantName** - it's the merchant's name.

- **TransactionInfo** - it’s the merchant’s or adjustment description.

- **TransactionOperator** - it's the identifier of the operator if manually processed and provided.

## Report format

## Report time frame

## Report sample

Note: file will automatically download upon clicking link

[CampaignName_Statement_YYYYMMDD.csv](https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_Statement_YYYYMMDD.csv)
