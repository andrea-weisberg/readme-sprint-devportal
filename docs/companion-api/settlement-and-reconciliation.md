---
title: Reconciliation
deprecated: false
hidden: false
metadata:
  robots: index
---
<p><strong>Reconciliation is the process of matching transactions reported by Paymentology to the transactions recorded on the wallet platform to ensure that the amount settled by the card scheme is accurate.</strong></p>

<h1><a id="authorization"></a>Authorization reconciliation process</h1>
<p><b>What is Authorization?</b></p>
<p>Authorization is the process of checking the available funds on a card in order to reserve funds when the card is used for a purchase.</p>

<h2>Authorization reports</h2>
<p>The report linked below assists client’s with authorization reconciliation.</p>
<ul>
<li><a href="https:developer.sprint.paymentology.com/companion-api/reports/mark-off-file/">Mark-off file</a></li>
</ul>
<p> </p>

<h1><a id="settlements"></a>Settlements</h1>
<section id="tutuka-block-1" className="tutuka-block tutuka-block--text-full-width"><strong>What is a settlement?</strong></section>
<section className="tutuka-block tutuka-block--text-full-width">A settlement is when funds are deducted from the Issuer/client’s bank account and deposited in to a merchants bank account to settle a card transaction.</section>
<section></section>
<p>**Dual-message-settlement-process.png IMAGE GOES HERE.**</p>

<h2>Settlement process:</h2>
<p><strong>step 1:</strong> 1 – 7 days after the successful authorization, merchants will request payments from the card association</p>
<p><strong>step 2:</strong> The card association debits the Issuing bank (the pool account that the card belongs to) and moves the funds to the Acquiring bank of the Merchant. The Acquiring bank then moves the funds to the merchants account.</p>
<p><strong>step 3:</strong> The card scheme sends Paymentology clearing files, containing each individual settled transaction. New forex conversion rates will be calculated for all international transactions and interchange is calculated and applied.</p>
<p>Different card schemes have different clearing cycles depending on the region/country and there can be up to 8 clearing cycles per day. All clearing cycles are included in our settlement reports. <strong>NOTE:</strong> Visa’s settlements are online.</p>
<p><strong>step 4:</strong> Paymentology will compare all settled transactions to previously authorized transactions and match these together. Paymentology creates a summary settlement report and calculates the net settlement amount that will be debited by the card association. Forex currency gains are calculated based on settlement amounts.</p>
<p><strong>step 5:</strong> The client will compare Paymentology’s settlement amounts to the amount debited by the card scheme and the amount that is debited from their bank accounts.</p>

<h2>Settlement reports</h2>
<p>The reports linked below assist client’s with settlement reconciliation.</p>
<ul>
<li><a href="https:developer.sprint.paymentology.com/companion-api/reports/summary-settlement-report/">summary settlement report</a></li>
<li><a href="https:developer.sprint.paymentology.com/companion-api/reports/detailed-settlement-report/">Detailed settlement report</a></li>
</ul>

<h1><a id="revenue"></a>Revenue</h1>
<p><strong>What is Revenue?</strong></p>
<p>Revenue is the income earned from Forex gains and interchange.</p>
<h2>Forex Fluctuation</h2>
<p>**Forex-fluctuation-v2.png IMAGE GOES HERE.**</p>

<h2><b>Revenue reports</b></h2>
<p>The report linked below assists client’s with revenue reconciliation and reporting:</p>
<ul>
<li><a href="https:developer.sprint.paymentology.com/companion-api/reports/forex-gains-report/">Forex gains report</a></li>
</ul>

<h1>Adjustment Handling</h1>
<h2>Deduct Adjustments</h2>
<ul>
<li>Negative forex fluctuation -> Issuer/client to absorb</li>
<li>Settlement with no authorizations -> Issuer/client to debit customer’s account</li>
</ul>
<h2>Load Adjustments</h2>
<ul>
<li>Positive forex fluctuation -> Issuer/client to absorb</li>
<li>Refunds -> Issuer/client credit customer’s account</li>
</ul>

<h1><a id="fraud"></a>Fraud</h1>
<p><strong>What is Fraud?</strong></p>
<p>Fraud is a false or illegal transaction which results in a loss of funds. Paymentology provides the following Risk Management features:</p>
<ul>
<li>Transaction Limits – Paymentology allows you to implement transaction limits per card or program. If the ceiling is reached, no further transactions are permitted.</li>
<li>Usage – Paymentology allows you to specify the payment methods that the card can be used with. If there is an attempted use of the card for an unspecified payment method, the transaction will fail and send a fraud alert.</li>
<li>Additional settings – Paymentology allows you to implement additional settings to reinforce the security of cards and help with fraud prevention.</li>
<li>Notifications – Paymentology lets you configure real-time notifications that keep customers informed about the state of their cards.</li>
<li>Checks and controls – Paymentology allows you to implement a variety of Issuance checks, Spend controls and Authorization checks</li>
</ul>
<p>Read more about Fraud and Risk <a href="https:developer.sprint.paymentology.com/get-started/fraud/">here</a></p>
<h2>Dispute Handling</h2>
<p><strong>What is a Dispute?</strong></p>
<p>A dispute is a transaction that a cardholder/customer does not agree with and therefore requests that part of, or the entire transaction be reversed or refunded.</p>
<h3>Types of Disputes:</h3>
<ol>
<li><strong>Reversal </strong>A reversal is essentially a request for a transaction that was not completed and could have failed at a particular step of the transaction process. It is an advisement message to all parties of the transaction and ensures that the card and store of value are put back into their original state if a failed to deduct transaction had been initiated.If you sent a transaction and did not receive a confirmation that the transaction was successful, it could imply that the transaction did not reach the intended destination.</li>
<li><strong><strong>Refund</strong></strong>A refund is when funds are credited back to the customer’s card from a previously debited transaction. A refund is processed when the merchant refunds the customer for returned goods and the funds which were settled to the merchant’s account need to move back to the cardholder’s account.</li>
<li><strong>Chargeback </strong>A chargeback is the return of funds for a deduct transaction that was previously processed from a cardholder’s card balance, due to a successful dispute by the consumer regarding the transaction</li>
</ol>
<p>Read about Chargeback related Dispute handling <a href="https:developer.sprint.paymentology.com/companion-api/disputes/">here</a></p>
</a></p></strong></li></strong></strong></li></strong></li></ol></h3></p></strong></p></h2></a></p></li></li></li></li></li></ul></p></strong></p></a></h1></li></li></ul></h2></li></li></ul></h2></h1></a></li></ul></p></b></h2></p></h2></p></strong></p></a></h1></a></li></a></li></ul></p></h2></strong></p></strong></p></strong></p></strong></p></strong></p></strong></p></h2></p></section></section></strong></section></a></h1></p></a></li></ul></p></h2></p></b></p></a></h1></strong></p>
