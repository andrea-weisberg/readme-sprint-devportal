---
title: Blocked transactions report
deprecated: false
hidden: false
metadata:
  robots: index
---
This report lists detailed information about filtered transactions for a specific set of campaigns, during a specified date range.
The report includes details about vouchers and reasons for transactions being filtered. This reports helps clients to identify if any whitelisted merchants (approved merchants) are blocked.

The report includes the following details:

* **Campaign** – name of client’s card program (string).
* **Terminal** – terminal information i.e. merchant name, city, country etc (string).
* **Reason** – filtered transaction reason i.e. unmatched (string).
* **Keyword** – filtered transaction blacklist keyword i.e. Estate Service Station (string). If there is no specific keyword then field will contain N/A.
* **type** – filtered transaction type, such as (string):

  * `POS`
  * `ATM`
* **Date Blocked** –  date the the transaction was blocked (YYYY/MM/DD HH:MM:SS).
* **Identifier** – the voucher number (numeric string).

## Report format

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
      <td align="center">XLS</td>
      <td align="center">\[CampaignName] Blocked Transactions - \[dateBegin:yymmdd] - \[dateEnd:yymmdd].xls</td>
      <td align="center">Weekly</td>
      <td align="center">Sent via email or SFTP</td>
    </tr>
  </tbody>
</table>

## Report time frame

<br />

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
      <td align="center">08:30</td>
      <td align="center">13:30</td>
      <td align="center">This report is generated weekly, only on Thursday.</td>
    </tr>
  </tbody>
</table>

## Report sample

<NavyBlock />

<br />

[CampaignName Blocked Transactions – 231015-231022.xls](https://developer.sprint.paymentology.com/wp-content/uploads/2024/02/CampaignName-Blocked-Transactions-231015-231022.xls)
