---
title: Mark-off file
deprecated: false
hidden: false
metadata:
  robots: index
---
This file contains a record of all successful transactions that Paymentology processes on behalf of a store of value like a wallet or a bank account. It includes the financial transactions between a store of value and Paymentology. Paymentology generates the Mark-off file daily at midnight in your local time zone. The file matches a report from a store of value for all successfully processed transactions.

Ideally, the Mark-off file report and the store of value report should be in sync each day as the systems mirror one another. In case of any discrepancy, you should log a ticket via your Zendesk Portal. Select the _Report a Service Incident_ form, and then choose **Reporting** and **Discrepancy** under the Request Type, indicate the file’s date and the transaction in question. We’ll promptly address the issue.

The Mark-off file has the following fields:

* Campaign Name – the name of the client’s campaign
* Paymentology System Date – Paymentology’s system date in UTC+7 time zone
* Time Date Stamp – the merchant’s timestamp, in their time zone
* Customer Reference – unique customer reference information
* Pocket ID – the UUID information for the client campaign
* Transaction Description – this described the transaction, such as:
* DeductFund – shows deductions/debits
* LoadFunds – shows loads/credits
* Transaction Type – the possible values for TransactionTypes are:
  * 0 – POS transaction
  * 1 – ATM transaction
  * 2 – Adjustment
* Transaction ID – the Transaction ID of the transaction, as created by the card network
* Sequence Number – Paymentology’s unique sequence identifier for the specific card used
* Tracking Number – Paymentology’s unique tracking identifier for the specific card used
* Amount – the transaction amount in cents

<br />

## Report format

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

      <td align="center">
        \[CampaignUUID]/\[CampaignName]*CardAPIMarkOffFile*\[YYYYMMDD].csv
      </td>

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
        transactions captured in this report is from:<br /><br />
        • <strong>2020-09-09 00:00:00 UTC+2</strong> (system time) to
        <strong>2020-09-09 11:59:59 UTC+2</strong> (system time)<br />
        • <strong>2020-09-10 00:00:00 UTC+7</strong> (Asia client time) to
        <strong>2020-09-10 11:59:59 UTC+7</strong> (Asia client time)
      </td>
    </tr>
  </tbody>
</table>

## Report sample

<Image border={false} src="https://files.readme.io/4e34f9a89ac1e4c8987cc060295d2485d33895b6d75c230af6e5c6cf82a7a6ec-image.png" />

<NavyBlock />

**CampaignName_MarkOffFile_YYYYMMDD.csv**
