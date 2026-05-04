---
title: VAU transaction report
category:
  uri: Reports
slug: companion-api-vau-transaction-report
position: 54
parent:
  uri: card-api-reports
---

The purpose of this report is to send to the client the transactions that are still being made to a certain card that was already sent to VISA via the VAU file.

So for example if a card was sent to VISA in a VAU file on the date Sep 18, 2023 and transactions are still happening after the file was generated the card will be on the report.

The VAU Transaction Report has the following fields:

- **Wallet Reference** - this is the unique identifier of the wallet (12 character string).

- **Merchant Name** - this is the name of the merchant where the transaction took place (string).

- **Pre Authorisation Date** - date of the pre-authorisation (MM/DD/YYYY HH:MM:SS).

- **Vau File System Date** - VAU file generation date (MM/DD/YYYY HH:MM:SS).

- **Voucher ID** - corresponds to the transaction ID associated with the voucher (integer).

- **TrackingNumber** - this is the unique identifier linked to the voucher number (15 character string).

- **Voucher Number** - the voucher number sent to VISA in the VAU file (16 character string).

- **Expiry Date** - the old expiry date sent to VISA in the VAU file (YYMM).

- **Service Identifier** - this identifies the type of change that occurred on the card (string).

## Report format

## Report time frame

## Report sample

Note: file will automatically download upon clicking link.

[VAUtransactionsReportClientName_YYYY-MM-DD.csv](https://developer.sprint.paymentology.com/wp-content/uploads/2024/02/VAUtransactionsReportClientName_YYYY-MM-DD.csv)
