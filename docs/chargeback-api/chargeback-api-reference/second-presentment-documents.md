---
title: Second Presentment Documents
deprecated: false
hidden: false
metadata:
  robots: index
original_path: chargeback-api/chargeback-api-reference
---
<p>Once in the 2nd Presentment phase, this API method is used to receive the supporting documents raised by the acquirer for a claim.</p>



<!-- spacing: desktop=20, mobile=10 -->


<h2>Request/response fields and samples</h2>



#### Path parameters

| Parameter | Type | Limits | Required | Description |
|---|---|---|:--:|---|
| chargebackId | String |  | ✓ | <p>Chargeback ID</p> |
| claimID | String |  | ✓ | <p>Claim ID</p> |
| format | String |  | ✓ | <p>File format. Possible values:<br /> ORIGINAL,<br /> MERGED_TIFF,<br /> MERGED PDF</p> |



<!-- spacing: desktop=20, mobile=10 -->



```json
{
    "chargebackId": "CHARGEBACK ID",
    "claimID": "CLAIM_ID",
    "format": "ORIGINAL_TIFF"
}
```




<!-- spacing: desktop=20, mobile=10 -->


#### Response schema

| Field | Type | Description |
|---|---|---|
| fileAttachment | Object | <p>File attachment</p> |
| filename | String | <p>Filename</p> |
| file | String | <p>File content in base64 encoded string</p> |



<!-- spacing: desktop=20, mobile=10 -->



```json
{
    "fileAttachment": {
        "filename": "FILE_NAME",
        "file": "BASE64_ENCODED_FILE"
    }
}
```




<h4>Other response codes</h4>
<p>Further response codes and details can be found <a href="https://developer.sprint.paymentology.com/chargeback-api/response-codes/">here</a>.</p>



<!-- spacing: desktop=20, mobile=10 -->


<h2>Additional info</h2>



<!-- unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":""},{"c":""}],"caption":false,"body":[[{"c":"HTTP Method"},{"c":"GET"}],[{"c":"URL_URI (SIT/UAT)"},{"c":"https://chargebacks.test.tutuka.cloud/client/claims/{claim-id}/chargebacks/{chargebackId}/documents?format={format}"}],[{"c":"HTTP Headers"},{"c":"Content-Type text/plain"}],[{"c":"Query String Parameters"},{"c":"format={format}"}],[{"c":"Format"},{"c":"JSON"}],[{"c":"Authentication"},{"c":"Bearer BEARER_TOKEN"}],[{"c":"Success Response Code"},{"c":"200"}],[{"c":"Error Response Code"},{"c":"500"}]]}} -->
