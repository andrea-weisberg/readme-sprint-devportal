---
title: Disputes
category:
  uri: Guides
slug: disputes-card-api
position: 42
parent:
  uri: card-api
---

# What is a Dispute?

A dispute is a transaction that a cardholder/customer does not agree with and therefore requests that part of, or the entire transaction be reversed or refunded.

## Types of Disputes:

- **Reversal –**A reversal is essentially a request for a transaction that was not completed and could have failed at a particular step of the transaction process. It is an advisement message to all parties of the transaction and ensures that the card and store of value are put back into their original state if a failed to deduct transaction had been initiated. If you sent a transaction and did not receive a confirmation that the transaction was successful, it could imply that the transaction did not reach the intended destination.

- **Refund** – A refund is when funds are credited back to the customer’s card from a previously debited transaction. A refund is processed when the merchant refunds the customer for returned goods and the funds which were settled to the merchant’s account need to move back to the cardholder’s account.

- **Chargeback –**A chargeback is the return of funds for a deduct transaction that was previously processed from a cardholder’s card balance, due to a successful dispute by the consumer regarding the transaction

# How Disputes Work

## What is a Chargeback?

Once a dispute is raised, card issuers (like Paymentology) are able to submit a chargeback using a specific set of reason codes via the card scheme (Mastercard/Visa). There are a specific set of rules and timeframes set out by the card scheme that need to be followed in order to submit a chargeback.

Chargebacks can only be submitted if the transaction has settled i.e. funds have moved from the Issuer’s bank account to the merchant’s bank account for the transaction.

## What is a Second Presentment?

A second presentment (sometimes called a re-presentment) is the merchant’s opportunity to disagree with the chargeback request submitted by the Issuer on behalf of the cardholder. After a chargeback request has been submitted, the merchant/acquirer will have 10/35/45 days in which they may submit second presentments (also called pre-arbitration with some card schemes), depending on card scheme rules.

## What is Pre-Arbitration and Arbitration?

Following a receipt of a second presentment (also knows as re-presentment), the cardholder can choose to further dispute the second presentment by submitting a Pre-Arbitration. If the Pre-Arbitration is not successful, the cardholder can further proceed with submitting an Arbitration (the final option in the Dispute cycle) which in most cases will mean that the card scheme will rule in the case, either in favour of the Issuer or Acquirer depending on the merit of the case. There are specific timeframes for these processes which differ between the card schemes.

# Dispute Lifecycle

Paymentology manages dispute handling and chargeback processing on behalf of our clients in three ways:

- Client initiated disputes

- Batch chargeback submission

## 1. Individual chargeback submission

- Paymentology will provide the client with one of two chargeback dispute forms: – General dispute form – Fraud dispute form

- The client’s merchant/customer will complete the form and select the appropriate reason

- The client will send this dispute to Paymentology's Global support team via email - support@paymentology.com

- Based on the information provided, Paymentology will investigate the transaction being disputed

- Paymentology will submit the chargeback using the appropriate chargeback reason code

## 2. Batch chargeback process

- The client can send Paymentology a list of disputes, using a predefined batch chargeback submission template that has been requested to chargeback. The client can define the chargeback reason code. Depending on whether the documentation is required or not, Paymentology will submit these chargebacks on the client’s behalf.

- Paymentology will monitor and track the chargeback throughout the dispute lifecycle of submission, second presentments and arbitration.

- Once the chargeback has been finalized, our Dispute Management Team will notify the client.

- We will credit the card balance.

- We will add the chargeback amounts to the Summary Settlement report so that reconciliation of funds can be done.

- Paymentology will submit the chargeback using the appropriate chargeback reason code.

# Chargeback Process Flow

![](https://developer.sprint.paymentology.com/wp-content/uploads/2023/03/Chargeback-process-flow-v2.png)

# Mastercard: Dispute/Chargeback categories and timeframes

When the transaction was completed with electronically recorded card information (whether card-read or key-entered), the acquirer has a maximum of seven calendar days after the transaction date to present the transaction to the issuer. A pending authorization should not be reversed before the seven calendar days. However, An issuer must accept a transaction submitted beyond the applicable time frame when the account is in good standing or the transaction can be honored.

There are four categories for chargeback processing:

[Dispute Resolution Form - Fraud](https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/Dispute-Resolution-Form-Fraud.docx)

[Dispute Resolution Form](https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/Dispute-Resolution-Form.docx)

Mastercard chargeback collaboration period is between 24-72 hours. Chargebacks can take up to 72 hours to reflect as processed by Mastercard. This means that the chargeback is actually paused for that period and the **45 days waiting for second presentment** only starts from the date the chargeback is actually processed. If no second presentment is received within 45 days, we automatically load the funds thereafter.

**Please be informed that all Mastercard chargebacks will have to wait for 48 days to see if a chargeback is successful (no second presentment) and then the funds will be loaded. Our Dispute Team will notify due date on each chargeback case accordingly.**

# Visa: Dispute/Chargeback categories and timeframes

Most disputes have 120 days time frame but for some such as, Authorization related are only 75 days.

There are four categories for chargeback processing:

[Visa Generic Dispute Form](https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/Visa-Generic-Dispute-Form.docx)

# What is a Fraud Dispute?

When a cardholder says that they do not recognize transactions and have no knowledge of the transactions and were not in the vicinity where the said transactions were performed – and their card was in their possession at the time of the the transaction i.e. they did not attempt the transaction at all.

For all Fraud related chargebacks, we have to report the fraudulent transaction to the various card schemes on their respective platforms:

- Mastercard – Fraud Center/SAFE

- Visa – VROL

- UPI – FRM

If a transaction was processed with [3D Secure](/guides/3d-secure), we are not able to submit a Fraud chargeback therefore, the first step is to establish if there was a 3D Secure validation done.
