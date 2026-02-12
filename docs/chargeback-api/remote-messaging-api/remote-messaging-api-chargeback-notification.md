---
title: 'Remote Messaging API: chargeback notification'
deprecated: false
hidden: false
metadata:
  robots: index
---
<!-- MIGRATION_METADATA
Migrated-From: https://developer.sprint.paymentology.com/chargeback-api/remote-messaging-api/remote-messaging-api-chargeback-notification/
Source-Slug: remote-messaging-api-chargeback-notification
Migrated-On: 2026-02-12T20:19:07+00:00
Migrated-By: wp-readme-migration
-->

This message is to notify the client of Chargeback status updates.


#### Path parameters

| Parameter | type | Limits | required | Description |
| --- | --- | --- | --- | --- |
| messageType | String |  | ✓ | Method name: chargeback.notification |
| detail | Object |  | ✓ | The detail about chargeback status that should include chargeback status, claimId, chargeback details, lastModifiedDate, caseType |


```md
curl --location --request POST 'https://api.tutuka.com/remoteMessaging/v1_0/jsonMock.cfm' \
--header 'Authorization: CS-HMAC-SHA-256 Terminal=0061218987,Checksum=9AE9FC1FCA7602C7000B708CA10B396C0E44FF324976AF70D406C22DC0D89A9B' \
--header 'Content-Type: application/json' \
```

```json
{
    "messageType": "chargeback.notification",
    "data": {
        "status": "Approved",
        "claimId": "123456",
        "isOpen": "true",
        "caseType": "Compliance",
        "caseFilingStatus": "Closed",
        "lastModifiedDate": "2022-03-21",
        "chargebackDetails": [
            {
                "chargebackId": "654321",
                "chargebackType": "CHARGEBACK"
            }
        ]
    }
}
```


#### Response schema

| Parameter | type | Description |
| --- | --- | --- |
| resultCode | String | As described in response reference below. |


```json
{
    "resultCode": "0000"
}
```


## Response reference

Response should contain all the same fields as the original request. In addition a resultCode will be always added and specific response information when that is required by the method. The resultCode will be a string field with values from the table below:


| Value | Meaning |
| --- | --- |
| 0000 | Message processed and confirmed |
| 1000 | API internal error |
| 1022 | Authorization error |
| 1101 | Balance limit exceeded |
| 1102 | Moving annual top up limit exceeded |


**NOTE:**

- The range of response codes may be expanded in the future. Ither response codes, not in the table above, should not be used without explicit written confirmation. The behavior of the system is undefined when using codes not in the listing.

- Response codes should always be four-digit codes. For example, using “0” instead of “0000” (approval) can, and will, yield different than expected results.
