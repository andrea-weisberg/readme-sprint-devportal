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

| Parameter | Type | Limits | Required | Description |
|---|---|---|:--:|---|
| chargebackId | String |  | ✓ | <p>Chargeback ID</p> |
| claimID | String |  | ✓ | <p>Claim ID</p> |

```json
{
    "chargebackId": "CHARGEBACK ID",
    "claimID": "CLAIM_ID"
}

```,```json
{
    "status": "COMPLETED"
}

```

#### Response schema

| Field | Type | Description |
|---|---|---|
| status | String | <p>Chargeback document status</p> |

```json
{
    "chargebackId": "CHARGEBACK ID",
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

</h2></a></p></h4></p></p></p></h2></p>
