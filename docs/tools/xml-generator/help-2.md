---
title: Help
deprecated: false
hidden: false
metadata:
  robots: index
---
## When to use XML Generator

You will use XML Generator to confirm that XML requests generated through your code are generated with the same request parameters as Paymentology Sprint – including the checksum, to ensure compatibility.

If the XML is identical but the checksums do not match, you can use the **Checksum Generator** tool to work solely on the checksum and debug further.

## Testing with XML Generator

- Check that the request parameters are identical (including spaces).
- When using copy and paste, beware of hidden characters that may not display, but affect the checksum calculation.
- When in doubt, type the data manually.

## How to use XML Generator

1. Go to [XML Poster & Generator](..xml-poster-generator/) under [Tools](..)
2. Select the API you want to create an XMLRPC request for (Companion Local API or Remote API)
3. Select the method you want to create an XMLRPC request for
4. Fill out the method arguments with your own data
5. Enter your terminal password in the **private key** field
6. Click **Create XML RPC Request**
7. Wait for the **Transaction result pop-up** that will contain the generated XML – both unformatted (for transaction purposes) and formatted (for readability purposes)

## When to use XML Poster

You will use XML Poster to post requests created with the XML Generator tool to Paymentology only in cases where there is no other route to take.

For example: When you start testing, you will not have a system in place to call the Companion Local API, so you can use this tool to post requests to the API directly – like when you test your first card.

## Testing with XML Poster

Check the following:

- The XML and checksum needs to be correct.
- It is advisable to use the XML Generator tool to create the XML in the first place, although you can also use the tool to check the validity of the XML created by your own system when you’re ready.

## How to use XML Poster

1. Go to [XML Poster & Generator](..xml-poster-generator/) under [Tools](..)
2. Choose the target API
3. Paste your XML request
4. Click on **Submit**
5. Wait for the **Transaction result pop-up** that will contain the XML response
