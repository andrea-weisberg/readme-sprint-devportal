---
title: Lifecycle Management
deprecated: false
hidden: false
metadata:
  robots: index
original_path: card-api/tokenization
---
<p>Token lifecycle management refers to handling the different states of the token, from creation to expiry. All tokens have a lifecycle; that is, the series of events happening from the date of creation to the expiry date when they’re no longer valid. The expiry date is usually linked to the expiry date of the full PAN that was used for provisioning.</p>
<p>Token lifecycle management involves passing messages between Paymentology and MDES that notify the client of the following token events:</p>
<ul>
<li aria-level="1">Token stopped (suspended)</li>
<li aria-level="1">Token digitized (resumed)</li>
<li aria-level="1">Token deleted from Device (deleted from a specific digital device only)</li>
<li aria-level="1">Token deleted (deleted in its entirety)</li>
<li aria-level="1">Token re-digitized (re-digitized or updated)</li>
</ul>
<p>The token lifecycle events are managed through the <b>AdministrativeMessage</b> method. The <b>messageName </b>path parameter, required in the <b>AdministrativeMessage</b> method, specifies the name of the administrative messages sent to the client.</p>
<p>These are the possible values for the <b>messageName </b>data field when managing tokens:</p>
<ul>
<li aria-level="1"><a href="https://developer.sprint.paymentology.com/administrative-message-values/#stopped">Digitization.event.stopped</a> (token suspended)</li>
<li aria-level="1"><a href="https://developer.sprint.paymentology.com/administrative-message-values/#digitized">Digitization.event.digitized</a> (token resumed)</li>
<li aria-level="1"><a href="https://developer.sprint.paymentology.com/administrative-message-values/#deletedfromdevice">Digitization.event.Deleted_from_device</a> (token deleted from device)</li>
<li aria-level="1"><a href="https://developer.sprint.paymentology.com/administrative-message-values/#eventdeleted">Digitization.event.Deleted</a> (token deleted in its entirety)</li>
<li aria-level="1"><a href="https://developer.sprint.paymentology.com/administrative-message-values/#replacement">digitization.event.Replacement</a> (token re-digitized or replaced)</li>
</ul>
<p>Let’s talk about each of the values in detail.</p>
<p>&nbsp;</p>
<ol>
<li><a href="https://developer.sprint.paymentology.com/administrative-message-values/#stopped"><b>Digitization.event.stopped</b></a></li>
</ol>
<p>This is when Paymentology informs a wallet that a token has been stopped or suspended. Paymentology will request the MDES to stop all the token transactions associated with the card’s full PAN.</p>
<p>&nbsp;</p>
<ol start="2">
<li><a href="https://developer.sprint.paymentology.com/administrative-message-values/#digitized"><b>Digitization.event.digitized</b></a></li>
</ol>
<p>This is when Paymentology informs a wallet that a stopped token has been resumed. Paymentology will request MDES to reactivate the token mapped to the card.</p>
<p>&nbsp;</p>
<ol start="3">
<li><a href="https://developer.sprint.paymentology.com/administrative-message-values/#deletedfromdevice"><b>Digitization.event.Deleted_from_device</b></a></li>
</ol>
<p>This is when Paymentology informs a wallet that the account holder has deleted the token from the wallet program on their device.</p>
<p>&nbsp;</p>
<ol start="4">
<li><a href="https://developer.sprint.paymentology.com/administrative-message-values/#eventdeleted"><b>Digitization.event.Deleted</b></a></li>
</ol>
<p>This is when Paymentology informs the wallet that a token has been removed in its entirety.</p>
<p>&nbsp;</p>
<ol start="5">
<li><b><a href="https://developer.sprint.paymentology.com/administrative-message-values/#replacement">Digitization.event.Replacement</a> </b></li>
</ol>
<p>This is when Paymentology informs the wallet that a token has been re-digitized or replaced. For example, a token expiry date can be updated based on the new replaced card.</p>



<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<h2>Tokenization with Digital Wallets</h2>
<p>To allow for tokenization, issuers have historically needed to contract and integrate with each service or wallet separately. Every digital wallet has different capabilities for enabling tokenization.</p>
<p>On the Sprint platform, these are the IDs associated with the various digital wallet programs:</p>



<!-- spacing: desktop=20, mobile=10 -->


<!-- unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"Digital Wallet IDs","table":{"use_header":true,"header":[{"c":"WALLET NAME"},{"c":"WID (WALLET ID)"}],"caption":false,"body":[[{"c":"Apple Pay"},{"c":"103"}],[{"c":"Samsung Pay"},{"c":"217"}],[{"c":"Google Pay"},{"c":"216"}],[{"c":"M4M"},{"c":"327"}]]}} -->


<!-- spacing: desktop=20, mobile=10 -->


<p>Note that a 3-digit numeric value represents the IDs.</p>
<p>Notably, the digital wallets handle token provisioning differently. For example, Apple Pay and Google Pay work in the same way. So, for manual provisioning, an OTP will be issued, and they’ll be no OTP for push provisioning.</p>
<p>However, Samsung Pay does not issue an OTP, either for manual provisioning or push provisioning. So, during manual provisioning, Paymentology will just notify the client via <b><a href="https://developer.sprint.paymentology.com/administrative-message-values/#complete">Digitization.complete</a> </b>of the successful tokenization of the cardholder’s card on Samsung Pay.</p>
