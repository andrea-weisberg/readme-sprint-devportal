---
title: LoadReversal
deprecated: false
hidden: false
metadata:
  robots: index
---
<section id="tutuka-block-33" className="tutuka-block tutuka-block--text-full-width">Reverse a load that was previously requested on a wallet.<strong>KLV will not be sent for reversals. Only reference data will be included if there is any. If KLV data is needed please lookup <a href="https:developer.sprint.paymentology.com/companion-api/klv-lookup/">KLV</a> from the reference data included.</strong></p>
</section>

#### Path parameters

| Parameter | type | Limits | required | Description |
|---|---|---|:--:|---|
| terminalID | String | 10 characters | ✓ | <p>The Paymentology issued terminal id of the terminal requesting the transaction</p> |
| reference | String | 1-255 characters | ✓ | <p>The reference of the wallet to reverse a previous load</p> |
| requestAmount | Integer |  | ✓ | <p>The amount of the original load to be reversed (can be partial)</p> |
| narrative | String | 1-255 characters | ✓ | <p>A description of the terminal where the card was used</p> |
| transactionData | String | 0-2048 characters | ✓ | <p>Extra information about the transaction in a <a href="https:developer.sprint.paymentology.com/companion-api/klv-lookup/">KLV format</a></p> |
| referenceID | String | 1-255 characters | ✓ | <p>Transaction id of the original load to be reversed</p> |
| referenceDate | Date |  | ✓ | <p>Transaction date of the original load to be reversed</p> |
| transactionID | String | 1-255 characters | ✓ | <p>Transaction id to identify the reversal message.</p> <p><em>Note that the Transaction id is not a unique value and may be duplicated over time.</em></p> |
| transactionDate | Date |  | ✓ | <p>Transaction date to identify the reversal message</p> |
| checksum | String |  | ✓ | <p>HMAC-SHA256 hashed signature of the concatenated method name with all argument values using the terminal password as private key</p> |

```xml
<?xml version="1.0"?>
<methodCall>
    <methodName>LoadReversal</methodName>
    <params >
        <param >
            <value>
                <string>0089753250</string>
            </value>
        </param>
        <param >
            <value>
                <string>592193355535</string>
            </value>
        </param>
        <param >
            <value>
                <int>7900000</int>
            </value>
        </param>
        <param >
            <value>
                <string>20200821T02:42:00/Lazada\Lazada, Ho Chi Minh, VN\Ho Chi Minh\          08 VNM</string>
            </value>
        </param>
        <param >
            <value>
                <string>
                </string>
            </value>
        </param>
        <param >
            <value>
                <string>2911DF1B-9F06-8EBA-F1E8EE0BDF673D4C</string>
            </value>
        </param>
        <param >
            <value>
                <dateTime.iso8601>20200824T01:44:00</dateTime.iso8601>
            </value>
        </param>
        <param >
            <value>
                <string>2010048</string>
            </value>
        </param>
        <param >
            <value>
                <dateTime.iso8601>20200824T01:44:07</dateTime.iso8601>
            </value>
        </param>
        <param >
            <value>
                <string>6F0D0CFF534288C848D7881CBFEFF88605DB6214</string>
            </value>
        </param>
    </params>
</methodCall>

```,```xml
"<methodResponse>
  <params >
    <param >
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
</methodResponse>"

```

<p> </p>

#### Response schema

| Field | type | Description |
|---|---|---|
| resultCode | Integer | <p>Status code indicating transaction result</p> |

```xml
<?xml version="1.0"?>
<methodCall>
    <methodName>LoadReversal</methodName>
    <params >
        <param >
            <value>
                <string>0089753250</string>
            </value>
        </param>
        <param >
            <value>
                <string>592193355535</string>
            </value>
        </param>
        <param >
            <value>
                <int>7900000</int>
            </value>
        </param>
        <param >
            <value>
                <string>20200821T02:42:00/Lazada\Lazada, Ho Chi Minh, VN\Ho Chi Minh\          08 VNM</string>
            </value>
        </param>
        <param >
            <value>
                <string>
                </string>
            </value>
        </param>
        <param >
            <value>
                <string>2911DF1B-9F06-8EBA-F1E8EE0BDF673D4C</string>
            </value>
        </param>
        <param >
            <value>
                <dateTime.iso8601>20200824T01:44:00</dateTime.iso8601>
            </value>
        </param>
        <param >
            <value>
                <string>2010048</string>
            </value>
        </param>
        <param >
            <value>
                <dateTime.iso8601>20200824T01:44:07</dateTime.iso8601>
            </value>
        </param>
        <param >
            <value>
                <string>6F0D0CFF534288C848D7881CBFEFF88605DB6214</string>
            </value>
        </param>
    </params>
</methodCall>

```,```xml
"<methodResponse>
  <params >
    <param >
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
</methodResponse>"

```

<p> </p>

<p><a className="btn btn--primary" href="https:developer.sprint.paymentology.com/companion-api/api-reference/remote/">Back to Remote API menu</a></p>
</a></p></p></int></value></name></member></struct></value></params></methodresponse></string></value></value></string></value></value></string></value></string></value></string></value></int></value></string></value></string></value></params></methodname></methodcall></p></p></int></value></name></member></struct></value></params></methodresponse></string></value></value></string></value></value></string></value></string></value></string></value></int></value></string></value></string></value></params></methodname></methodcall></p></p></em></p></p></p></p></a></p></p></p></p></p></a></strong></section>
