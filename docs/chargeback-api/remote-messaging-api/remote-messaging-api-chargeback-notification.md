---
title: 'Remote Messaging API: chargeback notification'
deprecated: false
hidden: false
metadata:
  robots: index
original_path: chargeback-api/remote-messaging-api
---
<p>This message is to notify the client of Chargeback status updates.</p>



\{/* spacing: desktop=20, mobile=10 */\}


#### Path parameters

| Parameter | Type | Limits | Required | Description |
|---|---|---|:--:|---|
| messageType | String |  | ✓ | <p>Method name: chargeback.notification</p> |
| detail | Object |  | ✓ | <p>The detail about chargeback status that should include chargeback status, claimId, chargeback details, lastModifiedDate, caseType</p> |




```md
curl --location --request POST 'https://api.tutuka.com/remoteMessaging/v1_0/jsonMock.cfm' \
--header 'Authorization: CS-HMAC-SHA-256 Terminal=0061218987,Checksum=9AE9FC1FCA7602C7000B708CA10B396C0E44FF324976AF70D406C22DC0D89A9B' \
--header 'Content-Type: application/json' \

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
--header 'Content-Type: application/json' \

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



\{/* spacing: desktop=20, mobile=10 */\}


#### Response schema

| Field | Type | Description |
|---|---|---|
| resultCode | String | <p>As described in response reference below.</p> |




```md
curl --location --request POST 'https://api.tutuka.com/remoteMessaging/v1_0/jsonMock.cfm' \
--header 'Authorization: CS-HMAC-SHA-256 Terminal=0061218987,Checksum=9AE9FC1FCA7602C7000B708CA10B396C0E44FF324976AF70D406C22DC0D89A9B' \
--header 'Content-Type: application/json' \

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



{/* spacing: desktop=20, mobile=10 */}


<h2>Response reference</h2>
<p>Response should contain all the same fields as the original request. In addition a resultCode will be always added and specific response information when that is required by the method. The resultCode will be a string field with values from the table below:</p>



{/* spacing: desktop=20, mobile=10 */}


{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"Value"},{"c":"Meaning"}],"caption":false,"body":[[{"c":"0000"},{"c":"Message processed and confirmed"}],[{"c":"1000"},{"c":"API internal error"}],[{"c":"1022"},{"c":"Authorization error"}],[{"c":"1101"},{"c":"Balance limit exceeded"}],[{"c":"1102"},{"c":"Moving annual top up limit exceeded"}]]}} */}


{/* spacing: desktop=20, mobile=10 */}


<p><strong>NOTE:</strong></p>
<ul>
<li>The range of response codes may be expanded in the future. Ither response codes, not in the table above, should not be used without explicit written confirmation. The behavior of the system is undefined when using codes not in the listing.</li>
<li>Response codes should always be four-digit codes. For example, using “0” instead of “0000” (approval) can, and will, yield different than expected results.</li>
</ul>
