---
title: Chargeback API REFERENCE
deprecated: false
hidden: false
metadata:
  robots: index
---
<!-- MIGRATION_METADATA
Migrated-From: https://developer.sprint.paymentology.com/chargeback-api/chargeback-api-reference/
Source-Slug: chargeback-api-reference
Migrated-On: 2026-02-12T20:19:05+00:00
Migrated-By: wp-readme-migration
-->

The Chargeback API contains the endpoints that you call in order to create chargebacks as well as maintain the chargeback lifecycle.


#### Endpoint

```
https://chargebacks.test.tutuka.cloud
```


# Available methods

- [API Gateway Token & Connectivity](../connectivity) – Generate an authentication token in order to call the rest of the Chargeback API endpoints

- [First Chargeback](first-chargeback) – Submit a new chargeback

- [Upload Supporting Document](upload-supporting-document) – Used to upload a supporting document after a chargeback is successfully created.

- [Document Status](document-status) – Use this endpoint to verify the status of document.

- [Second Presentment Documents](second-presentment-documents) – Once in the 2nd Presentment phase, this endpoint is used to receive the supporting documents raised by the acquirer for a claim.

- [Pre-Arbitration](pre-arbitration) – Used to submit submit a Pre-Arbitration case.

- [Query Chargeback](query-chargeback) – Used to query chargeback data.


---
