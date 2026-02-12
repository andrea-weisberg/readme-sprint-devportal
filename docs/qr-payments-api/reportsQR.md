---
title: Reports QR
deprecated: false
hidden: false
metadata:
  robots: index
---
<a id="Markoff"></a>

## 1. Mark-off file

This file contains a record of all successful transactions that Paymentology processes on behalf of a store of value like a wallet or a bank account. It includes the financial transactions between a store of value and Paymentology.

Paymentology generates the Mark-off file daily at midnight in your local time zone. The file matches a report from a store of value for all successfully processed transactions.

Ideally, the Mark-off file report and the store of value report should be in sync each day as the systems mirror one another. In case of any discrepancy, you should send a query to [support@paymentology.com](mailto:support@paymentology.com), indicating the file’s date and the transaction in question. We’ll promptly address the issue.

You can generate the Mark-off file by sending an HTTP GET request and download the report as a CSV file.

The Mark-off file has the following fields:

* **Time date** – the merchant’s timestamp, in their time zone.
* **Amount** – the transaction amount in cents.
* **Merchant description** – the merchant’s name, city and country.
* **Transaction description** – the API’s naming convention, such as card deduct, card reversal and card load.
* **Transaction id** – the Transaction id of the transaction, as created by the card network.
* **Transaction type** – it can be marked as 00 (for POS transactions), 01 (for ATM transactions), 02 (for adjustments), 09 (for cashback at POS), or 21 (for deposits).
* **Wallet / unique reference** – your unique customer reference information.
* **System date** – Paymentology’s system date in UTC +7 time zone.
* **Sequence number** – Paymentology’s unique sequence identifier for the specific card used.
* **Tracking number** – Paymentology’s unique tracking identifier for the specific card used.

## Report Sample

**Mark-Off-report-Companion-final.png IMAGE GOES HERE.**

---

<a id="summary"></a>

## 2. summary settlement report

This gives a daily summary of all the transactions settled by the card association. Paymentology gathers the information from the card association file and packages it into a summary report.

It is a report where you can find a summary of transaction types, the number of transactions that have been settled for the day, fees and interchanges earned.

The summary Settlement Report includes a separate tab for each currency you decide to settle in.

**Note:** If the client chooses to settle in one currency, then both domestic and international settlements will fall under one tab.

The report includes a combination of debits and credits that the network processes daily.

* **Credits** – include refunds, chargebacks and interchanges.
* **Debits** – include POS and ATM settlements, fees and unique transactions.

The network NETTs off the credits from the debits. So, only a single transfer will need to be made when settling with the network daily.

You can generate the summary Settlement Report by sending an HTTP GET request and download it in Excel format. The report is available daily from 2.00 a.m. (UTC+7).

Here is a description of the transactions you can find in the report:

* **Unique Transactions** – consist of transactions from merchants, such as casinos, gambling sites and pharmacies.
* **ATM Interchange** – it’s a debit fee that the card issuer sends to a card network to pay the bank agent where the ATM transaction took place.
* **Card Association Fee** – this can be either a debit or a credit transaction. As a debit transaction, there is a fee paid to a card network for a specific service rendered. As a credit transaction, there can be some discounts applied to the paid services. There is a difference between Card Association Fee Credit and Card Association Fee Reversal. The latter refers to a reversal provided back to the issuer via an incorrect charge, whereas the former is a discount given off the fees.
* **Payment transaction** – shows the settlements for MoneySend transactions

## Report Sample

**summary-Settlement-report-final.png IMAGE GOES HERE.**
