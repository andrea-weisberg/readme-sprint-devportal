---
title: First Chargeback
deprecated: false
hidden: false
metadata:
  robots: index
---
<p>After successfully connecting to the API Proxy, you can send the <b><i>fields/parameters</i></b> for the API request (as specified below) and receive a <b><i>response</i></b>.</p>
<p>A successfully submitted First Chargeback will remain in a “pending status” (no more than 72 hours) on issuers’ behalf to allow merchants to respond and resolve the inquiry.</p>

<h2>Request/response fields and samples</h2>

```json
{
    "trackingNumber": "tRaCkInGnUmBeR",
    "transactionId": "tRaNsAcTiOnId",
    "authnumber": "AuthNumber",
    "systemDate": "2021-08-24 00:00:00",
    "settlementAmount": 402.76,
    "chargebackAmount": 5.74,
    "reasonCode": "4834",
    "supportingDocument": "BASE64_ENCODED_FILE_HERE"
}

```,```json
{
    "chargebackId": "CHARGEBACK ID",
    "claimID": "CLAIM_ID"
}

```

#### Response schema

| Field | Type | Description |
|---|---|---|
| chargebackId | String | <p>Chargeback ID</p> |
| claimID | String | <p>Claim ID</p> |

```json
{
    "trackingNumber": "tRaCkInGnUmBeR",
    "transactionId": "tRaNsAcTiOnId",
    "authnumber": "AuthNumber",
    "systemDate": "2021-08-24 00:00:00",
    "settlementAmount": 402.76,
    "chargebackAmount": 5.74,
    "reasonCode": "4834",
    "supportingDocument": "BASE64_ENCODED_FILE_HERE"
}

```,```json
{
    "chargebackId": "CHARGEBACK ID",
    "claimID": "CLAIM_ID"
}

```

<h4>Other response codes</h4>
<p>Further response codes and details can be found <a href="https://developer.sprint.paymentology.com/chargeback-api/response-codes/">here</a>.</p>

<h2>Additional info</h2>

