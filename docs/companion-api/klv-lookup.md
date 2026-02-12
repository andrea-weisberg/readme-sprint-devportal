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

<br />

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
    <tr><td>Tracking Number</td><td align="center">002</td><td>Card tracking number</td><td /><td align="center">Virtual & Physical</td></tr>
    <tr><td>Original Transaction Amount</td><td align="center">004</td><td>Original amount of the incoming transaction</td><td /><td align="center">Virtual & Physical</td></tr>
    <tr><td>Conversion Rate</td><td align="center">010</td><td>Forex conversion rate at the time of the transaction. The same value received from the network is echoed in the companion call. The leftmost digit signifies the number of decimal places in the rate; the remaining 7 digits give the actual rate (e.g. 69972522 represents 9.972522).</td><td /><td align="center">Virtual & Physical</td></tr>
    <tr><td>Merchant category code</td><td align="center">026</td><td>The four digit MCC that defines the sort of merchant making the transaction</td><td /><td align="center">Virtual & Physical</td></tr>
    <tr><td>Acquiring Institution Code</td><td align="center">032</td><td>The code for the Acquiring Institution</td><td /><td align="center">Virtual & Physical</td></tr>
    <tr><td>Retrieval Reference Number</td><td align="center">037</td><td>The retrieval reference number of the transaction</td><td /><td align="center">Virtual & Physical</td></tr>
    <tr><td>Terminal ID</td><td align="center">041</td><td>The terminal ID where the transaction is done</td><td /><td align="center">Virtual & Physical</td></tr>
    <tr><td>Merchant Identifier</td><td align="center">042</td><td>The merchant identifier for the transaction</td><td /><td align="center">Virtual & Physical</td></tr>
    <tr><td>Merchant Description</td><td align="center">043</td><td>The merchant description for the data</td><td /><td align="center">Virtual & Physical</td></tr>
    <tr><td>Merchant name</td><td align="center">044</td><td>Merchant name provided as part of tokenization messages</td><td /><td align="center">Tokenization</td></tr>
    <tr><td>Transaction type Identifier</td><td align="center">045</td><td>Transaction type Identifier "TTI" used for funding</td><td /><td align="center">Virtual, physical and Money send</td></tr>
    <tr><td>Fraud scoring data</td><td align="center">048</td><td>Fraud score received in transaction message</td><td>Mastercard only</td><td align="center">Virtual & Physical</td></tr>
    <tr><td>Original Currency Code</td><td align="center">049</td><td>The original currency code of the transaction</td><td /><td align="center">Virtual & Physical</td></tr>

    <tr>
      <td>From Account</td>
      <td align="center">050</td>

      <td>
        Indicate cardholder account type:<br />
        00 = Default Account (Not specified or not applicable)<br />
        10 = Savings Account<br />
        20 = Checking Account<br />
        30 = Credit Card Account<br />
        Note: This type of multiple account card is currently specific to South American markets.
      </td>

      <td />

      <td align="center">Virtual & Physical</td>
    </tr>

    <tr><td>Pin Block</td><td align="center">052</td><td>A PIN block in 3DES ISO-1 format</td><td /><td align="center">Physical</td></tr>
    <tr><td>POS Data</td><td align="center">061</td><td>Data from the POS terminal used in the transaction</td><td /><td align="center">Physical</td></tr>
    <tr><td>TraceID</td><td align="center">063</td><td>Additional data received from Mastercard Network DE 48, Sub element 63</td><td /><td align="center">Virtual & Physical</td></tr>
    <tr><td>Extended payment code</td><td align="center">067</td><td>Code indicating extended payment transaction</td><td /><td align="center">Virtual & Physical</td></tr>
    <tr><td>Is recurring</td><td align="center">068</td><td>Indicates that a transaction is recurring</td><td /><td align="center">Virtual & Physical</td></tr>
    <tr><td>message reason code</td><td align="center">069</td><td>4 digit</td><td>can be empty</td><td align="center">All card types and transactions</td></tr>
    <tr><td>Markup Amount</td><td align="center">085</td><td>The markup amount applied to the transaction</td><td /><td align="center">Virtual & Physical</td></tr>

    <tr><td>Recipient Name</td><td align="center">108</td><td>Name of the recipient of the funds in the transaction</td><td /><td align="center">Moneysend</td></tr>
    <tr><td>Recipient address</td><td align="center">109</td><td>Street address of the person who receives the funds in the transaction</td><td /><td align="center">Moneysend</td></tr>
    <tr><td>Recipient account number</td><td align="center">110</td><td>The account number of the person who receives the funds</td><td /><td align="center">Moneysend</td></tr>
    <tr><td>Recipient account number type</td><td align="center">111</td><td>The account type of the person who receives the funds</td><td /><td align="center">Moneysend</td></tr>

    <tr>
      <td>Capture Mode</td>
      <td align="center">250</td>

      <td>
        \*\*\*Note: We are in a transition period to implement a new behavior of this KLV index. KLV 250 will be used in conjunction with KLV 262 to show capture mode and transaction type.<br />
        Details can be found at [https://developer.sprint.paymentology.com/get-started/whats-new/](https://developer.sprint.paymentology.com/get-started/whats-new/)<br /><br />
        MAG - Magstripe<br />
        MAN - Manual (Terminal)<br />
        EMV - EMV<br />
        OB - On Behalf (EMV)<br />
        NFC - NFC (EMV)<br />
        ECOM - Ecommerce<br />
        3DS - 3D-Secure (Ecommerce)<br />
        ADJ - Adjustment
      </td>

      <td />

      <td align="center">Virtual & Physical</td>
    </tr>

    <tr>
      <td>Network</td>
      <td align="center">251</td>

      <td>
        Local<br />
        Mastercard<br />
        VISA<br />
        CUP<br />
        Unknown<br />
        Adjustment
      </td>

      <td />

      <td align="center">Virtual & Physical</td>
    </tr>

    <tr>
      <td>Fee Type</td>
      <td align="center">252</td>

      <td>
        0 - No fee<br />
        31 - Insufficient Funds<br />
        32 - Withdrawal Limit Exceeded<br />
        33 - Security Violation<br />
        34 - Transaction Not Supported<br />
        35 - PIN Tries Exceeded<br />
        36 - Invalid PIN<br />
        37 - PIN Length Error<br />
        38 - Expired Card
      </td>

      <td />

      <td align="center">Virtual & Physical</td>
    </tr>

    <tr><td>Last four digits PAN</td><td align="center">253</td><td>The account number's last four digits of the card being swiped.</td><td /><td align="center">Physical</td></tr>
    <tr><td>MDES Digitized PAN</td><td align="center">254</td><td>The PAN which was digitized</td><td /><td align="center">Tokenization - MDES</td></tr>

    <tr>
      <td>MDES Digitized Wallet ID</td>
      <td align="center">255</td>

      <td>
        The Wallet ID (Wallet Reference) used to digitize the card.<br />
        327 - M4M<br />
        216 - Google Pay<br />
        217 - Samsung Pay<br />
        103 - Apple Pay
      </td>

      <td />

      <td align="center">Tokenization - MDES</td>
    </tr>

    <tr>
      <td>Adjustment Reason</td>
      <td align="center">256</td>

      <td>
        99 - Generic reason<br />
        00 - MasterCard initiated<br />
        01 - Forex conversion difference<br />
        02 - Settlement without authorization<br />
        03 - Reversal timeout/ not accepted<br />
        04 - Refund<br />
        05 - Chargeback<br />
        06 - MoneySend<br />
        07 - Purchase Cancellation - ONLY applicable to Union Pay<br />
        08 - Purchase Cancellation Reversal - ONLY applicable to Union Pay<br />
        09 - Stand-in<br />
        10 - Mass Transit Debt Collection<br />
        11 - Final settlement - Unused funds<br />
        26 - OCT (Visa only)
      </td>

      <td />

      <td align="center">Virtual, Physical and Moneysend</td>
    </tr>

    <tr><td>Reference ID</td><td align="center">257</td><td>Transaction ID of the original Deduct if any</td><td /><td align="center">Virtual & Physical</td></tr>

    <tr>
      <td>Markup Type</td>
      <td align="center">258</td>

      <td>
        0 - No markup<br />
        1 - Regular markup<br />
        2 - DCC markup
      </td>

      <td />

      <td align="center">Virtual & Physical</td>
    </tr>

    <tr><td>Acquirer Country</td><td align="center">259</td><td>Country of the acquirer of a transaction</td><td /><td align="center">Virtual & Physical</td></tr>
    <tr><td>Mobile number</td><td align="center">260</td><td>Data containing the mobile number entered</td><td /><td align="center">Virtual & Physical</td></tr>
    <tr><td>Transaction Fee Amount</td><td align="center">261</td><td>Fee amount applicable to the incoming transaction if any</td><td>Always sent in the 'Deduct' call</td><td align="center">Virtual & Physical</td></tr>

    <tr>
      <td>Transaction subtype</td>
      <td align="center">262</td>

      <td>
        \*\*\*Note: We are in a transition period to implement a new behavior of this KLV index. KLV 250 will be used in conjunction with KLV 262 to show capture mode and transaction type.<br />
        Details can be found at [https://developer.sprint.paymentology.com/get-started/whats-new/](https://developer.sprint.paymentology.com/get-started/whats-new/)<br />
        Identifies a transaction as MDES or 3DS.<br />
        NB. This field will be empty if the transaction is neither MDES nor 3DS.
      </td>

      <td />

      <td align="center">MDES - 3DS</td>
    </tr>

    <tr><td>Card Issuer Data</td><td align="center">263</td><td>Information about the card issuer</td><td>Colombia only</td><td align="center">Virtual & Physical</td></tr>
    <tr><td>Tax</td><td align="center">264</td><td>Amount of tax charged on transaction</td><td>Colombia only</td><td align="center">Virtual & Physical</td></tr>
    <tr><td>Tax amount base</td><td align="center">265</td><td>Value of the tax base amount used</td><td>Colombia only</td><td align="center">Virtual & Physical</td></tr>
    <tr><td>Retailer data</td><td align="center">266</td><td>Information about the retailer where transaction took place</td><td>Colombia only</td><td align="center">Virtual & Physical</td></tr>
    <tr><td>IAC Tax amount</td><td align="center">267</td><td>Rate levied by IAC</td><td>Colombia only</td><td align="center">Virtual & Physical</td></tr>
    <tr><td>Number of Installments</td><td align="center">268</td><td>Number of installments to pay for the transaction</td><td /><td align="center">Virtual & Physical</td></tr>
    <tr><td>Customer ID</td><td align="center">269</td><td>ID value that identifies the customer</td><td>Colombia only</td><td align="center">Virtual & Physical</td></tr>
    <tr><td>Security Services Data</td><td align="center">270</td><td>Authentication risk analysis reason codes (ARA)</td><td>Mastercard only</td><td align="center">Virtual & Physical</td></tr>
    <tr><td>On behalf of services</td><td align="center">271</td><td>Indicates this is a 'on behalf of' transaction</td><td /><td align="center">Virtual & Physical</td></tr>
    <tr><td>Original Merchant Description</td><td align="center">272</td><td>The original description received from the merchant</td><td /><td align="center">Virtual & Physical</td></tr>
    <tr><td>Installments financing type</td><td align="center">273</td><td>Type of financing selected to pay installments</td><td>Brazil only</td><td align="center">Virtual & Physical</td></tr>

    <tr>
      <td>Status</td>
      <td align="center">274</td>

      <td>
        Associated with 3D Secure Out of Band authentication, providing additional status information in the Administrative Message 3DSecureAppFinalisation.<br />
        Possible values:<br />
        0 - Successfully received final status<br />
        1 - Timer on browser expired before response was received<br />
        2 - General error<br />
        3 - Transaction cancelled before response was received
      </td>

      <td />

      <td align="center">Virtual & Physical</td>
    </tr>

    <tr><td>Installments grace period</td><td align="center">275</td><td>Duration of the grace period for payment of the installment</td><td>Mexico only</td><td align="center">Virtual & Physical</td></tr>
    <tr><td>Installments type of credit</td><td align="center">276</td><td>Type of credit used for the installment transaction</td><td>Mexico only</td><td align="center">Virtual & Physical</td></tr>
    <tr><td>Payments Initiator</td><td align="center">277</td><td>Represents who triggered the transaction. Values: "merchant", "cardholder", or empty/unknown.</td><td>Mastercard only</td><td align="center">Virtual & Physical</td></tr>

    <tr>
      <td>Payment Initiator Subtype</td>
      <td align="center">278</td>

      <td>
        Potential values (when available):<br />
        Unscheduled Credential on File<br />
        Standing Order<br />
        Subscription<br />
        Installment<br />
        Partial Shipment<br />
        Related/Delayed Charge<br />
        No Show Charge<br />
        Resubmission<br />
        Credential-on-file
      </td>

      <td>Mastercard only</td>
      <td align="center">Virtual & Physical</td>
    </tr>

    <tr><td>Additional amount</td><td align="center">300</td><td>Cashbacks come as an "additional amount"</td><td>Columbia only</td><td align="center" /></tr>
    <tr><td>Second additional amount</td><td align="center">301</td><td>Maximum of two cashback amounts can come through in a transaction</td><td /><td align="center">Virtual & Physical</td></tr>
    <tr><td>cashback POS currency code</td><td align="center">302</td><td>Currency code of the cashback amount</td><td /><td align="center">Physical</td></tr>
    <tr><td>cashback POS amount</td><td align="center">303</td><td>Actual cashback amount</td><td /><td align="center">Physical</td></tr>

    <tr><td>Sender name</td><td align="center">400</td><td>Name of the sender</td><td /><td align="center">Visa Direct & Money send</td></tr>
    <tr><td>Sender Address</td><td align="center">401</td><td>Street address of the person who sent the funds</td><td /><td align="center">Visa Direct & Money send</td></tr>
    <tr><td>Sender city</td><td align="center">402</td><td>City of the person who sent the funds</td><td>Visa Direct only</td><td align="center">Visa Direct only</td></tr>
    <tr><td>Sender state</td><td align="center">403</td><td>State of the person who sent the funds</td><td>Visa Direct only</td><td align="center">Visa Direct only</td></tr>
    <tr><td>Sender country</td><td align="center">404</td><td>Country of the person who sent the funds</td><td>Visa Direct only</td><td align="center">Visa Direct only</td></tr>
    <tr><td>Sanction screening score</td><td align="center">405</td><td>Score achieved during sanction screening</td><td /><td align="center">Visa Direct and Moneysend</td></tr>
    <tr><td>Business application identifier</td><td align="center">406</td><td>Code that identifies intended use of a push payment</td><td>Visa Direct only</td><td align="center">Visa Direct only</td></tr>
    <tr><td>Special condition indicator</td><td align="center">408</td><td>Any special conditions for the transaction</td><td>Visa Direct only</td><td align="center">Visa Direct only</td></tr>
    <tr><td>Business tax ID</td><td align="center">409</td><td>Business tax ID number</td><td>Visa Direct only</td><td align="center">Visa Direct only</td></tr>
    <tr><td>Individual tax ID</td><td align="center">410</td><td>Customer/individual tax ID number</td><td>Visa Direct only</td><td align="center">Visa Direct only</td></tr>
    <tr><td>Source of funds</td><td align="center">411</td><td>Where the funds come from</td><td /><td align="center">Visa Direct & Money send</td></tr>
    <tr><td>Sender account number</td><td align="center">412</td><td>Account number of the person who sent/paid the funds</td><td /><td align="center">Visa Direct & Money send</td></tr>
    <tr><td>Sender Account Number Type</td><td align="center">413</td><td>Account type of the person who sent/paid the funds</td><td /><td align="center">Visa Direct & Money send</td></tr>
    <tr><td>MVV</td><td align="center">414</td><td>Merchant Verification Value – identifies merchants participating in programs</td><td>Visa Direct only</td><td align="center">Visa Direct only</td></tr>
    <tr><td>Sender reference number</td><td align="center">415</td><td>Sender reference number</td><td>(Visa Direct only)</td><td align="center">Visa Direct only</td></tr>
    <tr><td>is afd transaction</td><td align="center">416</td><td>AFD Transaction indicator for MCC 5542. 1: AFD TXN, 0: NOT AFD</td><td /><td align="center">Virtual & Physical (AFD only)</td></tr>
    <tr><td>acquirer fee amount</td><td align="center">417</td><td>Acquirer fee amount in transaction currency</td><td /><td align="center">Virtual & Physical</td></tr>

    <tr>
      <td>Address Verification Result</td>
      <td align="center">418</td>

      <td>
        0 - postal/zip code and address matches<br />
        1 - postal/zip code matches, address does not<br />
        2 - address matches, postal/zip code does not match<br />
        3 - neither address nor postal/zip code match
      </td>

      <td />

      <td align="center">Virtual & Physical</td>
    </tr>

    <tr><td>Postal code / ZIP code</td><td align="center">419</td><td>Cardholder postal/ZIP code</td><td /><td align="center">Virtual & Physical</td></tr>
    <tr><td>Street address</td><td align="center">420</td><td>Cardholder street address only (without city/area)</td><td /><td align="center">Virtual & Physical</td></tr>
    <tr><td>Sender Date of Birth</td><td align="center">421</td><td>Date of Birth of the sender</td><td>Visa Direct only</td><td align="center">Visa Direct only</td></tr>

    <tr>
      <td>OCT Activity check result</td>
      <td align="center">422</td>

      <td>
        Activity check result of Original Credit Transaction (OCT):<br />
        1 = 1-day count or amount exceeded<br />
        2 = 7-day count or amount exceeded<br />
        3 = 30-day count or amount exceeded
      </td>

      <td>Visa Direct only</td>
      <td align="center">Visa Direct only</td>
    </tr>

    <tr><td>Sender postal code</td><td align="center">423</td><td>Sender postal code</td><td>Visa Direct only</td><td align="center">Visa Direct only</td></tr>
    <tr><td>Recipient city</td><td align="center">424</td><td>Recipient city</td><td>Visa Direct only</td><td align="center">Visa Direct only</td></tr>
    <tr><td>Recipient country</td><td align="center">425</td><td>Recipient country</td><td>Visa Direct only</td><td align="center">Visa Direct only</td></tr>

    <tr><td>3D Secure OTP</td><td align="center">900</td><td>Dynamic One Time Password for 3D Secure</td><td /><td align="center">3DS</td></tr>
    <tr><td>Digitization activation</td><td align="center">901</td><td>Password needed to activate an MDES digitization request</td><td /><td align="center">Tokenization</td></tr>
    <tr><td>Digitization activation method type</td><td align="center">902</td><td>Method used to send OTP to activate a token</td><td /><td align="center">Tokenization</td></tr>
    <tr><td>Digitization activation method value</td><td align="center">903</td><td>Code/numerical value indicating OTP delivery method</td><td /><td align="center">Tokenization</td></tr>
    <tr><td>Digitization activation expiry</td><td align="center">904</td><td>Expiry of the activation</td><td /><td align="center">Tokenization</td></tr>

    <tr>
      <td>Digitization final tokenization decision</td>
      <td align="center">905</td>

      <td>
        1 = approve<br />
        2 = approve but with additional authentication
      </td>

      <td />

      <td align="center">Tokenization</td>
    </tr>

    <tr><td>Device name</td><td align="center">906</td><td>Up to 20 characters. Device name associated with the wallet provider</td><td /><td align="center">Tokenization</td></tr>
    <tr><td>Digitized Device ID</td><td align="center">910</td><td>ID of the type of device used for tokenization</td><td /><td align="center">Tokenization</td></tr>
    <tr><td>Digitized PAN expiry</td><td align="center">911</td><td>Expiry date of the DPAN</td><td /><td align="center">Tokenization</td></tr>
    <tr><td>Digitized FPAN Masked</td><td align="center">912</td><td>The masked FPAN</td><td /><td align="center" /></tr>
    <tr><td>Token Unique Reference</td><td align="center">913</td><td>Token reference during the process</td><td /><td align="center">Tokenization</td></tr>
    <tr><td>Digitized Token Requestor ID</td><td align="center">915</td><td>Token Requestor ID during the process</td><td /><td align="center">Tokenization</td></tr>
    <tr><td>Visa Digitized PAN</td><td align="center">916</td><td>Digitized PAN for Visa</td><td>Visa only</td><td align="center">Tokenization - VTS</td></tr>
    <tr><td>Visa token type</td><td align="center">917</td><td>Data indicating the type of token</td><td>Visa only</td><td align="center">Tokenization - VTS</td></tr>

    <tr>
      <td>POS Transaction Status</td>
      <td align="center">920</td>

      <td>
        Point-of-Service Data about the transaction status:<br />
        0 = Standard request<br />
        1 = Deferred authorization<br />
        4 = Pre-authorization request
      </td>

      <td />

      <td align="center">Physical</td>
    </tr>

    <tr><td>POS Transaction Security</td><td align="center">921</td><td>Point-of-Service Data about the security</td><td /><td align="center">Physical</td></tr>
    <tr><td>POS Authorisation Lifecycle</td><td align="center">922</td><td>Point-of-Service Data about the Authorisation Lifecycle</td><td /><td align="center">Physical</td></tr>

    <tr>
      <td>Digitization event type</td>
      <td align="center">923</td>

      <td>
        Event types include:<br />
        Deleted<br />
        Deleted\_from\_device<br />
        Stopped<br />
        Digitized<br />
        Digitization\_Exception<br />
        Replacement
      </td>

      <td />

      <td align="center">Tokenization</td>
    </tr>

    <tr><td>Digitization event reason code</td><td align="center">924</td><td>Code relating to a Digitization Exception event type</td><td /><td align="center">Tokenization</td></tr>
    <tr><td>Supports partial auth</td><td align="center">925</td><td>Indicates a transaction supports partial authorisation</td><td /><td align="center">Virtual and Physical</td></tr>

    <tr>
      <td>Digitization path</td>
      <td align="center">929</td>

      <td>
        GREEN<br />
        YELLOW<br />
        ORANGE<br />
        RED
      </td>

      <td />

      <td align="center">Tokenization</td>
    </tr>

    <tr>
      <td>Wallet recommendation</td>
      <td align="center">930</td>

      <td>
        Decline<br />
        Approve<br />
        Require\_additional\_authentication
      </td>

      <td />

      <td align="center">Tokenization</td>
    </tr>

    <tr>
      <td>Tokenization pan source</td>
      <td align="center">931</td>

      <td>
        card\_on\_file<br />
        card\_added\_manually<br />
        card\_added\_via\_application<br />
        existing\_token\_credential<br />
        card\_added\_via\_browser
      </td>

      <td />

      <td align="center">Tokenization</td>
    </tr>

    <tr><td>Unique Transaction Reference</td><td align="center">932</td><td>Unique Transaction Reference number for Mastercard MoneySend payment</td><td /><td align="center">Moneysend</td></tr>
    <tr><td>Transaction purpose</td><td align="center">933</td><td>Transaction purpose details</td><td /><td align="center">Moneysend</td></tr>
    <tr><td>3D Secure OTP RefCode</td><td align="center">934</td><td>Dynamic 4 letters reference code to be used along with 3DS OTP messages</td><td>BankServ only</td><td align="center">3DS</td></tr>

    <tr><td>Generic Key</td><td align="center">999</td><td>Reserved for other uses</td><td /><td align="center" /></tr>
  </tbody>
</table>

***

## Stop Reason ID Codes

<br />

<table>
  <thead>
    <tr>
      <th align="center">Reason ID</th>
      <th align="center">Internal Code</th>
      <th align="center">Network response (Mastercard)</th>
      <th align="center">Network response (Visa)</th>
      <th align="center">Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td align="center">1</td>
      <td align="center">2008</td>
      <td align="center">41</td>
      <td align="center">41</td>
      <td align="center">Lost Card</td>
    </tr>

    <tr>
      <td align="center">2</td>
      <td align="center">2009</td>
      <td align="center">43</td>
      <td align="center">43</td>
      <td align="center">Stolen Card</td>
    </tr>

    <tr>
      <td align="center">3</td>
      <td align="center">1004</td>
      <td align="center">62</td>
      <td align="center">62</td>
      <td align="center">Do not honor</td>
    </tr>

    <tr>
      <td align="center">4</td>
      <td align="center">1016</td>
      <td align="center">51</td>
      <td align="center">51</td>
      <td align="center">Insufficient funds</td>
    </tr>

    <tr>
      <td align="center">5</td>
      <td align="center">1018</td>
      <td align="center">14</td>
      <td align="center">14</td>
      <td align="center">Invalid card number</td>
    </tr>

    <tr>
      <td align="center">6</td>
      <td align="center">1006</td>
      <td align="center">75</td>
      <td align="center">75</td>
      <td align="center">PIN tries exceeded</td>
    </tr>

    <tr>
      <td align="center">7</td>
      <td align="center">1002</td>
      <td align="center">05</td>
      <td align="center">59</td>
      <td align="center">Do not honor</td>
    </tr>

    <tr>
      <td align="center">Other</td>
      <td align="center">1000</td>
      <td align="center">05</td>
      <td align="center">05</td>
      <td align="center">Do not honor</td>
    </tr>
  </tbody>
</table>
