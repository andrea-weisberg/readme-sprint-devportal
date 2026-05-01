# Originating Institution

## Available Methods

- [TransferPaymentToMerchant](https://developer.sprint.paymentology.com/qr-payments-api/api-reference/originating-institution/#TransferPaymentToMerchant) - Transfer payment to merchant

## TransferPaymentToMerchant

Transfer payment to merchant.

The Paymentology issued terminal ID of the terminal requesting the transaction

Card Number of the recipient/merchant

First name of the recipient/merchant

Last name of the recipient/merchant

City of the recipient/merchant

ISO alpha country code of the recipient/merchant Ex. ZAF

Mastercard defined merchant category code

First name of the sender

Last name of the sender

Address of the sender

City of the sender

Postal code of the sender

ISO alpha country code of the sender Ex. ZAF

The user defined reference to the card; for example a member id or wallet number

The amount to be sent to the receiving subscriber

Currency of the requestAmount Ex. ZAR

Client generated transaction ID to assist in identify transactions on the client side

Client generated / local transaction date to assist in identifying transactions on the client side

Struct with optional fields, right now only "recipientPostalCode" field is accepted. See above for details. The maximum length of the recipientPostalCode is 10.

The calculated HMAC-SHA1 signature of the call as specified in the rules of thumb

<methodCall>
<methodName>TransferPaymentToMerchant</methodName>
<params>
<param>
<value>
<string>0039467951</string>
</value>
</param>
<param>
<value>
<string>AFF44112</string>
</value>
</param>
<param>
<value>
<string>John</string>
</value>
</param>
<param>
<value>
<string>Doe</string>
</value>
</param>
<param>
<value>
<string>Bangkok</string>
</value>
</param>
<param>
<value>
<string>THA</string>
</value>
</param>
<param>
<value>
<string>10261</string>
</value>
</param>
<param>
<value>
<string>Jeremy</string>
</value>
</param>
<param>
<value>
<string>Booster</string>
</value>
</param>
<param>
<value>
<string>137 Zoho Rade 12</string>
</value>
</param>
<param>
<value>
<string>Bangkok</string>
</value>
</param>
<param>
<value>
<string>45687</string>
</value>
</param>
<param>
<value>
<string>THA</string>
</value>
</param>
<param>
<value>
<string>039200071850</string>
</value>
</param>
<param>
<value>
<int>100</int>
</value>
</param>
<param>
<value>
<string>THB</string>
</value>
</param>
<param>
<value>
<string>txn1234567</string>
</value>
</param>
<param>
<value>
<dateTime.iso8601>20100102T12:34:56+0700</dateTime.iso8601>
</value>
</param>
<param>
<value>
<struct/>
</value>
</param>
<param>
<value>
<string>FE0F831A3AEB4925B97F3037D9B4BDDF5C615C3B</string>
</value>
</param>
</params>
</methodCall>

Status code indicating transaction result

Text indicating transaction result

<methodResponse>
<params>
<param>
<value>
<struct>
<member>
<name>resultCode</name>
<value>
<double>1</double>
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

[Appendix](https://developer.sprint.paymentology.com/qr-payments-api/api-reference/appendix/#OI)
