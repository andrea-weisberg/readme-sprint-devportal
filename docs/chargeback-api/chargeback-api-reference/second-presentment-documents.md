---
title: Second Presentment Documents
deprecated: false
hidden: false
metadata:
  robots: index
---
<p>Once in the 2nd Presentment phase, this API method is used to receive the supporting documents raised by the acquirer for a claim.</p>

<h2>Request/response fields and samples</h2>

#### Path parameters

| Parameter | Type | Limits | Required | Description |
|---|---|---|:--:|---|
| chargebackId | String |  | ✓ | <p>Chargeback ID</p> |
| claimID | String |  | ✓ | <p>Claim ID</p> |
| format | String |  | ✓ | <p>File format. Possible values:<br /> ORIGINAL,<br /> MERGED_TIFF,<br /> MERGED PDF</p> |

```json
{
    "chargebackId": "CHARGEBACK ID",
    "claimID": "CLAIM_ID",
    "format": "ORIGINAL_TIFF"
}

```,```json
{
    "fileAttachment": {
        "filename": "FILE_NAME",
        "file": "BASE64_ENCODED_FILE"
    }
}

```

#### Response schema

| Field | Type | Description |
|---|---|---|
| fileAttachment | Object | <p>File attachment</p> |
| filename | String | <p>Filename</p> |
| file | String | <p>File content in base64 encoded string</p> |

```json
{
    "chargebackId": "CHARGEBACK ID",
    "claimID": "CLAIM_ID",
    "format": "ORIGINAL_TIFF"
}

```,```json
{
    "fileAttachment": {
        "filename": "FILE_NAME",
        "file": "BASE64_ENCODED_FILE"
    }
}

```

<h4>Other response codes</h4>
<p>Further response codes and details can be found <a href="https://developer.sprint.paymentology.com/chargeback-api/response-codes/">here</a>.</p>

<h2>Additional info</h2>

