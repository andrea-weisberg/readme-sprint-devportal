# Manage funds

**Once a cardholder has been issued with a card, they can start to manage the funds associated with their card or pockets.**
​
These are the supported options for managing funds:​

- Loading funds onto the card

- Reversing the load

- Transferring funds between cards

- Reversing funds transferred between cards

- Transferring funds between pockets

- Reversing the pocket transfer

- Deducting funds from card or pocket

- Reversing the card deduction

- Devaluing a card or pocket

- Reversing the card's devalue

Let's look at each of them.

## 1. Loading funds onto the card​​

​You can load funds onto a card balance or a pocket (if you’ve opted for pockets). If you do not have pockets, then the funds will be loaded directly onto the card.​ If you’re loading the funds onto a pocket, then you’ll need to specify the target pocket’s UUID (universally unique identifier) number, which Paymentology provides.​

To carry out the loading of funds, the client manages a separate process that makes a debit from the store of value account and credits it to the card. ​It’s also possible to set limits that predefine the amount that can be loaded on the card.

You'll need to make a call to the LoadFunds method.

## 2. Reversing the load​

​If you want to reverse the loaded funds on the card, for any reason, and the funds have not been used, then you can initiate a reversal process.

You'll need to make a call to the LoadFundsReverse method.

## 3. Transferring funds between cards​​

​If there are cards issued within the same program, funds can be transferred between them easily.​ For example, if two people have cards from the same program, they can send each other funds easily.

You'll need to make a call to the TransferFunds method.

## ​4. Reversing funds transferred between cards​​

If you want to reverse the transferred funds, for any reason, and the funds have not been used, then you can initiate a reversal process.

You'll need to make a call to the​ TransferFundsReverse method.

## 5. Transferring funds between pockets​​

​You can transfer funds between pockets for the easy management of money. For example, you may want to transfer some funds from your expenditure pocket to your savings pocket.

You'll need to make a call to the​ PocketTransfer method.

## 6. Reversing the pocket transfer​​

​
If you want to reverse the funds transferred to a pocket, for any reason, and the funds have not been used, then you can initiate a reversal process.

You'll need to make a call to the​ PocketTransferReverse method.

## 7. Deducting funds from card or pocket​​

​If a cardholder wants to deduct funds from their card or pocket balances, then they can specify the value that needs to be deducted. The amount requested to be deducted must be equal or less than the balance; otherwise, the process will not be successful. After the deduction has been completed successfully, the client then credits the customer’s store of value account.

You'll need to make a call to the DeductFunds method.

## 8. Reversing the card deduction​ ​

​If you want to reverse the funds deducted, for any reason, then you can initiate a reversal process. ​Once successful, the balance will change based on the reversed amount.

You'll need to make a call to the ​ DeductFundsReverse method.

## ​9. Devaluing a card or pocket​​

​You can perform a deduction of the full amount available on the card or pocket. No partial amount will be removed from the card or pocket balances, but only all the funds.

You'll need to make a call to the ​Devalue method.

## 10. Reversing a devalue​​​

If you want to reverse the devaluing of funds from a card or pocket balance, for any reason, then you can initiate a reversal process. ​Once successful, the devalued amount will be credited to the card or pocket balance.

You'll need to make a call to the​ DevalueReverse method.
