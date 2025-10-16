---
title: Connectivity
deprecated: false
hidden: false
metadata:
  robots: index
original_path: chargeback-api
---
<p>This page explains how to connect to our Chargeback API gateway.<br />
Connecting to the Chargeback API means you can automate submissions of your chargebacks.</p>



<!-- spacing: desktop=20, mobile=10 -->


<h2>IP/Host details</h2>



<!-- unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"ENVIRONMENT"},{"c":"SERVICE"},{"c":"IP/HOST"},{"c":"PORT"},{"c":"URI"}],"caption":false,"body":[[{"c":"SIT/UAT"},{"c":"First chargeback"},{"c":"chargebacks.test.tutuka.cloud"},{"c":"443"},{"c":"https://chargebacks.test.tutuka.cloud/client/"}],[{"c":"PROD"},{"c":"First chargeback"},{"c":"chargebacks.prod.tutuka.cloud"},{"c":"443"},{"c":"https://chargebacks.prod.tutuka.cloud/client/"}]]}} -->


<!-- spacing: desktop=20, mobile=10 -->


<h2>API Gateway token</h2>
<p>Below are the default specifications for the <em><strong>token bearer </strong></em>details for authentication as reflected in the First Chargeback example <a href="https://developer.sprint.paymentology.com/chargeback-api/chargeback-api-reference/first-chargeback/">here</a>.</p>



<!-- unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":""},{"c":""}],"caption":false,"body":[[{"c":"HTTP Method"},{"c":"POST"}],[{"c":"URL+URI (SIT/UAT)"},{"c":"https://chargebacks.test.tutuka.cloud/token/generate"}],[{"c":"URL+URI (PROD)"},{"c":"https://chargebacks.prod.tutuka.cloud/token/generate"}],[{"c":"HTTP Headers"},{"c":"Content-Type = application/x-www-form-urlencoded"}],[{"c":"Query String Parameters"},{"c":"None"}],[{"c":"Format"},{"c":"JSON"}],[{"c":"Authentication"},{"c":"Basic BASE64_ENCODED_CREDENTIALS(user:pass)"}],[{"c":"Request"},{"c":"None"}],[{"c":"Success Response Code"},{"c":"200"}],[{"c":"Success Response"},{"c":"{\n \"access_token\": \"ACCESS_TOKEN\",\n \"expires_in\": TIME_IN_SECONDS,\n \"token_type\": \"Bearer\"\n}\n"}],[{"c":"Error Response Code"},{"c":"400"}],[{"c":"Error Response"},{"c":"{\n \"responseCode\": 0\",\n \"responseMessage\": \"invalid_client\|unauthorized_client\"\n}"}],[{"c":"Response Messages"},{"c":"Invalid_client - Client authentication failed.\nUnauthorized_client - client is not allowed to generate or refresh tokens."}]]}} -->


<!-- spacing: desktop=20, mobile=10 -->


<h4>Other response codes</h4>
<p>Further response codes and details can be found <a href="https://developer.sprint.paymentology.com/chargeback-api/response-codes/">here</a>.</p>
