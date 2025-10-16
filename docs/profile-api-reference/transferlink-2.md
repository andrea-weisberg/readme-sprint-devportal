---
title: TransferLink
deprecated: false
hidden: false
metadata:
  robots: index
---
<p>Transfer a reference to a new card. The old card will be stopped and the bearer details transferred to the new card. The new card will be linked and activated.</p>
<p><strong>NOTE:</strong> Applicable to our Visa product.</p>



\{/* spacing: desktop=20, mobile=10 */\}


#### Path parameters

| Parameter | Type | Limits | Required | Description |
|---|---|---|:--:|---|
| terminalID | String | 10 characters | ✓ | <p>The Paymentology issued terminal ID of the terminal requesting the transaction.</p> |
| reference | String | 1-255 characters | ✓ | <p>The user defined reference to the card; for example a member id or wallet number.</p> |
| oldCardIdentifier | String | 1-20 characters | ✓ | <p>The card number, sequence number or tracking number of the card being transferred FROM.</p> |
| newCardIdentifier | String | 1-20 characters | ✓ | <p>The card number, sequence number or tracking number of the card being transferred TO. This parameter can’t be empty for this call.</p> |
| transactionID | String | 1-255 characters | ✓ | <p>Client generated Transaction ID to assist in identify transactions on the client side.</p> |
| transactionDate | Date |  | ✓ | <p>Client generated / local Transaction Date to assist in identifying transactions on the client side.</p> |
| checksum | String |  | ✓ | <p>HMAC-SHA256 hashed signature of the concatenated method name with all argument values using the terminal password as private key.</p> |



\{/* spacing: desktop=20, mobile=10 */\}



```xml
<?xml version=""1.0""?>
<methodCall>
  <methodName>TransferLink</methodName>
  <params>
    <param>
      <value>
        <string>0014682067</string>
      </value>
    </param>
    <param>
      <value>
        <string>TESTTTK</string>
      </value>
    </param>
    <param>
      <value>
        <string>5267262238630233</string>
      </value>
    </param>
    <param>
      <value>
        <string>5267262930751857</string>
      </value>
    </param>
    <param>
      <value>
        <string>123456</string>
      </value>
    </param>
    <param>
      <value>
        <dateTime.iso8601>20200327T00:00:00</dateTime.iso8601>
      </value>
    </param>
    <param>
      <value>
        <string>B96AFC35F3C59A6B89575CA70C32948CBDEE0F41</string>
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
| resultCode | String | <p>Status code indicating transaction result.</p> |



{/* spacing: desktop=20, mobile=10 */}



```xml
<?xml version=""1.0""?>
<methodCall>
  <methodName>TransferLink</methodName>
  <params>
    <param>
      <value>
        <string>0014682067</string>
      </value>
    </param>
    <param>
      <value>
        <string>TESTTTK</string>
      </value>
    </param>
    <param>
      <value>
        <string>5267262238630233</string>
      </value>
    </param>
    <param>
      <value>
        <string>5267262930751857</string>
      </value>
    </param>
    <param>
      <value>
        <string>123456</string>
      </value>
    </param>
    <param>
      <value>
        <dateTime.iso8601>20200327T00:00:00</dateTime.iso8601>
      </value>
    </param>
    <param>
      <value>
        <string>B96AFC35F3C59A6B89575CA70C32948CBDEE0F41</string>
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




\{/* spacing: desktop=20, mobile=10 */\}
