---
title: Chargeback API REFERENCE
category:
  uri: Chargeback API
slug: chargeback-api-reference
position: 1
---

The Chargeback API contains the endpoints that you call in order to create chargebacks as well as maintain the chargeback lifecycle.

# Available methods

- [API Gateway Token & Connectivity](/api-reference/chargeback-api/connectivity) - Generate an authentication token in order to call the rest of the Chargeback API endpoints

- [First Chargeback](/api-reference/chargeback-api/first-chargeback) - Submit a new chargeback

- [Upload Supporting Document](/api-reference/chargeback-api/upload-supporting-document) - Used to upload a supporting document after a chargeback is successfully created.

- [Document Status](/api-reference/chargeback-api/document-status) - Use this endpoint to verify the status of document.

- [Second Presentment Documents](/api-reference/chargeback-api/second-presentment-documents) - Once in the 2nd Presentment phase, this endpoint is used to receive the supporting documents raised by the acquirer for a claim.

- [Pre-Arbitration](/api-reference/chargeback-api/pre-arbitration) - Used to submit submit a Pre-Arbitration case.

- [Query Chargeback](/api-reference/chargeback-api/query-chargeback) - Used to query chargeback data.
