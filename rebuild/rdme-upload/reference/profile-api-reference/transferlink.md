---
title: TransferLink
category:
  uri: Profile API Reference
slug: transferlink
position: 41
parent:
  uri: profile-api-reference
---

Transfer a reference to a new card. The old card will be stopped and the bearer details transferred to the new card. The new card will be linked and activated.

**NOTE:** Applicable to our Visa product.

The Paymentology issued terminal ID of the terminal requesting the transaction.

The user defined reference to the card; for example a member id or wallet number.

The card number, sequence number or tracking number of the card being transferred FROM.

The card number, sequence number or tracking number of the card being transferred TO. This parameter can’t be empty for this call.

Client generated Transaction ID to assist in identify transactions on the client side.

Client generated / local Transaction Date to assist in identifying transactions on the client side.

HMAC-SHA256 hashed signature of the concatenated method name with all argument values using the terminal password as private key.

```xml
<?xml version=""1.0""?>
<methodCall>
<methodName>TransferLink</methodName>
<params>
<param>
<value>
<string>0014682067</string>
</value>
</param>
<param>
<value>
<string>TESTTTK</string>
</value>
</param>
<param>
<value>
<string>5267262238630233</string>
</value>
</param>
<param>
<value>
<string>5267262930751857</string>
</value>
</param>
<param>
<value>
<string>123456</string>
</value>
</param>
<param>
<value>
<dateTime.iso8601>20200327T00:00:00</dateTime.iso8601>
</value>
</param>
<param>
<value>
<string>B96AFC35F3C59A6B89575CA70C32948CBDEE0F41</string>
</value>
</param>
</params>
</methodCall>
```

Status code indicating transaction result.

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
<member>
<name>resultText</name>
<value>
<string>Approved</string>
</value>
</member>
</struct>
</value>
</param>
</params>
</methodResponse>
```
