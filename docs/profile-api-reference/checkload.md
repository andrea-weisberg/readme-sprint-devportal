---
title: CheckLoad
deprecated: false
hidden: false
metadata:
  robots: index
---
<!-- MIGRATION_METADATA
Migrated-From: https://developer.sprint.paymentology.com/profile-api-reference/checkload/
Source-Slug: checkload
Migrated-On: 2026-02-12T20:54:45+00:00
Migrated-By: wp-readme-migration
-->

Provides a method to check if the specified amount was loaded on a card.


#### Path parameters

| Parameter | type | Limits | required | Description |
| --- | --- | --- | --- | --- |
| terminalID | String | 10 characters | ✓ | The Paymentology issued terminal ID of the terminal requesting the transaction. |
| profileNumber | String | 1-20 characters | ✓ | Profile number linked with this card. |
| cardIdentifier | String | 1-20 characters | ✓ | The card number, sequence number or tracking number of the specified card. |
| requestAmount | Integer |  | ✓ | The requested amount to have been loaded to the card and decucted from the profile, in cents. |
| referenceID | String | 1-255 characters | ✓ | Transaction ID number refering to the load to check |
| referenceDate | Date |  | ✓ | Transaction date refering to the load to check. |
| checksum | String |  | ✓ | HMAC-SHA1 hashed signature of the concatenated method name with all argument values using the terminal password as private key |


```xml
<?xml version="1.0" encoding="UTF-8"?>
<methodCall>
  <methodName>CheckLoad</methodName>
  <params>
    <param>
      <value>
        <string>1234123412</string>
      </value>
    </param>
    <param>
      <value>
        <string>3444495478</string>
      </value>
    </param>
    <param>
      <value>
        <string>5333123</string>
      </value>
    </param>
    <param>
      <value>
        <i4>145000</i4>
      </value>
    </param>
    <param>
      <value>
        <string>3658-2589-1234-56782</string>
      </value>
    </param>
    <param>
      <value>
        <dateTime.iso8601>20230228T11:38:08</dateTime.iso8601>
      </value>
    </param>
    <param>
      <value>
        <string>B322EB366737A1BE95ABE1AF2703590070FD43B7</string>
      </value>
    </param>
  </params>
</methodCall>
```


#### Response schema

| Parameter | type | Description |
| --- | --- | --- |
| terminalID | String | Echo of incoming value. |
| profileNumber | String | Echo of incoming value. |
| cardNumber | String | Number of the card found using the cardIdentifier. |
| clientTransactionID | String | Echo of incoming value. |
| resultCode | Integer | Status code indicating transaction result. |
| resultText | String | Text indicating transaction result. |


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
              <string>3658-2589-1458-36582</string>
            </value>
          </member>
          <member>
            <name>resultCode</name>
            <value>
              <int>-11</int>
            </value>
          </member>
          <member>
            <name>terminalID</name>
            <value>
              <string>1234123412</string>
            </value>
          </member>
          <member>
            <name>profileNumber</name>
            <value>
              <string>3444495478</string>
            </value>
          </member>
          <member>
            <name>cardNumber</name>
            <value>
              <string>5456745676789563</string>
            </value>
          </member>
          <member>
            <name>resultText</name>
            <value>
              <string>Transaction could not be found</string>
            </value>
          </member>
        </struct>
      </value>
    </param>
  </params>
</methodResponse>
```
