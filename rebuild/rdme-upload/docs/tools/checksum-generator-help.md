---
title: Help
category:
  uri: Tools
slug: checksum-generator-help
position: 3
parent:
  uri: tools
---

## About the Checksum Generator

The Checksum Generator is used to verify that the checksum calculation is correct and that it arrives at the same checksum result as our system.

## Testing with the Checksum Generator

Do this: Check the request data string matches the XML that is being sent (minus the XML tags). For example:

```xml
<?xml version="1.0"?><methodCall><methodName>Status</methodName><params><param><value><string>100123</string></value></param><param><value><string>ref</string></value></param><param><value><string>45556</string></value></param><param><value><string>123</string></value></param><param><value><dateTime.iso8601>20170223T12:00:00</dateTime.iso8601></value></param><param><value><string>B4919AC22BAE3E2FFC4373C7A9B478A096BF1CB2</string></value></param></params></methodCall>
```

The above would have a request data string (minus the checksum itself which of course isn't an input to the calculation) of:

Status100123ref4555612320170223T12:00:00

**NB.** **During testing, avoid entering any personally identifiable information (PII), such as, user IDs, card numbers or email addresses.**

## How to use Checksum Generator

- Go to [Checksum Generator](/tools/checksum-generator) under [Tools](/tools/tools)

- Enter your terminal password in the "Private Key" field

- Enter the request data in the "String to hash" field

- Click "Submit"

- Wait for the "Transaction Result Pop-up" that will display the calculated checksum together with the details behind the calculation
