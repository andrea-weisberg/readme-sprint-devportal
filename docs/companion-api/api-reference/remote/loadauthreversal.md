---
title: LoadAuthReversal
deprecated: false
hidden: false
metadata:
  robots: index
---
<p>This method can only return the result codes of 1 (success) or -9 (an error occurred while queuing the Reversal).</p>
<p><strong>KLV will not be sent for reversals. Only reference data will be included if there is any. If KLV data is needed please lookup <a href="https://developer.sprint.paymentology.com/companion-api/klv-lookup/">KLV</a> from the reference data included.</strong></p>

#### Path parameters

| Parameter | Type | Limits | Required | Description |
|---|---|---|:--:|---|
| terminalID | String | 10 characters | ✓ | <p>The Paymentology issued terminal ID of the terminal requesting the transaction</p> |
| reference | String | 1-255 characters | ✓ | <p>The reference of the wallet to reverse a previous load</p> |
| requestAmount | Integer |  | ✓ | <p>The amount of the original load to be reversed</p> |
| narrative | String | 1-255 characters | ✓ | <p>A description of the terminal where the card was used</p> |
| transactionData | String | 0-2048 characters | ✓ | <p>Extra information about the transaction in a <a href="https://developer.sprint.paymentology.com/companion-api/klv-lookup/">KLV format</a></p> |
| referenceID | String | 1-255 characters | ✓ | <p>Transaction ID of the original load to be reversed</p> |
| referenceDate | Date |  | ✓ | <p>Transaction date of the original load to be reversed</p> |
| transactionID | String | 1-255 characters | ✓ | <p>Transaction ID to identify the reversal message.</p> <p><em>Note that the Transaction ID is not a unique value and may be duplicated over time.</em></p> |
| transactionDate | Date |  | ✓ | <p>Transaction date to identify the reversal message</p> |
| checksum | String |  | ✓ | <p>HMAC-SHA256 hashed signature of the concatenated method name with all argument values using the terminal password as private key</p> |

```xml
<?xml version="1.0"?>
<methodCall>
    <methodName>LoadAuthReversal</methodName>
    <params>
        <param>
            <value>
                <string>0014682067</string>
            </value>
        </param>
        <param>
            <value>
                <string>IMPLTest</string>
            </value>
        </param>
        <param>
            <value>
                <int>10000</int>
            </value>
        </param>
        <param>
            <value>
                <string>Tutuka Test            Pretoria      ZAF</string>
            </value>
        </param>
        <param>
            <value>
                <string></string>
            </value>
        </param>
        <param>
            <value>
                <string>192316</string>
            </value>
        </param>
        <param>
            <value>
                <dateTime.iso8601>20240313T11:20:00</dateTime.iso8601>
            </value>
        </param>
         <param>
            <value>
                <string>192325</string>
            </value>
        </param>
         <param>
            <value>
                <dateTime.iso8601>20240313T11:20:00</dateTime.iso8601>
            </value>
        </param>
        <param>
            <value>
                <string>47D4F5C6E263FA295D492A925DF607773D3F1B9B</string>
            </value>
        </param>
    </params>
</methodCall>

```,```xml
<?xml version="1.0" encoding="UTF-8"?>
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

#### Response schema

| Field | Type | Description |
|---|---|---|
| resultCode | Integer | <p>Status code indicating transaction result</p> |

```xml
<?xml version="1.0"?>
<methodCall>
    <methodName>LoadAuthReversal</methodName>
    <params>
        <param>
            <value>
                <string>0014682067</string>
            </value>
        </param>
        <param>
            <value>
                <string>IMPLTest</string>
            </value>
        </param>
        <param>
            <value>
                <int>10000</int>
            </value>
        </param>
        <param>
            <value>
                <string>Tutuka Test            Pretoria      ZAF</string>
            </value>
        </param>
        <param>
            <value>
                <string></string>
            </value>
        </param>
        <param>
            <value>
                <string>192316</string>
            </value>
        </param>
        <param>
            <value>
                <dateTime.iso8601>20240313T11:20:00</dateTime.iso8601>
            </value>
        </param>
         <param>
            <value>
                <string>192325</string>
            </value>
        </param>
         <param>
            <value>
                <dateTime.iso8601>20240313T11:20:00</dateTime.iso8601>
            </value>
        </param>
        <param>
            <value>
                <string>47D4F5C6E263FA295D492A925DF607773D3F1B9B</string>
            </value>
        </param>
    </params>
</methodCall>

```,```xml
<?xml version="1.0" encoding="UTF-8"?>
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

<p><a class="btn btn--primary" href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/">Back to Remote API menu</a></p>
</a></p></p></int></value></name></member></struct></value></params></methodresponse></string></value></value></string></value></value></string></value></string></value></string></value></int></value></string></value></string></value></params></methodname></methodcall></p></p></int></value></name></member></struct></value></params></methodresponse></string></value></value></string></value></value></string></value></string></value></string></value></int></value></string></value></string></value></params></methodname></methodcall></p></p></em></p></p></p></p></a></p></p></p></p></p></a></strong></p></p>
