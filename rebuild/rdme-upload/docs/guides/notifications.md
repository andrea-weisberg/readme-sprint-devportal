---
title: Notifications
category:
  uri: Guides
slug: notifications
position: 51
---

**Paymentology's Sprint Transaction Stream service allows API consumers to receive real-time notifications of the undertaken transactions. By subscribing to the notification service, consumers can know the status of transactions in real-time.**

You can use the service for various purposes, including:

- Customizing customer transaction notifications.

- Tracking payment declines and notifying customers to improve their awareness.

- Monitoring fraudulent transactions to mitigate your liability.

- Creating targeted promotional messages.

- Quickly reviewing customer spending patterns by time period.

It enables you to receive real-time transaction information for the following types of transactions:

- Successful transactions

- Reversed transactions

- Verified transactions

- Declined transactions

You can get the following information for each undertaken transaction:

- Customer reference account number

- Transaction time and date

- Merchant name

- Decline reason code

- Transaction amount

- MCC (Merchant Category Code)

## What should the Transaction Stream be used for?

Any activities or notifications that can benefit from real time transaction monitoring and alerting. For example:

- Customizing customer transaction notifications

- Tracking payment declines and notifying customers to improve their awareness

- Monitoring fraudulent transactions to mitigate your liability

- Creating targeted promotional messages

- Quickly reviewing customer spending patterns by time period

## What should the Transaction Stream not be used for?

Because of the transient nature of the transaction stream, and the fact that delivery is not guaranteed, the stream cannot be used for any purposes that require complete and accurate information. This includes:

- Any kind of financial reconciliation

- Any kind of data reporting/ financial reporting

## What happens if some transactions from the Transaction Stream are lost/not received?

This can happen due to the nature of a streaming service. Every effort is made to ensure that all data is streamed timeously, but if records are not sent by us, or not received by you, those records are lost from the stream. Although not ideal:

- The stream cannot be resent later because the transactions are now stale, and there is no benefit to real-time notifications

- No financial activity will be impacted though, and all transactions will still be reflected in your daily files

## PubNub and the Transaction Stream Flow

Paymentology utilises PubNub (https://www.pubnub.com) for it’s real-time transaction streaming. PubNub is a third party, secure, real-time publish/subscribe messaging API. It allows one to send information from the Publisher (Paymentology) to Subscribers (Clients) in real time. In our case the information is a list of processed transactions.

Paymentology has used this service so that a client can simply subscribe to this service to receive information when a transaction is processed. This is a real-time service so clients will see transaction information as a transaction is completed. A client can then decide how to capture, store and use this information.

### How does it work

![Pubnub transaction stream flow](https://files.readme.io/0971789d6901565f21675e0ee3cc0b616efa79eeb6db8e3f8facd2e2cd1d6705-4554319bd482bae8077e6efe9414b1bf6823d7a8e2bda56f3ae635e12c966985-Diagram-for-Sprint-Developer-Porta_Lightmode-3.png)

- Transaction gets received from the VoucherEngine platform. As we receive it from the financial network and its being categorized according to the [Transaction types](#transaction) below

- VoucherEngine is determining which Campaign the transaction belongs to, if that transaction needs to be published, and based on those - it submits it to the respective CHANNEL (which is the Campaign UUID) to PubNub

- The Client Implementation is using their credentials (Terminal ID and password) to authenticate with VoucherEngine Events Authority API by making a request. See the [Get Authentication data](#authentication) section for an example of the request

- The Client Implementation receives the Paymentology response. See the [Get Authentication data](#response) section for an example of the response

- The Client Implementation uses the Paymentology response (specifically they have to use SUBKEY, CHANNEL, SUBSCRIBEURI and AUTH) so as to initiate a connection dictated by the SUBSCRIBEURI. The Client Implementation needs to keep that connection open listening to that CHANNELRespective documentation using the official PubNub Java SDK can be found [here](https://www.pubnub.com/docs/sdks/java#publish-and-subscribe) - It is best if the Client sets up an asynchronous callback when there is a new transaction received so as to be properly processed on their end - The PubNub SDK already covers the section of creating the callbacks but you can also have a look at the bottom with code samplesRespective documentation using the official PubNub REST API can be found [here](https://www.pubnub.com/docs/rest-api#publish-subscribe-subscribe-get) - It is best if the Client sets up an asynchronous callback when there is a new transaction received so as to be properly processed on their end - The PubNub REST API already covers the section of creating the callbacks but you can also have a look at the bottom with code samples

- The Client Implementation starts receiving transactions while that connection remains open from the Clients Implementations end. The Client Implementation is responsible for refreshing the call explained at Step 3 within the TTL timespan which is also refreshing their AUTH tokenSteps 5 and 6 are strongly advised to be implemented by using the respective PubNub SDK based on the Client's preferable implementation language/ framework. Even though the PubNub system offers a RESTful API section that uses the HTTP protocol, it completely changes the way the system should work. For example: if the client choose that, they would have to make regular calls to PubNub so as to receive the transactions as they are done at that exact time

## **How to Integrate Transaction Stream**

Paymentology provides the Paymentology Events Authority API to allow you to integrate the Transaction Stream service into your use case.

The API lets you observe and ingest information about transactional events, as they happen and are processed by Paymentology. It is implemented as a REST HTTP API using a custom authentication mechanism. The API connection is secured using TLS.

Paymentology also leverages the [PubNub](https://www.pubnub.com/) platform for powering the real-time transaction notification system. PubNub utilizes a Publishing/Subscribing model for accomplishing real-time communication.

This model consists of two important components:

- **Channels** —these are the transient paths over which your data is transmitted.

- **Messages** —these are the data you want to send to recipients.

Essentially, to enable users to receive the notifications sent to a particular channel, they need to subscribe to it. If you publish a message to a channel, the notification will be delivered to every user subscribed to that channel.

These are the steps to follow to implement the Transaction Stream feature into your application:

- Get authentication data

- Subscribe users to channel

- Get the notification feed

Let’s talk about the steps in more detail.

### **Step 1: Get authentication data**

First, you need to authenticate against the events system and get session and listening endpoint information before consuming the PubNub API.

So, you need to make a GET request to Paymentology's PubNub Authenticate REST API.

To consume the API, you need to call the following endpoint:

**https://api.voucherengine.com/pubnub/json.cfm**

Furthermore, the API requires the following query string parameters:

GET request parameters need to be URL encoded otherwise the checksum is not calculated correctly

This call is a recurring one. The Client must be calling the authentication before the TTL (Time To Live - in minutes - default is 86400 mins ie, 60 days) value expires. This is done for security reasons

Here is an example of a GET request to the REST API:
https://api.voucherengine.com/pubnub/json.cfm?checksum=00F3ED1C44826F692BCF47D654A085250879E192&deviceID=TESTING_TTK&method=Authenticate&terminalID=0090312345&transactionDate=20180524T12:00:00&transactionID=EI152698153428

The above request will give the following response:

{
"SUBKEY":"sub-c-21e941e8-e37c-11e6-b076-0619f8945a4f",
"CHANNEL":"8FF7B14F-155D-00FA-4D35CCE727CEA255",
"SUBSCRIBEURI":"https://pubsub.pubnub.com/v2/subscribe/",
"serverTransactionID":"94a90010-c531-46d5-9faa-2772dc121196",
"AUTH":"58426CDE-B5CB-423C-B72D-F3C84C26A1CD",
"terminalID":"0090312345",
"clientTransactionID":"49716b6b-1cfa-4355-bef3-1e71281c1862",
"TTL":"86400"
}

Here is a description of the above result:

Here is a description of the HTTP response status codes:

### **Step 2: Subscribe users to channel**

Next, you need to use the above response data to subscribe users to your channel so that they can receive notifications sent to that channel.

This will involve making a GET request to the [PubNub REST API](https://www.pubnub.com/docs/pubnub-rest-api-documentation#publish-subscribe-subscribe-get), via the **subscribe** endpoint:

**https://pubsub.pubnub.com/v2/subscribe/**

Note that the endpoint corresponds to the **SUBSCRIBEURI** value from the previous response data.

You need to specify the following path parameters:

- **SUBKEY** —this is your PubNub subscribe API key.

- **CHANNEL** —this is the channel name you are subscribing users to.

- **Callback** —this is a JSONP callback name. If there is none, just specify it as 0 (zero).

- **Timetoken** —for the initial subscribe, just specify it as 0 (zero).

Furthermore, you need to specify the following query string parameters:

GET{SUBSCRIBEURI}/{SUBKEY}/{CHANNEL}/{CALLBACK}/{TIMETOKEN}?auth={AUTH}&uuid={SERVERTRANSACTIONID}

GET https://ps.pndsn.com/subscribe/mySubKey/ch1/myFunction/0?auth=authValue&uuid=db9c5e39-7c95-40f5-8d71-125765b6f561

The above request will give the following response:

{"t":{"t":"16081395170424173","r":7},"m":[]}

As you can see above, the response is an object that contains two elements:

- The first element is an object consisting of two values: **t** —timetoken and **r** —region.

- The second element is an array of messages delivered from the subscribed channel.

Generally, let’s look at all the possible data that could be returned from such a request:

Here is the Message (transaction) data structure that is accessible via “ **d** ” key above. Note that the structure is extensible and new fields may be added to all versions, as it’s meant to be a backwards compatible change. Remember to always refer to the most up-to-date version of this document for a complete listing of the fields.

Here are the response code listings:

For more information on Transaction Stream/PubNub Response Codes and how they relate to Network and Card Scheme Response Codes, you can refer to the [Response and action code mapping table](/guides/response-and-action-code-mapping).

Here are the possible capture modes:

### **Step 3: Get the notification feed**

{
"response_code": "1016",
"merchant_category_code": "5814",
"system_time": "1608225195",
"terminal_id": "T_ID",
"capture_mode": "ECOM",
"request_time": "1608243193",
"merchant": "FOOD PANDA (THAILAND) HUAYKWANG THA",
"balance": 0,
"amount": 7500,
"tracking_number": "T_NUMBER",
"transaction_time": "1608217993",
"reference": "T_REFERENCE",
"transaction_id": "T_ID",
"type": "deduct authorisation"
}

## Subscribing and Retrieval via PubNub SDK

A client will implement the service using one of the [available SDKs](https://www.pubnub.com/docs/platform/sdks#client-sdks) combining it with our custom authentication mechanism described in Step 1

However we are able to provide a sample Java application which the client can download, run and then expand upon to build their own integration:

- Example application source code: We provide source code of a very simple JAVA application which will connect to Paymentology's transaction publishing service, subscribe to a campaign, and then open a window on the screen which will flash up the merchant name whenever a transaction is made. This is not an actual running application that one can run on a PC but source code that can be used by the clients developers in their development software and make further use of it. To start working with this sample application, following steps need to be taken: 1. Ask your CE to enable PubNub feeds via your campaign settings..

- 2. Then in src/main/java/com/tutuka/transactionscroller the following data need to be updated:

//unique identifier for the device
private static final String DEVICE_NAME = "";
//your terminal ID that is attached to your campaign
private static final String TERMINAL_ID = "";
//your terminal password, associated with your terminal ID
private static final String TERMINAL_PASSWORD = "";

- DEVICE_NAME is any string that can identify you as the client., It is just something we log on our side. It could be f.e. CLIENT_NAME_APP

- TERMINAL_ID is the Terminal ID of your Default Issuing Merchant

- TERMINAL_PASSWORD is the Terminal Password of your Default Issuing Merchant

Update the HTTP Builder in the src/main/java/com/tutuka/transactionscroller/authorization/AuthRequest.java with the correct environment:

Example for UAT:

![](https://files.readme.io/c79873439a22fd2eb4d3422ef088c23fe06a233eb842f1282bfca33774a6974c-8faff2dfc34ea9feda24f93a734b9434551640a69234973870d4224fa156cc25-TTS-UAT-300x62.png)

After following the above steps, you can start testing and working with the code.

## **Troubleshooting the Transaction Stream**

Importantly, you should use the Transaction Stream service for informational purposes only. The messages are not preserved anywhere, and in case of connectivity issues or other technical hiccups, they may be lost permanently.

Typically, this is how the Transaction Stream service works:

- Paymentology creates the messages as the transaction is happening.

- PubNub retains the messages for up to a maximum of 16 minutes.

- The client (or the receiver) requests to receive the messages from PubNub.

After the messages are streamed, they are only available for a short window of no more than 16 minutes. For example, if a transaction happens at 8.00 a.m., and the receiver system is disconnected after 8.16 a.m., the messages about the transaction will no longer be available.

So, you have up to 16 minutes to receive and process the messages from PubNub. Paymentology does not have any way of tracking if the client has received and processed the messages.

Here is how to troubleshoot issues with the Transaction Stream service and mitigate any potential data loss:

- The receiver reloads to request a new authentication token from the PubNub Authenticate API.

- The receiver tries to reconnect to PubNub using the token:

- If there is an error in connecting to PubNub, the receiver restarts the process at step 1;

- If it happens again within a 1-minute interval, the receiver must wait at least 30 seconds before retrying.

- The receiver receives messages from the Transaction Stream service.

- If there is an error at any point, the receiver must restart the process at step 1.

- The receiver may choose to store messages locally, in a way feasible to them. As mentioned previously, PubNub does not retain any messages, and they will be unavailable for retrieval after 16 minutes.

# Transaction Types

Transaction types published are the following:

- deduct authorisation When the client make a payment(deduct) and the transaction come through Paymentology

- deduct authorisation reversal When the client failed to make a payment(deduct) and the transaction come through Paymentology

- refund authorisation When there is a refund from VISA/MasterCard/CUP

- refund authorisation reversal When there is a reversal of a refund from VISA/MasterCard/CUP

- payment authorisation When the client make a p2p (person-to-person) or money send transaction

- payment authorisation reversal When the client failed to make a p2p (person-to-person) or money send transaction and we have to reverse the transaction

- balance When the client request for balance

## **Environments**

The Transaction Streaming system is available in all the environments Paymentology uses. The underlying Pubnub infrastructure is the same in all the environments, the only differentiation that happens only from Pubnub is the CHANNEL.

So, below is a breakdown of the respective Authentication Urls per environment:

- For Test the URL for authenticating is: https://stream.test.tutuka.cloud/json

- For Vexdev the URL for authenticating is: https://apidev.tutuka.com/pubnub/json.cfm

- For UAT the URL for authenticating is: https://stream.uat.tutuka.cloud/json

- For Live/PROD the URL for authenticating is: [https://api.voucherengine.com/pubnub/json.cfm](https://api.voucherengine.com/pubnub/json.cfm)
