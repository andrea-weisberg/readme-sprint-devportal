---
title: Card order
deprecated: false
hidden: false
metadata:
  robots: index
---
A **card order** is a request to print a physical card. With the Companion API, you can optionally issue a physical card to a customer by sending an order for printing to the card manufacturer. To initiate a request to print a physical card, you use the [OrderCard](https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/ordercard/) method in the Local API. On a daily basis at 19:30 UTC+2, Paymentology creates a batch order and submits it to the manufacturer for printing. A **card order** report lists all the orders that were processed on the previous day.

The report includes the following details:

* **Card Number** – this is the issued/created card number. Due to card numbers being sensitive data, the card number is usually presented in the format 1234xxxxxxxx5678.
* **Wallet Reference** – this is the unique customer reference for the card.
* **Date Created** – this is the date and time stamp of when the card number was issued. Usually in the format DD/MM/YYYY HH:MM.

## Report format

## Report time frame

## Report sample

**Card-Order1-300x195.png IMAGE GOES HERE.**

[CampaignName_PanDetails_YYYYMMDD.csv](https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_PanDetails_YYYYMMDD.csv)
