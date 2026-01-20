---
title: Reconciliation
deprecated: false
hidden: false
metadata:
  robots: index
---
# Settlement and Reconciliation

Reconciliation is the process of matching transactions reported by Paymentology to the transactions recorded on the client platform to ensure that the amount settled by the card scheme is accurate.

<br />

<div
  style={{
    display: "grid",
    gap: "32px",
    marginTop: "24px",
  }}
>
  {/* Authorizations */}

  <div
    style={{
      background: "#E9F6F1",
      padding: "24px",
    }}
  >
    <div
      style={{
        width: "64px",
        height: "64px",
        background: "#97E0CD",
        borderRadius: "14px 14px 14px 32px",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        marginBottom: "20px",
      }}
      aria-hidden="true"
    >
      ✓
    </div>

    <h3 style={{ margin: "0 0 8px 0", fontSize: "18px" }}>Authorizations</h3>

    <p style={{ margin: "0 0 12px 0", fontSize: "14px" }}>
      <strong>Paymentology provides a daily mark-off file</strong>
    </p>

    <p style={{ margin: 0, fontSize: "14px", lineHeight: "1.5" }}>
      The mark-off file shows successful transactions that Paymentology has
      processed on behalf of the Issuer.
    </p>
  </div>

  {/* Settlements */}

  <div
    style={{
      background: "#E9F6F1",
      padding: "24px",
    }}
  >
    <div
      style={{
        width: "64px",
        height: "64px",
        background: "#97E0CD",
        borderRadius: "14px 14px 14px 32px",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        marginBottom: "20px",
      }}
      aria-hidden="true"
    >
      $
    </div>

    <h3 style={{ margin: "0 0 8px 0", fontSize: "18px" }}>Settlements</h3>

    <p style={{ margin: "0 0 12px 0", fontSize: "14px" }}>
      <strong>
        Paymentology provides a daily summary and detailed settlement report
      </strong>
    </p>

    <p style={{ margin: 0, fontSize: "14px", lineHeight: "1.5" }}>
      The Issuer/client will compare the net settlement amount with the amount
      debited by the card scheme from the pool account.
    </p>
  </div>

  {/* Revenue */}

  <div
    style={{
      background: "#E9F6F1",
      padding: "24px",
    }}
  >
    <div
      style={{
        width: "64px",
        height: "64px",
        background: "#97E0CD",
        borderRadius: "14px 14px 14px 32px",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        marginBottom: "20px",
      }}
      aria-hidden="true"
    >
      $
    </div>

    <h3 style={{ margin: "0 0 8px 0", fontSize: "18px" }}>Revenue</h3>

    <p style={{ margin: "0 0 12px 0", fontSize: "14px" }}>
      <strong>
        Paymentology provides a daily forex gains report
      </strong>
    </p>

    <p style={{ margin: 0, fontSize: "14px", lineHeight: "1.5" }}>
      The Issuer/client also has sight of the daily interchange earned from the
      summary settlement report.
    </p>
  </div>

  {/* Fraud */}

  <div
    style={{
      background: "#E9F6F1",
      padding: "24px",
    }}
  >
    <div
      style={{
        width: "64px",
        height: "64px",
        background: "#97E0CD",
        borderRadius: "14px 14px 14px 32px",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        marginBottom: "20px",
      }}
      aria-hidden="true"
    >
      ⚠
    </div>

    <h3 style={{ margin: "0 0 8px 0", fontSize: "18px" }}>Fraud</h3>

    <p style={{ margin: 0, fontSize: "14px", lineHeight: "1.5" }}>
      <strong>Paymentology will report on all fraud cases</strong> via the card
      scheme’s online portal.
    </p>
  </div>
</div>

***

# Authorization reconciliation process

**What is Authorization?**

Authorization is the process of checking the available funds on a card in order to reserve funds when the card is used for a purchase.

<br />

<div
  style={{
    display: "grid",
    gridTemplateColumns: "repeat(3, minmax(0, 1fr))",
    gap: "24px",
    marginTop: "24px",
  }}
>
  {/* Paymentology */}

  <div
    style={{
      background: "#E9F6F1",
      padding: "28px",
    }}
  >
    <div
      style={{
        width: "64px",
        height: "64px",
        background: "#97E0CD",
        borderRadius: "14px 14px 14px 32px",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        marginBottom: "24px",
      }}
      aria-hidden="true"
    >
      {/* Chat icon */}

      <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#0B1320" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <path d="M21 11.5a8.5 8.5 0 0 1-8.5 8.5H4l2.5-2.5A8.5 8.5 0 1 1 21 11.5z" />

        <rect x="8" y="9" width="8" height="4" />
      </svg>
    </div>

    <h3 style={{ margin: "0 0 10px 0", fontSize: "18px" }}>
      Paymentology
    </h3>

    <p style={{ margin: "0 0 12px 0", fontSize: "14px", fontWeight: 600 }}>
      Paymentology will daily generate a mark-off file
    </p>

    <p style={{ margin: 0, fontSize: "14px", lineHeight: "1.5" }}>
      Showing all transactions successfully processed on behalf of the
      Issuer/client.
    </p>
  </div>

  {/* Issuer / Client */}

  <div
    style={{
      background: "#E9F6F1",
      padding: "28px",
    }}
  >
    <div
      style={{
        width: "64px",
        height: "64px",
        background: "#97E0CD",
        borderRadius: "14px 14px 14px 32px",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        marginBottom: "24px",
      }}
      aria-hidden="true"
    >
      {/* Laptop + user icon */}

      <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#0B1320" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <rect x="3" y="5" width="18" height="12" rx="2" />

        <line x1="3" y1="17" x2="21" y2="17" />

        <circle cx="18" cy="8" r="2" />
      </svg>
    </div>

    <h3 style={{ margin: "0 0 10px 0", fontSize: "18px" }}>
      Issuer/Client
    </h3>

    <p style={{ margin: "0 0 12px 0", fontSize: "14px", fontWeight: 600 }}>
      The Issuer/client will daily generate a similar mark-off file
    </p>

    <p style={{ margin: 0, fontSize: "14px", lineHeight: "1.5" }}>
      The Issuer/client will compare Paymentology's transaction list to
      their list.
    </p>
  </div>

  {/* Support */}

  <div
    style={{
      background: "#E9F6F1",
      padding: "28px",
    }}
  >
    <div
      style={{
        width: "64px",
        height: "64px",
        background: "#97E0CD",
        borderRadius: "14px 14px 14px 32px",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        marginBottom: "24px",
      }}
      aria-hidden="true"
    >
      {/* Headset icon */}

      <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#0B1320" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <path d="M4 12a8 8 0 0 1 16 0" />

        <path d="M4 12v4a2 2 0 0 0 2 2" />

        <path d="M20 12v4a2 2 0 0 1-2 2" />

        <circle cx="4" cy="14" r="2" />

        <circle cx="20" cy="14" r="2" />
      </svg>
    </div>

    <h3 style={{ margin: "0 0 10px 0", fontSize: "18px" }}>
      Support
    </h3>

    <p style={{ margin: "0 0 12px 0", fontSize: "14px", fontWeight: 600 }}>
      If there are any discrepancies, the Issuer/client will raise these with the
      Paymentology support team.
    </p>

    <p style={{ margin: 0, fontSize: "14px", lineHeight: "1.5" }}>
      Log a ticket via your Zendesk Portal, select the <strong>Report a Service
      Incident</strong> form, then choose <strong>Reporting</strong> and{" "}
      <strong>Discrepancy</strong> under Request Type.
    </p>
  </div>
</div>

<style>
  {`
    @media (max-width: 900px) {
      div[style*="grid-template-columns: repeat(3"] {
        grid-template-columns: 1fr !important;
      }
    }
  `}
</style>

<br />

## Authorization reports

The report linked below assists client’s with authorization reconciliation.

[Mark-off file]()

***

# Settlements

**What is a settlement?**

A settlement is when funds are deducted from the Issuer/client’s bank account and deposited in to a merchants bank account to settle a card transaction.

<Image border={false} src="https://files.readme.io/86f4b9ba3416a6c04b3504be8b24435bd173c20e3babf407dc73924fc0cb1cd9-image.png" />

## Settlement process:

**Step 1: **1 – 7 days after the successful authorization, merchants will request payments from the card association

**Step 2:** The card association debits the Issuing bank (the pool account that the card belongs to) and moves the funds to the Acquiring bank of the Merchant. The Acquiring bank then moves the funds to the merchants account.

**Step 3:** The card scheme sends Paymentology clearing files, containing each individual settled transaction. New forex conversion rates will be calculated for all international transactions and interchange is calculated and applied.

Different card schemes have different clearing cycles depending on the region/country and there can be up to 8 clearing cycles per day. All clearing cycles are included in our settlement reports.

**Step 4:** Paymentology will compare all settled transactions to previously authorized transactions and match these together. Paymentology creates a summary settlement report and calculates the net settlement amount that will be debited by the card association. Forex currency gains are calculated based on settlement amounts.

**Step 5:** The client will compare Paymentology’s settlement amounts to the amount debited by the card scheme and the amount that is debited from their bank accounts.

### **Settlement reports**

The reports linked below assist client’s with settlement reconciliation.

[Summary settlement report]()
[Detailed settlement report]()

***

# Revenue

**What is Revenue?**

Revenue is the income earned from Forex gains and interchange.

<Image border={false} src="https://files.readme.io/8318dc663b14b1dce0f16bc1dea935553e512fd70324ef749ed426a9dcb3c0db-image.png" />

<br />

### **Revenue reports**

The report linked below assists client’s with revenue reconciliation and reporting:

* [Forex gains report]()

***

# Adjustment Handling

## Deduct Adjustments

* Negative forex fluctuation -> Issuer/client to absorb
* Settlement with no authorizations -> Issuer/client to debit customer’s account

## Load Adjustments

* Positive forex fluctuation -> Issuer/client to absorb
* Refunds -> Issuer/client credit customer’s account

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
    <span style={{ fontWeight: 800, marginRight: "6px" }}>Note:</span>
    <span>All adjustments are recorded in the mark-off file</span>
  </span>
</div>
