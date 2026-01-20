---
title: Secure cards
deprecated: false
hidden: false
metadata:
  robots: index
---
# How to secure your cards

**The Sprint Card API allows you to access a wide range of features to ensure the security of card transactions.**

Here are the main features to use to ensure the security of your cards:

* Dynamic secure code on virtual cards
* Dynamic CVV on virtual cards
* PIN on physical cards
* Adding pockets to your card

Let’s look at each of them.

***

# 1. Using a dynamic secure code on virtual cards​​

A dynamic secure code allows you to increase the security of your virtual cards. If you add a dynamic secure code, it will be required at the time of making any transaction, enhancing payments security and safeguarding against fraud.
​
The secure code is what Mastercard refers to as 3D Secure, and Visa refers to it as Visa Secure (formerly Verified by Visa (VbV)). To secure your virtual card with a dynamic secure code, you’ll need to make a call to the `AdministrativeMessage` method.
​
Then, a One Time PIN (OTP), which is triggered by the `OTPRequest` method, will be delivered to the cardholder to enable them to complete the secure code process and finalize the transaction.

***

# 2. Using a dynamic CVV on virtual cards​

​The Card Verification Value (CVV), which comes with every virtual card, is an essential feature for improving security. This static number helps in validating the identity of the cardholder, ensuring the card cannot be used for making fraudulent transactions.
​
And if you intend to revamp the security of a virtual card, or if a cardholder suspects their CVV has been compromised, you can simply update the CVV.
​
To update the CVV, you’ll need to make a call to the `UpdateCVV` method. Paymentology will then create a new CVV that you can send to your cardholder.

***

# 3. Using a PIN on physical cards​

​A PIN (personal identification number) is required to perform all ATM transactions. A secret PIN verifies a user’s identity and allows them to perform secure transactions. Apart from managing the transactions on the card, Paymentology will also manage its PIN. The PIN can either be pre-printed in a tamper-proof package containing the card or it can be set when the card is linked/issued.
​
If the card PIN needs to be set for the first time or changed at a later time, or if the customer forgets it or requests it to be changed, you’ll need to make a call to the ​`ChangePIN` method. After the API request has been completed, Paymentology will issue a new PIN.

***

# 4. Adding pockets to your card

​Although the ability to add multiple pockets may not be suitable for everyone, this feature allows you to enhance the versatility and security of your card. You will have your main Permanent Account Number (PAN) as your “control” card and multiple pockets that sit under this with different balances.
​
Pockets are a useful feature to help customers manage their money.  Different pockets can be set up, like for example multiple currency pockets, savings pockets, expenditure pockets, or lifestyle pockets. Each pocket comes with its own balance management system, which also enhances its security.
​
To add multiple pockets to your card, you’ll need to make a call to the ​`AddPocket` method​.
