---
title: LoadReversal
deprecated: false
hidden: false
metadata:
  robots: index
---
Reverse a load that was previously requested on a wallet. **KLV will not be sent for reversals. Only reference data will be included if there is any. If KLV data is needed please lookup [KLV](https://developer.sprint.paymentology.com/companion-api/klv-lookup/) from the reference data included.**

#### Path parameters

| Parameter | type | Limits | required | Description |
|---|---|---|:--:|---|
| terminalID | String | 10 characters | ✓ | The Paymentology issued terminal id of the terminal requesting the transaction |
| reference | String | 1-255 characters | ✓ | The reference of the wallet to reverse a previous load |
| requestAmount | Integer |  | ✓ | The amount of the original load to be reversed (can be partial) |
| narrative | String | 1-255 characters | ✓ | A description of the terminal where the card was used |
| transactionData | String | 0-2048 characters | ✓ | Extra information about the transaction in a [KLV format](https://developer.sprint.paymentology.com/companion-api/klv-lookup/) |
| referenceID | String | 1-255 characters | ✓ | Transaction id of the original load to be reversed |
| referenceDate | Date |  | ✓ | Transaction date of the original load to be reversed |
| transactionID | String | 1-255 characters | ✓ | Transaction id to identify the reversal message. *Note that the Transaction id is not a unique value and may be duplicated over time.* |
| transactionDate | Date |  | ✓ | Transaction date to identify the reversal message |
| checksum | String |  | ✓ | HMAC-SHA256 hashed signature of the concatenated method name with all argument values using the terminal password as private key |

```xml
<?xml version="1.0"?>
<methodCall>
    <methodName>LoadReversal</methodName>
    <params  />
        <param  />
            <value>
                <string>0089753250</string>
            </value>
        </param>
        <param  />
            <value>
                <string>592193355535</string>
            </value>
        </param>
        <param  />
            <value>
                <int>7900000</int>
            </value>
        </param>
        <param  />
            <value>
                <string>20200821T02:42:00/Lazada\Lazada, Ho Chi Minh, VN\Ho Chi Minh\          08 VNM</string>
            </value>
        </param>
        <param  />
            <value>
                <string>
                </string>
            </value>
        </param>
        <param  />
            <value>
                <string>2911DF1B-9F06-8EBA-F1E8EE0BDF673D4C</string>
            </value>
        </param>
        <param  />
            <value>
                <dateTime.iso8601>20200824T01:44:00</dateTime.iso8601>
            </value>
        </param>
        <param  />
            <value>
                <string>2010048</string>
            </value>
        </param>
        <param  />
            <value>
                <dateTime.iso8601>20200824T01:44:07</dateTime.iso8601>
            </value>
        </param>
        <param  />
            <value>
                <string>6F0D0CFF534288C848D7881CBFEFF88605DB6214</string>
            </value>
        </param>
    </params>
</methodCall>
```

```xml
"<methodResponse>
  <params  />
    <param  />
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

#### Response schema

| Field | type | Description |
|---|---|---|
| resultCode | Integer | Status code indicating transaction result |

```xml
<?xml version="1.0"?>
<methodCall>
    <methodName>LoadReversal</methodName>
    <params  />
        <param  />
            <value>
                <string>0089753250</string>
            </value>
        </param>
        <param  />
            <value>
                <string>592193355535</string>
            </value>
        </param>
        <param  />
            <value>
                <int>7900000</int>
            </value>
        </param>
        <param  />
            <value>
                <string>20200821T02:42:00/Lazada\Lazada, Ho Chi Minh, VN\Ho Chi Minh\          08 VNM</string>
            </value>
        </param>
        <param  />
            <value>
                <string>
                </string>
            </value>
        </param>
        <param  />
            <value>
                <string>2911DF1B-9F06-8EBA-F1E8EE0BDF673D4C</string>
            </value>
        </param>
        <param  />
            <value>
                <dateTime.iso8601>20200824T01:44:00</dateTime.iso8601>
            </value>
        </param>
        <param  />
            <value>
                <string>2010048</string>
            </value>
        </param>
        <param  />
            <value>
                <dateTime.iso8601>20200824T01:44:07</dateTime.iso8601>
            </value>
        </param>
        <param  />
            <value>
                <string>6F0D0CFF534288C848D7881CBFEFF88605DB6214</string>
            </value>
        </param>
    </params>
</methodCall>
```

```xml
"<methodResponse>
  <params  />
    <param  />
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

[Back to Remote API menu](https://developer.sprint.paymentology.com/companion-api/api-reference/remote/)
