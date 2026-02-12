---
title: Receiving Institution (Remote)
deprecated: false
hidden: false
metadata:
  robots: index
---
## Available Methods

* [Load](https://developer.sprint.paymentology.com/qr-payments-api/api-reference/receiving-institution-remote/#Load) – Load to a wallet

* [LoadReversal](https://developer.sprint.paymentology.com/qr-payments-api/api-reference/receiving-institution-remote/#LoadReversal) – Reverse a load to a wallet

## Load

Load to a wallet.

#### Path parameters

| Parameter       | type    | Limits           | required | Description                                                                                                                    |
| --------------- | ------- | ---------------- | :------: | ------------------------------------------------------------------------------------------------------------------------------ |
| terminalID      | String  | 10 characters    |     ✓    | The Paymentology issued terminal id of the terminal requesting the transaction                                                 |
| Reference       | String  | 11-19 characters |     ✓    | The reference of the wallet to retrieve the balance for                                                                        |
| requestAmount   | Integer |                  |     ✓    | The amount to be loaded                                                                                                        |
| narrative       | String  | 1-255 characters |     ✓    | A description of the terminal where the card was used                                                                          |
| transactionType | String  | 2 characters     |     ✓    | 2 character string identifying the type of transaction: 28 => Payment                                                          |
| transactionID   | String  | 1-40 characters  |     ✓    | Client generated transaction id to assist in identify transactions on the client side                                          |
| transactionDate | Date    |                  |          | Client generated / local transaction date to assist in identifying transactions on the client side                             |
| checksum        | String  |                  |     ✓    | HMAC-SHA1 hashed signature of the concatenated method name with all argument values using the terminal password as private key |

```xml
<methodCall>
  <methodName>load</methodName>
  <params  />
    <param  />
      <value>
        <string>123456789</string>
      </value>
    </param>
    <param  />
      <value>
        <string>123456</string>
      </value>
    </param>
    <param  />
      <value>
        <int>20000</int>
      </value>
    </param>
    <param  />
      <value>
        <string>123455</string>
      </value>
    </param>
    <param  />
      <value>
        <string>2</string>
      </value>
    </param>
    <param  />
      <value>
        <string>123456</string>
      </value>
    </param>
    <param  />
      <value>
        <dateTime.iso8601>20100102T12:34:56+0700</dateTime.iso8601>
      </value>
    </param>
    <param  />
      <value>
        <string>945526A6F4DD41C92DD0CCB1CAC0B4DDDE3C3089</string>
      </value>
    </param>
  </params>
</methodCall>
```

```xml
<methodResponse>
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

```xml
<?xml version="1.0"?>
<methodCall>
  <methodName>LoadReversal</methodName>
  <params  />
    <param  />
      <value>
        <string>0043889641</string>
      </value>
    </param>
    <param  />
      <value>
        <string>019919</string>
      </value>
    </param>
    <param  />
      <value>
        <int>180000</int>
      </value>
    </param>
    <param  />
      <value>
        <string>Testing Load </string>
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
        <string>525337</string>
      </value>
    </param>
    <param  />
      <value>
        <dateTime.iso8601>20201218T08:40:28</dateTime.iso8601>
      </value>
    </param>
    <param  />
      <value>
        <string>8968578568978</string>
      </value>
    </param>
    <param  />
      <value>
        <dateTime.iso8601>20201218T13:52:52</dateTime.iso8601>
      </value>
    </param>
    <param  />
      <value>
        <string>A56B25A5145D0BBFFEC7107B4E95AF593728CC1E</string>
      </value>
    </param>
  </params>
</methodCall>
```

```xml
<methodResponse>
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

#### Response schema

| Field      | type    | Description                               |
| ---------- | ------- | ----------------------------------------- |
| resultCode | Integer | Status code indicating transaction result |
| resultText | String  | Text indicating transaction result        |

```xml
<methodCall>
  <methodName>load</methodName>
  <params  />
    <param  />
      <value>
        <string>123456789</string>
      </value>
    </param>
    <param  />
      <value>
        <string>123456</string>
      </value>
    </param>
    <param  />
      <value>
        <int>20000</int>
      </value>
    </param>
    <param  />
      <value>
        <string>123455</string>
      </value>
    </param>
    <param  />
      <value>
        <string>2</string>
      </value>
    </param>
    <param  />
      <value>
        <string>123456</string>
      </value>
    </param>
    <param  />
      <value>
        <dateTime.iso8601>20100102T12:34:56+0700</dateTime.iso8601>
      </value>
    </param>
    <param  />
      <value>
        <string>945526A6F4DD41C92DD0CCB1CAC0B4DDDE3C3089</string>
      </value>
    </param>
  </params>
</methodCall>
```

```xml
<methodResponse>
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

```xml
<?xml version="1.0"?>
<methodCall>
  <methodName>LoadReversal</methodName>
  <params  />
    <param  />
      <value>
        <string>0043889641</string>
      </value>
    </param>
    <param  />
      <value>
        <string>019919</string>
      </value>
    </param>
    <param  />
      <value>
        <int>180000</int>
      </value>
    </param>
    <param  />
      <value>
        <string>Testing Load </string>
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
        <string>525337</string>
      </value>
    </param>
    <param  />
      <value>
        <dateTime.iso8601>20201218T08:40:28</dateTime.iso8601>
      </value>
    </param>
    <param  />
      <value>
        <string>8968578568978</string>
      </value>
    </param>
    <param  />
      <value>
        <dateTime.iso8601>20201218T13:52:52</dateTime.iso8601>
      </value>
    </param>
    <param  />
      <value>
        <string>A56B25A5145D0BBFFEC7107B4E95AF593728CC1E</string>
      </value>
    </param>
  </params>
</methodCall>
```

```xml
<methodResponse>
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

## LoadReversal

Reverse a Load to a wallet

#### Path parameters

| Parameter       | type    | Limits           | required | Description                                                                                                                    |
| --------------- | ------- | ---------------- | :------: | ------------------------------------------------------------------------------------------------------------------------------ |
| terminalID      | String  | 10 characters    |     ✓    | The Paymentology issued terminal id of the terminal requesting the transaction                                                 |
| reference       | String  | 11-19 characters |     ✓    | The reference of the wallet to retrieve the balance for                                                                        |
| requestAmount   | Integer |                  |     ✓    | The amount to be loaded                                                                                                        |
| referenceID     | String  |                  |     ✓    | Transaction id of the original transaction to be adjusted                                                                      |
| referenceDate   | String  |                  |     ✓    | Transaction date of the original transaction or a repeat of the original deduct to be adjusted                                 |
| narrative       | String  | 1-255 characters |     ✓    | A description of the terminal where the card was used                                                                          |
| transactionID   | String  | 1-40 characters  |     ✓    | Transaction id number generated by the calling client                                                                          |
| transactionData | String  |                  |     ✓    | Extra information about the transaction in a KLV format                                                                        |
| transactionDate | Date    |                  |          | Transaction date generated by the calling client                                                                               |
| checksum        | String  |                  |     ✓    | HMAC-SHA1 hashed signature of the concatenated method name with all argument values using the terminal password as private key |

```xml
<methodCall>
  <methodName>load</methodName>
  <params  />
    <param  />
      <value>
        <string>123456789</string>
      </value>
    </param>
    <param  />
      <value>
        <string>123456</string>
      </value>
    </param>
    <param  />
      <value>
        <int>20000</int>
      </value>
    </param>
    <param  />
      <value>
        <string>123455</string>
      </value>
    </param>
    <param  />
      <value>
        <string>2</string>
      </value>
    </param>
    <param  />
      <value>
        <string>123456</string>
      </value>
    </param>
    <param  />
      <value>
        <dateTime.iso8601>20100102T12:34:56+0700</dateTime.iso8601>
      </value>
    </param>
    <param  />
      <value>
        <string>945526A6F4DD41C92DD0CCB1CAC0B4DDDE3C3089</string>
      </value>
    </param>
  </params>
</methodCall>
```

```xml
<methodResponse>
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

```xml
<?xml version="1.0"?>
<methodCall>
  <methodName>LoadReversal</methodName>
  <params  />
    <param  />
      <value>
        <string>0043889641</string>
      </value>
    </param>
    <param  />
      <value>
        <string>019919</string>
      </value>
    </param>
    <param  />
      <value>
        <int>180000</int>
      </value>
    </param>
    <param  />
      <value>
        <string>Testing Load </string>
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
        <string>525337</string>
      </value>
    </param>
    <param  />
      <value>
        <dateTime.iso8601>20201218T08:40:28</dateTime.iso8601>
      </value>
    </param>
    <param  />
      <value>
        <string>8968578568978</string>
      </value>
    </param>
    <param  />
      <value>
        <dateTime.iso8601>20201218T13:52:52</dateTime.iso8601>
      </value>
    </param>
    <param  />
      <value>
        <string>A56B25A5145D0BBFFEC7107B4E95AF593728CC1E</string>
      </value>
    </param>
  </params>
</methodCall>
```

```xml
<methodResponse>
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

#### Response schema

| Field      | type    | Description                               |
| ---------- | ------- | ----------------------------------------- |
| resultCode | Integer | Status code indicating transaction result |
| resultText | String  | Text indicating transaction result        |

```xml
<methodCall>
  <methodName>load</methodName>
  <params  />
    <param  />
      <value>
        <string>123456789</string>
      </value>
    </param>
    <param  />
      <value>
        <string>123456</string>
      </value>
    </param>
    <param  />
      <value>
        <int>20000</int>
      </value>
    </param>
    <param  />
      <value>
        <string>123455</string>
      </value>
    </param>
    <param  />
      <value>
        <string>2</string>
      </value>
    </param>
    <param  />
      <value>
        <string>123456</string>
      </value>
    </param>
    <param  />
      <value>
        <dateTime.iso8601>20100102T12:34:56+0700</dateTime.iso8601>
      </value>
    </param>
    <param  />
      <value>
        <string>945526A6F4DD41C92DD0CCB1CAC0B4DDDE3C3089</string>
      </value>
    </param>
  </params>
</methodCall>
```

```xml
<methodResponse>
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

```xml
<?xml version="1.0"?>
<methodCall>
  <methodName>LoadReversal</methodName>
  <params  />
    <param  />
      <value>
        <string>0043889641</string>
      </value>
    </param>
    <param  />
      <value>
        <string>019919</string>
      </value>
    </param>
    <param  />
      <value>
        <int>180000</int>
      </value>
    </param>
    <param  />
      <value>
        <string>Testing Load </string>
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
        <string>525337</string>
      </value>
    </param>
    <param  />
      <value>
        <dateTime.iso8601>20201218T08:40:28</dateTime.iso8601>
      </value>
    </param>
    <param  />
      <value>
        <string>8968578568978</string>
      </value>
    </param>
    <param  />
      <value>
        <dateTime.iso8601>20201218T13:52:52</dateTime.iso8601>
      </value>
    </param>
    <param  />
      <value>
        <string>A56B25A5145D0BBFFEC7107B4E95AF593728CC1E</string>
      </value>
    </param>
  </params>
</methodCall>
```

```xml
<methodResponse>
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

## Appendix

[https://developer.sprint.paymentology.com/qr-payments-api/api-reference/appendix/#RIRemote](https://developer.sprint.paymentology.com/qr-payments-api/api-reference/appendix/#RIRemote)
