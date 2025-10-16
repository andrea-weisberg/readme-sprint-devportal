---
title: OrderCard
deprecated: false
hidden: false
metadata:
  robots: index
---
<p>Order a card for a specific cardholder. A card can be printed with cardholder details by the card manufacturer. No commas, question marks or quotation marks are allowed in any of the fields</p>

#### Path parameters

| Parameter | Type | Limits | Required | Description |
|---|---|---|:--:|---|
| terminalID | String | 10 characters | ✓ | <p>The Paymentology issued terminal ID of the terminal requesting the transaction</p> |
| title | String | special - see description | ✓ | <p>This field can be used to enter the person’s title (e.g. Mr / Ms / Mrs / Dr / etc). Field is required but can accept empty string.</p> <p>(The combined value of title, initials and surname delimited with spaces should be maximum 20 characters.)</p> |
| initials | String | special - see description | ✓ | <p>This field can only contain alphabetic characters in UPPER CASE – no full stops are allowed between initials. Field is required but can accept empty string.</p> <p>(The combined value of title, initials and surname delimited with spaces should be maximum 20 characters.)</p> |
| lastName | String | special - see description | ✓ | <p>This field can only be alphabetic characters in UPPER CASE – no full stops and/or special characters are allowed. In the case of -double barrel- surnames, such as FABER-SMITH we may have a hyphen between the two parts of the surname but without any spaces.</p> <p>(The combined value of title, initials and surname delimited with spaces should be maximum 20 characters.)<br /> Field is required but can accept empty string.</p> |
| address1 | String | special - see description | ✓ | <p>This is the first line of the address field which will be printed on a card mailer when required by the client – maximum length is 27 to 60 characters (Manufacturer dependent).</p> <p>The field may not start (first character) with a comma, linefeed character, carriage return character, quotation marks or question mark.<br /> Field is required but can accept empty string.</p> |
| address2 | String | special - see description | ✓ | <p>This is the second line of the address field which will be printed on a card mailer when required by the client – maximum length is 27 to 60 characters (Manufacturer dependent).</p> <p>The field may not start (first character) with a comma, linefeed character, carriage return character, quotation marks or question mark. Field is required but can accept empty string.</p> |
| address3 | String | special - see description | ✓ | <p>This is the third line of the address field which will be printed on a card mailer when required by the client – maximum length is 27 to 60 characters (Manufacturer dependent).</p> <p>The field may not start (first character) with a comma, linefeed character, carriage return character, quotation marks or question mark. Field is required but can accept empty string.</p> |
| address4 | String | special - see description | ✓ | <p>This is the fourth line of the address field which will be printed on a card mailer when required by the client – maximum length is 27 to 60 characters (Manufacturer dependent).</p> <p>The field may not start (first character) with a comma, linefeed character, carriage return character, quotation marks or question mark. Field is required but can accept empty string.</p> |
| address5 | String | special - see description | ✓ | <p>This is the fifth line of the address field which will be printed on a card mailer when required by the client – maximum length is 27 to 60 characters (Manufacturer dependent).</p> <p>The field may not start (first character) with a comma, linefeed character, carriage return character, quotation marks or question mark. Field is required but can accept empty string.</p> |
| additionalData | String | special - see description | ✓ | <p>Customer specific additional data. Format to be negotiated per client. Maximum length is 350 characters (Manufacturer dependent).This field should not contain comma or new line(LF/CF) characters . Field is required but can accept empty string.</p> |
| transactionID | String | 1-255 characters | ✓ | <p>Client generated Transaction ID to assist in identify transactions on the client side</p> |
| transactionDate | Date |  | ✓ | <p>Client generated / local Transaction Date to assist in identifying transactions on the client side</p> |
| checksum | String |  | ✓ | <p>HMAC-SHA256 hashed signature of the concatenated method name with all argument values using the terminal password as private key</p> |

```xml
<?xml version=""1.0""?>
<methodCall>
  <methodName>OrderCard</methodName>
  <params>
    <param>
      <value>
        <string>0014682067</string>
      </value>
    </param>
    <param>
      <value>
        <string>Miss</string>
      </value>
    </param>
    <param>
      <value>
        <string>Tester</string>
      </value>
    </param>
    <param>
      <value>
        <string>Tutuka</string>
      </value>
    </param>
    <param>
      <value>
        <string>7 Plein</string>
      </value>
    </param>
    <param>
      <value>
        <string>Wanderers</string>
      </value>
    </param>
    <param>
      <value>
        <string>Johannesburg</string>
      </value>
    </param>
    <param>
      <value>
        <string>2001</string>
      </value>
    </param>
    <param>
      <value>
        <string>South Africa</string>
      </value>
    </param>
    <param>
      <value>
        <string>test123</string>
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
        <string>47E71AB6DD2D292A585399BAF8757E1352DBAA64</string>
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

<p> </p>

#### Response schema

| Field | Type | Description |
|---|---|---|
| resultCode | Integer | <p>Status code indicating transaction result</p> |

```xml
<?xml version=""1.0""?>
<methodCall>
  <methodName>OrderCard</methodName>
  <params>
    <param>
      <value>
        <string>0014682067</string>
      </value>
    </param>
    <param>
      <value>
        <string>Miss</string>
      </value>
    </param>
    <param>
      <value>
        <string>Tester</string>
      </value>
    </param>
    <param>
      <value>
        <string>Tutuka</string>
      </value>
    </param>
    <param>
      <value>
        <string>7 Plein</string>
      </value>
    </param>
    <param>
      <value>
        <string>Wanderers</string>
      </value>
    </param>
    <param>
      <value>
        <string>Johannesburg</string>
      </value>
    </param>
    <param>
      <value>
        <string>2001</string>
      </value>
    </param>
    <param>
      <value>
        <string>South Africa</string>
      </value>
    </param>
    <param>
      <value>
        <string>test123</string>
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
        <string>47E71AB6DD2D292A585399BAF8757E1352DBAA64</string>
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

<p> </p>

<p><a class="btn btn--primary" href="https://developer.sprint.paymentology.com/card-api/profile-api-reference/">Back to Profile API Reference</a></p>
