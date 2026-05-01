# Reconciliation

Reconciliation is the process of matching transactions reported by Paymentology to the transactions recorded on the wallet platform to ensure that the amount settled by the card scheme is accurate.

Reconciliation Process

# [Authorizations](#authorization)

Paymentology provides a daily mark-off file

The mark-off file shows successful transactions that Paymentology has processed on behalf of the Issuer

The Issuer/client will compare Paymentology's transactions to the wallet platform

# [Settlements](#settlements)

Paymentology provides a daily summary settlement report as well as a daily detailed settlement report

The Issuer/client will compare the net settlement amount with the amount that the card scheme has debited from the Issuer/client pool account

# [Revenue](#revenue)

Paymentology provides a daily forex gains report showing all revenue earned by the Issuer/client

The Issuer/client also has sight of the daily interchange earned from the summary settlement report

# [Fraud](#fraud)

Paymentology will report on all fraud cases via the card scheme's online portal

# Authorization reconciliation process

What is Authorization?

Authorization is the process of checking the available funds on a card in order to reserve funds when the card is used for a purchase.

# Paymentology

Paymentology will daily generate a mark-off file showing all transactions successfully processed on behalf of the Issuer/client

# Issuer/Client

The Issuer/client will daily generate a similar mark-off file

The Issuer/client will compare Paymentology's transaction list to their list

# Support

If there are any discrepancies, the Issuer/client will raise these with the Paymentology support team to investigate by logging a ticket via your Zendesk Portal, selecting the * Report a Service Incident * form, and then choosing * Reporting * and * Discrepancy * under the Request Type.

## Authorization reports

The report linked below assists client's with authorization reconciliation.

- [Mark-off file](/reports/companion-api/mark-off-file)

# Settlements

What is a settlement?

A settlement is when funds are deducted from the Issuer/client's bank account and deposited in to a merchants bank account to settle a card transaction.![](https://developer.sprint.paymentology.com/wp-content/uploads/2024/07/Dual-message-settlement-process.png)

## Settlement process:

Step 1: 1 – 7 days after the successful authorization, merchants will request payments from the card association

Step 2: The card association debits the Issuing bank (the pool account that the card belongs to) and moves the funds to the Acquiring bank of the Merchant. The Acquiring bank then moves the funds to the merchants account.

Step 3: The card scheme sends Paymentology clearing files, containing each individual settled transaction. New forex conversion rates will be calculated for all international transactions and interchange is calculated and applied.

Different card schemes have different clearing cycles depending on the region/country and there can be up to 8 clearing cycles per day. All clearing cycles are included in our settlement reports. NOTE: Visa's settlements are online.

Step 4: Paymentology will compare all settled transactions to previously authorized transactions and match these together. Paymentology creates a summary settlement report and calculates the net settlement amount that will be debited by the card association. Forex currency gains are calculated based on settlement amounts.

Step 5: The client will compare Paymentology's settlement amounts to the amount debited by the card scheme and the amount that is debited from their bank accounts.

## Revenue reports

The report linked below assists client's with revenue reconciliation and reporting:

- [Forex gains report](/reports/companion-api/forex-gains-report)

# Adjustment Handling

## Deduct Adjustments

- Negative forex fluctuation -> Issuer/client to absorb

- Settlement with no authorizations -> Issuer/client to debit customer's account

## Load Adjustments

- Positive forex fluctuation -> Issuer/client to absorb

- Refunds -> Issuer/client credit customer's account

## Settlement reports

The reports linked below assist client's with settlement reconciliation.

- [Summary settlement report](/reports/companion-api/summary-settlement-report)

- [Detailed settlement report](/reports/companion-api/detailed-settlement-report)

# Revenue

What is Revenue?

Revenue is the income earned from Forex gains and interchange.

## Forex Fluctuation![Forex fluctuation flow](https://developer.sprint.paymentology.com/wp-content/uploads/2023/03/Forex-fluctuation-v2.png)

All adjustments are recorded in the mark-off file

# Fraud

What is Fraud?

Fraud is a false or illegal transaction which results in a loss of funds. Paymentology provides the following Risk Management features:

- Transaction Limits - Paymentology allows you to implement transaction limits per card or program. If the ceiling is reached, no further transactions are permitted.

- Usage - Paymentology allows you to specify the payment methods that the card can be used with. If there is an attempted use of the card for an unspecified payment method, the transaction will fail and send a fraud alert.

- Additional settings - Paymentology allows you to implement additional settings to reinforce the security of cards and help with fraud prevention.

- Notifications - Paymentology lets you configure real-time notifications that keep customers informed about the state of their cards.

- Checks and controls - Paymentology allows you to implement a variety of Issuance checks, Spend controls and Authorization checks

Read more about Fraud and Risk [here](/guides/fraud)

## Dispute Handling

What is a Dispute?

A dispute is a transaction that a cardholder/customer does not agree with and therefore requests that part of, or the entire transaction be reversed or refunded.

### Types of Disputes:

- Reversal A reversal is essentially a request for a transaction that was not completed and could have failed at a particular step of the transaction process. It is an advisement message to all parties of the transaction and ensures that the card and store of value are put back into their original state if a failed to deduct transaction had been initiated.If you sent a transaction and did not receive a confirmation that the transaction was successful, it could imply that the transaction did not reach the intended destination.

- Refund A refund is when funds are credited back to the customer’s card from a previously debited transaction. A refund is processed when the merchant refunds the customer for returned goods and the funds which were settled to the merchant's account need to move back to the cardholder's account.

- Chargeback A chargeback is the return of funds for a deduct transaction that was previously processed from a cardholder’s card balance, due to a successful dispute by the consumer regarding the transaction

Read about Chargeback related Dispute handling [here](/guides/disputes)
