---
title: Disputes
deprecated: false
hidden: false
metadata:
  robots: index
original_path: card-api
---
<h1>What is a Dispute?</h1>
<p>A dispute is a transaction that a cardholder/customer does not agree with and therefore requests that part of, or the entire transaction be reversed or refunded.</p>



<!-- spacing: desktop=20, mobile=10 -->


<h2>Types of Disputes:</h2>
<ol>
<li><strong>Reversal – </strong>A reversal is essentially a request for a transaction that was not completed and could have failed at a particular step of the transaction process. It is an advisement message to all parties of the transaction and ensures that the card and store of value are put back into their original state if a failed to deduct transaction had been initiated. If you sent a transaction and did not receive a confirmation that the transaction was successful, it could imply that the transaction did not reach the intended destination.</li>
<li><strong>Refund</strong> – A refund is when funds are credited back to the customer’s card from a previously debited transaction. A refund is processed when the merchant refunds the customer for returned goods and the funds which were settled to the merchant’s account need to move back to the cardholder’s account.</li>
<li><strong>Chargeback – </strong>A chargeback is the return of funds for a deduct transaction that was previously processed from a cardholder’s card balance, due to a successful dispute by the consumer regarding the transaction</li>
</ol>



<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<h1>How Disputes Work</h1>
<h2>What is a Chargeback?</h2>
<p>Once a dispute is raised, card issuers (like Paymentology) are able to submit a chargeback using a specific set of reason codes via the card scheme (Mastercard/Visa). There are a specific set of rules and timeframes set out by the card scheme that need to be followed in order to submit a chargeback.</p>
<p>Chargebacks can only be submitted if the transaction has settled i.e. funds have moved from the Issuer’s bank account to the merchant’s bank account for the transaction.</p>



<!-- spacing: desktop=20, mobile=10 -->


<h2>What is a Second Presentment?</h2>
<p>A second presentment (sometimes called a re-presentment) is the merchant’s opportunity to disagree with the chargeback request submitted by the Issuer on behalf of the cardholder. After a chargeback request has been submitted, the merchant/acquirer will have 10/35/45 days in which they may submit second presentments (also called pre-arbitration with some card schemes), depending on card scheme rules.</p>



<!-- spacing: desktop=20, mobile=10 -->


<h2>What is Pre-Arbitration and Arbitration?</h2>
<p>Following a receipt of a second presentment (also knows as re-presentment), the cardholder can choose to further dispute the second presentment by submitting a Pre-Arbitration. If the Pre-Arbitration is not successful, the cardholder can further proceed with submitting an Arbitration (the final option in the Dispute cycle) which in most cases will mean that the card scheme will rule in the case, either in favour of the Issuer or Acquirer depending on the merit of the case. There are specific timeframes for these processes which differ between the card schemes.</p>



<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<h1>Dispute Lifecycle</h1>
<p>Paymentology manages dispute handling and chargeback processing on behalf of our clients in three ways:</p>
<ol>
<li>Client initiated disputes</li>
<li>Batch chargeback submission</li>
</ol>



<!-- spacing: desktop=20, mobile=10 -->


<h2>1. Individual chargeback submission</h2>
<ul>
<li>Paymentology will provide the client with one of two chargeback dispute forms:<br />
– General dispute form<br />
– Fraud dispute form</li>
<li>The client’s merchant/customer will complete the form and select the appropriate reason</li>
<li>The client will send this dispute to Paymentology&#8217;s Global support team via email &#8211; support@paymentology.com</li>
<li>Based on the information provided, Paymentology will investigate the transaction being disputed</li>
<li>Paymentology will submit the chargeback using the appropriate chargeback reason code</li>
</ul>



<!-- spacing: desktop=20, mobile=10 -->


<h2>2. Batch chargeback process</h2>
<ul>
<li>The client can send Paymentology a list of disputes, using a predefined batch chargeback submission template that has been requested to chargeback. The client can define the chargeback reason code. Depending on whether the documentation is required or not, Paymentology will submit these chargebacks on the client’s behalf.</li>
<li>Paymentology will monitor and track the chargeback throughout the dispute lifecycle of submission, second presentments and arbitration.</li>
<li>Once the chargeback has been finalized, our Dispute Management Team will notify the client.</li>
<li>We will credit the card balance.</li>
<li>We will add the chargeback amounts to the Summary Settlement report so that reconciliation of funds can be done.</li>
<li>Paymentology will submit the chargeback using the appropriate chargeback reason code.</li>
</ul>



<!-- spacing: desktop=20, mobile=10 -->


<h1>Chargeback Process Flow</h1>
<p><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-2084" src="https://developer.sprint.paymentology.com/wp-content/uploads/2023/03/Chargeback-process-flow-v2.png" alt="" width="1280" height="720" /></p>



<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<h1>Mastercard: Dispute/Chargeback categories and timeframes</h1>
<p>When the transaction was completed with electronically recorded card information (whether card-read or key-entered), the acquirer has a maximum of seven calendar days after the transaction date to present the transaction to the issuer. A pending authorization should not be reversed before the seven calendar days. However, An issuer must accept a transaction submitted beyond the applicable time frame when the account is in good standing or the transaction can be honored.</p>
<p>There are four categories for chargeback processing:</p>



<!-- spacing: desktop=20, mobile=10 -->


<!-- unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"Mastercard Categories and Timeframes","table":{"use_header":true,"header":[{"c":"REASON CODE"},{"c":"REASON CODE DESCRIPTION"},{"c":"TIMEFRAME"}],"caption":false,"body":[[{"c":"4808"},{"c":"Authorization-related Chargeback"},{"c":"90 calendar days"}],[{"c":"4853"},{"c":"Cardholder dispute"},{"c":"120 calendar days"}],[{"c":"4837/4849/4870/4871"},{"c":"Fraud <br>\n- No cardholder authorization <br>\n- Questionable merchant activity <br>\n- Chip liability shift <br>\n- Chip liability shift - Lost/Stolen/ Never Received Issue (NRI) fraud "},{"c":"120 calendar days"}],[{"c":"4834"},{"c":"Point-of-interaction error"},{"c":"90 calendar days but for ATM related disputes - 120 calendar days apply"}]]}} -->


<!-- spacing: desktop=20, mobile=10 -->


<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/Dispute-Resolution-Form-Fraud.docx">Dispute Resolution Form &#8211; Fraud</a></p>
<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/Dispute-Resolution-Form.docx">Dispute Resolution Form</a></p>



<!-- spacing: desktop=20, mobile=10 -->


<!-- unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":false,"text":"<p>Mastercard chargeback collaboration period is between 24-72 hours. Chargebacks can take up to 72 hours to reflect as processed by Mastercard. This means that the chargeback is actually paused for that period and the <strong>45 days waiting for second presentment</strong> only starts from the date the chargeback is actually processed. If no second presentment is received within 45 days, we automatically load the funds thereafter.</p>\n<p><strong>Please be informed that all Mastercard chargebacks will have to wait for 48 days to see if a chargeback is successful (no second presentment) and then the funds will be loaded. Our Dispute Team will notify due date on each chargeback case accordingly.</strong></p>\n"}]} -->


<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<h1>Visa: Dispute/Chargeback categories and timeframes</h1>
<p>Most disputes have 120 days time frame but for some such as, Authorization related are only 75 days.</p>
<p>There are four categories for chargeback processing:</p>



<!-- spacing: desktop=20, mobile=10 -->


<!-- unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"FRAUD"},{"c":"AUTHORIZATION"},{"c":"PROCESSING ERRORS"},{"c":"CONSUMER DISPUTES"}],"caption":false,"body":[[{"c":"EMV Liability Shift Non-Counterfeit Fraud"},{"c":"Visa Fraud Monitoring Program"},{"c":"Late Presentment"},{"c":"Merchandise/Services not received "}],[{"c":"EMV Liability Shift Non-Counterfeit Fraud"},{"c":"Declined Authorization"},{"c":"Incorrect Transaction Code"},{"c":"Cancelled Recurring"}],[{"c":"EMV Liability Shift Non-Counterfeit Fraud"},{"c":"No Authorization"},{"c":"Incorrect Currency"},{"c":"Not as Described or Defective Merchandise/Services"}],[{"c":"EMV Liability Shift Non-Counterfeit Fraud"},{"c":""},{"c":"Incorrect Account Number"},{"c":"Counterfeit Merchandise"}],[{"c":"Visa Fraud Monitoring Program"},{"c":""},{"c":"Incorrect Amount"},{"c":"Misrepresentation"}],[{"c":""},{"c":""},{"c":"Duplicate Processing/Paid by Other Means"},{"c":"Credit Not Processed"}],[{"c":""},{"c":""},{"c":"Invalid Data"},{"c":"Cancelled Merchandise/Services"}],[{"c":""},{"c":""},{"c":""},{"c":"Original Transaction Not Accepted"}],[{"c":""},{"c":""},{"c":""},{"c":"Non-Receipt of Cash or Load Transaction Value"}]]}} -->


<!-- spacing: desktop=20, mobile=10 -->


<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/Visa-Generic-Dispute-Form.docx">Visa Generic Dispute Form</a></p>



<!-- spacing: desktop=20, mobile=10 -->


<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<h1>What is a Fraud Dispute?</h1>
<p>When a cardholder says that they do not recognize transactions and have no knowledge of the transactions and were not in the vicinity where the said transactions were performed – and their card was in their possession at the time of the the transaction i.e. they did not attempt the transaction at all.</p>
<p>For all Fraud related chargebacks, we have to report the fraudulent transaction to the various card schemes on their respective platforms:</p>
<ul>
<li>Mastercard – Fraud Center/SAFE</li>
<li>Visa – VROL</li>
<li>UPI – FRM</li>
</ul>
<p>If a transaction was processed with <a href="https://developer.sprint.paymentology.com/companion-api/manage-funds/3d-secure/">3D Secure</a>, we are not able to submit a Fraud chargeback therefore, the first step is to establish if there was a 3D Secure validation done.</p>
