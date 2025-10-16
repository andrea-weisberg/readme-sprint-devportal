---
title: Upload Supporting Document
deprecated: false
hidden: false
metadata:
  robots: index
---
<p>This API method is used to upload a supporting document after a chargeback is successfully created.</p>



\{/* spacing: desktop=20, mobile=10 */\}


<h2>Request/response fields and samples</h2>



#### Path parameters

| Parameter | Type | Limits | Required | Description |
|---|---|---|:--:|---|
| chargebackId | String |  | ✓ | <p>Chargeback ID</p> |
| claimID | String |  | ✓ | <p>Claim ID</p> |
| memo | String |  | ✓ | <p>Memo</p> |
| filename | String |  | ✓ | <p>Filename</p> |
| file | String |  | ✓ | <p>File content</p> |



\{/* spacing: desktop=20, mobile=10 */\}



```json
{
    "chargebackId": "CHARGEBACK ID",
    "claimID": "CLAIM_ID",
    "memo": "MEMO",
    "filename": "FILENAME",
    "file": "File content stored in a base64 encoded string"
}

```,```json
{
    "chargebackId": "chargebackId"
}

```




{/* spacing: desktop=20, mobile=10 */}


#### Response schema

| Field | Type | Description |
|---|---|---|
| chargebackId | String |  |



{/* spacing: desktop=20, mobile=10 */}



```json
{
    "chargebackId": "CHARGEBACK ID",
    "claimID": "CLAIM_ID",
    "memo": "MEMO",
    "filename": "FILENAME",
    "file": "File content stored in a base64 encoded string"
}

```,```json
{
    "chargebackId": "chargebackId"
}

```




<h4>Other response codes</h4>
<p>Further response codes and details can be found <a href="https://developer.sprint.paymentology.com/chargeback-api/response-codes/">here</a>.</p>



\{/* spacing: desktop=20, mobile=10 */\}


<h2>Additional info</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":""\},\{"c":""\}],"caption":false,"body":[[\{"c":"HTTP Method"\},\{"c":"PUT"\}],[\{"c":"URL+URI (SIT/UAT)"\},\{"c":"https://chargebacks.test.tutuka.cloud/client/claims/{claim-id\}/chargebacks/\{chargeback-id\}/document"}],[\{"c":"HTTP Headers"\},\{"c":"Content-Type text/plain"\}],[\{"c":"Query String Parameters"\},\{"c":""\}],[\{"c":"Format"\},\{"c":"JSON"\}],[\{"c":"Authentication"\},\{"c":"Bearer BEARER_TOKEN"\}],[\{"c":"Successful Response Code"\},\{"c":"200"\}],[\{"c":"Error Response Code"\},\{"c":"500"\}]]}} */}
