---
title: AFD Transactions
deprecated: false
hidden: false
metadata:
  robots: index
---

Automated Fuel Dispensers (AFD) are unattended terminals at fuel stations that allow cardholders to purchase fuel without requiring an attendant. The emergence of AFD transactions has revolutionized the fuel purchase industry and greatly benefitted both merchants and customers.

In the past, fueling was a tedious process—an attendant had to manually pump the requested amount of fuel, usually resulting in lines and customer queues. However, AFDs have turned this around—no more direct engagements with staff and other time-consuming hassles.

With Paymentology Sprint’s support for AFD transactions, you can make payments for your cardholders at the pump painless, fast, and secure.

## **Benefits of AFD Transactions**

* **Speeds up fueling for customers**
  At unattended terminals, a customer can quickly and conveniently obtain fuel without the time-consuming hassle of having to wait to be served. A customer can simply tap, dip, or swipe their card without the manual process of engaging an attendant.

* **Enhances customer experience**
  AFDs offer a convenient way for drivers to gas up and get back on the road without the usual fueling hassles. This streamlined experience results in customer loyalty and more business to merchants.

* **Reduces costs**
  Although AFDs require an initial capital cost to install and set up, they can reduce operational costs in the long run. Their automated nature implies that personnel costs are minimal.
  The convenience of AFDs also enables customers not to waste time and fuel—which equals money—when fueling their vehicles.

* **Increases purchase sizes**
  Since AFDs allow customers to use their payment cards, which could be directly connected to their deposit and line-of-credit accounts, they reduce the chances of abandoning payments. Merchants do not need to worry about customers not having enough cash in their wallets.

* **Lowers theft possibilities**
  The traditional way of using cash at fuel outlets is prone to employee theft, robbery, or unintentional miscounting. By eliminating cash, this risk is drastically reduced.

## **Best Practices For AFD Transactions**

* Ensure all purchase transactions are properly authorized. Remember that the available authorization methods vary based on the merchant type and region.
* Ensure that any approved amount that was not settled is promptly reversed. This would avert any cardholder account holds and/or unnecessary potential fees.
* Ensure estimated transactions are handled appropriately. If the final amount surpasses the estimated amount, you should obtain additional authorization. Remember that the confirmation advice or the settlement should never be higher than the initial authorization amount sent from the AFD POS.

## AFD Transactions Flow

**AFD-Transaction-processing-v2.png IMAGE GOES HERE.**

1. Cardholder makes a transaction at an AFD POS
2. POS sends an authorization request to a card scheme
3. Card scheme sends an authorization to Paymentology
4. Paymentology sends payment authorization to a wallet provider
5. Wallet provider accepts or rejects the transaction based on the availability of funds
6. If the wallet accepts successfully, confirmation advice is passed from AFD POS to the card scheme. If the wallet declines, the decline reason response will be sent
7. AFD POS device passes confirmation to the card scheme. Card scheme sends confirmation advice to Paymentology
8. Paymentology processes the confirmation advice and checks if there is a pending balance from the original authorization
9. Paymentology sends a reversal to the wallet provider for the balance of the original pre-authorization amount.
