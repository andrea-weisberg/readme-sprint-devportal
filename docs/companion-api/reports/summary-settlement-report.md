---
title: Summary settlement report
deprecated: false
hidden: false
metadata:
  robots: index
---
This gives a daily summary of all the transactions settled by the card association. Paymentology gathers the information from the card association file and packages it into a summary report.It is a report where you can find a summary of transaction types, the number of transactions that have been settled for the day, fees and interchanges earned.

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
      <td align="center">CSV or XLS</td>

      <td align="center">
        \[CampaignUUID]/\[CampaignName]Daily\_Settlement\_Report\_\[ICA]*\[YYYY\_MM\_DD].csv<br />
        or<br />
        \[CampaignUUID]/\[CampaignName]Daily\_Settlement\_Report*\[ICA]\_\[YYYY\_MM\_DD].xls
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
      <td align="center">08:00</td>
      <td align="center">13:00</td>

      <td align="center">
        When the report is generated at <strong>08:00 UTC+2</strong> /
        <strong>13:00 UTC+7</strong> (2020-09-10), the timeframe of all settled
        transactions captured in this report is from
        <strong>2020-09-09 00:00:00</strong> to
        <strong>2020-09-09 11:59:59</strong> in:

        <br />

        <br />

        • System time zone UTC+2<br />
        • Asia client time zone UTC+7<br />
        • Merchant time zone
      </td>
    </tr>
  </tbody>
</table>

## Report Sample

<Image border={false} src="https://files.readme.io/c6628862e371c950bd9e9f3ad091d46530c7158ba61dcfd2bc054e0b65fba296-image.png" />

<br />

[Daily_Settlement_Report_ICA_(YYYY_MM_DD).xls](https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/Daily_Settlement_Report_ICA_YYYY_MM_DD.xls)
