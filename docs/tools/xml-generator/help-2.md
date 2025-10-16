---
title: Help
deprecated: false
hidden: false
metadata:
  robots: index
original_path: tools/xml-generator
---
<h2 id="intro">When to use XML Generator</h2>
<p>You will use XML Generator to confirm that XML requests generated through your code are generated with the same request parameters as Paymentology Sprint &#8211; including the checksum, to ensure compatibility.</p>
<p>If the XML is identical but the checksums do not match, you can use the <strong>Checksum Generator</strong> tool to work solely on the checksum and debug further.</p>
<h2 id="intro">Testing with XML Generator</h2>
<ul>
<li>Check that the request parameters are identical (including spaces).</li>
<li>When using copy and paste, beware of hidden characters that may not display, but affect the checksum calculation.</li>
<li>When in doubt, type the data manually.</li>
</ul>



<!-- spacing: desktop=20, mobile=10 -->


<!-- unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":false,"text":"<p><strong>NB.</strong> <strong>During testing, avoid entering any personally identifiable information (PII), such as, user IDs, card numbers or email addresses.</strong></p>\n"}]} -->


<!-- spacing: desktop=20, mobile=10 -->


<h2>How to use XML Generator</h2>
<ol>
<li>Go to <a href="https://developer.sprint.paymentology.com/tools/xml-poster-generator/">XML Poster &amp; Generator</a> under <a href="https://developer.sprint.paymentology.com/tools/">Tools</a></li>
<li>Select the API you want to create an XMLRPC request for Companion Local API or Remote API)</li>
<li>Select the method you want to create an XMLRPC request for</li>
<li>Fill out the method arguments with your own data</li>
<li>Enter your terminal password in the &#8220;<strong>private key</strong>&#8221; field</li>
<li>Click &#8220;<strong>Create XML RPC Request</strong>&#8220;</li>
<li>Wait for the &#8220;<strong>Transaction result pop-up</strong>&#8221; that will contain the generated XML &#8211; both unformatted (for transaction purposes) and formatted (for readability purposes)</li>
</ol>



<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<h2 id="intro">When to use XML Poster</h2>
<p>You will use XML Poster to post requests created with the XML Generator tool to Paymentology only in cases where there is no other route to take.</p>
<p>For example: When you start testing, you will not have a system in place to call the Companion Local API, so you can use this tool to post requests to the API directly &#8211; like when you test your first card.</p>
<h2 id="intro">Testing with XML Poster</h2>
<p>Check the following:</p>
<ul>
<li>The XML and checksum needs to be correct.</li>
<li>It is advisable to use the XML Generator tool to create the XML in the first place, although you can also use the tool to check the validity of the XML created by your own system when you&#8217;re ready.</li>
</ul>



<!-- spacing: desktop=20, mobile=10 -->


<h2>How to use XML Poster</h2>
<ol>
<li>Go to <a href="https://developer.sprint.paymentology.com/tools/xml-poster-generator/">XML Poster &amp; Generator</a> under <a href="https://developer.sprint.paymentology.com/tools/">Tools</a></li>
<li>Choose the target API</li>
<li>Paste your XML request</li>
<li>Click on &#8220;<strong>Submit</strong>&#8220;</li>
<li>Wait for the &#8220;<strong>Transaction result pop-up</strong>&#8221; that will contain the XML response</li>
</ol>
