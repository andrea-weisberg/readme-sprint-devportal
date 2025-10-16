---
title: KLV Lookup
deprecated: false
hidden: false
metadata:
  robots: index
---
<p>Key-Length-value (KLV) is a data encoding standard where the <strong>Key</strong> identifies the data, <strong>Length</strong> specifies the data’s length and <strong>value </strong>is the data itself. KLV is an instance of the TLV encoding scheme used for optional information element within communication protocols.</p>
<p><strong>The length of each string is:</strong></p>
<ol>
<li>A Key indicator of 3 digits, zero left padded.</li>
<li>A Length indicator of 2 digits, zero left padded.</li>
<li>A value with the number of characters as specified by the Length indicator.</li>
</ol>
<p><strong>It is important to note:</strong></p>
<ul>
<li>Keys do not need to be in any particular order or sequence within transactionData.</li>
<li>Customers must be able to receive all keys available within transactionData,</li>
<li>Customers may ignore keys not pertinent to processing.</li>
<li>You must be able to successfully process messages that contain new unannounced keys.</li>
<li>Available keys are subject to change and will often be customer specific, thus these will be communicated via means other than this API documentation.<br >
For example, the KLV 00206AB48DE026044577 contains:<br >
1. Key 002 with length 06 and value AB48DE<br >
2. Key 026 with length 04 and value 4577</li>
<li>Transactions may or may not contain keys depending on the type of transactions.</li>
<li>Transaction types which include KLV data are:<br >
<a href="https:developer.sprint.paymentology.com/companion-api/api-reference/remote/balance/">Balance</a><br >
<a href="https:developer.sprint.paymentology.com/companion-api/api-reference/remote/#Deduct">Deduct</a><br >
<a href="https:developer.sprint.paymentology.com/companion-api/api-reference/remote/#DeductAdjustment">Deduct Adjustment</a><br >
<a href="https:developer.sprint.paymentology.com/companion-api/api-reference/remote/#LoadAuth">Load Auth</a><br >
<a href="https:developer.sprint.paymentology.com/companion-api/api-reference/remote/loadauthreversal/">Load Auth Reversal</a><br >
<a href="https:developer.sprint.paymentology.com/companion-api/api-reference/remote/#LoadAdjustment">Load Adjustment</a><br >
<a href="https:developer.sprint.paymentology.com/companion-api/api-reference/remote/#Stop">Stop</a></li>
<li>Tokenisation<br >
<a href="https:developer.sprint.paymentology.com/companion-api/api-reference/remote/#AdministrativeMessage">Administrative</a><strong><a href="https:developer.sprint.paymentology.com/companion-api/api-reference/remote/#AdministrativeMessage"> Message</a></strong></li>
<li>3DSecure<br >
<a href="https:developer.sprint.paymentology.com/companion-api/api-reference/remote/administrativemessage/#3DSecure">3DSecureOTP</a><br >
<a href="https:developer.sprint.paymentology.com/companion-api/api-reference/remote/administrativemessage/#3DSAppAuth">3DSecureAppAuthentication</a></p>
<ul className="ak-ul" data-indent-level="2">
<li>
<p data-renderer-start-pos="2119">original transaction amount</p>
</li>
<li>
<p data-renderer-start-pos="2150">original currency code</p>
</li>
<li>
<p data-renderer-start-pos="2176">merchant description</p>
</li>
</ul>
</li>
<li>
<p data-renderer-start-pos="2176"><a href="https:developer.sprint.paymentology.com/companion-api/api-reference/remote/administrativemessage/#3DSAppFinal">3DSecureAppFinalisation</a></p>
<ul>
<li style={{listStyleType: "none"}}>
<ul className="ak-ul" data-indent-level="2">
<li>
<p data-renderer-start-pos="2229">status</p>
</li>
</ul>
</li>
</ul>
</li>
</ul>

</p></li></ul></li></ul></a></p></li></p></li></p></li></p></li></ul></a></a></li></a></strong></a></li></a></a></a></a></a></a></a></li></li></li></li></li></li></li></ul></strong></p></li></li></li></ol></strong></p></strong></strong></strong></p>
