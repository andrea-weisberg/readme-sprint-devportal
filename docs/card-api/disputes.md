---
title: Disputes
deprecated: false
hidden: false
metadata:
  robots: index
---
# What is a Dispute?

A dispute is a transaction that a cardholder/customer does not agree with and therefore requests that part of, or the entire transaction be reversed or refunded.

## Types of Disputes:

1. **Reversal –** A reversal is essentially a request for a transaction that was not completed and could have failed at a particular step of the transaction process. It is an advisement message to all parties of the transaction and ensures that the card and store of value are put back into their original state if a failed to deduct transaction had been initiated. If you sent a transaction and did not receive a confirmation that the transaction was successful, it could imply that the transaction did not reach the intended destination.

2. **Refund** – A refund is when funds are credited back to the customer’s card from a previously debited transaction. A refund is processed when the merchant refunds the customer for returned goods and the funds which were settled to the merchant’s account need to move back to the cardholder’s account.

3. **Chargeback –** A chargeback is the return of funds for a deduct transaction that was previously processed from a cardholder’s card balance, due to a successful dispute by the consumer regarding the transaction.

***

# How Disputes Work

## What is a Chargeback?

Once a dispute is raised, card issuers (like Paymentology) are able to submit a chargeback using a specific set of reason codes via the card scheme (Mastercard/Visa). There are a specific set of rules and timeframes set out by the card scheme that need to be followed in order to submit a chargeback.

Chargebacks can only be submitted if the transaction has settled i.e. funds have moved from the Issuer’s bank account to the merchant’s bank account for the transaction.

## What is a Second Presentment?

A second presentment (sometimes called a re-presentment) is the merchant’s opportunity to disagree with the chargeback request submitted by the Issuer on behalf of the cardholder. After a chargeback request has been submitted, the merchant/acquirer will have 10/35/45 days in which they may submit second presentments (also called pre-arbitration with some card schemes), depending on card scheme rules.

## What is Pre-Arbitration and Arbitration?

Following a receipt of a second presentment (also knows as re-presentment), the cardholder can choose to further dispute the second presentment by submitting a Pre-Arbitration. If the Pre-Arbitration is not successful, the cardholder can further proceed with submitting an Arbitration (the final option in the Dispute cycle) which in most cases will mean that the card scheme will rule in the case, either in favour of the Issuer or Acquirer depending on the merit of the case. There are specific timeframes for these processes which differ between the card schemes.

***

# Dispute Lifecycle

Paymentology manages dispute handling and chargeback processing on behalf of our clients in three ways:

1. Client initiated disputes
2. Batch chargeback submission

## 1. Individual chargeback submission

* Paymentology will provide the client with one of two chargeback dispute forms:
  – General dispute form
  – Fraud dispute form
* The client’s merchant/customer will complete the form and select the appropriate reason
* The client will send this dispute to Paymentology’s Global support team via email – [support@paymentology.com](mailto:support@paymentology.com)
* Based on the information provided, Paymentology will investigate the transaction being disputed
* Paymentology will submit the chargeback using the appropriate chargeback reason code

## 2. Batch chargeback process

* The client can send Paymentology a list of disputes, using a predefined batch chargeback submission template that has been requested to chargeback. The client can define the chargeback reason code. Depending on whether the documentation is required or not, Paymentology will submit these chargebacks on the client’s behalf.
* Paymentology will monitor and track the chargeback throughout the dispute lifecycle of submission, second presentments and arbitration.
* Once the chargeback has been finalized, our Dispute Management Team will notify the client.
* We will credit the card balance.
* We will add the chargeback amounts to the summary Settlement report so that reconciliation of funds can be done.
* Paymentology will submit the chargeback using the appropriate chargeback reason code.

# Chargeback Process Flow

<Image border={false} src="https://files.readme.io/f65228ea164d4243d6699ba16f60a6aa97148370465bdf7c643fb50442611889-image.png" />

***

# Mastercard: Dispute/Chargeback categories and timeframes

When the transaction was completed with electronically recorded card information (whether card-read or key-entered), the acquirer has a maximum of seven calendar days after the transaction date to present the transaction to the issuer. A pending authorization should not be reversed before the seven calendar days. However, An issuer must accept a transaction submitted beyond the applicable time frame when the account is in good standing or the transaction can be honored.

There are four categories for chargeback processing:

<br />

<table>
  <thead>
    <tr>
      <th align="center">REASON CODE</th>
      <th align="center">REASON CODE DESCRIPTION</th>
      <th align="center">TIMEFRAME</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td align="center">4808</td>
      <td align="center">Authorization-related Chargeback</td>
      <td align="center">90 calendar days</td>
    </tr>

    <tr>
      <td align="center">4853</td>
      <td align="center">Cardholder dispute</td>
      <td align="center">120 calendar days</td>
    </tr>

    <tr>
      <td align="center">4837 / 4849 / 4870 / 4871</td>

      <td align="center">
        <strong>Fraud</strong><br /><br />
        • No cardholder authorization<br />
        • Questionable merchant activity<br />
        • Chip liability shift<br />
        • Chip liability shift – Lost/Stolen / Never Received Issue (NRI) fraud
      </td>

      <td align="center">120 calendar days</td>
    </tr>

    <tr>
      <td align="center">4834</td>
      <td align="center">Point-of-interaction error</td>

      <td align="center">
        90 calendar days<br />
        (ATM-related disputes: 120 calendar days)
      </td>
    </tr>
  </tbody>
</table>

<br />

* [Dispute Resolution Form – Fraud](https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/Dispute-Resolution-Form-Fraud.docx)
* [Dispute Resolution Form](https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/Dispute-Resolution-Form.docx)

<div
  style={{
    background: "#0F1F3A",
    color: "#FFFFFF",
    padding: "24px 28px",
    fontSize: "15px",
    lineHeight: "1.6",
  }}
>
  <p style={{ margin: "0 0 20px 0" }}>
    Mastercard chargeback collaboration period is between <strong>24–72 hours</strong>.
    Chargebacks can take up to <strong>72 hours</strong> to reflect as processed by
    Mastercard. This means that the chargeback is paused for that period and the
    <strong> 45 days waiting for second presentment</strong> only starts from the
    date the chargeback is actually processed. If no second presentment is
    received within 45 days, we automatically load the funds thereafter.
  </p>

  <p style={{ margin: 0, fontWeight: 600 }}>
    Please be informed that all Mastercard chargebacks will have to wait for
    <strong> 48 days</strong> to see if a chargeback is successful (no second
    presentment) and then the funds will be loaded. Our Dispute Team will notify
    the due date on each chargeback case accordingly.
  </p>
</div>

***

# Visa: Dispute/Chargeback categories and timeframes

Most disputes have 120 days time frame but for some such as, Authorization related are only 75 days.

There are four categories for chargeback processing:

<br />

<table>
  <thead>
    <tr>
      <th align="center">FRAUD</th>
      <th align="center">AUTHORIZATION</th>
      <th align="center">PROCESSING ERRORS</th>
      <th align="center">CONSUMER DISPUTES</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td align="center">EMV Liability Shift Non-Counterfeit Fraud</td>
      <td align="center">Visa Fraud Monitoring Program</td>
      <td align="center">Late Presentment</td>
      <td align="center">Merchandise / Services not received</td>
    </tr>

    <tr>
      <td align="center">EMV Liability Shift Non-Counterfeit Fraud</td>
      <td align="center">Declined Authorization</td>
      <td align="center">Incorrect Transaction Code</td>
      <td align="center">Cancelled Recurring</td>
    </tr>

    <tr>
      <td align="center">EMV Liability Shift Non-Counterfeit Fraud</td>
      <td align="center">No Authorization</td>
      <td align="center">Incorrect Currency</td>
      <td align="center">Not as Described or Defective Merchandise / Services</td>
    </tr>

    <tr>
      <td align="center">EMV Liability Shift Non-Counterfeit Fraud</td>

      <td align="center" />

      <td align="center">Incorrect Account Number</td>
      <td align="center">Counterfeit Merchandise</td>
    </tr>

    <tr>
      <td align="center">Visa Fraud Monitoring Program</td>

      <td align="center" />

      <td align="center">Incorrect Amount</td>
      <td align="center">Misrepresentation</td>
    </tr>

    <tr>
      <td align="center" />

      <td align="center" />

      <td align="center">Duplicate Processing / Paid by Other Means</td>
      <td align="center">Credit Not Processed</td>
    </tr>

    <tr>
      <td align="center" />

      <td align="center" />

      <td align="center">Invalid Data</td>
      <td align="center">Cancelled Merchandise / Services</td>
    </tr>

    <tr>
      <td align="center" />

      <td align="center" />

      <td align="center">Original Transaction Not Accepted</td>

      <td align="center" />
    </tr>

    <tr>
      <td align="center" />

      <td align="center" />

      <td align="center">Non-Receipt of Cash or Load Transaction Value</td>

      <td align="center" />
    </tr>
  </tbody>
</table>

* [Visa Generic Dispute Form](https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/Visa-Generic-Dispute-Form.docx)

# What is a Fraud Dispute?

When a cardholder says that they do not recognize transactions and have no knowledge of the transactions and were not in the vicinity where the said transactions were performed – and their card was in their possession at the time of the the transaction i.e. they did not attempt the transaction at all.

For all Fraud related chargebacks, we have to report the fraudulent transaction to the various card schemes on their respective platforms:

* Mastercard – Fraud Center/SAFE
* Visa – VROL
* UPI – FRM

If a transaction was processed with [3D Secure](https://developer.sprint.paymentology.com/companion-api/manage-funds/3d-secure/), we are not able to submit a Fraud chargeback therefore, the first step is to establish if there was a 3D Secure validation done.
