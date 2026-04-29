---
title: Help
deprecated: false
hidden: false
metadata:
  robots: index
---
## About the Checksum Generator

The Checksum Generator is used to verify that the checksum calculation is correct and that it arrives at the same checksum result as our system.

## Testing with the Checksum Generator

Do this: Check the request data string matches the XML that is being sent (minus the XML tags). For example:

```xml
<?xml version="”1.0″?>
<methodCall>
  <methodName>Status</methodName>
  <params>
    <param><value><string>100123</string></value></param>
    <param><value><string>ref</string></value></param>
    <param><value><string>45556</string></value></param>
    <param><value><string>123</string></value></param>
    <param><value><dateTime.iso8601>20170223T12:00:00</dateTime.iso8601></value></param>
    <param><value><string>B4919AC22BAE3E2FFC4373C7A9B478A096BF1CB2</string></value></param>
  </params>
</methodCall>
````

The above would have a request data string (minus the checksum itself which of course isn’t an input to the calculation) of:

```
Status100123ref4555612320170223T12:00:00
```

## How to use Checksum Generator

1. Go to [Checksum Generator](.) under [Tools](..)
2. Enter your terminal password in the “Private Key” field
3. Enter the request data in the “String to hash” field
4. Click “Submit”
5. Wait for the “Transaction Result Pop-up” that will display the calculated checksum together with the details behind the calculation
