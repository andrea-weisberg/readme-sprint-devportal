# Remote Messaging API: chargeback notification

This message is to notify the client of Chargeback status updates.

Method name: chargeback.notification

The detail about chargeback status that should include chargeback status, claimId, chargeback details, lastModifiedDate, caseType

curl --location --request POST 'https://api.tutuka.com/remoteMessaging/v1_0/jsonMock.cfm' \
--header 'Authorization: CS-HMAC-SHA-256 Terminal=0061218987,Checksum=9AE9FC1FCA7602C7000B708CA10B396C0E44FF324976AF70D406C22DC0D89A9B' \
--header 'Content-Type: application/json' \

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

As described in response reference below.

{
"resultCode": "0000"
}

## Response reference

Response should contain all the same fields as the original request. In addition a resultCode will be always added and specific response information when that is required by the method. The resultCode will be a string field with values from the table below:

NOTE:

- The range of response codes may be expanded in the future. Ither response codes, not in the table above, should not be used without explicit written confirmation. The behavior of the system is undefined when using codes not in the listing.

- Response codes should always be four-digit codes. For example, using "0" instead of "0000" (approval) can, and will, yield different than expected results.
