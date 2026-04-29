---
title: Reconciliation
deprecated: false
hidden: false
metadata:
  robots: index
---
**Reconciliation is the process of matching transactions reported by Paymentology to the transactions recorded on the wallet platform to ensure that the amount settled by the card scheme is accurate.**

<br />

<div style={{ display: "grid", gap: "32px" }}>
  {[
                  {
                    title: "Authorizations",
                    lines: [
                      "Paymentology provides a daily mark-off file",
                      "The mark-off file shows successful transactions that Paymentology has processed on behalf of the Issuer",
                      "The Issuer/client will compare Paymentology's transactions to the wallet platform",
                    ],
                  },
                  {
                    title: "Settlements",
                    lines: [
                      "Paymentology provides a daily summary settlement report as well as a daily detailed settlement report.",
          						"The Issuer/client will compare the net settlement amount with the amount that the card scheme has debited from the Issuer/client pool account",
                    ],
                  },
                  {
                    title: "Revenue",
                    lines: [
                      "Paymentology provides a daily forex gains report showing all revenue earned by the Issuer/client",
                      "The Issuer/client also has sight of the daily interchange earned from the summary settlement report",
                    ],
                  },
                  {
                    title: "Fraud",
                    lines: [
                      "Paymentology will report on all fraud cases via the card scheme’s online portal",
                    ],
                  },
                ].map((item, idx) => (
                  <div
                    key={idx}
                    style={{
                      background: "#E9F6F1",
                      padding: "28px 32px",
                      position: "relative",
                        minHeight: "200px",
                          display: "flex",
      								alignItems: "center", 
                    }}
                  >
                    {/* Icon */}
                    <div style={{ position: "absolute", top: "20px", left: "32px" }} aria-hidden="true">
                      <div
                        style={{
                          width: "72px",
                          height: "72px",
                          background: "#97E0CD",
                          borderRadius: "14px 14px 14px 32px",
                          display: "grid",
                          placeItems: "center",
                        }}
                      >
                        <svg
                          width="44"
                          height="44"
                          viewBox="0 0 86 86"
                          fill="none"
                          xmlns="http://www.w3.org/2000/svg"
                        >
                          <rect x="54" y="10" width="22" height="22" rx="6" fill="#58C7AE" />
                          <path
                            d="M59.5 21.5l4.2 4.3 8.8-9.3"
                            stroke="#FFFFFF"
                            strokeWidth="3"
                            strokeLinecap="round"
                            strokeLinejoin="round"
                          />
                          <rect x="18" y="36" width="28" height="20" rx="4" fill="#7FE3CC" />
                          <path d="M42 60 L56 46" stroke="#0B1320" strokeWidth="3" strokeLinecap="round" />
                        </svg>
                      </div>
                    </div>

                    {/* Content */}
                    <div style={{ paddingLeft: "120px" }}>
                      <h3 style={{ margin: "0 0 12px 0", fontSize: "22px", fontWeight: 700 }}>
                        {item.title}
                      </h3>

                      {item.lines.map((line, i) => (
                        <p
                          key={i}
                          style={{
                            margin: "0 0 8px 0",
                            fontSize: "16px",
                            lineHeight: 1.4,
                            fontWeight: 500,
                          }}
                        >
                          {line}
                        </p>
                      ))}
                    </div>
                  </div>
                ))}
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
  }}
>
  {[
        {
          title: "Paymentology",
          body: (
            <>
              <strong>Paymentology will</strong> daily generate a mark-off file showing all
              transactions successfully processed on behalf of the Issuer/client.
            </>
          ),
        },
        {
          title: "Issuer/Client",
          body: (
            <>
              <strong>The Issuer/client will</strong> daily generate a similar mark-off file.
              <br /><br />
              The Issuer/client will compare Paymentology&apos;s transaction list to their list.
            </>
          ),
        },
        {
          title: "Support",
          body: (
            <>
              <strong>If there are any discrepancies</strong>, the Issuer/client will raise these
              with the Paymentology support team by logging a ticket via your Zendesk Portal,
              selecting the <strong>Report a Service Incident</strong> form, then choosing
              <strong> Reporting</strong> and <strong> Discrepancy</strong>.
            </>
          ),
        },
      ].map((card, idx) => (
        <div
          key={idx}
          style={{
            background: "#E9F6F1",
            padding: "32px",
            minHeight: "440px",
            display: "flex",
            flexDirection: "column",
          }}
        >
          {/* Icon placeholder */}
          <div
            style={{
              width: "104px",
              height: "104px",
              background: "#97E0CD",
              borderRadius: "20px 20px 20px 52px",
              marginBottom: "88px",
            }}
            aria-hidden="true"
          />

          {/* Title */}
          <div
            style={{
              fontSize: "18px",
              fontWeight: 600,
              marginBottom: "10px",
              color: "#0B1320",
            }}
          >
            {card.title}
          </div>

          {/* Body */}
          <div
            style={{
              fontSize: "14px",
              lineHeight: 1.55,
              fontWeight: 500,
              color: "#0B1320",
            }}
          >
            {card.body}
          </div>
        </div>
      ))}
</div>

<style>
  {`
      @media (max-width: 1100px) {
        div[style*="grid-template-columns: repeat(3"] {
          grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
        }
      }
      @media (max-width: 700px) {
        div[style*="grid-template-columns"] {
          grid-template-columns: 1fr !important;
        }
      }
    `}
</style>

<br />

***

# Authorization reports

The report linked below assists client’s with authorization reconciliation.

* [Mark-off file](https://developer.sprint.paymentology.com/companion-api/reports/mark-off-file/)

***

# Settlements

**What is a settlement?**  
A settlement is when funds are deducted from the Issuer/client’s bank account and deposited in to a merchants bank account to settle a card transaction.

<Image border={false} src="https://files.readme.io/583c37b6e0094362b0cdaf01992f8da33abf67db8c5f2eae9d948d8b8ac9dc6e-image.png" />

<br />

## Settlement process:

**Step 1:** 1 – 7 days after the successful authorization, merchants will request payments from the card association

**Step 2:** The card association debits the Issuing bank (the pool account that the card belongs to) and moves the funds to the Acquiring bank of the Merchant. The Acquiring bank then moves the funds to the merchants account.

Step 3:** The card scheme sends Paymentology clearing files, containing each individual settled transaction. New forex conversion rates will be calculated for all international transactions and interchange is calculated and applied.

Different card schemes have different clearing cycles depending on the region/country and there can be up to 8 clearing cycles per day. All clearing cycles are included in our settlement reports. **NOTE: **Visa’s settlements are online.

**Step 4:** Paymentology will compare all settled transactions to previously authorized transactions and match these together. Paymentology creates a summary settlement report and calculates the net settlement amount that will be debited by the card association. Forex currency gains are calculated based on settlement amounts.

**Step 5:** The client will compare Paymentology’s settlement amounts to the amount debited by the card scheme and the amount that is debited from their bank accounts.

## Settlement reports

The reports linked below assist client’s with settlement reconciliation.

* [summary settlement report](reports/summary-settlement-report)
* [Detailed settlement report](https://developer.sprint.paymentology.com/companion-api/reports/detailed-settlement-report/)

***

# Revenue

**What is Revenue?**  
Revenue is the income earned from Forex gains and interchange.

## Forex Fluctuation

<Image border={false} src="https://files.readme.io/e28efad1710f0f3865f3800ccf1cff6c90dae39267f847545a2b024d1e6a4379-image.png" />

<br />

## **Revenue reports**

The report linked below assists client’s with revenue reconciliation and reporting:

* [Forex gains report](reports/forex-gains-report)

# Adjustment Handling

## Deduct Adjustments

* Negative forex fluctuation -> Issuer/client to absorb
* Settlement with no authorizations -> Issuer/client to debit customer’s account

## Load Adjustments

* Positive forex fluctuation -> Issuer/client to absorb
* Refunds -> Issuer/client credit customer’s account

**NOTE:** All adjustments are recorded in the mark-off file

***

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
