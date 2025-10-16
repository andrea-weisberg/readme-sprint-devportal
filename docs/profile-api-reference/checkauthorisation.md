---
title: CheckAuthorisation
deprecated: false
hidden: false
metadata:
  robots: index
---
<p>Provides a method to check if the specified amount was deducted from a card.</p>

#### Path parameters

| Parameter | type | Limits | required | Description |
|---|---|---|:--:|---|
| terminalID | String | 10 characters | ✓ | <p>The Paymentology issued terminal id of the terminal requesting the transaction.</p> |
| profileNumber | String | 1-20 characters | ✓ | <p>Profile number linked with this card.</p> |
| cardIdentifier | String | 1-20 characters | ✓ | <p>The card number, sequence number or tracking number of the specified card.</p> |
| requestAmount | Integer |  | ✓ | <p>The requested amount to have been deducted from the card and loaded onto the profile, in cents.</p> |
| referenceID | String | 1-255 characters | ✓ | <p>Transaction id number refering to the Authorisation to check.</p> |
| referenceDate | Date |  | ✓ | <p>Transaction date refering to the Authorisation to check.</p> |
| checksum | String |  | ✓ | <p>HMAC-SHA1 hashed signature of the concatenated method name with all argument values using the terminal password as private key.</p> |

```xml
<?xml version="1.0" encoding="UTF-8"?>
<methodCall>
   <methodName>CheckAuthorisation</methodName>
   <params >
       <param >
           <value>
               <string>0020123425</string>
           </value>
       </param>
       <param >
           <value>
               <string>9012349072</string>
           </value>
       </param>
       <param >
           <value>
               <string>401234567800001</string>
           </value>
       </param>
       <param >
           <value>
               <int>20</int>
           </value>
       </param>
        <param >
           <value>
               <string>txn123456</string>
           </value>
       </param>
       <param >
           <value>
               <dateTime.iso8601>20240531T12:00:00</dateTime.iso8601>
           </value>
       </param>
       <param >
           <value>
               <string>42801707830541bd6789abcfcd4bc18ae272611ca73d881f484d83a1d1f80bb3</string>
           </value>
       </param>
   </params>
</methodCall>

```,```xml
<?xml version="1.0" encoding="UTF-8"?>
<methodResponse>
    <params >
        <param >
            <value>
                <struct>
                    <member>
                        <name>clientTransactionID</name>
                        <value>
                            <string>txn123456</string>
                        </value>
                    </member>
                    <member>
                        <name>resultCode</name>
                        <value>
                            <int>1</int>
                        </value>
                    </member>
                    <member>
                        <name>terminalID</name>
                        <value>
                            <string>0020123425</string>
                        </value>
                    </member>
                    <member>
                        <name>profileNumber</name>
                        <value>
                            <string>9012349072</string>
                        </value>
                    </member>
                    <member>
                        <name>cardNumber</name>
                        <value>
                            <string>4119876547004528</string>
                        </value>
                    </member>
                    <member>
                        <name>resultText</name>
                        <value>
                            <string>OK</string>
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

| Field | type | Description |
|---|---|---|
| terminalID | String | <p>Echo of the incoming value.</p> |
| profileNumber | String | <p>Echo of the incoming value.</p> |
| cardNumber | String | <p>Number of the card found using the cardIdentifier</p> |
| clientTransactionID | String | <p>Echo of the incoming value.</p> |
| resultCode | Integer | <p>Status code indicating the transaction result.</p> |
| resultText | String | <p>Text indicating the transaction result.</p> |

```xml
<?xml version="1.0" encoding="UTF-8"?>
<methodCall>
   <methodName>CheckAuthorisation</methodName>
   <params >
       <param >
           <value>
               <string>0020123425</string>
           </value>
       </param>
       <param >
           <value>
               <string>9012349072</string>
           </value>
       </param>
       <param >
           <value>
               <string>401234567800001</string>
           </value>
       </param>
       <param >
           <value>
               <int>20</int>
           </value>
       </param>
        <param >
           <value>
               <string>txn123456</string>
           </value>
       </param>
       <param >
           <value>
               <dateTime.iso8601>20240531T12:00:00</dateTime.iso8601>
           </value>
       </param>
       <param >
           <value>
               <string>42801707830541bd6789abcfcd4bc18ae272611ca73d881f484d83a1d1f80bb3</string>
           </value>
       </param>
   </params>
</methodCall>

```,```xml
<?xml version="1.0" encoding="UTF-8"?>
<methodResponse>
    <params >
        <param >
            <value>
                <struct>
                    <member>
                        <name>clientTransactionID</name>
                        <value>
                            <string>txn123456</string>
                        </value>
                    </member>
                    <member>
                        <name>resultCode</name>
                        <value>
                            <int>1</int>
                        </value>
                    </member>
                    <member>
                        <name>terminalID</name>
                        <value>
                            <string>0020123425</string>
                        </value>
                    </member>
                    <member>
                        <name>profileNumber</name>
                        <value>
                            <string>9012349072</string>
                        </value>
                    </member>
                    <member>
                        <name>cardNumber</name>
                        <value>
                            <string>4119876547004528</string>
                        </value>
                    </member>
                    <member>
                        <name>resultText</name>
                        <value>
                            <string>OK</string>
                        </value>
                    </member>
                </struct>
            </value>
        </param>
    </params>
</methodResponse>

```

</string></value></name></member></string></value></name></member></string></value></name></member></string></value></name></member></int></value></name></member></string></value></name></member></struct></value></params></methodresponse></string></value></value></string></value></int></value></string></value></string></value></string></value></params></methodname></methodcall></p></p></p></p></p></p></p></string></value></name></member></string></value></name></member></string></value></name></member></string></value></name></member></int></value></name></member></string></value></name></member></struct></value></params></methodresponse></string></value></value></string></value></int></value></string></value></string></value></string></value></params></methodname></methodcall></p></p></p></p></p></p></p></p>
