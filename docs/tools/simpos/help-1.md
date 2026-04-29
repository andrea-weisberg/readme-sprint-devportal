---
title: Help
deprecated: false
hidden: false
metadata:
  robots: index
---
## How SimPOS works

SimPOS is used to test the flow of a virtual card transaction over the Companion Card API, and to check that all components are working.

- When a transaction is performed on SimPOS, a message is sent to Paymentology’s Sprint test card platform (in the same format that would be received from a POS with all the transaction details included).
- The card platform then creates a **Deduct** call message using the wallet id linked to the card and includes some of the transaction details received in the message received for the transaction.
- The call message Paymentology creates is then sent to the web service URL provided for the wallet platform, over the **Remote API**.
- Once the call message is received and processed on the wallet side, an XML response needs to be sent to the card platform to approve or decline the transaction. This is where a **local API** call message is sent to the Paymentology Sprint platform using a **Result Code** included in the **Companion Card API** documentation.
- Once the card platform receives the response, a response is then sent to SimPOS to either approve or decline the transaction.

## Testing with SimPOS

Things to check:

- Did the wallet platform receive a **Deduct** call message for the transaction from Paymentology?
- Did the wallet platform deduct funds from the wallet for the transaction?
- Did the wallet platform send a response to the Paymentology Sprint local API?
- What was the response on SimPOS for the transaction?
- Does the response received on SimPOS match the response sent to Paymentology’s Sprint platform or not?

## How to use SimPOS

1. Go to [SimPOS](.) under [Tools](..)
2. Click on the **Web** tab
3. Enter the card number, expiry date and CVV for the test card that was created using `CreateLinkedCard` method on the **local API**
4. Enter a random amount for the test transaction
5. Enter a random merchant
6. Click on **Swipe** button
7. Wait for **Transaction result pop-up** which will show various response codes. Refer to the full list of response codes on the API documentation page.

You can find a list of SimPOS Response codes [here](simpos-result-codes).
