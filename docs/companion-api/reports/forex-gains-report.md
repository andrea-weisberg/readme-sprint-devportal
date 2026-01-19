---
title: Forex gains report
deprecated: false
hidden: false
metadata:
  robots: index
---
If you’re marking up a transaction with a forex fee, you’ll receive a report each day showing the FX amount that you earned as revenue for the day.

You can access this report by making an HTTP GET request and downloading it.

The report includes the following details:

* **Date** – the date of the settlement.
* **Voucher number** – the masked card number.
* **Activation data** – the unique wallet reference number.
* **Merchant description** – the merchant name.
* **Transaction id** – the unique transaction id used for the initial deduct.
* **reversed** – this shows if a fee was reversed.
* **Currency** – this shows the currency of the fee.
* **Fee** – the actual amount earned in forex fees.

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
      <td align="center">XLS or CSV</td>

      <td align="center">
        \[CampaignUUID]*DailyForexReport\_CAMID\[CampaignID]*\[YYYY\_MM\_DD].xls<br />
        or<br />
        \[CampaignUUID]*DailyForexReport\_CAMID\[CampaignID]*\[YYYY\_MM\_DD].csv
      </td>

      <td align="center">Daily</td>
      <td align="center">HTTP GET request or client SFTP folder</td>
    </tr>
  </tbody>
</table>

## Report time frame

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
        <strong>13:00 UTC+7</strong> (2020-09-10), the timeframe of all Forex Gains
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

## Report sample

<Image border={false} src="https://files.readme.io/950d55e521599b60f3926f3a5d8572ff276dd186de428cf651fc545f90a8a7f2-image.png" />

<NavyBlock />

<br />

[DailyForexReport_CAMID_(YYYY_MM_DD).xls](https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/DailyForexReport_CAMID_YYYY_MM_DD.xls)
