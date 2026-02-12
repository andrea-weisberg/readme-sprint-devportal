---
title: Document Status
deprecated: false
hidden: false
metadata:
  robots: index
---
<!-- MIGRATION_METADATA
Migrated-From: https://developer.sprint.paymentology.com/chargeback-api/chargeback-api-reference/document-status/
Source-Slug: document-status
Migrated-On: 2026-02-12T21:14:58+00:00
Migrated-By: wp-readme-migration
-->

Once a document is uploaded, use this method to verify the status of document.


## Request/response fields and samples


#### Path parameters

| Parameter | type | Limits | required | Description |
| --- | --- | --- | --- | --- |
| chargebackId | String |  | ✓ | Chargeback ID |
| claimID | String |  | ✓ | Claim ID |


```json
{
    "chargebackId": "CHARGEBACK ID",
    "claimID": "CLAIM_ID"
}
```


#### Response schema

| Parameter | type | Description |
| --- | --- | --- |
| status | String | Chargeback document status |


```json
{
    "status": "COMPLETED"
}
```


#### Other response codes

Further response codes and details can be found [here](../response-codes).


## Additional info


|  |  |
| --- | --- |
| HTTP Method | GET |
| URL+URI (SIT/UAT) | https://chargebacks.test.tutuka.cloud/client/claims/{claim-id}/chargebacks/{chargeback-id}/document/status |
| HTTP Headers | Content-Type text/plain |
| Query String Parameters | - |
| Format | JSON |
| Authentication | Bearer BEARER_TOKEN |
| Successful Response Code | 200 |
| Error Response Code | 500 |
