---
title: Response codes
deprecated: false
hidden: false
metadata:
  robots: index
---
<!-- MIGRATION_METADATA
Migrated-From: https://developer.sprint.paymentology.com/chargeback-api/response-codes/
Source-Slug: response-codes
Migrated-On: 2026-02-12T21:14:50+00:00
Migrated-By: wp-readme-migration
-->

## Error response code 400

An error response code of 400 indicates client authentication failure. The response message will contain a “responseCode” of 0 and the “responseMessage” will contain either of the below values:


| responseMessage | Definition |
| --- | --- |
| invalid_client | Client authentication failed |
| unauthorized_client | Client is not allowed to generate or refresh tokens. |


## Error response code 422

An error response code of 422 indicates validation errors. The response message will advise which field name was unable to be validated and the error type.

- **EMPTY** – field is empty when it is mandatory

- **INVALID_VALUE** – the value provided for the field is invalid


## Error response code 500

An error response code of 500 will contain an error response message with the “responseCode” and “responseMessage”. Below is the full list of responses that may be returned.


| RESPONSE CODE | RESPONSE MESSAGE | APPLICABLE CHARGEBACK API |
| --- | --- | --- |
| 1 | No such method | First Chargeback |
| 2 | No card found for tracking number: {trackingNumber} | First Chargeback |
| 10 | No authorizations found | First Chargeback |
| 11 | Multiple matching authorizations | First Chargeback |
| 12 | No clearings found | First Chargeback |
| 13 | Multiple matching clearings | First Chargeback |
| 20 | Claim could not be created | First Chargeback |
| 21 | Error creating claim | First Chargeback |
| 30 | Chargeback could not be created | First Chargeback |
| 31 | Error creating chargeback | First Chargeback |
| 40 | Cannot get chargeback doc | Second Presentment Documents |
| 41 | Error getting chargeback doc | Second Presentment Documents |
| 42 | Cannot get chargeback document status | Document Status |
| 43 | Error getting chargeback status | Document Status |
| 44 | Cannot find chargeback with chargebackId = $chargebackId and claimId = $claimId | Upload Supporting Document |
| 45 | Cannot upload chargeback document | Upload Supporting Document |
| 46 | Error uploading chargeback document | Upload Supporting Document |
| 50 | Claim could not be retrived | Pre-Arbitration |
| 51 | Error retrieving claim | Pre-Arbitration |
| 52 | No chargebacks related to the claim | Pre-Arbitration |
| 53 | Time limit of SECOND_PRESENTMENT_TIME_LIMIT days has been exceeded | Pre-Arbitration |
| 54 | No second presentments related to the claim | Pre-Arbitration |
| 55 | Could not retrieve chargeback detail | Pre-Arbitration |
| 56 | Could not retrieve second presentment details | Pre-Arbitration |
| 58 | Case could not be filed | Pre-Arbitration |
| 59 | Error filing case | Pre-Arbitration |
