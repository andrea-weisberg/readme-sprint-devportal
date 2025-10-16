---
title: Response Codes – Remote API
deprecated: false
hidden: false
metadata:
  robots: index
---

<h2>Important</h2>
<p>Any argument that has the type <span class="xml-highlight">date</span> needs to follow the XML-RPC specified ISO 8601 date-time format: <dateTime.iso8601>YYYYMMDDTHH:mm:ss<dateTime.iso8601></p>

<p>Any transaction amount is represented as its cent value; therefore an integer rather than a decimal.</p>
<ul>
<li>R100.50 is therefore represented as 10050 rand cents.</li>
<li>$10.50 is therefore represented as 1050 dollar cents.</li>
</ul>

<p>KLV: A type of TLV encoded string with characteristics:</p>
<ol>
<li>A Key indicator of 3 digits, zero left padded.</li>
<li>A Length indicator of 2 digits, zero left padded.</li>
<li>A Value with the number of characters as specified by the Length indicator.</li>
</ol>
<h3>It is important to note:</h3>
<ul>
<li>Transactions may or may not contain keys depending on the type of transactions</li>
<li>Keys do not need to be in any particular order or sequence within <span class="xml-highlight">transactionData</span></li>
<li>Customers must be able to receive all keys available within <span class="xml-highlight">transactionData</span></li>
<li>Customers may ignore keys not pertinent to processing.</li>
<li>You must be able to successfully process messages that contain new unannounced keys.</li>
<li>Available keys are subject to change and will often be customer specific, thus these will be communicated via means other than this API documentation.</li>
</ul>
<p>For example the KLV <b>01206AB48DE003044577</b> contains:</p>
<ol>
<li>Key 012 with length 06 and value AB48DE</li>
<li>Key 003 with length 04 and value 4577</li>
</ol>
<p>Please refer to the lookup table for the available values.</p>

<h2>Matching response codes</h2>
<p>You can refer to the <a href="https://developer.sprint.paymentology.com/response-codes-2/response-and-action-code-mapping/">Response and action code mapping table</a> to understand how Remote API Response Codes map to different networks.</p>
</a></p></h2></p></li></li></ol></b></p></li></li></li></span></li></span></li></li></ul></h3></li></li></li></ol></p></li></li></ul></p></span></p></h2>
