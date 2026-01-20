---
title: QVR data report
deprecated: false
hidden: false
metadata:
  robots: index
---
The purpose of this report is to send to the client the transactions that are still being made to a certain card that was already sent to VISA via the VAU file.

So for example if a card was sent to VISA in a VAU file on the date Sep 18, 2023 and transactions are still happening after the file was generated the card will be on the report.

The VAU Transaction Report has the following fields:

* **Wallet Reference** – this is the unique identifier of the wallet (12 character string).
* **Merchant Name** – this is the name of the merchant where the transaction took place (string).
* **Pre Authorisation Date** – date of the pre-authorisation (MM/DD/YYYY HH:MM:SS).
* **Vau File System Date** – VAU file generation date (MM/DD/YYYY HH:MM:SS).
* **Voucher ID** – corresponds to the transaction ID associated with the voucher (integer).
* **TrackingNumber** – this is the unique identifier linked to the voucher number (15 character string).
* **Voucher Number** – the voucher number sent to VISA in the VAU file (16 character string).
* **Expiry Date** – the old expiry date sent to VISA in the VAU file (YYMM).
* **Service Identifier** – this identifies the type of change that occurred on the card (string).

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
        VAUTransactionsReport\[ClientName]\_\[report generation date YYYY-MM-DD].csv
      </td>

      <td align="center">Monthly</td>
      <td align="center">Sent via email</td>
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
      <td align="center">08:05</td>
      <td align="center">08:05</td>

      <td align="center">
        Generated daily in the client's campaign timezone.
      </td>
    </tr>
  </tbody>
</table>

## Report sample

<NavyBlock />

[VAUtransactionsReportClientName_YYYY-MM-DD.csv]()
