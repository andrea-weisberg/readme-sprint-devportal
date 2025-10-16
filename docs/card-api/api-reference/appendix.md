---
title: Response Codes
deprecated: false
hidden: false
metadata:
  robots: index
original_path: card-api/api-reference
---
<!-- unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"Result Codes","table":{"use_header":true,"header":[{"c":"Code"},{"c":"Description"}],"caption":false,"body":[[{"c":"\"0\""},{"c":"Approved no action. Note: code is 0 and does not include \"\""}],[{"c":"1"},{"c":"Approved"}],[{"c":"-3"},{"c":"Duplicate Transaction ID"}],[{"c":"-4"},{"c":"Validation error. Please verify the values you provided are correct"}],[{"c":"-5"},{"c":"Operation not Allowed"}],[{"c":"-6"},{"c":"Operation not Supported"}],[{"c":"-7"},{"c":"Transaction Timeout"}],[{"c":"-8"},{"c":"Authentication failed"}],[{"c":"-9"},{"c":"Do not honour (general decline, no specific reason given)"}],[{"c":"-10"},{"c":"Transaction could not be processed. Please check card is valid and working"}],[{"c":"-17"},{"c":"Insufficient funds"}],[{"c":"-18"},{"c":"Exceeds withdrawal amount limit"}],[{"c":"-19"},{"c":"Invalid amount"}],[{"c":"-21"},{"c":"Maximum card value would be exceeded"}],[{"c":"-22"},{"c":"Maximum monthly load value would be exceeded"}],[{"c":"-23"},{"c":"Invalid terminal for campaign"}],[{"c":"-24"},{"c":"Security violation"}],[{"c":"-25"},{"c":"Incorrect PIN"}],[{"c":"-26"},{"c":"Allowable PIN tries exceeded"}],[{"c":"-27"},{"c":"Invalid PIN block"}],[{"c":"-28"},{"c":"PIN length error"}],[{"c":"-29"},{"c":"Invalid Card Data"}],[{"c":"-33"},{"c":"Card has a balance"}],[{"c":"-34"},{"c":"Card already active"}],[{"c":"-35"},{"c":"Card not active"}],[{"c":"-36"},{"c":"Expired Card"}],[{"c":"-37"},{"c":"Suspected fraud"}],[{"c":"-38"},{"c":"Lost card"}],[{"c":"-39"},{"c":"Stolen card"}],[{"c":"-248"},{"c":"Invalid MSISDN"}],[{"c":"-250"},{"c":"Invalid initials"}],[{"c":"-251"},{"c":"Invalid Address OR Invalid Contact Number"}],[{"c":"-252"},{"c":"Invalid Address 2"}],[{"c":"-253"},{"c":"Invalid Address 3"}],[{"c":"-254"},{"c":"Invalid Address 4"}],[{"c":"-255"},{"c":"Invalid Address 5 OR Invalid PinBlock"}],[{"c":"-294"},{"c":"Invalid stop reason code"}],[{"c":"-295"},{"c":"Invalid expiry date"}],[{"c":"-296"},{"c":"Invalid transaction date"}],[{"c":"-297"},{"c":"Invalid transaction ID"}],[{"c":"-298"},{"c":"Invalid reference data"}],[{"c":"-299"},{"c":"Invalid reference ID\n"}],[{"c":"-780"},{"c":"Invalid card reference"}],[{"c":"-781"},{"c":"Invalid card - Not a physical card"}],[{"c":"-782"},{"c":"Cannot disable physical card OR Print card request already requested"}]]}} -->


<!-- spacing: desktop=20, mobile=10 -->


<h2>Important</h2>
<p>Any argument that has the type &#8216;date&#8217; needs to follow the XML-RPC specified ISO 8601 date-time format:</p>
<p><span class="xml-highlight">&lt;dateTime.iso8601&gt;YYYYMMDDTHH:mm:ss&lt;dateTime.iso8601&gt;</span></p>
<p>&nbsp;</p>
<p>Any transaction amount is represented as it&#8217;s cents value. Therefore, an integer rather than a decimal.</p>
<ul>
<li>R100.50 is therefore represented as 10050 rand cents.</li>
<li>$10.50 is therefore represented as 1050 dollar cents.</li>
</ul>



<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<h1><a id="feeTypes"> Fee Types</a></h1>



<!-- unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"Fee Types","table":{"use_header":true,"header":[{"c":"Fee ID"},{"c":"Fee Name"}],"caption":false,"body":[[{"c":"1"},{"c":"SMS Balance Enquiry"}],[{"c":"2"},{"c":"ATM Balance Enquiry"}],[{"c":"3"},{"c":"ATM - Balance Enquiry - Agent Bank"}],[{"c":"4"},{"c":"ATM Cash Withdrawal"}],[{"c":"5"},{"c":"ATM Cash Withdrawal - Agent Bank"}],[{"c":"6"},{"c":"POS Purchase"}],[{"c":"7"},{"c":"POS Purchase with Cashback"}],[{"c":"8"},{"c":"SMS Transaction Notification"}],[{"c":"9"},{"c":"Emergency Card Advance"}],[{"c":"10"},{"c":"Emergency Card Replacement/ Cash Advance"}],[{"c":"11"},{"c":"Cashout"}],[{"c":"12"},{"c":"Card Order"}],[{"c":"13"},{"c":"Card Delivery"}],[{"c":"14"},{"c":"Card Load"}],[{"c":"15"},{"c":"Monthly Active Card"}],[{"c":"16"},{"c":"Monthly Inactive Card"}],[{"c":"17"},{"c":"Spillage"}],[{"c":"18"},{"c":"Cash Deposit"}],[{"c":"19"},{"c":"Card Initiation"}],[{"c":"20"},{"c":"Card Reinitiation"}],[{"c":"21"},{"c":"Replacement Card"}]]}} -->
