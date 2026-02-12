---
title: Document Status
deprecated: false
hidden: false
metadata:
  robots: index
---
<p>Once a document is uploaded, use this method to verify the status of document.</p>

<h2>Request/response fields and samples</h2>

#### Path parameters

| Parameter | type | Limits | required | Description |
|---|---|---|:--:|---|
| chargebackId | String |  | ✓ | <p>Chargeback id</p> |
| claimID | String |  | ✓ | <p>Claim id</p> |

```json
{
    "chargebackId": "CHARGEBACK id",
    "claimID": "CLAIM_ID"
}

```,```json
{
    "status": "COMPLETED"
}

```

#### Response schema

| Field | type | Description |
|---|---|---|
| status | String | <p>Chargeback document status</p> |

```json
{
    "chargebackId": "CHARGEBACK id",
    "claimID": "CLAIM_ID"
}

```,```json
{
    "status": "COMPLETED"
}

```

<h4>Other response codes</h4>
<p>Further response codes and details can be found <a href="https://developer.sprint.paymentology.com/chargeback-api/response-codes/">here</a>.</p>

<h2>Additional info</h2>

