---
title: Blocked transactions report
category:
  uri: Reports
slug: card-api-blocked-transactions-report
position: 4
parent:
  uri: card-api-reports
---

This report lists detailed information about filtered transactions for a specific set of campaigns, during a specified date range.
The report includes details about vouchers and reasons for transactions being filtered. This reports helps clients to identify if any whitelisted merchants (approved merchants) are blocked.

The report includes the following details:

- **Campaign** - name of client’s card program (string).

- **Terminal** - terminal information i.e. merchant name, city, country etc (string).

- **Reason** - filtered transaction reason i.e. unmatched (string).

- **Keyword** - filtered transaction blacklist keyword i.e. Estate Service Station (string). If there is no specific keyword then field will contain N/A.

- **Type** - filtered transaction type, such as (string): POS

- ATM

- **Date Blocked** - date the the transaction was blocked (YYYY/MM/DD HH:MM:SS).

- **Identifier** - the voucher number (numeric string).

## Report format

## Report time frame

## Report sample

Note: file will automatically download upon clicking link

[CampaignName Blocked Transactions - 231015-231022.xls](https://developer.sprint.paymentology.com/wp-content/uploads/2024/02/CampaignName-Blocked-Transactions-231015-231022.xls)
