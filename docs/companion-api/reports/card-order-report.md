---
title: Card order
deprecated: false
hidden: false
metadata:
  robots: index
---
A **card order** is a request to print a physical card. With the Companion API, you can optionally issue a physical card to a customer by sending an order for printing to the card manufacturer. To initiate a request to print a physical card, you use the [OrderCard](https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/ordercard/) method in the Local API. On a daily basis at 19:30 UTC+2, Paymentology creates a batch order and submits it to the manufacturer for printing. A **card order** report lists all the orders that were processed on the previous day.

The report includes the following details:

* **Card Number** – this is the issued/created card number. Due to card numbers being sensitive data, the card number is usually presented in the format 1234xxxxxxxx5678.
* **Wallet Reference** – this is the unique customer reference for the card.
* **Date Created** – this is the date and time stamp of when the card number was issued. Usually in the format DD/MM/YYYY HH:MM.

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
      <td align="center">\[CampaignUUID]/\[CampaignName]*PanDetails*\[YYYYMMDD].csv</td>
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
      <td align="center">02:45</td>
      <td align="center">07:45</td>

      <td align="center">
        <strong>00:00:00 → 00:00:00 day + 1</strong>, UTC +2<br />
        Based on the time in UTC +2 that the report was requested.
      </td>
    </tr>
  </tbody>
</table>

## Report sample

<Image border={false} src="https://files.readme.io/05246a1defd16dbc32a29f85e691779d3372c0b7389d2d5d11bff95cf276556b-image.png" />

<br />

<NavyBlock />

<br />

[CampaignName_PanDetails_YYYYMMDD.csv](https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_PanDetails_YYYYMMDD.csv)
