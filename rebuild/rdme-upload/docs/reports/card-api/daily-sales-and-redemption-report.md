---
title: Daily sales and redemption report
category:
  uri: Reports
slug: card-api-daily-sales-and-redemption-report
position: 7
parent:
  uri: card-api-reports
---

A report which includes all Loads, Redemptions, Authorization, Fees that takes place on a voucher/card.

The report includes the following details:

- **VoucherEngineRef** - this is the vouchers table reference (integer).

- **VoucherNumber** - this is the actual card number (10 character string).

- **ControlVoucherNumber** - this is the main card number for a pocket campaign, where one plastic card is linked to multiple cards i.e. the pockets. Note: **ControlVoucherNumber** is only included in PocketCampaigns (16 character string).

- **TrackingNumber** - this is the public card number that we share with clients (15 character string).

- **MerchantName** - this is the name of the merchant (string).

- **Date** - this is the date of the transaction (YYYY/MM/DD HH:MM:SS).

- **Type** - this is the transaction type, which include (string): **Issued** - a card allocated to a cardholder and loaded.

- **Redeemed** - spend.

- **Cancelled** - removing a load from a cardholders account.

- **Authorised** - an authorisation, the first level of a transaction.

- **Method** - this is how the transaction was initiated or processed, which include (string): **Web**

- **SMS**

- **Batch**

- **Terminal**

- **Application**

- **IVR**

- **n/a**

- **Value** - this is the amount of the transaction (decimal).

- **Description** - this describes the transaction (string).

- **SequenceNumber** - A sequence number is essentially another card identifier which tells you the actual sequence number of the card/voucher (string).

## Report format

## Report time frame

## Report sample

Note: file will automatically download upon clicking link.

[CampaignName_DailySalesRedmeptionStatement YYYY-MM-DD.csv](https://developer.sprint.paymentology.com/wp-content/uploads/2024/02/CampaignName_DailySalesRedmeptionStatement-YYYY-MM-DD.csv)
