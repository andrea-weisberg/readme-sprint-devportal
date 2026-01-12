---
title: Secure APIs
deprecated: false
hidden: false
metadata:
  robots: index
---
In the payment industry, sensitive data has real importance. Confidentiality of the sensitive data is important even while processing transactions and should be kept private (encrypted).

To achieve this, we offer Secure API methods to support end-to-end encryption of data.

> **IMPORTANT:** Specific campaign settings are required for these Secure APIs. To have these enabled, please reach out to your Client Executive or lodge a request via our [Customer Support Platform](https://support.paymentology.com/).

## Encryption details

Information related to card data (PAN, CVV2, PIN etc.) are sensitive and our Secure API methods are able to hide that information through encryption.

This encryption uses RSA and AES algorithms. RSA is an asymmetric key cryptography system that is used in this context to encrypt the AES key with the RSA public key, and to decrypt the AES key using the RSA private key.

### Encryption steps

1. Paymentology generates the RSA private/public key pair and associates it to a particular Terminal.
2. Paymentology shares the public key with the client via email.
3. The client generates an AES key (256-bit with AES/GCM/NoPadding cipher) and encrypts it using the provided RSA public key. The AES key is generated per session, typically on the cardholder device.
4. The client calls the relevant API method and includes the encrypted AES key in the HTTP header as `Session-id`, encoded as a base64 string.
5. Paymentology’s API decrypts the `Session-id` to obtain the AES key. Using it, depending on the API method, it will either:

   * Encrypt card sensitive data in the response and include the `iv` used to decrypt.
   * Decrypt card sensitive data in the request using the received `iv`.

## Keys

### RSA KeyPair

This is an RSA key of size 1024 (both `rsa_public` and `rsa_private`), generated using `java.security.KeyPairGenerator`.

RSA encryption is used for asymmetric encryption between the cardholder and Paymentology. This prevents intercept attacks and loss of sensitive data.
_([RSA algorithm reference](https://simple.wikipedia.org/wiki/RSA_alogrithm))_

### session_key

Clients must create a 16-byte session key using `SecureRandom` (per standards) and encrypt it with the RSA public key.

AES-256 encryption (AES/CBC/PKCS5PADDING) is used to encrypt sensitive data (e.g. PIN, PAN, CVV2). This session key is generated per call and wrapped under the RSA KeyPair. This method is stronger than traditional Triple DES.
_([AES reference](https://simple.wikipedia.org/wiki/Advanced_Encryption_Standard))_

### Session-id Generation

1. Create a 32-byte random string → `session_key`
2. Encrypt `session_key` with `rsa_public` key → `Session-id`

### PIN Block Format

PIN Block Format ISO format 2 will be used to communicate the encrypted PIN block between the cardholder and Paymentology.

### IV

The IV (Initialization Vector) length depends on the encryption mode being used.

## Algorithm used for protecting sensitive data

|                      Parameter                     |                                                      Value                                                      |
| :------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------: |
|                      Algorithm                     |                                                       AES                                                       |
|                  Key size options                  |                                               256 bits (32 bytes)                                               |
|                 Preferred key size                 |                                               256 bits (32 bytes)                                               |
|                   Transformation                   |                            AES/GCM/NoPadding (or AES/CBC/PKCS5Padding if considered)                            |
|                Additional parameters               |                                            Initialization vector (IV)                                           |
|   Initialization vector sizes (AES/GCM/NoPadding)  |                           The length of the IV key depends on the encryption mode used                          |
| Initialization vector sizes (AES/CBC/PKCS5Padding) |                           The length of the IV key depends on the encryption mode used                          |
|                 AES key generation                 | Preferred method is to use the Java `KeyGenerator` class; using only a random generator may result in weak keys |
|                    IV generation                   |                         Preferred method is to use Java `SecureRandom()` implementation                         |

<br />

## Algorithm used for protecting keys

When we talk about encrypting/decrypting keys the correct terminology is the wrapping or unwrapping of a key. There are algorithms that are specifically created for wrapping/unwrapping keys.

|                Parameter                |                                      Value                                     |
| :-------------------------------------: | :----------------------------------------------------------------------------: |
|                Algorithm                |                                       RSA                                      |
|             Key size options            |                           1024, 2048, 3072, 4096 bits                          |
|            Preferred key size           |                                    2048 bits                                   |
|             Transformations             | RSA/ECB/OAEPWithSHA-256AndMGF1Padding or RSA/ECB/OAEPWithSHA-512AndMGF1Padding |
| Additional parameters for the algorithm |            OAEP configuration, specified during wrapping/unwrapping            |
|          RSA keypair generation         |                         Use the Java `KeyPairGenerator`                        |

#### Important notes

* When not explicitly specified in the OAEP configuration the MGF1 padding will default to using SHA-1 which is not sufficient.
* It is important to specify the same hashing algorithm as is used by the rest of the algorithm when configuring OAEP. The following is an example of configuring OAEP (when using Java JCE):

```java
new OAEPParameterSpec(
    "SHA-256",
    "MGF1",
    new MGF1ParameterSpec("SHA-256"),
    PSource.PSpecified.DEFAULT
);
```

* When wrapping (encrypting) a key, it is important to use the public key.
* When unwrapping (decrypting) a key, it is important to use the private key.

In both cases the key type must be specified as Cipher.SECRET_KEY and the algorithm of the secret key as AES

* Format of public key for transport:  Base64 encoding of X509 encoded data.  The latter is important when parsing the key.
* Format of public key:  Base64 encoding of PKCS8 encoded data.  The latter is important for parsing the key.
  If possible and necessary, code samples can be provided.

## API methods using card data encryption

> **REMINDER:** These API methods contain PCI sensitive information.

### API methods with encrypted data in the response

The following API methods return encrypted data in the API response. Along with the encrypted data, they will also return an extra element `iv` that is needed by the calling code in order to decrypt the data:

* [GetActiveLinkedCards](https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/getactivelinkedcards/) — `cardNumber`, `cvv2`, and `expiryDate` will be encrypted in the response.
* [GetCardDetails](https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/getcarddetails/) — `cardNumber`, `cvv2`, and `expiryDate`will be encrypted in the response.
* [GetLinkedCards](https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/getlinkedcards/) — `cardNumber`, `cvv2`, and `expiryDate` will be encrypted in the response.
* [UpdateCVV](https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/updatecvv/) — `cvv2` will be encrypted in the response.

### API methods with encrypted data in the request

The following API methods will contain encrypted card data in the API request, the Companion API will decrypt the data using the provided Session-Id header:

* [ChangePin](https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/changepin/) — `newPin` will be encrypted in the request.
* [CreateLinkedCard](https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/createlinkedcard/) — `cardNumber`, `cvv2`, and `expiryDate` will be encrypted in the response. Note: this is only applicable if the campaign setting “Companion API Return Masked PAN for Create Methods” is set to  false.

<br />
