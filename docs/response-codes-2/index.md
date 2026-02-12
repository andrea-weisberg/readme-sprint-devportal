---
title: Response Codes – Remote API
deprecated: false
hidden: false
metadata:
  robots: index
---
<!-- MIGRATION_METADATA
Migrated-From: https://developer.sprint.paymentology.com/response-codes-2/
Source-Slug: response-codes-2
Migrated-On: 2026-02-12T21:14:56+00:00
Migrated-By: wp-readme-migration
-->

| Code | Description |
| --- | --- |
| 1 | Approved |
| 2 | Approved - Partial amount |
| -2 | Invalid card number |
| -3 | Duplicate transmission |
| -4 | Invalid card number (use for invalid wallet reference) |
| -5 | Transaction not permitted to Terminal / Transaction not permitted to Acquirer |
| -6 | Function not supported / Invalid transaction |
| -7 | Transaction timeout |
| -8 | Authentication failed (Incorrect checksum) |
| -9 | Do not honor (general decline, no specific reason given, technical error) |
| -13 | Stolen card |
| -14 | Insufficient funds |
| -16 | Exceeds Purchase amount limit |
| -17 | Not sufficient funds |
| -18 | Exceeds withdrawal amount limit |
| -19 | Invalid amount |
| -24 | Security violation |
| -25 | Incorrect PIN |
| -26 | Allowable PIN tries exceeded |
| -27 | Invalid PIN block |
| -28 | PIN length error |
| -29 | Restricted card |
| -34 | Account closed / Invalid account |
| -36 | Expired card |
| -37 | Suspected fraud |
| -38 | Lost card |
| -39 | Stolen card |
| -41 | Requested function not supported / Invalid transaction |
| -783 | Do not honor (general decline, no specific reason given, technical  error) |
| -784 | Transaction not permitted to Cardholder / Transaction not permitted to Issuer |


---

## Important

Any argument that has the type date needs to follow the XML-RPC specified ISO 8601 date-time format: <dateTime.iso8601>YYYYMMDDTHH:mm:ss<dateTime.iso8601>


Any transaction amount is represented as its cent value; therefore an integer rather than a decimal.

- R100.50 is therefore represented as 10050 rand cents.

- $10.50 is therefore represented as 1050 dollar cents.


KLV: A type of TLV encoded string with characteristics:

- A Key indicator of 3 digits, zero left padded.

- A Length indicator of 2 digits, zero left padded.

- A Value with the number of characters as specified by the Length indicator.

### It is important to note:

- Transactions may or may not contain keys depending on the type of transactions

- Keys do not need to be in any particular order or sequence within transactionData

- Customers must be able to receive all keys available within transactionData

- Customers may ignore keys not pertinent to processing.

- You must be able to successfully process messages that contain new unannounced keys.

- Available keys are subject to change and will often be customer specific, thus these will be communicated via means other than this API documentation.

For example the KLV **01206AB48DE003044577** contains:

- Key 012 with length 06 and value AB48DE

- Key 003 with length 04 and value 4577

Please refer to the lookup table for the available values.


## Matching response codes

You can refer to the [Response and action code mapping table](response-and-action-code-mapping) to understand how Remote API Response Codes map to different networks.
