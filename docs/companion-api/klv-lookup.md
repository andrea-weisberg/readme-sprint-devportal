---
title: KLV Lookup
excerpt: >-
  Understand the Key-Length-Value (KLV) data encoding standard and its
  application in transaction data.
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  robots: index
---
<!-- MIGRATION_METADATA
Migrated-From: https://developer.sprint.paymentology.com/companion-api/klv-lookup/
Source-Slug: klv-lookup
Migrated-On: 2026-02-12T18:44:20+00:00
Migrated-By: wp-readme-migration
-->

Key-Length-Value (KLV) is a data encoding standard where the **Key** identifies the data, **Length** specifies the data’s length and **Value** is the data itself. KLV is an instance of the TLV encoding scheme used for optional information element within communication protocols.

**The length of each string is:**

- A Key indicator of 3 digits, zero left padded.

- A Length indicator of 2 digits, zero left padded.

- A Value with the number of characters as specified by the Length indicator.

**It is important to note:**

- Keys do not need to be in any particular order or sequence within transactionData.

- Customers must be able to receive all keys available within transactionData,

- Customers may ignore keys not pertinent to processing.

- You must be able to successfully process messages that contain new unannounced keys.

- Available keys are subject to change and will often be customer specific, thus these will be communicated via means other than this API documentation.

For example, the KLV 00206AB48DE026044577 contains:

1. Key 002 with length 06 and value AB48DE

2. Key 026 with length 04 and value 4577

- Transactions may or may not contain keys depending on the type of transactions.

- Transaction types which include KLV data are:

[Balance](api-reference-companion/remote/balance/)

[Deduct](api-reference-companion/remote/#Deduct)

[Deduct Adjustment](api-reference-companion/remote/#DeductAdjustment)

[Load Auth](api-reference-companion/remote/#LoadAuth)

[Load Auth Reversal](api-reference-companion/remote/loadauthreversal/)

[Load Adjustment](api-reference-companion/remote/#LoadAdjustment)

[Stop](api-reference-companion/remote/#Stop)

- Tokenisation

[Administrative](api-reference-companion/remote/#AdministrativeMessage)**[ Message](api-reference-companion/remote/#AdministrativeMessage)**

- 3DSecure

[3DSecureOTP](api-reference-companion/remote/administrativemessage/#3DSecure)

[3DSecureAppAuthentication](api-reference-companion/remote/administrativemessage/#3DSAppAuth)

-

original transaction amount

-

original currency code

-

merchant description

-

[3DSecureAppFinalisation](api-reference-companion/remote/administrativemessage/#3DSAppFinal)

-

-

status


---

### KLV Data

| Key Name | Index | Values | Additional Information | Applicable to |
| --- | --- | --- | --- | --- |
| Tracking Number | 002 | Card tracking number |  | Virtual & Physical |
| Original Transaction Amount | 004 | Original amount of the incoming transaction |  | Virtual & Physical |
| Conversion Rate | 010 | Forex conversion rate at the time of the transaction. The same value received from the network is echoed in the companion call. The leftmost digit of this field signifies the number of decimal places in the rate, and the remaining 7 digits give the actual rate. For example, 69972522 represents 9.972522 |  | Virtual & Physical |
| Merchant category code | 026 | The four digit MCC that defines the sort of merchant making the transaction |  | Virtual & Physical |
| Acquiring Institution Code | 032 | The code for the Acquiring Institution |  | Virtual & Physical |
| Retrieval Reference Number | 037 | The retrieval reference number of the transaction |  | Virtual & Physical |
| Terminal ID | 041 | The terminal ID where the transaction is done |  | Virtual & Physical |
| Merchant Identifier | 042 | The merchant identifier for the transaction |  | Virtual & Physical |
| Merchant Description | 043 | The merchant description for the data |  | Virtual & Physical |
| Merchant name | 044 | Merchant name provided as part of tokenization messages |  | Tokenization |
| Transaction type Identifier | 045 | Transaction type Identifier "TTI" used for funding |  | Virtual, physical and Money send |
| Fraud scoring data | 048 | Fraud score received in transaction message | Mastercard only | Virtual & Physical |
| Original Currency Code | 049 | The original currency code of the transaction |  | Virtual & Physical |
| From Account | 050 | Indicate cardholder account type :<br><br>00 = Default Account (Not specified or not applicable)<br><br> 10 = Savings Account<br><br> 20 = Checking Account<br><br>30 = Credit Card Account<br> **Note:** This type of multiple account card is currently specific to South American markets. |  | Virtual & Physical |
| Pin Block | 052 | A PIN block in 3DES ISO-1 format |  | Physical |
| POS Data | 061 | Data from the POS terminal used in the transaction |  | Physical |
| TraceID | 063 | Additional data received from Mastercard Network DE 48, Sub element 63 |  | Virtual & Physical |
| Extended payment code | 067 | Code indicating extended payment transaction |  | Virtual & Physical |
| Is recurring | 068 | Indicates that a transaction is recurring |  | Virtual & Physical |
| message reason code | 069 | 4 digit | can be empty | All card types and transactions |
| Markup Amount | 085 | The markup amount applied to the transaction |  | Virtual & Physical |
| Recipient Name | 108 | Name of the recipient of the funds in the transaction |  | Moneysend |
| Recipient address | 109 | Street address of the person who receives the funds in the transaction |  | Moneysend |
| Recipient account number | 110 | The account number of the person who receives the funds |  | Moneysend |
| Recipient account number type | 111 | The account type of the person who receives the funds |  | Moneysend |
| Capture Mode | 250 | **Note:** We are in a transition period to implement a new behavior of this KLV index. KLV 250 will be used in conjunction with KLV 262 to show capture mode and transaction type.<br>Details can be found at [What's New](../get-started/whats-new)<br><br>MAG - Magstripe<br><br> MAN - Manual (Terminal)<br><br> EMV - EMV<br><br> OB - On Behalf (EMV)<br><br> NFC - NFC (EMV)<br><br> ECOM - Ecommerce<br><br>3DS - 3D-Secure (Ecommerce)<br><br> ADJ - Adjustment |  | Virtual & Physical |
| Network | 251 | Local<br> Mastercard<br> VISA<br>CUP<br>Unknown<br> Adjustment |  | Virtual & Physical |
| Fee Type | 252 | 0 - No fee<br><br>31 - Insufficient Funds<br><br>32 - Withdrawal Limit Exceeded<br><br>33 - Security Violation<br><br>34 - Transaction Not Supported<br><br>35 - PIN Tries Exceeded<br><br>36 - Invalid PIN<br><br> 37 - PIN Length Error<br>38 - Expired Card |  | Virtual & Physical |
| Last four digits PAN | 253 | The account number's last four digits of the card being swiped. |  | Physical |
| MDES Digitized PAN | 254 | The PAN which was digitized |  | Tokenization - MDES |
| MDES Digitized Wallet ID | 255 | The Wallet ID (Wallet Reference) used to digitize the card.<br><br>327 - M4M<br><br>216 - Google Pay<br><br>217 - Samsung Pay<br><br>103 - Apple Pay |  | Tokenization - MDES |
| Adjustment Reason | 256 | 99 - Generic reason<br><br>00 - MasterCard initiated<br><br>01 - Forex conversion difference<br><br>02 - Settlement without authorization<br><br>03 - Reversal timeout/ not accepted<br><br>04 - Refund<br><br>05 - Chargeback<br><br>06 - MoneySend<br><br>07 - Purchase Cancellation - ONLY applicable to Union Pay<br><br>08 - Purchase Cancellation Reversal - ONLY applicable to Union Pay<br><br> 09 - Stand-in<br><br> 10 - Mass Transit Debt Collection<br><br> 11 - Final settlement - Unused funds<br><br> 26 - OCT (Visa only) |  | Virtual, Physical and Moneysend |
| Reference ID | 257 | Transaction ID of the original Deduct if any |  | Virtual & Physical |
| Markup Type | 258 | 0 - No markup<br><br>1 - Regular markup<br><br>2 - DCC markup |  | Virtual & Physical |
| Acquirer Country | 259 | Country of the acquirer of a transaction |  | Virtual & Physical |
| Mobile number | 260 | Data containing the mobile number entered |  | Virtual & Physical |
| Transaction Fee Amount | 261 | Fee amount applicable to the incoming transaction if any | Always sent in the 'Deduct' call | Virtual & Physical |
| Transaction subtype | 262 | **Note:** We are in a transition period to implement a new behavior of this KLV index. KLV 250 will be used in conjunction with KLV 262 to show capture mode and transaction type.<br>Details can be found at [What's New](../get-started/whats-new)<br><br>Identifies a transaction as MDES or 3DS<br>*NB. This field will be empty if the transaction is neither MDES nor 3DS* |  | MDES - 3DS |
| Card Issuer Data | 263 | Information about the card issuer | Colombia only | Virtual & Physical |
| Tax | 264 | Amount of tax charged on transaction | Colombia only | Virtual & Physical |
| Tax amount base | 265 | Value of the tax base amount used | Colombia only | Virtual & Physical |
| Retailer data | 266 | Information about the retailer where transaction took place | Colombia only | Virtual & Physical |
| IAC Tax amount | 267 | Rate levied by IAC | Colombia only | Virtual & Physical |
| Number of Installments | 268 | Number of installments to pay for the transaction |  | Virtual & Physical |
| Customer ID | 269 | ID value that identifies the customer | Colombia only | Virtual & Physical |
| Security Services Data | 270 | Authentication risk analysis reason codes (ARA) | Mastercard only | Virtual & Physical |
| On behalf of services | 271 | Indicates this is a 'on behalf of' transaction |  | Virtual & Physical |
| Original Merchant Description | 272 | The original description received from the merchant |  | Virtual & Physical |
| Installments financing type | 273 | Data that indicates the type of financing selected to pay installments | Brazil only | Virtual & Physical |
| Status | 274 | Associated with 3D Secure Out of Band authentication, providing additional status information in the Administrative Message 3DSecureAppFinalisation.<br>This field communicates status updates crucial for verifying transactions securely through a separate channel, typically a mobile app.<br><br>Possible values:<br><br>0 - Successfully received final status<br><br>1 - Timer on browser expired before response was received<br><br>2 - General error<br><br>3 - Transaction cancelled before response was received |  | Virtual & Physical |
| Installments grace period | 275 | Data indicating duration of the grace period for payment of the installment | Mexico only | Virtual & Physical |
| Installments type of credit | 276 | Data indicating the type of credit used for the installment transaction | Mexico only | Virtual & Physical |
| Payments Initiator | 277 | Represents who triggered the transaction. Potential values are "merchant", "cardholder", or an empty string/no value when cannot be determined | Mastercard only | Virtual & Physical |
| Payment Initiator Subtype | 278 | Some values can be either merchant initiated transactions or cardholder initiated transactions, such as Standing Order, where the first payment would typically be initiated by the cardholder. Potential values, when available:<br><br>- "Unscheduled Credential on File"<br><br>- "Standing Order"<br><br>- "Subscription"<br><br>-  "Installment"<br><br>- "Partial Shipment"<br><br>-  "Related/Delayed Charge"<br><br>- "No Show Charge"<br><br>- "Resubmission"<br><br>- "Credential-on-file" | Mastercard only | Virtual & Physical |
| Additional amount | 300 | Cashbacks come as an "additional amount" | Columbia only |  |
| Second additional amount | 301 | There can be a maximum of two cashback amounts that can come through in a transaction |  | Virtual & Physical |
| cashback POS currency code | 302 | Represents the currency code of the cashback amount |  | Physical |
| cashback POS amount | 303 | Displays the actual cashback amount |  | Physical |
| Sender name | 400 | Name of the sender |  | Visa Direct & Money send |
| Sender Address | 401 | Street address of the person who sent the funds in the transaction |  | Visa Direct & Money send |
| Sender city | 402 | Name of the city of the person who sent the funds in the transaction | Visa Direct only | Visa Direct only |
| Sender state | 403 | Name of the State if the person who sent the funds in the transaction | Visa Direct only | Visa Direct only |
| Sender country | 404 | Name of the country of the person who sent the funds in the transaction | Visa Direct only | Visa Direct only |
| Sanction screening score | 405 | Data indicating the score achieved during sanction screening in the transaction |  | Visa Direct and Moneysend |
| Business application identifier | 406 | Code that identifies the intended use of a push payment in the transaction | Visa Direct only | Visa Direct only |
| Special condition indicator | 408 | Data indicating any special conditions for the transaction | Visa Direct only | Visa Direct only |
| Business tax ID | 409 | Data indicating the value of the business's tax ID number | Visa Direct only | Visa Direct only |
| Individual tax ID | 410 | Data indicating the value of the customer/individual's tax ID number | Visa Direct only | Visa Direct only |
| Source of funds | 411 | Data indicating where the funds come from |  | Visa Direct  & Money send |
| Sender account number | 412 | The account number of the person who sent/paid the funds |  | Visa Direct  & Money send |
| Sender Account Number Type | 413 | The account type of the person who sent/paid the funds |  | Visa Direct  & Money send |
| MVV | 414 | Merchant Verification Value is used to identify merchants that participate in various programs and is unique to a merchant | Visa Direct only | Visa Direct only |
| Sender reference number | 415 | sender reference number | (Visa Direct only) | Visa Direct only |
| is afd transaction | 416 | AFD Transaction indicator for MCC 5542.<br><br>1: AFD TXN, 0: NOT AFD |  | Virtual & Physical (AFD only) |
| acquirer fee amount | 417 | Acquirer fee amount in transaction currency |  | Virtual & Physical |
| Address Verification Result | 418 | 0- postal/zip code and address matches<br><br>1-postal/zip code matches, address does not<br><br>2-Address matches, postal/zip code does not match<br><br>3-Neither address nor postal/zip code match |  | Virtual & Physical |
| Postal code / ZIP code | 419 | Cardholder postal/ZIP code |  | Virtual & Physical |
| Street address | 420 | Cardholder street address only without city or area |  | Virtual & Physical |
| Sender Date of Birth | 421 | The Date of Birth of the person who sends the funds in the transaction. | Visa Direct only | Visa Direct only |
| OCT Activity check result | 422 | The activity check result of the Original Credit Transaction (OCT) when velocity checking has been performed.<br><br>1 = 1-day count or amount exceeded.<br><br>2 = 7-day count or amount exceeded.<br><br>3 = 30-day count or amount exceeded. | Visa Direct only | Visa Direct only |
| Sender postal code | 423 | The postal code of the person who sends the funds in the transaction. | Visa Direct only | Visa Direct only |
| Recipient city | 424 | The city of the person who receives the funds in the transaction. | Visa Direct only | Visa Direct only |
| Recipient country | 425 | The country of the person who receives the funds in the transaction. | Visa Direct only | Visa Direct only |
| 3D Secure OTP | 900 | Dynamic One Time Password for 3D Secure |  | 3DS |
| Digitization activation | 901 | The password needed to activate an MDES digitization request |  | Tokenization |
| Digitization activation method type | 902 | Method used to send OTP to activate a token |  | Tokenization |
| Digitization activation method value | 903 | Code/ numerical value that indicates method used to send OTP to activate a token |  | Tokenization |
| Digitization activation expiry | 904 | Expiry of the activation |  | Tokenization |
| Digitization final tokenization decision | 905 | 1 = approve<br><br>2 = approve but with additional authentication |  | Tokenization |
| Device name | 906 | Up tp 20 characters. This is the device name associated with the wallet provider |  | Tokenization |
| Digitized Device ID | 910 | The ID of the type of device used for tokenization |  | Tokenization |
| Digitized PAN expiry | 911 | Expiry date of the DPAN |  | Tokenization |
| Digitized FPAN Masked | 912 | The masked FPAN |  |  |
| Token Unique Reference | 913 | The token reference during the process |  | Tokenization |
| Digitized Token Requestor ID | 915 | Token Requestor ID during the process |  | Tokenization |
| Visa Digitized PAN | 916 | The digitized PAN for Visa | Visa only | Tokenization - VTS |
| Visa token type | 917 | Data indicating the type of token | Visa only | Tokenization - VTS |
| POS Transaction Status | 920 | Point-of-Service Data about the transaction status<br> 0 = Standard request<br> 1 = Deferred authorization<br> 4 = Pre-authorization request |  | Physical |
| POS Transaction Security | 921 | Point-of-Service Data about the security |  | Physical |
| POS Authorisation Lifecycle | 922 | Point-of-Service Data about the Authorisation Lifecycle |  | Physical |
| Digitization event type | 923 | Event types include:<br>Deleted<br><br> Deleted_from_device<br><br>Stopped<br><br>Digitized<br><br> Digitization_Exception<br><br>Replacement |  | Tokenization |
| Digitization event reason code | 924 | Code relating to a Digitization Exception event type |  | Tokenization |
| Supports partial auth | 925 | Indicates a transaction supports partial authorisation transaction |  | Virtual and Physical |
| Digitization path | 929 | GREEN<br><br>YELLOW<br><br>ORANGE<br><br>RED |  | Tokenization |
| Wallet recommendation | 930 | Decline<br><br>Approve<br><br>Require_additional_authentication |  | Tokenization |
| Tokenization pan source | 931 | card_on_file<br><br>card_added_manually<br><br>card_added_via_application<br><br>existing_token_credential<br><br>card_added_via_browser |  | Tokenization |
| Unique Transaction Reference | 932 | Unique Transaction Reference number for Mastercard MoneySend payment |  | Moneysend |
| Transaction purpose | 933 | Transaction purpose details |  | Moneysend |
| 3D Secure OTP RefCode | 934 | Dynamic 4 letters reference code to be used along with 3DS OTP messages | BankServ only | 3DS |
| Generic Key | 999 | Reserved for other uses |  |  |


---

### Stop Reason ID Codes

| Reason ID | Internal Code | Network response (Mastercard) | Network response (Visa) | Description |
| --- | --- | --- | --- | --- |
| 1 | 2008 | 41 | 41 | Lost Card |
| 2 | 2009 | 43 | 43 | Stolen Card |
| 3 | 1004 | 62 | 62 | Do not honor |
| 4 | 1016 | 51 | 51 | Insufficient funds |
| 5 | 1018 | 14 | 14 | Invalid card number |
| 6 | 1006 | 75 | 75 | PIN tries exceeded |
| 7 | 1002 | 05 | 59 | Do not honor |
| Other | 1000 | 05 | 05 | Do not honor |
