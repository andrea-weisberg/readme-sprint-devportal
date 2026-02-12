---
title: Linked cards report
deprecated: false
hidden: false
metadata:
  robots: index
---
This report lists the cards that have been linked to a customer and when this occurred.

The report includes the following details:

* **Campaign** – name of client’s card program.
* **Voucher number** – the customer’s card number.
* **Reference** – this is a unique customer reference for the card.
* **Date linked** – specifies the date and time in which the card was linked to the **Reference**.

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
      <td align="center">CSV or XLS</td>

      <td align="center">
        \[CampaignName]*Linked\_Cards*\[YYYYMMDD].csv<br />
        or<br />
        \[CampaignName]*Linked\_Cards*\[YYYYMMDD].xls
      </td>

      <td align="center">Daily</td>
      <td align="center">Via email</td>
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
      <td align="center">07:30</td>
      <td align="center">12:30</td>

      <td align="center">
        When the report is generated, the timeframe of all captured data in this
        report is from <strong>00:00:00</strong> to <strong>11:59:59</strong> the
        day before in:

        <br />

        <br />

        • System time zone UTC+2<br />
        • Asia client time zone UTC+7
      </td>
    </tr>
  </tbody>
</table>

## Report sample

<Image border={false} src="https://files.readme.io/ea7f62be02e27c7c4eaf88705abe4fc4d1fbc6ac38a5d7c2dc27d4e6abc2eab3-image.png" />

<NavyBlock />

<br />

CampaignName_Linked_Cards_YYYYMMDD.csv
