---
title: Appendix
deprecated: false
hidden: false
metadata:
  robots: index
---
<p><a id="RI"></p>
<h2>Receiving Institution</h2>
<p></a></p>

<ul>
<li>The checksum that accompanies each request should be calculated as the HMAC-SHA1 hash of the method name concatenated with all the parameters in order. The terminal password should be used as the key for the hash:</li>
</ul>
<pre style={{paddingLeft: "40px"}}>hmac_sha1('TerminalPassword', 'MethodNameParam1Param2Param3')

</pre>
<ul>
<li>Any argument that has the type ‘date’ needs to follow the <a href="https://developer.sprint.paymentology.com/mpqr/documentation/http://xmlrpc.scripting.com/spec">XML-RPC specified</a> ISO 8601 dateTime format:</li>
</ul>
<p style={{paddingLeft: "40px"}}><dateTime.iso8601>YYYYMMDDTHH:mm:ss±HH:mm<dateTime.iso8601></p>
<ul>
<li>Any transaction amount is represented as its cent value; therefore an integer rather than a decimal.
<ul>
<li>R100.50 is therefore represented as 10050 rand cents.</li>
<li>$10.50 is therefore represented as 1050 dollar cents.</li>
</ul>
</li>
<li>The field optionalData is mandatory but its contents are optional. It accepts an XML-RPC struct, for example:
<pre><struct ></pre>
<p>or:</p>
<pre><struct><member><name>postalCode</name><value><string>10260</string></value></member></struct></pre>
</li>
</ul>

<p><a id="OI"></p>
<h2>Originating Institution</h2>
<p></a></p>

<p>The checksum that accompanies each request should be calculated as the HMAC-SHA1 hash of the method name concatenated with all the parameters in order. The terminal password should be used as the key for the hash:</p>
<pre>hmac_sha1('TerminalPassword', 'MethodNameParam1Param2Param3')

</pre>
<p>Any argument that has the type ‘date’ needs to follow the XML-RPC specified ISO 8601 dateTime format:</p>
<pre><dateTime.iso8601>YYYYMMDDTHH:mm:ss±HH:mm<dateTime.iso8601>

Any transaction amount is represented as its cent value; therefore an integer rather than a decimal.</pre>
<ul>
<li>R100.50 is therefore represented as 10050 rand cents.</li>
<li>$10.50 is therefore represented as 1050 dollar cents.</li>
</ul>
<p> </p>
<p>The field optionalData is mandatory but its contents are optional. It accepts an XML-RPC struct, for example:</p>
<pre><struct ></pre>
<p>or:</p>
<pre><struct><member><name>recipientPostalCode</name><value><string>10260</string></value></member></struct></pre>

<p><a id="RIRemote"></p>
<h2>Receiving Institution (Remote)</h2>
<p></a></p>

<p>The checksum that accompanies each request should be calculated as the HMAC-SHA1 hash of the method name concatenated with all the parameters in order. The terminal password should be used as the key for the hash:</p>
<pre>hmac_sha1(`TerminalPassword`, `MethodNameParam1Param2Param3`)</pre>

<p>Any argument that has the type “date” needs to follow the XML-RPC specified ISO 8601 dateTime format:</p>
<p><dateTime.iso8601>YYYYMMDDTHH:mm:ss±HH:mm<dateTime.iso8601></p>
<p> </p>
<p>Any transaction amount is represented as it’s cent value therefore an integer rather than a decimal.</p>
<ul>
<li>R100.50 is therefore represented as 10050 rand cents.</li>
<li>$10.50 is therefore represented as 1050 dollar cents.</li>
</ul>
<p> </p>
<pre></pre>
<p>The field optionalData is mandatory but its contents are optional. It accepts an XML-RPC struct, for example:</p>
<pre><struct ></pre>
<p>or:</p>
<pre><struct><member><name>recipientPostalCode</name><value><string>10260</string></value></member></struct></pre>
