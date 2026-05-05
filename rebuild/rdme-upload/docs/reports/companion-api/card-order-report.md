---
title: Card order
category:
  uri: Reports
slug: companion-api-card-order-report
position: 46
parent:
  uri: companion-api-reports
---

A **card order** is a request to print a physical card. With the Companion API, you can optionally issue a physical card to a customer by sending an order for printing to the card manufacturer. To initiate a request to print a physical card, you use the [OrderCard](/api-reference/companion-api/ordercard) method in the Local API. On a daily basis at 19:30 UTC+2, Paymentology creates a batch order and submits it to the manufacturer for printing. A **card order**report lists all the orders that were processed on the previous day. SFTP folder

-->

The report includes the following details:

- **Card Number**- this is the issued/created card number. Due to card numbers being sensitive data, the card number is usually presented in the format 1234xxxxxxxx5678.

- **Wallet Reference** - this is the unique customer reference for the card.

- **Date Created** - this is the date and time stamp of when the card number was issued. Usually in the format DD/MM/YYYY HH:MM.

## Report format

## Report time frame

## Report sample

![Card order report](https://files.readme.io/c7cb6002150860f823b7ec758d8061582c8c8ad4669fb356872047e5d95f997e-91c11ca4ea4e9d48e15f98858a4e17d59f9f83dfaf7d89dc5448b127c00273af-Card-Order1-300x195.png)

**Note: file will automatically download upon clicking link**

[CampaignName_PanDetails_YYYYMMDD.csv](https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_PanDetails_YYYYMMDD.csv)
