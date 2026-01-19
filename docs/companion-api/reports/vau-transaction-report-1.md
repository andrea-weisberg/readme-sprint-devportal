---
title: VAU transaction report
deprecated: false
hidden: false
metadata:
  robots: index
---
The purpose of this report is to provide a list of transactions still occurring on a card that was previously submitted to VISA via the VAU (Visa Account Updater) file.

For example, if a card was sent to VISA in a VAU file on **Sep 18, 2023**, and transactions continued after the file was generated, that card will appear in this report.

### VAU Transaction Report fields

* **Wallet Reference** – unique identifier of the wallet (12-character string).
* **Merchant name** – name of the merchant where the transaction occurred.
* **Pre Authorisation Date** – date and time of the pre-authorisation (MM/DD/YYYY HH:MM:SS).
* **Vau File System Date** – generation date of the VAU file (MM/DD/YYYY HH:MM:SS).
* **Voucher id** – transaction ID associated with the voucher.
* **TrackingNumber** – unique identifier linked to the voucher number (15-character string).
* **Voucher Number** – the 16-digit card number sent to VISA in the VAU file.
* **Expiry Date** – the previous expiry date sent to VISA (YYMM format).
* **Service Identifier** – type of change that occurred on the card.

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
      <td align="center">VAUTransactionsReport\[ClientName]\_\[report generation date YYYY-MM-DD].csv</td>
      <td align="center">Monthly</td>
      <td align="center">Sent via email</td>
    </tr>
  </tbody>
</table>

## Report time frame

<ReportTimeFrame />

## Report sample

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
      <td align="center">VAUTransactionsReport\[ClientName]\_\[report generation date YYYY-MM-DD].csv</td>
      <td align="center">Monthly</td>
      <td align="center">Sent via email</td>
    </tr>
  </tbody>
</table>

<NavyBlock />

<br />

[VAUtransactionsReportClientName_YYYY-MM-DD.csv](https://developer.sprint.paymentology.com/wp-content/uploads/2024/02/VAUtransactionsReportClientName_YYYY-MM-DD.csv)
