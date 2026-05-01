# Issue cards

## With the Card API you can o ffer your customers two types of cards:

**Virtual card**A digital card without any physical components

**Physical card**
The traditional plastic payment card![Card API Issuing process flow](https://developer.sprint.paymentology.com/wp-content/uploads/2023/03/Card-API-issuing-process-flow-v2.png)

## 1. Issuing a virtual card

You can use the Card API to create a Virtual Card Number (VCN), which you can link to the unique customer reference number.

The VCN will then act as your customer’s identifier, which is useful if you want to manage or fund the card at a later stage. This means that you may not need to store the PAN number (Permanent Account Number) at all.

Once the API receives the request, it will create a 16-digit PAN number, CVV (Card Verification Value), and an expiry date — which are the constituents of the virtual card. You can then forward this information to your customer.

PAN number is a unique alphanumeric number (containing both alphabetical and numerical characters) used for identification purposes.

CVV is a static number similar to the separately-grouped numbers, usually three digits, found at the back of most physical debit and credit cards.

After the VCN has been linked to the customer’s store of value, they can instantly start transacting on any e-commerce site or application that accepts the chosen card association.

​You can also create and issue multiple virtual cards and label them differently to allow for easier management and identification.

You’ll need to make a call to the ​ CreateVirtualCard method ​​ to create a VCN.

## 2. Issuing a physical card​​

You can create and issue a physical card and send a request to Paymentology to link it to a unique customer reference number.​

You can decide to have one card linked per customer or multiple cards linked to a single customer.​

Once the card is linked, it is now ready to be funded and used as per the predefined use cases, like making ATM withdrawals, local and international online payments, point of sale transactions, or closed-loop network transactions.

​There are two options for issuing physical cards: Issue on-site and link immediately or issue with courier and link later

**Option 1: Issue on-site and link immediately**

You can use this option if you want the physical cards to be linked immediately, when they are bulk produced and stored on your end.

​You could have a batch of cards at the stores, branches, or agent facilities. Then, if someone requests a card, you can decide whether to apply a fee for this purchase.

After issuing the card, you’ll need to send a request to Paymentology, using the ​LinkCard method ​​, for the physical card to be linked to a unique customer reference number.

After issuing the card, you’ll need to send a request to Paymentology, using the ​LinkCard method ​​, for the physical card to be linked to a unique customer reference number.

**Option 2: Issue with courier and link later**

You can use this option if you want to order physical cards through your interface.

For example, if you want to use a courier delivery process or personalize a cardholder's name on the card, then this option could be for you.

Note: Since the card manufacturer may take a few days before completing the order, using this option does not allow the physical cards to be issued instantly.

For Option 2, you'll need to make a call to the OrderCard method, which allows you to use your interface to enter the cardholder's details, address, and their unique reference number.

Making this call will lead to the following:

- A PAN number file will be created and sent to the card manufacturer automatically.

- The card manufacturer will create the physical card and deliver it to the cardholder.

- The cardholder will need to activate and link the card using the ActivateCard and LinkCard API method.

**Note:**

For **virtual cards**: Multiple cards can be linked to one reference.

For **physical cards**: Only one reference can be linked to a card.

**A cardholder can have a virtual and a physical card linked to the same reference.**
