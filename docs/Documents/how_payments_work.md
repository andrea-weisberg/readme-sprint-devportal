---
title: How Payments Work
deprecated: false
hidden: false
metadata:
  robots: index
---
<p><b>There are different stages of a transaction when a card is used to pay for goods and services. </b></p>
<p>Let’s look at each of them.</p>

<h2>Who is involved in the transaction?</h2>

<h2>What is a transaction?</h2>
<p>A transaction is the movement of money from a cardholder’s account to a merchant’s account in exchange for goods or services provided.</p>
<h2>Stages in a transaction</h2>
<p><strong>Payment request – </strong>This is when the cardholder uses their card and the request is routed to the Issuer (Tutuka)<br >
<strong><a href="https:developer.sprint.paymentology.com/companion-api/settlement-and-reconciliation/#authorization">Authorisation</a> – </strong>This is the process of checking the available funds on a card in order to reserve funds when the card is used for a purchase<br >
<strong><a href="https:developer.sprint.paymentology.com/companion-api/settlement-and-reconciliation/#settlements">Settlement</a> – </strong>This is when funds are deducted from the Issuer/client’s bank account and deposited into a merchants bank account to settle a card transaction.<br >
<a href="https:developer.sprint.paymentology.com/companion-api/disputes/"><strong>Disputes</strong></a> <strong>–</strong> This happens when a cardholder disagrees with a deduct on their card statement</p>

<h2>How the transaction is processed</h2>
<ul>
<li>The Cardholder uses their card to pay for goods or services at a Merchant</li>
<li>The card information is sent to the Acquirer. The Acquirer uses the BIN to identify the relevant Card scheme and sends the payment request to the Card scheme</li>
<li>The Card scheme receives the payment request and routes the transaction to the Issuer (Tutuka) linked to the BIN for authentication and approval</li>
<li>The Issuer (Tutuka) receives the payment request from the Card scheme and verifies the card details. Tutuka identifies the product type (<a href="https:developer.sprint.paymentology.com/card-api/">Card API</a> or <a href="https:developer.sprint.paymentology.com/companion-api/">Companion API</a>)</li>
<li>If the card is registered for Card API, Tutuka checks the balance on the card. If there are insufficient funds for the purchase, a decline response is sent. If there are sufficient funds, Tutuka reserves the funds on the card and an authorisation response is sent to the Card scheme</li>
<li>If the card is registered for Companion API, Tutuka routes the payment request to the wallet provider who responds to Tutuka with an approval or decline based on the wallet balance. Tutuka sends this response to the Card scheme</li>
<li>The Card scheme routes the authorisation or decline response to the Acquirer</li>
<li>The Acquirer sends the response to the Merchant and the Cardholder</li>
<li>The transaction is completed once funds are deducted from the Cardholder’s balance and settled in the Merchant’s account</li>
</ul>

<p>**Payment-lifecycle.png IMAGE GOES HERE.**</p>

<h1>Types of Transactions</h1>
<h2>Card Present</h2>
<p>POS Systems with card readers – This is a Point Of Sale terminal where you insert/swipe your card to pay for the transaction.</p>
<p>Contactless enabled terminals – This is a terminal which allows you tap your card using near-field communication.</p>
<p>ATM Transactions – This is when you use your physical card at an ATM to withdraw cash.</p>
<p><a href="https:developer.sprint.paymentology.com/companion-api/manage-funds/automated-fuel-dispensers-afd-transactions/">AFD Transactions</a> – Automated Fuel Dispensers (AFD) are unattended terminals at fuel stations that allow cardholders to purchase fuel without requiring an attendant. The emergence of AFD transactions has revolutionized the fuel purchase industry and greatly benefitted both merchants and customers. (Applicable to Asia only)</p>
<h2>Card Not Present</h2>
<p><a href="https:developer.sprint.paymentology.com/companion-api/tokenization2/">Tokenization</a> – Tokenization is the process of substituting the card’s sensitive data, such as an account number, with non-sensitive, surrogate data, called a token. The PAN (Primary Account Number) is usually replaced with a unique string of numbers that acts as a secure reference to the card.</p>
<p><a href="https:developer.sprint.paymentology.com/qr-payments-api/">QR Payments</a> – The QR Payments plug-in allows you to create a contactless merchant payment system where customers can make electronic payments by scanning a QR code from a smartphone application.</p>
<p><a href="https:developer.sprint.paymentology.com/companion-api/manage-funds/3d-secure/">3D Secure</a> – 3D Secure is an additional authentication step that provides an added layer of security for online card transactions (e-commerce) by reducing the risk of unauthorized card use due to the card not being physically present by sending an OTP to the cardholder when the card is being used.</p>

<h1><a href="https:developer.sprint.paymentology.com/companion-api/disputes/">Disputes</a></h1>
<ol>
<li><strong>Reversal<br >
</strong>A reversal is essentially a request for a transaction that was not completed and could have failed at a particular step of the transaction process. It is an advisement message to all parties of the transaction and ensures that the card and store of value are put back into their original state if a failed to deduct transaction had been initiated. If you sent a transaction and did not receive a confirmation that the transaction was successful, it could imply that the transaction did not reach the intended destination. Read more about Reversals <a href="https:developer.sprint.paymentology.com/companion-api/manage-funds/#Reversal">here</a>.</li>
<li><strong>Refund<br >
</strong>A refund is when funds are credited back to the customer’s card from a previously debited transaction. A refund could be processed when the customer returns previously purchased goods hence the funds which were settled to the merchant’s account need to move back to the cardholder’s account. Read more about Refunds <a href="https:developer.sprint.paymentology.com/companion-api/manage-funds/#Loadadjustment">here</a>.</li>
<li><strong>Chargeback<br >
</strong>A chargeback is the return of funds for a deduct transaction that was previously processed from a cardholder’s card balance, due to a successful dispute by the consumer regarding the transaction. Read about Chargeback related Dispute handling <a href="https:developer.sprint.paymentology.com/companion-api/disputes/">here</a></li>
</ol>
</a></strong></li></a></strong></li></a></strong></li></ol></a></h1></a></p></a></p></a></p></h2></a></p></p></p></p></h2></h1></p></li></li></li></li></li></a></a></li></li></li></li></ul></h2></strong></strong></a></a></strong></a></strong></strong></p></h2></p></h2></h2></p></b></p>
