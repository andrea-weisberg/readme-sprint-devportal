---
title: Offline PIN
deprecated: false
hidden: false
metadata:
  robots: index
---
Offline PIN is a card verification method used for EMV chip cards as the PIN is stored on the chip. This means that cardholder verification can occur even if a POS terminal is not connected to a network.

<div
  style={{
    background: "#0F1F3A",
    color: "#FFFFFF",
    padding: "16px 20px",
    fontSize: "15px",
    lineHeight: "1.6",
    fontWeight: 500,
  }}
>
  As with any PIN, the offline PIN will be blocked after too many unsuccessful
  attempts.
</div>

The way the offline PIN transactions differ from online PIN transactions is with online PIN, the PIN is encrypted and sent to Paymentology in an ISO message however with offline PIN transactions, we use different cardholder verification methods and checks to validate the transaction.

<br />

## How to update the Offline PIN

1. The issuer calls the `ChangePIN` API
2. We instantly update the online PIN, and record the fact that the offline PIN needs updating
3. The next time a card-present transaction arrives, that is not NFC based, we will return the issuer script to the terminal, which should tell the card to update the script
4. In the following transaction, if it specifies that the previous attempt to update the issuer script fails, we will mark the update as needing reprocessing again
