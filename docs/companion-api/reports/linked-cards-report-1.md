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
      <td align="center">07:30</td>
      <td align="center">12:30</td>

      <td align="center">
        When the report is generated, the timeframe of all captured data in this report is from 00:00:00 to 11:59:59 the day before in: • System time zone UTC+2 • Asia client time zone UTC+7
      </td>
    </tr>
  </tbody>
</table>

## Report sample

<Image border={false} src="https://files.readme.io/bd945b717057cff9bdc01381ce99350a5731cd733116d5de9399f1f30bc2b3c2-image.png" />

<NavyBlock />

<br />

[CampaignName_Linked_Cards_YYYYMMDD.csv](https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_Linked_Cards_YYYYMMDD.csv)
