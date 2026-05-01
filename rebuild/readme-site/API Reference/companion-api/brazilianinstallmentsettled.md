# BrazilianInstallmentSettled

Notifies that a Brazilian installment transaction is settled.

The Paymentology issued terminal ID of the terminal requesting the transaction

The reference of the wallet that the installment transaction just got settled.

Transaction ID of the original authorisation that was settled.

Transaction date of the original authorisation that was settled.

The total number of the installments linked to the installment transaction.

One of 403 (with interest), 407 (without interest), 488 (IATA), 410 (CrediDolar, specific for Banco Itau)

The total amount of the transaction linked to the installment transaction in cents.

The current number of the installment that is being settled.

The amount of the installment that is being settled in cents.

The airport fee amount related to the installment that is being settled in cents.

The down payment amount related to the installment that is being settled in cents.

HMAC-SHA256 hashed signature of the concatenated method name with all argument values using the terminal password as private key.

<?xml version="1.0"?>
<methodCall>
<methodName>
BrazilianInstallmentSettled
</methodName>
<params>
<param>
<value>
<string>
0097852049
</string>
</value>
</param>
<param>
<value>
<string>
5a332769-264a-402c-851b-2d7a5ddb7bee
</string>
</value>
</param>
<param>
<value>
<string>
117363249782
</string>
</value>
</param>
<param>
<value>
<dateTime.iso8601>
20220223T03:48:27
</dateTime.iso8601>
</value>
</param>
<param>
<value>
<string>
03
</string>
</value>
</param>
<param>
<value>
<int>
403
</int>
</value>
</param>
<param>
<value>
<int>
000000015000
</int>
</value>
</param>
<param>
<value>
<string>
03
</string>
</value>
</param>
<param>
<value>
<int>
000000005000
</int>
</value>
</param>
<param>
<value>
<int>
000000000000
</int>
</value>
</param>
<param>
<value>
<int>
000000000000
</int>
</value>
</param>
<param>
<value>
<string>
346C246D7B79896C8507370CC449DEF4C23E447D
</string>
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

[back to remote api menu](/api-reference/companion-api/remote)
