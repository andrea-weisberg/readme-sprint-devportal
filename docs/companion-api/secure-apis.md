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
*([RSA algorithm reference](https://simple.wikipedia.org/wiki/RSA_alogrithm))*

### session_key

Clients must create a 16-byte session key using `SecureRandom` (per standards) and encrypt it with the RSA public key.

AES-256 encryption (AES/CBC/PKCS5PADDING) is used to encrypt sensitive data (e.g. PIN, PAN, CVV2). This session key is generated per call and wrapped under the RSA KeyPair. This method is stronger than traditional Triple DES.
*([AES reference](https://simple.wikipedia.org/wiki/Advanced_Encryption_Standard))*

### Session-id Generation

1. Create a 32-byte random string → `session_key`
2. Encrypt `session_key` with `rsa_public` key → `Session-id`

### PIN Block Format

PIN Block Format ISO format 2 will be used to communicate the encrypted PIN block between the cardholder and Paymentology.

### IV

The IV (Initialization Vector) length depends on the encryption mode being used.

## Algorithm usage

### Protecting sensitive data

Details are protected using AES encryption as described above.

### Protecting keys (key wrapping)

When encrypting or decrypting keys, the proper terminology is *wrapping* and *unwrapping*. Specialized algorithms are used for this purpose.

#### Important notes

* If OAEP padding configuration is not explicitly set, it defaults to MGF1 with SHA-1 (which is insufficient).
* The hashing algorithm used in MGF1 should match the one used elsewhere. For Java JCE, you can use:

```java
new OAEPParameterSpec(
    "SHA-256",
    "MGF1",
    new MGF1ParameterSpec("SHA-256"),
    PSource.PSpecified.DEFAULT
);
```

* Use the **public key** to wrap (encrypt) a key.
* Use the **private key** to unwrap (decrypt) a key.
* Always specify `Cipher.SECRET_KEY` and the algorithm as `AES`.
* Public key format for transport: Base64 encoding of **X509** encoded data.
* Private key format: Base64 encoding of **PKCS8** encoded data.

*Code samples can be provided if needed.*

## API methods using card data encryption

> **REMINDER:** These API methods contain PCI sensitive information.

### Encrypted data in the **response**

The following methods return encrypted data and also return an `iv` element required for decryption:

* [GetActiveLinkedCards](https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/getactivelinkedcards/) — `cardNumber`, `cvv2`, `expiryDate`
* [GetCardDetails](https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/getcarddetails/) — `cardNumber`, `cvv2`, `expiryDate`
* [GetLinkedCards](https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/getlinkedcards/) — `cardNumber`, `cvv2`, `expiryDate`
* [UpdateCVV](https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/updatecvv/) — `cvv2`

### Encrypted data in the **request**

The following methods include encrypted data in the request, decrypted by the API using the provided `Session-id`:

* [ChangePin](https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/changepin/) — `newPin`
* [CreateLinkedCard](https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/createlinkedcard/) — `cardNumber`, `cvv2`, `expiryDate`
  *(Only if the campaign setting “Companion API Return Masked PAN for Create Methods” is set to false.)*

