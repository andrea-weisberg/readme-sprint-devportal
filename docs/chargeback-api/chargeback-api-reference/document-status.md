---
title: Document Status
deprecated: false
hidden: false
metadata:
  robots: index
original_path: chargeback-api/chargeback-api-reference
---
<p>Once a document is uploaded, use this method to verify the status of document.</p>



\{/* spacing: desktop=20, mobile=10 */\}


<h2>Request/response fields and samples</h2>



#### Path parameters

| Parameter | Type | Limits | Required | Description |
|---|---|---|:--:|---|
| chargebackId | String |  | ✓ | <p>Chargeback ID</p> |
| claimID | String |  | ✓ | <p>Claim ID</p> |



\{/* spacing: desktop=20, mobile=10 */\}



```json
{
    "chargebackId": "CHARGEBACK ID",
    "claimID": "CLAIM_ID"
}

```,```json
{
    "status": "COMPLETED"
}

```




{/* spacing: desktop=20, mobile=10 */}


#### Response schema

| Field | Type | Description |
|---|---|---|
| status | String | <p>Chargeback document status</p> |



{/* spacing: desktop=20, mobile=10 */}



```json
{
    "chargebackId": "CHARGEBACK ID",
    "claimID": "CLAIM_ID"
}

```,```json
{
    "status": "COMPLETED"
}

```




<h4>Other response codes</h4>
<p>Further response codes and details can be found <a href="https://developer.sprint.paymentology.com/chargeback-api/response-codes/">here</a>.</p>



\{/* spacing: desktop=20, mobile=10 */\}


<h2>Additional info</h2>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":""\},\{"c":""\}],"caption":false,"body":[[\{"c":"HTTP Method"\},\{"c":"GET"\}],[\{"c":"URL+URI (SIT/UAT)"\},\{"c":"https://chargebacks.test.tutuka.cloud/client/claims/{claim-id\}/chargebacks/\{chargeback-id\}/document/status"}],[\{"c":"HTTP Headers"\},\{"c":"Content-Type text/plain"\}],[\{"c":"Query String Parameters"\},\{"c":"-"\}],[\{"c":"Format"\},\{"c":"JSON"\}],[\{"c":"Authentication"\},\{"c":"Bearer BEARER_TOKEN"\}],[\{"c":"Successful Response Code"\},\{"c":"200"\}],[\{"c":"Error Response Code"\},\{"c":"500"\}]]}} */}
