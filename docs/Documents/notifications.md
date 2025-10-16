---
title: Notifications
deprecated: false
hidden: false
metadata:
  robots: index
---
<p><strong>Paymentology’s Sprint Transaction Stream service allows API consumers to receive real-time notifications of the undertaken transactions. By subscribing to the notification service, consumers can know the status of transactions in real-time. </strong></p>
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
<p> </p>



\{/* spacing: desktop=20, mobile=10 */\}


<h2>What should the Transaction Stream be used for?</h2>
<p>Any activities or notifications that can benefit from real time transaction monitoring and alerting. For example:</p>
<ul>
<li>Customizing customer transaction notifications</li>
<li>Tracking payment declines and notifying customers to improve their awareness</li>
<li>Monitoring fraudulent transactions to mitigate your liability</li>
<li>Creating targeted promotional messages</li>
<li>Quickly reviewing customer spending patterns by time period</li>
</ul>



\{/* spacing: desktop=20, mobile=10 */\}


<h2>What should the Transaction Stream not be used for?</h2>
<p>Because of the transient nature of the transaction stream, and the fact that delivery is not guaranteed, the stream cannot be used for any purposes that require complete and accurate information. This includes:</p>
<ul>
<li>Any kind of financial reconciliation</li>
<li>Any kind of data reporting/ financial reporting</li>
</ul>



\{/* spacing: desktop=20, mobile=10 */\}


<h2>What happens if some transactions from the Transaction Stream are lost/not received?</h2>
<p>This can happen due to the nature of a streaming service. Every effort is made to ensure that all data is streamed timeously, but if records are not sent by us, or not received by you, those records are lost from the stream. Although not ideal:</p>
<ul>
<li>The stream cannot be resent later because the transactions are now stale, and there is no benefit to real-time notifications</li>
<li>No financial activity will be impacted though, and all transactions will still be reflected in your daily files</li>
</ul>



\{/* unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"\} */}


<h2>PubNub and the Transaction Stream Flow</h2>
<p><span style="font-weight: 400;">Paymentology utilises PubNub (https://www.pubnub.com) for it’s real-time transaction streaming. PubNub is a third party, secure, real-time publish/subscribe messaging API. It allows one to send information from the Publisher (Paymentology) to Subscribers (Clients) in real time. In our case the information is a list of processed transactions. </span><span style="font-weight: 400;"><br />
</span></p>
<p><span style="font-weight: 400;">Paymentology has used this service so that a client can simply subscribe to this service to receive information when a transaction is processed. This is a real-time service so clients will see transaction information as a transaction is completed. A client can then decide how to capture, store and use this information.</span></p>
<h3>How does it work</h3>
<p><img loading="lazy" decoding="async" class="alignleft size-full wp-image-4323" src="https://developer.sprint.paymentology.com/wp-content/uploads/2024/02/Diagram-for-Sprint-Developer-Porta_Lightmode-3.png" alt="Pubnub transaction stream flow" width="6393" height="3955" srcset="https://developer.sprint.paymentology.com/wp-content/uploads/2024/02/Diagram-for-Sprint-Developer-Porta_Lightmode-3.png 6393w, https://developer.sprint.paymentology.com/wp-content/uploads/2024/02/Diagram-for-Sprint-Developer-Porta_Lightmode-3-300x186.png 300w, https://developer.sprint.paymentology.com/wp-content/uploads/2024/02/Diagram-for-Sprint-Developer-Porta_Lightmode-3-1024x633.png 1024w, https://developer.sprint.paymentology.com/wp-content/uploads/2024/02/Diagram-for-Sprint-Developer-Porta_Lightmode-3-768x475.png 768w, https://developer.sprint.paymentology.com/wp-content/uploads/2024/02/Diagram-for-Sprint-Developer-Porta_Lightmode-3-1536x950.png 1536w, https://developer.sprint.paymentology.com/wp-content/uploads/2024/02/Diagram-for-Sprint-Developer-Porta_Lightmode-3-2048x1267.png 2048w" sizes="auto, (max-width: 6393px) 100vw, 6393px" /></p>



\{/* spacing: desktop=20, mobile=10 */\}


<ol>
<li>Transaction gets received from the VoucherEngine platform. As we receive it from the financial network and its being categorized according to the <a href="#transaction">Transaction types</a> below</li>
<li>VoucherEngine is determining which Campaign the transaction belongs to, if that transaction needs to be published, and based on those – it submits it to the respective CHANNEL (which is the Campaign UUID) to PubNub</li>
<li>The Client Implementation is using their credentials (Terminal ID and password) to authenticate with VoucherEngine Events Authority API by making a request. See the <a href="#authentication"><span class="xml-highlight">Get Authentication data</span></a> section for an example of the request</li>
<li>The Client Implementation receives the Paymentology response. See the <a href="#response"><span class="xml-highlight">Get Authentication data</span></a> section for an example of the response</li>
<li>The Client Implementation uses the Paymentology response (specifically they have to use SUBKEY, CHANNEL, SUBSCRIBEURI and AUTH) so as to initiate a connection dictated by the SUBSCRIBEURI. The Client Implementation needs to keep that connection open listening to that CHANNELRespective documentation using the official PubNub Java SDK can be found <a href="https://www.pubnub.com/docs/sdks/java#publish-and-subscribe">here</a><br />
– It is best if the Client sets up an asynchronous callback when there is a new transaction received so as to be properly processed on their end<br />
– The PubNub SDK already covers the section of creating the callbacks but you can also have a look at the bottom with code samplesRespective documentation using the official PubNub REST API can be found <a href="https://www.pubnub.com/docs/rest-api#publish-subscribe-subscribe-get">here</a><br />
– It is best if the Client sets up an asynchronous callback when there is a new transaction received so as to be properly processed on their end<br />
– The PubNub REST API already covers the section of creating the callbacks but you can also have a look at the bottom with code samples</li>
<li>The Client Implementation starts receiving transactions while that connection remains open from the Clients Implementations end. The Client Implementation is responsible for refreshing the call explained at Step 3 within the TTL timespan which is also refreshing their AUTH tokenSteps 5 and 6 are strongly advised to be implemented by using the respective PubNub SDK based on the Client’s preferable implementation language/ framework. Even though the PubNub system offers a RESTful API section that uses the HTTP protocol, it completely changes the way the system should work. For example: if the client choose that, they would have to make regular calls to PubNub so as to receive the transactions as they are done at that exact time</li>
</ol>



\{/* unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"\} */}


<h2><b>How to Integrate Transaction Stream</b></h2>
<p><span style="font-weight: 400;">Paymentology provides the Paymentology Events Authority API to allow you to integrate the Transaction Stream service into your use case. </span></p>
<p><span style="font-weight: 400;">The API lets you observe and ingest information about transactional events, as they happen and are processed by Paymentology. It is implemented as a REST HTTP API using a custom authentication mechanism. The API connection is secured using TLS. </span></p>
<p><span style="font-weight: 400;">Paymentology also leverages the </span><a href="https://www.pubnub.com/"><span style="font-weight: 400;">PubNub</span></a><span style="font-weight: 400;"> platform for powering the real-time transaction notification system. PubNub utilizes a Publishing/Subscribing model for accomplishing real-time communication.</span></p>
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



\{/* spacing: desktop=20, mobile=10 */\}


<h3><b><a id="authentication"></a>Step 1: Get authentication data </b></h3>
<p><span style="font-weight: 400;">First, you need to authenticate against the events system and get session and listening endpoint information before consuming the PubNub API.</span></p>
<p><span style="font-weight: 400;">So, you need to make a GET request to Paymentology’s </span><span style="font-weight: 400;">PubNub Authenticate REST API.</span></p>
<p><span style="font-weight: 400;">To consume the API, you need to call the following endpoint:</span></p>
<p><b>https://api.voucherengine.com/pubnub/json.cfm</b></p>
<p><span style="font-weight: 400;">Furthermore, the API requires the following query string parameters:</span></p>
<p> </p>



\{/* spacing: desktop=20, mobile=10 */\}


\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"Authentication data request parameters","table":{"use_header":true,"header":[{"c":"Name"\},\{"c":"Type"\},\{"c":"Description"\}],"caption":false,"body":[[\{"c":"deviceID"\},\{"c":"String (255)"\},\{"c":"Unique identifier for your application. Each of your applications must use a unique identifier. If you have just one application consuming events, ensure that it remains the same, as long as you intend to keep the application’s state"\}],[\{"c":"method"\},\{"c":"String"\},\{"c":"Authentication method to be used"\}],[\{"c":"transactionID"\},\{"c":"String (255)"\},\{"c":"Unique transaction ID generated by the calling client application"\}],[\{"c":"transactionDate"\},\{"c":"Date"\},\{"c":"Transaction date generated by the calling client application"\}],[\{"c":"terminalID"\},\{"c":"String (10)"\},\{"c":"Paymentology's issued terminal ID of the terminal carrying out the transaction"\}],[\{"c":"checksum"\},\{"c":"String"\},\{"c":"HMAC-SHA1 hashed signature of the concatenated method name with all parameter values using the terminal password as private key. You can use the Checksum Generator tool to get the checksum of the transaction."\}]]}} */}


\{/* unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21\}},"text":"<p>GET request parameters need to be URL encoded otherwise the <span class=\"xml-highlight\">checksum</span> is not calculated correctly</p>\n"},\{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21\}},"text":"<p>This call is a recurring one. The Client must be calling the authentication before the TTL (Time To Live – in minutes – default is 86400 mins ie, 60 days) value expires. This is done for security reasons</p>\n"}]} */}


<p><span style="font-weight: 400;">Here is an example of a GET request to the REST API:</span></p>

```json
https://api.voucherengine.com/pubnub/json.cfm?checksum=00F3ED1C44826F692BCF47D654A085250879E192&deviceID=TESTING_TTK&method=Authenticate&terminalID=0090312345&transactionDate=20180524T12:00:00&transactionID=EI152698153428

```,```json
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

```,```null
GET{SUBSCRIBEURI}/{SUBKEY}/{CHANNEL}/{CALLBACK}/{TIMETOKEN}?auth={AUTH}&uuid={SERVERTRANSACTIONID}

GET https://ps.pndsn.com/subscribe/mySubKey/ch1/myFunction/0?auth=authValue&uuid=db9c5e39-7c95-40f5-8d71-125765b6f561

```,```json
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

```,```null
//unique identifier for the device
private static final String DEVICE_NAME = "";
//your terminal ID that is attached to your campaign
private static final String TERMINAL_ID = "";
//your terminal password, associated with your terminal ID
private static final String TERMINAL_PASSWORD = "";

```

<p> </p>
<p> </p>
<p><span style="font-weight: 400;">The above request will give the following <a id="response"></a>response:</span></p>
<p> </p>




```json
https://api.voucherengine.com/pubnub/json.cfm?checksum=00F3ED1C44826F692BCF47D654A085250879E192&deviceID=TESTING_TTK&method=Authenticate&terminalID=0090312345&transactionDate=20180524T12:00:00&transactionID=EI152698153428

```,```json
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

```,```null
GET{SUBSCRIBEURI}/{SUBKEY}/{CHANNEL}/{CALLBACK}/{TIMETOKEN}?auth={AUTH}&uuid={SERVERTRANSACTIONID}

GET https://ps.pndsn.com/subscribe/mySubKey/ch1/myFunction/0?auth=authValue&uuid=db9c5e39-7c95-40f5-8d71-125765b6f561

```,```json
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

```,```null
//unique identifier for the device
private static final String DEVICE_NAME = "";
//your terminal ID that is attached to your campaign
private static final String TERMINAL_ID = "";
//your terminal password, associated with your terminal ID
private static final String TERMINAL_PASSWORD = "";

```

<p> </p>



<p><span style="font-weight: 400;">Here is a description of the above result:</span></p>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"Authentication data response parameters","table":{"use_header":true,"header":[{"c":"Name"\},\{"c":"Type"\},\{"c":"Description"\}],"caption":false,"body":[[\{"c":"clientTransactionID"\},\{"c":"String (255)"\},{"c":"Echo of <b>transactionID</b>"}],[\{"c":"SUBKEY"\},\{"c":"String (255)"\},{"c":"Value to be used as “sub_key” when accessing <b>subscribe</b> endpoint"}],[\{"c":"terminalID"\},\{"c":"String (10)"\},{"c":"Echo of <b>terminalID</b>"}],[\{"c":"CHANNEL "\},\{"c":"String (255)"\},{"c":"Value to be used as “channel” when accessing <b>subscribe</b> endpoint"}],[\{"c":"AUTH "\},\{"c":"String (255)"\},{"c":"Value to be used as “auth” when accessing <b>subscribe</b> endpoint"}],[\{"c":"serverTransactionID"\},\{"c":"Integer"\},\{"c":"Transaction ID number generated by Paymentology"\}],[\{"c":"SUBSCRIBEURI "\},\{"c":"String (255)"\},\{"c":"Actual URI to use for subscriptions; that is, the full URI to be used with the Paymentology Events Authority SDK, or when accessing manually"\}],[\{"c":"TTL"\},\{"c":"Integer"\},{"c":"Time, in seconds, until the auth value expires. It’s calculated as an offset from <b>transactionDate</b>"}]]}} */}


<p><span style="font-weight: 400;">Here is a description of the HTTP response status codes:</span></p>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"Response codes ","table":{"use_header":true,"header":[{"c":"Code"\},\{"c":"Description"\}],"caption":false,"body":[[\{"c":"200"\},\{"c":"OK"\}],[\{"c":"403"\},\{"c":"TerminalID not valid or password incorrect"\}],[\{"c":"501"\},\{"c":"A general error occurred"\}]]}} */}


\{/* spacing: desktop=20, mobile=10 */\}


\{/* spacing: desktop=20, mobile=10 */\}


<h3><b>Step 2: Subscribe users to channel</b></h3>
<p><span style="font-weight: 400;">Next, you need to use the above response data to subscribe users to your channel so that they can receive notifications sent to that channel.</span></p>
<p><span style="font-weight: 400;">This will involve making a GET request to the </span><a href="https://www.pubnub.com/docs/pubnub-rest-api-documentation#publish-subscribe-subscribe-get"><span style="font-weight: 400;">PubNub REST API</span></a><span style="font-weight: 400;">, via the </span><b>subscribe </b><span style="font-weight: 400;">endpoint:</span></p>
<p><b>https://pubsub.pubnub.com/v2/subscribe/</b></p>
<p><span style="font-weight: 400;">Note that the endpoint corresponds to the </span><b>SUBSCRIBEURI</b><span style="font-weight: 400;"> value from the previous response data.</span></p>
<p><span style="font-weight: 400;">You need to specify the following path parameters:</span></p>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"Subscribe request parameters","table":{"use_header":true,"header":[{"c":"Name"\},\{"c":"Type"\},\{"c":"Description"\}],"caption":false,"body":[[\{"c":"sub_key"\},\{"c":"String (255)"\},{"c":"Subscription API key as issued by Paymentology during <b>authenticate</b> call"}],[\{"c":"channel"\},\{"c":"string (255)"\},{"c":"This is the channel name you are subscribing users to. Paymentology Events Authority uses channels to provide different data for different products. Channel is provided during <b>authenticate</b> call"}],[\{"c":"callback"\},\{"c":"String (255)"\},\{"c":"This is an optional JSONP callback function to wrap responses in. It’s useful when writing frontend JavaScript functions. If there is none, just specify it as 0 (zero)"\}],[\{"c":"timetoken"\},\{"c":"String (255)"\},\{"c":"Just specify it as 0 (zero) for the initial subscribe, or a valid timetoken if resuming / continuing / fast-forwarding from a previous subscribe flow"\}]]}} */}


<ul>
<li style="font-weight: 400;" aria-level="1"><b>SUBKEY</b><span style="font-weight: 400;">—this is your PubNub subscribe API key.</span></li>
<li style="font-weight: 400;" aria-level="1"><b>CHANNEL</b><span style="font-weight: 400;">—this is the channel name you are subscribing users to.</span></li>
<li style="font-weight: 400;" aria-level="1"><b>Callback</b><span style="font-weight: 400;">—this is a JSONP callback name. If there is none, just specify it as 0 (zero).</span></li>
<li style="font-weight: 400;" aria-level="1"><b>Timetoken</b><span style="font-weight: 400;">—for the initial subscribe, just specify it as 0 (zero).</span></li>
</ul>
<p><span style="font-weight: 400;">Furthermore, you need to specify the following query string parameters:</span></p>
<p> </p>




```json
https://api.voucherengine.com/pubnub/json.cfm?checksum=00F3ED1C44826F692BCF47D654A085250879E192&deviceID=TESTING_TTK&method=Authenticate&terminalID=0090312345&transactionDate=20180524T12:00:00&transactionID=EI152698153428

```,```json
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

```,```null
GET{SUBSCRIBEURI}/{SUBKEY}/{CHANNEL}/{CALLBACK}/{TIMETOKEN}?auth={AUTH}&uuid={SERVERTRANSACTIONID}

GET https://ps.pndsn.com/subscribe/mySubKey/ch1/myFunction/0?auth=authValue&uuid=db9c5e39-7c95-40f5-8d71-125765b6f561

```,```json
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

```,```null
//unique identifier for the device
private static final String DEVICE_NAME = "";
//your terminal ID that is attached to your campaign
private static final String TERMINAL_ID = "";
//your terminal password, associated with your terminal ID
private static final String TERMINAL_PASSWORD = "";

```

<p> </p>



{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"Name"},{"c":"Type"},{"c":"Description"}],"caption":false,"body":[[{"c":"tr"},{"c":"String (255)"},{"c":"Region as returned from the initial call with tt=0"}],[{"c":"auth"},{"c":"String (255)"},{"c":"This the authentication (session) key authorized to read messages from the given channel. It’s returned from the <b>authenticate</b> call"}]]}} */}


<p><span style="font-weight: 400;">The above request will give the following response:</span></p>
<p><span style="font-weight: 400;">{“t”:{“t”:”16081395170424173″,”r”:7},”m”:[]}</span></p>
<p> </p>
<p><span style="font-weight: 400;">As you can see above, the response is an object that contains two elements:</span></p>
<ul>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">The first element is an object consisting of two values: </span><b>t</b><span style="font-weight: 400;">—timetoken and </span><b>r</b><span style="font-weight: 400;">—region.</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">The second element is an array of messages delivered from the subscribed channel.</span></li>
</ul>
<p><span style="font-weight: 400;">Generally, let’s look at all the possible data that could be returned from such a request:</span></p>
<p> </p>



{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"Subscribe Response parameters","table":{"use_header":true,"header":[{"c":"Name"},{"c":"Type"},{"c":"Description"}],"caption":false,"body":[[{"c":"0"},{"c":"Object"},{"c":"Timetoken to be used in <b>tt</b> and <b>tr</b> fields respectively in later requests to receive new messages"}],[{"c":"t"},{"c":"String (255)"},{"c":"Timetoken (17-digit UNIX timestamp representation).  (Objects internal structure)"}],[{"c":"r"},{"c":"Integer"},{"c":"Region (publishing location numeric identifier)"}],[{"c":"1"},{"c":"Array of objects"},{"c":"Transaction ID number generated by Paymentology "}],[{"c":"a "},{"c":"String (255)"},{"c":"Shared (server delivering the payload identifier). (Structure of a typical object within a zero-indexed array)"}],[{"c":"b"},{"c":"String (255)"},{"c":"Internal channel identifier which was used to deliver the message"}],[{"c":"c"},{"c":"String (255)"},{"c":"Echo of channel"}],[{"c":"d"},{"c":"Object"},{"c":"Message (transaction) data. See more details below"}],[{"c":"f"},{"c":"Integer"},{"c":"Flags metadata"}],[{"c":"i"},{"c":"String (255)"},{"c":"Issuer identifier (information related to the Paymentology sub-system that published the transaction)"}],[{"c":"k"},{"c":"String (255)"},{"c":"Echo of sub_key"}],[{"c":"0"},{"c":"Object with <b>t</b> and <b>r</b> values (see above)"},{"c":"Originating timetoken metadata"}],[{"c":"p"},{"c":"Object with <b>t</b> and <b>r</b> values (see above)"},{"c":"Publish timetoken metadata"}],[{"c":"u"},{"c":"Object"},{"c":"User meta data (reflection of authentication information)"}]]}} */}


<p><span style="font-weight: 400;">Here is the Message (transaction) data structure that is accessible via “</span><b>d</b><span style="font-weight: 400;">” key above. Note that the structure is extensible and new fields may be added to all versions, as it’s meant to be a backwards compatible change. Remember to always refer to the most up-to-date version of this document for a complete listing of the fields.</span></p>
<p> </p>



{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"Name"},{"c":"Type"},{"c":"Description"}],"caption":false,"body":[[{"c":"type"},{"c":"String (255)"},{"c":"Currently only \"deduct authorization\" value is available. It will be extended in the future"}],[{"c":"amount"},{"c":"Integer"},{"c":"Transaction value in cents, in products currency. For example, if the product is in USD, then a value of 4215 will mean $42.15"}],[{"c":"reference"},{"c":"String (255)"},{"c":"Card customer reference number linked with this card"}],[{"c":"tracking_number"},{"c":"String (255)"},{"c":"Tracking number as available on the card"}],[{"c":"merchant"},{"c":"String (255)"},{"c":"Tracking number as available on the card"}],[{"c":"merchant"},{"c":"String (255)"},{"c":"Merchant identifier associated with the transaction"}],[{"c":"system_time"},{"c":"String (17)"},{"c":"Transactions system date, represented as a 17-digit UNIX timestamp"}],[{"c":"response_code"},{"c":"String (4)"},{"c":"Response code indicating status. See more details below"}],[{"c":"campaign"},{"c":"String (36)"},{"c":"Unique identifier associated with the campaign/product of the card which was used in the transaction"}],[{"c":"balance"},{"c":"Integer"},{"c":"Returns the remaining balance of the card after the transaction. The amount is in cents"}],[{"c":"terminal_id"},{"c":"Integer"},{"c":"The corresponding terminal ID from the received and processed transaction"}],[{"c":"capture_mode"},{"c":"String (4)"},{"c":"Returns the respective capture mode of the card's transaction. See more details below"}]]}} */}


<p><span style="font-weight: 400;">Here are the response code listings:</span></p>



{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"Response Codes","table":{"use_header":true,"header":[{"c":"Code"},{"c":"Description"}],"caption":false,"body":[[{"c":"0000"},{"c":"Approved"}],[{"c":"1000"},{"c":"Do not honor"}],[{"c":"1001"},{"c":"Expired card"}],[{"c":"1006"},{"c":"Allowable PIN tries exceeded"}],[{"c":"1009"},{"c":"Invalid card acceptor/ Invalid transaction"}],[{"c":"1011"},{"c":"Invalid card number"}],[{"c":"1015"},{"c":"A general error occurred"}],[{"c":"1016"},{"c":"Insufficient funds"}],[{"c":"1017 / 1027"},{"c":"Invalid PIN/ PIN length error"}],[{"c":"1018"},{"c":"No card record/ Invalid card number"}],[{"c":"1025"},{"c":"Account closed/ Invalid account"}],[{"c":"1075"},{"c":"Transaction with missing expiry"}],[{"c":"1076"},{"c":"Transaction with invalid expiry"}],[{"c":"1077"},{"c":"Card with Expired CVV2"}],[{"c":"2008"},{"c":"Lost card"}],[{"c":"2009"},{"c":"Stolen card"}],[{"c":"4000"},{"c":"Successful reversal   (<i>NB. This applies only to Reversals) </i>"}]]}} */}


<p>For more information on Transaction Stream/PubNub Response Codes and how they relate to Network and Card Scheme Response Codes, you can refer to the <a href="https://developer.sprint.paymentology.com/response-codes-2/response-and-action-code-mapping/">Response and action code mapping table</a>.</p>



{/* spacing: desktop=20, mobile=10 */}


<p><span style="font-weight: 400;">Here are the possible capture modes:</span></p>



{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"Capture mode codes","table":{"use_header":true,"header":[{"c":"Code"},{"c":"Description"}],"caption":false,"body":[[{"c":"MAG"},{"c":"Magnetic Stripe captured transaction"}],[{"c":"EMV"},{"c":"Electronic chip captured transaction"}],[{"c":"ECOM"},{"c":"Transaction captured online"}],[{"c":"MAN"},{"c":"Manually captured transaction"}],[{"c":"NFC"},{"c":"Transaction captured via the NFC app"}]]}} */}


{/* spacing: desktop=20, mobile=10 */}


<h3><b>Step 3: Get the notification feed</b></h3>

```json
https://api.voucherengine.com/pubnub/json.cfm?checksum=00F3ED1C44826F692BCF47D654A085250879E192&deviceID=TESTING_TTK&method=Authenticate&terminalID=0090312345&transactionDate=20180524T12:00:00&transactionID=EI152698153428

```,```json
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

```,```null
GET{SUBSCRIBEURI}/{SUBKEY}/{CHANNEL}/{CALLBACK}/{TIMETOKEN}?auth={AUTH}&uuid={SERVERTRANSACTIONID}

GET https://ps.pndsn.com/subscribe/mySubKey/ch1/myFunction/0?auth=authValue&uuid=db9c5e39-7c95-40f5-8d71-125765b6f561

```,```json
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

```,```null
//unique identifier for the device
private static final String DEVICE_NAME = "";
//your terminal ID that is attached to your campaign
private static final String TERMINAL_ID = "";
//your terminal password, associated with your terminal ID
private static final String TERMINAL_PASSWORD = "";

```

<p> </p>



\{/* spacing: desktop=20, mobile=10 */\}


<h2>Subscribing and Retrieval via PubNub SDK</h2>
<p><span style="font-weight: 400;">A  client will implement the service using one of the</span><a href="https://www.pubnub.com/docs/platform/sdks#client-sdks"> <span style="font-weight: 400;">available SDKs</span></a> <span style="font-weight: 400;">combining it with our custom authentication mechanism described in Step 1</span></p>
<p><span style="font-weight: 400;">However we are able to provide a sample Java application which the client can download, run and then expand upon to build their own integration:</span></p>
<p> </p>
<ul>
<li style="list-style-type: none;">
<ul>
<li style="font-weight: 400;" aria-level="3"><span style="font-weight: 400;">Example application source code:</span>
<ul>
<li style="font-weight: 400;" aria-level="4"><span style="font-weight: 400;">We provide source code of a very simple JAVA application which will connect to Paymentology’s transaction publishing service, subscribe to a campaign, and then open a window on the screen which will flash up the merchant name whenever a transaction is made. This is not an actual running application that one can run on a PC but source code that can be used by the clients developers in their development software and make further use of it.</span><span style="font-weight: 400;"><br />
</span><span style="font-weight: 400;"><br />
</span><span style="font-weight: 400;">To start working with this sample application, following steps need to be taken:</span> </p>
<ul>
<li style="font-weight: 400;" aria-level="5"><span style="font-weight: 400;">1. Ask your CE to enable PubNub feeds via your campaign settings..</span></li>
<li style="font-weight: 400;" aria-level="5"><span style="font-weight: 400;">2. Then in src/main/java/com/tutuka/transactionscroller the following data need to be updated:</span></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>




```json
https://api.voucherengine.com/pubnub/json.cfm?checksum=00F3ED1C44826F692BCF47D654A085250879E192&deviceID=TESTING_TTK&method=Authenticate&terminalID=0090312345&transactionDate=20180524T12:00:00&transactionID=EI152698153428

```,```json
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

```,```null
GET{SUBSCRIBEURI}/{SUBKEY}/{CHANNEL}/{CALLBACK}/{TIMETOKEN}?auth={AUTH}&uuid={SERVERTRANSACTIONID}

GET https://ps.pndsn.com/subscribe/mySubKey/ch1/myFunction/0?auth=authValue&uuid=db9c5e39-7c95-40f5-8d71-125765b6f561

```,```json
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

```,```null
//unique identifier for the device
private static final String DEVICE_NAME = "";
//your terminal ID that is attached to your campaign
private static final String TERMINAL_ID = "";
//your terminal password, associated with your terminal ID
private static final String TERMINAL_PASSWORD = "";

```

<p> </p>



<ul>
<li style="font-weight: 400;" aria-level="6"><span style="font-weight: 400;">DEVICE_NAME is any string that can identify you as the client., It is just something we log on our side. It could be f.e. CLIENT_NAME_APP</span></li>
<li style="font-weight: 400;" aria-level="6"><span style="font-weight: 400;">TERMINAL_ID is the Terminal ID of your Default Issuing Merchant  </span></li>
<li style="font-weight: 400;" aria-level="6"><span style="font-weight: 400;">TERMINAL_PASSWORD is the Terminal Password of your Default Issuing Merchant</span></li>
</ul>
<p><span style="font-weight: 400;">Update the HTTP Builder in the src/main/java/com/tutuka/transactionscroller/authorization/AuthRequest.java with the correct environment:</span><span style="font-weight: 400;"><br />
</span><span style="font-weight: 400;"><br />
</span><span style="font-weight: 400;">Example for UAT:</span><span style="font-weight: 400;"><br />
</span></p>
<p><img loading="lazy" decoding="async" class="alignnone size-medium wp-image-2446" src="https://developer.sprint.paymentology.com/wp-content/uploads/2022/03/TTS-UAT-300x62.png" alt="" width="300" height="62" srcset="https://developer.sprint.paymentology.com/wp-content/uploads/2022/03/TTS-UAT-300x62.png 300w, https://developer.sprint.paymentology.com/wp-content/uploads/2022/03/TTS-UAT.png 598w" sizes="auto, (max-width: 300px) 100vw, 300px" /></p>
<p> </p>
<p>After following the above steps, you can start testing and working with the code.</p>



{/* unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} */}


<h2><b>Troubleshooting the Transaction Stream</b></h2>
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



{/* unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} */}


<h1><a id="transaction"></a>Transaction Types</h1>
<p><span style="font-weight: 400;">Transaction types published are the following:</span></p>
<ul>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">deduct authorisation</span>
<ul>
<li style="font-weight: 400;" aria-level="2"><span style="font-weight: 400;">When the client make a payment(deduct) and the transaction come through Paymentology</span></li>
</ul>
</li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">deduct authorisation reversal</span>
<ul>
<li style="font-weight: 400;" aria-level="2"><span style="font-weight: 400;">When the client failed to make a payment(deduct) and the transaction come through Paymentology</span></li>
</ul>
</li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">refund authorisation</span>
<ul>
<li style="font-weight: 400;" aria-level="2"><span style="font-weight: 400;">When there is a refund from VISA/MasterCard/CUP</span></li>
</ul>
</li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">refund authorisation reversal</span>
<ul>
<li style="font-weight: 400;" aria-level="2"><span style="font-weight: 400;">When there is a reversal of a refund from VISA/MasterCard/CUP</span></li>
</ul>
</li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">payment authorisation</span>
<ul>
<li style="font-weight: 400;" aria-level="2"><span style="font-weight: 400;">When the client make a p2p (person-to-person) or money send transaction</span></li>
</ul>
</li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">payment authorisation reversal</span>
<ul>
<li style="font-weight: 400;" aria-level="2"><span style="font-weight: 400;">When the client failed to make a p2p (person-to-person) or money send transaction and we have to reverse the transaction</span></li>
</ul>
</li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">balance</span>
<ul>
<li style="font-weight: 400;" aria-level="2"><span style="font-weight: 400;">When the client request for balance</span></li>
</ul>
</li>
</ul>
<p> </p>
<h2><b>Environments</b></h2>
<p><span style="font-weight: 400;">The Transaction Streaming system is available in all the environments Paymentology uses. The underlying Pubnub infrastructure is the same in all the environments, the only differentiation that happens only from Pubnub is the CHANNEL.</span></p>
<p><span style="font-weight: 400;">So, below is a breakdown of the respective Authentication Urls per environment:</span></p>
<ul>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">For Test the URL for authenticating is: https://stream.test.tutuka.cloud/json</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">For Vexdev the URL for authenticating is: https://apidev.tutuka.com/pubnub/json.cfm</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">For UAT the URL for authenticating is: https://stream.uat.tutuka.cloud/json</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">For Live/PROD the URL for authenticating is: </span><a href="https://api.voucherengine.com/pubnub/json.cfm"><span style="font-weight: 400;">https://api.voucherengine.com/pubnub/json.cfm</span></a></li>
</ul>
<p> </p>
