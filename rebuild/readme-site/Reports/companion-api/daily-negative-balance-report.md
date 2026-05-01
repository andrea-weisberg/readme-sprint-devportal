# Daily negative balance report

This report provides clients with detailed information on cards that have entered into a negative balance status. It provides essential, actionable information to trace the transactions and correct the negative balance scenarios.

- Clients will receive this report via email daily with the data from the previous day.

- All sensitive information, such as voucher numbers, are masked for security

The report includes the following details:

- **VoucherNumber** - The voucher number associated with the card (masked for security purposes, only last four digits visible).

- **TrackingNumber** - Unique identifier for tracking the transaction.

- **WalletReference** - The unique wallet identifier associated with the card.

- **CardStatus** - Current status of the card (e.g. Active, Inactive).

- **VoucherBalanceAmount** - The balance of the card.

- **CampaignName** - Name of the campaign to which the card belongs.

- **AuthorisationID** - The unique authorization ID for the transaction that led to the balance.

- **AuthorisationAmount** - The authorized amount for the transaction.

- **AuthorisationDate** - The date when the authorization was made.

- **TransactionType** - Type of transaction. 0 = POS transaction, 1 = ATM transaction, 2 = Adjustment.

- **CampaignCurrencySymbol** - The currency of the campaign to which the card belongs in ISO4217 alpha (e.g. USD).

- **MerchantName** - The name and address of the merchant where the transaction occurred.

## Report format

## Report time frame

## Report sample

**Note: sample file will automatically download upon clicking link**

[DailyNegativeBalanceReportOnChargebackQueue_CampaignName_YYYYMMDD.csv](https://developer.sprint.paymentology.com/wp-content/uploads/2024/10/DailyNegativeBalanceReportOnChargebackQueue_CampaignName_YYYYMMDD.csv)

[Back to Companion API Reports](#https://developer.sprint.paymentology.com/companion-api/reports/)
