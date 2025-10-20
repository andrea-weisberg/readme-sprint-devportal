---
title: 3D Secure – Out of band Authentication
deprecated: false
hidden: false
metadata:
  robots: index
---

<h2>Overview of Out-of-Band (OOB) Authentication</h2>
<p>Out-of-Band (OOB) authentication is an advanced type of two-factor authentication (2FA) that necessitates an additional verification method via a distinct communication channel. It is an optional yet highly advised Challenge flow authentication method for conducting 3DS transactions for Paymentology clients.</p>
<p>This applies to both Mastercard and Visa transactions.</p>

<h3>Operational Workflow</h3>
<p>OOB serves as an authentication technique during the 3DS Challenge flow, steering the process to an Issuer’s mobile application rather than utilizing a one-time password (OTP) dispatched through SMS or text message.</p>
<p>During the 3DS Challenge flow, a Push Notification is sent to the Issuer’s mobile application. This initiates the sending of an authentication request to the cardholder. Subsequently, the cardholder undergoes authentication in the Issuer’s application using biometric methods like facial recognition or thumbprint, or a one-time password.</p>
<p>Following the authentication, the issuer communicates the result. If authenticated successfully, the merchant is enabled to initiate the authorization request, culminating in the completion of the transaction processing.</p>

<h3>Paymentology’s OOB Solution:</h3>
<p>In the OOB Solution, several participants play crucial roles:</p>
<ul>
<li><strong>Cardholder:</strong> Undertakes online purchases and authenticates via the Issuer Mobile app.</li>
<li><strong>ACS provider:</strong> The Access Control Server, authenticating the cardholder.</li>
<li><strong>Paymentology:</strong> Acts as the Issuer Processor, managing and executing the card transaction for the client.</li>
<li><strong>Issuing Client:</strong> Manages the OOB Issuer Mobile app and authenticates the client.</li>
</ul>

<h3>Interaction Sequence:</h3>
<ol>
<li><strong>Message Reception and Forwarding:</strong> Paymentology intercepts a JSON message from the ACS provider at a newly defined endpoint, enclosing pertinent details. This data is relayed to our clients (administrative messages to Companion clients and Remote Messaging to others). The client, upon receipt, acknowledges and responds directly to Paymentology’s request and contacts their cardholder.</li>
<li><strong>Transaction Approval/Denial:</strong> Subsequently, the client, in a separate API request sent to Paymentology’s Card or Companion API, sanctions or refutes the transaction. Post-receipt, this acknowledgment is forwarded from Paymentology to the ACS provider, culminating in the process.</li>
</ol>

<h2>Transaction flow</h2>
<p>When a 3DS enrolled cardholder performs an e-commerce transaction, authentication will need to take place:</p>
<h3>Request and initial response</h3>
<p>Paymentology is informed of the requested authentication by the ACS provider via an <strong>Authentication Request</strong> message.</p>
<ul>
<li>
<p>Paymentology check what type of product the client uses:</p>
<ul>
<li>
<p>If the client is a Companion API client, Paymentology sends an Administrative Message to the client<br />
MessageType: <strong><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/administrativemessage/#3DSAppAuth">3DSecureAppAuthentication</a><br />
</strong></p>
</li>
<li>If the client is a Card API client, Paymentology sends a RemoteMessaging message to the client<br />
MessageType: <strong><a href="https://developer.sprint.paymentology.com/card-api/api-reference/remotemessaging/#appauth">3DSecure.AppAuthentication</a> </strong></li>
</ul>
</li>
<li>
<p>The client does validation separately with their cardholder and the client acknowledges that they have received the <strong>3DSecure.AppAuthentication </strong>message (mentioned above) from Paymentology by responding.</p>
</li>
<li>
<p>Paymentology sends a message to the ACS provider to acknowledge they have forwarded the <strong>Authentication Request</strong> to the client.</p>
</li>
</ul>
<p><em>Request-and-initial-response-Light.png IMAGE GOES HERE.</em></p>

<h3>Final response and final confirmation</h3>
<p>Once the client completes the authentication with the cardholder:</p>
<ul>
<li>
<p>The client sends a request to the <strong>ThreeDSAuthenticationOutcome</strong> API saying whether the authentication was successful or not.</p>
<ul>
<li>Companion API client’s use this <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/threedsauthenticationoutcome/">ThreeDSAuthenticationOutcome</a> API.</li>
<li>Card API client’s use this <a href="https://developer.sprint.paymentology.com/card-api/api-reference/threedsauthenticationoutcome/">ThreeDSAuthenticationOutcome</a> API.</li>
</ul>
</li>
<li>
<p>Paymentology sends a message to the ACS provider containing the authentication outcome.</p>
</li>
</ul>
<ul>
<li>
<p>The ACS provider sends a final confirmation message to Paymentology.</p>
</li>
<li>
<p>Paymentology check what type of product the client uses:</p>
<ul>
<li>
<p>Companion API clients receive an Administrative Message from Paymentology.<br />
MessageType: <strong><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/administrativemessage/#3DSAppFinal">3DSecureAppFinalisation</a> </strong></p>
</li>
<li>
<p>Card API clients receive a RemoteMessaging message from Paymentology.<br />
MessageType: <a href="https://developer.sprint.paymentology.com/card-api/api-reference/remotemessaging/#appfinal"><strong>3DSecure.AppFinalisation </strong></a></p>
</li>
</ul>
</li>
</ul>
<p><em>Final-Response-and-Final-Confirmation-Light.png IMAGE GOES HERE.</em></p>

<h3>In summary:</h3>
<p>This secure and advanced authentication method ensures a seamless and secure transaction process, reinforcing the security apparatus by involving distinct communication channels for verification, thereby fostering enhanced security in online transactions. It is recommended for Paymentology clients aiming for robust and secure 3DS transaction processing.</p>
