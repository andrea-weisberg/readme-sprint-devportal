---
title: Processing
deprecated: false
hidden: false
metadata:
  robots: index
---
<!-- MIGRATION_METADATA
Migrated-From: https://developer.sprint.paymentology.com/card-api/tokenization/processing/
Source-Slug: processing
Migrated-On: 2026-02-12T20:19:12+00:00
Migrated-By: wp-readme-migration
-->

Processing a transaction using a token basically follows these steps:

(We’ll assume that the card’s data has already been provisioned)


**Step 1: **The cardholder initiates the transaction and provides their sensitive credit card details. The transaction can be initiated via a mobile app, at an NFC store, or on an e-commerce site.

**Step 2: **The merchant initiates the payment authorization request by submitting a token, in place of a PAN, to their acquiring bank.

**Step 3:** The acquiring bank passes the token to the credit card network.

**Step 4:** The credit card network maps the token with the original PAN, and verifies the rightful use of the payment token. During provisioning, the card network stores the original PAN in its secure token vault. After the processing, the card network transmits the PAN and token to Paymentology, which is the issuer, for authorization.

**Step 5: **Paymentology authorizes or declines the transaction

**Step 6: **Paymentology sends the authorization response to the card network.

**Step 7: **The card network substitutes the PAN back to the token and sends the response to the acquirer and to the merchant.

**Step 8**: The merchant and the acquiring bank coordinate to finalize the transaction.
