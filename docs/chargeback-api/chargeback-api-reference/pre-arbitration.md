---
title: Pre-Arbitration
deprecated: false
hidden: false
metadata:
  robots: index
---
<!-- MIGRATION_METADATA
Migrated-From: https://developer.sprint.paymentology.com/chargeback-api/chargeback-api-reference/pre-arbitration/
Source-Slug: pre-arbitration
Migrated-On: 2026-02-12T21:15:03+00:00
Migrated-By: wp-readme-migration
-->

This method is used to submit a Pre-Arbitration case.


## Request/response fields and samples


#### Path parameters

| Parameter | type | Limits | required | Description |
| --- | --- | --- | --- | --- |
| claimId | String |  | ✓ | Claim ID |
| chargebackId | String |  | ✓ | Chargeback ID |
| preArbitrationAmount | String |  | ✓ | Pre-Arbitration case amount in cardholder currency. |
| memo | String |  | ✓ | Memo for the case |
| messageText | String |  |  | Message text. Use only when applicable, otherwise leave empty |
| newReasonCode | String |  |  | New reason code. Use only when applicable i.e. changing reason code. Otherwise left empty.<br><br>Chargeback reason code list available [here](../chargeback-reason-codes) |
| supportingDocument | String |  |  | Document to support the case.<br><br>Use only when applicable, otherwise leave empty |
| clientReferenceNumber | String |  |  | Client reference number.<br><br>Use only when applicable, otherwise leave empty |
| caseNotes | String |  |  | Case notes.<br><br>Use only when applicable, otherwise leave empty |


```json
{
    "claimId": "CLAIM_ID",
    "chargebackId": "CHARGEBACK_ID",
    "preArbitrationAmount": "PREARBITRATION_AMOUNT",
    "memo": "MEMO",
    "messageText": "MESSAGE_TEXT",
    "newReasonCode": "NEW_REASON_CODE",
    "supportingDocument": "BASE64_ENCODED_FILE_HERE",
    "clientReferenceNumber": "CLIENT_REFERENCE_NUMBER",
    "caseNotes": "CASE_NOTES"
}
```


#### Response schema

| Parameter | type | Description |
| --- | --- | --- |
| caseId | String | Pre-arbitration case ID |


```json
{
    "caseId": "CASE_ID"
}
```


#### Other response codes

Further response codes and details can be found [here](../response-codes).


## Additional info


|  |  |
| --- | --- |
| HTTP Method | POST |
| URL_URI (SIT/UAT) | https://chargebacks.test.tutuka.cloud/client/prearbitration |
| HTTP Headers | Content-Type text/plain |
| Query String Parameters | - |
| Format | JSON |
| Authentication | Bearer BEARER_TOKEN |
| Successful Response Code | 200 |
| Error Response Code | 500 |
| Validation Error Response Code | 422 |
