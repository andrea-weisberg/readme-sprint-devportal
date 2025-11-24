---
title: Originating Institution
deprecated: false
hidden: false
metadata:
  robots: index
---
## Available Methods

* [TransferPaymentToMerchant](https://developer.sprint.paymentology.com/qr-payments-api/api-reference/originating-institution/#TransferPaymentToMerchant) – Transfer payment to merchant

---

## TransferPaymentToMerchant

Transfer payment to merchant.

#### Path parameters

| Parameter              | type    |           Limits | required | Description                                                                                                                                                      |
| ---------------------- | ------- | ---------------: | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| terminalID             | String  |    10 characters | ✓        | The Paymentology issued terminal id of the terminal requesting the transaction                                                                                   |
| recipientAccountNumber | String  | 11-19 characters | ✓        | Card Number of the recipient/merchant                                                                                                                            |
| recipientFirstName     | String  |  1-40 characters | ✓        | First name of the recipient/merchant                                                                                                                             |
| recipientLastName      | String  |  1-40 characters | ✓        | Last name of the recipient/merchant                                                                                                                              |
| recipientCity          | String  |  1-25 characters | ✓        | City of the recipient/merchant                                                                                                                                   |
| recipientCountry       | String  |     3 characters | ✓        | ISO alpha country code of the recipient/merchant Ex. ZAF                                                                                                         |
| recipientCategoryCode  | String  |   1-4 characters | ✓        | Mastercard defined merchant category code                                                                                                                        |
| senderFirstName        | String  |  1-40 characters | ✓        | First name of the sender                                                                                                                                         |
| senderLastName         | String  |  1-40 characters | ✓        | Last name of the sender                                                                                                                                          |
| senderAddress          | String  | 1-100 characters | ✓        | Address of the sender                                                                                                                                            |
| senderCity             | String  |  1-25 characters | ✓        | City of the sender                                                                                                                                               |
| senderPostalCode       | String  |   4-5 characters | ✓        | Postal code of the sender                                                                                                                                        |
| senderCountry          | String  |     3 characters | ✓        | ISO alpha country code of the sender Ex. ZAF                                                                                                                     |
| reference              | String  | 1-100 characters | ✓        | The user defined reference to the card; for example a member id or wallet number                                                                                 |
| requestAmount          | Integer |                  | ✓        | The amount to be sent to the receiving subscriber                                                                                                                |
| transactionCurrency    | String  |     3 characters | ✓        | Currency of the requestAmount Ex. ZAR                                                                                                                            |
| transactionID          | String  |  1-40 characters | ✓        | Client generated transaction id to assist in identify transactions on the client side                                                                            |
| transactionDate        | Date    |                  |          | Client generated / local transaction date to assist in identifying transactions on the client side                                                               |
| optionalData           | String  |                  | ✓        | Struct with optional fields, right now only “recipientPostalCode” field is accepted. See above for details. The maximum length of the recipientPostalCode is 10. |
| checksum               | String  |                  | ✓        | The calculated HMAC-SHA1 signature of the call as specified in the rules of thumb                                                                                |

```xml
<methodCall>
    <methodName>TransferPaymentToMerchant</methodName>
    <params  />
        <param  />
            <value>
                <string>0039467951</string>
            </value>
        </param>
        <param  />
            <value>
                <string>AFF44112</string>
            </value>
        </param>
        <param  />
            <value>
                <string>John</string>
            </value>
        </param>
        <param  />
            <value>
                <string>Doe</string>
            </value>
        </param>
        <param  />
            <value>
                <string>Bangkok</string>
            </value>
        </param>
        <param  />
            <value>
                <string>THA</string>
            </value>
        </param>
        <param  />
            <value>
                <string>10261</string>
            </value>
        </param>
        <param  />
            <value>
                <string>Jeremy</string>
            </value>
        </param>
        <param  />
            <value>
                <string>Booster</string>
            </value>
        </param>
        <param  />
            <value>
                <string>137 Zoho Rade 12</string>
            </value>
        </param>
        <param  />
            <value>
                <string>Bangkok</string>
            </value>
        </param>
        <param  />
            <value>
                <string>45687</string>
            </value>
        </param>
        <param  />
            <value>
                <string>THA</string>
            </value>
        </param>
        <param  />
            <value>
                <string>039200071850</string>
            </value>
        </param>
        <param  />
            <value>
                <int>100</int>
            </value>
        </param>
        <param  />
            <value>
                <string>THB</string>
            </value>
        </param>
        <param  />
            <value>
                <string>txn1234567</string>
            </value>
        </param>
        <param  />
            <value>
                <dateTime.iso8601>20100102T12:34:56+0700</dateTime.iso8601>
            </value>
        </param>
        <param  />
            <value>
                <struct  />
            </value>
        </param>
        <param  />
            <value>
                <string>FE0F831A3AEB4925B97F3037D9B4BDDF5C615C3B</string>
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
                            <double>1</double>
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

#### Response schema

| Field      | type    | Description                               |
| ---------- | ------- | ----------------------------------------- |
| resultCode | Integer | Status code indicating transaction result |
| resultText | String  | Text indicating transaction result        |

```xml
<methodCall>
    <methodName>TransferPaymentToMerchant</methodName>
    <params  />
        <param  />
            <value>
                <string>0039467951</string>
            </value>
        </param>
        <param  />
            <value>
                <string>AFF44112</string>
            </value>
        </param>
        <param  />
            <value>
                <string>John</string>
            </value>
        </param>
        <param  />
            <value>
                <string>Doe</string>
            </value>
        </param>
        <param  />
            <value>
                <string>Bangkok</string>
            </value>
        </param>
        <param  />
            <value>
                <string>THA</string>
            </value>
        </param>
        <param  />
            <value>
                <string>10261</string>
            </value>
        </param>
        <param  />
            <value>
                <string>Jeremy</string>
            </value>
        </param>
        <param  />
            <value>
                <string>Booster</string>
            </value>
        </param>
        <param  />
            <value>
                <string>137 Zoho Rade 12</string>
            </value>
        </param>
        <param  />
            <value>
                <string>Bangkok</string>
            </value>
        </param>
        <param  />
            <value>
                <string>45687</string>
            </value>
        </param>
        <param  />
            <value>
                <string>THA</string>
            </value>
        </param>
        <param  />
            <value>
                <string>039200071850</string>
            </value>
        </param>
        <param  />
            <value>
                <int>100</int>
            </value>
        </param>
        <param  />
            <value>
                <string>THB</string>
            </value>
        </param>
        <param  />
            <value>
                <string>txn1234567</string>
            </value>
        </param>
        <param  />
            <value>
                <dateTime.iso8601>20100102T12:34:56+0700</dateTime.iso8601>
            </value>
        </param>
        <param  />
            <value>
                <struct  />
            </value>
        </param>
        <param  />
            <value>
                <string>FE0F831A3AEB4925B97F3037D9B4BDDF5C615C3B</string>
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
                            <double>1</double>
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

---

### Appendix

[https://developer.sprint.paymentology.com/qr-payments-api/api-reference/appendix/#OI](https://developer.sprint.paymentology.com/qr-payments-api/api-reference/appendix/#OI)
