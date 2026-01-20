---
title: Reports
excerpt: >-
  Explore Paymentology's comprehensive reporting and reconciliation
  capabilities, including various financial and transaction reports.
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  robots: index
---
**Paymentology provides end-to-end reporting and reconciliation capabilities to allow you to track all the financial movements, revenues collected, failed transactions, and more.**

<div
  style={{
    background: '#0F1F3A',
    color: '#FFFFFF',
    padding: '0 16px',
    minHeight: '48px',
    display: 'flex',
    alignItems: 'center',
    gap: '12px',
    fontSize: '14px',
    fontWeight: 500,
    lineHeight: '20px',
  }}
>
  {/* Info icon (SVG, perfectly centered) */}

  <span
    style={{
      width: '20px',
      height: '20px',
      borderRadius: '50%',
      background: '#3B6EDC',
      display: 'inline-flex',
      alignItems: 'center',
      justifyContent: 'center',
      flexShrink: 0,
    }}
    aria-hidden="true"
  >
    <svg width="12" height="12" viewBox="0 0 12 12" xmlns="http://www.w3.org/2000/svg" style={{ display: 'block' }}>
      {/* dot */}

      <circle cx="6" cy="3" r="1" fill="#FFFFFF" />

      {/* stem */}

      <rect x="5.25" y="5" width="1.5" height="5" rx="0.75" fill="#FFFFFF" />
    </svg>
  </span>

  <span style={{ display: 'inline-flex', alignItems: 'center' }}>
    <span style={{ fontWeight: 800, marginRight: '6px' }}>Note:</span>
    <span>You can generate all reports below by sending a HTTP GET Request and downloading the report as a CSV file. These downloadable reports are only available for 60 days.</span>
  </span>
</div>

You can generate the following reports:

* [Mark-off file](https://developer.sprint.paymentology.com/companion-api/reports/mark-off-file)
* [Summary settlement report](https://developer.sprint.paymentology.com/companion-api/reports/summary-settlement-report)
* [Detailed settlement report](https://developer.sprint.paymentology.com/companion-api/reports/detailed-settlement-report)
* [Forex gains report](https://developer.sprint.paymentology.com/companion-api/reports/forex-gains-report)
* [Failed transaction report](https://developer.sprint.paymentology.com/companion-api/reports/failed-transaction-report)
* [Card order report](https://developer.sprint.paymentology.com/companion-api/reports/card-order-report)
* [Unsettled transactions report](https://developer.sprint.paymentology.com/companion-api/reports/unsettled-transactions-report-2/)
* [eCommerce report](https://developer.sprint.paymentology.com/companion-api/reports/ecommerce-report/)
* [Inactive cards report](https://developer.sprint.paymentology.com/companion-api/reports/inactive-cards-report/)
* [Authorisation income report](https://developer.sprint.paymentology.com/companion-api/reports/authorisation-income-report/)
* [Card balance report](https://developer.sprint.paymentology.com/companion-api/reports/card-balance-report/)
* [Daily statement report](https://developer.sprint.paymentology.com/companion-api/reports/daily-statement-report/)

***

## Other Reports

### Apple Pay

For clients using Paymentology’s tokenization services, Paymentology can issue the following reports to assist with Apple Pay reporting requirements:

* [Apple Pay quarterly fee billing report](https://developer.sprint.paymentology.com/companion-api/reports/apple-pay-quarterly-fee-billing-report/)
* [Apple Pay monthly top merchant report](https://developer.sprint.paymentology.com/companion-api/reports/apple-pay-monthly-top-merchant-report/)
* [Apple Pay monthly metric report](https://developer.sprint.paymentology.com/companion-api/reports/apple-pay-monthly-metric-report/)
* [Apple Pay monthly usage frequency report](https://developer.sprint.paymentology.com/companion-api/reports/apple-pay-monthly-usage-frequency-report/)
* [Apple Pay monthly fee billing report](https://developer.sprint.paymentology.com/companion-api/reports/apple-pay-monthly-fee-billing-report/)
* [Apple Pay monthly declines report](https://developer.sprint.paymentology.com/companion-api/reports/apple-pay-monthly-declines-report/)

### Google Pay

For clients using Paymentology’s tokenization services, Paymentology can issue the following report to assist with Google Pay reporting:

* [Google Pay monthly report](https://developer.sprint.paymentology.com/companion-api/reports/google-pay-monthly-report/)

### Emailed Reports

These reports can be sent to clients via email upon request:

* [Linked cards report](https://developer.sprint.paymentology.com/companion-api/reports/linked-cards-report/)
* [Blocked transactions report](https://developer.sprint.paymentology.com/companion-api/reports/blocked-transactions-report/)
* [Daily negative balance report](https://developer.sprint.paymentology.com/companion-api/reports/daily-negative-balance-report/)

### Card Scheme Reports

For clients using Mastercard or Visa, the following reports support quarterly card scheme reporting requirements. These are sent via email and must be requested through your Paymentology Client Executive:

* [QVR (Visa) data report](https://developer.sprint.paymentology.com/companion-api/reports/qvr-data-report/)
* [QMR (Mastercard) data report](https://developer.sprint.paymentology.com/companion-api/reports/qmr-data-report/)
* [VAU (Visa) transaction report](https://developer.sprint.paymentology.com/companion-api/reports/vau-transaction-report/)

### Reports Accessible via URL

These reports can be downloaded directly from a URL:

* [Daily sales and redemption report](https://developer.sprint.paymentology.com/companion-api/reports/daily-sales-and-redemption-report/)

<br />