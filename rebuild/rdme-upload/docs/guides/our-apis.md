---
title: Our APIs
category:
  uri: Guides
slug: our-apis
position: 34
---

**Paymentology's Sprint product provides simple, seamless, and scalable API integration solutions that enable quick and easy implementation and management of your card programs. We act as a payment enabler between card schemes like Mastercard, Visa, and Union Pay and your closed-loop wallet platform. Through our APIs, we are able to connect you with the card scheme of your choice, shielding you from all the complexities necessary for direct integration, so that you can focus on your business.**

We offer four main APIs:

Companion
API

Card
API

QR Payments
API

Transaction
Stream

Discover which one is right for you.

## 1. [Companion API](/guides/companion-api)

A Companion card is a card that is linked to a store of value (SVA) like a wallet or a bank account.

What makes this API different from the other APIs we offer is that the customer’s card balance sits within the SVA and not on the card. This means that you hold the customer's balance on your own platform.

With this API, you can issue physical and virtual prepaid cards linked to a separate SVA. Cards are linked to the SVA, so whenever transactions are made, the store of value is debited. Paymentology is the payment processor that manages all transactions against a centralized store of value (SVA). **You’ll be responsible for authorizing transactions with this API.**

Transactions may use open-loop accounts like debit and credit cards, and closed-loop cards, like gift tokens or airtime vouchers. Companion cards allow individuals the flexibility to perform a wide range of transactions – from merchant payments to cash withdrawals to eCommerce to P2P transfers – all using their mobile wallet. You can generate pre-loaded Companion cards based on a customer’s SVA balance.

Choose the Companion API if you want to:

Issue cards and hold your customers’ card balances on your own platform

Maintain your customers' balance and be responsible for authorizing transactions

Issue virtual and physical cards yourself

Promote brand awareness, engage new customers and increase brand loyalty

Grow your business in the mobile money ecosystem

Provide more accessible services to unbanked customers in developing economies or customers with no credit ranking

Maximize the ability to integrate closed and open loop products and services

Let your customers do more with their mobile money accounts - like perform merchant payments, P2P payments, transact online and make ATM withdrawals

Open up the world of e-commerce to your customers

Learn more about [Companion API!](/guides/companion-api)

## 2. [Card API](/guides/card-api)

The Card API is a prepaid card management interface that enables you to instantly generate and issue virtual and/or physical cards. These cards are funded from a stored value account (SVA) and are loaded as a balance on the card.

The Card API is different from the Companion API in that Paymentology stores the customer’s balance and we are responsible for authorizing transactions based on the stipulated card balances and limits.

With this API, you can provide anything from simple gift cards to multi-currency cards for travelling, payout and payroll cards or general-purpose reloadable cards for the unbanked, and many other types of secure payment cards. It offers a prepaid card and pocket management solution that acts as a link between Mastercard, Visa, Union Pay International, bank switches, and all kinds of reloadable customer cards.

Choose the Card API if you want to:

Have Paymentology manage your customers' card balances and authorize card transactions

Issue virtual and physical cards yourself

Load and deduct funds from a customer's pre-funded account

Onboard customers who don’t have access to traditional banking facilities or a strong credit rating

Integrate customers with traditional open-loop cards, such as Mastercard, Visa and Union Pay

Offer 3D Secure functionality, view card balances and add pockets to your customers' accounts

Learn more about [Card API!](/guides/card-api)

## 3. [QR Payments API](/guides/qr-payments-api)

The QR Payments API allows you to create a **contactless merchant payment system** where customers can make electronic payments by scanning a QR code from a smartphone application. It’s a simple and secure way for consumers to push payments to merchants using their mobile money wallets or bank account balances.

**Paymentology's Sprint product allows integration into Mastercard QR** and **Visa QR** for the issuing and acceptance of QR payments, offering a safe, innovative way for consumers to scan and pay. Where businesses don’t have the infrastructure or finances to purchase expensive in-a-box software, the QR Payments API provides a customizable solution, which mitigates the steep cost of specialized PoS hardware and alleviates the time delay between purchase and payment often associated with using bank cards. Money is transferred directly from their mobile account to merchant, no POS terminal needed, in a single transaction.

Unlike barcodes, which they loosely resemble, QR codes can store URLs, geographic coordinates, and text.

**The benefits of QR payments**

- Customers can make cashless payments using their smartphones without needing bank accounts or physical plastic cards.

- Low cost to issue digital products.

- QR payments are instant, safe, and secure.

The QR Payments API is ideal for:

Small shops with limited POS resources

Mobile payments on-the-go, e.g. at outdoor events

Promoting products, events and services

Providing business information to new customers

Customers without traditional bank accounts wanting to purchase goods and services

Ecommerce and other online transactions

Learn more about [QR Payments API!](https://developer.sprint.paymentology.com/digital-api/)

## 4. [Transaction Stream](/guides/notifications)

The Transaction Stream service allows API consumers to receive real-time notifications of the undertaken transactions. By subscribing to the notification service, consumers can know the status of transactions in real-time.

It enables you to receive real-time transaction information for the following types of transactions:

- Successful transactions

- Reversed transactions

- Verified transactions

- Declined transactions

You can get the following information for each undertaken transaction:

- Customer reference account number

- Transaction time and date

- Merchant name

- Decline reason code

- Transaction amount

- MCC (Merchant Category Code)

You can use the Transaction Stream to:

Customize customer transaction notifications

Track payment declines and notify customers to improve their awareness

Monitor fraudulent transactions to mitigate your liability

Create targeted promotional messages

Quickly review customer spending patterns by time period

Receive real-time transaction information for successful, reversed, verified and declined transactions

## What should the Transaction Stream be used for?

Any activities or notifications that can benefit from real time transaction monitoring and alerting. For example:

- Customizing customer transaction notifications

- Tracking payment declines and notifying customers to improve their awareness

- Monitoring fraudulent transactions to mitigate your liability

- Creating targeted promotional messages

- Quickly reviewing customer spending patterns by time period

## What should the Transaction Stream not be used for?

Because of the transient nature of the transaction stream, and the fact that delivery is not guaranteed, the stream cannot be used for any purposes that require complete and accurate information. This includes:

- Any kind of financial reconciliation

- Any kind of data reporting/ financial reporting
