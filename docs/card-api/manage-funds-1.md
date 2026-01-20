---
title: Manage funds
deprecated: false
hidden: false
metadata:
  robots: index
---
# How to manage funds

**Once a cardholder has been issued with a card, they can start to manage the funds associated with their card or pockets.**
​
These are the supported options for managing funds:​

* Loading funds onto the card
* Reversing the load
* Transferring funds between cards
* Reversing funds transferred between cards
* Transferring funds between pockets
* Reversing the pocket transfer
* Deducting funds from card or pocket
* Reversing the card deduction
* Devaluing a card or pocket
* Reversing the card’s devalue

Let’s look at each of them.

***

# 1. Loading funds onto the card​​

You can load funds onto a card balance or a pocket (if you’ve opted for pockets). If you do not have pockets, then the funds will be loaded directly onto the card.​ If you’re loading the funds onto a pocket, then you’ll need to specify the target pocket’s UUID (universally unique identifier) number, which Paymentology provides.​

To carry out the loading of funds, the client manages a separate process that makes a debit from the store of value account and credits it to the card. ​It’s also possible to set limits that predefine the amount that can be loaded on the card.

You’ll need to make a call to the LoadFunds method.

<br />
