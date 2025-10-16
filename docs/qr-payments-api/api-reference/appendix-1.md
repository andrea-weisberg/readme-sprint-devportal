---
title: Appendix
deprecated: false
hidden: false
metadata:
  robots: index
original_path: qr-payments-api/api-reference
---
<p><a id="RI"></p>
<h2>Receiving Institution</h2>
<p></a></p>



<!-- spacing: desktop=20, mobile=10 -->


<!-- unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"Result Codes","table":{"use_header":true,"header":[{"c":"Code"},{"c":"Description"}],"caption":false,"body":[[{"c":"1"},{"c":"Success / OK."}],[{"c":"0"},{"c":"Approved - No Action."}],[{"c":"-4"},{"c":"Invalid card number or reference."}],[{"c":"-5"},{"c":"Operation not Allowed"}],[{"c":"-6"},{"c":"Operation not Supported"}],[{"c":"-7"},{"c":"Transaction Timeout"}],[{"c":"-8"},{"c":"Authentication failed"}],[{"c":"-9"},{"c":"Do not honor (general decline, no specific reason given)"}]]}} -->


<!-- spacing: desktop=20, mobile=10 -->


<ul>
<li>The checksum that accompanies each request should be calculated as the HMAC-SHA1 hash of the method name concatenated with all the parameters in order. The terminal password should be used as the key for the hash:</li>
</ul>
<pre style="padding-left: 40px;">hmac_sha1('TerminalPassword', 'MethodNameParam1Param2Param3')


</pre>
<ul>
<li>Any argument that has the type &#8216;date&#8217; needs to follow the <a href="https://developer.sprint.paymentology.com/mpqr/documentation/http://xmlrpc.scripting.com/spec">XML-RPC specified</a> ISO 8601 datetime format:</li>
</ul>
<p style="padding-left: 40px;">&lt;dateTime.iso8601&gt;YYYYMMDDTHH:mm:ss±HH:mm&lt;dateTime.iso8601&gt;</p>
<ul>
<li>Any transaction amount is represented as its cent value; therefore an integer rather than a decimal.
<ul>
<li>R100.50 is therefore represented as 10050 rand cents.</li>
<li>$10.50 is therefore represented as 1050 dollar cents.</li>
</ul>
</li>
<li>The field optionalData is mandatory but its contents are optional. It accepts an XML-RPC struct, for example:
<pre>&lt;struct/&gt;</pre>
<p>or:</p>
<pre>&lt;struct&gt;&lt;member&gt;&lt;name&gt;postalCode&lt;/name&gt;&lt;value&gt;&lt;string&gt;10260&lt;/string&gt;&lt;/value&gt;&lt;/member&gt;&lt;/struct&gt;</pre>
</li>
</ul>



<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<p><a id="OI"></p>
<h2>Originating Institution</h2>
<p></a></p>



<!-- spacing: desktop=20, mobile=10 -->


<!-- unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"Result Codes","table":{"use_header":true,"header":[{"c":"Code"},{"c":"Description"}],"caption":false,"body":[[{"c":"1"},{"c":"Success / OK."}],[{"c":"0"},{"c":"Approved - No Action."}],[{"c":"-4"},{"c":"Invalid card number or reference"}],[{"c":"-300"},{"c":"Error from Mastercard. See resultText for reference."}]]}} -->


<!-- spacing: desktop=20, mobile=10 -->


<p>The checksum that accompanies each request should be calculated as the HMAC-SHA1 hash of the method name concatenated with all the parameters in order. The terminal password should be used as the key for the hash:</p>
<pre>hmac_sha1('TerminalPassword', 'MethodNameParam1Param2Param3')

</pre>
<p>Any argument that has the type &#8216;date&#8217; needs to follow the XML-RPC specified ISO 8601 datetime format:</p>
<pre>&lt;dateTime.iso8601&gt;YYYYMMDDTHH:mm:ss±HH:mm&lt;dateTime.iso8601&gt;


Any transaction amount is represented as its cent value; therefore an integer rather than a decimal.</pre>
<ul>
<li>R100.50 is therefore represented as 10050 rand cents.</li>
<li>$10.50 is therefore represented as 1050 dollar cents.</li>
</ul>
<p>&nbsp;</p>
<p>The field optionalData is mandatory but its contents are optional. It accepts an XML-RPC struct, for example:</p>
<pre>&lt;struct/&gt;</pre>
<p>or:</p>
<pre>&lt;struct&gt;&lt;member&gt;&lt;name&gt;recipientPostalCode&lt;/name&gt;&lt;value&gt;&lt;string&gt;10260&lt;/string&gt;&lt;/value&gt;&lt;/member&gt;&lt;/struct&gt;</pre>



<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<p><a id="RIRemote"></p>
<h2>Receiving Institution (Remote)</h2>
<p></a></p>



<!-- spacing: desktop=20, mobile=10 -->


<!-- unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"Result Codes","table":{"use_header":true,"header":[{"c":"Code"},{"c":"Description"}],"caption":false,"body":[[{"c":"1"},{"c":"Success / OK"}],[{"c":"0"},{"c":"Approved - No Action"}],[{"c":"-4"},{"c":"Invalid card number or reference"}],[{"c":"-300"},{"c":"Error from Mastercard. See resultText for reference"}]]}} -->


<!-- spacing: desktop=20, mobile=10 -->


<p>The checksum that accompanies each request should be calculated as the HMAC-SHA1 hash of the method name concatenated with all the parameters in order. The terminal password should be used as the key for the hash:</p>
<pre>hmac_sha1(`TerminalPassword`, `MethodNameParam1Param2Param3`)</pre>



<!-- spacing: desktop=20, mobile=10 -->


<p>Any argument that has the type &#8220;date&#8221; needs to follow the XML-RPC specified ISO 8601 datetime format:</p>
<p>&lt;dateTime.iso8601&gt;YYYYMMDDTHH:mm:ss±HH:mm&lt;dateTime.iso8601&gt;</p>
<p>&nbsp;</p>
<p>Any transaction amount is represented as it&#8217;s cent value therefore an integer rather than a decimal.</p>
<ul>
<li>R100.50 is therefore represented as 10050 rand cents.</li>
<li>$10.50 is therefore represented as 1050 dollar cents.</li>
</ul>
<p>&nbsp;</p>
<pre></pre>
<p>The field optionalData is mandatory but its contents are optional. It accepts an XML-RPC struct, for example:</p>
<pre>&lt;struct/&gt;</pre>
<p>or:</p>
<pre>&lt;struct&gt;&lt;member&gt;&lt;name&gt;recipientPostalCode&lt;/name&gt;&lt;value&gt;&lt;string&gt;10260&lt;/string&gt;&lt;/value&gt;&lt;/member&gt;&lt;/struct&gt;</pre>
