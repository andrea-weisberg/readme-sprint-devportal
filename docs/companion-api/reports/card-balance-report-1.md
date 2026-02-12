---
title: Card balance report
deprecated: false
hidden: false
metadata:
  robots: index
---
This report provides clients with card details such as, current available balance, last load and lifetime expenditure. It is available for each Campaign.

The report includes the following details:

* **Campaign name** – name of client’s card program.
* **Voucher Number** – the customer’s card number.
* **Sequence Number** – this is a unique sequence card identifier showing a running number for the cards created.
* **Tracking Number** – this is a unique 15-digit tracking identifier for the card.
* **WalletReference** – this is a unique customer reference for the card.
* **Balance** – this is the amount available on the card.
* **Last Load Amount** – this is the value of the most recent load/top-up made to the card.
* **Last Load Date** – this is the date the most recent load/top up was received on the card.
* **Last Load Merchant** – this is the description of the merchant the **Last Load** was made through.
* **Load Total** – this is the total value the card has been loaded since it was first issued.
* **Authorisation Total** – this is the total value of all successful transactions the card has made since it was first issued.
* **Cancelled** – this advises whether the card is currently in a cancelled state at the time of the report.
* **Stopped** – this advises whether the card is currently in a stopped state at the time of the report.
* **Retired** – this advises whether the card is in a retired state at the time of the report.
* **Voucher Expiry Date** – specifies the date in which the card expires.

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
      <td align="center">[CampaignName]_cardbalance_[YYYY]_[MM]_[DD].csv</td>
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
      <td align="center">08:00</td>
      <td align="center">13:00</td>

      <td align="center">
        When the report is generated, the timeframe of all captured data in this report is from 00:00:00 to 11:59:59 of the previous day: • System time zone UTC+2 • Asia client time zone UTC+7
      </td>
    </tr>
  </tbody>
</table>

## Report sample

<Image border={false} src="https://files.readme.io/742b51c0d34de54601aa8469cb10cca4279d96d47c7a762f1148af065a87c1d2-image.png" />

<NavyBlock />

<br />

[CampaignName_cardbalances_YYYY_MM_DD.csv](https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_cardbalances_YYYY_MM_DD.csv)
