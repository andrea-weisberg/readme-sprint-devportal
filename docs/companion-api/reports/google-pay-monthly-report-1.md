---
title: Google Pay monthly report
deprecated: false
hidden: false
metadata:
  robots: index
---
A report which provides detailed information about cards that were tokenised to a Google Pay wallet within a given month. Client’s can use the data from this report to fulfil their Google Pay reporting requirements.

The report includes the following details:

* **FirstLastName** – Customer’s first and last name
* **BillingPostalCode** – Customer’s postal code
* **BillingStreetAddress** – Customer’s postal street address
* **BillingCountryCode** – Customer’s postal country
* **BillingCity** – Customer’s postal city
* **BillingAdministrativeArea** – Customer’s postal region or state
* **FullPhoneNumber** – Customer’s contact number
* **OpaquePaymentCard** – Google Pay tokenised card number
* **FundingPrimaryAccountNumber** – Voucher number/Customer’s card number
* **ExpirationDate** – Expiry date of **OpaquePaymentCard**

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
      <td align="center">[CampaignName]googlepaymonthlyreport[MMM YYYY].csv</td>
      <td align="center">Monthly</td>
      <td align="center">HTTP get request and email.</td>
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
      <td align="center">12:00</td>
      <td align="center">17:00</td>

      <td align="center">
        WThe report is generated on day 1 of every month, the timeframe of all the captured data in this report is from 00:00:00 day 1 of previous month to 11:59:59 of last day of previous month in: • System time zone UTC+2 • Asia client time zone UTC+7.
      </td>
    </tr>
  </tbody>
</table>

## Report sample

**CampaignName_googlepay_monthlyreport_MMM-YYYY-.png IMAGE GOES HERE.**

[CampaignNamegooglepaymonthlyreportMMM YYYY.csv](https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignNamegooglepaymonthlyreportMMM-YYYY.csv)
