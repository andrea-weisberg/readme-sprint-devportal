---
title: QMR data report
category:
  uri: Reports - Card API
slug: qmr-data-report
position: 23
parent:
  uri: reports
---

Paymentology's QMR (Quarterly Mastercard Report) data report contains transaction data and card/account data for the given quarter. The report can be provided to clients using Mastercard, to assist clients with their Mastercard quarterly reporting requirements.

The report includes the following:

### Cardholder activity

- **Purchases** - transaction count and volume of cleared transactions enacted to purchase goods or services.

- **Funding MCC 4829** - transaction count and volume of cleared funding transactions under MCC (Merchant Category Code) 4829 (Money Transfer)

- **Funding MCC 6540** - transaction count and volume of cleared funding transactions under MCC (Merchant Category Code) 6540 (Point of Interaction Funding Transactions)

- **Funding MCC 6538** - transaction count and volume of cleared funding transactions under MCC (Merchant Category Code) 6538 (MoneySend Funding)

- **Cash Disbursements** - transaction count and volume of cleared transactions enacted to withdraw cash either at an ATM, Branch, Teller, Balance Transfer or Convenience Check (used to obtain cash).

- **Breakdown of Cash Disbursements** - transaction count and volume of cleared transactions enacted to withdraw cash at an ATM and Teller.

- **Refunds/Returns/Credits** - total or partial refund of the amount of a previously cleared transaction for the return of unwanted goods or services. This can also be known as a reversal.

- **Payment Consumer** - transaction count and volume of cleared Money Send payment transactions identified as consumer initiated.

- **Payment Government** - transaction count and volume of cleared Money Send payment transactions identified as consumer initiated.

- **Payment Gaming Gambling** - transaction count and volume of cleared Money Send payment transactions identified as business or government initiated.

The Cardholder Activity section is split by the following:

- **Domestic On-us** - a cleared transaction made at a merchant within the issuing country and the Issuing Bank and Acquiring Bank are the same.

- **Domestic Other Brand/Non-Mastercard Processed** - a cleared transaction made at a merchant within the issuing country where the Issuing Bank and Acquiring Bank differ, Mastercard interchange is not applied, a competing domestic brand/scheme is on the card and present at the POS or ATM and the transaction is intentionally routed through the competing domestic brand/scheme.

- **Domestic Interchange** - a cleared transaction made at a merchant within the issuing country and the Issuing Bank and Acquiring Bank differ.

- **International** **Within Region** - a cleared transaction where the Issuing country and Acquiring country differ and both are in the EEA (European Economic Area).

- **International Outside Region** - a cleared transaction where either the Issuer **or** Acquirer is outside the EEA.

### Accounts/Cards

- **Accounts at beginning of quarter** - number of open and temporarily blocked accounts on the last day of the previous quarter.

- **New accounts obtained during quarter** - number of accounts added to the card program since the end of the previous quarter.

- **Accounts terminated during quarter** - number of accounts retired or expired since the end of the previous quarter.

- **Accounts at end of quarter** - number of open and temporarily blocked accounts on the last day of the reported quarter.

- **Accounts with at least one transaction during quarter** - number of accounts that made at least one transaction during the reported quarter.

- **Cards at beginning of quarter** - number of open and temporarily blocked cards on the last day of the previous quarter.

- **New cards** - number of cards added to the card program since the end of the previous quarter.

- **Cards at end of quarter** - number of open and temporarily blocked cards on the last day of the reported quarter.

- **Cards with at least one transaction during quarter** - number of cards that made at least one transaction during the reported quarter.

### Charged-Off Losses

Unless otherwise instructed by Paymentology, this data will be left blank or contain a 0. The data for this section is to be collated and reported by the client.

### Card Feature Details

- **Breakout of EMV-compliant Chip enabled Cards** - total number of cards at the end of the reported quarter that have the EMV-compliant Chip.

- **Total Mastercard contactless Cards issued** - total number of physical plastic contactless cards at the end of the reported quarter (both magstripe and EMV compliant contactless cards) and the associated transactions and volume on those cards and devices. Contactless cards use NFC technology.

- **Total number of Cards enrolled in the Mastercard Biometric Card program** - total number of physical Mastercard biometric cards in market. Biometric refers to fingerprint sensor-enabled payment cards.

- **Total number of Mastercard Digital Accounts** - total number of Mastercard Digital Accounts at the end of the reported quarter.

- **Total number of virtual, non-reloadable prepaid and full metal body cards** - total number of virtual, non-reloadable prepaid and full metal body cards at the end of the reported quarter. These types of cards do not have contactless capability.

## Report format

## Report time frame

## Report sample

Note: file will automatically download upon clicking link

[QMR_BIN_ClientName_YYYYQQ](https://developer.sprint.paymentology.com/wp-content/uploads/2025/01/QMR_BIN_ClientName_YYYYQQ.xls)
