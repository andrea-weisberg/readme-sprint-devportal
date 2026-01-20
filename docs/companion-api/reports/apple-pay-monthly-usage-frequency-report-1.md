---
title: Apple Pay monthly usage frequency report
deprecated: false
hidden: false
metadata:
  robots: index
---
For clients using Paymentology’s tokenization, Paymentology can issue monthly reports to assist in compiling their Apple report through the Apple Partner Connect platform.

This report refers to the number of times a specific account is used to make a transaction in a given month. This includes any type of Apple Pay transaction i.e. POS or eCommerce.

The report includes the following details:

* **Month** – the month the report data is based on.
* **Not used in current month** – the total count of available DPANs that did not make any successful transaction in the given month.
* **Once(1) in current month** – the total count of available DPANs that have successfully transacted exactly one time in the given month.
* **Twice(2) in current month** – the total count of available DPANs that have successfully transacted exactly two times in the given month.
* **3 times in current month** – the total count of available DPANs that have successfully transacted exactly three times in the given month.
* **4 times in current month** – the total count of available DPANs that have successfully transacted exactly four times in the given month.
* **5 times in current month** – the total count of available DPANs that have successfully transacted exactly five times in the given month.
* **6 times in current month** – the total count of available DPANs that have successfully transacted exactly six times in the given month.
* **7 times in current month** – the total count of available DPANs that have successfully transacted exactly seven times in the given month.
* **8 times in current month** – the total count of available DPANs that have successfully transacted exactly eight times in the given month.
* **9 times in current month** – the total count of available DPANs that have successfully transacted exactly nine times in the given month.
* **>= 10 times in current month** – the total count of available DPANs that have successfully transacted at least ten times in the given month.
* **Total** – the total count of available DPANs in the given month.
* **Active DPAN rate** – the percentage of DPANs that have transacted in the given month out of the total available DPANs. An available DPAN is defined as a token that is provisioned and available for transacting, i.e. it is not temporarily blocked.

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
    <span style={{ fontWeight: 800, marginRight: "6px" }} />

    <span>DPAN (Device Primary Account Number) – A token that acts as a surrogate for the customer’s card number and is used to make contactless and e-commerce transactions using an Apple device.</span>
  </span>
</div>

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
    <span style={{ fontWeight: 800, marginRight: "6px" }} />

    <span>Only settled transactions are counted.</span>
  </span>
</div>

***

# Report Format

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
        \[CampaignName]\_ApplePay Monthly Frequency Report<br />
        \[Month] YYYY.xls
      </td>

      <td align="center">Monthly</td>
      <td align="center">Via email</td>
    </tr>
  </tbody>
</table>

# Report time frame

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

# Report Sample

<Image border={false} src="https://files.readme.io/60a1a7955b6db5769c33aed9edd580bb24feebd5655b07e45f77fed464306f26-image.png" />

<NavyBlock />

CampaignName_ApplePay Monthly Frequency Report Month YYYY.xls

<br />
