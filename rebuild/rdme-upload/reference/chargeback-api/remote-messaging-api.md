---
title: Remote Messaging API
category:
  uri: Chargeback API
slug: remote-messaging-api
position: 5
parent:
  uri: chargeback-api
---

Paymentology will notify clients on 2nd Presentments. Remote messaging API allows Paymentology to call you to send administrative advice messages. These advice messages are sent using webhook-like schema. If you are integrating the service, you must create an endpoint accessible from the Paymentology network, which would be able to process the requests outlined below.

## How it works:

- All messages are sent as HTTP POST requests.

- Message content is always a JSON document.

- Method structure to be defined, and should correspond to the schema of the JSON document sent.

- The message type (eg. chargeback.notification) is to be included in the JSON message as messageType. The message will be sent using the client-supplied URL eg.[http://www.example.com/api/endpoint](http://www.example.com/api/endpoint)

- The messageData will contain KLV data related to the chargebacks.

- In the code samples to be provided, we use cURL to send requests

- In the code samples to be provided, we use a mock endpoint for testing – [https://api.tutuka.com/remoteMessaging/v1_0/jsonMock.cfm](https://api.tutuka.com/remoteMessaging/v1_0/jsonMock.cfm)

## Available methods

- [Remote Messaging API: chargeback notification](/api-reference/chargeback-api/remote-messaging-api-chargeback-notification)
