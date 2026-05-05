---
title: Manage funds
category:
  uri: Guides
slug: manage-funds
position: 22
parent:
  uri: companion-api-guide
---

**When the cardholder has either a virtual or a physical companion card (or both), they can start transacting against their store of value. These transactions originate from the merchant and are then sent to Paymentology via the card schemes, before being forwarded to the store of value for validation and authorization.**

To enable and manage this process, Paymentology Sprint uses what is called the [Remote API](/api-reference/companion-api/remote).

These are the supported transaction management options:

- Getting a balance on a card

- Doing a deduct transaction on a card

- A reversal for a deduct transaction

- Adjustments on a card

## 1. Getting a balance on a card

If a card is enabled for ATM transactions, then the cardholder can make balance inquiries at an ATM machine. The balance that is sent back is the amount remaining in the stored value.

You’ll need to make a call to the [Balance](/api-reference/companion-api/remotebalance/) method.

## 2. Doing a deduct transaction on a card​

When a cardholder makes an ATM, point of sale (POS), or e-commerce transaction, Paymentology will send a Deduct request for the funds to be deducted from the store of value.

You’ll need to respond with Approved for the transaction to be concluded successfully.

![Companion API transaction processing](https://files.readme.io/d88d63598252f493642679a06d4eb85161d4080668635f64adf0537b1b7ed5b6-d04a2f183bd6bf4e85405338e2c5df4e3b9e53e4e98228379e7029ad1d379771-Companion-transaction-processing-3-v2.png)

## 3. A reversal for a deduct transaction

A reversal is essentially a request for a transaction that was not completed and could have failed at a particular step of the transaction process. It is an advisement message to all parties of the transaction and ensures that the card and store of value are put back into their original state if a failed to deduct transaction had been initiated.

If you sent a transaction and did not receive a confirmation that the transaction was successful, it could imply that the transaction did not reach the intended destination.

Reversals are triggered by merchants for three reasons:

#### 1. The merchant did not receive any response back from the card scheme for the authorization request. In this case, the merchant would timeout the transaction

Scenario: In this scenario, a [Deduct](/api-reference/companion-api/remotededuct/)request was sent to the store of value system but there was no response received. This will cause a time out, as no response will be sent back to the merchant.

**A full cycle of an authorization must be concluded within 5 seconds meaning a response from the store of value system needs to be received with 2 seconds maximum.**

Due to no response, a [DeductReversal](/api-reference/companion-api/remotedeductreversal/) will be triggered and the store of value system will match the **TransactionID**of the initial [Deduct](/api-reference/companion-api/remotededuct/)and match it with the **ReferenceID** in the [DeductReversal](/api-reference/companion-api/remotedeductreversal/)and **Approves** the [DeductReversal](/api-reference/companion-api/remotedeductreversal/)by responding with **1 - Success** and reverse the funds the funds back.

The store of value system does not have the option to respond with a -9 Crashed or disapproved response.

#### 2. The merchant receives a timeout request from the card scheme due to connectivity issues

Scenario: In the scenario, due to connectivity issues the [Deduct](/api-reference/companion-api/remotededuct/)request is not sent to the store of value system. This results in a timeout in the transaction. The merchant will timeout the transaction and trigger a [DeductReversal](/api-reference/companion-api/remotedeductreversal/)which will be sent to the store of value system. At this point, the store of value system has no record of the initial [Deduct](/api-reference/companion-api/remotededuct/).

The store of value system will attempt to match the **ReferenceID** in the [DeductReversal](/api-reference/companion-api/remotedeductreversal/), which they will not find as the initial [Deduct](/api-reference/companion-api/remotededuct/)did not reach the store of value system. The store of value system will send an acknowledgement = **1 – Success**but no funds will be moved on the store of value system

The store of value system may not respond with a -9 Crashed or disapproved response.

#### 3. The merchant voided the transaction

Scenario: In this scenario, the authorization is cancelled/ voided immediately after a successful transaction has been concluded. The store of value system will have received the initial [Deduct](/api-reference/companion-api/remotededuct/)request.

The store of value system will match the **ReferenceID** of the [DeductReversal](/api-reference/companion-api/remotedeductreversal/)to the **Transaction ID** of the initial [Deduct](/api-reference/companion-api/remotededuct/)request. They will reverse the funds and respond with **1 – Success.**

The store of value system may not respond with a -9 Crashed or disapproved response.

Also, the transaction could have reached the destination and was processed correctly, but the confirmation response was “lost” along the way.

Paymentology will link the deduct reversal to the original authorization, we do this by including a ReferenceID in the [DeductReversal](/api-reference/companion-api/remotedeductreversal/)API request. The ReferenceID field is the transaction ID of the original authorization (Deduct).

Here is a table that shows the only acceptable response codes that can be sent to Paymentology:

![Reversal flow](https://files.readme.io/092575ff0b6822bf700b1ea7e64b881dc1f29b64650ffe151fb400adf8dc8a0b-a3fa269f2206e8108483dc14d7120a08ef380343bf9e77145d9bb04690a2dc51-Reversal-v2.png)

## 4. Adjustments on a card

Just like in any other account, there may be times when your funds need to be adjusted to reflect some changes that have occurred.

For example, a refund could have been issued to your card, and it needs to be adjusted on the store of value as this is where the balance will be managed eventually.

These are the common types of adjustment transactions on companion cards:

- Load adjustment transactions

- Load reversal transactions

- Deduct adjustment transactions

Let’s look at each of them.

### **i) Load adjustment transactions**

If there is a need to load money back into a store of value, Paymentology will send a load adjustment request so that the store of value makes the adjustment.

**LoadAuth**

LoadAuth is an authorisation, but for a load, rather than a deduct. This would most commonly be the result of a **refund** from a merchant. But it could also be a load from a "money send" type transaction, where cardholders can transfer funds over the MC network, if your program allows this. This method is most similar to the [Deduct](/api-reference/companion-api/remotededuct/) method, which is an authorisation for a redemption.

You can decline this transaction i.e. choose not to approve it. If you decline, the refund will not be completed at the merchant. There are 3 important things to note:

- If you approve this transaction, **do not** immediately load the card

- Unlike [Deduct](/api-reference/companion-api/remotededuct/), the card should **only** be loaded when the funds are cleared because then you know you have received them (for most systems, after evaluating and approving this transaction, there would be nothing further for you to do). You may choose to reflect a pending amount on cardholder statements but this should not be included in their available balance

- If you decline this transaction, you should expect cardholder frustration because cardholders are not familiar with refunds being declined because it does not depend on their available balance. Therefore, it is recommended that you approve these transactions unless there are strong reasons not to. NB. If a refund is fraudulent for some reason, the liability sits with the Merchant.

Mastercard has mandated that refunds should be authorised but merchants do not follow this. Therefore, you will find very few [LoadAuth](/api-reference/companion-api/remoteloadauth/)requests as most as just sent immediately as settlement (which you will receive as [LoadAdjustments](/api-reference/companion-api/remoteloadadjustment/))

Once the request has been approved, the amounts on both the card and the store of value will be balanced.

However, if the request is not accepted by the store of value, Paymentology will continue sending it ten times at regular intervals. If unsuccessful, the adjustment request will be retired as not processed.

Here is a table that shows the only acceptable response codes that can be sent to Paymentology:

You’ll need to respond to the [LoadAdjustment](/api-reference/companion-api/remoteloadadjustment/)method.

A Refund is a movement of funds from a merchant to a cardholder and may or may not relate to a previous deduct of funds. This uses the [LoadAuth](/api-reference/companion-api/remoteloadauth/) method. Refunds are a new movement of funds.

A Load Adjustment is an adjustment being made that gives money to the cardholder that has to be accepted by the wallet. It relates to a previous transaction. This uses the [LoadAdjustment](/api-reference/companion-api/remoteloadadjustment/) method. Load Adjustments happen when the cardholder has more money than anticipated, such as when a settlement is cancelled or a settlement happens for less than the authorization amount.

### LoadAdjustment

As for a [LoadAuth](/api-reference/companion-api/remoteloadauth/), this is the result of a refund or a money transfer request that loads funds to a cardholder but this is an advice message confirming that the funds have moved.

When a [LoadAuth](/api-reference/companion-api/remoteloadauth/)is settled, it will result in a [LoadAdjustment](/api-reference/companion-api/remoteloadadjustment/)(this assumes no [LoadAuthReversal](/api-reference/companion-api/remoteloadauthreversal/)occurred). As with all advice messages, it is **required** that the message is approved. There is no other option except for a system failure/crash. Your response of "1" is not "approving" the adjustment, it is confirming that you have been notified of the adjustment. All adjustments have already occurred and declining such a message will not change that. If you respond with anything besides approval, it results in a process of manual intervention to investigate why the failure occurred and to work with you to take steps to correct it.

Many clients wish to link any refunds back to the original transaction. MasterCard has implemented some fields to allow this, but merchants do not use these fields. From their perspective, they do not see any reason necessary to complete the development necessary for this to work. This is similar to merchants being mandated to obtain authorisation for refunds, which they also tend not to do. To a significant degree, you would want to be cautious about how much energy you invest in trying to do this. As an Issuer, if you receive a refund settlement, you must process and if there is fraud taking place at the Merchant, it is at the Merchant's cost - not yours.

If you really don't want to refund a wallet unless you can reconcile the refund, our recommended course of action is:

- Acknowledgement of he adjustment API (you have to do this)

- But then, do not load the wallet

In other words, once you have acknowledged the API call with a valid APO response, Paymentology does not concern itself with how you handle those funds. so, you could choose to reflect the funds in some holding account and the you work through some administrative process to approve the refund and then you transfer to the wallet when you are satisfied it is legitimate. This way:

- You are still responding correctly to the API calls

- You still have control of the funds and when and where to load them without having caused a failure by rejecting the API call

### ​ii) Load reversal transactions

If there is a need to load money back into a store of value, and the client is not accepting the adjustment request, Paymentology will send a load reversal request to ensure that no action is undertaken.

**LoadAuthReversal**

This is a reversal message for [LoadAuth](/api-reference/companion-api/remoteloadauth/). It is the equivalent of [DeductReversal](/api-reference/companion-api/remotedeductreversal/). This will be sent if we do not receive any response to the [LoadAuth](/api-reference/companion-api/remoteloadauth/). As with all adjustments and reversals, they are "advice" messages, they are "telling" you to do something. They are not asking you to approve something. Your response should therefore be an acknowledgement that you have received the message not that you "approve" the message. For all reversals, we will keep resending if we do not receive positive acknowledgement. Failure to respond repeatedly results in manual intervention which should only happen if your system is down.

Our recommendation for reversals is:

- You should add the reversal to an internal queue (a low intensity operation)

- You should then immediately respond positively to our API call

- And only then, attempt to process the reversal (a high intensity operation)

- This is because very often, reversals only happen during problems s o you don't want to exacerbate the problem, by performing complex tasks as you receive the reversal

- It's therefore best to queue the complex tasks for processing only after you have responded

- This way we stop messaging you with repeats of reversals, which will only add to your load

After that, Paymentology will resend a [LoadAdjustment](/api-reference/companion-api/remoteloadadjustment/)request so that an OK response can be returned. This pattern will continue ten times until the adjustment is processed adequately against the stored value.

You’ll need to make a call to the [LoadReversal](/api-reference/companion-api/remoteloadreversal/)method.

NB. You are putting the system back to how it was before the transaction that is being reversed but you should never delete anything, only post contra-transactions. However, be careful of repeats - you don't want to accidentally keep deducting or loading additional funds every time a reversal is repeated

Remember, the transaction and reversal failures may be the result of a network interruption that is happening after you have responded each time. You may receive multiple reversals for a reversal which you have already processed so you must be able to identify that you have already processed the reversal to prevent "duplication".

What you do on your system for a [LoadAuthReversal](/api-reference/companion-api/remoteloadauthreversal/)will depend on what you do for a [LoadAuth](/api-reference/companion-api/remoteloadauth/). If you approve and did nothing else (see [LoadAuth](#LoadAuth) above for more information), then there isn't anything for you to do when reversing. If your system records and reflects the "pending" load, you'd need to remove this pending load.

A Reversal is a cancellation (in whole or in part) of a fund movement from the cardholder to the merchant. This uses the [LoadAuthReversal](/api-reference/companion-api/remoteloadauthreversal/) method.

Partial settlements/adjustments occur when:

- There are significant changes in currency exchange rates

- Authorizing payments before the final amount is known (i.e online groceries when items may be substituted)

### LoadReversal

This is sent if we do not receive any response to the [LoadAdjustment](/api-reference/companion-api/remoteloadadjustment/). All the other rules mentioned in [LoadAuthReversal](/api-reference/companion-api/remoteloadauthreversal/)still apply.

- It is an advice message which you must "approve" (i.e. send a response acknowledging the advice message)

- It will be repeated if you not respond to it

- After 10 repeats, it will be logged for manual intervention

- You should add to an internal queue and respond immediately and then process from your queue

One big difference is that, almost without exception, a [LoadAdjustment](/api-reference/companion-api/remoteloadadjustment/)will result in actual funds having been loaded to a cardholder balance, and so reversing this means you will need to "undo" that load. Again, undoing a load might practically be done through a deduct but you are not deducting, you are putting the wallet back to it's previous state. The difference becomes important when ensuring that you are able to handle repeats. Do not keep deducting every reversal you receive as you may already have done the deduction. Remember that the connection failure we are experiencing with you, might only be for messages after you have processed them.

Some important points to note about reversals:

- It **is** possible to receive a reversal for which you cannot find the original reference. - You might not find it because you never received the original transaction (this is normal, and part of the design of reversals) - You might not find it because, even though you received it, you already reversed it In both cases, you would effectively do nothing, because there is nothing to reverse.

- Do **not** debit/credit (whichever is applicable) just because you received a reversal. You have to find the original transaction, confirm it has not been reversed, and reverse it. If you cannot find it, or it has already been reversed, there is nothing further to do. You must also still respond positively to the Reversal API call confirming you received it

- You do not need to tell us (since it is not relevant) whether you found the original transaction to reverse or not

### iii) Deduct adjustment transactions

In some cases, there may be a discrepancy between the funds that were authorized on a transaction and what was actually settled. When a user makes a purchase at a point of sale, it takes a two-step process for the transaction to be completed.

First, an authorization request is made and the funds for the transaction are taken from the card and kept in reserve.

Then, the second half of the transaction takes place when the bank that processes the merchant’s payments generates a clearing request to the given card association for this authorization to be settled. Just like the authorization request, the card associations also forward this settlement request to Paymentology.

So, whenever the clearing request amount is higher than the authorization request amount for any reason, such as due to rising exchange rates, the store of value will be debited for this differing amount. The store of value must acknowledge this request for it to be handled appropriately. Although the cardholder has the right to dispute this transaction, the debit should happen first before the dispute can be filed.

If the store of value does not send an OK response to Paymentology, then the card will remain in a state of having a pending adjustment, and no transaction would be processed until the adjustment has been rectified.

You’ll need to make a call to the [DeductAdjustment](/api-reference/companion-api/remotedeductadjustment/)method.

A Deduct Adjustment is an adjustment being made that takes money from the cardholder, that has to be accepted by the wallet. This uses the [DeductAdjustment](/api-reference/companion-api/remotedeductadjustment/) method. Deduct Adjustments happens because a settlement wasn’t authorized, or was authorized for less.

Adjustments must be accepted, even if there are not sufficient funds on the wallet. You have to accept the adjustment and record the fact that you have this negative balance with the wallet, regardless of whether or not you would actually ever show the wallet as having negative funds
