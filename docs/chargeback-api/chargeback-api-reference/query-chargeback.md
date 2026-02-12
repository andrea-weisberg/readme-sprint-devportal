---
title: Query Chargeback
deprecated: false
hidden: false
metadata:
  robots: index
---
<!-- MIGRATION_METADATA
Migrated-From: https://developer.sprint.paymentology.com/chargeback-api/chargeback-api-reference/query-chargeback/
Source-Slug: query-chargeback
Migrated-On: 2026-02-12T21:14:59+00:00
Migrated-By: wp-readme-migration
-->

This method is used to query chargeback data from Paymentology.


## Request/response fields and samples


#### Path parameters

| Parameter | type | Limits | required | Description |
| --- | --- | --- | --- | --- |
| trackingNumber | String |  | ✓ | Tracking number |
| transactionId | String |  | ✓ | Transaction ID |
| authNumber | String |  |  | Auth number |
| systemDate | Date |  | ✓ | System date |
| settlementAmount | String |  |  | Settlement amount |
| chargebackAmount | String |  |  | Amount to chargeback |
| reasonCode | String |  | ✓ | Reason code. Chargeback reason code list available [here](../chargeback-reason-codes) |


```json
{
    "trackingNumber": "TRACKING_NUMBER",
    "transactionId": "TRANSACTION_ID",
    "authNumber": "AUTH_NUMBER",
    " systemDate": "systemDate",
    " settlementAmount": "SETTLEMENT_AMOUNT",
    " chargebackAmount": "CHARGEBACK_AMOUNT",
    " reasonCode": "REASON_CODE"
}
```


#### Response schema

| Parameter | type | Description |
| --- | --- | --- |
| claimID | String | Claim ID |
| chargebackID | String | Chargeback ID |


```json
[
    {
        " claimID": "CLAIM_ID",
        " chargebackID": "CHARGEBACK_ID"
    }
]
```
