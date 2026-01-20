---
title: Apple Pay monthly metric report
deprecated: false
hidden: false
metadata:
  robots: index
---
<p>
  For clients using Paymentology’s tokenization, Paymentology can issue monthly
  reports to clients to assist in compiling their Apple report through the Apple
  Partner Connect platform.
</p>

<p>
  The monthly metric report provides clients with a breakdown of POS (Point of
  Sale), remote (in-App, Apple Pay on the web and eCommerce) and COF (Credential
  on File) Apple Pay spends for the specified month.
</p>

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

    <span>All amounts reported are in the cardholder billing currency.</span>
  </span>
</div>

<p>The report includes the following details:</p>

<ul>
  <li>
    <strong>Reporting Month</strong> – the month the report data is based on.
  </li>

  <li>
    <strong>Monthly DPAN transaction count</strong> – total number of settled
    DPAN transactions made using Apple Pay for the given month.
  </li>

  <li>
    <strong>Monthly DPAN spend</strong> – total value of settled DPAN transactions
    made using Apple Pay for the given month.
  </li>

  <li>
    <strong>
      % of POS DPAN transactions out of the monthly processed DPAN transactions
    </strong>

    – percentage split of <strong>Monthly DPAN transaction count</strong> that
    were POS (Point of Sale) type spends.
  </li>

  <li>
    <strong>
      % of Remote DPAN transactions out of the monthly processed DPAN transactions
    </strong>

    – percentage split of <strong>Monthly DPAN transaction count</strong> that
    were remote type spends (in-App, Apple Pay on the web and eCommerce).
  </li>

  <li>
    <strong>
      % of COF DPAN transactions out of the monthly processed DPAN transactions
    </strong>

    – percentage split of <strong>Monthly DPAN transaction count</strong> that
    were COF (Credential on File) type spends.
  </li>

  <li>
    <strong>
      % of POS DPAN spend amount out of the monthly processed DPAN transactions
    </strong>

    – percentage split of <strong>Monthly DPAN spend</strong> value that were POS
    (Point of Sale) type spends.
  </li>

  <li>
    <strong>
      % of Remote DPAN spend amount out of the monthly processed DPAN transactions
    </strong>

    – percentage split of <strong>Monthly DPAN spend</strong> value that were
    remote type spends (in-App, Apple Pay on the web and eCommerce).
  </li>

  <li>
    <strong>
      % of COF DPAN spend amount out of the monthly processed DPAN transactions
    </strong>

    – percentage split of <strong>Monthly DPAN spend</strong> value that were COF
    (Credential on File) type spends.
  </li>

  <li>
    <strong>Total Available DPANs</strong> – tokens available for use on Apple Pay
    as of the end of the reporting month. This includes DPANs successfully
    provisioned since launch, excluding inactive, pending, suspended, and deleted
    tokens.
  </li>

  <li>
    <strong>Monthly Active DPANs</strong> – count of DPANs that have transacted at
    least once in the given month.
  </li>
</ul>

<h2>Report format</h2>

<h2>Report time frame</h2>

<h2>Report sample</h2>

<p>
  <strong>
    CampaignName\_ApplePay-Monthly-Metric-Report-Month-YYYY-\_-002.png
  </strong>

  <br />

  IMAGE GOES HERE
</p>

<p>
  <a href="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_ApplePay-Monthly-Metric-Report-Month-YYYY.xls">
    CampaignName\_ApplePay Monthly Metric Report Month YYYY.xls
  </a>
</p>
