---
title: First Chargeback
deprecated: false
hidden: false
metadata:
  robots: index
---
<!-- MIGRATION_METADATA
Migrated-From: https://developer.sprint.paymentology.com/chargeback-api/chargeback-api-reference/first-chargeback/
Source-Slug: first-chargeback
Migrated-On: 2026-02-12T21:15:02+00:00
Migrated-By: wp-readme-migration
-->

After successfully connecting to the API Proxy, you can send the ***fields/parameters*** for the API request (as specified below) and receive a ***response***.

A successfully submitted First Chargeback will remain in a “pending status” (no more than 72 hours) on issuers’ behalf to allow merchants to respond and resolve the inquiry.


## Request/response fields and samples


#### Path parameters

| Parameter | type | Limits | required | Description |
| --- | --- | --- | --- | --- |


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
```


#### Response schema

| Parameter | type | Description |
| --- | --- | --- |
| chargebackId | String | Chargeback ID |
| claimID | String | Claim ID |


```json
{
    "chargebackId": "CHARGEBACK ID",
    "claimID": "CLAIM_ID"
}
```


#### Other response codes

Further response codes and details can be found [here](../response-codes).


## Additional info


|  |  |
| --- | --- |
| HTTP Method | POST |
| URL+URI (SIT/UAT) | https://chargebacks.test.tutuka.cloud/client/chargebacks |
| HTTP Headers | Content-Type text/plain |
| Query String Parameters | ---- |
| Format | JSON |
| Authentication | Bearer BEARER_TOKEN |
| Successful Response Code | 200 |
| Error Response Code | 500 |
| Validation Error Response Code | 422 |
