# Failed transaction report

This report gives details of the transactions that were declined daily. It contains a list of transactions that Paymentology or the client declined, and sent a declined response code to the card association. With the failed transaction report file, it becomes easier to find the reasons for failures in transactions and improve the process.

The report is also generated monthly and contains the same report details as the daily report.

There are two versions of this report available:

[Version 1.0](#FTRV1)

[Version 2.0](#FTRV2)

### Version 1

Version 1 includes the following details:

- Campaign Name - name of client's campaign.

- Voucher Number - the customer's card number.

- Transaction Amount - the value of the transaction.

- Transaction Date - this is the settlement date of the transaction.

- Transaction Method - the API method used in sending the transaction to the client.

- Transaction Error Code - the code indicating the reason for the decline.

- Acceptor Name - the name of the merchant.

- Merchant No - the unique number used to identify the merchant.

- Voucher Value - the voucher value at the point the transaction failed. Voucher Value = Voucher Load Value - (Already settled amount + Authorised amount).

- Wallet Reference - this is a unique customer reference for the card.

- Transaction ID - it’s a unique reference for the transaction. In most cases, the provided Transaction ID will be the same Transaction ID as the original authorization. It’s usually 7 to 10 digits.

- In case of refunds, there will be a unique Transaction ID for each of them. The ID does not relate to the original authorization. It’s also longer, up to 23 characters.

- In case of chargebacks, there will be a unique Transaction ID for each of them. The ID does not relate to the original authorization. It’s also longer, up to 23 characters.

- Tracking Number - this is a unique 15-digit tracking identifier for the card.

- MCC - the merchant category code.

- POS Entry mode - indicates how the transaction was captured (Capture Mode). Possible values include: ECOM (Ecommerce), NFC (Near Field Communication), MAG (Magnetic stripe), MAN (Manually), EMV (EMV chip).

- Transaction Internal Code - this is a code that gives you the reason for transaction declines. List of codes can be downloaded [here](https://developer.sprint.paymentology.com/wp-content/uploads/2021/04/Failed-transaction-report-code-descriptions.xlsx)

- Digitized Wallet ID - the 3 digit numeric code that identifies the Xpay App. Find a list of the Wallet IDs [here](https://developer.sprint.paymentology.com/companion-api/tokenization2/token-lifecycle-management/#WID).

If the transaction did not reach Paymentology and was declined, this would not appear on the report.

### Version 2

Version 2 includes the following details:

- Campaign Name - name of client's campaign.

- Voucher Number - the customer's card number.

- Transaction Amount - the value of the transaction.

- Transaction Date - this is the settlement date of the transaction.

- Transaction Method - the API method used in sending the transaction to the client.

- Transaction Error Code - the code indicating the reason for the decline.

- Acceptor Name - the name of the merchant.

- Merchant No - the unique number used to identify the merchant.

- Voucher Value - the voucher value at the point the transaction failed. Voucher Value = Voucher Load Value - (Already settled amount + Authorised amount).

- Wallet Reference - this is a unique customer reference for the card.

- Transaction ID - it’s a unique reference for the transaction. In most cases, the provided Transaction ID will be the same Transaction ID as the original authorization. It’s usually 7 to 10 digits.

- In case of refunds, there will be a unique Transaction ID for each of them. The ID does not relate to the original authorization. It’s also longer, up to 23 characters.

- In case of chargebacks, there will be a unique Transaction ID for each of them. The ID does not relate to the original authorization. It’s also longer, up to 23 characters.

- Tracking Number - this is a unique 15-digit tracking identifier for the card.

- MCC - the merchant category code.

- POS Entry mode - indicates how the transaction was captured (Capture Mode). Possible values include: ECOM (Ecommerce), NFC (Near Field Communication), MAG (Magnetic stripe), MAN (Manually), EMV (EMV chip).

- Transaction Internal Code - this is a code that gives you the reason for transaction declines. List of codes can be downloaded [here](https://developer.sprint.paymentology.com/wp-content/uploads/2021/04/Failed-transaction-report-code-descriptions.xlsx)

- Digitized Wallet ID - the 3 digit numeric code that identifies the Xpay App. Find a list of the Wallet IDs [here](https://developer.sprint.paymentology.com/companion-api/tokenization2/token-lifecycle-management/#WID).

- Payment Initiator - indicates whether a transaction was initiated by the Cardholder (CIT - Cardholder Initiated Transaction) or the Merchant (MIT - Merchant Initiated Transaction)

## Report format

## Report time frame

If the transaction did not reach Paymentology and was declined, this would not appear on the report.

## Report sample![](https://developer.sprint.paymentology.com/wp-content/uploads/2021/01/Failed-transactions-report-Card-Final.png)

Note: file will automatically download upon clicking link

[CampaignName_DailyAuthFailure_YYYYMMDD.csv](https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_DailyAuthFailure_YYYYMMDD.csv)

[CampaignName_DailyAuthFailure_YYYYMMDD.csv V2 sample](https://developer.sprint.paymentology.com/wp-content/uploads/2024/10/CampaignName_DailyAuthFailure_YYYYMMDD-.csv)
