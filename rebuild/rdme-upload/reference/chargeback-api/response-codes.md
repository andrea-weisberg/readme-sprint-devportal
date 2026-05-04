---
title: Response codes
category:
  uri: Chargeback API
slug: response-codes
position: 12
---

## Error response code 400

An error response code of 400 indicates client authentication failure. The response message will contain a "responseCode" of 0 and the "responseMessage" will contain either of the below values:

## Error response code 422

An error response code of 422 indicates validation errors. The response message will advise which field name was unable to be validated and the error type.

- **EMPTY** - field is empty when it is mandatory

- **INVALID_VALUE** - the value provided for the field is invalid

## Error response code 500

An error response code of 500 will contain an error response message with the "responseCode" and "responseMessage". Below is the full list of responses that may be returned.
