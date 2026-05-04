---
title: KLV Lookup
category:
  uri: Guides
slug: klv-lookup
position: 23
---

Key-Length-Value (KLV) is a data encoding standard where the **Key** identifies the data, **Length** specifies the data's length and **Value**is the data itself. KLV is an instance of the TLV encoding scheme used for optional information element within communication protocols.

**The length of each string is:**

- A Key indicator of 3 digits, zero left padded.

- A Length indicator of 2 digits, zero left padded.

- A Value with the number of characters as specified by the Length indicator.

**It is important to note:**

- Keys do not need to be in any particular order or sequence within transactionData.

- Customers must be able to receive all keys available within transactionData,

- Customers may ignore keys not pertinent to processing.

- You must be able to successfully process messages that contain new unannounced keys.

- Available keys are subject to change and will often be customer specific, thus these will be communicated via means other than this API documentation. For example, the KLV 00206AB48DE026044577 contains: 1. Key 002 with length 06 and value AB48DE 2. Key 026 with length 04 and value 4577

- Transactions may or may not contain keys depending on the type of transactions.

- Transaction types which include KLV data are: [Balance](/api-reference/companion-api/balance) [Deduct](https://developer.sprint.paymentology.com/companion-api/api-reference/remote/#Deduct) [Deduct Adjustment](https://developer.sprint.paymentology.com/companion-api/api-reference/remote/#DeductAdjustment) [Load Auth](https://developer.sprint.paymentology.com/companion-api/api-reference/remote/#LoadAuth) [Load Auth Reversal](/api-reference/companion-api/loadauthreversal) [Load Adjustment](https://developer.sprint.paymentology.com/companion-api/api-reference/remote/#LoadAdjustment) [Stop](https://developer.sprint.paymentology.com/companion-api/api-reference/remote/#Stop)

- Tokenisation [Administrative](https://developer.sprint.paymentology.com/companion-api/api-reference/remote/#AdministrativeMessage)**[Message](https://developer.sprint.paymentology.com/companion-api/api-reference/remote/#AdministrativeMessage)**

- 3DSecure [3DSecureOTP](https://developer.sprint.paymentology.com/companion-api/api-reference/remote/administrativemessage/#3DSecure) [3DSecureAppAuthentication](https://developer.sprint.paymentology.com/companion-api/api-reference/remote/administrativemessage/#3DSAppAuth) original transaction amount

- original currency code

- merchant description

- [3DSecureAppFinalisation](https://developer.sprint.paymentology.com/companion-api/api-reference/remote/administrativemessage/#3DSAppFinal) status
