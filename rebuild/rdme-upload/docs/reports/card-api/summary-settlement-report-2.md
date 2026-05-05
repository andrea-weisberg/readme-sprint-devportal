---
title: Summary settlement report
category:
  uri: Reports
slug: card-api-summary-settlement-report-2
position: 16
parent:
  uri: card-api-reports
---

This gives a daily summary of all the transactions settled by the card association. Paymentology gathers the information from the card association file and packages it into a summary report. It is a report where you can find a summary of transaction types, the number of transactions that have been settled for the day, fees and interchanges earned.

The Summary Settlement Report includes a separate tab for each currency you decide to settle in.

**Note:** If the client chooses to settle in one currency, then both domestic and international settlements will fall under one tab.

The report includes a combination of debits and credits that the network processes daily.

- **Credits** - include refunds, chargebacks and interchanges.

- **Debits** - include POS and ATM settlements, fees and unique transactions.

The network NETTs off the credits from the debits. So, only a single transfer will need to be made when settling with the network daily.

Here is a description of the transactions you can find in the report:

- **Unique Transactions** - consist of transactions from merchants, such as casinos, gambling sites and pharmacies.

- **ATM Interchange** - it’s a debit fee that the card issuer sends to a card network to pay the bank agent where the ATM transaction took place.

- **Card Association Fee** - this can be either a debit or a credit transaction. As a debit transaction, there is a fee paid to a card network for a specific service rendered. As a credit transaction, there can be some discounts applied to the paid services. There is a difference between Card Association Fee Credit and Card Association Fee Reversal. The latter refers to a reversal provided back to the issuer via an incorrect charge, whereas the former is a discount given off the fees.

## Report format

## Report time frame

## Report sample

![](https://files.readme.io/95590d58d103d5682fd117cc41a891217824c4eef49492cfd8011aba6e2b61fe-2bb5e9d1b99970b394e480386336e1c2c810d40cfd7dd68b5762bce3c8cdeecc-Summary-Settlement-report-final.png)

**Note: file will automatically download upon clicking link**

[Daily_Settlement_Report_ICA_(YYYY_MM_DD).xls](https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/Daily_Settlement_Report_ICA_YYYY_MM_DD-1.xls)
