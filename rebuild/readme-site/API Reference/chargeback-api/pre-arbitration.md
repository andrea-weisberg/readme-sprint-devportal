# Pre-Arbitration

This method is used to submit a Pre-Arbitration case.

## Request/response fields and samples

Claim ID

Chargeback ID

Pre-Arbitration case amount in cardholder currency.

Memo for the case

Message text. Use only when applicable, otherwise leave empty

New reason code. Use only when applicable i.e. changing reason code. Otherwise left empty.
Chargeback reason code list available [here](/api-reference/chargeback-api/chargeback-reason-codes)

Document to support the case.
Use only when applicable, otherwise leave empty

Client reference number.
Use only when applicable, otherwise leave empty

Case notes.
Use only when applicable, otherwise leave empty

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

Pre-arbitration case ID

{
"caseId": "CASE_ID"
}

#### Other response codes

Further response codes and details can be found [here](/api-reference/chargeback-api/response-codes).

## Additional info
