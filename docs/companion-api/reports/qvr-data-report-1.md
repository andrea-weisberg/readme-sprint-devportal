---
title: QVR data report
deprecated: false
hidden: false
metadata:
  robots: index
---
The QVR data report can be provided to clients using Visa. It contains data to assist clients with their Visa quarterly reporting requirements.

### Category definitions

* **On Us** – when the issuer and acquirer of the transaction is the same member and the transaction was made at a merchant within the issuing country/region.
* **National** – when the transaction was made at a merchant within the issuing country/region and the issuer and acquirer are different.
* **International** – when the transaction was made at a merchant outside of the issuing country/region.
* **Debit Classic** – only applicable for debit classic campaigns.

### Cardholder activity

The report includes Cardholder Activity data for **On Us**, **National**, **International**, and **Debit Classic**. This data includes:

* **Payments – Card Present** – count and volume of successful payments/purchase transactions where the card was present.
* **Payments – Card Not Present** – count and volume of successful payments/purchase transactions where the card was not present.
* **ATM Cash Advances** – count and volume of successful ATM cash withdrawal transactions.
* **Manual Cash** – count and volume of successful cash withdrawals not made via an ATM (e.g. via teller).
* **Account funding transaction** – count and volume of successful transactions considered as account funding.
* **Original Credits** – count and volume of original credit transactions.
* **Cashback** – count and volume of successful cashback transactions.

### Card/account data

In addition to the above, the following card/account data is provided:

* **Total Number of Cards** – total issued cards, including temporarily blocked (excluding terminated/retired/closed cards).
* **Number of Cards – Magnetic Stripe** – cards issued with magnetic stripe only.
* **Number of Cards – Magnetic Stripe, Chip** – cards issued with magnetic stripe and chip only.
* **Number of Cards – Magnetic Stripe, Contactless** – cards issued with magnetic stripe and contactless only.
* **Number of Cards – Magnetic Stripe, Chip, Contactless** – cards with all three: magnetic stripe, chip, and contactless.
* **Total Number of Active Cards** – cards that made at least one transaction during the reporting period.
* **Total Number of Active Cards – used at Contactless device** – cards used at least once at a contactless device.
* **Number of Accounts – Domestic use Only** – accounts capable of transacting only within the issuing country.
* **Number of Accounts – International enabled** – accounts capable of transacting internationally.
* **Payments Transactions Declined for Insufficient Funds – Count** – number of payments declined due to insufficient funds.
* **Cash Transactions Declined for Insufficient Funds – Count** – number of cash transactions declined due to insufficient funds.

## Report format

## Report time frame

## Report sample

[QVR_SRE[SRE]_[YYYYMMDD]-[YYYYMMDD].xls](https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/QVR_SRE-SRE_YYYYMMDD-YYYYMMDD.xls)
