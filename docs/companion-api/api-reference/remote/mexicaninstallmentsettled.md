---
title: MexicanInstallmentSettled
deprecated: false
hidden: false
metadata:
  robots: index
---
<p>Notifies that a Mexican installment transaction is settled.</p>

#### Path parameters

| Parameter | type | Limits | required | Description |
|---|---|---|:--:|---|
| terminalID  | String | 10 characters | ✓ | <p>The Paymentology issued terminal id of the terminal requesting the transaction</p> |
| reference | String | 10 characters | ✓ | <p>The reference of the wallet that the installment transaction just got settled.</p> |
| referenceID | String | 1-255 characters | ✓ | <p>Transaction id of the original authorisation that was settled.</p> |
| referenceDate | String |  | ✓ | <p>Transaction date of the original authorisation that was settled.</p> |
| typeOfCredit | Integer |  | ✓ | <p>One of the following:<br > 00 (No Promotion)<br > 03 (Without interest for the cardholder)<br > 05 (With interest for the cardholder)<br > 07 (Buy today, pay later)</p> |
| totalNumberOfInstallments | String | 2 characters | ✓ | <p>The total number of the installments linked to the installment transaction.</p> |
| gracePeriod | Integer |  | ✓ | <p>Grace period (in months) before first installment</p> |
| transactionCurrencyCode | Integer |  | ✓ | <p>The local currency code of the acquirer or source location of the transaction (eg. 484 = Mexican Peso)</p> |
| checksum | String |  | ✓ | <p>HMAC-SHA256 hashed signature of the concatenated method name with all argument values using the terminal password as private key.</p> |

```xml
<?xml version="1.0"?>
<methodCall>
    <methodName>MexicanInstallmentSettled</methodName>
    <params >
        <param >
            <value>
                <string>0097852049</string>
            </value>
        </param>
        <param >
            <value>
                <string>5a332769-264a-402c-851b-2d7a5ddb7bee</string>
            </value>
        </param>
        <param >
            <value>
                <string>117363249782</string>
            </value>
        </param>
        <param >
            <value>
                <dateTime.iso8601>20230223T03:48:27</dateTime.iso8601>
            </value>
        </param>
        <param >
            <value>
                <int>05</int>
            </value>
        </param>
        <param >
            <value>
                <string>03</string>
            </value>
        </param>
        <param >
            <value>
                <int>02</int>
            </value>
        </param>
        <param >
            <value>
                <int>484</int>
            </value>
        </param>
        <param >
            <value>
                <string>B90B6C3D75173C0CEB312DF2E0225EC1A4A3FF0F</string>
            </value>
        </param>
    </params>
</methodCall>

```,```xml
<methodResponse>
  <params >
    <param >
      <value>
        <struct>
          <member>
            <name>
              resultCode
            </name>
            <value>
              <int>
                1
              </int>
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
| resultCode | Integer | <p>Status code indicating transaction result</p> |

```xml
<?xml version="1.0"?>
<methodCall>
    <methodName>MexicanInstallmentSettled</methodName>
    <params >
        <param >
            <value>
                <string>0097852049</string>
            </value>
        </param>
        <param >
            <value>
                <string>5a332769-264a-402c-851b-2d7a5ddb7bee</string>
            </value>
        </param>
        <param >
            <value>
                <string>117363249782</string>
            </value>
        </param>
        <param >
            <value>
                <dateTime.iso8601>20230223T03:48:27</dateTime.iso8601>
            </value>
        </param>
        <param >
            <value>
                <int>05</int>
            </value>
        </param>
        <param >
            <value>
                <string>03</string>
            </value>
        </param>
        <param >
            <value>
                <int>02</int>
            </value>
        </param>
        <param >
            <value>
                <int>484</int>
            </value>
        </param>
        <param >
            <value>
                <string>B90B6C3D75173C0CEB312DF2E0225EC1A4A3FF0F</string>
            </value>
        </param>
    </params>
</methodCall>

```,```xml
<methodResponse>
  <params >
    <param >
      <value>
        <struct>
          <member>
            <name>
              resultCode
            </name>
            <value>
              <int>
                1
              </int>
            </value>
          </member>
        </struct>
      </value>
    </param>
  </params>
</methodResponse>

```

<p> </p>

<p><a className="btn btn--primary" href="https:developer.sprint.paymentology.com/companion-api/api-reference/remote/">BACK TO REMOTE API MENU</a></p>
</a></p></p></int></value></name></member></struct></value></params></methodresponse></string></value></int></value></int></value></string></value></int></value></value></string></value></string></value></string></value></params></methodname></methodcall></p></p></int></value></name></member></struct></value></params></methodresponse></string></value></int></value></int></value></string></value></int></value></value></string></value></string></value></string></value></params></methodname></methodcall></p></p></p></p></p></p></p></p></p></p>
