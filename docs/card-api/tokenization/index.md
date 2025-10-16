---
title: Tokenization
deprecated: false
hidden: false
metadata:
  robots: index
---
<p><span style="font-weight: 400;">Tokenization is the process of substituting the card’s sensitive data, such as an account number, with non-sensitive, surrogate data, called a token. The PAN (Primary Account Number) is usually replaced with a unique string of numbers that acts as a secure reference to the card. </span></p>
<p><span style="font-weight: 400;">Only the token is provided when a payment transaction is initiated, without revealing the original card details. This desensitization greatly improves the security of transactions. </span></p>
<p><span style="font-weight: 400;">The Sprint platform allows you to take advantage of the tokenization technology—both by facilitating the provisioning of the cards and by providing control over the token lifecycle management process. With an existing virtual or physical card that has been issued by Paymentology, enabling card tokenization becomes easier.</span></p>
<p><span style="font-weight: 400;">So, tokenization mainly involves two key tasks:</span></p>
<ul>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;"><strong>Card provisioning</strong> – when a token is created for a full PAN.</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;"><strong>Token lifecycle management</strong> – when an event occurs on a token.</span></li>
</ul>



\{/* spacing: desktop=20, mobile=10 */\}


<h2><b>Benefits of Tokenization</b></h2>
<ul>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">Tokenizing customers’ private account data greatly enhances the security of transactions. A token has no meaningful value, if breached. </span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">It drives payment innovation on Paymentology’s Sprint platform, such as the adoption of digital wallet technology—like Apple Pay and Android Pay. These wallets store digital versions of payment cards, avoiding the need to carry physical cards. </span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">It creates smooth, secure, and fast customer payment experiences when making contactless payments or face-to-face payments. </span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">It simplifies attaining and maintaining compliance with the payment industry standards, which fosters customer loyalty and trust. </span></li>
</ul>



\{/* spacing: desktop=20, mobile=10 */\}


<h2><b>Terminology</b></h2>
<p><span style="font-weight: 400;">Here is a table describing the common phrases used in the tokenization process.</span></p>



\{/* spacing: desktop=20, mobile=10 */\}


\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"TERM"\},\{"c":"DEFINITION"\}],"caption":false,"body":[[\{"c":"TSP (Token Service Provider)"\},\{"c":"The TSP is the custodian of all token. It's responsible for token creation, token suspension, token resumption, token deletion, and token re-digitization."\}],[\{"c":"Token Vault"\},\{"c":"The TSP owned secure vault where tokens are stored along with their full PANs mapped to each token."\}],[\{"c":"Card provisioning "\},\{"c":"The process of a card being tokenized."\}],[\{"c":"Push provisioning"\},\{"c":"The cardholder pushes the card from their card app directly into a digitized wallet with a click of the button."\}],[\{"c":"Manual provisioning "\},\{"c":"The cardholder physically enters the card details into the digitized wallet."\}],[\{"c":"TAV (Token Authentication Value)"\},\{"c":"An encrypted value sent to MDES to verify that the card details exist and are valid. TAV is only used on Push provisioning."\}],[\{"c":"TER"\},\{"c":"Token Eligibility Request"\}],[\{"c":"Token Suspended"\},\{"c":"When a token is stopped"\}],[\{"c":"Token Resumed"\},\{"c":"When a token is unstopped"\}],[\{"c":"Token Deleted from Device"\},\{"c":"When a token has been deleted from a specific digital device."\}],[\{"c":"Token Deleted"\},\{"c":"Token has been deleted in it's entirety. The token cannot be retrieved ever again."\}],[\{"c":"Token Requester"\},\{"c":"An online merchant or digital wallet that requests a token to be provided for a transaction. Examples include M4Ms, Apple Pay, Samsung Pay, Google Pay and Garmin Pay"\}],[\{"c":"Digitized Wallet or Xpay"\},\{"c":"These include digital wallets such as M4Ms, Apple Pay, Samsung Pay, Google Pay and Garmin Pay"\}],[\{"c":"WID"\},\{"c":"The is the Wallet ID for the above-listed wallets/merchants. It is represented by a 3-digit numeric value"\}],[\{"c":"KLV (Key Length Value)"\},{"c":"Is a string of data that is passed onto clients through the Sprint API. The <i>key</i> identifies the data, <i>length</i> specifies the data's length, and <i>value</i> is the data itself."}]]}} */}
