---
title: Card balance report
deprecated: false
hidden: false
metadata:
  robots: index
---
A report which includes all Loads, Redemptions, Authorization, Fees that takes place on a voucher/card.

The report includes the following details:

* **VoucherEngineRef** – this is the vouchers table reference (integer).
* **VoucherNumber** – this is the actual card number (10 character string).
* **ControlVoucherNumber** – this is the main card number for a pocket campaign, where one plastic card is linked to multiple cards i.e. the pockets. Note: **ControlVoucherNumber** is only included in PocketCampaigns (16 character string).
* **TrackingNumber** – this is the public card number that we share with clients (15 character string).
* **MerchantName** – this is the name of the merchant (string).
* **Date** – this is the date of the transaction (YYYY/MM/DD HH:MM:SS).
* **Type** – this is the transaction type, which include (string):
  * **Issued** – a card allocated to a cardholder and loaded.
  * **Redeemed** – spend.
  * **Cancelled** – removing a load from a cardholders account.
  * **Authorised** – an authorisation, the first level of a transaction.
* **Method** – this is how the transaction was initiated or processed, which include (string):
  * Web
  * SMS
  * Batch
  * Terminal
  * Application
  * IVR
  * n/a
* **Value** – this is the amount of the transaction (decimal).
* **Description** – this describes the transaction (string).
* **SequenceNumber** – A sequence number is essentially another card identifier which tells you the actual sequence number of the card/voucher (string).

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
        [CampaignName]_cardbalance_[YYYY]_[MM]_[DD].csv
      </td>
      <td align="center">Daily</td>
      <td align="center">HTTP GET request</td>
    </tr>
  </tbody>
</table>

## Report time frame

<table>
  <thead>
    <tr>
      <th align="center">UTC +2</th>
      <th align="center">UTC +7</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td align="center">08:00</td>
      <td align="center">13:00</td>
    </tr>
  </tbody>
</table>

## Report sample

<Image border={false} src="https://files.readme.io/85749b116fabeda29ec501d1b9b3c4bfc975b2da17ff592ec2f9a235e92fb654-image.png" />

<br />

<NavyBlock />

<br />

CampaignName_DailySalesRedmeptionStatement YYYY-MM-DD.csv

<br />
