---
title: Apple Pay monthly declines report
deprecated: false
hidden: false
metadata:
  robots: index
---
For clients using Paymentology’s tokenization, Paymentology can issue monthly reports to clients to utilize the report data to compile their Apple report through the Apple Partner Connect platform.

The purpose of the Apple Pay monthly declines report is to provide oversight on Apple Pay transactions that have been declined. It is important to note that failed transactions are NOT considered as declined and therefore not considered for this report.

Declined transactions include those that were declined due to: daily limits exceeded, unable to authorize, no account, card status suspended, over credit line, unavailable funds, invalid PIN, expired card, cardholder authorization file, delinquent account.

The Apple Pay monthly declines report includes the following details:

* **Transaction size** – is the transaction amount of the reported transaction, denominated in Euros. In cases where the campaign billing currency, is in US Dollars (USD) [This also applies to other currencies], the amount will be converted to Euros using Paymentology’s exchange rate applicable at the end of the relevant month. Transaction size is split into:

  * `<10`
  * `10 – 25`
  * `25 – 50`
  * `50 – 100`
  * `100 – 250`
  * `250 – 1000`
  * `>1000`
* **Apple Pay Total POS Transactions** – this is the total number of transactions made using Apple Pay at Point of Sale for the reported month i.e. Apple Pay transactions that were not considered eCommerce.
* **Apple Pay Declined POS Transactions** – this is the total number of declined transactions for the reported month that were attempted using Apple Pay at Point of Sale.
* **Issuer POS Decline Rate (%)** – this is the percentage decline rate for the given month for Apple Pay POS transactions. The calculation is _Apple Pay Declined POS Transactions_ / _Apple Pay Total POS Transactions_ = _**Issuer POS Decline Rate.**_
* **Apple Pay Total Remote Transactions** – this is the total number of remote transactions made using Apple Pay for the reported month i.e. Apple Pay transactions that were considered eCommerce.
* **Apple Pay Declined Remote Transactions** – this is the total number of declined remote transactions for the reported month that were attempted using Apple Pay.
* **Issuer Remote Decline Rate (%)** – this is the percentage decline rate for the given month for Apple Pay remote transactions. The calculation is _Apple Pay Declined Remote Transactions_ / _Apple Pay Total Remote Transactions_ = _**Issuer Remote Decline Rate.**_

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
      <td align="center">XLS</td>

      <td align="center">
        \[CampaignName]\_ApplePay Declines Report<br />
        \[Month YYYY].xls
      </td>

      <td align="center">Monthly</td>
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
      <td align="center">02:00</td>
      <td align="center">07:00</td>

      <td align="center">
        Monthly Apple Pay reports are produced on day 2 of the following month.
      </td>
    </tr>
  </tbody>
</table>

## Report sample

<NavyBlock />

<br />

[CampaignName_ApplePay Declines Report MONTH YYYY.xls](https://developer.sprint.paymentology.com/wp-content/uploads/2024/01/CampaignName_ApplePay-Declines-Report-MONTH-YYYY.xls)
