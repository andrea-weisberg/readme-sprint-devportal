---
title: Remote Messaging API
deprecated: false
hidden: false
metadata:
  robots: index
---
<p>Paymentology will notify clients on 2nd Presentments. Remote messaging API allows Paymentology to call you to send administrative advice messages. These advice messages are sent using webhook-like schema. If you are integrating the service, you must create an endpoint accessible from the Paymentology network, which would be able to process the requests outlined below.</p>

<h2>How it works:</h2>
<ul>
<li>All messages are sent as HTTP POST requests.</li>
<li>Message content is always a JSON document.</li>
<li>method structure to be defined, and should correspond to the schema of the JSON document sent.</li>
<li>The message type (eg. chargeback.notification) is to be included in the JSON message as messageType. The message will be sent using the client-supplied URL eg.<a href="http:www.example.com/api/endpoint">http://www.example.com/api/endpoint</a></li>
<li>The messageData will contain KLV data related to the chargebacks.</li>
<li>In the code samples to be provided, we use cURL to send requests</li>
<li>In the code samples to be provided, we use a mock endpoint for testing – <a href="https:api.tutuka.com/remoteMessaging/v1_0/jsonMock.cfm">https://api.tutuka.com/remoteMessaging/v1_0/jsonMock.cfm</a></li>
</ul>

<h2>Available methods</h2>
<ul>
<li><a href="https:developer.sprint.paymentology.com/chargeback-api/remote-messaging-api/remote-messaging-api-chargeback-notification/">Remote Messaging API: chargeback notification</a></li>
</ul>
</a></li></ul></h2></a></li></li></li></a></li></li></li></li></ul></h2></p>
