---
title: Tokenization
deprecated: false
hidden: false
metadata:
  robots: index
---
<p><span style={{fontWeight: "400"}}>Tokenization is the process of substituting the card’s sensitive data, such as an account number, with non-sensitive, surrogate data, called a token. The PAN (Primary Account Number) is usually replaced with a unique string of numbers that acts as a secure reference to the card. </span></p>
<p><span style={{fontWeight: "400"}}>Only the token is provided when a payment transaction is initiated, without revealing the original card details. This desensitization greatly improves the security of transactions. </span></p>
<p><span style={{fontWeight: "400"}}>The Sprint platform allows you to take advantage of the tokenization technology—both by facilitating the provisioning of the cards and by providing control over the token lifecycle management process. With an existing virtual or physical card that has been issued by Paymentology, enabling card tokenization becomes easier.</span></p>
<p><span style={{fontWeight: "400"}}>So, tokenization mainly involves two key tasks:</span></p>

<ul>
  <li style={{fontWeight: "400"}} aria-level="1"><span style={{fontWeight: "400"}}><strong>Card provisioning</strong> – when a token is created for a full PAN.</span></li>
  <li style={{fontWeight: "400"}} aria-level="1"><span style={{fontWeight: "400"}}><strong>Token lifecycle management</strong> – when an event occurs on a token.</span></li>
</ul>

<h2><b>Benefits of Tokenization</b></h2>

<ul>
  <li style={{fontWeight: "400"}} aria-level="1"><span style={{fontWeight: "400"}}>Tokenizing customers’ private account data greatly enhances the security of transactions. A token has no meaningful value, if breached. </span></li>
  <li style={{fontWeight: "400"}} aria-level="1"><span style={{fontWeight: "400"}}>It drives payment innovation on Paymentology’s Sprint platform, such as the adoption of digital wallet technology—like Apple Pay and Android Pay. These wallets store digital versions of payment cards, avoiding the need to carry physical cards. </span></li>
  <li style={{fontWeight: "400"}} aria-level="1"><span style={{fontWeight: "400"}}>It creates smooth, secure, and fast customer payment experiences when making contactless payments or face-to-face payments. </span></li>
  <li style={{fontWeight: "400"}} aria-level="1"><span style={{fontWeight: "400"}}>It simplifies attaining and maintaining compliance with the payment industry standards, which fosters customer loyalty and trust. </span></li>
</ul>

<h2><b>Terminology</b></h2>
<p><span style={{fontWeight: "400"}}>Here is a table describing the common phrases used in the tokenization process.</span></p>

<br />

<table>
  <thead>
    <tr>
      <th align="center">TERM</th>
      <th align="center">DEFINITION</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td align="center">TSP (Token Service Provider)</td>

      <td>
        The TSP is the custodian of all tokens. It is responsible for token
        creation, suspension, resumption, deletion, and re-digitization.
      </td>
    </tr>

    <tr>
      <td align="center">Token Vault</td>

      <td>
        The TSP-owned secure vault where tokens are stored along with their full
        PANs mapped to each token.
      </td>
    </tr>

    <tr>
      <td align="center">Card provisioning</td>
      <td>The process of a card being tokenized.</td>
    </tr>

    <tr>
      <td align="center">Push provisioning</td>

      <td>
        The cardholder pushes the card from their card app directly into a
        digitized wallet with the click of a button.
      </td>
    </tr>

    <tr>
      <td align="center">Manual provisioning</td>

      <td>
        The cardholder physically enters the card details into the digitized
        wallet.
      </td>
    </tr>

    <tr>
      <td align="center">TAV (Token Authentication Value)</td>

      <td>
        An encrypted value sent to MDES to verify that the card details exist and
        are valid. TAV is only used for push provisioning.
      </td>
    </tr>

    <tr>
      <td align="center">TER</td>
      <td>Token Eligibility Request.</td>
    </tr>

    <tr>
      <td align="center">Token Suspended</td>
      <td>When a token is stopped.</td>
    </tr>

    <tr>
      <td align="center">Token Resumed</td>
      <td>When a token is unstopped.</td>
    </tr>

    <tr>
      <td align="center">Token Deleted from Device</td>

      <td>
        When a token has been deleted from a specific digital device.
      </td>
    </tr>

    <tr>
      <td align="center">Token Deleted</td>

      <td>
        The token has been deleted in its entirety and cannot be retrieved again.
      </td>
    </tr>

    <tr>
      <td align="center">Token Requester</td>

      <td>
        An online merchant or digital wallet that requests a token for a
        transaction. Examples include M4Ms, Apple Pay, Samsung Pay, Google Pay,
        and Garmin Pay.
      </td>
    </tr>

    <tr>
      <td align="center">Digitized Wallet or Xpay</td>

      <td>
        Digital wallets such as M4Ms, Apple Pay, Samsung Pay, Google Pay, and
        Garmin Pay.
      </td>
    </tr>

    <tr>
      <td align="center">WID</td>

      <td>
        The Wallet ID for supported wallets or merchants, represented by a
        3-digit numeric value.
      </td>
    </tr>

    <tr>
      <td align="center">KLV (Key Length Value)</td>

      <td>
        A string of data passed to clients through the Sprint API. The key
        identifies the data, the length specifies the data length, and the value
        is the data itself.
      </td>
    </tr>
  </tbody>
</table>
