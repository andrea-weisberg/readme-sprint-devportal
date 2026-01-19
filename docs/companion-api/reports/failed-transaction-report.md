---
title: Failed transaction report
deprecated: false
hidden: false
metadata:
  robots: index
---
This report gives details of the transactions that were declined daily.
It contains a list of transactions that Paymentology or the client declined, and sent a declined response code to the card association.
With the failed transaction report file, it becomes easier to find the reasons for failures in transactions and improve the process.

The report is also generated monthly and contains the same report details as the daily report.

There are two versions of this report available:

[Version 1.0](#FTRV1)
[Version 2.0](#FTRV2)

### Version 1

Version 1 includes the following details:

* **Campaign name** – name of client’s campaign.
* **Voucher Number** – the customer’s card number.
* **Transaction Amount** – the value of the transaction.
* **Transaction Date** – this is the settlement date of the transaction.
* **Transaction method** – the API method used in sending the transaction to the client.
* **Transaction Error Code** – the code indicating the reason for the decline.
* **Acceptor name** – the name of the merchant.
* **Merchant No** – the unique number used to identify the merchant.
* **Voucher value** – the voucher value at the point the transaction failed. Voucher value = Voucher Load value – (Already settled amount + Authorised amount).
* **Wallet Reference** – this is a unique customer reference for the card.
* **Transaction id** – it’s a unique reference for the transaction.

  * In most cases, the provided Transaction id will be the same Transaction id as the original authorization. It’s usually 7 to 10 digits.
  * In case of refunds, there will be a unique Transaction id for each of them. The id does not relate to the original authorization. It’s also longer, up to 23 characters.
  * In case of chargebacks, there will be a unique Transaction id for each of them. The id does not relate to the original authorization. It’s also longer, up to 23 characters.
* **Tracking Number** – this is a unique 15-digit tracking identifier for the card.
* **MCC** – the merchant category code.
* **POS Entry mode** – indicates how the transaction was captured (capture Mode). Possible values include: ECOM (Ecommerce), NFC (Near Field Communication), MAG (Magnetic stripe), MAN (Manually), EMV (EMV chip).
* **Transaction Internal Code** – this is a code that gives you the reason for transaction declines. List of codes can be downloaded [here](https://developer.sprint.paymentology.com/wp-content/uploads/2021/04/Failed-transaction-report-code-descriptions.xlsx)
* **Digitized Wallet id** – the 3 digit numeric code that identifies the Xpay App. Find a list of the Wallet IDs [here](https://developer.sprint.paymentology.com/companion-api/tokenization2/token-lifecycle-management/#WID).

<DeclinedNavyBox />

***

### Version 2

Version 2 includes the following details:

* **VoucherNumber** – the customer’s card number
* **FailedTransactionID** – it’s a unique reference for the transaction.

  * In most cases, the provided Transaction id will be the same Transaction id as the original authorization. It’s usually 7 to 10 digits.
  * In case of refunds, there will be a unique Transaction id for each of them. The id does not relate to the original authorization. It’s also longer, up to 23 characters.
  * In case of chargebacks, there will be a unique Transaction id for each of them. The id does not relate to the original authorization. It’s also longer, up to 23 characters.
* **FailedVoucherNumber** – the customer’s card number.
* **CampaignName** – name of client’s campaign.
* **FailedTransactionAmount** – the value of the transaction.
* **FailedTransactionDate** – this is the settlement date of the transaction.
* **FailedTransactionMethod** – the API method used in sending the transaction to the client.
* **FailedTransactionManager** –
* **FailedTransactionErrorCode** – the code indicating the reason for the decline. List of codes can be downloaded [here.](https://developer.sprint.paymentology.com/wp-content/uploads/2021/04/Failed-transaction-report-code-descriptions.xlsx)
* **FailedTransactionInternalCode** – this is a code that gives you the reason for the decline, when the failure was due to an internal reason. In most cases this will be NULL.
* **FailedTransactionAcquiringInstitution** – the acquiring institution (typically the merchants bank) or its agent.
* **FailedTransactionDescription** – the name of the merchant.
* **FailedTransactionErrorDescription** – a textual description on why a transaction failed with more reasons. For example: “Reject With Action Code 1061; ruleID: 6839”.
* **TrackingNumber** – this is a unique 15-digit tracking identifier for the card.
* **WalletReference** – this is a unique customer reference for the card.
* **TransactionID** – it’s a unique reference for the failed transaction record.

  * In most cases, the provided TransactionID will be different from the FailedTransactionID, as it’s a reference to the failed record. It’s usually 12-16 digits.
* **FailedTransactionVoucherValue** – the voucher value at the point the transaction failed. Voucher value = Voucher Load value – (Already settled amount + Authorised amount).
* **EntryMode** – indicates how the transaction was captured (capture Mode). Possible values include: ECOM (Ecommerce), NFC (Near Field Communication), MAG (Magnetic stripe), MAN (Manually), EMV (EMV chip).
* **DigitizedWalletID** – the 3 digit numeric code that identifies the Xpay App. Find a list of the Wallet IDs [here](https://developer.sprint.paymentology.com/companion-api/tokenization2/token-lifecycle-management/#WID).
* **MerchantNo** – the unique number used to identify the merchant.
* **MerchantCategoryCode** – the merchant category code.
* **PaymentInitiator** – indicates whether a transaction was initiated by the Cardholder (CIT – Cardholder Initiated Transaction) or the Merchant (MIT – Merchant Initiated Transaction)

<DeclinedNavyBox />

***

## Report format

<table>
  <thead>
    <tr>
      <th align="center">FORMAT</th>
      <th align="center">FILE NAME</th>
      <th align="center">FREQUENCY</th>
      <th align="center">ACCESSIBILITY</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td align="center">CSV</td>

      <td align="center">
        <strong>DAILY REPORT:</strong><br />
        \[CampaignUUID]/\[CampaignName]*DailyAuthFailure*\[YYYYMMDD].csv<br /><br />
        <strong>MONTHLY REPORT:</strong><br />
        \[CampaignUUID]/failedtransactions\_\[CampaignName]\_\[YYYY-MM-DD-YYYY-MM-DD].csv
      </td>

      <td align="center">Daily & Monthly</td>
      <td align="center">HTTP GET request or client SFTP folder</td>
    </tr>
  </tbody>
</table>

## Report time frame

<table>
  <thead>
    <tr>
      <th align="center">UTC +2</th>
      <th align="center">UTC +7</th>
      <th align="center">REMARKS</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td align="center">06:30</td>
      <td align="center">11:30</td>

      <td align="center">
        When the report is generated at <strong>06:30 UTC+2</strong> /
        <strong>11:30 UTC+7</strong> (2020-09-10), the timeframe of all failed
        transactions captured in this report is from
        <strong>2020-09-09 00:00:00</strong> to
        <strong>2020-09-09 11:59:59</strong> in:

        <br />

        <br />

        • System time zone UTC+2<br />
        • Asia client time zone UTC+7<br />
        • Merchant time zone
      </td>
    </tr>
  </tbody>
</table>

## Report sample

**Failed-transaction-report1-1.png IMAGE GOES HERE.**

[CampaignName_DailyAuthFailure_YYYYMMDD.csv](https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_DailyAuthFailure_YYYYMMDD.csv)
[CampaignName_DailyAuthFailure_YYYYMMDD.csv – V2 sample](https://developer.sprint.paymentology.com/wp-content/uploads/2025/05/CampaignName_DailyAuthFailure_YYYYMMDD-V2.csv)
