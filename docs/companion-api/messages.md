---
title: Messages
deprecated: false
hidden: false
metadata:
  robots: index
---
<p><strong>These are two types of messages that Paymentology Sprint can send to a client:</strong></p>
<p> </p>
<h2>1. Administrative Messages</h2>
<p>These messages are <strong>sent to the client to complete certain actions</strong>.</p>
<p> </p>
<h3>Use cases:</h3>
<ul>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/#AdminsitrativeMessage3DSecureOTP">3DS OTP authentication</a> – Paymentology will send OTP messages to the fintech this will be sent on to the card holder to input during checkout</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/#AdministrativeMessage">Token digitization</a> – During digitization, if authentication is required Paymentology will pass the authentication OTP to the fintech, the OTP will be passed to the card holder to complete digitization</li>
<li><a href="https://developer.sprint.paymentology.com/administrative-message-values/">Token management notifications</a> – Paymentology will send token update notifications to the fintech if the status of the token changes</li>
</ul>
<p> </p>
<p> </p>
<p> </p>



\{/* spacing: desktop=20, mobile=10 */\}


<h2>2. Stop Messages</h2>
<p>These messages are <strong style="font-size: 16px;">sent to notify you if Paymentology stopped the companion card.</strong><span style="font-size: 16px;"> For example, if a validation process has failed to pass, Paymentology would stop the card for security reasons and send a notification to that effect. This requires making a call to the </span><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/stopcard/"><span class="xml-highlight">StopCard</span></a><span style="font-size: 16px;"> method.</span></p>
