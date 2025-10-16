---
title: Secure APIs
deprecated: false
hidden: false
metadata:
  robots: index
original_path: companion-api
---
<p>In the payment industry sensitive data has a real importance. Confidentiality of the sensitive data is important even while processing transactions and should be kept private (encrypted).</p>
<p>To achieve this we offer Secure API methods to support end to end encryption of data.</p>
<p><span style="color: #ff0000;"><strong>IMPORTANT:</strong></span> <span style="color: #000000;">Specific campaign settings are required for these Secure API’s. To have these enabled, please reach out to your Client Executive or lodge a request via our <a href="https://support.paymentology.com/">Customer Support Platform</a>.</span></p>



\{/* spacing: desktop=20, mobile=10 */\}


<h2>Encryption details</h2>
<p>Information related to card data (PAN, CVV2, PIN etc.) are sensitive and our Secure API methods are able to hide that information through encryption.</p>
<p>This encryption uses RSA and AES algorithm. RSA is an asymmetric key crytography system that is used in this context to encrypt the AES key with the RSA public key, and to decrypt the AES key using the RSA private key.</p>



\{/* spacing: desktop=20, mobile=10 */\}


<h3>Encryption steps</h3>
<ol>
<li>Paymentology generates the RSA private/public key pair and associates it to a particular Terminal.</li>
<li>
<p data-renderer-start-pos="775">Paymentology shares to the client the public key, via email.</p>
</li>
<li>
<p data-renderer-start-pos="838">The client generates an AES key (256 bits key with AES/GCM/NoPadding cipher) and encrypts it using the public RSA key provided to them. The AES key is generated on a per-session basis, on the cardholder device if that’s the device that’s going to read the encrypted data.</p>
</li>
<li>
<p data-renderer-start-pos="1113">The client calls the relevant API method and includes the encrypted AES key in the HTTP header as Session-Id, encoded as a base64 string.</p>
</li>
<li>
<p data-renderer-start-pos="1254">Paymentology’s API decrypts the Session-Id value to get the AES key and using it, depending on the API method, it will either:</p>
<ul class="ak-ul" data-indent-level="2">
<li>
<p data-renderer-start-pos="1384">encrypt card sensitive data in the response, adding the <code class="code cc-1o5d2cw" data-renderer-mark="true">iv</code> used to decrypt.</p>
</li>
<li>
<p data-renderer-start-pos="1462">decrypt card sensitive data from the received request, based on the <code class="code cc-1o5d2cw" data-renderer-mark="true">iv</code> received alongside the encrypted data.</p>
</li>
</ul>
</li>
</ol>



\{/* spacing: desktop=20, mobile=10 */\}


<h2>Keys</h2>
<h3>RSA KeyPair</h3>
<p>This is RSA key of size 1024 each (rsa_public and rsa_private).</p>
<p>It’s generated using java.security KeyPairGenerator in java.</p>
<p>RSA Encryption will be used for asymmetric Encryption between Cardholder and Paymentology. This will prevent any intercept attacks and loss of sensitive data.<br />
<em>(https://simple.wikipedia.org/wiki/RSA_alogrithm)</em></p>
<h3>session_key</h3>
<p>Client need to create 16 bytes session key using SECURERANDOM (as per standard) and encrypt it with RSA public key.</p>
<p>AES 256 Encryption (AES/CBC/PKCS5PADDING) will be used for Encryption of the Sensitive data e.g. PIN, PAN, and CVV2.  This will be a random key generated for each call and shared under the RSA Key Pair, stronger than conventional Triple DES algorithm. <em>(https://simple.wikipedia.org/wiki/Advanced_Encryption_Standard)</em></p>
<h3>Session-Id Generation</h3>
<ol>
<li>Create a 32 bytes length random string -> session_key</li>
<li>Encrypt session_key with rsa_public Key -> Session-Id</li>
</ol>
<h3>PIN Block Format</h3>
<p>PIN BLOCK Format ISO format 2 will be used to communicate the encrypted PIN block to and from the cardholder to Paymentology.</p>
<h3>IV</h3>
<p>The length of IV key will be dependent on the mode of encryption used.</p>



<h3>Algorithm used for protecting sensitive data</h3>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":""\},\{"c":""\}],"caption":false,"body":[[\{"c":"Algorithm"\},\{"c":"AES"\}],[\{"c":"Key size options"\},\{"c":"256 bits (32 bytes)"\}],[\{"c":"Preferred key size"\},\{"c":"256 bits (32 bytes)"\}],[\{"c":"Transformation"\},\{"c":"AES/GCM/NoPadding (or AES/CBC/PKCS5Padding if considered)"\}],[\{"c":"Additional parameters"\},\{"c":"Initialization vector (IV)"\}],[\{"c":"Initialization vector sizes (AES/GCM/NoPadding)"\},\{"c":"The length of IV key will be dependent on the mode of encryption used."\}],[\{"c":"Initialization vector sizes (AES/CBC/PKCS5Padding)"\},\{"c":"The length of IV key will be dependent on the mode of encryption used."\}],[\{"c":"AES key generation"\},\{"c":"Preferred method is to use Java KeyGenerator class, doing it with only a random generator may result in weak keys."\}],[\{"c":"IV generation"\},\{"c":"Preferred method is to use Java SecureRandom() implementation."\}]]}} */}


<h3>Algorithm used for protecting keys</h3>
<p>When we talk about encrypting/decrypting keys the correct terminology is the wrapping or unwrapping of a key. There are algorithms that are specifically created for wrapping/unwrapping keys.</p>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":""\},\{"c":""\}],"caption":false,"body":[[\{"c":"Algorithm"\},\{"c":"RSA"\}],[\{"c":"Key size options"\},\{"c":"1024, 2048, 3072, 4096 bits."\}],[\{"c":"Preferred key size"\},\{"c":"2048 bits"\}],[\{"c":"Transformations"\},\{"c":"RSA/ECB/OAEPWithSHA-256AndMGF1Padding or RSA/ECB/OAEPWithSHA-512AndMGF1Padding."\}],[\{"c":"Additional parameters for the algorithm"\},\{"c":"OAEP configuration. Specified during wrapping/unwrapping."\}],[\{"c":"RSA keypair generation"\},\{"c":"Use Java KeyPairGenerator."\}]]}} */}


<h3>Important notes</h3>
<ul>
<li>When not explicitly specified in the OAEP configuration the MGF1 padding will default to using SHA-1 which is not sufficient.</li>
<li>It is important to specify the same hashing algorithm as is used by the rest of the algorithm when configuring OAEP. The following is an example of configuring OAEP (when using Java JCE):</li>
</ul>

```java
new OAEPParameterSpec(
    "SHA-256",
    "MGF1",
    new MGF1ParameterSpec("SHA-256"),
    PSource.PSpecified.DEFAULT
);

```

<ul>
<li>When wrapping (encrypting) a key, it is important to use the public key.</li>
<li>When unwrapping (decrypting) a key, it is important to use the private key.</li>
</ul>
<p>In both cases the key type must be specified as Cipher.SECRET_KEY and the algorithm of the secret key as AES.</p>
<ul>
<li>Format of public key for transport:  Base64 encoding of X509 encoded data.  The latter is important when parsing the key.</li>
<li>Format of public key:  Base64 encoding of PKCS8 encoded data.  The latter is important for parsing the key.</li>
</ul>
<p>If possible and necessary, code samples can be provided.</p>



{/* spacing: desktop=20, mobile=10 */}


<h2>API methods using card data encryption</h2>
<p><span style="color: #ff0000;"><strong>REMINDER:</strong></span> <span style="color: #000000;">These API methods contain PCI sensitive information.</span></p>
<h3>API methods with encrypted data in the response</h3>
<p>The following API methods return encrypted data in the API response. Along with the encrypted data, they will also return an extra element <code class="code cc-1o5d2cw" data-renderer-mark="true">iv</code> that is needed by the calling code in order to decrypt the data:</p>
<ul>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/getactivelinkedcards/">GetActiveLinkedCards</a> – <code class="code cc-1o5d2cw" data-renderer-mark="true">cardNumber</code>, <code class="code cc-1o5d2cw" data-renderer-mark="true">cvv2</code> and  <code class="code cc-1o5d2cw" data-renderer-mark="true">expiryDate</code> will be encrypted in the response.</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/getcarddetails/">GetCardDetails</a> – <code class="code cc-1o5d2cw" data-renderer-mark="true">cardNumber</code>, <code class="code cc-1o5d2cw" data-renderer-mark="true">cvv2</code> and  <code class="code cc-1o5d2cw" data-renderer-mark="true">expiryDate</code> will be encrypted in the response.</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/getlinkedcards/">GetLinkedCards</a> –  <code class="code cc-1o5d2cw" data-renderer-mark="true">cardNumber</code>, <code class="code cc-1o5d2cw" data-renderer-mark="true">cvv2</code> and  <code class="code cc-1o5d2cw" data-renderer-mark="true">expiryDate</code> will be encrypted in the response.</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/updatecvv/">UpdateCVV</a> –  <code class="code cc-1o5d2cw" data-renderer-mark="true">cvv2</code>  will be encrypted in the response.</li>
</ul>
<h3>API methods with encrypted data in the request</h3>
<p>The following API methods will contain encrypted card data in the API request, the Companion API will decrypt the data using the provided Session-Id header:</p>
<ul>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/changepin/">ChangePin</a> – <code class="code cc-1o5d2cw" data-renderer-mark="true">newPin</code> will be encrypted in the request.</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/createlinkedcard/">CreateLinkedCard</a> – <code class="code cc-1o5d2cw" data-renderer-mark="true">cardNumber</code>, <code class="code cc-1o5d2cw" data-renderer-mark="true">cvv2</code> and  <code class="code cc-1o5d2cw" data-renderer-mark="true">expiryDate</code> will be encrypted in the response. Note: this is only applicable if the campaign setting “Companion API Return Masked PAN for Create Methods” is set to  false.</li>
</ul>



{/* spacing: desktop=20, mobile=10 */}
