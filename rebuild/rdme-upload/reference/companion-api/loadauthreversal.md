---
title: LoadAuthReversal
category:
  uri: Companion API
slug: loadauthreversal
position: 25
parent:
  uri: api-reference
---

This method can only return the result codes of 1 (success) or -9 (an error occurred while queuing the Reversal).

**KLV will not be sent for reversals. Only reference data will be included if there is any. If KLV data is needed please lookup [KLV](/guides/klv-lookup) from the reference data included.**

The Paymentology issued terminal ID of the terminal requesting the transaction

The reference of the wallet to reverse a previous load

The amount of the original load to be reversed

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
<methodName>LoadAuthReversal</methodName>
<params>
<param>
<value>
<string>0014682067</string>
</value>
</param>
<param>
<value>
<string>IMPLTest</string>
</value>
</param>
<param>
<value>
<int>10000</int>
</value>
</param>
<param>
<value>
<string>Tutuka Test Pretoria ZAF</string>
</value>
</param>
<param>
<value>
<string></string>
</value>
</param>
<param>
<value>
<string>192316</string>
</value>
</param>
<param>
<value>
<dateTime.iso8601>20240313T11:20:00</dateTime.iso8601>
</value>
</param>
<param>
<value>
<string>192325</string>
</value>
</param>
<param>
<value>
<dateTime.iso8601>20240313T11:20:00</dateTime.iso8601>
</value>
</param>
<param>
<value>
<string>47D4F5C6E263FA295D492A925DF607773D3F1B9B</string>
</value>
</param>
</params>
</methodCall>
```

Status code indicating transaction result

```xml
<?xml version="1.0" encoding="UTF-8"?>
<methodResponse>
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
</methodResponse>
```

[Back to Remote API menu](/api-reference/companion-api/remote)
