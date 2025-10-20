---
title: Transaction Stream
deprecated: false
hidden: false
metadata:
  robots: index
---
## Transaction Stream

The Transaction Stream is a powerful feature that allows you to monitor and analyze transactions in real-time. It provides detailed insights into each transaction, including metadata, status, and execution details.

### Features

- Real-time transaction monitoring
- Detailed transaction metadata
- Execution status and logs
- Support for multiple transaction types

### Usage

To use the Transaction Stream, subscribe to the stream using the provided API endpoint. You will receive JSON objects representing each transaction as they occur.

```json
{
  "t": {
    "t": "16081395170424173",
    "r": 7
  },
  "m": []
}
```

Ensure you handle the stream efficiently to process transactions without delay. For more information, refer to the [Transaction Stream API documentation](https://example.com/transaction-stream-api).

**Paymentology’s Transaction Stream service allows API consumers to receive real-time notifications of the undertaken transactions. By subscribing to the notification service, consumers can know the status of transactions in real-time.**

You can use the service for various purposes, including:

- Customizing customer transaction notifications.
- Tracking payment declines and notifying customers to improve their awareness.
- Monitoring fraudulent transactions to mitigate your liability.
- Creating targeted promotional messages.
- Quickly reviewing customer spending patterns by time period.

It enables you to receive real-time transaction information for the following types of transactions:

- Successful transactions
- reversed transactions
- Verified transactions
- Declined transactions

You can get the following information for each undertaken transaction:

- Customer reference account number  
- Transaction time and date
- Merchant name  
- Decline reason code
- Transaction amount  
- MCC (Merchant Category Code)

## **How to Integrate Transaction Stream**

Paymentology provides the Events Authority API to allow you to integrate the Transaction Stream service into your use case. 

The API lets you observe and ingest information about transactional events, as they happen and are processed. It is implemented as a REST HTTP API using a custom authentication mechanism. The API connection is secured using TLS. 

The [PubNub](https://www.pubnub.com/) platform is levergaed for powering the real-time transaction notification system. PubNub utilizes a Publishing/Subscribing model for accomplishing real-time communication.

This model consists of two important components:

- **Channels**—these are the transient paths over which your data is transmitted.
- **Messages**—these are the data you want to send to recipients.

Essentially, to enable users to receive the notifications sent to a particular channel, they need to *subscribe* to it. If you *publish* a message to a channel, the notification will be delivered to every user subscribed to that channel. 

These are the steps to follow to implement the Transaction Stream feature into your application:

- Get authentication data 
- Subscribe users to channel
- Get the notification feed

Let’s talk about the steps in more detail.

### **step 1: Get authentication data**

First, you need to authenticate against the events system and get session and listening endpoint information before consuming the PubNub API.

So, you need to make a GET request to Paymentology’s  PubNub Authenticate REST API.

To consume the API, you need to call the following endpoint:

**https://api.tutuka.com/pubnub/json.cfm**

Here is an example of a GET request to the REST API:

[https://api.tutuka.com/pubnub/json.cfm?method="Authenticate&deviceID=DUNNE_PC&transactionID=49716b6b-1cfa-4355-bef3-1e71281c1862&transactionDate=2017-02-01T12%3A37%3A20.108%2B02%3A00&terminalID=0090424741&checksum=54CDCAD914E6E97E648F3DF1BA64F41C2C441862](https://api.tutuka.com/pubnub/json.cfm?method=Authenticate&deviceID=DUNNE_PC&transactionID=49716b6b-1cfa-4355-bef3-1e71281c1862&transactionDate=2017-02-01T12%3A37%3A20.108%2B02%3A00&terminalID=0090424741&checksum=54CDCAD914E6E97E648F3DF1BA64F41C2C441862)

The above request will give the following response:

```null
{
  "clientTransactionID": "49716b6b-1cfa-4355-bef3-1e71281c1862",
  "SUBKEY": "sub-c-21e941e8-e37c-11e6-b076-0619f8945a4f",
  "terminalID": "0090424741",
  "CHANNEL": "5163EA72-155D-EEA3-23F93447CA5DE111",
  "AUTH": "c9df5019-96bc-4fc3-b77d-dc73e420cd1f",
  "serverTransactionID": "4716cfbc-d66a-4dfd-a496-9bbcc9877e12",
  "SUBSCRIBEURI": "https://pubsub.pubnub.com/v2/subscribe/",
  "TTL": "86400"
}
```

### **step 2: Subscribe users to channel**

Next, you need to use the above response data to subscribe users to your channel so that they can receive notifications sent to that channel.

This will involve making a GET request to the [PubNub REST API](https://www.pubnub.com/docs/pubnub-rest-api-documentation#publish-subscribe-subscribe-get), via the **subscribe** endpoint:

**https://pubsub.pubnub.com/v2/subscribe/**

Note that the endpoint corresponds to the **SUBSCRIBEURI** value from the previous response data.

You need to specify the following path parameters:

- **SUBKEY**—this is your PubNub subscribe API key.
- **CHANNEL**—this is the channel name you are subscribing users to.
- **Callback**—this is a JSONP callback name. If there is none, just specify it as 0 (zero).
- **Timetoken**—for the initial subscribe, just specify it as 0 (zero).

The above request will give the following response:

`{“t”:{“t”:”16081395170424173″,”r”:7},”m”:[]}`

As you can see above, the response is an object that contains two elements:

- The first element is an object consisting of two values: **t**—timetoken and **r**—region.
- The second element is an array of messages delivered from the subscribed channel.

## **Troubleshooting Transaction Stream**

Importantly, you should use the Transaction Stream service for informational purposes only. The messages are not preserved anywhere, and in case of connectivity issues or other technical hiccups, they may be lost permanently.

Typically, this is how the Transaction Stream service works:

- Paymentology creates the messages as the transaction is happening.
- PubNub retains the messages for up to a maximum of 16 minutes.
- The client (or the receiver) requests to receive the messages from PubNub.

After the messages are streamed, they are only available for a short window of no more than 16 minutes. For example, if a transaction happens at 8.00 a.m., and the receiver system is disconnected after 8.16 a.m., the messages about the transaction will no longer be available.

So, you have up to 16 minutes to receive and process the messages from PubNub. Paymentology does not have any way of tracking if the client has received and processed the messages.

Here is how to troubleshoot issues with the Transaction Stream service and mitigate any potential data loss:

1. The receiver reloads to request a new authentication token from the PubNub Authenticate API.
2. The receiver tries to reconnect to PubNub using the token:
   - If there is an error in connecting to PubNub, the receiver restarts the process at step 1;
   - If it happens again within a 1-minute interval, the receiver must wait at least 30 seconds before retrying.
   - The receiver receives messages from the Transaction Stream service.
   - If there is an error at any point, the receiver must restart the process at step 1.
   - The receiver may choose to store messages locally, in a way feasible to them. As mentioned previously, PubNub does not retain any messages, and they will be unavailable for retrieval after 16 minutes.