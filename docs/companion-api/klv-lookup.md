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
Key-Length-value (KLV) is a data encoding standard where the **Key** identifies the data, **Length** specifies the data’s length and **value** is the data itself. KLV is an instance of the TLV encoding scheme used for optional information element within communication protocols.

**The length of each string is:**

1. A Key indicator of 3 digits, zero left padded.
2. A Length indicator of 2 digits, zero left padded.
3. A value with the number of characters as specified by the Length indicator.

**It is important to note:**

* Keys do not need to be in any particular order or sequence within transactionData.

* Customers must be able to receive all keys available within transactionData,

* Customers may ignore keys not pertinent to processing.

* You must be able to successfully process messages that contain new unannounced keys.

* Available keys are subject to change and will often be customer specific, thus these will be communicated via means other than this API documentation.  
  For example, the KLV 00206AB48DE026044577 contains:
  1. Key 002 with length 06 and value AB48DE
  2. Key 026 with length 04 and value 4577

* Transactions may or may not contain keys depending on the type of transactions.

* Transaction types which include KLV data are:  
  [Balance](https://developer.sprint.paymentology.com/companion-api/api-reference/remote/balance/)  
  [Deduct](https://developer.sprint.paymentology.com/companion-api/api-reference/remote/#Deduct)  
  [Deduct Adjustment](https://developer.sprint.paymentology.com/companion-api/api-reference/remote/#DeductAdjustment)  
  [Load Auth](https://developer.sprint.paymentology.com/companion-api/api-reference/remote/#LoadAuth)  
  [Load Auth Reversal](https://developer.sprint.paymentology.com/companion-api/api-reference/remote/loadauthreversal/)  
  [Load Adjustment](https://developer.sprint.paymentology.com/companion-api/api-reference/remote/#LoadAdjustment)  
  [Stop](https://developer.sprint.paymentology.com/companion-api/api-reference/remote/#Stop)

* Tokenisation  
  [Administrative Message](https://developer.sprint.paymentology.com/companion-api/api-reference/remote/#AdministrativeMessage)

* 3DSecure  
  [3DSecureOTP](https://developer.sprint.paymentology.com/companion-api/api-reference/remote/administrativemessage/#3DSecure)  
  [3DSecureAppAuthentication](https://developer.sprint.paymentology.com/companion-api/api-reference/remote/administrativemessage/#3DSAppAuth)

  * original transaction amount
  * original currency code
  * merchant description

* [3DSecureAppFinalisation](https://developer.sprint.paymentology.com/companion-api/api-reference/remote/administrativemessage/#3DSAppFinal)

  * status

***

## KLV Data

<table>
  <thead>
    <tr>
      <th align="center">Key Name</th>
      <th align="center">Index</th>
      <th align="center">Values</th>
      <th align="center">Additional Information</th>
      <th align="center">Applicable to</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">Tracking Number</td>
      <td align="center">002</td>
      <td>Card tracking number</td>
      <td></td>
      <td align="center">Virtual &amp; Physical</td>
    </tr>

    <tr>
      <td align="center">Original Transaction Amount</td>
      <td align="center">004</td>
      <td>Original amount of the incoming transaction</td>
      <td></td>
      <td align="center">Virtual &amp; Physical</td>
    </tr>

    <tr>
      <td align="center">Conversion Rate</td>
      <td align="center">010</td>
      <td>
        Forex conversion rate at the time of the transaction. The leftmost digit
        signifies the number of decimal places and the remaining digits give the
        actual rate (e.g. 69972522 → 9.972522).
      </td>
      <td></td>
      <td align="center">Virtual &amp; Physical</td>
    </tr>

    <tr>
      <td align="center">Merchant Category Code</td>
      <td align="center">026</td>
      <td>The four-digit MCC defining the merchant type</td>
      <td></td>
      <td align="center">Virtual &amp; Physical</td>
    </tr>

    <tr>
      <td align="center">Retrieval Reference Number</td>
      <td align="center">037</td>
      <td>Retrieval reference number of the transaction</td>
      <td></td>
      <td align="center">Virtual &amp; Physical</td>
    </tr>

    <tr>
      <td align="center">Terminal ID</td>
      <td align="center">041</td>
      <td>Terminal ID where the transaction occurred</td>
      <td></td>
      <td align="center">Physical</td>
    </tr>

    <tr>
      <td align="center">Merchant Identifier</td>
      <td align="center">042</td>
      <td>Merchant identifier for the transaction</td>
      <td></td>
      <td align="center">Virtual &amp; Physical</td>
    </tr>

    <tr>
      <td align="center">Merchant Name</td>
      <td align="center">044</td>
      <td>Merchant name provided in tokenization messages</td>
      <td></td>
      <td align="center">Tokenization</td>
    </tr>

    <tr>
      <td align="center">Transaction Type Identifier (TTI)</td>
      <td align="center">045</td>
      <td>Transaction type identifier used for funding</td>
      <td></td>
      <td align="center">Virtual, Physical &amp; MoneySend</td>
    </tr>

    <tr>
      <td align="center">Fraud Scoring Data</td>
      <td align="center">048</td>
      <td>Fraud score received in transaction message</td>
      <td>Mastercard only</td>
      <td align="center">Virtual &amp; Physical</td>
    </tr>

    <tr>
      <td align="center">Original Currency Code</td>
      <td align="center">049</td>
      <td>Original currency code of the transaction</td>
      <td></td>
      <td align="center">Virtual &amp; Physical</td>
    </tr>

    <tr>
      <td align="center">PIN Block</td>
      <td align="center">052</td>
      <td>PIN block in 3DES ISO-1 format</td>
      <td></td>
      <td align="center">Physical</td>
    </tr>

    <tr>
      <td align="center">Trace ID</td>
      <td align="center">063</td>
      <td>Additional data from Mastercard Network (DE48, Sub-element 63)</td>
      <td></td>
      <td align="center">Virtual &amp; Physical</td>
    </tr>

    <tr>
      <td align="center">Is Recurring</td>
      <td align="center">068</td>
      <td>Indicates the transaction is recurring</td>
      <td></td>
      <td align="center">Virtual &amp; Physical</td>
    </tr>

    <tr>
      <td align="center">Message Reason Code</td>
      <td align="center">069</td>
      <td>4-digit reason code (may be empty)</td>
      <td></td>
      <td align="center">All card types</td>
    </tr>

    <tr>
      <td align="center">Last Four Digits PAN</td>
      <td align="center">253</td>
      <td>Last four digits of the PAN</td>
      <td></td>
      <td align="center">Physical</td>
    </tr>

    <tr>
      <td align="center">MDES Digitized PAN</td>
      <td align="center">254</td>
      <td>PAN which was digitized</td>
      <td></td>
      <td align="center">Tokenization (MDES)</td>
    </tr>

    <tr>
      <td align="center">Digitization Event Type</td>
      <td align="center">923</td>
      <td>
        Deleted, Deleted_from_device, Stopped, Digitized,
        Digitization_Exception, Replacement
      </td>
      <td></td>
      <td align="center">Tokenization (MDES)</td>
    </tr>
  </tbody>
</table>