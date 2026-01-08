---
title: Manage funds
deprecated: false
hidden: false
metadata:
  robots: index
---
How to manage funds



**When the cardholder has either a virtual or a physical companion card (or both), they can start transacting against their store of value. These transactions originate from the merchant and are then sent to Paymentology via the card schemes, before being forwarded to the store of value for validation and authorization.**

To enable and manage this process, Paymentology Sprint uses what is called the [Remote API]() .

These are the supported transaction management options:

* Getting a balance on a card
* Doing a deduct transaction on a card
* A reversal for a deduct transaction
* Adjustments on a card

***

## 1. Getting a balance on a card

If a card is enabled for ATM transactions, then the cardholder can make balance inquiries at an ATM machine. The balance that is sent back is the amount remaining in the stored value.

You’ll need to make a call to the `Balance` method.

***

## 2. Doing a deduct transaction on a card​

When a cardholder makes an ATM, point of sale (POS), or e-commerce transaction, Paymentology will send a Deduct request for the funds to be deducted from the store of value.

You’ll need to respond with Approved for the transaction to be concluded successfully.

<Image border={false} src="https://files.readme.io/ae4453cdf9910f36c1cadc40d6c43593c79d1eb05195a6efceb0c47d8f9dbbd4-image.png" />

***

## 3. A reversal for a deduct transaction

A reversal is essentially a request for a transaction that was not completed and could have failed at a particular step of the transaction process. It is an advisement message to all parties of the transaction and ensures that the card and store of value are put back into their original state if a failed to deduct transaction had been initiated.

If you sent a transaction and did not receive a confirmation that the transaction was successful, it could imply that the transaction did not reach the intended destination.

Reversals are triggered by merchants for three reasons:

1. **The merchant did not receive any response back from the card scheme for the authorization request. In this case, the merchant would timeout the transaction**

Scenario: In this scenario, a `Deduct` request was sent to the store of value system but there was no response received. This will cause a time out, as no response will be sent back to the merchant.

_A full cycle of an authorization must be concluded within 5 seconds meaning a response from the store of value system needs to be received with 2 seconds maximum._

Due to no response, a `DeductReversal` will be triggered and the store of value system will match the **TransactionID** of the initial `Deduct` and match it with the **ReferenceID** in the `DeductReversal` and **Approves** the `DeductReversal` by responding with **1 – Success** and reverse the funds the funds back.

The store of value system does not have the option to respond with a -9 Crashed or disapproved response.

2. **The merchant receives a timeout request from the card scheme due to connectivity issues**

Scenario: In the scenario, due to connectivity issues the `Deduct` request is not sent to the store of value system. This results in a timeout in the transaction. The merchant will timeout the transaction and trigger a `DeductReversal` which will be sent to the store of value system. At this point, the store of value system has no record of the initial `Deduct`.

The store of value system will attempt to match the **ReferenceID** in the `DeductReversal`, which they will not find as the initial `Deduct` did not reach the store of value system. The store of value system will send an acknowledgement = 1 – Success but no funds will be moved on the store of value system

The store of value system may not respond with a -9 Crashed or disapproved response.

3. **The merchant voided the transaction**

Scenario: In this scenario, the authorization is cancelled/ voided immediately after a successful transaction has been concluded. The store of value system will have received the initial `Deduct` request.

The store of value system will match the **ReferenceID** of the `DeductReversal` to the **Transaction ID** of the initial `Deduct` request. They will reverse the funds and respond with **1 – Success**.

The store of value system may not respond with a -9 Crashed or disapproved response.

Also, the transaction could have reached the destination and was processed correctly, but the confirmation response was “lost” along the way.

Paymentology will link the deduct reversal to the original authorization, we do this by including a `ReferenceID` in the `DeductReversal` API request. The `ReferenceID` field is the transaction ID of the original authorization (Deduct).

Here is a table that shows the only acceptable response codes that can be sent to Paymentology:

Table: Response codes for the Reversals method

| Code | Description              |
| ---- | ------------------------ |
| 1    | Success (or approved)    |
| -9   | Crashed (or disapproved) |

<Image border={false} src="https://files.readme.io/bb12aa3330d56a949be2d13c202e18a3f19083b76737a8f5a4415c152a0cfe39-image.png" />

***

## 4. Reversing funds transferred between cards

If you want to reverse the transferred funds, for any reason, and the funds have not been used, then you can initiate a reversal process.

You’ll need to make a call to the `TransferFundsReverse` method.

***

## 5. Transferring funds between pockets

You can transfer funds between pockets for the easy management of money.
For example, you may want to transfer some funds from your expenditure pocket to your savings pocket.

You’ll need to make a call to the `PocketTransfer` method.

***

## 6. Reversing the pocket transfer

If you want to reverse the funds transferred to a pocket, for any reason, and the funds have not been used, then you can initiate a reversal process.

You’ll need to make a call to the `PocketTransferReverse` method.

***

## 7. Deducting funds from card or pocket

If a cardholder wants to deduct funds from their card or pocket balances, then they can specify the value that needs to be deducted.
The amount requested to be deducted must be equal or less than the balance; otherwise, the process will not be successful.
After the deduction has been completed successfully, the client then credits the customer’s store of value account.

You’ll need to make a call to the `DeductFunds` method.

***

## 8. Reversing the card deduction

If you want to reverse the funds deducted, for any reason, then you can initiate a reversal process.
Once successful, the balance will change based on the reversed amount.

[You’ll need to make a call to the `DeductFundsReverse` method.](https://developer.sprint.paymentology.com/card/documentation/card-api#deductfundsreverse)

***

## 9. Devaluing a card or pocket

You can perform a deduction of the full amount available on the card or pocket.
No partial amount will be removed from the card or pocket balances, but only all the funds.

You’ll need to make a call to the `Devalue` method.

***

## 10. Reversing a devalue

If you want to reverse the devaluing of funds from a card or pocket balance, for any reason, then you can initiate a reversal process.
Once successful, the devalued amount will be credited to the card or pocket balance.

You’ll need to make a call to the `DevalueReverse` method.
