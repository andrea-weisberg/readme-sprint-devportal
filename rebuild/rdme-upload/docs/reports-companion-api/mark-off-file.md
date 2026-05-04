---
title: Mark-off file
category:
  uri: Reports - Companion API
slug: mark-off-file
position: 22
parent:
  uri: reports
---

This file contains a record of all successful transactions that Paymentology processes on behalf of a store of value like a wallet or a bank account. It includes the financial transactions between a store of value and Paymentology.Paymentology generates the Mark-off file daily at midnight in your local time zone. The file matches a report from a store of value for all successfully processed transactions.

Ideally, the Mark-off file report and the store of value report should be in sync each day as the systems mirror one another. In case of any discrepancy, you should log a ticket via your Zendesk Portal. Select the ***Report a Service Incident*** form, and then choose ***Reporting*** and ***Discrepancy*** under the Request Type, indicate the file’s date and the transaction in question. We’ll promptly address the issue.

You can generate the Mark-off file by sending an HTTP GET request and downloading the report as a CSV file.

The Mark-off file has the following fields:

- **CampaignName** - name of client's card program.

- **TransactionDate**- the merchant’s timestamp in their time zone.

- **TransactionAmount**- the transaction value in cents. For example, a value of 4215 will mean 42.15. Amount is in the card campaign's billing currency. '-' states the value is a debit and '+' or no symbol states the value is a credit.

- **TransactionNarrative** - it's the merchant's description. Usually, the merchant’s name, city and country.

- **TransactionDescription** - this describes the transactions purpose such as: Deduct – a deduction/debit.

- Load – a refund/credit.

- **TransactionID** - the Transaction ID of the transaction, as created by the card network**.**

- **TransactionType**- it can be marked as any of the following: 0 – POS transaction

- 1 – ATM transaction

- 2 – Adjustment

- 20 - Refund

- 28 - Money Send

- **WalletReference** - the customer reference associated to the card that transacted.

- **SystemDate** - Paymentology's system date in UTC +2 time zone.

- **SequenceNumber** - Paymentology's unique sequence identifier for the specific card used.

- **TrackingNumber** - Paymentology's unique tracking identifier for the specific card used.

- **NetworkTransactionID** - (Mastercard only) this is the Networks TraceID, it assists clients with matching pre-authorizations and incremental pre-authorizations to the settlements for those transactions.

## Report format

## Report time frame

## Report sample

![MarkOff sample](https://developer.sprint.paymentology.com/wp-content/uploads/2021/10/Mark-Off-report-Companion-final.png)

**Note: file will automatically download upon clicking link**

[CampaignName_MarkOffFile_GMT_plus_3_00h00_YYYYMMDD.csv](https://developer.sprint.paymentology.com/wp-content/uploads/2024/02/CampaignName_MarkOffFile_GMT_plus_3_00h00_YYYYMMDD.csv)
