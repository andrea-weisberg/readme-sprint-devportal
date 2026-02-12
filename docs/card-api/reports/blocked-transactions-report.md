---
title: Blocked transactions report
deprecated: false
hidden: false
metadata:
  robots: index
---
<!-- MIGRATION_METADATA
Migrated-From: https://developer.sprint.paymentology.com/companion-api/reports/blocked-transactions-report/
Source-Slug: blocked-transactions-report
Migrated-On: 2026-02-12T21:32:22+00:00
Migrated-By: wp-readme-migration
-->

This report lists detailed information about filtered transactions for a specific set of campaigns, during a specified date range.

The report includes details about vouchers and reasons for transactions being filtered. This reports helps clients to identify if any whitelisted merchants (approved merchants) are blocked.

The report includes the following details:

- **Campaign** – name of client’s card program (string).

- **Terminal** – terminal information i.e. merchant name, city, country etc (string).

- **Reason** – filtered transaction reason i.e. unmatched (string).

- **Keyword** – filtered transaction blacklist keyword i.e. Estate Service Station (string). If there is no specific keyword then field will contain N/A.

- **Type** – filtered transaction type, such as (string):

- POS

- ATM

- **Date Blocked** –  date the the transaction was blocked (YYYY/MM/DD HH:MM:SS).

- **Identifier** – the voucher number (numeric string).


## Report format


| FORMAT | FILE NAME | FREQUENCY | ACCESSIBILITY |
| --- | --- | --- | --- |
| XLS | [CampaignName] Blocked Transactions - [dateBegin:yymmdd] - [dateEnd:yymmdd].xls | Weekly | Sent via email or SFTP |


## Report time frame


| UTC +2 | UTC +7 | REMARKS |
| --- | --- | --- |
| 08:30 | 13:30 | This report is generated weekly, only on Thursday. |


## Report sample


> 📘 Info
>
> Note: file will automatically download upon clicking link


[CampaignName Blocked Transactions – 231015-231022.xls](../../../assets/CampaignName-Blocked-Transactions-231015-231022.xls)
