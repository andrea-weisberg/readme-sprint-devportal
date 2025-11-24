---
title: Issue cards
deprecated: false
hidden: false
metadata:
  robots: index
---

## With the Card API you can offer your customers two types of cards:

**Card-API-issuing-process-flow-v2.png IMAGE GOES HERE.**

## 1. Issuing a virtual card

You can use the Card API to create a Virtual Card Number (VCN), which you can link to the unique customer reference number.

The VCN will then act as your customer’s identifier, which is useful if you want to manage or fund the card at a later stage. This means that you may not need to store the PAN number (Permanent Account Number) at all.

Once the API receives the request, it will create a 16-digit PAN number, CVV (Card Verification value), and an expiry date — which are the constituents of the virtual card. You can then forward this information to your customer.

After the VCN has been linked to the customer’s store of value, they can instantly start transacting on any e-commerce site or application that accepts the chosen card association.

You can also create and issue multiple virtual cards and label them differently to allow for easier management and identification.

## <a name="#physical" />2. Issuing a physical card

You can create and issue a physical card and send a request to Paymentology to link it to a unique customer reference number.

You can decide to have one card linked per customer or multiple cards linked to a single customer.

Once the card is linked, it is now ready to be funded and used as per the predefined use cases, like making ATM withdrawals, local and international online payments, point of sale transactions, or closed-loop network transactions.

There are two options for issuing physical cards: Issue on-site and link immediately or issue with courier and link later

Making this call will lead to the following:

* A PAN number file will be created and sent to the card manufacturer automatically.
* The card manufacturer will create the physical card and deliver it to the cardholder.
* The cardholder will need to activate and link the card using the ActivateCard and LinkCard API method.
