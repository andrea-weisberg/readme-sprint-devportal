---
title: Connectivity
deprecated: false
hidden: false
metadata:
  robots: index
---
<!-- MIGRATION_METADATA
Migrated-From: https://developer.sprint.paymentology.com/chargeback-api/connectivity/
Source-Slug: connectivity
Migrated-On: 2026-02-12T21:14:53+00:00
Migrated-By: wp-readme-migration
-->

This page explains how to connect to our Chargeback API gateway.

Connecting to the Chargeback API means you can automate submissions of your chargebacks.


## IP/Host details


| ENVIRONMENT | SERVICE | IP/HOST | PORT | URI |
| --- | --- | --- | --- | --- |
| SIT/UAT | First chargeback | chargebacks.test.tutuka.cloud | 443 | https://chargebacks.test.tutuka.cloud/client/ |
| PROD | First chargeback | chargebacks.prod.tutuka.cloud | 443 | https://chargebacks.prod.tutuka.cloud/client/ |


## API Gateway token

Below are the default specifications for the ***token bearer ***details for authentication as reflected in the First Chargeback example [here](chargeback-api-reference/first-chargeback).


|  |  |
| --- | --- |
| HTTP Method | POST |
| URL+URI (SIT/UAT) | https://chargebacks.test.tutuka.cloud/token/generate |
| URL+URI (PROD) | https://chargebacks.prod.tutuka.cloud/token/generate |
| HTTP Headers | Content-Type = application/x-www-form-urlencoded |
| Query String Parameters | None |
| Format | JSON |
| Authentication | Basic BASE64_ENCODED_CREDENTIALS(user:pass) |
| Request | None |
| Success Response Code | 200 |
| Success Response | {<br> "access_token": "ACCESS_TOKEN",<br> "expires_in": TIME_IN_SECONDS,<br> "token_type": "Bearer"<br>} |
| Error Response Code | 400 |
| Error Response | {<br> "responseCode": 0",<br> "responseMessage": "invalid_client\|unauthorized_client"<br>} |
| Response Messages | Invalid_client - Client authentication failed.<br>Unauthorized_client - client is not allowed to generate or refresh tokens. |


#### Other response codes

Further response codes and details can be found [here](response-codes).
