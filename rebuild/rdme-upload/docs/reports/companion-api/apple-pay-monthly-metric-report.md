---
title: Apple Pay monthly metric report
category:
  uri: Reports
slug: companion-api-apple-pay-monthly-metric-report
position: 51
parent:
  uri: companion-api-reports
---

For clients using Paymentology’s tokenization, Paymentology can issue monthly reports to clients to assist in compiling their Apple report through the Apple Partner Connect platform.

The monthly metric report provides clients with a breakdown of POS (Point of Sale), remote (in-App, Apple Pay on the web and eCommerce) and COF (Credential on File) Apple Pay spends for the specified month.

The report includes the following details:

- **Reporting Month**- the month the report data is based on.

- **Monthly DPAN transaction count**- total number of settled DPAN transactions made using Apple Pay for the given month.

- **Monthly DPAN spend** - total value of settled DPAN transactions made using Apple Pay for the given month.

- **% of POS DPAN transactions out of the monthly processed DPAN transactions** - percentage split of **Monthly DPAN transaction count** that were POS (Point of Sale) type spends.

- **% of Remote DPAN transactions out of the monthly processed DPAN transactions**- percentage split of **Monthly DPAN transaction count** that were remote type spends i.e. in-App, Apple Pay on the web and eCommerce.

- **% of COF DPAN transactions out of the monthly processed DPAN transactions**- percentage split of **Monthly DPAN transaction count** that were COF (Credential on File) type spends.

- **% of POS DPAN spend amount out of the monthly processed DPAN transactions** - percentage split of **Monthly DPAN spend** value that were POS (Point of Sale) type spends.

- **% of Remote DPAN spend amount out of the monthly processed DPAN transactions**- percentage split of **Monthly DPAN spend** value that were remote type spends i.e. in-App, Apple Pay on the web and eCommerce.

- **% of COF DPAN spend amount out of the monthly processed DPAN transactions**- percentage split of **Monthly DPAN spend** value that were COF (Credential on File) type spends.

- **Total Available DPANs**- these are the tokens that are available for use on Apple Pay as of the end of the reporting month. Total Available DPANs are defined as successfully provisioned since launch onto Apple Pay, excluding all inactive, pending, suspended, and deleted tokens.

- **Monthly Active DPANs** - this is the count of DPANs that have transacted at least once in the given month.

DPAN (Device Primary Account Number) - A token that acts as a surrogate for the customer’s card number and is used to make contactless and e-commerce transactions using an Apple device.

Only settled transactions are included and all values specified are in the cardholder billing currency.

## Report format

## Report time frame

## Report sample

![](https://files.readme.io/db7f6d9638c39963d9b5f4174b8316965eb159ff1bdad319eff9fda3b3611cca-60fed221a1e73aa846093e85dbe7126e1dde47918040c810cf1521b8f9a26885-CampaignName_ApplePay-Monthly-Metric-Report-Month-YYYY-_-002.png)

**Note: file will automatically download upon clicking link**

[CampaignName_ApplePay Monthly Metric Report Month YYYY.xls](https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_ApplePay-Monthly-Metric-Report-Month-YYYY.xls)
