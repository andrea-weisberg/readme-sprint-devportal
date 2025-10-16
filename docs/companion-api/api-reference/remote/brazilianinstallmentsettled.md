---
title: BrazilianInstallmentSettled
deprecated: false
hidden: false
metadata:
  robots: index
---
<p>Notifies that a Brazilian installment transaction is settled.</p>



\{/* spacing: desktop=20, mobile=10 */\}


#### Path parameters

| Parameter | Type | Limits | Required | Description |
|---|---|---|:--:|---|
| terminalID | String | 10 | ✓ | <p>The Paymentology issued terminal ID of the terminal requesting the transaction</p> |
| reference | String | 1-255 | ✓ | <p>The reference of the wallet that the installment transaction just got settled.</p> |
| referenceID | String | 1-255 | ✓ | <p>Transaction ID of the original authorisation that was settled.</p> |
| referenceDate | String |  | ✓ | <p>Transaction date of the original authorisation that was settled.</p> |
| totalInstallments | String | 2 | ✓ | <p>The total number of the installments linked to the installment transaction.</p> |
| installmentPaymentType | Integer |  | ✓ | <p>One of 403 (with interest), 407 (without interest), 488 (IATA), 410 (CrediDolar, specific for Banco Itau)</p> |
| installmentPaymentTotalAmount | Integer |  | ✓ | <p>The total amount of the transaction linked to the installment transaction in cents.</p> |
| installmentPaymentNumber | String | 2 | ✓ | <p>The current number of the installment that is being settled.</p> |
| installmentPaymentAmount | Integer |  | ✓ | <p>The amount of the installment that is being settled in cents.</p> |
| airportFeeAmount | Integer |  | ✓ | <p>The airport fee amount related to the installment that is being settled in cents.</p> |
| downPaymentAmount | Integer |  | ✓ | <p>The down payment amount related to the installment that is being settled in cents.</p> |
| checksum | String |  | ✓ | <p>HMAC-SHA256 hashed signature of the concatenated method name with all argument values using the terminal password as private key.</p> |



\{/* spacing: desktop=20, mobile=10 */\}



```xml
<?xml version="1.0"?>
<methodCall>
  <methodName>
    BrazilianInstallmentSettled
  </methodName>
  <params>
    <param>
      <value>
        <string>
          0097852049
        </string>
      </value>
    </param>
    <param>
      <value>
        <string>
          5a332769-264a-402c-851b-2d7a5ddb7bee
        </string>
      </value>
    </param>
    <param>
      <value>
        <string>
          117363249782
        </string>
      </value>
    </param>
    <param>
      <value>
        <dateTime.iso8601>
          20220223T03:48:27
        </dateTime.iso8601>
      </value>
    </param>
    <param>
      <value>
        <string>
          03
        </string>
      </value>
    </param>
    <param>
      <value>
        <int>
          403
        </int>
      </value>
    </param>
    <param>
      <value>
        <int>
          000000015000
        </int>
      </value>
    </param>
    <param>
      <value>
        <string>
          03
        </string>
      </value>
    </param>
    <param>
      <value>
        <int>
          000000005000
        </int>
      </value>
    </param>
    <param>
      <value>
        <int>
          000000000000
        </int>
      </value>
    </param>
    <param>
      <value>
        <int>
          000000000000
        </int>
      </value>
    </param>
    <param>
      <value>
        <string>
          346C246D7B79896C8507370CC449DEF4C23E447D
        </string>
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



{/* spacing: desktop=20, mobile=10 */}


#### Response schema

| Field | Type | Description |
|---|---|---|
| resultCode  | Integer | <p>Status code indicating transaction result</p> |



{/* spacing: desktop=20, mobile=10 */}



```xml
<?xml version="1.0"?>
<methodCall>
  <methodName>
    BrazilianInstallmentSettled
  </methodName>
  <params>
    <param>
      <value>
        <string>
          0097852049
        </string>
      </value>
    </param>
    <param>
      <value>
        <string>
          5a332769-264a-402c-851b-2d7a5ddb7bee
        </string>
      </value>
    </param>
    <param>
      <value>
        <string>
          117363249782
        </string>
      </value>
    </param>
    <param>
      <value>
        <dateTime.iso8601>
          20220223T03:48:27
        </dateTime.iso8601>
      </value>
    </param>
    <param>
      <value>
        <string>
          03
        </string>
      </value>
    </param>
    <param>
      <value>
        <int>
          403
        </int>
      </value>
    </param>
    <param>
      <value>
        <int>
          000000015000
        </int>
      </value>
    </param>
    <param>
      <value>
        <string>
          03
        </string>
      </value>
    </param>
    <param>
      <value>
        <int>
          000000005000
        </int>
      </value>
    </param>
    <param>
      <value>
        <int>
          000000000000
        </int>
      </value>
    </param>
    <param>
      <value>
        <int>
          000000000000
        </int>
      </value>
    </param>
    <param>
      <value>
        <string>
          346C246D7B79896C8507370CC449DEF4C23E447D
        </string>
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



\{/* spacing: desktop=20, mobile=10 */\}


<p><a class="btn btn--primary" href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/">back to remote api menu</a></p>
