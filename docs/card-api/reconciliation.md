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

<br />
