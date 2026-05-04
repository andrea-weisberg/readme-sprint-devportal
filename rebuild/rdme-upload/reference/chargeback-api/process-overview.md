---
title: Process overview
category:
  uri: Chargeback API
slug: process-overview
position: 8
---

## Breakdown of the chargebacks process with Chargeback API

The Paymentology dispute resolution cycle facilitates the whole process of reversing payments to cardholders. Card transaction disputes usually start when a cardholder or an issuer identifies suspicious, fraudulent, or erroneous charges on accounts.
Issuers and acquirers then follow a process to attempt to resolve the dispute. In the case of Mastercard, the two parties use the Mastercom platform to create and manage disputes throughout their lifecycle, expedite the dispute resolution process, and ensure satisfactory handling of the claims.

All chargebacks initiated will be processed using Mastercom Version 6.

## Typical dispute resolution cycle steps:

# [Step 1: First chargeback](#step 1)

# [Step 2: Collaboration phase](#step 2)

# [Step 3: Second presentment](#step 3)

# [Step 4: Pre-arbitration case](#step 4)

# [Step 5: Arbitration case](#step 5)

![Chargeback process flow](https://developer.sprint.paymentology.com/wp-content/uploads/2024/02/Diagram-for-Sprint-Developer-Porta_Lightmode-2.png)

As part of the claim resolution process:

- Paymentology provides a Chargeback API that allows clients to submit the required data for making the first chargeback.

- Paymentology handles all chargebacks that move into second presentment, pre-arbitration, and arbitration stages.

- Paymentology provides an API that allows clients to submit the required data for pre-arbitration case filings.

- Paymentology allows clients to track the status of each phase of the dispute resolution cycle. We also provide up-to-date reports about the outcome of each step.

## Let's take a look at the steps in more detail

After every step, the issuer or acquirer can opt to close the dispute. If not, the matter will eventually be escalated to Mastercard to issue a ruling.

### Step 1: First chargeback

If we deem the claim to be valid, we can make the first chargeback, transferring the disputed funds from the acquirer to us.
We then communicate to the acquirer about the chargeback by giving a chargeback reason code as well as supportive data.
The chargeback must be for a lesser transaction amount or the entire transaction amount—it cannot be higher than the entire amount.
To successfully complete this step, we provide a Chargeback API that allows you to send us the following information:

#### Payload example

{
"trackingNumber": "tRaCkInGnUmBeR",
"transactionId": "tRaNsAcTiOnId",
"authnumber": "AuthNumber",
"systemDate": "2021-08-24 00:00:00",
"settlementAmount": 402.76,
"chargebackAmount": 5.74,
"reasonCode": "4834",
"supportingDocument": "BASE64_ENCODED_FILE_HERE"
}

### Step 2: Collaboration phase

Issuer-initiated chargebacks remain in a pending status (no more than 72 hours) on issuers’ behalf to allow merchants to respond and resolve the inquiry.
In this phase, the acquirer can reject the first chargeback and refund the disputed amount. This closes the dispute and prevents them from going through the chargeback process.
If the acquirer rejects the first chargeback, we will get a notification of rejection and a refund should be processed by the acquirer. If they don't reject it, the chargeback is then processed as normal to which the acquirer can then dispute if they disagree by making a second presentment.

### Step 3: Second presentment

If the acquirer is dissatisfied with the chargeback reason, they can create a second presentment that gives their side of the story.
This step transfers the money from the issuer to the acquirer. The second presentment must be for a lesser chargeback amount or the entire chargeback amount. It cannot be higher than the entire amount.
After receiving the second presentment, Paymentology will notify the client and present the documents for the case.
The client will then decide the next course of action - either to accept the second presentment and close the dispute or continue with the dispute.

### Step 4: Pre-arbitration case

If we are dissatisfied with the second presentment reason, we can make a second chargeback, which is referred to as an pre-arbitration case.
Paymentology provides an API that allows clients to submit the required data for pre-arbitration case filings.
The pre-arbitration case must be for a lesser second presentment amount or the entire amount—it cannot be higher than the entire amount.

### Step 5: Arbitration case

The arbitration case filing step escalates the issue to Mastercard. Mastercard will then examine the evidence provided by both the issuer and the acquirer to determine the party that carries the day.
