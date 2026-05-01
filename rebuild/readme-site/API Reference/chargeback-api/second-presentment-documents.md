# Second Presentment Documents

Once in the 2nd Presentment phase, this API method is used to receive the supporting documents raised by the acquirer for a claim.

Once in the 2nd Presentment phase, this API method is used to receive the supporting documents raised by the acquirer for a claim.

## Request/response fields and samples

Chargeback ID

Claim ID

File format. Possible values:
ORIGINAL,
MERGED_TIFF,
MERGED PDF

{
"chargebackId": "CHARGEBACK ID",
"claimID": "CLAIM_ID",
"format": "ORIGINAL_TIFF"
}

File attachment

Filename

File content in base64 encoded string

{
"fileAttachment": {
"filename": "FILE_NAME",
"file": "BASE64_ENCODED_FILE"
}
}

#### Other response codes

Further response codes and details can be found [here](/api-reference/chargeback-api/response-codes).

## Additional info
