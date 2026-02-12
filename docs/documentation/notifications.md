---
title: Notifications
deprecated: false
hidden: false
metadata:
  robots: index
---
## Paymentology Sprint Transaction Stream

**Paymentology’s Sprint Transaction Stream service allows API consumers to receive real-time notifications of undertaken transactions. By subscribing to the notification service, consumers can know the status of transactions in real time.**

You can use the service for various purposes, including:

- Customizing customer transaction notifications.
- Tracking payment declines and notifying customers to improve awareness.
- Monitoring fraudulent transactions to mitigate liability.
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

Any activities or notifications that benefit from real-time transaction monitoring and alerting. For example:

- Customizing customer transaction notifications
- Tracking payment declines and notifying customers
- Monitoring fraudulent transactions
- Creating targeted promotional messages
- Reviewing customer spending patterns by time period

## What should the Transaction Stream not be used for?

Because delivery is not guaranteed and the stream is transient, do not use it where complete and accurate information is required, including:

- Financial reconciliation
- Data or financial reporting

## What happens if some transactions from the Transaction Stream are lost or not received?

This can happen with streaming services. Every effort is made to stream data promptly, but if records are not sent or not received, they are lost from the stream.

- The stream cannot be resent later. The transactions would be stale and not useful for real time.
- No financial activity is impacted. All transactions still appear in daily files.

## PubNub and the Transaction Stream Flow

Paymentology uses [PubNub](https://www.pubnub.com) for real-time transaction streaming. PubNub is a secure, real-time publish/subscribe messaging API. The publisher is Paymentology and subscribers are clients. The information is a list of processed transactions.

Paymentology uses this service so a client can subscribe and receive information as transactions complete. The client then decides how to capture, store, and use the information.

### How does it work

*Diagram-for-Sprint-Developer-Porta_Lightmode-3.png IMAGE GOES HERE.*

1. A transaction is received from the VoucherEngine platform from the financial network and categorized according to the [Transaction Types](#transaction-types) below.
2. VoucherEngine determines which campaign the transaction belongs to and whether it needs to be published, then submits it to the respective channel (the campaign UUID) in PubNub.
3. The client implementation uses its credentials (terminal ID and password) to authenticate with the VoucherEngine Events Authority API. See the [Get authentication data](#step-1-get-authentication-data) section.
4. The client receives the Paymentology response. See the [Response](#response) example.
5. The client uses the Paymentology response values (**SUBKEY**, **CHANNEL**, **SUBSCRIBEURI**, **AUTH**) to initiate a connection to **SUBSCRIBEURI** and keeps that connection open, listening to **CHANNEL**.  
   - PubNub Java SDK docs: [here](https://www.pubnub.com/docs/sdks/java#publish-and-subscribe)  
   - Best practice: set up an asynchronous callback for incoming transactions.  
   - PubNub REST API docs: [here](https://www.pubnub.com/docs/rest-api#publish-subscribe-subscribe-get)  
   - Best practice: also use async callbacks if using REST.
6. The client starts receiving transactions while the connection remains open. The client is responsible for refreshing the call from step 3 within the TTL window to refresh the **AUTH** token. Steps 5 and 6 are strongly recommended to be implemented with an official PubNub SDK. Using only REST changes behavior and would require polling to receive transactions at the exact time they occur.

## How to Integrate Transaction Stream

Paymentology provides the Events Authority API to integrate the Transaction Stream. The API lets you observe and ingest transactional events in real time. It is a REST HTTP API with custom authentication over TLS.

Paymentology also leverages the [PubNub](https://www.pubnub.com/) platform using a publish/subscribe model:

- **Channels** — transient paths over which data is transmitted.
- **Messages** — the data sent to recipients.

To receive notifications sent to a channel, users must *subscribe* to it. When you *publish* a message to a channel, all subscribers receive it.

These are the steps:

- Get authentication data
- Subscribe users to channel
- Get the notification feed

### Step 1: Get authentication data

Authenticate against the events system and obtain session and listening endpoint information before consuming PubNub.

Call the PubNub Authenticate REST API:

**Endpoint**

`https://api.voucherengine.com/pubnub/json.cfm`

**Example request URL**

`https://api.voucherengine.com/pubnub/json.cfm?checksum=00F3ED1C44826F692BCF47D654A085250879E192&deviceID=TESTING_TTK&method=Authenticate&terminalID=0090312345&transactionDate=20180524T12:00:00&transactionID=EI152698153428`

**Example response**

```json
{
  "SUBKEY": "sub-c-21e941e8-e37c-11e6-b076-0619f8945a4f",
  "CHANNEL": "8FF7B14F-155D-00FA-4D35CCE727CEA255",
  "SUBSCRIBEURI": "https://pubsub.pubnub.com/v2/subscribe/",
  "serverTransactionID": "94a90010-c531-46d5-9faa-2772dc121196",
  "AUTH": "58426CDE-B5CB-423C-B72D-F3C84C26A1CD",
  "terminalID": "0090312345",
  "clientTransactionID": "49716b6b-1cfa-4355-bef3-1e71281c1862",
  "TTL": "86400"
}
```

**Subscribe URL pattern**

```
GET {SUBSCRIBEURI}/{SUBKEY}/{CHANNEL}/{CALLBACK}/{TIMETOKEN}?auth={AUTH}&uuid={SERVERTRANSACTIONID}
```

**Example subscribe URL**

`GET https://ps.pndsn.com/subscribe/mySubKey/ch1/myFunction/0?auth=authValue&uuid=db9c5e39-7c95-40f5-8d71-125765b6f561`

**Example message payload**

```json
{
  "response_code": "1016",
  "merchant_category_code": "5814",
  "system_time": "1608225195",
  "terminal_id": "T_ID",
  "capture_mode": "ECOM",
  "request_time": "1608243193",
  "merchant": "FOOD PANDA (THAILAND)  HUAYKWANG     THA",
  "balance": 0,
  "amount": 7500,
  "tracking_number": "T_NUMBER",
  "transaction_time": "1608217993",
  "reference": "T_REFERENCE",
  "transaction_id": "T_ID",
  "type": "deduct authorisation"
}
```

**Client constants (Java sample)**

```java
// unique identifier for the device
private static final String DEVICE_NAME = "";
// terminal id attached to your campaign
private static final String TERMINAL_ID = "";
// terminal password associated with your terminal id
private static final String TERMINAL_PASSWORD = "";
```

*... rest of content unchanged, with URLs either in inline backticks or converted to [links](url), and image placeholders preserved as "IMAGE GOES HERE".*
