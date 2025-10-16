---
title: Help
deprecated: false
hidden: false
metadata:
  robots: index
original_path: tools/checksum-generator
---
<h2 id="intro">About the Checksum Generator</h2>
<p>The Checksum Generator is used to verify that the checksum calculation is correct and that it arrives at the same checksum result as our system.</p>
<h2 id="intro">Testing with the Checksum Generator</h2>
<p>Do this: Check the request data string matches the XML that is being sent (minus the XML tags).  For example:</p>
<p><span class="xml-highlight">&lt;?xml version=&#8221;1.0&#8243;?&gt;&lt;methodCall&gt;&lt;methodName&gt;Status&lt;/methodName&gt;&lt;params&gt;&lt;param&gt;&lt;value&gt;&lt;string&gt;100123&lt;/string&gt;&lt;/value&gt;&lt;/param&gt;&lt;param&gt;&lt;value&gt;&lt;string&gt;ref&lt;/string&gt;&lt;/value&gt;&lt;/param&gt;&lt;param&gt;&lt;value&gt;&lt;string&gt;45556&lt;/string&gt;&lt;/value&gt;&lt;/param&gt;&lt;param&gt;&lt;value&gt;&lt;string&gt;123&lt;/string&gt;&lt;/value&gt;&lt;/param&gt;&lt;param&gt;&lt;value&gt;&lt;dateTime.iso8601&gt;20170223T12:00:00&lt;/dateTime.iso8601&gt;&lt;/value&gt;&lt;/param&gt;&lt;param&gt;&lt;value&gt;&lt;string&gt;B4919AC22BAE3E2FFC4373C7A9B478A096BF1CB2&lt;/string&gt;&lt;/value&gt;&lt;/param&gt;&lt;/params&gt;&lt;/methodCall&gt;</span></p>
<p>The above would have a request data string (minus the checksum itself which of course isn&#8217;t an input to the calculation) of:</p>
<p><code>Status100123ref4555612320170223T12:00:00</code></p>



<!-- spacing: desktop=20, mobile=10 -->


<!-- unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":false,"text":"<p><strong>NB.</strong> <strong>During testing, avoid entering any personally identifiable information (PII), such as, user IDs, card numbers or email addresses.</strong></p>\n"}]} -->


<!-- spacing: desktop=20, mobile=10 -->


<h2>How to use Checksum Generator</h2>
<ol>
<li>Go to <a href="https://developer.sprint.paymentology.com/tools/checksum-generator/">Checksum Generator</a> under <a href="https://developer.sprint.paymentology.com/tools/">Tools</a></li>
<li>Enter your terminal password in the &#8220;Private Key&#8221; field</li>
<li>Enter the request data in the &#8220;String to hash&#8221; field</li>
<li>Click &#8220;Submit&#8221;</li>
<li>Wait for the &#8220;Transaction Result Pop-up&#8221; that will display the calculated checksum together with the details behind the calculation</li>
</ol>
