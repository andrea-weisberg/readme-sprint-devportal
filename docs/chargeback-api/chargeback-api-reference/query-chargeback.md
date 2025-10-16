---
title: Query Chargeback
deprecated: false
hidden: false
metadata:
  robots: index
---
<p>This method is used to query chargeback data from Paymentology.</p>

<h2>Request/response fields and samples</h2>

#### Path parameters

| Parameter | Type | Limits | Required | Description |
|---|---|---|:--:|---|
| trackingNumber | String |  | ✓ | <p>Tracking number</p> |
| transactionId | String |  | ✓ | <p>Transaction ID</p> |
| authNumber | String |  |  | <p>Auth number</p> |
| systemDate | Date |  | ✓ | <p>System date</p> |
| settlementAmount | String |  |  | <p>Settlement amount</p> |
| chargebackAmount | String |  |  | <p>Amount to chargeback</p> |
| reasonCode | String |  | ✓ | <p>Reason code. Chargeback reason code list available <a href="https://developer.sprint.paymentology.com/chargeback-api/chargeback-reason-codes/">here</a></p> |

```json
{
    "trackingNumber": "TRACKING_NUMBER",
    "transactionId": "TRANSACTION_ID",
    "authNumber": "AUTH_NUMBER",
    " systemDate": "systemDate",
    " settlementAmount": "SETTLEMENT_AMOUNT",
    " chargebackAmount": "CHARGEBACK_AMOUNT",
    " reasonCode": "REASON_CODE"
}

```,```json
[
    {
        " claimID": "CLAIM_ID",
        " chargebackID": "CHARGEBACK_ID"
    }
]

```

#### Response schema

| Field | Type | Description |
|---|---|---|
| claimID | String | <p>Claim ID</p> |
| chargebackID | String | <p>Chargeback ID</p> |

```json
{
    "trackingNumber": "TRACKING_NUMBER",
    "transactionId": "TRANSACTION_ID",
    "authNumber": "AUTH_NUMBER",
    " systemDate": "systemDate",
    " settlementAmount": "SETTLEMENT_AMOUNT",
    " chargebackAmount": "CHARGEBACK_AMOUNT",
    " reasonCode": "REASON_CODE"
}

```,```json
[
    {
        " claimID": "CLAIM_ID",
        " chargebackID": "CHARGEBACK_ID"
    }
]

```
