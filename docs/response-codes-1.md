---
title: Response Codes &#8211; Local API
deprecated: false
hidden: false
metadata:
  robots: index
---
<!-- unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"Result Codes","table":{"use_header":true,"header":[{"c":"Code"},{"c":"Description"}],"caption":false,"body":[[{"c":"\"0\""},{"c":"Approved no Action. Note; code is 0 and does not include \"\""}],[{"c":"1"},{"c":"Approved"}],[{"c":"-3"},{"c":"Duplicate Transaction ID"}],[{"c":"-4"},{"c":"Validation error. Please verify the values you provided are correct"}],[{"c":"-5"},{"c":"Operation not Allowed"}],[{"c":"-6"},{"c":"Operation not Supported"}],[{"c":"-7"},{"c":"Transaction Timeout"}],[{"c":"-8"},{"c":"Authentication Failed"}],[{"c":"-9"},{"c":"Do not honor (general decline, no specific reason given)"}],[{"c":"-29"},{"c":"There are invalid characters in either the pin block or one of these fields:<br>\ntitle, initials, surname, address1,  address2, address3, address4, address5, additionalData"}],[{"c":"-34"},{"c":"Card already active"}],[{"c":"-35"},{"c":"Card not active"}],[{"c":"-36"},{"c":"Expired card"}],[{"c":"-38"},{"c":"Lost card"}],[{"c":"-39"},{"c":"Stolen card"}],[{"c":"-244"},{"c":"Invalid last name"}],[{"c":"-246"},{"c":"Invalid first name"}],[{"c":"-247"},{"c":"Invalid ID number"}],[{"c":"-248"},{"c":"Invalid MSISDN"}],[{"c":"-250"},{"c":"Invalid initials"}],[{"c":"-251"},{"c":"Invalid Address 1 OR Invalid Contact Number"}],[{"c":"-252"},{"c":"Invalid Address 2"}],[{"c":"-253"},{"c":"Invalid Address 3"}],[{"c":"-254"},{"c":"Invalid Address 4"}],[{"c":"-255"},{"c":"Invalid Address 5 OR Invalid PinBlock"}],[{"c":"-295"},{"c":"Invalid expiry date"}],[{"c":"-333"},{"c":"sessionKey not present in header and \"Companion API Require Session Key\" is enabled"}],[{"c":"-334"},{"c":"sessionKey present and not decryptable/parsable"}],[{"c":"-778"},{"c":"Reference has no linked cards"}],[{"c":"-779"},{"c":"Card already linked to a different reference"}],[{"c":"-780"},{"c":"Invalid card reference"}],[{"c":"-781"},{"c":"Invalid card - Not a physical card"}],[{"c":"-782"},{"c":"Cannot disable physical card OR Print card request already requested"}]]}} -->


<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<h2>Important</h2>
<p>The checksum that accompanies each request should be calculated as the HMAC-SHA256 hash of the method name concatenated with all the parameters in order. The terminal password should be used as the key for the hash:<br />
<span class="xml-highlight">hmac_sha256(&#8216;TerminalPassword&#8217;, &#8216;MethodNameParam1Param2Param3&#8217;)</span></p>
<p>&nbsp;</p>
<p>Any method with both the <span class="xml-highlight">reference</span> and <span class="xml-highlight">cardIdentifier</span> parameters will accept an empty reference parameter if the campaign is set to use the card number as <span class="xml-highlight">reference</span> and the <span class="xml-highlight">cardIdentifier</span> parameter is supplied.</p>
<p>&nbsp;</p>
<p>The <span class="xml-highlight">cardIdentifier</span> parameter can be empty for most calls if the reference only refers to a single card</p>
<p>&nbsp;</p>
<p>Any argument that has the type &#8216;date&#8217; needs to follow the XML-RPC specified ISO 8601 datetime format:<br />
<span class="xml-highlight">&lt;dateTime.iso8601&gt;YYYYMMDDTHH:mm:ss&lt;dateTime.iso8601&gt;</span></p>



<!-- spacing: desktop=20, mobile=10 -->


<p>Any transaction amount is represented as its cent value; therefore an integer rather than a decimal.</p>
<ul>
<li>R100.50 is therefore represented as 10050 rand cents.</li>
<li>$10.50 is therefore represented as 1050 dollar cents.</li>
</ul>
