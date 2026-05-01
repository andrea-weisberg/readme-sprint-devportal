# Query Chargeback

This method is used to query chargeback data from Paymentology.

## Request/response fields and samples

Tracking number

Transaction ID

Auth number

System date

Settlement amount

Amount to chargeback

Reason code. Chargeback reason code list available [here](/api-reference/chargeback-api/chargeback-reason-codes)

{
"trackingNumber": "TRACKING_NUMBER",
"transactionId": "TRANSACTION_ID",
"authNumber": "AUTH_NUMBER",
" systemDate": "systemDate",
" settlementAmount": "SETTLEMENT_AMOUNT",
" chargebackAmount": "CHARGEBACK_AMOUNT",
" reasonCode": "REASON_CODE"
}

Claim ID

Chargeback ID

[
{
" claimID": "CLAIM_ID",
" chargebackID": "CHARGEBACK_ID"
}
]
