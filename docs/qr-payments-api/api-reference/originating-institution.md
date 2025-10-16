---
title: Originating Institution
deprecated: false
hidden: false
metadata:
  robots: index
---
<h2>Available Methods</h2>
<ul>
<li><a href ="https://developer.sprint.paymentology.com/qr-payments-api/api-reference/originating-institution/#TransferPaymentToMerchant">TransferPaymentToMerchant</a> – Transfer payment to merchant</li>
</ul>



\{/* unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"\} */}


<p><a id="TransferPaymentToMerchant"></p>
<h2>TransferPaymentToMerchant</h2>
<p></a><br />
Transfer payment to merchant.</p>



\{/* spacing: desktop=20, mobile=10 */\}


#### Path parameters

| Parameter | Type | Limits | Required | Description |
|---|---|---|:--:|---|
| terminalID | String | 10 characters | ✓ | <p>The Paymentology issued terminal ID of the terminal requesting the transaction</p> |
| recipientAccountNumber | String | 11-19 characters | ✓ | <p>Card Number of the recipient/merchant</p> |
| recipientFirstName | String | 1-40 characters | ✓ | <p>First name of the recipient/merchant</p> |
| recipientLastName | String | 1-40 characters | ✓ | <p>Last name of the recipient/merchant</p> |
| recipientCity | String | 1-25 characters | ✓ | <p>City of the recipient/merchant</p> |
| recipientCountry | String | 3 characters | ✓ | <p>ISO alpha country code of the recipient/merchant Ex. ZAF</p> |
| recipientCategoryCode | String | 1-4 characters | ✓ | <p>Mastercard defined merchant category code</p> |
| senderFirstName | String | 1-40 characters | ✓ | <p>First name of the sender</p> |
| senderLastName | String | 1-40 characters | ✓ | <p>Last name of the sender</p> |
| senderAddress | String | 1-100 characters | ✓ | <p>Address of the sender</p> |
| senderCity | String | 1-25 characters | ✓ | <p>City of the sender</p> |
| senderPostalCode | String | 4-5 characters | ✓ | <p>Postal code of the sender</p> |
| senderCountry | String | 3 characters | ✓ | <p>ISO alpha country code of the sender Ex. ZAF</p> |
| reference | String | 1-100 characters | ✓ | <p>The user defined reference to the card; for example a member id or wallet number</p> |
| requestAmount | Integer |  | ✓ | <p>The amount to be sent to the receiving subscriber</p> |
| transactionCurrency | String | 3 characters | ✓ | <p>Currency of the requestAmount Ex. ZAR</p> |
| transactionID | String | 1-40 characters | ✓ | <p>Client generated transaction ID to assist in identify transactions on the client side</p> |
| transactionDate | Date |  |  | <p>Client generated / local transaction date to assist in identifying transactions on the client side</p> |
| optionalData | String |  | ✓ | <p>Struct with optional fields, right now only “recipientPostalCode” field is accepted. See above for details. The maximum length of the recipientPostalCode is 10.</p> |
| checksum | String |  | ✓ | <p>The calculated HMAC-SHA1 signature of the call as specified in the rules of thumb</p> |



\{/* spacing: desktop=20, mobile=10 */\}



```xml
<methodCall>
    <methodName>TransferPaymentToMerchant</methodName>
    <params>
        <param>
            <value>
                <string>0039467951</string>
            </value>
        </param>
        <param>
            <value>
                <string>AFF44112</string>
            </value>
        </param>
        <param>
            <value>
                <string>John</string>
            </value>
        </param>
        <param>
            <value>
                <string>Doe</string>
            </value>
        </param>
        <param>
            <value>
                <string>Bangkok</string>
            </value>
        </param>
        <param>
            <value>
                <string>THA</string>
            </value>
        </param>
        <param>
            <value>
                <string>10261</string>
            </value>
        </param>
        <param>
            <value>
                <string>Jeremy</string>
            </value>
        </param>
        <param>
            <value>
                <string>Booster</string>
            </value>
        </param>
        <param>
            <value>
                <string>137 Zoho Rade 12</string>
            </value>
        </param>
        <param>
            <value>
                <string>Bangkok</string>
            </value>
        </param>
        <param>
            <value>
                <string>45687</string>
            </value>
        </param>
        <param>
            <value>
                <string>THA</string>
            </value>
        </param>
        <param>
            <value>
                <string>039200071850</string>
            </value>
        </param>
        <param>
            <value>
                <int>100</int>
            </value>
        </param>
        <param>
            <value>
                <string>THB</string>
            </value>
        </param>
        <param>
            <value>
                <string>txn1234567</string>
            </value>
        </param>
        <param>
            <value>
                <dateTime.iso8601>20100102T12:34:56+0700</dateTime.iso8601>
            </value>
        </param>
        <param>
            <value>
                <struct/>
            </value>
        </param>
        <param>
            <value>
                <string>FE0F831A3AEB4925B97F3037D9B4BDDF5C615C3B</string>
            </value>
        </param>
    </params>
</methodCall>

```,```xml
<methodResponse>
    <params>
        <param>
            <value>
                <struct>
                    <member>
                        <name>resultCode</name>
                        <value>
                            <double>1</double>
                        </value>
                    </member>
                    <member>
                        <name>resultText</name>
                        <value>
                            <string>Approved</string>
                        </value>
                    </member>
                </struct>
            </value>
        </param>
    </params>
</methodResponse>

```




{/* spacing: desktop=20, mobile=10 */}


#### Response schema

| Field | Type | Description |
|---|---|---|
| resultCode | Integer | <p>Status code indicating transaction result</p> |
| resultText | String | <p>Text indicating transaction result</p> |



{/* spacing: desktop=20, mobile=10 */}



```xml
<methodCall>
    <methodName>TransferPaymentToMerchant</methodName>
    <params>
        <param>
            <value>
                <string>0039467951</string>
            </value>
        </param>
        <param>
            <value>
                <string>AFF44112</string>
            </value>
        </param>
        <param>
            <value>
                <string>John</string>
            </value>
        </param>
        <param>
            <value>
                <string>Doe</string>
            </value>
        </param>
        <param>
            <value>
                <string>Bangkok</string>
            </value>
        </param>
        <param>
            <value>
                <string>THA</string>
            </value>
        </param>
        <param>
            <value>
                <string>10261</string>
            </value>
        </param>
        <param>
            <value>
                <string>Jeremy</string>
            </value>
        </param>
        <param>
            <value>
                <string>Booster</string>
            </value>
        </param>
        <param>
            <value>
                <string>137 Zoho Rade 12</string>
            </value>
        </param>
        <param>
            <value>
                <string>Bangkok</string>
            </value>
        </param>
        <param>
            <value>
                <string>45687</string>
            </value>
        </param>
        <param>
            <value>
                <string>THA</string>
            </value>
        </param>
        <param>
            <value>
                <string>039200071850</string>
            </value>
        </param>
        <param>
            <value>
                <int>100</int>
            </value>
        </param>
        <param>
            <value>
                <string>THB</string>
            </value>
        </param>
        <param>
            <value>
                <string>txn1234567</string>
            </value>
        </param>
        <param>
            <value>
                <dateTime.iso8601>20100102T12:34:56+0700</dateTime.iso8601>
            </value>
        </param>
        <param>
            <value>
                <struct/>
            </value>
        </param>
        <param>
            <value>
                <string>FE0F831A3AEB4925B97F3037D9B4BDDF5C615C3B</string>
            </value>
        </param>
    </params>
</methodCall>

```,```xml
<methodResponse>
    <params>
        <param>
            <value>
                <struct>
                    <member>
                        <name>resultCode</name>
                        <value>
                            <double>1</double>
                        </value>
                    </member>
                    <member>
                        <name>resultText</name>
                        <value>
                            <string>Approved</string>
                        </value>
                    </member>
                </struct>
            </value>
        </param>
    </params>
</methodResponse>

```




\{/* unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"\} */}


<p><a href="https://developer.sprint.paymentology.com/qr-payments-api/api-reference/appendix/#OI"></p>
<h3>Appendix</h3>
<p></a></p>
