# Appendix

## Receiving Institution

- The checksum that accompanies each request should be calculated as the HMAC-SHA1 hash of the method name concatenated with all the parameters in order. The terminal password should be used as the key for the hash:

hmac_sha1('TerminalPassword', 'MethodNameParam1Param2Param3')

- Any argument that has the type 'date' needs to follow the [XML-RPC specified](https://developer.sprint.paymentology.com/mpqr/documentation/http://xmlrpc.scripting.com/spec) ISO 8601 datetime format:

<dateTime.iso8601>YYYYMMDDTHH:mm:ss±HH:mm<dateTime.iso8601>

- Any transaction amount is represented as its cent value; therefore an integer rather than a decimal. R100.50 is therefore represented as 10050 rand cents.

- $10.50 is therefore represented as 1050 dollar cents.

- The field optionalData is mandatory but its contents are optional. It accepts an XML-RPC struct, for example: or: postalCode 10260

## Originating Institution

The checksum that accompanies each request should be calculated as the HMAC-SHA1 hash of the method name concatenated with all the parameters in order. The terminal password should be used as the key for the hash:
hmac_sha1('TerminalPassword', 'MethodNameParam1Param2Param3')

Any argument that has the type 'date' needs to follow the XML-RPC specified ISO 8601 datetime format:
<dateTime.iso8601>YYYYMMDDTHH:mm:ss±HH:mm<dateTime.iso8601>

Any transaction amount is represented as its cent value; therefore an integer rather than a decimal.

- R100.50 is therefore represented as 10050 rand cents.

- $10.50 is therefore represented as 1050 dollar cents.

The field optionalData is mandatory but its contents are optional. It accepts an XML-RPC struct, for example:
<struct/>
or:
<struct><member><name>recipientPostalCode</name><value><string>10260</string></value></member></struct>

## Receiving Institution (Remote)

The checksum that accompanies each request should be calculated as the HMAC-SHA1 hash of the method name concatenated with all the parameters in order. The terminal password should be used as the key for the hash:
hmac_sha1(`TerminalPassword`, `MethodNameParam1Param2Param3`)

Any argument that has the type "date" needs to follow the XML-RPC specified ISO 8601 datetime format:

<dateTime.iso8601>YYYYMMDDTHH:mm:ss±HH:mm<dateTime.iso8601>

Any transaction amount is represented as it's cent value therefore an integer rather than a decimal.

- R100.50 is therefore represented as 10050 rand cents.

- $10.50 is therefore represented as 1050 dollar cents.

The field optionalData is mandatory but its contents are optional. It accepts an XML-RPC struct, for example:
<struct/>
or:
<struct><member><name>recipientPostalCode</name><value><string>10260</string></value></member></struct>
