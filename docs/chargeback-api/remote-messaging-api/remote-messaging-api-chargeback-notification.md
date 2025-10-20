---
title: 'Remote Messaging API: chargeback notification'
deprecated: false
hidden: false
metadata:
  robots: index
---
<p>This message is to notify the client of Chargeback status updates.</p>

#### Path parameters

| Parameter | type | Limits | required | Description |
|---|---|---|:--:|---|
| messageType | String |  | ✓ | <p>method name: chargeback.notification</p> |
| detail | Object |  | ✓ | <p>The detail about chargeback status that should include chargeback status, claimId, chargeback details, lastModifiedDate, caseType</p> |

```md
curl --location --request POST 'https://api.tutuka.com/remoteMessaging/v1_0/jsonMock.cfm' \
--header 'Authorization: CS-HMAC-SHA-256 Terminal=0061218987,Checksum=9AE9FC1FCA7602C7000B708CA10B396C0E44FF324976AF70D406C22DC0D89A9B' \
--header 'Content-type: application/json' \

```,```json
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

```,```json
{
    "resultCode": "0000"
}

```

<p> </p>

```md
curl --location --request POST 'https://api.tutuka.com/remoteMessaging/v1_0/jsonMock.cfm' \
--header 'Authorization: CS-HMAC-SHA-256 Terminal=0061218987,Checksum=9AE9FC1FCA7602C7000B708CA10B396C0E44FF324976AF70D406C22DC0D89A9B' \
--header 'Content-type: application/json' \

```,```json
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

```,```json
{
    "resultCode": "0000"
}

```

<p> </p>

#### Response schema

| Field | type | Description |
|---|---|---|
| resultCode | String | <p>As described in response reference below.</p> |

```md
curl --location --request POST 'https://api.tutuka.com/remoteMessaging/v1_0/jsonMock.cfm' \
--header 'Authorization: CS-HMAC-SHA-256 Terminal=0061218987,Checksum=9AE9FC1FCA7602C7000B708CA10B396C0E44FF324976AF70D406C22DC0D89A9B' \
--header 'Content-type: application/json' \

```,```json
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

```,```json
{
    "resultCode": "0000"
}

```

<p> </p>

<h2>Response reference</h2>
<p>Response should contain all the same fields as the original request. In addition a resultCode will be always added and specific response information when that is required by the method. The resultCode will be a string field with values from the table below:</p>

<p><strong>NOTE:</strong></p>
<ul>
<li>The range of response codes may be expanded in the future. Ither response codes, not in the table above, should not be used without explicit written confirmation. The behavior of the system is undefined when using codes not in the listing.</li>
<li>Response codes should always be four-digit codes. For example, using “0” instead of “0000” (approval) can, and will, yield different than expected results.</li>
</ul>
