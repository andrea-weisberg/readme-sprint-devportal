---
title: Unsettled transactions report
category:
  uri: Reports
slug: companion-api-unsettled-transactions-report-2
position: 47
parent:
  uri: companion-api-reports
---

This report provides client's with a full list of unsettled transactions, it assists with overall reconciliation.

There are two versions of this report available:

[Version 1.0](#UTRV1)

[Version 2.0](#UTRV2.0)

### Version 1

This report includes the following details:

- **CampaignName** - Name of client’s campaign

- **TransactionDate**- This is the authorization date of the transaction

- **TransactionAmount** - the value of the transaction

- **TransactionNarrative** - it’s the merchant’s description

- **TransactionDecription**- this describes the transaction type, such as: DEDUCT - deductions or debits

- LOAD - refunds or credits

- CHARGEBACK

- **TransactionID** - it’s a reference for the transaction

- **TransactionType** - it can be marked as any of the following: 0 - POS Transaction

- 1 - ATM Transaction

- 2 - Adjustment

- **WalletReference** - this is a unique customer reference for the card (applicable to Companion API). This column will be empty for Card API reporting.

- **SystemDate** - this is Paymentology’s system date in UTC +2 time zone.

- **SequenceNumber**- this is a unique sequence card identifier showing a running number for the cards created.

- **TrackingNumber** - this is a unique 15-digit tracking identifier for the card.

### Version 2

This report includes the following details:

- **CampaignName** - Name of client’s campaign

- **TransactionDate**- This is the authorization date of the transaction

- **TransactionAmount** - the value of the transaction

- **TransactionNarrative** - it’s the merchant’s description

- **TransactionDecription**- this describes the transaction type, such as: DEDUCT - deductions or debits

- LOAD - refunds or credits

- CHARGEBACK

- **TransactionID** - it’s a reference for the transaction

- **TransactionType** - it can be marked as any of the following: 0 - POS Transaction

- 1 - ATM Transaction

- 2 - Adjustment

- **WalletReference** - this is a unique customer reference for the card (applicable to Companion API). This column will be empty for Card API reporting.

- **SystemDate** - this is Paymentology’s system date in UTC +2 time zone.

- **SequenceNumber**- this is a unique sequence card identifier showing a running number for the cards created.

- **TrackingNumber** - this is a unique 15-digit tracking identifier for the card.

- **NetworkTransactionID** - the Transaction ID of the transaction, as created by the card network. You can match this against the Transaction ID on the [Mark-off file](/reports/companion-api/mark-off-file)

## Report format

## Report time frame

## Report sample

![](https://files.readme.io/c2c50e3a784b38eee19a01ae6a93c837513045e5e16a10dcead2539f65b24fc2-cabd41a28af62f156ef463924aa92ba462f6ad6cc7957aa4e804fe9013eba11f-CampaignName_UnsettledTransactionReport_YYYYMMDD-.png)

**Note: file will automatically download upon clicking link**

[CampaignName_UnsettledTransactionReport_YYYYMMDD.csv](https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_UnsettledTransactionReport_YYYYMMDD.csv)

[CampaignName_UnsettledTransactionReport_YYYYMMDD.csv V2 sample](https://developer.sprint.paymentology.com/wp-content/uploads/2024/01/CampaignName_UnsettledTransactionReport_YYYYMMDD-V2sample.csv)
