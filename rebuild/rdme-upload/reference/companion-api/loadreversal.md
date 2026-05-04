---
title: LoadReversal
category:
  uri: Companion API
slug: loadreversal
position: 26
parent:
  uri: api-reference
---

Reverse a load that was previously requested on a wallet.**KLV will not be sent for reversals. Only reference data will be included if there is any. If KLV data is needed please lookup [KLV](/guides/klv-lookup) from the reference data included.**

The Paymentology issued terminal ID of the terminal requesting the transaction

The reference of the wallet to reverse a previous load

The amount of the original load to be reversed (can be partial)

A description of the terminal where the card was used

Extra information about the transaction in a [KLV format](/guides/klv-lookup)

Transaction ID of the original load to be reversed

Transaction date of the original load to be reversed

Transaction ID to identify the reversal message.

Note that the Transaction ID is not a unique value and may be duplicated over time.

Transaction date to identify the reversal message

HMAC-SHA256 hashed signature of the concatenated method name with all argument values using the terminal password as private key

```xml
<?xml version="1.0"?>
<methodCall>
<methodName>LoadReversal</methodName>
<params>
<param>
<value>
<string>0089753250</string>
</value>
</param>
<param>
<value>
<string>592193355535</string>
</value>
</param>
<param>
<value>
<int>7900000</int>
</value>
</param>
<param>
<value>
<string>20200821T02:42:00/Lazada\Lazada, Ho Chi Minh, VN\Ho Chi Minh\ 08 VNM</string>
</value>
</param>
<param>
<value>
<string>
</string>
</value>
</param>
<param>
<value>
<string>2911DF1B-9F06-8EBA-F1E8EE0BDF673D4C</string>
</value>
</param>
<param>
<value>
<dateTime.iso8601>20200824T01:44:00</dateTime.iso8601>
</value>
</param>
<param>
<value>
<string>2010048</string>
</value>
</param>
<param>
<value>
<dateTime.iso8601>20200824T01:44:07</dateTime.iso8601>
</value>
</param>
<param>
<value>
<string>6F0D0CFF534288C848D7881CBFEFF88605DB6214</string>
</value>
</param>
</params>
</methodCall>
```

Status code indicating transaction result

"<methodResponse>
<params>
<param>
<value>
<struct>
<member>
<name>resultCode</name>
<value>
<int>1</int>
</value>
</member>
</struct>
</value>
</param>
</params>
</methodResponse>"

[Back to Remote API menu](/api-reference/companion-api/remote)
