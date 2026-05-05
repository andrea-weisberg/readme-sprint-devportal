---
title: Upload Supporting Document
category:
  uri: Chargeback API
slug: upload-supporting-document
position: 11
parent:
  uri: chargeback-api-reference
---

This API method is used to upload a supporting document after a chargeback is successfully created.

## Request/response fields and samples

Chargeback ID

Claim ID

Memo

Filename

File content

{
"chargebackId": "CHARGEBACK ID",
"claimID": "CLAIM_ID",
"memo": "MEMO",
"filename": "FILENAME",
"file": "File content stored in a base64 encoded string"
}

{
"chargebackId": "chargebackId"
}

#### Other response codes

Further response codes and details can be found [here](/api-reference/chargeback-api/response-codes).

## Additional info
