---
title: Unsettled transactions report
deprecated: false
hidden: false
metadata:
  robots: index
---
This report provides client’s with a full list of unsettled transactions, it assists with overall reconciliation.

There are two versions of this report available:

[Version 1.0](#UTRV1)
[Version 2.0](#UTRV2.0)

### Version 1

This report includes the following details:

* **CampaignName** – name of client’s campaign
* **TransactionDate** – This is the authorization date of the transaction
* **TransactionAmount** – the value of the transaction
* **TransactionNarrative** – it’s the merchant’s description
* **TransactionDecription** – this describes the transaction type, such as:

  * `DEDUCT` – deductions or debits
  * `LOAD` – refunds or credits
  * `CHARGEBACK`
* **TransactionID** – it’s a reference for the transaction
* **TransactionType** – it can be marked as any of the following:

  * `0 – POS Transaction`
  * `1 – ATM Transaction`
  * `2 – Adjustment`
* **WalletReference** – this is a unique customer reference for the card (applicable to Companion API). This column will be empty for Card API reporting.
* **SystemDate** – this is Paymentology’s system date in UTC +2 time zone.
* **SequenceNumber** – this is a unique sequence card identifier showing a running number for the cards created.
* **TrackingNumber** – this is a unique 15-digit tracking identifier for the card.

***

<br />

### Version 2

This report includes the following details:

* **CampaignName** – name of client’s campaign
* **TransactionDate** – This is the authorization date of the transaction
* **TransactionAmount** – the value of the transaction
* **TransactionNarrative** – it’s the merchant’s description
* **TransactionDecription** – this describes the transaction type, such as:

  * `DEDUCT` – deductions or debits
  * `LOAD` – refunds or credits
  * `CHARGEBACK`
* **TransactionID** – it’s a reference for the transaction
* **TransactionType** – it can be marked as any of the following:

  * `0 – POS Transaction`
  * `1 – ATM Transaction`
  * `2 – Adjustment`
* **WalletReference** – this is a unique customer reference for the card (applicable to Companion API). This column will be empty for Card API reporting.
* **SystemDate** – this is Paymentology’s system date in UTC +2 time zone.
* **SequenceNumber** – this is a unique sequence card identifier showing a running number for the cards created.
* **TrackingNumber** – this is a unique 15-digit tracking identifier for the card.
* **NetworkTransactionID** – the Transaction id of the transaction, as created by the card network. You can match this against the Transaction id on the [Mark-off file](https://developer.sprint.paymentology.com/companion-api/reports/mark-off-file/)

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
      <td align="center">\[CampaignName]*UnsettledTransactionReport*\[YYMMDD].csv</td>
      <td align="center">Hourly</td>
      <td align="center">HTTP GET request</td>
    </tr>
  </tbody>
</table>

## Report time frame

<table>
  <thead>
    <tr>
      <th align="center">REMARKS</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td align="center">
        The report is generated once per hour for every campaign.
      </td>
    </tr>
  </tbody>
</table>

## Report sample

<Image border={false} src="https://files.readme.io/6d38d57300edd4c4bdef5c0bbaa590ead1353ff6cfc67dcee2ede7a1a0191b84-image.png" />

<NavyBlock />

<br />

[CampaignName_UnsettledTransactionReport_YYYYMMDD.csv](https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_UnsettledTransactionReport_YYYYMMDD.csv)
[CampaignName_UnsettledTransactionReport_YYYYMMDD.csv V2 sample](https://developer.sprint.paymentology.com/wp-content/uploads/2024/01/CampaignName_UnsettledTransactionReport_YYYYMMDD-V2sample.csv)
