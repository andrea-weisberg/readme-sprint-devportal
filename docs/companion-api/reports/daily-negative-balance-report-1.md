---
title: Daily negative balance report
deprecated: false
hidden: false
metadata:
  robots: index
---
This report provides clients with detailed information on cards that have entered into a negative balance status. It provides essential, actionable information to trace the transactions and correct the negative balance scenarios.

* Clients will receive this report via email daily with the data from the previous day.
* All sensitive information, such as voucher numbers, are masked for security.

The report includes the following details:

* **VoucherNumber** – The voucher number associated with the card (masked for security purposes, only last four digits visible).
* **TrackingNumber** – Unique identifier for tracking the transaction.
* **WalletReference** – The unique wallet identifier associated with the card.
* **CardStatus** – Current status of the card (e.g. Active, Inactive).
* **VoucherBalanceAmount** – The balance of the card.
* **CampaignName** – name of the campaign to which the card belongs.
* **AuthorisationID** – The unique authorization id for the transaction that led to the balance.
* **AuthorisationAmount** – The authorized amount for the transaction.
* **AuthorisationDate** – The date when the authorization was made.
* **TransactionType** – type of transaction. 0 = POS transaction, 1 = ATM transaction, 2 = Adjustment.
* **CampaignCurrencySymbol** – The currency of the campaign to which the card belongs in ISO4217 alpha (e.g. USD).
* **MerchantName** – The name and address of the merchant where the transaction occurred.

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
      <td align="center">DailyNegativeBalanceReportOnChargebackQueue\_\[CampaignName]\_\[YYYYMMDD].csv</td>
      <td align="center">Daily</td>
      <td align="center">Email (automated)</td>
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
      <td align="center">Defined by client and configured by Paymentology.</td>
      <td align="center">Defined by client and configured by Paymentology.</td>

      <td align="center">
        The daily scheduled task generates the report for the previous day.
      </td>
    </tr>
  </tbody>
</table>

## Report sample

<NavyBlock />

<br />

[DailyNegativeBalanceReportOnChargebackQueue_CampaignName_YYYYMMDD.csv](https://developer.sprint.paymentology.com/wp-content/uploads/2024/10/DailyNegativeBalanceReportOnChargebackQueue_CampaignName_YYYYMMDD.csv)

[Back to Companion API Reports](https://developer.sprint.paymentology.com/companion-api/reports/)
