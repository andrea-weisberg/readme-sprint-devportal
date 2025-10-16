---
title: Pre-Arbitration
deprecated: false
hidden: false
metadata:
  robots: index
---
<p>This method is used to submit a Pre-Arbitration case.</p>

<h2>Request/response fields and samples</h2>

#### Path parameters

| Parameter | type | Limits | required | Description |
|---|---|---|:--:|---|
| claimId | String |  | ✓ | <p>Claim id</p> |
| chargebackId | String |  | ✓ | <p>Chargeback id</p> |
| preArbitrationAmount | String |  | ✓ | <p>Pre-Arbitration case amount in cardholder currency.</p> |
| memo | String |  | ✓ | <p>Memo for the case</p> |
| messageText | String |  |  | <p>Message text. Use only when applicable, otherwise leave empty</p> |
| newReasonCode | String |  |  | <p>New reason code. Use only when applicable i.e. changing reason code. Otherwise left empty.<br  /> Chargeback reason code list available <a href="https://developer.sprint.paymentology.com/chargeback-api/chargeback-reason-codes/">here</a></p> |
| supportingDocument | String |  |  | <p>Document to support the case.<br  /> Use only when applicable, otherwise leave empty</p> |
| clientReferenceNumber | String |  |  | <p>Client reference number.<br  /> Use only when applicable, otherwise leave empty</p> |
| caseNotes | String |  |  | <p>Case notes.<br  /> Use only when applicable, otherwise leave empty</p> |

```json
{
    "claimId": "CLAIM_ID",
    "chargebackId": "CHARGEBACK_ID",
    "preArbitrationAmount": "PREARBITRATION_AMOUNT",
    "memo": "MEMO",
    "messageText": "MESSAGE_TEXT",
    "newReasonCode": "NEW_REASON_CODE",
    "supportingDocument": "BASE64_ENCODED_FILE_HERE",
    "clientReferenceNumber": "CLIENT_REFERENCE_NUMBER",
    "caseNotes": "CASE_NOTES"
}

```,```json
{
    "caseId": "CASE_ID"
}

```

#### Response schema

| Field | type | Description |
|---|---|---|
| caseId | String | <p>Pre-arbitration case id</p> |

```json
{
    "claimId": "CLAIM_ID",
    "chargebackId": "CHARGEBACK_ID",
    "preArbitrationAmount": "PREARBITRATION_AMOUNT",
    "memo": "MEMO",
    "messageText": "MESSAGE_TEXT",
    "newReasonCode": "NEW_REASON_CODE",
    "supportingDocument": "BASE64_ENCODED_FILE_HERE",
    "clientReferenceNumber": "CLIENT_REFERENCE_NUMBER",
    "caseNotes": "CASE_NOTES"
}

```,```json
{
    "caseId": "CASE_ID"
}

```

<h4>Other response codes</h4>
<p>Further response codes and details can be found <a href="https://developer.sprint.paymentology.com/chargeback-api/response-codes/">here</a>.</p>

<h2>Additional info</h2>

