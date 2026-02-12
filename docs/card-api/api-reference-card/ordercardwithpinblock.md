---
title: OrderCardWithPinBlock
deprecated: false
hidden: false
metadata:
  robots: index
---
<!-- MIGRATION_METADATA
Migrated-From: https://developer.sprint.paymentology.com/card-api/api-reference/ordercardwithpinblock/
Source-Slug: ordercardwithpinblock
Migrated-On: 2026-02-12T18:11:17+00:00
Migrated-By: wp-readme-migration
-->

Order a card for a specific cardholder. You can choose this method if you want the PIN of the card printed on its card carrier or if you have Offline PIN validation in your country.

**IMPORTANT:** No commas, question marks or quotation marks are allowed in any of the fields.

### How it works

- Clients send the OrderCardWithPinBlock API request to Paymentology in Format 1 (using the key shared with them, which is the same key that is shared with the Card Manufacturer).

- Paymentology receives the API request and converts PIN block Format 1 to clear text PIN.

- Paymentology saves the details in the backend.

- Paymentology re-encrypts the clear text PIN into PIN block Format 0, this is then used in the PAN file sent to the Card Manufacturer.

- The Card Manufacturer then decrypts the PIN block as Format 0.

### Request details

#### Path parameters

| Parameter | type | Limits | required | Description |
| --- | --- | --- | --- | --- |
| terminalID | String | 10 characters | ✓ | The Paymentology issued terminal ID of the terminal requesting the transaction |
| campaignUUID | String | 1-35 characters | ✓ | Indicator for which campaign the card is to be ordered for |
| title | String | special - see description | ✓ | This field can be used to enter the person’s title (e.g. Mr / Ms / Mrs / Dr / etc). Field is required but can accept empty string.<br><br>(The combined value of title, initials and surname delimited with spaces should be maximum 20 characters.) |
| initials | String | special - see description | ✓ | This field can only contain alphabetic characters in UPPER CASE – no full stops are allowed between initials. Field is required but can accept empty string.<br><br>(The combined value of title, initials and surname delimited with spaces should be maximum 20 characters.) |
| lastName | String | special - see description | ✓ | This field can only be alphabetic characters in UPPER CASE – no full stops and/or special characters are allowed. In the case of -double barrel- surnames, such as FABER-SMITH we may have a hyphen between the two parts of the surname but without any spaces.<br><br>(The combined value of title, initials and surname delimited with spaces should be maximum 20 characters.)<br><br>Field is required but can accept empty string. |
| address1 | String | special - see description | ✓ | This is the first line of the address field which will be printed on a card mailer when required by the client – maximum length is 27 to 60 characters (Manufacturer dependent).<br><br>The field may not start (first character) with a comma, linefeed character, carriage return character, quotation marks or question mark.<br><br>Field is required but can accept empty string. |
| address2 | String | special - see description | ✓ | This is the second line of the address field which will be printed on a card mailer when required by the client – maximum length is 27 to 60 characters (Manufacturer dependent).<br><br>The field may not start (first character) with a comma, linefeed character, carriage return character, quotation marks or question mark. Field is required but can accept empty string. |
| address3 | String | special - see description | ✓ | This is the third line of the address field which will be printed on a card mailer when required by the client – maximum length is 27 to 60 characters (Manufacturer dependent).<br><br>The field may not start (first character) with a comma, linefeed character, carriage return character, quotation marks or question mark. Field is required but can accept empty string. |
| address4 | String | special - see description | ✓ | This is the fourth line of the address field which will be printed on a card mailer when required by the client – maximum length is 27 to 60 characters (Manufacturer dependent).<br><br>The field may not start (first character) with a comma, linefeed character, carriage return character, quotation marks or question mark. Field is required but can accept empty string. |
| address5 | String | special - see description | ✓ | This is the fifth line of the address field which will be printed on a card mailer when required by the client – maximum length is 27 to 60 characters (Manufacturer dependent).<br><br>The field may not start (first character) with a comma, linefeed character, carriage return character, quotation marks or question mark. Field is required but can accept empty string. |
| additionalData | String | special - see description | ✓ | Customer specific additional data. Format to be negotiated per client. Maximum length is 350 characters (Manufacturer dependent).This field should not contain comma or new line(LF/CF) characters . Field is required but can accept empty string. |
| pinBlock | String | special - see description | ✓ | Customer specific generated pin block.<br><br>Refer to [pinBlock PIN encryption](#pinencryption) to help perform the PIN encryption required. |
| transactionID | String | 1-255 characters | ✓ | A unique identifier generated by the client, which must not be duplicated over time. |
| transactionDate | Date |  | ✓ | Transaction date generated by the calling client |
| checksum | String |  | ✓ | HMAC-SHA256 hashed signature of the concatenated method name with all argument values using the terminal password as private key |

#### Code sample

```xml
<?xml version="1.0"?>
<methodCall>
  <methodName>OrderCardWithPinBlock</methodName>
  <params>
    <param>
      <value>
        <string>00134564</string>
      </value>
    </param>
<param>
      <value>
        <string>1234-5678-9087</string>
      </value>
    </param>
    <param>
      <value>
        <string>Miss</string>
      </value>
    </param>
    <param>
      <value>
        <string>MT</string>
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
        <string>12345</string>
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
```

<a id="pinencryption"></a>
#### pinBlock PIN encryption

The Java example snippet below is to be used to help perform the PIN encryption for the PIN that is to be inserted into the CardOrderWithPinBlock API request call.

- This is an example that encrypts the PIN using ISO Format 1.

- The key and PIN are removed from the main method.

- The code that takes a PIN and encrypts it using a key when you run it has the following values:

-

- String plainKey = “”;

- String pin = “”;

```java
package com.tutuka.cipher;

import org.apache.commons.codec.binary.Hex;

import javax.crypto.*;
import javax.crypto.spec.DESedeKeySpec;
import java.security.InvalidParameterException;
import java.security.Key;

public class PINEncryptExample {

    private static String formatPinBlock(String pin, int format) throws Exception {
        StringBuilder formattedPin = new StringBuilder();
        String dpb;
        byte[] anbValue;
        byte[] pinValue;
        byte[] dpbValue = new byte [8];
        int i=0;

        formattedPin.append(format);
        formattedPin.append(pin.length());
        formattedPin.append(pin);
        int count = 14 - pin.length();
        formattedPin.append(format == 0 ? new String(new char[count]).replace("\0", "F") : new String(new char[count]).replace("\0", "0"));

        pinValue = Hex.decodeHex(formattedPin.toString().toCharArray());

        anbValue = Hex.decodeHex("0000000000000000".toCharArray());
        for (byte b : pinValue) {
            dpbValue[i] = (byte) (b ^ anbValue[i++]);
        }

        dpb = Hex.encodeHexString(dpbValue);

        return dpb;
    }

    private static String getPinFromPinBlock(String dpb) throws Exception {
        byte[] dpbValue = Hex.decodeHex(dpb.toCharArray());
        byte[] anbValue = new byte[8];
        byte[] pinValue = new byte[8];
        int i = 0;

        anbValue = Hex.decodeHex("0000000000000000".toCharArray());
        for (byte b : dpbValue) {
            pinValue[i] = (byte) (b ^ anbValue[i++]);
        }

        String pinBlock = Hex.encodeHexString(pinValue);
        int len = Integer.parseInt(pinBlock.substring(1, 2)) + 2;
        String pin = pinBlock.substring(2, len);

        return pin;
    }

    public static String encode(String pin, String transformation, Key secKey) throws Exception {
        byte[] dpbValue = Hex.decodeHex(formatPinBlock(pin,1).toCharArray());

        Cipher encrypter = Cipher.getInstance(transformation);
        encrypter.init(Cipher.ENCRYPT_MODE, secKey);

        byte[] encrypted = encrypter.doFinal(dpbValue);

        return Hex.encodeHexString(encrypted).toUpperCase();
    }

    public static String decode(String epb, String transformation, Key secKey) throws Exception {
        byte[] epbValue = Hex.decodeHex(epb.toCharArray());

        Cipher decrypter = Cipher.getInstance(transformation);
        decrypter.init(Cipher.DECRYPT_MODE, secKey);

        byte[] decrypted = decrypter.doFinal(epbValue);

        return getPinFromPinBlock(Hex.encodeHexString(decrypted).toUpperCase());
    }

    public static void main(String args[]) throws Exception {
        String plainKey = ";
        String pin = ";
        String algorithm = "DESede";
        String transformation = "DESede/ECB/Nopadding";

        if(plainKey.length() != 32 && plainKey.length() != 48) throw new InvalidParameterException("the key argument needs to be either 32 or 48 characters");

        String fullKey = plainKey;
        if(plainKey.length() == 32) fullKey = plainKey + plainKey.substring(0, 16);

        byte[] keyValue = Hex.decodeHex(fullKey.toCharArray());
        DESedeKeySpec keySpec = new DESedeKeySpec(keyValue);
        SecretKey secKey = SecretKeyFactory.getInstance(algorithm).generateSecret(keySpec);

        String encryptedPin = encode(pin, transformation, secKey);

        System.out.println("Encrypted PIN: " + encryptedPin);

        String decrypted = decode(encryptedPin, transformation, secKey);

        System.out.println("Decrypted PIN: " + decrypted);

    }

}
```


---

### Response details

#### Response schema

| Parameter | type | Description |
| --- | --- | --- |
| terminalID | String | Echo |
| campaignUUID | String | Echo |
| title | String | Echo |
| initials | String | Echo |
| lastName | String | Echo |
| Address1 | String | Echo |
| Address2 | String | Echo |
| Address3 | String | Echo |
| Address4 | String | Echo |
| Address5 | String | Echo |
| additionalData | String | Echo |
| pinBlock | String | Echo |
| resultCode | Integer | Status code indicating transaction result |
| resultText | String | Status text indicating transaction result |

#### Code sample

```xml
<methodResponse>
    <params>
        <param>
            <value>
                <struct>
      <member>
                        <name>terminalID</name>
                        <value>
                            <string>00134564</string>
                        </value>
                    </member>
      <member>
                        <name>campaignUUID</name>
                        <value>
                            <string>1234-5678-9087</string>
                        </value>
                    </member>
                    <member>
                        <name>title</name>
                        <value>
                            <string>Miss</string>
                        </value>
                    </member>
                    <member>
                        <name>initials</name>
                        <value>
                            <string>MT</string>
                        </value>
                    </member>
                    <member>
                        <name>surname</name>
                        <value>
                            <string>Tutuka</string>
                        </value>
                    </member>
                    <member>
                        <name>address1</name>
                        <value>
                            <string>7 Plein</string>
                        </value>
                    </member>
                          <member>
                        <name>address2</name>
                        <value>
                            <string>Wanderers</string>
                        </value>
                    </member>
                    <member>
                        <name>address3</name>
                        <value>
                            <string>Johannesburg</string>
                        </value>
                    </member>
      <member>
                        <name>address4</name>
                        <value>
                            <string>2001</string>
                        </value>
                    </member>
                        <member>
                        <name>address5</name>
                        <value>
                            <string>South Africa</string>
                        </value>
                    </member>
                        <member>
                        <name>additionalData</name>
                        <value>
                            <string>1234567</string>
                        </value>
                    </member>
      <member>
                        <name>pinBlock</name>
                        <value>
                            <string>12345</string>
                        </value>
                    </member>
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

[Back to card API menu](./index)
