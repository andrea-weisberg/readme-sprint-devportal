---
title: QVR data report
category:
  uri: Reports
slug: companion-api-qvr-data-report
position: 13
parent:
  uri: companion-api-reports
---

The QVR data report can be provided to clients using Visa. It contains data to assist clients with their Visa quarterly reporting requirements. The report includes the following:

### Category definitions

- **On Us** - is when the issuer and acquirer of the transaction is the same member and the transaction was made at a merchant within the issuing country/region.

- **National** - is when the transaction was made at a merchant within the issuing country/region and the issuer and acquirer are different.

- **International** - is when the transaction was made at a merchant outside of the issuing country/region.

- **Debit Classic** - only applicable for debit classic campaigns.

### Cardholder activity

The report includes the Cardholder Activity data for **On Us**, **National**, **International** and **Debit Classic**. This data includes:

- **Payments - Card Present**- this is the count and volume of successful payments/purchase transactions within the period where the card was considered as present.

- **Payments - Card Not Present** - this is the count and volume of successful payments/purchase transactions within the period where the card was considered as not present.

- **ATM Cash Advances** - this is the count and volume of successful cash withdrawal transactions made at an ATM within the period.

- **Manual Cash** - this is the count and volume of successful cash withdrawal transactions made via a teller or not at an ATM within the period.

- **Account funding transaction**- this is the count and volume of successful transactions considered as an account funding transaction within the period.

- **Original Credits** - this is the count and volume of successful transactions considered as an original credit transaction within the period.

- **Cashback**- this is the count and volume of successful transactions considered as a cashback transaction within the period.

### Card/account data:

In addition to the above the following Card/Account data is provided:

- **Total Number of Cards** - this is the total number of cards that are issued on the program. This includes cards that are temporarily blocked and excludes those that have been terminated/retired or closed (i.e. the card cannot return to an active state).

- **Number of Cards - Magnetic Stripe** - this is the number of cards that are issued with magnetic stripe only functionality. This includes cards that are temporarily blocked and excludes those that have been terminated/retired or closed (i.e. the card cannot return to an active state).

- **Number of Cards - Magnetic Stripe, Chip** - this is the number of cards that are issued with magnetic stripe & chip functionality only. This includes cards that are temporarily blocked and excludes those that have been terminated/retired or closed (i.e. the card cannot return to an active state).

- **Number of Cards - Magnetic Stripe, Contactless** - this is the number of cards that are issued with magnetic stripe & contactless functionality only. This includes cards that are temporarily blocked and excludes those that have been terminated/retired or closed (i.e. the card cannot return to an active state).

- **Number of Cards - Magnetic Stripe, Chip, Contactless** - this is the number of cards that are issued with magnetic stripe, chip & contactless functionality. This includes cards that are temporarily blocked and excludes those that have been terminated/retired or closed (i.e. the card cannot return to an active state).

- **Total Number of Active Cards** - this is the number of cards that have made at least 1 transaction during the time period.

- **Total Number of Active Cards - used at Contactless device** - this is the number of cards that have made at least 1 transaction via a contactless device during the time period.

- **Number of Accounts - Domestic use Only** - this is the number of accounts that are only capable of transacting within the issuing country.

- **Number of Accounts - International enabled** - this is the number of accounts that are capable of transacting outside the issuing country.

- **Payments Transactions Declined for Insufficient Funds - Count** - this is the number of payments transactions that were attempted but declined due to insufficient funds.

- **Cash Transactions Declined for Insufficient Fund - Count** - this is the number of cash transactions that were attempted but declined due to insufficient funds.

## Report format

## Report time frame

## Report sample

Note: file will automatically download upon clicking link

[QVR_SRE[SRE]_[YYYYMMDD]-[YYYYMMDD].xls](https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/QVR_SRE-SRE_YYYYMMDD-YYYYMMDD.xls)
