# Offline PIN

Offline PIN is a card verification method used for EMV chip cards as the PIN is stored on the chip. This means that cardholder verification can occur even if a POS terminal is not connected to a network.

As with any PIN, the offline PIN will be blocked after too many unsuccessful attempts.

The way the offline PIN transactions differ from online PIN transactions is with online PIN, the PIN is encrypted and sent to Paymentology in an ISO message however with offline PIN transactions, we use different cardholder verification methods and checks to validate the transaction.

### How to update the Offline PIN

- The Issuer calls the [ChangePIN](/api-reference/companion-api/changepin) API

- We instantly update the online PIN, and record that the offline PIN needs to be updated

- The next time a card-present transaction arrives, that is not NFC based, Paymentology will return a message to the terminal, which should tell the card to update the issuer script

- In the following transaction, if it specifies that the previous attempt to update the issuer script fails, we will mark the update as needing reprocessing again
