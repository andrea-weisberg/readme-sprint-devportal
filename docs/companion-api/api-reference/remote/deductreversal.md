---
title: DeductReversal
deprecated: false
hidden: false
metadata:
  robots: index
original_path: companion-api/api-reference/remote
---
<p>Reverse a deduct that was previously requested on a wallet.</p>
<p><strong>KLV will not be sent for reversals. </strong></p>



\{/* spacing: desktop=20, mobile=10 */\}


#### Path parameters

| Parameter | Type | Limits | Required | Description |
|---|---|---|:--:|---|
| terminalID | String | 10 characters | ✓ | <p>The Paymentology issued terminal ID of the terminal requesting the transaction</p> |
| reference | String | 1-255 characters | ✓ | <p>The reference of the wallet to reverse a previous deduct</p> |
| requestAmount | Integer |  | ✓ | <p>The amount of the original deduct to be reversed</p> |
| narrative | String | 1-255 characters | ✓ | <p>A description of the terminal where the card was used</p> |
| transactionData | String | 0-2048 characters | ✓ | <p>Extra information about the transaction in a <a href="https://developer.sprint.paymentology.com/companion-api/klv-lookup/">KLV format</a></p> |
| referenceID | String | 1-255 characters | ✓ | <p>Transaction ID of the original deduct to be reversed</p> |
| referenceDate | Date |  | ✓ | <p>Transaction date (in UTC) of the original deduct to be reversed</p> |
| transactionID | String | 1-255 characters | ✓ | <p>Transaction ID to identify the reversal message. Note that the Transaction ID is not a unique value and may be duplicated over time</p> |
| transactionDate | Date |  | ✓ | <p>Transaction date (in UTC) to identify the reversal message</p> |
| checksum | String |  | ✓ | <p>HMAC-SHA256 hashed signature of the concatenated method name with all argument values using the terminal password as private key</p> |



\{/* spacing: desktop=20, mobile=10 */\}



```xml
<?xml version="1.0"?>
<methodCall>
    <methodName>DeductReversal</methodName>
    <params>
        <param>
            <value>
                <string>0034048207</string>
            </value>
        </param>
        <param>
            <value>
                <string>68263116</string>
            </value>
        </param>
        <param>
            <value>
                <int>559</int>
            </value>
        </param>
        <param>
            <value>
                <string>PAYPAL                 4029357733    SGP</string>
            </value>
        </param>
        <param>
            <value>
                <string>
                </string>
            </value>
        </param>
        <param>
            <value>
                <string>571156</string>
            </value>
        </param>
        <param>
            <value>
                <dateTime.iso8601>20200824T01:52:15</dateTime.iso8601>
            </value>
        </param>
        <param>
            <value>
                <string>2010206</string>
            </value>
        </param>
        <param>
            <value>
                <dateTime.iso8601>20200824T03:52:22</dateTime.iso8601>
            </value>
        </param>
        <param>
            <value>
                <string>D86B50F9FB658F5AB00A280BF52A40DAD7A3B89919D98ADABBC93FD42D5AF9E8</string>
            </value>
        </param>
    </params>
</methodCall>

```,```xml
<?xml version=""1.0"" encoding=""UTF-8""?>
<methodResponse>
   <params>
      <param>
         <value>
            <struct>
               <member>
                  <name>resultCode</name>
                  <value>
                     <int>1</int>
                  </value>
               </member>
            </struct>
         </value>
      </param>
   </params>
</methodResponse>

```

<p> </p>



{/* spacing: desktop=20, mobile=10 */}


#### Response schema

| Field | Type | Description |
|---|---|---|
| resultCode | Integer | <p>Status code indicating transaction result</p> |



{/* spacing: desktop=20, mobile=10 */}



```xml
<?xml version="1.0"?>
<methodCall>
    <methodName>DeductReversal</methodName>
    <params>
        <param>
            <value>
                <string>0034048207</string>
            </value>
        </param>
        <param>
            <value>
                <string>68263116</string>
            </value>
        </param>
        <param>
            <value>
                <int>559</int>
            </value>
        </param>
        <param>
            <value>
                <string>PAYPAL                 4029357733    SGP</string>
            </value>
        </param>
        <param>
            <value>
                <string>
                </string>
            </value>
        </param>
        <param>
            <value>
                <string>571156</string>
            </value>
        </param>
        <param>
            <value>
                <dateTime.iso8601>20200824T01:52:15</dateTime.iso8601>
            </value>
        </param>
        <param>
            <value>
                <string>2010206</string>
            </value>
        </param>
        <param>
            <value>
                <dateTime.iso8601>20200824T03:52:22</dateTime.iso8601>
            </value>
        </param>
        <param>
            <value>
                <string>D86B50F9FB658F5AB00A280BF52A40DAD7A3B89919D98ADABBC93FD42D5AF9E8</string>
            </value>
        </param>
    </params>
</methodCall>

```,```xml
<?xml version=""1.0"" encoding=""UTF-8""?>
<methodResponse>
   <params>
      <param>
         <value>
            <struct>
               <member>
                  <name>resultCode</name>
                  <value>
                     <int>1</int>
                  </value>
               </member>
            </struct>
         </value>
      </param>
   </params>
</methodResponse>

```

<p> </p>



\{/* spacing: desktop=20, mobile=10 */\}


<p><a class="btn btn--primary" href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/">Back to Remote API menu</a></p>
