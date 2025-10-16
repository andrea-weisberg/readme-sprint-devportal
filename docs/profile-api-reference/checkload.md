---
title: CheckLoad
deprecated: false
hidden: false
metadata:
  robots: index
original_path: profile-api-reference
---
<p>Provides a method to check if the specified amount was loaded on a card.</p>



<!-- spacing: desktop=20, mobile=10 -->


#### Path parameters

| Parameter | Type | Limits | Required | Description |
|---|---|---|:--:|---|
| terminalID | String | 10 characters | ✓ | <p>The Paymentology issued terminal ID of the terminal requesting the transaction.</p> |
| profileNumber | String | 1-20 characters | ✓ | <p>Profile number linked with this card.</p> |
| cardIdentifier | String | 1-20 characters | ✓ | <p>The card number, sequence number or tracking number of the specified card.</p> |
| requestAmount | Integer |  | ✓ | <p>The requested amount to have been loaded to the card and decucted from the profile, in cents.</p> |
| referenceID | String | 1-255 characters | ✓ | <p>Transaction ID number refering to the load to check</p> |
| referenceDate | Date |  | ✓ | <p>Transaction date refering to the load to check.</p> |
| checksum | String |  | ✓ | <p>HMAC-SHA1 hashed signature of the concatenated method name with all argument values using the terminal password as private key</p> |



<!-- spacing: desktop=20, mobile=10 -->



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

<p>&nbsp;</p>



<!-- spacing: desktop=20, mobile=10 -->


#### Response schema

| Field | Type | Description |
|---|---|---|
| terminalID | String | <p>Echo of incoming value.</p> |
| profileNumber | String | <p>Echo of incoming value.</p> |
| cardNumber | String | <p>Number of the card found using the cardIdentifier.</p> |
| clientTransactionID | String | <p>Echo of incoming value.</p> |
| resultCode | Integer | <p>Status code indicating transaction result.</p> |
| resultText | String | <p>Text indicating transaction result.</p> |



<!-- spacing: desktop=20, mobile=10 -->



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

<p>&nbsp;</p>



<!-- spacing: desktop=20, mobile=10 -->
