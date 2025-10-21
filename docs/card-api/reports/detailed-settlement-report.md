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

- [Version 1.0](#dsrv1)
- [Version 2.0](#dsrv20)
- [Version 2.1](#dsrv21)

The report includes the following details:

<a id="dsrv1"></a>

### Version 1

Contains the Chargeback report.

- **Transactions date** – this is the settlement date of the transaction.
- **The amount in the issuing currency (cardholder currency)** – the actual amount is a decimal number.
- **The amount in the settlement currency** – it’s the amount passed over by the network. It should be multiplied by 100 to include cents. If the settlement currency does not have decimals, you’ll take the value as-is.
- **Transaction narrative** – it’s the merchant’s description.
- **Transaction description** – describes the transaction type:
  - Deduct – shows all deductions at the time of settlement.
  - Load – shows refunds.
  - Chargeback – gives positive or negative amounts for chargebacks.
- **Transaction ID** – a reference for the transaction.
  - In most cases, the provided Transaction ID will be the same Transaction ID as the original authorization. It’s usually 7 to 10 digits.
  - In case of refunds, there will be a unique Transaction ID for each of them. The ID does not relate to the original authorization. It’s also longer, up to 23 characters.
  - In case of chargebacks, there will be a unique Transaction ID for each of them. The ID does not relate to the original authorization. It’s also longer, up to 23 characters.
- **Currency code** – this is the currency code for the settlement currency.
- **Transaction types** – can be marked as `00` (POS), `01` (ATM), or `02` (adjustment).
- **Wallet reference** – empty for Card API reporting.
- **System date** – Paymentology’s system date in UTC +2.
- **Sequence number** – a unique sequence card identifier showing a running number for the cards created.
- **Tracking number** – a unique 15-digit tracking identifier for the card.
- **Settlement currency** – the currency code for the settlement currency.
- **Interchange amount** – the individual amounts earned per transaction.

---

<a id="dsrv20"></a>

### Version 2.0

Does not contain the Chargeback record (see Transaction Description column).

- **Transactions date** – settlement date of the transaction.
- **The amount in the issuing currency (cardholder currency)** – the actual amount is a decimal number.
- **The amount in the settlement currency** – passed over by the network. Multiply by 100 for cents. If no decimals exist in the settlement currency, take as-is.
- **Transaction narrative** – the merchant’s description.
- **Transaction description** – describes the transaction type:
  - Deduct – shows all deductions at the time of settlement.
  - Load – shows refunds.
- **Transaction ID** – a reference for the transaction.
  - Same as authorization in most cases (7–10 digits).
  - Refunds: unique Transaction ID, unrelated to authorization, up to 23 characters.
  - Chargebacks: unique Transaction ID, unrelated to authorization, up to 23 characters.
- **Currency code** – settlement currency code.
- **Transaction types** – `00` (POS), `01` (ATM), `02` (adjustment).
- **Wallet reference** – empty for Card API reporting.
- **System date** – Paymentology’s system date in UTC +2.
- **Sequence number** – unique sequence identifier for cards created.
- **Tracking number** – unique 15-digit tracking identifier for the card.
- **Settlement currency** – settlement currency code.
- **Interchange amount** – individual amounts earned per transaction.

---

<a id="dsrv21"></a>

### Version 2.1

Builds off Version 2.0 and does not contain the Chargeback record.  
Changes include additional information to the **Transaction Narrative** column, delimited by pipes, e.g. `TransactionNarrative|AdditionalTraceRef|CustomIdentifier`.

- **Transactions date** – settlement date of the transaction.
- **The amount in the issuing currency (cardholder currency)** – the actual amount is a decimal number.
- **The amount in the settlement currency** – passed over by the network. Multiply by 100 for cents. If no decimals exist, take as-is.
- **Transaction narrative|AdditionalTraceRef|CustomIdentifier** – merchant’s description with additional values.
- **Transaction description** – describes the transaction type:
  - Deduct – shows all deductions at the time of settlement.
  - Load – shows refunds.
- **Transaction ID** – a reference for the transaction.
  - Same as authorization in most cases (7–10 digits).
  - Refunds: unique Transaction ID, unrelated to authorization, up to 23 characters.
  - Chargebacks: unique Transaction ID, unrelated to authorization, up to 23 characters.
- **Currency code** – settlement currency code.
- **Transaction types** – `00` (POS), `01` (ATM), `02` (adjustment).
- **Wallet reference** – empty for Card API reporting.
- **System date** – Paymentology’s system date in UTC +2.
- **Sequence number** – unique sequence identifier for cards created.
- **Tracking number** – unique 15-digit tracking identifier for the card.
- **Settlement currency** – settlement currency code.
- **Interchange amount** – individual amounts earned per transaction.

---

## Report format

## Report time frame

## Report sample

**Detailed-Settlement-report-1.png IMAGE GOES HERE.**

[CampaignNameDailySettlementsYYYYMMDD.csv](https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignNameDailySettlementsYYYYMMDD-1.csv)  
[CampaignNameDailySettlementsYYYYMMDDsample.csv](https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignNameDailySettlementsYYYYMMDD-2.csv)
