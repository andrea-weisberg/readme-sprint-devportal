---
title: Help
deprecated: false
hidden: false
metadata:
  robots: index
---
<h2 id="intro">How SimPOS works</h2>
<p>SimPOS is used to test the flow of a virtual card transaction over the Companion Card API, and to check that all components are working.</p>
<ul>
<li>When a transaction is performed on SimPOS, a message is sent to Paymentology’s Sprint test card platform (in the same format that would be received from a POS with all the transaction details included).</li>
<li>The card platform then creates a “<strong>Deduct</strong>” call message using the wallet id linked to the card and includes some of the transaction details received in the message received for the transaction.</li>
<li>The call message Paymentology creates is then sent to the web service URL provided for the wallet platform, over the <strong>Remote API</strong>.</li>
<li>Once the call message is received and processed on the wallet side, an XML response needs to be sent to the card platform to approve or decline the transaction. This is where a <strong>local API</strong> call message is sent to the Paymentology Sprint platform using a <strong>Result Code</strong> included in the <strong>Companion Card API</strong> documentation.</li>
<li>Once the card platform receives the response, a response is then sent to SimPOS to either approve or decline the transaction.</li>
</ul>

<h2 id="intro">Testing with SimPOS</h2>
<p>Things to check:</p>
<ul>
<li>Did the wallet platform receive a “<strong>Deduct</strong>” call message for the transaction from Paymentology?</li>
<li>Did the wallet platform deduct funds from the wallet for the transaction?</li>
<li>Did the wallet platform send a response to the Paymentology Sprint local API?</li>
<li>What was the response on SimPOS for the transaction?</li>
<li>Does the response received on SimPOS match the response sent to Paymentology’s Sprint platform or not?</li>
</ul>

<h2>How to use SimPOS</h2>
<ol>
<li>Go to <a href="https://developer.sprint.paymentology.com/tools/simpos/">SimPOS</a> under <a href="https://developer.sprint.paymentology.com/tools/">Tools</a></li>
<li>Click on the “<strong>Web</strong>” tab</li>
<li>Enter the card number, expiry date and CVV for the test card that was created using <span class="xml-highlight">CreateLinkedCard</span> method on the <strong>local API</strong></li>
<li>Enter a random amount for the test transaction</li>
<li>Enter a random merchant</li>
<li>Click on “<strong>Swipe</strong>” button</li>
<li>Wait for “<strong>Transaction result pop-up</strong>” which will show various response codes. Refer to the full list of response codes on the API documentation page.</li>
</ol>

<p>You can find a list if SimPOS Response codes <a href="https://developer.sprint.paymentology.com/tools/simpos/simpos-result-codes/">here</a>.</p>
