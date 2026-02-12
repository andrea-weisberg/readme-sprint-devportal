---
title: eCommerce report
deprecated: false
hidden: false
metadata:
  robots: index
---
A report that shows successful and failed Ecommerce transactions along with associated eCommerce fees.

The report includes the following details:

* **TransactionID –** it’s a reference for the transaction
* **TrackingNumber** – this is a unique 15-digit tracking identifier for the card.
* **TransactionDescription** – this is a description of the merchant.
* **TransactionAmount** – the value of the transaction
* **TransactionDate** – This is the authorization date of the transaction
* **MerchantIdentitifer** – this is numeric identifier of the merchant. Usually 15 digits.
* **Fee** – this is the value of a fee the card has incurred for the transaction. Fee type must be one of the below:

  * `51 – Ecommerce Fee`
  * `52 – Online Fee`
  * `6 – POS Purchase Fee`
* **3DS** – specifies whether 3DS authentication occurred prior to the authorisation.
* **SuccessfulTransaction** – specifies whether the transaction was approved or declined.
* **TransactionFeeID** – the identifier of the transaction fee incurred.
* **TransactionFeeDescription** – describes the transaction fee.
* **TransactionFeeDate** – the date in which the transaction fee was applied.
* **DeclineReason** – describes why the transaction was declined. If the transaction was successful then this filed is left blank.
* **CaptureType** – capture type must be one of the below:

  * `ECOM – Transaction captured online`
  * `MAG – Magnetic Stripe captured transaction`
  * `MAN – Manually captured transaction`
  * `ECOF – Online Card On File transaction`
* **CaptureMode** – this is the respective capture mode of the card’s transaction. capture Mode must be one of the below:

  * `MAG – Magnetic Stripe captured transaction`
  * `EMV – Electronic chip captured transaction`
  * `ECOM – Transaction captured online (with no 3DS authentication)`
  * `3DS – Transaction captured online using 3DS authentication`
  * `MAN – Manually captured transaction`
  * `NFC – Transaction captured via a Near Field Communication device`
* **Recurring** – specifies whether the transactions is a once off or recurring through COF method.

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
      <td align="center">EcommerceTransactions\_\[CampaignName]\_\[YYYYMMDD].csv</td>
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
      <th align="center">REMARKS</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td align="center">09:00</td>
      <td align="center">14:00</td>

      <td align="center">
        When the report is generated, the timeframe of all captured data in this
        report is from <strong>00:00:00</strong> to <strong>11:59:59</strong> of
        the previous day in:

        <br />

        <br />

        • System time zone UTC+2<br />
        • Asia client time zone UTC+7
      </td>
    </tr>
  </tbody>
</table>

## Report sample

<Image border={false} src="https://files.readme.io/0cc5ea1a226c0bb50341fcdb5f3f58f48a186885fc8cdf5221005bab83d119d8-image.png" />

<NavyBlock />

<br />

[EcommerceTransactions_CampaignName_YYYYMMDD.csv](https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/EcommerceTransactions_CampaignName_YYYYMMDD.csv)
