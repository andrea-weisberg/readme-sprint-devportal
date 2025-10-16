---
title: First Chargeback
deprecated: false
hidden: false
metadata:
  robots: index
---
<p>After successfully connecting to the API Proxy, you can send the <b><i>fields/parameters</i></b> for the API request (as specified below) and receive a <b><i>response</i></b>.</p>
<p>A successfully submitted First Chargeback will remain in a “pending status” (no more than 72 hours) on issuers’ behalf to allow merchants to respond and resolve the inquiry.</p>



\{/* spacing: desktop=20, mobile=10 */\}


<h2>Request/response fields and samples</h2>





```json
{
    "trackingNumber": "tRaCkInGnUmBeR",
    "transactionId": "tRaNsAcTiOnId",
    "authnumber": "AuthNumber",
    "systemDate": "2021-08-24 00:00:00",
    "settlementAmount": 402.76,
    "chargebackAmount": 5.74,
    "reasonCode": "4834",
    "supportingDocument": "BASE64_ENCODED_FILE_HERE"
}

```,```json
{
    "chargebackId": "CHARGEBACK ID",
    "claimID": "CLAIM_ID"
}

```




{/* spacing: desktop=20, mobile=10 */}


#### Response schema

| Field | Type | Description |
|---|---|---|
| chargebackId | String | <p>Chargeback ID</p> |
| claimID | String | <p>Claim ID</p> |




```json
{
    "trackingNumber": "tRaCkInGnUmBeR",
    "transactionId": "tRaNsAcTiOnId",
    "authnumber": "AuthNumber",
    "systemDate": "2021-08-24 00:00:00",
    "settlementAmount": 402.76,
    "chargebackAmount": 5.74,
    "reasonCode": "4834",
    "supportingDocument": "BASE64_ENCODED_FILE_HERE"
}

```,```json
{
    "chargebackId": "CHARGEBACK ID",
    "claimID": "CLAIM_ID"
}

```




<h4>Other response codes</h4>
<p>Further response codes and details can be found <a href="https://developer.sprint.paymentology.com/chargeback-api/response-codes/">here</a>.</p>



\{/* spacing: desktop=20, mobile=10 */\}


<h2>Additional info</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":""\},\{"c":""\}],"caption":false,"body":[[\{"c":"HTTP Method"\},\{"c":"POST"\}],[\{"c":"URL+URI (SIT/UAT)"\},\{"c":"https://chargebacks.test.tutuka.cloud/client/chargebacks"\}],[\{"c":"HTTP Headers"\},\{"c":"Content-Type text/plain"\}],[\{"c":"Query String Parameters"\},\{"c":"----"\}],[\{"c":"Format"\},\{"c":"JSON"\}],[\{"c":"Authentication"\},\{"c":"Bearer BEARER_TOKEN"\}],[\{"c":"Successful Response Code"\},\{"c":"200"\}],[\{"c":"Error Response Code"\},\{"c":"500 "\}],[\{"c":"Validation Error Response Code"\},\{"c":"422"\}]]}} */}
