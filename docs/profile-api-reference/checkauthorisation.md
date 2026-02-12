---
title: CheckAuthorisation
deprecated: false
hidden: false
metadata:
  robots: index
---
<!-- MIGRATION_METADATA
Migrated-From: https://developer.sprint.paymentology.com/profile-api-reference/checkauthorisation/
Source-Slug: checkauthorisation
Migrated-On: 2026-02-12T20:43:48+00:00
Migrated-By: wp-readme-migration
-->

Provides a method to check if the specified amount was deducted from a card.


#### Path parameters

| Parameter | type | Limits | required | Description |
| --- | --- | --- | --- | --- |
| terminalID | String | 10 characters | ✓ | The Paymentology issued terminal ID of the terminal requesting the transaction. |
| profileNumber | String | 1-20 characters | ✓ | Profile number linked with this card. |
| cardIdentifier | String | 1-20 characters | ✓ | The card number, sequence number or tracking number of the specified card. |
| requestAmount | Integer |  | ✓ | The requested amount to have been deducted from the card and loaded onto the profile, in cents. |
| referenceID | String | 1-255 characters | ✓ | Transaction ID number refering to the Authorisation to check. |
| referenceDate | Date |  | ✓ | Transaction date refering to the Authorisation to check. |
| checksum | String |  | ✓ | HMAC-SHA1 hashed signature of the concatenated method name with all argument values using the terminal password as private key. |


```xml
<?xml version="1.0" encoding="UTF-8"?>
<methodCall>
   <methodName>CheckAuthorisation</methodName>
   <params>
       <param>
           <value>
               <string>0020123425</string>
           </value>
       </param>
       <param>
           <value>
               <string>9012349072</string>
           </value>
       </param>
       <param>
           <value>
               <string>401234567800001</string>
           </value>
       </param>
       <param>
           <value>
               <int>20</int>
           </value>
       </param>
        <param>
           <value>
               <string>txn123456</string>
           </value>
       </param>
       <param>
           <value>
               <dateTime.iso8601>20240531T12:00:00</dateTime.iso8601>
           </value>
       </param>
       <param>
           <value>
               <string>42801707830541bd6789abcfcd4bc18ae272611ca73d881f484d83a1d1f80bb3</string>
           </value>
       </param>
   </params>
</methodCall>
```


#### Response schema

| Parameter | type | Description |
| --- | --- | --- |
| terminalID | String | Echo of the incoming value. |
| profileNumber | String | Echo of the incoming value. |
| cardNumber | String | Number of the card found using the cardIdentifier |
| clientTransactionID | String | Echo of the incoming value. |
| resultCode | Integer | Status code indicating the transaction result. |
| resultText | String | Text indicating the transaction result. |


```xml
<?xml version="1.0" encoding="UTF-8"?>
<methodResponse>
    <params>
        <param>
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
