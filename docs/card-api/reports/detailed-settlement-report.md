---
title: Detailed settlement report
deprecated: false
hidden: false
metadata:
  robots: index
---

Paymentology also provides a detailed version of the summary Settlement Report.  
The Detailed Settlement Report shows each settled transaction, which allows you to use the Transaction ID to mark off settled transactions from authorized transactions. This also assists in confirming the values of the amounts in the summary Settlement Report. The network provides the Transaction ID field during authorization. The same Transaction ID for authorizations is included in the Detailed Settlement Report.

There are 3 versions of this report available:  
[Version 1.0](#DSRV1)  
[Version 2.0](#DSRV2.0)  
[Version 2.1](#DSRV2.1)

The report includes the following details:

### Version 1.0 {#DSRV1}

Contains the Chargeback report.

- **Transactions date** – this is the settlement date of the transaction.
- **The amount in the issuing currency (cardholder currency)** – the actual amount is a decimal number.
- **The amount in the settlement currency** – the amount passed over by the network. Multiply by 100 to include cents. If the settlement currency does not have decimals, take the value as-is.
- **Transaction narrative** – the merchant’s description.
- **Transaction description** – describes the transaction type:
  - Deduct – shows all deductions at the time of settlement.
  - Load – shows refunds.
  - Chargeback – gives positive or negative amounts for chargebacks.
- **Transaction ID** – reference for the transaction:
  - Usually 7–10 digits, same as the original authorization.
  - Refunds: unique ID, not related to the original authorization, up to 23 characters.
  - Chargebacks: unique ID, not related to the original authorization, up to 23 characters.
- **Currency code** – settlement currency code.
- **Transaction types** – 00 (POS), 01 (ATM), 02 (adjustment).
- **Wallet reference** – empty for Card API reporting.
- **System date** – Paymentology’s system date in UTC +2.
- **Sequence number** – unique sequence card identifier for created cards.
- **Tracking number** – unique 15-digit tracking identifier for the card.
- **Settlement currency** – currency code for the settlement currency.
- **Interchange amount** – individual amounts earned per transaction.

### Version 2.0 {#DSRV2.0}

Does not contain the Chargeback record (see Transaction Description column).

- **Transactions date** – settlement date of the transaction.
- **The amount in the issuing currency (cardholder currency)** – decimal number.
- **The amount in the settlement currency** – amount from the network, multiply by 100 for cents if needed.
- **Transaction narrative** – merchant’s description.
- **Transaction description** – describes the transaction type:
  - Deduct – shows all deductions at the time of settlement.
  - Load – shows refunds.
- **Transaction ID** – reference for the transaction:
  - Usually 7–10 digits, same as the original authorization.
  - Refunds: unique ID, up to 23 characters.
  - Chargebacks: unique ID, up to 23 characters.
- **Currency code** – settlement currency code.
- **Transaction types** – 00 (POS), 01 (ATM), 02 (adjustment).
- **Wallet reference** – empty for Card API reporting.
- **System date** – Paymentology’s system date in UTC +2.
- **Sequence number** – unique sequence card identifier.
- **Tracking number** – unique 15-digit tracking identifier for the card.
- **Settlement currency** – currency code for settlement currency.
- **Interchange amount** – amounts earned per transaction.

### Version 2.1 {#DSRV2.1}

Builds off V2.0 and does not contain the Chargeback record.  
Changes include additional information in the **TransactionNarrative** column delimited by pipes, e.g. `TransactionNarrative|AdditionalTraceRef|CustomIdentifier`.

- **Transactions date** – settlement date of the transaction.
- **The amount in the issuing currency (cardholder currency)** – decimal number.
- **The amount in the settlement currency** – amount from the network, multiply by 100 for cents if needed.
- **Transaction narrative|AdditionalTraceRef|CustomIdentifier** – merchant’s description with appended identifiers.
- **Transaction description** – describes the transaction type:
  - Deduct – shows all deductions at the time of settlement.
  - Load – shows refunds.
- **Transaction ID** – reference for the transaction:
  - Usually 7–10 digits, same as the original authorization.
  - Refunds: unique ID, up to 23 characters.
  - Chargebacks: unique ID, up to 23 characters.
- **Currency code** – settlement currency code.
- **Transaction types** – 00 (POS), 01 (ATM), 02 (adjustment).
- **Wallet reference** – empty for Card API reporting.
- **System date** – Paymentology’s system date in UTC +2.
- **Sequence number** – unique sequence card identifier.
- **Tracking number** – unique 15-digit tracking identifier.
- **Settlement currency** – settlement currency code.
- **Interchange amount** – amounts earned per transaction.

## Report format

## Report time frame

## Report sample

**Detailed-Settlement-report-1.png IMAGE GOES HERE.**

[CampaignNameDailySettlementsYYYYMMDD.csv](https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignNameDailySettlementsYYYYMMDD-1.csv)  
[CampaignNameDailySettlementsYYYYMMDDsample.csv](https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignNameDailySettlementsYYYYMMDD-2.csv)
