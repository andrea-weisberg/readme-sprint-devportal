---
title: Help
deprecated: false
hidden: false
metadata:
  robots: index
---
<h2 id="intro">About the Checksum Generator</h2>
<p>The Checksum Generator is used to verify that the checksum calculation is correct and that it arrives at the same checksum result as our system.</p>
<h2 id="intro">Testing with the Checksum Generator</h2>
<p>Do this: Check the request data string matches the XML that is being sent (minus the XML tags).  For example:</p>
<p><span className="xml-highlight"><?xml version="”1.0″?><methodCall><methodName>Status</methodName><params><param><value><string>100123</string></value></param><param><value><string>ref</string></value></param><param><value><string>45556</string></value></param><param><value><string>123</string></value></param><param><value><dateTime.iso8601>20170223T12:00:00</dateTime.iso8601></value></param><param><value><string>B4919AC22BAE3E2FFC4373C7A9B478A096BF1CB2</string></value></param></params></methodCall></span"></p>
<p>The above would have a request data string (minus the checksum itself which of course isn’t an input to the calculation) of:</p>
<p><code>Status100123ref4555612320170223T12:00:00</code></p>

<h2>How to use Checksum Generator</h2>
<ol>
<li>Go to <a href="https://developer.sprint.paymentology.com/tools/checksum-generator/">Checksum Generator</a> under <a href="https://developer.sprint.paymentology.com/tools/">Tools</a></li>
<li>Enter your terminal password in the “Private Key” field</li>
<li>Enter the request data in the “String to hash” field</li>
<li>Click “Submit”</li>
<li>Wait for the “Transaction Result Pop-up” that will display the calculated checksum together with the details behind the calculation</li>
</ol>
