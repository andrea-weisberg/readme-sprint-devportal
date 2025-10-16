---
title: Response Codes – Remote API
deprecated: false
hidden: false
metadata:
  robots: index
---
\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"Code"\},\{"c":"Description"\}],"caption":false,"body":[[\{"c":"1"\},\{"c":"Approved"\}],[\{"c":"2"\},\{"c":"Approved - Partial amount"\}],[\{"c":"-2"\},\{"c":"Invalid card number"\}],[\{"c":"-3"\},\{"c":"Duplicate transmission"\}],[\{"c":"-4"\},\{"c":"Invalid card number (use for invalid wallet reference)"\}],[\{"c":"-5"\},\{"c":"Transaction not permitted to Terminal / Transaction not permitted to Acquirer"\}],[\{"c":"-6"\},\{"c":"Function not supported / Invalid transaction"\}],[\{"c":"-7"\},\{"c":"Transaction timeout"\}],[\{"c":"-8"\},\{"c":"Authentication failed (Incorrect checksum)"\}],[\{"c":"-9"\},\{"c":"Do not honor (general decline, no specific reason given, technical error)"\}],[\{"c":"-13"\},\{"c":"Stolen card"\}],[\{"c":"-14"\},\{"c":"Insufficient funds"\}],[\{"c":"-16"\},\{"c":"Exceeds Purchase amount limit"\}],[\{"c":"-17"\},\{"c":"Not sufficient funds"\}],[\{"c":"-18"\},\{"c":"Exceeds withdrawal amount limit"\}],[\{"c":"-19"\},\{"c":"Invalid amount"\}],[\{"c":"-24"\},\{"c":"Security violation"\}],[\{"c":"-25"\},\{"c":"Incorrect PIN"\}],[\{"c":"-26"\},\{"c":"Allowable PIN tries exceeded"\}],[\{"c":"-27"\},\{"c":"Invalid PIN block"\}],[\{"c":"-28"\},\{"c":"PIN length error"\}],[\{"c":"-29"\},\{"c":"Restricted card"\}],[\{"c":"-34"\},\{"c":"Account closed / Invalid account"\}],[\{"c":"-36"\},\{"c":"Expired card"\}],[\{"c":"-37"\},\{"c":"Suspected fraud"\}],[\{"c":"-38"\},\{"c":"Lost card"\}],[\{"c":"-39"\},\{"c":"Stolen card"\}],[\{"c":"-41"\},\{"c":"Requested function not supported / Invalid transaction"\}],[\{"c":"-783"\},\{"c":"Do not honor (general decline, no specific reason given, technical  error)"\}],[\{"c":"-784"\},\{"c":"Transaction not permitted to Cardholder / Transaction not permitted to Issuer"\}]]}} */}


\{/* unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"\} */}


<h2>Important</h2>
<p>Any argument that has the type <span class="xml-highlight">date</span> needs to follow the XML-RPC specified ISO 8601 date-time format: <dateTime.iso8601>YYYYMMDDTHH:mm:ss<dateTime.iso8601></p>



\{/* spacing: desktop=20, mobile=10 */\}


<p>Any transaction amount is represented as its cent value; therefore an integer rather than a decimal.</p>
<ul>
<li>R100.50 is therefore represented as 10050 rand cents.</li>
<li>$10.50 is therefore represented as 1050 dollar cents.</li>
</ul>



\{/* spacing: desktop=20, mobile=10 */\}


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



\{/* spacing: desktop=20, mobile=10 */\}


<h2>Matching response codes</h2>
<p>You can refer to the <a href="https://developer.sprint.paymentology.com/response-codes-2/response-and-action-code-mapping/">Response and action code mapping table</a> to understand how Remote API Response Codes map to different networks.</p>
