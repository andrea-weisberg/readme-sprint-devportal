---
title: Remote Messaging API
deprecated: false
hidden: false
metadata:
  robots: index
original_path: card-api/api-reference
---
<p class="BodyA"><strong><span lang="EN-US">Remote messaging API allows Paymentology to call you to send administrative advice messages for Card API. These advice messages are sent using webhook-like schema. If you are integrating the service, you must create an endpoint accessible from the Paymentology network, which would be able to process the requests outlined below.</span></strong></p>



<!-- spacing: desktop=20, mobile=10 -->


<h2>How it works</h2>
<ul>
<li>All messages are sent as <strong>HTTP POST</strong> requests.</li>
<li>Message content is always a <strong>JSON</strong> document.</li>
<li>Methods structure is defined below, and it corresponds to the schema of the JSON document sent.</li>
<li>The message type (eg. <span class="xml-highlight">3DSecure.OTP</span>, <span class="xml-highlight">digitization.event</span>, etc.) is to be included in the JSON message as <span class="xml-highlight">messageType</span>. The message will be sent using the client-supplied URL eg. http://www.example.com/api/endpoint</li>
<li>In the code samples provided, we use cURL to send requests</li>
<li>In the code samples provided, we use a <strong>mock</strong> <strong>endpoint</strong> for testing<strong> &#8211; <a href="https://api.voucherengine.com/remoteMessaging/v1_0/jsonMock.cfm">https://api.voucherengine.com/remoteMessaging/v1_0/jsonMock.cfm</a></strong></li>
</ul>



<!-- spacing: desktop=20, mobile=10 -->


<h2>Expectations</h2>
<p>Total round-trip time, including network overload, should be less than 4 seconds. Failing to meet this, the transaction is considered failed.</p>



<!-- spacing: desktop=20, mobile=10 -->


<h2>Security</h2>
<p>For detailed security measures, please see the end of the Method summary &#8211; <a href="#payload">Payload Integrity Verification</a></p>
<p>Client specific headers can be used, if previously agreed, in accordance to measures used for all methods simultaneously.</p>



<!-- spacing: desktop=20, mobile=10 -->


<h2>Response</h2>
<p>HTTP response code <strong>200 (OK)</strong> is expected to confirm that the message was accepted.</p>



<!-- spacing: desktop=20, mobile=10 -->


<h2>Methods:</h2>
<p><a href="#3DSecure">3DSecure.OTP</a></p>
<p><a href="#3DSecureCCD">3DSecure Cardholder&#8217;s Contact Detail Collection</a></p>
<p><a href="#activation">digitization.activation</a></p>
<p><a href="#event">digitization.event</a></p>
<p><a href="#activationmethods">digitization.activationmethods</a></p>
<p><a href="#appauth">3DSecure.AppAuthentication</a></p>
<p><a href="#appfinal">3DSecure.AppFinalisation</a></p>
<p><a href="#responsereference">Response Reference</a></p>



<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<h1><a id="3DSecure"></a>3DSecure.OTP</h1>
<p class="SubtitleA"><span class="Hyperlink1"><span lang="EN-US">Process 3DS OTP token for an end customer to be able to complete the challenge of a live transaction.</span></span></p>
<p><strong>IMPORTANT:</strong> the &#8220;refCode&#8221; field is only applicable if the campaign option is enabled.</p>



<!-- spacing: desktop=20, mobile=10 -->


#### Path parameters

| Parameter | Type | Limits | Required | Description |
|---|---|---|:--:|---|
| challenge | String |  | ✓ | <p>OTP challenge code</p> |
| customerReference | String |  | ✓ | <p>Customer reference this card is linked to</p> |
| messageType | String |  | ✓ | <p>Method name: 3DSecure.OTP</p> |
| trackingNumber | String |  | ✓ | <p>Tracking number of the card, for which OTP token is being sent</p> |
| merchantDescription | String |  | ✓ | <p>Name of or information related to the merchant</p> |
| transactionAmount  | Integer |  | ✓ | <p>The monetary amount related the transaction</p> |
| refCode | String |  |  | <p>Dynamic generated 4 letters code to be used along with OTP messages<br /> <strong data-renderer-mark="true">if Campaign is configured to.</strong></p> |
| currencyCode | Integer |  | ✓ | <p>The local currency code of the acquirer or source location of the transaction</p> |



<!-- spacing: desktop=20, mobile=10 -->



```json
curl --location --request POST 'https: //api.voucherengine.com/remoteMessaging/v1_0/jsonMock.cfm' \
--header 'Authorization: CS-HMAC-SHA-256 Terminal=0123456789,Checksum=1A11111B2222222C33D44E5555C3F666F1111722228B168892D544050B9B4D3A' \
--header 'Content-Type: application/json' \
--data-raw ‘{
    "challenge": "123456",
    "customerReference": "12b6405c-1120-123b-b55b-12b8f5a46ac1",
    "messageType": "3DSecure.OTP",
    "trackingNumber": "765432100000123",
    "merchantDescription": "SellerDesc4",
    "transactionAmount": "5105",
    "refCode": "QUJA",
    "currencyCode": "840"
}'
```

<p>&nbsp;</p>



<!-- spacing: desktop=20, mobile=10 -->


#### Response schema

| Field | Type | Description |
|---|---|---|
| challenge | String | <p>Echo</p> |
| resultCode | String | <p>As described in response reference</p> |
| customerReference | String | <p>Echo</p> |
| messageType | String | <p>Method name: 3DSecure.OTP</p> |
| merchantDescription | String | <p>Echo</p> |
| transactionAmount | Integer | <p>Echo</p> |
| trackingNumber | String | <p>Echo</p> |
| currencyCode | Integer | <p>Echo</p> |



<!-- spacing: desktop=20, mobile=10 -->



```json
{
    "challenge": "123456",
    "resultCode": "0000",
    "customerReference": "12b6405c-1120-123b-b55b-12b8f5a46ac1",
    "messageType": "3DSecure.OTP",
    "merchantDescription": "SellerDesc4",
    "transactionAmount": "5105",
    "trackingNumber": "765432100000123",
    "currencyCode": "840"
}
```

<p>&nbsp;</p>



<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<h1><a id="3DSecureCCD"></a>Administrative Message – 3D Secure Cardholder Contact Detail Collection</h1>
<p class="SubtitleA"><span class="Hyperlink1"><span lang="EN-US">Collects the cardholder’s masked contact details to be used upon 3DS checkout.</span></span></p>



<!-- spacing: desktop=20, mobile=10 -->


#### Path parameters

| Parameter | Type | Limits | Required | Description |
|---|---|---|:--:|---|
| messageType | String |  | ✓ | <p>cardholder.maskedContactDetails</p> |
| trackingNumber | String |  | ✓ | <p>Tracking number of the card, for which OTP token is being sent</p> |
| customerReference | String |  | ✓ | <p>Customer reference this card is linked to</p> |



<!-- spacing: desktop=20, mobile=10 -->



```json
curl --location --request POST 'https://api.voucherengine.com/remoteMessaging/v1_0/jsonMock.cfm' \
--header 'Authorization: CS-HMAC-SHA-256 Terminal=0123456789,Checksum=1A11111B2222222C33D44E5555C3F666F1111722228B168892D544050B9B4D3A' \
--header 'Content-Type: application/json' \
--data-raw ‘{
"messageType":"cardholder.maskedContactDetails",
"trackingNumber":"212345678900321",
"customerReference":"7353500987654321",}'
```

<p>&nbsp;</p>



<!-- spacing: desktop=20, mobile=10 -->


#### Response schema

| Field | Type | Description |
|---|---|---|
| resultCode | String | <p>Status code indicating transaction result</p> |
| maskedContactDetails | Array | <p>Masked contact details (phone number and email address) linked with the card</p> |



<!-- spacing: desktop=20, mobile=10 -->



```json
STATUS 200 OK
{
"resultCode":"1",
"maskedContactDetails" : [ { "phoneNumber" : "(###) ### 4321", "emailAddress" : "t****a@g****.com" } ] ",
}
```

<p>&nbsp;</p>



<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<h1><a id="activation"></a>digitization.activation</h1>
<p><span class="Hyperlink1"><span lang="EN-US">Process MDES OTP token for an end customer to be able to complete the challenge and activate the wallet.</span></span></p>



<!-- spacing: desktop=20, mobile=10 -->


#### Path parameters

| Parameter | Type | Limits | Required | Description |
|---|---|---|:--:|---|
| messageType | String |  | ✓ | <p>Method name: digitization.activation</p> |
| trackingNumber | String |  | ✓ | <p>Tracking number of the card, for which tokenization is being performed</p> |
| customerReference | String |  | ✓ | <p>Customer reference this card is linked to</p> |
| walletIdentifier | String |  | ✓ | <p>3-digit wallet identifier:</p> <ul> <li>103 – Apple Pay</li> <li>216 – Google Pay</li> <li>217 – Samsung Pay</li> <li>327 – Merchant tokenization program</li> </ul> |
| challenge | String |  | ✓ | <p>OTP activation code</p> |
| tokenRequestorID | String |  | ✓ | <p>The ID assigned by the Token Service Provider to the Token Requestor</p> |



<!-- spacing: desktop=20, mobile=10 -->



```json
curl --location --request POST 'https://api.voucherengine.com/remoteMessaging/v1_0/jsonMock.cfm' \
--header 'Authorization: CS-HMAC-SHA-256 Terminal=0061218987,Checksum=a6d5abb4a4c0e5a6f45287b040ed6cccc82900454959cbf65bbe8cbbf3c24794' \
--header 'Content-Type: application/json' \
--data-raw '{"challenge":"123456","customerReference":"500110022","messageType":"digitization.activation","walletIdentifier":"217","trackingNumber":"544911100000042","tokenRequestorId":"54139059333"}'
```




<!-- spacing: desktop=20, mobile=10 -->


#### Response schema

| Field | Type | Description |
|---|---|---|
| challenge | String | <p>Echo</p> |
| resultCode | Integer | <p>As described in response reference</p> |
| customerReference | String | <p>Echo</p> |
| messageType | String | <p>Echo</p> |
| walletIdentifier | String | <p>Echo</p> |
| trackingNumber | String | <p>Echo</p> |
| tokenRequesterId | String | <p>Echo</p> |



<!-- spacing: desktop=20, mobile=10 -->



```json
{
    "challenge": "123456",
    "resultCode": "0000",
    "customerReference": "500110022",
    "messageType": "digitization.activation",
    "walletIdentifier": "217",
    "trackingNumber": "544911100000042",
    "tokenRequestorId": "54139059333"
}
```




<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<h1><a id="event"></a>digitization.event</h1>
<section id="tutuka-block-1" class="tutuka-block tutuka-block--text-full-width">
<p class="SubtitleA"><span class="Hyperlink1"><span lang="EN-US">Used to communicate tokenization events in MDES</span></span></p>
</section>



<!-- spacing: desktop=20, mobile=10 -->


#### Path parameters

| Parameter | Type | Limits | Required | Description |
|---|---|---|:--:|---|
| messageType | String |  | ✓ | <p>Method name: digitization.event</p> |
| eventType | String |  | ✓ | <p>MDES digitalization status:</p> <p>Digitized</p> <p>Stopped</p> <p>Deleted</p> <p>Digitization_exception</p> <p>Deleted_from_Device</p> <p>Replacement</p> <p>complete</p> |
| trackingNumber | String |  | ✓ | <p>Tracking number of the card, for which tokenization is being performed</p> |
| customerReference | String |  | ✓ | <p>Customer reference the card is linked to</p> |
| walletIdentifier | String |  | ✓ | <p>3-digit wallet identifier:</p> <p>103 – Apple Pay</p> <p>216 – Google Pay</p> <p>217 – Samsung Pay</p> <p>327 – Merchant tokenization program</p> |
| digitizedDeviceIdentifier | String |  | ✓ | <p>Single digit device type identifier:</p> <p>1 – Mobile phone</p> <p>2 – Tablet</p> <p>3 – Watch</p> |
| digitizedPan | String |  | ✓ | <p>The DPAN (Token)</p> |
| digitizedPanExpiry | String |  | ✓ | <p>Expiry date of the DPAN</p> |
| digitizedFpanMasked | String |  | ✓ | <p>Masked Funding Account PAN</p> |
| digitizedTokenReference | String |  | ✓ | <p>Token reference</p> |
| tokenRequestorId | String |  | ✓ | <p>The ID assigned by the Token Service Provider to the Token Requestor</p> |



<!-- spacing: desktop=20, mobile=10 -->



```json
curl --location --request POST 'https://api.voucherengine.com/remoteMessaging/v1_0/jsonMock.cfm' \ 
--header 'Authorization: CS-HMAC-SHA-256 Terminal=0061218987,Checksum=1282C9FFD2586A2DAD5A74B003A34531310007521E65DA17F55D1B744A28B409' \
--header 'Content-Type: application/json' \
--data-raw ‘{"eventType":"complete","digitizedDeviceIdentifier":"21","digitizedPan":"5412345678908888","digitizedTokenReference":"DSACBA000012290985be8cd35f7e46f38b569829de110852","customerReference":"15e6405d-9220-453b-b66b-02d8f9a46ac7","messageType":"digitization.event","walletIdentifier":"217","digitizedFpanMasked":"5473XXXXXXXX1234","digitizedPanExpiry":"2402","trackingNumber":"533223100000004","tokenRequestorId":"54239059112"}'
```




<!-- spacing: desktop=20, mobile=10 -->


#### Response schema

| Field | Type | Description |
|---|---|---|
| resultCode | String | <p>As described in response reference</p> |



<!-- spacing: desktop=20, mobile=10 -->



```json
{"digitizedTokenReference":"DSACBA000012290985be8cd35f7e46f38b569829de110852","customerReference":"15e6405d-9220-453b-b66b-02d8f9a46ac7","walletIdentifier":"217","resultCode":"0000","eventType":"complete","digitizedDeviceIdentifier":"21","digitizedPan":"5412345678908888","messageType":"digitization.event","digitizedFpanMasked":"5473XXXXXXXX1234","digitizedPanExpiry":"2402","trackingNumber":"533223100000004","tokenRequestorId":"54239059112"}
```




<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<h1><a id="activationmethods"></a>digitization.activationmethods</h1>
<p>This message signals that a token provision has been made and requires a verification method in order to push the OTP validation. The type of method will need to be returned as well as the data for the method. At the moment only activation types 1 (mobile phone number) and 2 (cardholder’s email address) are supported.</p>
<p>The response will follow the same conventions described in response reference but in this case it will contain additional information (the activation methods). For simplicity the input parameters are omitted although they are expected in the response.</p>



<!-- spacing: desktop=20, mobile=10 -->


#### Path parameters

| Parameter | Type | Limits | Required | Description |
|---|---|---|:--:|---|
| messageType | String |  | ✓ | <p>Method name: digitization.activationmethods</p> |
| trackingNumber | String |  | ✓ | <p>Tracking number of the card, for which tokenization is being performed</p> |
| customerReference | String |  | ✓ | <p>Customer reference the card is linked to</p> |
| walletIdentifier | String |  | ✓ | <p>3-digit wallet identifier:</p> <ul> <li>103 &#8211; Apple Pay</li> <li>216 &#8211; Google Pay</li> <li>217 &#8211; Samsung Pay</li> <li>327 &#8211; Merchant tokenization program</li> </ul> |
| tokenRequestorId | String |  | ✓ | <p>The ID assigned by the Token Service Provider to the Token Requestor</p> |
| digitizationPath  | String |  | ✓ | <p>Specifies which path was chosen based on our logic and rules: green, yellow, orange or red</p> |
| digitizedDeviceType | String |  | ✓ | <p>Indicates the type of device used at the terminal.</p> |
| walletRecommendation | String |  | ✓ | <p>Tokenization decision suggested by the wallet provider. One of the following values: decline, approve or require_additional_authentication</p> |
| tokenizationPanSource  | String |  | ✓ | <p>Identifies the method which the cardholder is attempting to tokenize a primary account number. One of the following values: card_on_file, card_added_manually, card_added_via_application, existing_token_credential or card_added_via_browser</p> |



<!-- spacing: desktop=20, mobile=10 -->



```json
curl --location --request POST 'https://api.voucherengine.com/remoteMessaging/v1_0/jsonMock.cfm' \
--header 'Authorization: CS-HMAC-SHA-256 Terminal=0061218987,Checksum=9AE9FC1FCA7602C7000B708CA10B396C0E44FF324976AF70D406C22DC0D89A9B' \
--header 'Content-Type: application/json' \
--data-raw ‘{“messageType":"digitization.activationmethods","customerReference":"15e6405d-9220-453b-b66b-02d8f9a46ac7","trackingNumber":"162961400000233","walletIdentifier":"217","tokenRequestorId":"50139059239","digitizationPath":"GREEN","digitizedDeviceType":"00","walletRecommendation":"approve",
"tokenizationPanSource":"card_on_file"}'
```




<!-- spacing: desktop=20, mobile=10 -->


#### Response schema

| Field | Type | Description |
|---|---|---|
| resultCode | String | <p>As described in response reference</p> |
| activationMethods | Array | <p>JSON array of methods where each element has:</p> <ul> <li>type: 1 (phone number) or 2 (email).</li> <li>value: Cardholder’s phone number (type 1) or email (type 2).</li> </ul> |



<!-- spacing: desktop=20, mobile=10 -->



```json
{"resultCode":"0000","customerReference":"15e6405d-9220-453b-b66b-02d8f9a46ac7","messageType":"digitization.activationmethods","walletIdentifier":"217","activationMethods":[{"value":"555123451","type":1}],"trackingNumber":"162961400000233","tokenRequestorId":"50139059239"}
```




<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<!-- spacing: desktop=20, mobile=10 -->


<h2><a id="appauth"></a>3DSecure.AppAuthentication</h2>
<p>This message is used to trigger the process of cardholder authentication. You only need to respond to this message to indicate you have received the message and will initiate the cardholder authentication. Once you have completed cardholder authentication you will send a message to our <a href="https://developer.sprint.paymentology.com/card-api/api-reference/threedsauthenticationoutcome/">ThreeDSAuthenticationOutcome</a> API.<br />
Messages should be as following:</p>
<p>&nbsp;</p>



<!-- spacing: desktop=20, mobile=10 -->


#### Path parameters

| Parameter | Type | Limits | Required | Description |
|---|---|---|:--:|---|
| messageType  | String |  | ✓ | <p>Method name: 3DSecure.AppAuthentication</p> |
| trackingNumber | String |  | ✓ | <p>Tracking number of the card, for which authorisation is being performed</p> |
| customerReference | String |  | ✓ | <p>Customer reference this card is linked to</p> |
| transactionID | String |  | ✓ | <p>Transaction ID to link all messages. The same transaction ID should be used for the following message send to Paymentology.</p> |
| purchaseAmount | String |  | ✓ | <p>Amount of the transaction, formatted with currency included</p> |
| merchant | String |  | ✓ | <p>Name of the merchant transaction is being done at</p> |
| amount | Integer |  | ✓ | <p>Numeric value of the amount, unformatted, in minor units</p> |
| currency | Integer |  | ✓ | <p>ISO code of the currency of the transaction</p> |



<!-- spacing: desktop=20, mobile=10 -->



```json
curl --location --request POST 'https://api.voucherengine.com/remoteMessaging/v1_0/jsonMock.cfm' \--header 'Authorization: CS-HMAC-SHA-256 Terminal=0061218987,Checksum=1282C9FFD2586A2DAD5A74B003A34531310007521E65DA17F55D1B744A28B409' \--header 'Content-Type: application/json' \--data-raw ‘{"messageType":"3DSecure.AppAuthentication","customerReference":"12e1234d-1234-123b-b12b-12d8f9a12ac7","trackingNumber":"123456700000004","transactionID":"123456-123456","purchaseAmount":"R100.00","amount":"10000", "merchant": "Itunes", "currency": "840"}'
```

<p>&nbsp;</p>



<!-- spacing: desktop=20, mobile=10 -->


#### Response schema

| Field | Type | Description |
|---|---|---|
| resultCode | String | <p>As described in response reference</p> |



<!-- spacing: desktop=20, mobile=10 -->



```json
{"resultCode":"0000"}
```

<p>&nbsp;</p>



<!-- spacing: desktop=20, mobile=10 -->


<h2><a id="appfinal"></a>3DSecure.AppFinalisation</h2>
<p>This administrative message is used to inform the client of the final status of the 3DSecure authentication.<br />
Messages include the following:</p>



<!-- spacing: desktop=20, mobile=10 -->


#### Path parameters

| Parameter | Type | Limits | Required | Description |
|---|---|---|:--:|---|
| messageType | String |  | ✓ | <p>Method name: 3DSecure.AppFinalisation</p> |
| trackingNumber | String |  | ✓ | <p>Tracking number of the card, for which authorisation is being performed</p> |
| customerReference | String |  | ✓ | <p>Customer reference this card is linked to</p> |
| transactionID | String |  | ✓ | <p>Unique ID provided by the ACS</p> |
| status | String |  | ✓ | <p>Value indicating the status. Values include:<br /> 0 &#8211; Successfully received final status<br /> 1 &#8211; Timer on browser expired before response was received<br /> 2 &#8211; General error<br /> 3 &#8211; Transaction cancelled before response was received</p> |



<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<!-- spacing: desktop=20, mobile=10 -->


<h1><a id="responsereference"></a>Response Reference</h1>
<p>Response should contain all the same fields as the original request. In addition, a <span class="xml-highlight">resultCode</span> will be always added and specific response information when that is required by the method. The <span class="xml-highlight">resultCode</span> will be a string field with values from the table below:</p>
<p><img loading="lazy" decoding="async" class="aligncenter wp-image-2161" src="https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/Result-codes.png" alt="" width="1223" height="519" srcset="https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/Result-codes.png 885w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/Result-codes-300x127.png 300w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/Result-codes-768x326.png 768w" sizes="auto, (max-width: 1223px) 100vw, 1223px" /></p>



<!-- spacing: desktop=20, mobile=10 -->


<h2>Note:</h2>
<ul>
<li>The range of response codes may be expanded in the future. Other response codes, not in the table above, should not be used without explicit written confirmation. The behavior of the system is undefined when using codes not in the listing.</li>
<li>Response codes should always be four-digit codes. For example, using “0” instead of “0000” (approval) can, and will, yield different than expected results.</li>
</ul>



<!-- spacing: desktop=20, mobile=10 -->


<h2><a id="payload"></a>Optional Payload Integrity Verification</h2>
<p>In order to ensure the integrity of data, all messages can optionally (enabled per client) have a HTTP header named Authorization with a key and a hash of the entire payload.</p>
<p><strong>NOTE: Unless otherwise declared &#8211; this is applicable to all the methods of the API.</strong></p>
<p>Example</p>
<p>Authorization: CS-HMAC-SHA-256 Terminal=0061218987,Checksum=9AE9FC1FCA7602C7000B708CA10B396C0E44FF324976AF70D406C22DC0D89A9B</p>
<p><img loading="lazy" decoding="async" class="aligncenter wp-image-2165" src="https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/Structure.png" alt="" width="1088" height="478" srcset="https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/Structure.png 877w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/Structure-300x132.png 300w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/06/Structure-768x337.png 768w" sizes="auto, (max-width: 1088px) 100vw, 1088px" /></p>



<!-- spacing: desktop=20, mobile=10 -->


<h2>Method</h2>
<p>To calculate the checksum, the payload is treated as a single UTF-8 byte stream, excluding surrounding space characters, if any. The resulting value is passed into HMAC function: HMAC(secret, payload), which signifies the HMAC-keyed hash algorithm using octet string represented by &#8220;secret&#8221; as the key and the octet string &#8220;payload&#8221; as the input string. The size of the result is the hash result size for the hash function in use. In this case, it is 32 octets for SHA-256 as mandated. The &#8220;secret&#8221; is associated with the Terminal value and shared in a separate communication medium prior to enactment of the API.</p>
<p><em>All the examples supplied in the documentation calculate the authorization header using the non existing terminal 0061218987 with the password: 1234567890</em></p>
<p>Example (javascript)</p>

```js
const crypto = require('crypto-js')
const authorizationTerminal = '0061218987'
const terminalPassword = '1234567890'
const payload = `{"challenge":"123456","customerReference":"500110022","messageType":"digitization.activation","walletIdentifier":"217","trackingNumber":"544911100000042","tokenRequestorId":"54139059333"}`
const hashing = crypto.HmacSHA256(payload,terminalPassword).toString(crypto.enc.Hex)
const httpHeader = 'Authorization: CS-HMAC-SHA-256 Terminal=' + authorizationTerminal + ',Checksum=' + hashing
console.log(httpHeader)
```

<p>Will produce the following output:</p>

```js
Authorization: CS-HMAC-SHA-256 Termi-nal=0061218987,Checksum=a6d5abb4a4c0e5a6f45287b040ed6cccc82900454959cbf65bbe8cbbf3c24794
```




<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<!-- spacing: desktop=20, mobile=10 -->


<p><a class="btn btn--primary" href="https://developer.sprint.paymentology.com/card-api/api-reference/">Back to Card API menu</a></p>
