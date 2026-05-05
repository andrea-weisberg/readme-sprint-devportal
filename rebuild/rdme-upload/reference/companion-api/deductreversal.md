---
title: DeductReversal
category:
  uri: Companion API
slug: deductreversal
position: 41
parent:
  uri: remote
---

Reverse a deduct that was previously requested on a wallet.

**KLV will not be sent for reversals.**

The Paymentology issued terminal ID of the terminal requesting the transaction

The reference of the wallet to reverse a previous deduct

The amount of the original deduct to be reversed

A description of the terminal where the card was used

Extra information about the transaction in a [KLV format](/guides/klv-lookup)

Transaction ID of the original deduct to be reversed

Transaction date (in UTC) of the original deduct to be reversed

Transaction ID to identify the reversal message. Note that the Transaction ID is not a unique value and may be duplicated over time

Transaction date (in UTC) to identify the reversal message

HMAC-SHA256 hashed signature of the concatenated method name with all argument values using the terminal password as private key

```xml
<?xml version="1.0"?>
<methodCall>
<methodName>DeductReversal</methodName>
<params>
<param>
<value>
<string>0034048207</string>
</value>
</param>
<param>
<value>
<string>68263116</string>
</value>
</param>
<param>
<value>
<int>559</int>
</value>
</param>
<param>
<value>
<string>PAYPAL 4029357733 SGP</string>
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
<string>571156</string>
</value>
</param>
<param>
<value>
<dateTime.iso8601>20200824T01:52:15</dateTime.iso8601>
</value>
</param>
<param>
<value>
<string>2010206</string>
</value>
</param>
<param>
<value>
<dateTime.iso8601>20200824T03:52:22</dateTime.iso8601>
</value>
</param>
<param>
<value>
<string>D86B50F9FB658F5AB00A280BF52A40DAD7A3B89919D98ADABBC93FD42D5AF9E8</string>
</value>
</param>
</params>
</methodCall>
```

Status code indicating transaction result

```xml
<?xml version=""1.0"" encoding=""UTF-8""?>
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
