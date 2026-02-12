---
title: Upload Supporting Document
deprecated: false
hidden: false
metadata:
  robots: index
---
<!-- MIGRATION_METADATA
Migrated-From: https://developer.sprint.paymentology.com/chargeback-api/chargeback-api-reference/upload-supporting-document/
Source-Slug: upload-supporting-document
Migrated-On: 2026-02-12T21:32:09+00:00
Migrated-By: wp-readme-migration
-->

This API method is used to upload a supporting document after a chargeback is successfully created.


## Request/response fields and samples


#### Path parameters

| Parameter | type | Limits | required | Description |
| --- | --- | --- | --- | --- |
| chargebackId | String |  | ✓ | Chargeback ID |
| claimID | String |  | ✓ | Claim ID |
| memo | String |  | ✓ | Memo |
| filename | String |  | ✓ | Filename |
| file | String |  | ✓ | File content |


```json
{
    "chargebackId": "CHARGEBACK ID",
    "claimID": "CLAIM_ID",
    "memo": "MEMO",
    "filename": "FILENAME",
    "file": "File content stored in a base64 encoded string"
}
```


#### Response schema

| Parameter | type | Description |
| --- | --- | --- |
| chargebackId | String |  |


```json
{
    "chargebackId": "chargebackId"
}
```


#### Other response codes

Further response codes and details can be found [here](../response-codes).


## Additional info


|  |  |
| --- | --- |
| HTTP Method | PUT |
| URL+URI (SIT/UAT) | https://chargebacks.test.tutuka.cloud/client/claims/{claim-id}/chargebacks/{chargeback-id}/document |
| HTTP Headers | Content-Type text/plain |
| Query String Parameters |  |
| Format | JSON |
| Authentication | Bearer BEARER_TOKEN |
| Successful Response Code | 200 |
| Error Response Code | 500 |
