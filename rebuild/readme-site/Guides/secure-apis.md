# Secure APIs

In the payment industry sensitive data has a real importance. Confidentiality of the sensitive data is important even while processing transactions and should be kept private (encrypted).

To achieve this we offer Secure API methods to support end to end encryption of data.

IMPORTANT: Specific campaign settings are required for these Secure API's. To have these enabled, please reach out to your Client Executive or lodge a request via our [Customer Support Platform](https://support.paymentology.com/).

## Encryption details

Information related to card data (PAN, CVV2, PIN etc.) are sensitive and our Secure API methods are able to hide that information through encryption.

This encryption uses RSA and AES algorithm. RSA is an asymmetric key crytography system that is used in this context to encrypt the AES key with the RSA public key, and to decrypt the AES key using the RSA private key.

### Encryption steps

- Paymentology generates the RSA private/public key pair and associates it to a particular Terminal.

- Paymentology shares to the client the public key, via email.

- The client generates an AES key (256 bits key with AES/GCM/NoPadding cipher) and encrypts it using the public RSA key provided to them. The AES key is generated on a per-session basis, on the cardholder device if that’s the device that’s going to read the encrypted data.

- The client calls the relevant API method and includes the encrypted AES key in the HTTP header as Session-Id, encoded as a base64 string.

- Paymentology’s API decrypts the Session-Id value to get the AES key and using it, depending on the API method, it will either: encrypt card sensitive data in the response, adding the iv used to decrypt.

- decrypt card sensitive data from the received request, based on the iv received alongside the encrypted data.

## Keys

### RSA KeyPair

This is RSA key of size 1024 each (rsa_public and rsa_private).

It’s generated using java.security KeyPairGenerator in java.

RSA Encryption will be used for asymmetric Encryption between Cardholder and Paymentology. This will prevent any intercept attacks and loss of sensitive data.
(https://simple.wikipedia.org/wiki/RSA_alogrithm)

### session_key

Client need to create 16 bytes session key using SECURERANDOM (as per standard) and encrypt it with RSA public key.

AES 256 Encryption (AES/CBC/PKCS5PADDING) will be used for Encryption of the Sensitive data e.g. PIN, PAN, and CVV2. This will be a random key generated for each call and shared under the RSA Key Pair, stronger than conventional Triple DES algorithm. (https://simple.wikipedia.org/wiki/Advanced_Encryption_Standard)

### Session-Id Generation

- Create a 32 bytes length random string -> session_key

- Encrypt session_key with rsa_public Key -> Session-Id

### PIN Block Format

PIN BLOCK Format ISO format 2 will be used to communicate the encrypted PIN block to and from the cardholder to Paymentology.

### IV

The length of IV key will be dependent on the mode of encryption used.

### Important notes

- When not explicitly specified in the OAEP configuration the MGF1 padding will default to using SHA-1 which is not sufficient.

- It is important to specify the same hashing algorithm as is used by the rest of the algorithm when configuring OAEP. The following is an example of configuring OAEP (when using Java JCE):

new OAEPParameterSpec(
"SHA-256",
"MGF1",
new MGF1ParameterSpec("SHA-256"),
PSource.PSpecified.DEFAULT
);

- When wrapping (encrypting) a key, it is important to use the public key.

- When unwrapping (decrypting) a key, it is important to use the private key.

In both cases the key type must be specified as Cipher.SECRET_KEY and the algorithm of the secret key as AES.

- Format of public key for transport: Base64 encoding of X509 encoded data. The latter is important when parsing the key.

- Format of public key: Base64 encoding of PKCS8 encoded data. The latter is important for parsing the key.

If possible and necessary, code samples can be provided.

### Algorithm used for protecting sensitive data

### Algorithm used for protecting keys

When we talk about encrypting/decrypting keys the correct terminology is the wrapping or unwrapping of a key. There are algorithms that are specifically created for wrapping/unwrapping keys.

## API methods using card data encryption

REMINDER: These API methods contain PCI sensitive information.

### API methods with encrypted data in the response

The following API methods return encrypted data in the API response. Along with the encrypted data, they will also return an extra element iv that is needed by the calling code in order to decrypt the data:

- [GetActiveLinkedCards](/api-reference/companion-api/getactivelinkedcards) - cardNumber, cvv2 and expiryDate will be encrypted in the response.

- [GetCardDetails](/api-reference/companion-api/getcarddetails) - cardNumber, cvv2 and expiryDate will be encrypted in the response.

- [GetLinkedCards](/api-reference/companion-api/getlinkedcards) - cardNumber, cvv2 and expiryDate will be encrypted in the response.

- [UpdateCVV](/api-reference/companion-api/updatecvv) - cvv2 will be encrypted in the response.

### API methods with encrypted data in the request

The following API methods will contain encrypted card data in the API request, the Companion API will decrypt the data using the provided Session-Id header:

- [ChangePin](/api-reference/companion-api/changepin) - newPin will be encrypted in the request.

- [CreateLinkedCard](/api-reference/companion-api/createlinkedcard) - cardNumber, cvv2 and expiryDate will be encrypted in the response. Note: this is only applicable if the campaign setting "Companion API Return Masked PAN for Create Methods" is set to false.
