---
title: Apple Pay Quarterly Fee Billing Report
excerpt: >-
  Learn about the Apple Pay quarterly fee billing report, including details on
  total debit spend, POS and e-commerce spend shares, and report formats.
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  robots: index
---
For clients using Paymentology’s tokenization, Paymentology can issue a quarterly report to clients to utilize the report data to compile their Apple report through the Apple Partner Connect platform.

The report includes the following details:

* **Total Debit Spend** – this is the total settled transaction value of Apple Pay transactions for the given quarter. This includes contactless and eCommerce transactions that have been made using Apple Pay.
* **POS debit spend share** – this is the percentage of **Total Debit Spend** that was made at Point of Sale (POS) using Apple Pay. This includes the following capture Mode’s:

  * `EMV – chip cards`
  * `NFC – Near Field Communication devices`
  * `MAG – Magnetic stripe`
  * `MAN – Manual entry`
* **E-commerce debit spend share** – this is the percentage of **Total Debit Spend** that was eCommerce using Apple Pay. This includes the following capture Mode’s:

  * `ECOM – eCommerce`
  * `ECOF – eCommerce Card on File`
* **Active Debit DPANS** – this is the total number of cards that made at least one successful spend.

<br />

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
    <span style={{ fontWeight: 800, marginRight: "6px" }}></span>
    <span>DPAN (Device Primary Account Number) – A token that acts as a surrogate for the customer’s card number and is used to make contactless and e-commerce transactions using an Apple device.</span>
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
        \[CampaignName]\_ApplePay Quarterly Fee Billing Report<br />
        \[Month] YYYY.xls
      </td>

      <td align="center">Quarterly</td>
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
      <td align="center">02:00, day 2 of month produced</td>
      <td align="center">07:00, day 2 of month produced</td>

      <td align="center">
        Quarterly reports are produced as follows:<br /><br />
        <strong>Q1</strong> – (January, February, March) → produced April<br />
        <strong>Q2</strong> – (April, May, June) → produced July<br />
        <strong>Q3</strong> – (July, August, September) → produced October<br />
        <strong>Q4</strong> – (October, November, December) → produced January
      </td>
    </tr>
  </tbody>
</table>

## Report sample

<Image border={false} src="https://files.readme.io/236bf3afcd34df2a9eb997a056af48562258d18c911b93e3cbc261b2aec9eb8a-image.png" />

<NavyBlock />

[CampaignName_ApplePay Quarterly Fee Billing Report Month YYYY.xls](https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_ApplePay-Quarterly-Fee-Billing-Report-Month-YYYY.xls)

<br />
