---
title: Forex gains report
category:
  uri: Reports - Companion API
slug: forex-gains-report
position: 18
parent:
  uri: reports
---

If you’re marking up a transaction with a forex fee, you’ll receive a report each day showing the FX amount that you earned as revenue for the day.

You can access this report by making an HTTP GET request and downloading it.

​

The report includes the following details:

- **Date** - the date of the settlement.

- **Voucher number** - the masked card number.

- **Activation data** - the unique wallet reference number.

- **Merchant description** - the merchant name.

- **Transaction ID** - the unique transaction ID used for the initial deduct.

- **Reversed** - this shows if a fee was reversed.

- **Currency**- this shows the currency of the fee.

- **Fee** - the actual amount earned in forex fees.

## Report format

## Report time frame

## Report sample

![](https://developer.sprint.paymentology.com/wp-content/uploads/2021/10/Forex-Gains1.png)

**Note: file will automatically download upon clicking link**

[DailyForexReport_CAMID_(YYYY_MM_DD).xls](https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/DailyForexReport_CAMID_YYYY_MM_DD.xls)
