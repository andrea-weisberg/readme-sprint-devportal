---
title: Receiving Institution (Remote)
deprecated: false
hidden: false
metadata:
  robots: index
original_path: qr-payments-api/api-reference
---
<h2>Available Methods</h2>
<ul>
<li><a href="https://developer.sprint.paymentology.com/qr-payments-api/api-reference/receiving-institution-remote/#Load">Load</a> – Load to a wallet</li>
<li><a href="https://developer.sprint.paymentology.com/qr-payments-api/api-reference/receiving-institution-remote/#LoadReversal">LoadReversal</a> – Reverse a load to a wallet</li>
</ul>



\{/* unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"\} */}


<p> <br />
<a id="Load"></p>
<h2>Load</h2>
<p></a><br />
Load to a wallet.</p>



\{/* spacing: desktop=20, mobile=10 */\}


#### Path parameters

| Parameter | Type | Limits | Required | Description |
|---|---|---|:--:|---|
| terminalID | String | 10 characters | ✓ | <p>The Paymentology issued terminal ID of the terminal requesting the transaction</p> |
| Reference | String | 11-19 characters | ✓ | <p>The reference of the wallet to retrieve the balance for</p> |
| requestAmount | Integer |  | ✓ | <p>The amount to be loaded</p> |
| narrative | String | 1-255 characters | ✓ | <p>A description of the terminal where the card was used</p> |
| transactionType | String | 2 characters | ✓ | <p>2 character string identifying the type of transaction: 28 => Payment</p> |
| transactionID | String | 1-40 characters | ✓ | <p>Client generated transaction ID to assist in identify transactions on the client side</p> |
| transactionDate | Date |  |  | <p>Client generated / local transaction date to assist in identifying transactions on the client side</p> |
| checksum | String |  | ✓ | <p>HMAC-SHA1 hashed signature of the concatenated method name with all argument values using the terminal password as private key</p> |



\{/* spacing: desktop=20, mobile=10 */\}



```xml
<methodCall>
  <methodName>load</methodName>
  <params>
    <param>
      <value>
        <string>123456789</string>
      </value>
    </param>
    <param>
      <value>
        <string>123456</string>
      </value>
    </param>
    <param>
      <value>
        <int>20000</int>
      </value>
    </param>
    <param>
      <value>
        <string>123455</string>
      </value>
    </param>
    <param>
      <value>
        <string>2</string>
      </value>
    </param>
    <param>
      <value>
        <string>123456</string>
      </value>
    </param>
    <param>
      <value>
        <dateTime.iso8601>20100102T12:34:56+0700</dateTime.iso8601>
      </value>
    </param>
    <param>
      <value>
        <string>945526A6F4DD41C92DD0CCB1CAC0B4DDDE3C3089</string>
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
                            <int>1</int>
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

```,```xml
<?xml version="1.0"?>
<methodCall>
  <methodName>LoadReversal</methodName>
  <params>
    <param>
      <value>
        <string>0043889641</string>
      </value>
    </param>
    <param>
      <value>
        <string>019919</string>
      </value>
    </param>
    <param>
      <value>
        <int>180000</int>
      </value>
    </param>
    <param>
      <value>
        <string>Testing Load </string>
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
        <string>525337</string>
      </value>
    </param>
    <param>
      <value>
        <dateTime.iso8601>20201218T08:40:28</dateTime.iso8601>
      </value>
    </param>
    <param>
      <value>
        <string>8968578568978</string>
      </value>
    </param>
    <param>
      <value>
        <dateTime.iso8601>20201218T13:52:52</dateTime.iso8601>
      </value>
    </param>
    <param>
      <value>
        <string>A56B25A5145D0BBFFEC7107B4E95AF593728CC1E</string>
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
                            <int>1</int>
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




{/* spacing: desktop=20, mobile=10 */}


#### Response schema

| Field | Type | Description |
|---|---|---|
| resultCode | Integer | <p>Status code indicating transaction result</p> |
| resultText | String | <p>Text indicating transaction result</p> |



{/* spacing: desktop=20, mobile=10 */}



```xml
<methodCall>
  <methodName>load</methodName>
  <params>
    <param>
      <value>
        <string>123456789</string>
      </value>
    </param>
    <param>
      <value>
        <string>123456</string>
      </value>
    </param>
    <param>
      <value>
        <int>20000</int>
      </value>
    </param>
    <param>
      <value>
        <string>123455</string>
      </value>
    </param>
    <param>
      <value>
        <string>2</string>
      </value>
    </param>
    <param>
      <value>
        <string>123456</string>
      </value>
    </param>
    <param>
      <value>
        <dateTime.iso8601>20100102T12:34:56+0700</dateTime.iso8601>
      </value>
    </param>
    <param>
      <value>
        <string>945526A6F4DD41C92DD0CCB1CAC0B4DDDE3C3089</string>
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
                            <int>1</int>
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

```,```xml
<?xml version="1.0"?>
<methodCall>
  <methodName>LoadReversal</methodName>
  <params>
    <param>
      <value>
        <string>0043889641</string>
      </value>
    </param>
    <param>
      <value>
        <string>019919</string>
      </value>
    </param>
    <param>
      <value>
        <int>180000</int>
      </value>
    </param>
    <param>
      <value>
        <string>Testing Load </string>
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
        <string>525337</string>
      </value>
    </param>
    <param>
      <value>
        <dateTime.iso8601>20201218T08:40:28</dateTime.iso8601>
      </value>
    </param>
    <param>
      <value>
        <string>8968578568978</string>
      </value>
    </param>
    <param>
      <value>
        <dateTime.iso8601>20201218T13:52:52</dateTime.iso8601>
      </value>
    </param>
    <param>
      <value>
        <string>A56B25A5145D0BBFFEC7107B4E95AF593728CC1E</string>
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
                            <int>1</int>
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




\{/* unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"\} */}


<p> <br />
<a id="LoadReversal"></p>
<h2>LoadReversal</h2>
<p></a><br />
Reverse a Load to a wallet</p>



\{/* spacing: desktop=20, mobile=10 */\}


#### Path parameters

| Parameter | Type | Limits | Required | Description |
|---|---|---|:--:|---|
| terminalID | String | 10 characters | ✓ | <p>The Paymentology issued terminal ID of the terminal requesting the transaction</p> |
| reference | String | 11-19 characters | ✓ | <p>The reference of the wallet to retrieve the balance for</p> |
| requestAmount | Integer |  | ✓ | <p>The amount to be loaded</p> |
| referenceID | String |  | ✓ | <p>Transaction ID of the original transaction to be adjusted</p> |
| referenceDate | String |  | ✓ | <p>Transaction date of the original transaction or a repeat of the original deduct to be adjusted</p> |
| narrative | String | 1-255 characters | ✓ | <p>A description of the terminal where the card was used</p> |
| transactionID | String | 1-40 characters | ✓ | <p>Transaction ID number generated by the calling client</p> |
| transactionData | String |  | ✓ | <p>Extra information about the transaction in a KLV format</p> |
| transactionDate | Date |  |  | <p>Transaction date generated by the calling client</p> |
| checksum | String |  | ✓ | <p>HMAC-SHA1 hashed signature of the concatenated method name with all argument values using the terminal password as private key</p> |



\{/* spacing: desktop=20, mobile=10 */\}



```xml
<methodCall>
  <methodName>load</methodName>
  <params>
    <param>
      <value>
        <string>123456789</string>
      </value>
    </param>
    <param>
      <value>
        <string>123456</string>
      </value>
    </param>
    <param>
      <value>
        <int>20000</int>
      </value>
    </param>
    <param>
      <value>
        <string>123455</string>
      </value>
    </param>
    <param>
      <value>
        <string>2</string>
      </value>
    </param>
    <param>
      <value>
        <string>123456</string>
      </value>
    </param>
    <param>
      <value>
        <dateTime.iso8601>20100102T12:34:56+0700</dateTime.iso8601>
      </value>
    </param>
    <param>
      <value>
        <string>945526A6F4DD41C92DD0CCB1CAC0B4DDDE3C3089</string>
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
                            <int>1</int>
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

```,```xml
<?xml version="1.0"?>
<methodCall>
  <methodName>LoadReversal</methodName>
  <params>
    <param>
      <value>
        <string>0043889641</string>
      </value>
    </param>
    <param>
      <value>
        <string>019919</string>
      </value>
    </param>
    <param>
      <value>
        <int>180000</int>
      </value>
    </param>
    <param>
      <value>
        <string>Testing Load </string>
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
        <string>525337</string>
      </value>
    </param>
    <param>
      <value>
        <dateTime.iso8601>20201218T08:40:28</dateTime.iso8601>
      </value>
    </param>
    <param>
      <value>
        <string>8968578568978</string>
      </value>
    </param>
    <param>
      <value>
        <dateTime.iso8601>20201218T13:52:52</dateTime.iso8601>
      </value>
    </param>
    <param>
      <value>
        <string>A56B25A5145D0BBFFEC7107B4E95AF593728CC1E</string>
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
                            <int>1</int>
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



{/* spacing: desktop=20, mobile=10 */}


#### Response schema

| Field | Type | Description |
|---|---|---|
| resultCode | Integer | <p>Status code indicating transaction result</p> |
| resultText | String | <p>Text indicating transaction result</p> |



{/* spacing: desktop=20, mobile=10 */}



```xml
<methodCall>
  <methodName>load</methodName>
  <params>
    <param>
      <value>
        <string>123456789</string>
      </value>
    </param>
    <param>
      <value>
        <string>123456</string>
      </value>
    </param>
    <param>
      <value>
        <int>20000</int>
      </value>
    </param>
    <param>
      <value>
        <string>123455</string>
      </value>
    </param>
    <param>
      <value>
        <string>2</string>
      </value>
    </param>
    <param>
      <value>
        <string>123456</string>
      </value>
    </param>
    <param>
      <value>
        <dateTime.iso8601>20100102T12:34:56+0700</dateTime.iso8601>
      </value>
    </param>
    <param>
      <value>
        <string>945526A6F4DD41C92DD0CCB1CAC0B4DDDE3C3089</string>
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
                            <int>1</int>
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

```,```xml
<?xml version="1.0"?>
<methodCall>
  <methodName>LoadReversal</methodName>
  <params>
    <param>
      <value>
        <string>0043889641</string>
      </value>
    </param>
    <param>
      <value>
        <string>019919</string>
      </value>
    </param>
    <param>
      <value>
        <int>180000</int>
      </value>
    </param>
    <param>
      <value>
        <string>Testing Load </string>
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
        <string>525337</string>
      </value>
    </param>
    <param>
      <value>
        <dateTime.iso8601>20201218T08:40:28</dateTime.iso8601>
      </value>
    </param>
    <param>
      <value>
        <string>8968578568978</string>
      </value>
    </param>
    <param>
      <value>
        <dateTime.iso8601>20201218T13:52:52</dateTime.iso8601>
      </value>
    </param>
    <param>
      <value>
        <string>A56B25A5145D0BBFFEC7107B4E95AF593728CC1E</string>
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
                            <int>1</int>
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




\{/* unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"\} */}


<p><a href="https://developer.sprint.paymentology.com/qr-payments-api/api-reference/appendix/#RIRemote"

<h2>Appendix</h2>
<p></a></p>
