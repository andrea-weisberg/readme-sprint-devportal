---
title: Daily statement report
deprecated: false
hidden: false
metadata:
  robots: index
---

The daily statement report can be used by clients to assist with reconciliation and program activity reporting.

The report includes the following details:

- **TransactionID** – a unique reference for the transaction.
- **TransactionDate** – the date and time of the transaction.
- **TerminalTransactionDate** – the date and time of the initial transaction if the transaction has settled.
- **VoucherNumber** – the customer’s card number.
- **VoucherSequenceNumber** – a unique sequence card identifier showing a running number for the cards created.
- **VoucherTrackingNumber** – a unique 15-digit tracking identifier for the card.
- **TransactionAmount** – the transaction value in cents. For example, a value of 4215 means 42.15. Amount is in the card campaign’s billing currency.
- **TransactionType** – can be marked as any of the following:
  - 0 – POS transaction
  - 1 – ATM transaction
  - 2 – Adjustment
- **MerchantCode** – the identifier code of the merchant.
- **MerchantName** – the merchant’s name.
- **TransactionInfo** – the merchant’s or adjustment description.
- **TransactionOperator** – the identifier of the operator if manually processed and provided.

## Report format

## Report time frame

## Report sample

[CampaignName_Statement_YYYYMMDD.csv](https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_Statement_YYYYMMDD.csv)
