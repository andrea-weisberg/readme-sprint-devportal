---
title: Transaction Stream
deprecated: false
hidden: false
metadata:
  robots: index
---
<p><strong>Paymentology’s Transaction Stream service allows API consumers to receive real-time notifications of the undertaken transactions. By subscribing to the notification service, consumers can know the status of transactions in real-time. </strong></p>
<p><span style="font-weight: 400;">You can use the service for various purposes, including:</span></p>
<ul>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">Customizing customer transaction notifications.</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">Tracking payment declines and notifying customers to improve their awareness.</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">Monitoring fraudulent transactions to mitigate your liability.</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">Creating targeted promotional messages.</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">Quickly reviewing customer spending patterns by time period.<br />
</span></li>
</ul>
<p><span style="font-weight: 400;">It enables you to receive real-time transaction information for the following types of transactions:</span></p>
<ul>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">Successful transactions</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">Reversed transactions</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">Verified transactions</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">Declined transactions</span></li>
</ul>
<p><span style="font-weight: 400;">You can get the following information for each undertaken transaction:</span></p>
<ul>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">Customer reference account number </span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">Transaction time and date</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">Merchant name  </span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">Decline reason code</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">Transaction amount </span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">MCC (Merchant Category Code)</span></li>
</ul>

<h2><b>How to Integrate Transaction Stream</b></h2>
<p><span style="font-weight: 400;">Paymentology provides the Events Authority API to allow you to integrate the Transaction Stream service into your use case. </span></p>
<p><span style="font-weight: 400;">The API lets you observe and ingest information about transactional events, as they happen and are processed. It is implemented as a REST HTTP API using a custom authentication mechanism. The API connection is secured using TLS. </span></p>
<p><span style="font-weight: 400;">The </span><a href="https://www.pubnub.com/"><span style="font-weight: 400;">PubNub</span></a><span style="font-weight: 400;"> platform is levergaed for powering the real-time transaction notification system. PubNub utilizes a Publishing/Subscribing model for accomplishing real-time communication.</span></p>
<p><span style="font-weight: 400;">This model consists of two important components:</span></p>
<ul>
<li style="font-weight: 400;" aria-level="1"><b>Channels</b><span style="font-weight: 400;">—these are the transient paths over which your data is transmitted.</span></li>
<li style="font-weight: 400;" aria-level="1"><b>Messages</b><span style="font-weight: 400;">—these are the data you want to send to recipients.</span></li>
</ul>
<p><span style="font-weight: 400;">Essentially, to enable users to receive the notifications sent to a particular channel, they need to </span><i><span style="font-weight: 400;">subscribe</span></i><span style="font-weight: 400;"> to it. If you </span><i><span style="font-weight: 400;">publish</span></i><span style="font-weight: 400;"> a message to a channel, the notification will be delivered to every user subscribed to that channel. </span></p>
<p><span style="font-weight: 400;">These are the steps to follow to implement the Transaction Stream feature into your application:</span></p>
<ul>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">Get authentication data </span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">Subscribe users to channel</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">Get the notification feed</span></li>
</ul>
<p><span style="font-weight: 400;">Let’s talk about the steps in more detail.</span></p>

<h3><b>Step 1: Get authentication data </b></h3>
<p><span style="font-weight: 400;">First, you need to authenticate against the events system and get session and listening endpoint information before consuming the PubNub API.</span></p>
<p><span style="font-weight: 400;">So, you need to make a GET request to Paymentology’s</span><span style="font-weight: 400;"> PubNub Authenticate REST API.</span></p>
<p><span style="font-weight: 400;">To consume the API, you need to call the following endpoint:</span></p>
<p><b>https://api.tutuka.com/pubnub/json.cfm</b></p>
<p> </p>
<p><span style="font-weight: 400;">Here is an example of a GET request to the REST API:</span></p>
<p><a href="https://api.tutuka.com/pubnub/json.cfm?method=Authenticate&deviceID=DUNNE_PC&transactionID=49716b6b-1cfa-4355-bef3-1e71281c1862&transactionDate=2017-02-01T12%3A37%3A20.108%2B02%3A00&terminalID=0090424741&checksum=54CDCAD914E6E97E648F3DF1BA64F41C2C441862"><b>https://api.tutuka.com/pubnub/json.cfm?method=Authenticate&deviceID=DUNNE_PC&transactionID=49716b6b-1cfa-4355-bef3-1e71281c1862&transactionDate=2017-02-01T12%3A37%3A20.108%2B02%3A00&terminalID=0090424741&checksum=54CDCAD914E6E97E648F3DF1BA64F41C2C441862</b></a></p>
<p> </p>
<p><span style="font-weight: 400;">The above request will give the following response:</span></p>

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

<p> </p>

<h3><b>Step 2: Subscribe users to channel</b></h3>
<p><span style="font-weight: 400;">Next, you need to use the above response data to subscribe users to your channel so that they can receive notifications sent to that channel.</span></p>
<p><span style="font-weight: 400;">This will involve making a GET request to the </span><a href="https://www.pubnub.com/docs/pubnub-rest-api-documentation#publish-subscribe-subscribe-get"><span style="font-weight: 400;">PubNub REST API</span></a><span style="font-weight: 400;">, via the </span><b>subscribe </b><span style="font-weight: 400;">endpoint:</span></p>
<p><b>https://pubsub.pubnub.com/v2/subscribe/</b></p>
<p><span style="font-weight: 400;">Note that the endpoint corresponds to the </span><b>SUBSCRIBEURI</b><span style="font-weight: 400;"> value from the previous response data.</span></p>
<p> </p>
<p><span style="font-weight: 400;">You need to specify the following path parameters:</span></p>
<ul>
<li style="font-weight: 400;" aria-level="1"><b>SUBKEY</b><span style="font-weight: 400;">—this is your PubNub subscribe API key.</span></li>
<li style="font-weight: 400;" aria-level="1"><b>CHANNEL</b><span style="font-weight: 400;">—this is the channel name you are subscribing users to.</span></li>
<li style="font-weight: 400;" aria-level="1"><b>Callback</b><span style="font-weight: 400;">—this is a JSONP callback name. If there is none, just specify it as 0 (zero).</span></li>
<li style="font-weight: 400;" aria-level="1"><b>Timetoken</b><span style="font-weight: 400;">—for the initial subscribe, just specify it as 0 (zero).</span></li>
</ul>
<p> </p>
<p><span style="font-weight: 400;">The above request will give the following response:</span></p>
<p><span style="font-weight: 400;">{“t”:{“t”:”16081395170424173″,”r”:7},”m”:[]}</span></p>
<p> </p>
<p><span style="font-weight: 400;">As you can see above, the response is an object that contains two elements:</span></p>
<ul>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">The first element is an object consisting of two values: </span><b>t</b><span style="font-weight: 400;">—timetoken and </span><b>r</b><span style="font-weight: 400;">—region.</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">The second element is an array of messages delivered from the subscribed channel.</span></li>
</ul>
<p> </p>

<h2><b>Troubleshooting Transaction Stream</b></h2>
<p><span style="font-weight: 400;">Importantly, you should use the Transaction Stream service for informational purposes only. The messages are not preserved anywhere, and in case of connectivity issues or other technical hiccups, they may be lost permanently.</span></p>
<p><span style="font-weight: 400;">Typically, this is how the Transaction Stream service works:</span></p>
<ul>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">Paymentology creates the messages as the transaction is happening.</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">PubNub retains the messages for up to a maximum of 16 minutes.</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">The client (or the receiver) requests to receive the messages from PubNub.</span></li>
</ul>
<p><span style="font-weight: 400;">After the messages are streamed, they are only available for a short window of no more than 16 minutes. For example, if a transaction happens at 8.00 a.m., and the receiver system is disconnected after 8.16 a.m., the messages about the transaction will no longer be available.</span></p>
<p><span style="font-weight: 400;">So, you have up to 16 minutes to receive and process the messages from PubNub. Paymentology does not have any way of tracking if the client has received and processed the messages.</span></p>
<p><span style="font-weight: 400;">Here is how to troubleshoot issues with the Transaction Stream service and mitigate any potential data loss:</span></p>
<ol>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">The receiver reloads to request a new authentication token from the PubNub Authenticate API.</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">The receiver tries to reconnect to PubNub using the token:</span></li>
</ol>
<ul>
<li style="font-weight: 400;" aria-level="2"><span style="font-weight: 400;">If there is an error in connecting to PubNub, the receiver restarts the process at step 1;</span></li>
<li style="font-weight: 400;" aria-level="2"><span style="font-weight: 400;">If it happens again within a 1-minute interval, the receiver must wait at least 30 seconds before retrying.</span></li>
<li style="font-weight: 400;" aria-level="2"><span style="font-weight: 400;">The receiver receives messages from the Transaction Stream service.</span></li>
<li style="font-weight: 400;" aria-level="2"><span style="font-weight: 400;">If there is an error at any point, the receiver must restart the process at step 1.</span></li>
<li style="font-weight: 400;" aria-level="2"><span style="font-weight: 400;">The receiver may choose to store messages locally, in a way feasible to them. As mentioned previously, PubNub does not retain any messages, and they will be unavailable for retrieval after 16 minutes.</span></li>
</ul>
