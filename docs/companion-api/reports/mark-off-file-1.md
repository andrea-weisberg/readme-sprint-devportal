---
title: Mark-off file
deprecated: false
hidden: false
metadata:
  robots: index
---
This file contains a record of all successful transactions that Paymentology processes on behalf of a store of value like a wallet or a bank account. It includes the financial transactions between a store of value and Paymentology.Paymentology generates the Mark-off file daily at midnight in your local time zone. The file matches a report from a store of value for all successfully processed transactions.

Ideally, the Mark-off file report and the store of value report should be in sync each day as the systems mirror one another. In case of any discrepancy, you should log a ticket via your Zendesk Portal. Select the _**Report a Service Incident**_ form, and then choose _**Reporting**_ and _**Discrepancy**_ under the Request type, indicate the file’s date and the transaction in question. We’ll promptly address the issue.

You can generate the Mark-off file by sending an HTTP GET request and downloading the report as a CSV file.

The Mark-off file has the following fields:

* **CampaignName** – name of client’s card program.
* **TransactionDate** – the merchant’s timestamp in their time zone.
* **TransactionAmount** – the transaction value in cents. For example, a value of 4215 will mean 42.15. Amount is in the card campaign’s billing currency. ‘-’ states the value is a debit and ‘+’ or no symbol states the value is a credit.
* **TransactionNarrative** – it’s the merchant’s description. Usually, the merchant’s name, city and country.
* **TransactionDescription** – this describes the transactions purpose such as:

  * `Deduct` – a deduction/debit.
  * `Load` – a refund/credit.
* **TransactionID** – the Transaction id of the transaction, as created by the card network.
* **TransactionType** – it can be marked as any of the following:

  * `0 – POS transaction`
  * `1 – ATM transaction`
  * `2 – Adjustment`
  * `20 – Refund`
  * `28 – Money Send`
* **WalletReference** – the customer reference associated to the card that transacted.
* **SystemDate** – Paymentology’s system date in UTC +2 time zone.
* **SequenceNumber** – Paymentology’s unique sequence identifier for the specific card used.
* **TrackingNumber** – Paymentology’s unique tracking identifier for the specific card used.
* **NetworkTransactionID** – (Mastercard only) this is the Networks TraceID, it assists clients with matching pre-authorizations and incremental pre-authorizations to the settlements for those transactions.

## Report format

<br />

<table>
  <thead>
    <tr>
      <th align="center">FORMAT</th>
      <th align="center">FILE NAME</th>
      <th align="center">FREQUENCY</th>
      <th align="center">ACCESSIBILITY</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td align="center">CSV</td>
      <td align="center">\[CampaignUUID]/\[CampaignName]*MarkOffFile*\[YYYYMMDD].csv</td>
      <td align="center">Daily</td>
      <td align="center">HTTP GET request or client SFTP folder</td>
    </tr>
  </tbody>
</table>

## Report time frame

<br />

<table>
  <thead>
    <tr>
      <th align="center">UTC +2</th>
      <th align="center">UTC +7</th>
      <th align="center">REMARKS</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td align="center">19:00</td>
      <td align="center">00:00</td>

      <td align="center">
        When the report is generated at <strong>19:00 UTC+2 (2020-09-10)</strong> /
        <strong>00:00 UTC+7 (2020-09-11)</strong>, the timeframe of all authorized
        transactions captured in this report is:<br /><br />
        • 2020-09-09 00:00:00 UTC+7 (system time) to 2020-09-09 11:59:59 UTC+2 (system time)<br />
        • 2020-09-10 00:00:00 UTC+7 (Asia client time) to 2020-09-10 11:59:59 UTC+2 (Asia client time)
      </td>
    </tr>
  </tbody>
</table>

## Report sample

<Image border={false} src="https://files.readme.io/60da279f946b5549f5bf0b8e50d5ca5209930fed5debcb7efffb62946c9e5f1e-image.png" />

<NavyBlock />

<br />

[CampaignName_MarkOffFile_GMT_plus_3_00h00_YYYYMMDD.csv](https://developer.sprint.paymentology.com/wp-content/uploads/2024/02/CampaignName_MarkOffFile_GMT_plus_3_00h00_YYYYMMDD.csv)
