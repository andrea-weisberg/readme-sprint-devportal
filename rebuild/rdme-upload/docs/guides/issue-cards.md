---
title: Issue cards
category:
  uri: Guides
slug: issue-cards
position: 22
---

## With the Paymentology Sprint Companion API, you can offer your customers different types of cards:

**A virtual card** - A digital card without any physical components

**A physical card**- The traditional plastic payment card.

**A [digital-first](/guides/digital-first) card** - A digital card which can be printed to plastic later. (Region specific)

## 1. Issuing a virtual card​ ​​

You can use the Companion API to create a Virtual Card Number (VCN), which you can link to the unique customer reference number.

If the API receives the request, it will create a 16-digit PAN (Permanent Account Number), CVV (Card Verification Value), and expiry date. You can then deliver this information to your customer.

![](https://developer.sprint.paymentology.com/wp-content/uploads/2023/03/How-to-issue-a-virtual-card-v2.png)

**PAN number** is the 16 digit card number printed on the front of a physical card, or the 16 digit virtual card number.

**CVV** is a static number similar to the separately-grouped numbers, usually three digits, found at the back of most physical debit and credit cards.

The VCN will be linked to your customer’s store of value. Customers can then start making transactions instantly on any e-commerce site or application that accepts the chosen card association.

You’ll need to make a call to the [CreateLinkedCard](/api-reference/companion-api/createlinkedcard) method to create a VCN.

## 2. Issuing a physical card​ ​

You can choose either of the following options for issuing a physical companion card: Issue on-site and link immediately or issue with courier and link later.

![](https://developer.sprint.paymentology.com/wp-content/uploads/2023/03/Physical-card-fulfilment-flow-v2.png)

### Option 1: Issue on-site and link immediately

You can use this option if you want the physical cards to be activated and linked immediately, when they are bulk produced and stored on your end.

You could have a batch of cards at the stores, branches, or agent facilities. Then, if someone requests a card, you can decide whether to apply a fee for this purchase.

When activating and linking the card, you’ll need to make a call to the [ActivateCard](/api-reference/companion-api/activatecard) method first to ensure the card is in an active state. Once the card is activated, you’ll need to send a request to Paymentology, using the [LinkCard](/api-reference/companion-api/linkcard) method, for the card to be linked to a unique customer reference number.

When activating and linking the card, you’ll need to make a call to the [ActivateCard](/api-reference/companion-api/activatecard) method first to ensure the card is in an active state. Once the card is activated, you’ll need to send a request to Paymentology, using the [LinkCard](/api-reference/companion-api/linkcard) method, for the card to be linked to a unique customer reference number.

![Companion API card issuing flow](https://developer.sprint.paymentology.com/wp-content/uploads/2023/03/Companion-card-issuing-flow-1-v2.png)

### Option 2: Issue with courier and link later

You can use this option if you want the physical cards to be ordered through your interface. You’ll find it useful if you’d like to use a courier delivery process or personalize a cardholder’s name on the card.

**Note:** Since it would take a few days for the card manufacturer to fulfill the order, using this option does not allow the cards to be issued instantly.

For Option 2, you’ll need to make a call to the [OrderCard](/api-reference/companion-api/ordercard) or [OrderCardWithPINBlock](/api-reference/companion-api/ordercardwithpinblock) methods, which allow you to use your interface to enter the cardholder´s details, address and unique reference number.

Making this call will lead to three results:

- Creates a PAN number file to send to the card manufacturer automatically

- Making the OrderCard call, a new PAN file will be created and automatically sent to the card manufacturer.

- Making the OrderCardWithPINBlock call, a new PAN file will be created and also sent to the card manufacturer, with the PIN of the card printed on the card carrier.

After the new card is created, you need to make the corresponding calls to **Link** that card to your customer´s reference number and **Activate** it to get it ready to use.

For both Option 1 and 2, you can decide to have one card linked per customer or multiple cards linked to one customer.

Once the card is activated and linked, it is now ready to be funded and used as per the predefined use cases, such as making ATM withdrawals, local and international online payments, point of sale transactions, or closed loop network transactions.

## 3. Issuing a [digital-first](/guides/digital-first) card

Digital-first cards are available with Mastercard or Visa and currently available in select regions. The cards are issued similarly as a virtual card where you can use Companion API to create a Virtual Card Number (VCN) as described in the section Issuing a Virtual Card. To print it later, you can follow the steps below:

### Step 1: PrintLinkedCard

You can use this option if you want the existing digital first cards to be printed.

When printing the card, you'll need to make a call to either [PrintLinkedCard](/api-reference/companion-api/printlinkedcard) OR [PrintLinkedCardWithPINBlock](/api-reference/companion-api/printlinkedcardwithpinblock) method first to ensure that card is sent for printing.

**Note:**Since it would take a few days for the card manufacturer to fulfill the order, using this option does not allow the cards to be issued instantly.

### Step 2: ToggleVoucherFeature

You can use this option if you want the printed digital-first cards to be used at POS terminals.

For step 2, you'll need to make a call to the [ToggleVoucherFeature](/api-reference/companion-api/togglevoucherfeature) method, which allows you to use your interface to enable usage at POS terminals using a unique reference number.

**Note:**Since it would take a few days for the card manufacturer to fulfill the order, using step 2 should be done one day after step 1.
