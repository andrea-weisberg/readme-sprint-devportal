---
title: eCommerce report
deprecated: false
hidden: false
metadata:
  robots: index
---
<p data-renderer-start-pos="25">A report that shows successful and failed Ecommerce transactions along with associated eCommerce fees.</p>
<p data-renderer-start-pos="25">The report includes the following details:</p>
<ul>
<li data-renderer-start-pos="71"><strong data-renderer-mark="true">TransactionID – </strong>it’s a reference for the transaction</li>
<li data-renderer-start-pos="127"><strong data-renderer-mark="true">TrackingNumber</strong> – this is a unique 15-digit tracking identifier for the card.</li>
<li data-renderer-start-pos="207"><strong data-renderer-mark="true">TransactionDescription </strong>– this is a description of the merchant.</li>
<li data-renderer-start-pos="274"><strong data-renderer-mark="true">TransactionAmount</strong> – the value of the transaction</li>
<li data-renderer-start-pos="326"><strong data-renderer-mark="true">TransactionDate </strong>– This is the authorization date of the transaction</li>
<li data-renderer-start-pos="397"><strong data-renderer-mark="true">MerchantIdentitifer</strong> – this is numeric identifier of the merchant. Usually 15 digits.</li>
<li data-renderer-start-pos="485"><strong data-renderer-mark="true">Fee</strong> – this is the value of a fee the card has incurred for the transaction. Fee type must be one of the below:
<ul>
<li data-renderer-start-pos="592">51 – Ecommerce Fee</li>
<li data-renderer-start-pos="614">52 – Online Fee</li>
<li data-renderer-start-pos="633">6 – POS Purchase Fee</li>
</ul>
</li>
<li data-renderer-start-pos="702"><strong data-renderer-mark="true">3DS </strong>– specifies whether 3DS authentication occurred prior to the authorisation.</li>
<li data-renderer-start-pos="785"><strong data-renderer-mark="true">SuccessfulTransaction</strong> – specifies whether the transaction was approved or declined.</li>
<li data-renderer-start-pos="872"><strong data-renderer-mark="true">TransactionFeeID</strong> – the identifier of the transaction fee incurred.</li>
<li data-renderer-start-pos="942"><strong data-renderer-mark="true">TransactionFeeDescription</strong> – describes the transaction fee.</li>
<li data-renderer-start-pos="1004"><strong data-renderer-mark="true">TransactionFeeDate</strong> – the date in which the transaction fee was applied.</li>
<li data-renderer-start-pos="1079"><strong data-renderer-mark="true">DeclineReason</strong> – describes why the transaction was declined. If the transaction was successful then this filed is left blank.</li>
<li data-renderer-start-pos="1207"><strong data-renderer-mark="true">CaptureType</strong><em data-renderer-mark="true"> – </em>Capture type must be one of the below:
<ul>
<li data-renderer-start-pos="1256">ECOM – Transaction captured online</li>
<li data-renderer-start-pos="1294">MAG – Magnetic Stripe captured transaction</li>
<li data-renderer-start-pos="1340">MAN – Manually captured transaction</li>
<li data-renderer-start-pos="1379">ECOF – Online Card On File transaction</li>
</ul>
</li>
<li data-renderer-start-pos="1425"><strong data-renderer-mark="true">CaptureMode</strong> – this is the respective capture mode of the card’s transaction. Capture Mode must be one of the below:
<ul>
<li data-renderer-start-pos="1537">MAG – Magnetic Stripe captured transaction</li>
<li data-renderer-start-pos="1583">EMV – Electronic chip captured transaction</li>
<li data-renderer-start-pos="1629">ECOM – Transaction captured online (with no 3DS authentication)</li>
<li data-renderer-start-pos="1696">3DS – Transaction captured online using 3DS authentication</li>
<li data-renderer-start-pos="1758">MAN – Manually captured transaction</li>
<li data-renderer-start-pos="1797">NFC – Transaction captured via a Near Field Communication device</li>
</ul>
</li>
<li data-renderer-start-pos="1869"><strong data-renderer-mark="true">Recurring</strong> – specifies whether the transactions is a once off or recurring through COF method.</li>
</ul>
<p> </p>

<h2>Report format</h2>

<h2>Report time frame</h2>

<h2>Report sample</h2>
<p>**EcommerceTransactions_CampaignName_YYYYMMDD-.png IMAGE GOES HERE.**</p>

<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2023/12/EcommerceTransactions_CampaignName_YYYYMMDD.csv">EcommerceTransactions_CampaignName_YYYYMMDD.csv</a></p>

