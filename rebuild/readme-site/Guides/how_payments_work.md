# How Payments Work

There are different stages of a transaction when a card is used to pay for goods and services.

Let's look at each of them.

## What is a transaction?

A transaction is the movement of money from a cardholder's account to a merchant's account in exchange for goods or services provided.

## Stages in a transaction

Payment request - This is when the cardholder uses their card and the request is routed to the Issuer (Tutuka)
[Authorisation](/guides/companion-apisettlement-and-reconciliation/#authorization) - This is the process of checking the available funds on a card in order to reserve funds when the card is used for a purchase
[Settlement](/guides/companion-apisettlement-and-reconciliation/#settlements) - This is when funds are deducted from the Issuer/client’s bank account and deposited into a merchants bank account to settle a card transaction.
[Disputes](/guides/disputes) - This happens when a cardholder disagrees with a deduct on their card statement

## How the transaction is processed

- The Cardholder uses their card to pay for goods or services at a Merchant

- The card information is sent to the Acquirer. The Acquirer uses the BIN to identify the relevant Card scheme and sends the payment request to the Card scheme

- The Card scheme receives the payment request and routes the transaction to the Issuer (Tutuka) linked to the BIN for authentication and approval

- The Issuer (Tutuka) receives the payment request from the Card scheme and verifies the card details. Tutuka identifies the product type ([Card API](/guides/card-api) or [Companion API](/guides/companion-api))

- If the card is registered for Card API, Tutuka checks the balance on the card. If there are insufficient funds for the purchase, a decline response is sent. If there are sufficient funds, Tutuka reserves the funds on the card and an authorisation response is sent to the Card scheme

- If the card is registered for Companion API, Tutuka routes the payment request to the wallet provider who responds to Tutuka with an approval or decline based on the wallet balance. Tutuka sends this response to the Card scheme

- The Card scheme routes the authorisation or decline response to the Acquirer

- The Acquirer sends the response to the Merchant and the Cardholder

- The transaction is completed once funds are deducted from the Cardholder’s balance and settled in the Merchant’s account

## Who is involved in the transaction?

Cardholder – the customer who uses their card to pay for goods and services

Merchant – a person or business that provides the goods and services

Card scheme – the payment network linked to the card eg. Mastercard, Visa, UnionPay, etc. that links the two financial institutions on either end of the transaction

Issuer – the financial institution that issued the card to the Cardholder (Tutuka)

Acquirer – the bank that processes the transaction on behalf of the Merchant to ensure settlement of the transaction![General transaction lifecycle](https://developer.sprint.paymentology.com/wp-content/uploads/2021/10/Payment-lifecycle.png)

# Types of Transactions

## Card Present

POS Systems with card readers - This is a Point Of Sale terminal where you insert/swipe your card to pay for the transaction.

Contactless enabled terminals - This is a terminal which allows you tap your card using near-field communication.

ATM Transactions - This is when you use your physical card at an ATM to withdraw cash.

[AFD Transactions](/guides/companion-apimanage-funds/automated-fuel-dispensers-afd-transactions/) - Automated Fuel Dispensers (AFD) are unattended terminals at fuel stations that allow cardholders to purchase fuel without requiring an attendant. The emergence of AFD transactions has revolutionized the fuel purchase industry and greatly benefitted both merchants and customers. (Applicable to Asia only)

## Card Not Present

[Tokenization](/guides/companion-apitokenization2/) - Tokenization is the process of substituting the card’s sensitive data, such as an account number, with non-sensitive, surrogate data, called a token. The PAN (Primary Account Number) is usually replaced with a unique string of numbers that acts as a secure reference to the card.

[QR Payments](/guides/qr-payments-api) - The QR Payments plug-in allows you to create a contactless merchant payment system where customers can make electronic payments by scanning a QR code from a smartphone application.

[3D Secure](/guides/companion-apimanage-funds/3d-secure/) - 3D Secure is an additional authentication step that provides an added layer of security for online card transactions (e-commerce) by reducing the risk of unauthorized card use due to the card not being physically present by sending an OTP to the cardholder when the card is being used.

# [Disputes](/guides/disputes)

- Reversal A reversal is essentially a request for a transaction that was not completed and could have failed at a particular step of the transaction process. It is an advisement message to all parties of the transaction and ensures that the card and store of value are put back into their original state if a failed to deduct transaction had been initiated. If you sent a transaction and did not receive a confirmation that the transaction was successful, it could imply that the transaction did not reach the intended destination. Read more about Reversals [here](/guides/companion-apimanage-funds/#Reversal).

- Refund A refund is when funds are credited back to the customer’s card from a previously debited transaction. A refund could be processed when the customer returns previously purchased goods hence the funds which were settled to the merchant’s account need to move back to the cardholder’s account. Read more about Refunds [here](/guides/companion-apimanage-funds/#Loadadjustment).

- Chargeback A chargeback is the return of funds for a deduct transaction that was previously processed from a cardholder’s card balance, due to a successful dispute by the consumer regarding the transaction. Read about Chargeback related Dispute handling [here](/guides/disputes)
