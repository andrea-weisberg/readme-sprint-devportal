---
title: Companion API
category:
  uri: Guides
slug: companion-api-guide
position: 10
---

## Companion API is a simple API that allows you to issue cards and hold your customers' card balances on your platform

**A Companion card is a card that is linked to a store of value (SVA) like a wallet or a bank account. What makes this API different from the others we offer, is that the customer's card balance sits within the SVA and not on the card. Choose the Companion API if you want to issue cards and hold your customers' card balances on your own platform.**

With this API, you can issue physical and virtual prepaid cards linked to a separate SVA. Cards are linked to the SVA, so whenever transactions are made, the SVA is debited.

**Note:** You’ll be responsible for authorising transactions with this API.

If you want Paymentology to hold your customer’s balance for you, use the [Card API](/guides/card-api) instead. If you're not sure which API to choose, read about [our APIs](/guides/our-apis) first or [get in touch](/guides/contact-us).

Choose the Companion API if you want to:

Store your customers’ account balances on your platform and be responsible for authorising transactions

Issue your own virtual and physical cards instantly

Connect your customers to an open-loop environment with just one integration

Give your cardholders access to the global open-loop world of payments so that they can transact securely anywhere 24/7

Empower customers who don’t qualify for a credit card or bank account with a virtual or physical card that they can use to shop online

The Companion API is split into two separate APIs based on whether we are calling you (we call it **Remote API**), or you're calling us (**Local API**):

**Local API - you call us**

- This API allows you to call us to perform necessary actions on your cards

- It contains all the API methods you will need e.g. linking a card to the SVA or updating cardholder details

- It is hosted by Paymentology

**Remote API - we call you**

- This API allows us to call you to perform actions on your SVA/wallet e.g. Deducting/loading funds, balance inquiries, etc.

- It is hosted by you

![Companion transaction processing flow](https://developer.sprint.paymentology.com/wp-content/uploads/2023/03/Companion-Transaction-processing-v2-1.png)

#### Find out how to use the Companion Card API to:

- [Issue cards](/guides/issue-cards)

- [Manage cards](/guides/manage-cards)

- [Secure cards](/guides/secure-cards)

- [Manage funds](/guides/manage-funds)

- [Send messages](/guides/messages)

- [Make Tokenized payments](/guides/tokenization2)

- [Generate reports](/reports/companion-api/reports)
