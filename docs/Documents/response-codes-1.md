---
title: Response Codes – Local API
deprecated: false
hidden: false
metadata:
  robots: index
---

<h2>Important</h2>
<p>The checksum that accompanies each request should be calculated as the HMAC-SHA256 hash of the method name concatenated with all the parameters in order. The terminal password should be used as the key for the hash:<br  />
<span className="xml-highlight">hmac_sha256(‘TerminalPassword’, ‘MethodNameParam1Param2Param3’)</span></p>
<p> </p>
<p>Any method with both the <span className="xml-highlight">reference</span> and <span className="xml-highlight">cardIdentifier</span> parameters will accept an empty reference parameter if the campaign is set to use the card number as <span className="xml-highlight">reference</span> and the <span className="xml-highlight">cardIdentifier</span> parameter is supplied.</p>
<p> </p>
<p>The <span className="xml-highlight">cardIdentifier</span> parameter can be empty for most calls if the reference only refers to a single card</p>
<p> </p>
<p>Any argument that has the type ‘date’ needs to follow the XML-RPC specified ISO 8601 dateTime format:<br  />
<span className="xml-highlight"><dateTime.iso8601>YYYYMMDDTHH:mm:ss<dateTime.iso8601></span></p>

<p>Any transaction amount is represented as its cent value; therefore an integer rather than a decimal.</p>
<ul>
<li>R100.50 is therefore represented as 10050 rand cents.</li>
<li>$10.50 is therefore represented as 1050 dollar cents.</li>
</ul>
