---
title: Detailed settlement report
deprecated: false
hidden: false
metadata:
  robots: index
---
Paymentology also provides a detailed version of the summary Settlement Report.The Detailed Settlement Report shows each settled transaction, which allows you to use the Transaction id to mark off settled transactions from authorized transactions. This also assists in confirming the values of the amounts in the summary Settlement Report. The network provides the Transaction id field during authorization. The same Transaction id for authorizations is included in the Detailed Settlement Report.

You can generate the Detailed Settlement Report by sending an HTTP GET request and download it as a CSV file.

There are two versions of this report available:

[Version 1.0](#DSRV1)
[Version 2.4](#DSRV2)

### Version 1

Version 1 includes the following details:

* **Transactions date** – this is the settlement date of the transaction.
* **The amount in the issuing currency (cardholder currency)** – the actual amount is a decimal number.
* **The amount in the settlement currency** – it’s the amount passed over by the network. It should be multiplied by 100 to include cents. If the settlement currency does not have decimals, you’ll take the value as-is.
* **Transaction narrative** – it’s the merchant’s description.
* **Transaction description** – this describes the transaction type, such as:

  * `Deduct` – shows all deductions at the time of settlement.
  * `Load` – shows loads/credits at the time of settlement.
  * `Reversal` – shows reversals at the time of settlement. In most cases these are reversals of an original deduct transaction.
  * `Load reversal` – shows loads that have been reversed at the time of settlement.
  * `2nd presentment` – shows 2nd presentments at the time of settlement.
  * `2nd presentment reversal` – shows a 2nd presentment that has been reversed at the time of settlement.
* **Transaction id** – it’s a reference for the transaction.

  * In most cases, the provided Transaction id will be the same Transaction id as the original authorization. It’s usually 7 to 10 digits.
  * In case of refunds, there will be a unique Transaction id for each of them. The id does not relate to the original authorization. It’s also longer, up to 23 characters.
  * In case of chargebacks, there will be a unique Transaction id for each of them. The id does not relate to the original authorization. It’s also longer, up to 23 characters.
* **Currency code** – this is the currency code for the settlement currency.
* **Transaction types** – they can be marked as 00 (for POS transactions), 01 (for ATM transactions), or 02 (for adjustment transactions).
* **Wallet reference** – this is a unique customer reference for the card.
* **System date** – this is Paymentology’s system date in UTC +2 time zone.
* **Sequence number** – this is a unique sequence card identifier showing a running number for the cards created.
* **Tracking number** – this is a unique 15-digit tracking identifier for the card.
* **Settlement currency** – this is the currency code for the settlement currency.
* **Interchange amount** – this is the individual amounts earned per transaction.
* **Network transaction id** – (Mastercard only) this is the Networks TraceID, it assists clients with matching pre-authorizations and incremental pre-authorizations to the settlements for those transactions.

### Version 2.4

Version 2.4 includes the following details:

* **TransactionDate** – this is the settlement date of the transaction.
* **Transaction Amount (SettlementAmount)** – it’s the amount passed over by the network. It should be multiplied by 100 to include cents. If the settlement currency does not have decimals, you’ll take the value as-is.
* **TransactionAmount (CardholderCurrency)** – the actual amount is a decimal number.
* **TransactionNarrative** – it’s the merchant’s description.
* **TransactionDescription** – this describes the transaction type, such as:

  * `DEDUCT` – shows all deductions at the time of settlement.
  * `LOAD` – shows loads/credits at the time of settlement.
  * `REVERSAL` – shows reversals at the time of settlement. In most cases these are reversals of an original deduct transaction.
  * `LOAD REVERSAL` – shows loads that have been reversed at the time of settlement.
  * `2ND PRESENTMENT` – shows 2nd presentments at the time of settlement.
  * `2ND PRESENTMENT REVERSAL` – shows a 2nd presentment that has been reversed at the time of settlement.
* **TransactionID** – it’s a reference for the transaction.

  * In most cases, the provided Transaction id will be the same Transaction id as the original authorization. It’s usually 7 to 10 digits.
  * In case of refunds, there will be a unique Transaction id for each of them. The id does not relate to the original authorization. It’s also longer, up to 23 characters.
  * In case of chargebacks, there will be a unique Transaction id for each of them. The id does not relate to the original authorization. It’s also longer, up to 23 characters.
* **TransactionType** – they can be marked as 00 (for POS transactions), 01 (for ATM transactions), or 02 (for adjustment transactions).
* **WalletReference** – this is a unique customer reference for the card.
* **SystemDate** – this is Paymentology’s system date in UTC +2 time zone.
* **SequenceNumber** – this is a unique sequence card identifier showing a running number for the cards created.
* **TrackingNumber** – this is a unique 15-digit tracking identifier for the card.
* **SettlementCurrency** – this is the currency code for the settlement currency and relates to the **Transaction Amount (SettlementAmount)**.
* **CardholderCurrency** – this is the currency code for the cardholder currency and relares to the **TransactionAmount(CardholderCurrency)**.
* **Interchange Amount** – this is the individual amounts earned per transaction.
* **LocalAmount** – this is the local amount of the transaction (DE4).
* **LocalCurrency** – this is the local currency of the transaction (DE49) and refers to **LocalAmount**
* **NetworkTransactionID** – (Mastercard only) this is the Networks TraceID, it assists clients with matching pre-authorizations and incremental pre-authorizations to the settlements for those transactions.
* **AcquirerReferenceNumber** – this is the Acquirer Reference Data (DE31)
* **TransactionAuthorisationNumber** – this is the Approval Code (DE38) (Authorisation id Response) provided by the network.
* **OriginatingMessageFormat** – identifies whether the acquirer was domestic or international (MEXICO ONLY).

## Report format

## Report time frame

## Report Sample

**Detailed-Settlement-report1.png IMAGE GOES HERE.**

[CampaignNameDailySettlementsYYYYMMDD.csv](https://developer.sprint.paymentology.com/wp-content/uploads/2024/02/CampaignNameDailySettlementsYYYYMMDD.csv)
