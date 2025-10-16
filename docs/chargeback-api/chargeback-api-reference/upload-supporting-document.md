---
title: Upload Supporting Document
deprecated: false
hidden: false
metadata:
  robots: index
---
<p>This API method is used to upload a supporting document after a chargeback is successfully created.</p>

<h2>Request/response fields and samples</h2>

#### Path parameters

| Parameter | Type | Limits | Required | Description |
|---|---|---|:--:|---|
| chargebackId | String |  | ✓ | <p>Chargeback ID</p> |
| claimID | String |  | ✓ | <p>Claim ID</p> |
| memo | String |  | ✓ | <p>Memo</p> |
| filename | String |  | ✓ | <p>Filename</p> |
| file | String |  | ✓ | <p>File content</p> |

```json
{
    "chargebackId": "CHARGEBACK ID",
    "claimID": "CLAIM_ID",
    "memo": "MEMO",
    "filename": "FILENAME",
    "file": "File content stored in a base64 encoded string"
}

```,```json
{
    "chargebackId": "chargebackId"
}

```

#### Response schema

| Field | Type | Description |
|---|---|---|
| chargebackId | String |  |

```json
{
    "chargebackId": "CHARGEBACK ID",
    "claimID": "CLAIM_ID",
    "memo": "MEMO",
    "filename": "FILENAME",
    "file": "File content stored in a base64 encoded string"
}

```,```json
{
    "chargebackId": "chargebackId"
}

```

<h4>Other response codes</h4>
<p>Further response codes and details can be found <a href="https://developer.sprint.paymentology.com/chargeback-api/response-codes/">here</a>.</p>

<h2>Additional info</h2>

</h2></a></p></h4></p></p></p></p></p></h2></p>
