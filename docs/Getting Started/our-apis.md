---
title: Our APIs
deprecated: false
hidden: false
metadata:
  robots: index
---
**Paymentology’s Sprint product provides simple, seamless, and scalable API integration solutions that enable quick and easy implementation and management of your card programs. We act as a payment enabler between card schemes like Mastercard, Visa, and Union Pay and your closed-loop wallet platform. Through our APIs, we are able to connect you with the card scheme of your choice, shielding you from all the complexities necessary for direct integration, so that you can focus on your business.**

{/* Section intro */}

<p
  style={{
    margin: '8px 0 24px 0',
    fontSize: '16px',
    fontWeight: 500,
    color: '#4A5A6A',
  }}
>
  We offer four main APIs, discover which one is right for you:
</p>

{/* 2x2 API tiles (HTML/JSX version) */}

<div
  style={{
    display: 'grid',
    gridTemplateColumns: 'repeat(2, 1fr)',
    gap: '24px',
    margin: '0 0 32px 0',
  }}
>
  {/* Companion API */}

  <a
    href="companian-api.md"
    style={{
      background: '#F3FBF8',
      borderRadius: '16px',
      padding: '32px',
      textDecoration: 'none',
      color: 'inherit',
      display: 'block',
      minHeight: '220px',
    }}
  >
    <div
      style={{
        width: '64px',
        height: '64px',
        background: '#9ADBC0',
        borderRadius: '16px',
        marginBottom: '56px',
      }}
    />

    <h3 style={{ margin: 0, fontSize: '32px', lineHeight: '36px' }}>
      Companion<br />API
    </h3>
  </a>

  {/* Card API */}

  <a
    href="card-api.md"
    style={{
      background: '#EDF9F5',
      borderRadius: '16px',
      padding: '32px',
      textDecoration: 'none',
      color: 'inherit',
      display: 'block',
      minHeight: '220px',
    }}
  >
    <div
      style={{
        width: '64px',
        height: '64px',
        background: '#9ADBC0',
        borderRadius: '16px',
        marginBottom: '56px',
      }}
    />

    <h3 style={{ margin: 0, fontSize: '32px', lineHeight: '36px' }}>
      Card<br />API
    </h3>
  </a>

  {/* QR Payments API */}

  <a
    href="qr-payments-api.md"
    style={{
      background: '#F3FBF8',
      borderRadius: '16px',
      padding: '32px',
      textDecoration: 'none',
      color: 'inherit',
      display: 'block',
      minHeight: '220px',
    }}
  >
    <div
      style={{
        width: '64px',
        height: '64px',
        background: '#9ADBC0',
        borderRadius: '16px',
        marginBottom: '56px',
      }}
    />

    <h3 style={{ margin: 0, fontSize: '32px', lineHeight: '36px' }}>
      QR Payments<br />API
    </h3>
  </a>

  {/* Transaction Stream */}

  <a
    href="transaction-stream.md"
    style={{
      background: '#EDF9F5',
      borderRadius: '16px',
      padding: '32px',
      textDecoration: 'none',
      color: 'inherit',
      display: 'block',
      minHeight: '220px',
    }}
  >
    <div
      style={{
        width: '64px',
        height: '64px',
        background: '#9ADBC0',
        borderRadius: '16px',
        marginBottom: '56px',
      }}
    />

    <h3 style={{ margin: 0, fontSize: '32px', lineHeight: '36px' }}>
      Transaction<br />Stream
    </h3>
  </a>
</div>

***

<br />

## 1. [Companion API](https://developer.sprint.paymentology.com/companion-api/)

A Companion card is a card that is linked to a store of value (SVA) like a wallet or a bank account.

With this API, you can issue physical and virtual prepaid cards linked to a separate SVA. Cards are linked to the SVA, so whenever transactions are made, the store of value is debited. Paymentology is the payment processor that manages all transactions against a centralized store of value (SVA). **You’ll be responsible for authorizing transactions with this API.**

Transactions may use open-loop accounts like debit and credit cards, and closed-loop cards, like gift tokens or airtime vouchers. Companion cards allow individuals the flexibility to perform a wide range of transactions – from merchant payments to cash withdrawals to eCommerce to P2P transfers – all using their mobile wallet. You can generate pre-loaded Companion cards based on a customer’s SVA balance.

## 2. [Card API](https://developer.sprint.paymentology.com/card-api/)

The Card API is a prepaid card management interface that enables you to instantly generate and issue virtual and/or physical cards. These cards are funded from a stored value account (SVA) and are loaded as a balance on the card.

With this API, you can provide anything from simple gift cards to multi-currency cards for travelling, payout and payroll cards or general-purpose reloadable cards for the unbanked, and many other types of secure payment cards. It offers a prepaid card and pocket management solution that acts as a link between Mastercard, Visa, Union Pay International, bank switches, and all kinds of reloadable customer cards.

## 3. [QR Payments API](../qr-payments-api)

The QR Payments API allows you to create a **contactless merchant payment system** where customers can make electronic payments by scanning a QR code from a smartphone application. It’s a simple and secure way for consumers to push payments to merchants using their mobile money wallets or bank account balances.

**Paymentology’s Sprint product allows integration into Mastercard QR** and **Visa QR** for the issuing and acceptance of QR payments, offering a safe, innovative way for consumers to scan and pay. Where businesses don’t have the infrastructure or finances to purchase expensive in-a-box software, the QR Payments API provides a customizable solution, which mitigates the steep cost of specialized PoS hardware and alleviates the time delay between purchase and payment often associated with using bank cards. Money is transferred directly from their mobile account to merchant, no POS terminal needed, in a single transaction.

Unlike barcodes, which they loosely resemble, QR codes can store URLs, geographic coordinates, and text.

**The benefits of QR payments**

* Customers can make cashless payments using their smartphones without needing bank accounts or physical plastic cards.
* Low cost to issue digital products.
* QR payments are instant, safe, and secure.

## 4. [Transaction Stream](https://developer.sprint.paymentology.com/notifications/)

The Transaction Stream service allows API consumers to receive real-time notifications of the undertaken transactions. By subscribing to the notification service, consumers can know the status of transactions in real-time.

It enables you to receive real-time transaction information for the following types of transactions:

* Successful transactions
* reversed transactions
* Verified transactions
* Declined transactions

You can get the following information for each undertaken transaction:

* Customer reference account number
* Transaction time and date
* Merchant name
* Decline reason code
* Transaction amount
* MCC (Merchant Category Code)

## What should the Transaction Stream be used for?

Any activities or notifications that can benefit from real time transaction monitoring and alerting. For example:

* Customizing customer transaction notifications
* Tracking payment declines and notifying customers to improve their awareness
* Monitoring fraudulent transactions to mitigate your liability
* Creating targeted promotional messages
* Quickly reviewing customer spending patterns by time period

## What should the Transaction Stream not be used for?

Because of the transient nature of the transaction stream, and the fact that delivery is not guaranteed, the stream cannot be used for any purposes that require complete and accurate information. This includes:

* Any kind of financial reconciliation
* Any kind of data reporting/ financial reporting
