---
title: Inactive cards report
deprecated: false
hidden: false
metadata:
  robots: index
---
This report provides client’s with a list of inactive cards across their campaign. This allows client’s to better manage their campaign’s and internal reporting requirements.

The report includes the following details:

* **VoucherNumber** – the customer’s card number.
* **SequenceNumber** – this is a unique sequence card identifier showing a running number for the cards created.
* **ProfileNumber** – Profile number linked with the VoucherNumber.

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
      <td align="center">InactiveCards\_\[CampaignName]\_\[YYYY-MM-DD]-\[YYYY-MM-DD].csv</td>
      <td align="center">Monthly</td>
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
      <td align="center">06:50, on day 1 of month</td>
      <td align="center">11:50, on day 1 of month</td>

      <td align="center">
        When the report is generated, the timeframe of all captured data in this report is from 11:59:59 of the last day of previous month in:System time zone UTC+2 and Asia client time zone UTC+7
      </td>
    </tr>
  </tbody>
</table>

## Report sample

<Image border={false} src="https://files.readme.io/2103c99f7170f5f074394017d47623bbf1106d6341611fb35de32488cc736e90-image.png" />

<NavyBlock />

[InactiveCards_CampaignName_YYYY-MM-DD-YYYY-MM-DD.csv](https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/InactiveCards_CampaignName_YYYY-MM-DD-YYYY-MM-DD.csv)
