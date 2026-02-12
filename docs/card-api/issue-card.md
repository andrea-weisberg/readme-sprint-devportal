---
title: Issue cards
deprecated: false
hidden: false
metadata:
  robots: index
---
# How to issue cards

## With the Card API you can offer your customers two types of cards:

<div
  style={{
    display: "grid",
    gridTemplateColumns: "repeat(2, minmax(0, 1fr))",
    gap: "24px",
    marginTop: "24px",
  }}
>
  {/* Virtual card */}

  <div
    style={{
      background: "#E9F6F1",
      padding: "28px",
      minHeight: "200px",
    }}
  >
    {/* Icon */}

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
      <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#0B1320" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <rect x="6" y="2" width="12" height="20" rx="2" />

        <rect x="8" y="7" width="8" height="6" />
      </svg>
    </div>

    <h3 style={{ margin: "0 0 6px 0", fontSize: "18px" }}>Virtual card</h3>

    <p style={{ margin: 0, fontSize: "14px", lineHeight: "1.5" }}>
      A digital card without any physical components
    </p>
  </div>

  {/* Physical card */}

  <div
    style={{
      background: "#E9F6F1",
      padding: "28px",
      minHeight: "200px",
    }}
  >
    {/* Icon */}

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
      <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#0B1320" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <rect x="2" y="5" width="20" height="14" rx="2" />

        <line x1="2" y1="10" x2="22" y2="10" />

        <circle cx="18" cy="15" r="1.5" />
      </svg>
    </div>

    <h3 style={{ margin: "0 0 6px 0", fontSize: "18px" }}>Physical card</h3>

    <p style={{ margin: 0, fontSize: "14px", lineHeight: "1.5" }}>
      The traditional plastic payment card
    </p>
  </div>
</div>

<style>
  {`
                  @media (max-width: 900px) {
                    div[style*="grid-template-columns: repeat(2"] {
                      grid-template-columns: 1fr !important;
                    }
                  }
                `}
</style>

<Image border={false} src="https://files.readme.io/3b362893802c4f7f54194e744a4d8ce483d44262612f9059104a8ea6d2bec7eb-image.png" />

***

# 1. Issuing a virtual card

You can use the Card API to create a Virtual Card Number (VCN), which you can link to the unique customer reference number.

The VCN will then act as your customer’s identifier, which is useful if you want to manage or fund the card at a later stage. This means that you may not need to store the PAN number (Permanent Account Number) at all.

Once the API receives the request, it will create a 16-digit PAN number, CVV (Card Verification value), and an expiry date — which are the constituents of the virtual card. You can then forward this information to your customer.

{/* PAN info */}

<div
  style={{
    background: "#0F1F3A",
    color: "#FFFFFF",
    padding: "20px 24px",
    display: "flex",
    alignItems: "center",
    gap: "16px",
    marginBottom: "24px",
  }}
>
  {/* Icon */}

  <div
    style={{
      width: "56px",
      height: "56px",
      borderRadius: "8px",
      background: "#3558B8",
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      flexShrink: 0,
    }}
    aria-hidden="true"
  >
    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <rect x="5" y="3" width="14" height="18" rx="2" />

      <line x1="8" y1="7" x2="16" y2="7" />

      <line x1="8" y1="11" x2="16" y2="11" />

      <line x1="8" y1="15" x2="14" y2="15" />
    </svg>
  </div>

  {/* Text */}

  <p
    style={{
      margin: 0,
      fontSize: "15px",
      lineHeight: "1.6",
      fontWeight: 500,
    }}
  >
    <strong>PAN number</strong> is a unique alphanumeric number (containing both
    alphabetical and numerical characters) used for identification purposes.
  </p>
</div>

{/* CVV info */}

<div
  style={{
    background: "#0F1F3A",
    color: "#FFFFFF",
    padding: "20px 24px",
    display: "flex",
    alignItems: "center",
    gap: "16px",
  }}
>
  {/* Icon */}

  <div
    style={{
      width: "56px",
      height: "56px",
      borderRadius: "8px",
      background: "#3558B8",
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      flexShrink: 0,
    }}
    aria-hidden="true"
  >
    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <rect x="5" y="3" width="14" height="18" rx="2" />

      <line x1="8" y1="7" x2="16" y2="7" />

      <line x1="8" y1="11" x2="16" y2="11" />

      <line x1="8" y1="15" x2="14" y2="15" />
    </svg>
  </div>

  {/* Text */}

  <p
    style={{
      margin: 0,
      fontSize: "15px",
      lineHeight: "1.6",
      fontWeight: 500,
    }}
  >
    <strong>CVV</strong> is a static number similar to the separately grouped
    numbers, usually three digits, found at the back of most physical debit and
    credit cards.
  </p>
</div>

After the VCN has been linked to the customer’s store of value, they can instantly start transacting on any e-commerce site or application that accepts the chosen card association.

You can also create and issue multiple virtual cards and label them differently to allow for easier management and identification.

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

    <span>You’ll need to make a call to the ​CreateVirtualCard method​​ to create a VCN.</span>
  </span>
</div>

***

# 2. Issuing a physical card

You can create and issue a physical card and send a request to Paymentology to link it to a unique customer reference number.

You can decide to have one card linked per customer or multiple cards linked to a single customer.

Once the card is linked, it is now ready to be funded and used as per the predefined use cases, like making ATM withdrawals, local and international online payments, point of sale transactions, or closed-loop network transactions.

There are two options for issuing physical cards: Issue on-site and link immediately or issue with courier and link later

**Option 1: Issue on-site and link immediately**

You can use this option if you want the physical cards to be linked immediately, when they are bulk produced and stored on your end.

​You could have a batch of cards at the stores, branches, or agent facilities. Then, if someone requests a card, you can decide whether to apply a fee for this purchase.

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

    <span>After issuing the card, you’ll need to send a request to Paymentology, using the ​LinkCard method​​, for the physical card to be linked to a unique customer reference number.</span>
  </span>
</div>

<br />

**Option 2: Issue with courier and link later**

You can use this option if you want to order physical cards through your interface.

For example, if you want to use a courier delivery process or personalize a cardholder’s name on the card, then this option could be for you.

Note: Since the card manufacturer may take a few days before completing the order, using this option does not allow the physical cards to be issued instantly.

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

    <span>For Option 2, you’ll need to make a call to the OrderCard method, which allows you to use your interface to enter the cardholder’s details, address, and their unique reference number.</span>
  </span>
</div>

Making this call will lead to the following:

* A PAN number file will be created and sent to the card manufacturer automatically.
* The card manufacturer will create the physical card and deliver it to the cardholder.
* The cardholder will need to activate and link the card using the ActivateCard and LinkCard API method.

<div
  style={{
    background: "#0F1F3A",
    color: "#FFFFFF",
    padding: "24px 28px",
    fontSize: "15px",
    lineHeight: "1.6",
  }}
>
  <p style={{ margin: "0 0 16px 0", fontWeight: 700 }}>
    Note:
  </p>

  <p style={{ margin: "0 0 16px 0" }}>
    <strong>For virtual cards:</strong> Multiple cards can be linked to one
    reference.
  </p>

  <p style={{ margin: "0 0 16px 0" }}>
    <strong>For physical cards:</strong> Only one reference can be linked to a
    card.
  </p>

  <p style={{ margin: 0, fontWeight: 600 }}>
    A cardholder can have a virtual and a physical card linked to the same
    reference.
  </p>
</div>

<br />
