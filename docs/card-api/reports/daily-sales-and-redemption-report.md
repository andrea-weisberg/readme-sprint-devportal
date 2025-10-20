---
title: Daily sales and redemption report
deprecated: false
hidden: false
metadata:
  robots: index
---

A report which includes all Loads, Redemptions, Authorizations, and Fees that take place on a voucher/card.

The report includes the following details:

- **VoucherEngineRef** – the vouchers table reference (integer).
- **VoucherNumber** – the actual card number (10-character string).
- **ControlVoucherNumber** – the main card number for a pocket campaign, where one plastic card is linked to multiple cards (the pockets).  
  _Note: ControlVoucherNumber is only included in Pocket Campaigns (16-character string)._
- **TrackingNumber** – the public card number shared with clients (15-character string).
- **MerchantName** – the name of the merchant (string).
- **Date** – the date of the transaction (YYYY/MM/DD HH:MM:SS).
- **type** – the transaction type, which can include:
  - **Issued** – a card allocated to a cardholder and loaded.
  - **Redeemed** – spend.
  - **Cancelled** – removing a load from a cardholder’s account.
  - **Authorised** – an authorization, the first level of a transaction.
- **method** – how the transaction was initiated or processed, which can include:
  - **Web**
  - **SMS**
  - **Batch**
  - **Terminal**
  - **Application**
  - **IVR**
  - **n/a**
- **value** – the amount of the transaction (decimal).
- **Description** – description of the transaction (string).
- **SequenceNumber** – another card identifier which shows the actual sequence number of the card/voucher (string).

## Report format

## Report time frame

## Report sample

[CampaignName_DailySalesRedmeptionStatement YYYY-MM-DD.csv](https://developer.sprint.paymentology.com/wp-content/uploads/2024/02/CampaignName_DailySalesRedmeptionStatement-YYYY-MM-DD.csv)
