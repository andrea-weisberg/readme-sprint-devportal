---
title: Reconciliation
deprecated: false
hidden: false
metadata:
  robots: index
---
**Reconciliation is the process of matching transactions reported by Paymentology to the transactions recorded on the wallet platform to ensure that the amount settled by the card scheme is accurate.**

<br />

<div
  style={{
    background: "#E9F6F1",
    padding: "56px",
    position: "relative",
    minHeight: "420px",
  }}
>
  {/* Icon */}

  <div style={{ position: "absolute", top: "48px", left: "56px" }} aria-hidden="true">
    <div
      style={{
        width: "120px",
        height: "120px",
        background: "#97E0CD",
        borderTopLeftRadius: "18px",
        borderTopRightRadius: "18px",
        borderBottomLeftRadius: "18px",
        borderBottomRightRadius: "48px",
        display: "grid",
        placeItems: "center",
      }}
    >
      <svg width="86" height="86" viewBox="0 0 86 86" fill="none" xmlns="http://www.w3.org/2000/svg" style={{ display: "block" }}>
        {/* check badge */}

        <rect x="54" y="10" width="22" height="22" rx="6" fill="#58C7AE" />

        <path d="M59.5 21.5l4.2 4.3 8.8-9.3" stroke="#FFFFFF" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round" />

        {/* small card */}

        <rect x="18" y="36" width="28" height="20" rx="4" fill="#7FE3CC" opacity="0.7" />

        <rect x="21" y="39" width="12" height="4" rx="2" fill="#E6FFFA" opacity="0.9" />

        {/* arrow */}

        <path d="M42 60 L56 46" stroke="#0B1320" strokeWidth="3" strokeLinecap="round" />

        <path d="M56 46 L56 54" stroke="#0B1320" strokeWidth="3" strokeLinecap="round" />

        <path d="M56 46 L48 46" stroke="#0B1320" strokeWidth="3" strokeLinecap="round" />

        {/* simplified hand */}

        <path d="M20 70c2-6 6-10 12-12 3-1 6 0 7 2 1 2-1 4-4 5l-5 2" stroke="#0B1320" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round" />

        <path d="M20 70c3 2 8 4 14 4" stroke="#0B1320" strokeWidth="3" strokeLinecap="round" />
      </svg>
    </div>
  </div>

  {/* Text */}

  <div style={{ paddingTop: "180px" }}>
    <h2 style={{ margin: "0 0 12px 0", fontSize: "44px", lineHeight: 1.1, fontWeight: 800 }}>
      Authorizations
    </h2>

    <p style={{ margin: "0 0 38px 0", fontSize: "28px", lineHeight: 1.25, fontWeight: 800 }}>
      Paymentology provides a daily mark-off file
    </p>

    <p style={{ margin: "0 0 22px 0", fontSize: "28px", lineHeight: 1.25, fontWeight: 800 }}>
      The mark-off file shows successful transactions that Paymentology has processed on behalf of the Issuer
    </p>

    <p style={{ margin: 0, fontSize: "28px", lineHeight: 1.25, fontWeight: 800 }}>
      The Issuer/client will compare Paymentology's transactions to the wallet platform
    </p>
  </div>
</div>

# Authorization reconciliation process

**What is Authorization?**  
Authorization is the process of checking the available funds on a card in order to reserve funds when the card is used for a purchase.

## Authorization reports

The report linked below assists client’s with authorization reconciliation.

* [Mark-off file](https://developer.sprint.paymentology.com/companion-api/reports/mark-off-file/)

# Settlements

**What is a settlement?**  
A settlement is when funds are deducted from the Issuer/client’s bank account and deposited in to a merchants bank account to settle a card transaction.

**Dual-message-settlement-process.png IMAGE GOES HERE.**

## Settlement process:

**step 1:** 1 – 7 days after the successful authorization, merchants will request payments from the card association  
**step 2:** The card association debits the Issuing bank (the pool account that the card belongs to) and moves the funds to the Acquiring bank of the Merchant. The Acquiring bank then moves the funds to the merchants account.  
**step 3:** The card scheme sends Paymentology clearing files, containing each individual settled transaction. New forex conversion rates will be calculated for all international transactions and interchange is calculated and applied.  
Different card schemes have different clearing cycles depending on the region/country and there can be up to 8 clearing cycles per day. All clearing cycles are included in our settlement reports. **NOTE:** Visa’s settlements are online.  
**step 4:** Paymentology will compare all settled transactions to previously authorized transactions and match these together. Paymentology creates a summary settlement report and calculates the net settlement amount that will be debited by the card association. Forex currency gains are calculated based on settlement amounts.  
**step 5:** The client will compare Paymentology’s settlement amounts to the amount debited by the card scheme and the amount that is debited from their bank accounts.

## Settlement reports

The reports linked below assist client’s with settlement reconciliation.

* [summary settlement report](https://developer.sprint.paymentology.com/companion-api/reports/summary-settlement-report/)
* [Detailed settlement report](https://developer.sprint.paymentology.com/companion-api/reports/detailed-settlement-report/)

# Revenue

**What is Revenue?**  
Revenue is the income earned from Forex gains and interchange.

## Forex Fluctuation

**Forex-fluctuation-v2.png IMAGE GOES HERE.**

## **Revenue reports**

The report linked below assists client’s with revenue reconciliation and reporting:

* [Forex gains report](https://developer.sprint.paymentology.com/companion-api/reports/forex-gains-report/)

# Adjustment Handling

## Deduct Adjustments

* Negative forex fluctuation -> Issuer/client to absorb
* Settlement with no authorizations -> Issuer/client to debit customer’s account

## Load Adjustments

* Positive forex fluctuation -> Issuer/client to absorb
* Refunds -> Issuer/client credit customer’s account

# Fraud

**What is Fraud?**  
Fraud is a false or illegal transaction which results in a loss of funds. Paymentology provides the following Risk Management features:

* Transaction Limits – Paymentology allows you to implement transaction limits per card or program. If the ceiling is reached, no further transactions are permitted.
* Usage – Paymentology allows you to specify the payment methods that the card can be used with. If there is an attempted use of the card for an unspecified payment method, the transaction will fail and send a fraud alert.
* Additional settings – Paymentology allows you to implement additional settings to reinforce the security of cards and help with fraud prevention.
* Notifications – Paymentology lets you configure real-time notifications that keep customers informed about the state of their cards.
* Checks and controls – Paymentology allows you to implement a variety of Issuance checks, Spend controls and Authorization checks

Read more about Fraud and Risk [here](https://developer.sprint.paymentology.com/get-started/fraud/)

## Dispute Handling

**What is a Dispute?**  
A dispute is a transaction that a cardholder/customer does not agree with and therefore requests that part of, or the entire transaction be reversed or refunded.

### Types of Disputes:

1. **Reversal** A reversal is essentially a request for a transaction that was not completed and could have failed at a particular step of the transaction process. It is an advisement message to all parties of the transaction and ensures that the card and store of value are put back into their original state if a failed to deduct transaction had been initiated.If you sent a transaction and did not receive a confirmation that the transaction was successful, it could imply that the transaction did not reach the intended destination.
2. **Refund** A refund is when funds are credited back to the customer’s card from a previously debited transaction. A refund is processed when the merchant refunds the customer for returned goods and the funds which were settled to the merchant’s account need to move back to the cardholder’s account.
3. **Chargeback** A chargeback is the return of funds for a deduct transaction that was previously processed from a cardholder’s card balance, due to a successful dispute by the consumer regarding the transaction

Read about Chargeback related Dispute handling [here](https://developer.sprint.paymentology.com/companion-api/disputes/)
