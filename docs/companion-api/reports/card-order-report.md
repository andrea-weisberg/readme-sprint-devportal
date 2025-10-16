---
title: Card order
deprecated: false
hidden: false
metadata:
  robots: index
---

<p>A <strong>card order</strong> is a request to print a physical card. With the Companion API, you can optionally issue a physical card to a customer by sending an order for printing to the card manufacturer. To initiate a request to print a physical card, you use the <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/ordercard/"><span className="xml-highlight">OrderCard</span></a> method in the Local API. On a daily basis at 19:30 UTC+2, Paymentology creates a batch order and submits it to the manufacturer for printing. A <strong>card order </strong>report lists all the orders that were processed on the previous day.</p>
<p>The report includes the following details:</p>
<ul>
<li><strong>Card Number </strong>– this is the issued/created card number. Due to card numbers being sensitive data, the card number is usually presented in the format 1234xxxxxxxx5678.</li>
<li><strong>Wallet Reference</strong> – this is the unique customer reference for the card.</li>
<li><strong>Date Created</strong> – this is the date and time stamp of when the card number was issued. Usually in the format DD/MM/YYYY HH:MM.</li>
</ul>

<h2>Report format</h2>

<h2>Report time frame</h2>

<h2>Report sample</h2>
<p>**Card-Order1-300x195.png IMAGE GOES HERE.**</p>

<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/CampaignName_PanDetails_YYYYMMDD.csv">CampaignName_PanDetails_YYYYMMDD.csv</a></p>

