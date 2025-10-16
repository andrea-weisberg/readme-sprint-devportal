---
title: Response codes
deprecated: false
hidden: false
metadata:
  robots: index
original_path: chargeback-api
---
<h2>Error response code 400</h2>
<p>An error response code of 400 indicates client authentication failure. The response message will contain a &#8220;responseCode&#8221; of 0 and the &#8220;responseMessage&#8221; will contain either of the below values:</p>



<!-- unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"responseMessage"},{"c":"Definition"}],"caption":false,"body":[[{"c":"invalid_client"},{"c":"Client authentication failed"}],[{"c":"unauthorized_client"},{"c":"Client is not allowed to generate or refresh tokens."}]]}} -->


<h2>Error response code 422</h2>
<p>An error response code of 422 indicates validation errors. The response message will advise which field name was unable to be validated and the error type.</p>
<ul>
<li><strong>EMPTY</strong> &#8211; field is empty when it is mandatory</li>
<li><strong>INVALID_VALUE</strong> &#8211; the value provided for the field is invalid</li>
</ul>



<!-- spacing: desktop=20, mobile=10 -->


<h2>Error response code 500</h2>
<p>An error response code of 500 will contain an error response message with the &#8220;responseCode&#8221; and &#8220;responseMessage&#8221;. Below is the full list of responses that may be returned.</p>



<!-- spacing: desktop=20, mobile=10 -->


<!-- unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"RESPONSE CODE"},{"c":"RESPONSE MESSAGE"},{"c":"APPLICABLE CHARGEBACK API"}],"caption":false,"body":[[{"c":"1"},{"c":"No such method"},{"c":"First Chargeback"}],[{"c":"2"},{"c":"No card found for tracking number: {trackingNumber} "},{"c":"First Chargeback"}],[{"c":"10"},{"c":"No authorizations found"},{"c":"First Chargeback"}],[{"c":"11"},{"c":"Multiple matching authorizations"},{"c":"First Chargeback"}],[{"c":"12"},{"c":"No clearings found"},{"c":"First Chargeback"}],[{"c":"13"},{"c":"Multiple matching clearings"},{"c":"First Chargeback"}],[{"c":"20"},{"c":"Claim could not be created"},{"c":"First Chargeback"}],[{"c":"21"},{"c":"Error creating claim"},{"c":"First Chargeback"}],[{"c":"30"},{"c":"Chargeback could not be created"},{"c":"First Chargeback"}],[{"c":"31"},{"c":"Error creating chargeback"},{"c":"First Chargeback"}],[{"c":"40"},{"c":"Cannot get chargeback doc"},{"c":"Second Presentment Documents"}],[{"c":"41"},{"c":"Error getting chargeback doc"},{"c":"Second Presentment Documents"}],[{"c":"42"},{"c":"Cannot get chargeback document status"},{"c":"Document Status"}],[{"c":"43"},{"c":"Error getting chargeback status"},{"c":"Document Status"}],[{"c":"44"},{"c":"Cannot find chargeback with chargebackId = $chargebackId and claimId = $claimId"},{"c":"Upload Supporting Document"}],[{"c":"45"},{"c":"Cannot upload chargeback document"},{"c":"Upload Supporting Document"}],[{"c":"46"},{"c":"Error uploading chargeback document"},{"c":"Upload Supporting Document"}],[{"c":"50"},{"c":"Claim could not be retrived"},{"c":"Pre-Arbitration"}],[{"c":"51"},{"c":"Error retrieving claim"},{"c":"Pre-Arbitration"}],[{"c":"52"},{"c":"No chargebacks related to the claim"},{"c":"Pre-Arbitration"}],[{"c":"53"},{"c":"Time limit of SECOND_PRESENTMENT_TIME_LIMIT days has been exceeded"},{"c":"Pre-Arbitration"}],[{"c":"54"},{"c":"No second presentments related to the claim"},{"c":"Pre-Arbitration"}],[{"c":"55"},{"c":"Could not retrieve chargeback detail"},{"c":"Pre-Arbitration"}],[{"c":"56"},{"c":"Could not retrieve second presentment details"},{"c":"Pre-Arbitration"}],[{"c":"58"},{"c":"Case could not be filed"},{"c":"Pre-Arbitration"}],[{"c":"59"},{"c":"Error filing case"},{"c":"Pre-Arbitration"}]]}} -->
