---
title: Apple Pay Monthly Fee Billing Report
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  robots: index
---
For clients using Paymentology’s tokenization, Paymentology can issue monthly reports to clients to utilize the report data to compile their Apple report through the Apple Partner Connect platform.

The Apple Pay monthly fee billing report includes the following details:

* **Total Debit Spend** – this is the total settled transaction value of Apple Pay transactions in a given month. This includes contactless and eCommerce transactions that have been made using Apple Pay.
* **POS debit spend share** – this is the percentage of **Total Debit Spend** that was made at Point of Sale (POS) using Apple Pay. This includes the following capture Mode’s:

  * `EMV`
  * `NFC`
  * `MAG`
  * `MAN`
* **E-commerce debit spend share** – this is the percentage of **Total Debit Spend** that was eCommerce using Apple Pay. This includes the following capture Mode’s:

  * `ECOM`
  * `ECOF`

<div
  style={{
    background: "#0F1F3A",
    color: "#FFFFFF",
    padding: "0 16px",
    minHeight: "48px",
    display: "flex",
    alignItems: "center",
    gap: "12px",
    fontSize: "14px",
    fontWeight: 500,
    lineHeight: "20px",
  }}
>
  {/* Info icon (SVG, perfectly centered) */}

  <span
    style={{
      width: "20px",
      height: "20px",
      borderRadius: "50%",
      background: "#3B6EDC",
      display: "inline-flex",
      alignItems: "center",
      justifyContent: "center",
      flexShrink: 0,
    }}
    aria-hidden="true"
  >
    <svg width="12" height="12" viewBox="0 0 12 12" xmlns="http://www.w3.org/2000/svg" style={{ display: "block" }}>
      {/* dot */}

      <circle cx="6" cy="3" r="1" fill="#FFFFFF" />

      {/* stem */}

      <rect x="5.25" y="5" width="1.5" height="5" rx="0.75" fill="#FFFFFF" />
    </svg>
  </span>

  <span style={{ display: "inline-flex", alignItems: "center" }}>
    <span style={{ fontWeight: 800, marginRight: "6px" }}>Amount’s reported are in the cardholder billing currency.</span>
  </span>
</div>

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
        \[CampaignName]\_ApplePay Monthly Fee Billing Report<br />
        \[Month] YYYY.xls
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

<Image border={false} src="https://files.readme.io/7f1c377f5d27da2d91f65444997b9801ecb21ef5967824da982381d3e27e1b22-image.png" />

<NavyBlock />

<br />

[CampaignName_ApplePay Monthly Fee Billing Report Month YYYY.xls](https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_ApplePay-Monthly-Fee-Billing-Report-Month-YYYY.xls)