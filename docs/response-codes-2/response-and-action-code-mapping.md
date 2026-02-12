---
title: Response and action code mapping
deprecated: false
hidden: false
metadata:
  robots: index
---
<!-- MIGRATION_METADATA
Migrated-From: https://developer.sprint.paymentology.com/response-codes-2/response-and-action-code-mapping/
Source-Slug: response-and-action-code-mapping
Migrated-On: 2026-02-12T21:32:07+00:00
Migrated-By: wp-readme-migration
-->

Each action taken on a transaction is associated with a code; different codes are assigned to the same action by different parties/networks i.e. Mastercard, Visa, Remote API, Transaction Stream.

The table below shows the different codes used by Mastercard, UnionPay and Visa and how they are mapped to [Remote API Response Codes](/) and [Paymentology’s Transaction Stream (PubNub)](../documentation/notifications).


## Response and action code mapping table


| TRANSACTION STREAM/PUBNUB RESPONSE CODE | REMOTE API RESPONSE CODE | DESCRIPTION | ISO_VAR_1993 (GIM) | MASTERCARD | VISA (BASE 1) | UNIONPAY |
| --- | --- | --- | --- | --- | --- | --- |
| 0000 | 1 | APPROVED | 00 | 00 | 00 | 00 |
| 0002 | 2 | APPROVED FOR APRTIAL AMOUNT | 3 *** (3) | 10 | 10 | 10 |
| 1000 | -7 AND -9 | DO NOT HONOUR | 100 | 05 | 05 | 05 |
| 1001 | -36 | EXPIRED CARD | 201 *** (2001) | 54 | 54 | 54 |
| 1002 | -37 | SUSPECTED FRAUD | 102 | 57 *** (1019) | 59 | 59 |
| 1004 | -29 | RESTRICTED CARD | 104 *** (1018) | 62 | 62 | 62 *** (9999) |
| 1006 | -26 | ALLOWABLE PIN TRIES EXCEEDED | 106 *** (2006) | 75 | 75 | 75 |
| 1009 | -8 | INVALID CARD ACCEPTOR | 109 | 12 | 03 *** (3) | 12 *** (9102) |
| 1010 | -19 | INVALID AMOUNT | 110 | 13 | 13 *** (13) | 13 |
| 1011 | -4 | INVALID CARD NUMBER | 202 *** (2002) | 14 | 14 *** (14) | 14 |
| 1015 | -41 | REQUESTED FUNCTION NOT SUPPORTED | 115 | 12 *** (1009) | 12 *** (1061) | 12 *** (9102) |
| 1016 | -17 | NOT SUFFICIENT FUNDS | 116 | 51 | 51 *** (51) | 51 |
| 1017 | -25 | INCORRECT PIN | 117 | 55 | 55 | 55 |
| 1018 | -16 | NO CARD RECORD | 202 *** (2002) | 14 *** (1011) | 14 *** (14) | 14 *** (1011) |
| 1019 | -784 | TRANSACTION NOT PERMITTED TO CARDHOLDER | 119 | 57 | 57 *** (57) | 57 |
| 1020 | -5 | TRANSACTION NOT PERMITTED TO TERMINAL | 120 | 58 | 58 | 58 |
| 1021 | -18 | EXCEEDS WITHDRAWAL AMOUNT LIMIT | 123 *** (1023) | 61 | 61 | 61 |
| 1022 | -24 | SECURITY VIOLATION | 183 *** (1045) | 63 | 63 *** (63) | 05 *** (1000) |
| 1025 | -17 | CARD NOT EFFECTIVE | - | 96 *** (9109) | 06 *** (9999) | - |
| 1026 | -27 | INVALID PIN BLOCK | - | 96 *** (9109) | 81 *** (9119) | - |
| 1027 | -28 | PIN LENGTH ERROR | 127 | 55 *** (1017) | 55 *** (1017) | 55 *** (1017) |
| 1035 | -34 | CLOSED ACCOUNT | 125 *** (1000) | 78 | 46 *** (46) | - |
| 1075 |  | MISSING EXPIRY DATE | 201 *** (2001) | 54 *** (1001) | 54 *** (1001) | 54 *** (1001) |
| 1076 |  | INCORRECT EXPIRY DATE | 201 *** (2001) | 54 *** (1001) | 54 *** (1001) | 54 *** (1001) |
| 1077 |  | EXPIRED CVV2 | 183 *** (1045) | 63 *** (1022) | N7 *** (9124) | 05 *** (1000) |
| 2008 | -38 | LOST CARD | 208 | 41 | 41 | 41 |
| 2009 | -39 | STOLEN CARD | 209 | 43 | 43 | 43 |
| 4000 |  | REVERSAL ACCEPTED | - | 96 *** (9109) | 06 *** (9999) | 00 *** (0) |
| 9102 | -41 | INVALID TRANSACTION | 902 | 12 *** (1009) | 12 *** (1061) | 12 |
| 9111 | -7 | CARD ISSUER TIMED OUT | 911 | 82 | 91 *** (9107) | 98 *** (9999) |
| 9113 | -3 | DUPLICATE TRANSMISSION | 308 *** (3008) | 94 | 12 *** (1061) | 94 |
