---
title: Apple Pay monthly top merchant report
deprecated: false
hidden: false
metadata:
  robots: index
---
For clients using Paymentology’s tokenization, Paymentology can issue monthly reports to assist with compiling the required Apple Pay reports through the Apple Partner Connect platform.

The purpose of this report is for Apple to identify the **top 100 merchants** that accept Apple Pay. Only approved/settled transactions are reported, and merchants are listed in descending order based on total spend.

The report includes the following details:

* **Rank** – Merchant rank in descending order based on % of total Apple Pay transaction (spend).
* **Top 100 Merchants** – The merchant description.
* **% of Total Apple Pay Transaction (Spend)** – The merchant's total spend amount as a percent of the overall Apple Pay transaction spend.
* **Transaction Spend** – The total value in Apple Pay transactions spent at the merchant within the given month.
* **Transaction Count** – The total number of Apple Pay transactions at the merchant within the given month.

***

## Report Format

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
        \[CampaignName]\_ApplePay Monthly Top Merchant Report<br />
        \[Month] YYYY.xls
      </td>

      <td align="center">Monthly</td>
      <td align="center">Via email</td>
    </tr>
  </tbody>
</table>

## Report Time Frame

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

## Report Sample

<Image border={false} src="https://files.readme.io/6000680592f26151b636c4b78b2b2f4d8ea7811a62be6f4e8690402628b02ba7-image.png" />

<NavyBlock />

[Download the sample report (XLS)](https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_ApplePay-Top-Merchant-Report-MMM-YYYY.xls)

<br />
