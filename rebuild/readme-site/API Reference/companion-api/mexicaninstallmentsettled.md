# MexicanInstallmentSettled

Notifies that a Mexican installment transaction is settled.

The Paymentology issued terminal ID of the terminal requesting the transaction

The reference of the wallet that the installment transaction just got settled.

Transaction ID of the original authorisation that was settled.

Transaction date of the original authorisation that was settled.

One of the following:
00 (No Promotion)
03 (Without interest for the cardholder)
05 (With interest for the cardholder)
07 (Buy today, pay later)

The total number of the installments linked to the installment transaction.

Grace period (in months) before first installment

The local currency code of the acquirer or source location of the transaction (eg. 484 = Mexican Peso)

HMAC-SHA256 hashed signature of the concatenated method name with all argument values using the terminal password as private key.

<?xml version="1.0"?>
<methodCall>
<methodName>MexicanInstallmentSettled</methodName>
<params>
<param>
<value>
<string>0097852049</string>
</value>
</param>
<param>
<value>
<string>5a332769-264a-402c-851b-2d7a5ddb7bee</string>
</value>
</param>
<param>
<value>
<string>117363249782</string>
</value>
</param>
<param>
<value>
<dateTime.iso8601>20230223T03:48:27</dateTime.iso8601>
</value>
</param>
<param>
<value>
<int>05</int>
</value>
</param>
<param>
<value>
<string>03</string>
</value>
</param>
<param>
<value>
<int>02</int>
</value>
</param>
<param>
<value>
<int>484</int>
</value>
</param>
<param>
<value>
<string>B90B6C3D75173C0CEB312DF2E0225EC1A4A3FF0F</string>
</value>
</param>
</params>
</methodCall>

Status code indicating transaction result

<methodResponse>
<params>
<param>
<value>
<struct>
<member>
<name>
resultCode
</name>
<value>
<int>
1
</int>
</value>
</member>
</struct>
</value>
</param>
</params>
</methodResponse>

[BACK TO REMOTE API MENU](/api-reference/companion-api/remote)
