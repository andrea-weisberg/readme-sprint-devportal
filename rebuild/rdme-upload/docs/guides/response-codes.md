---
title: Response Codes - Local API
category:
  uri: Guides
slug: response-codes
position: 49
---

## Important

The checksum that accompanies each request should be calculated as the HMAC-SHA256 hash of the method name concatenated with all the parameters in order. The terminal password should be used as the key for the hash:
hmac_sha256('TerminalPassword', 'MethodNameParam1Param2Param3')

Any method with both the reference and cardIdentifier parameters will accept an empty reference parameter if the campaign is set to use the card number as reference and the cardIdentifier parameter is supplied.

The cardIdentifier parameter can be empty for most calls if the reference only refers to a single card

Any argument that has the type 'date' needs to follow the XML-RPC specified ISO 8601 datetime format:
<dateTime.iso8601>YYYYMMDDTHH:mm:ss<dateTime.iso8601>

Any transaction amount is represented as its cent value; therefore an integer rather than a decimal.

- R100.50 is therefore represented as 10050 rand cents.

- $10.50 is therefore represented as 1050 dollar cents.
