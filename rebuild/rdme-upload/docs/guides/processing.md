---
title: Processing
category:
  uri: Guides
slug: processing
position: 39
parent:
  uri: tokenization
---

Processing a transaction using a token basically follows these steps:

(We’ll assume that the card’s data has already been provisioned)

![Authorization Request flow](https://developer.sprint.paymentology.com/wp-content/uploads/2023/03/Tokenization-Flow_01-v2.png)

**Step 1:**The cardholder initiates the transaction and provides their sensitive credit card details. The transaction can be initiated via a mobile app, at an NFC store, or on an e-commerce site.

**Step 2:**The merchant initiates the payment authorization request by submitting a token, in place of a PAN, to their acquiring bank.

**Step 3:** The acquiring bank passes the token to the credit card network.

**Step 4:** The credit card network maps the token with the original PAN, and verifies the rightful use of the payment token. During provisioning, the card network stores the original PAN in its secure token vault. After the processing, the card network transmits the PAN and token to Paymentology, which is the issuer, for authorization.

**Step 5:**Paymentology authorizes or declines the transaction

**Step 6:**Paymentology sends the authorization response to the card network.

**Step 7:**The card network substitutes the PAN back to the token and sends the response to the acquirer and to the merchant.

**Step 8**: The merchant and the acquiring bank coordinate to finalize the transaction.
