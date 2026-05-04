---
title: Authorisation income report
category:
  uri: Reports
slug: card-api-authorisation-income-report
position: 10
parent:
  uri: card-api-reports
---

This daily report provides client's with transaction markup data to support their internal reporting and P & L reconciliation. The report includes the following details:

- **CampaignID** - ID number of client’s campaign.

- **CampaignName**- name of client’s campaign.

- **TransactionDate** - this is the date the transaction was authorised.

- **AccumulatedTransactionOriginalAmount** - this is the total value of all the original amounts of the transactions without any markup.

- **AccumulatedMarkupAmount** - this is the total value of all the markup amounts of the transactions.

- **AccumulatedTransactionAuthorisedAmount** - this is the total value of all the transaction authorised amounts.

- **TransactionOriginalAmount** - this is the value of the transaction without any markup.

- **TransactionMarkupAmount**- this is the value of the markup amount.

- **TransactionAuthorisedAmount** - this is the value of the full transaction including markup.

- **TransactionDescription** - it’s the merchant’s description.

- **TransactionID** - it’s a reference for the transaction.

- **TransactionType** - ch2aracter string identifying the type of transaction: 0 = POS

- 1 = ATM

- 2 = Adjustments

- **WalletReference**- this is a unique customer reference for the card.

- **SystemDate** - this is Paymentology’s system date in UTC +2 time zone.

- **SequenceNumber** - this is a unique sequence card identifier showing a running number for the cards created.

- **TrackingNumber** - this is a unique 15-digit tracking identifier for the card.

## Report format

## Report time frame

## Report sample

![](https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_authorisationincomereport_YYYY_MM_DD-.png)

Note: file will automatically download upon clicking link

[CampaignName_authorisationincomereport_YYYY_MM_DD.csv](https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_authorisationincomereport_YYYY_MM_DD.csv)
