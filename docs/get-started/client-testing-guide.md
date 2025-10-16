---
title: Client Testing Guide
deprecated: false
hidden: false
metadata:
  robots: index
original_path: get-started
---
<h2>How to start testing</h2>
<p><span style="font-weight: 400;">Testing with Paymentology&#8217;s Sprint platform is easy. By following the steps below you can safely try out our API functionality:</span></p>
<ol>
<li style="font-weight: 400;"><span style="font-weight: 400;">Sign up</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Get your testing credentials</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Select the correct API </span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Implement API methods with help from our tools</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Download the test scenarios for your API</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Return the signed testing document to us for verification </span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Book an implementation review meeting with us</span></li>
</ol>
<p><span style="font-weight: 400;">Read on to find out exactly how to complete these steps to get your API testing started. If you would like assistance along the way, email implementations@paymentology.com</span><span style="font-weight: 400;"> to book a short call with our Implementations Team</span></p>



<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<h3>1. Sign up for a testing account</h3>
<p><span style="font-weight: 400;">As a first step, you will need to sign up for a testing account. You should receive your test credentials within 24 hours.</span></p>



<!-- spacing: desktop=20, mobile=10 -->


<!-- unsupported_acf_block: sign_up_block {"acf_fc_layout":"sign_up_block","main_text":"Create Testing Account","button_text":"Create an account"} -->


<!-- spacing: desktop=20, mobile=10 -->


<h3>2. <b>Get your testing credentials</b></h3>
<p><span style="font-weight: 400;">Signed up and have an account? Great! You should now have received your testing credentials</span><span style="font-weight: 400;">. </span><span style="font-weight: 400;">Make sure to take note of these and keep them safe as this information is confidential and is used to identify you.</span></p>
<p>&nbsp;</p>
<h3>3. <b>Select the right API</b></h3>
<p><span style="font-weight: 400;">Select </span><span style="color: #0000ff;"><a style="color: #0000ff;" href="https://developer.sprint.paymentology.com/get-started/our-apis/"><span style="font-weight: 400;">the type</span></a></span><span style="font-weight: 400;"> of API that works best for you. We have three distinct APIs.  <strong>It is important that you test the right API</strong>. </span><span style="font-weight: 400;">Depending on the API you choose, the testing credentials will vary as follows:</span></p>
<h2><b>Testing Credentials</b></h2>
<ol>
<li style="font-weight: 400;"><b>Companion and QR API</b><b><br />
</b><span style="font-weight: 400;">Terminal ID</span><span style="font-weight: 400;"><br />
</span><span style="font-weight: 400;">Password/Private Key</span></li>
<li style="font-weight: 400;"><b>Card API</b><b><br />
</b><span style="font-weight: 400;">Terminal ID</span><span style="font-weight: 400;"><br />
</span><span style="font-weight: 400;">Password/Private Key</span><span style="font-weight: 400;"><br />
</span><span style="font-weight: 400;">Campaign UUID</span></li>
</ol>
<p><span style="font-weight: 400;">If you have not yet received any of these details, please</span><a href="https://developer.sprint.paymentology.com/contact-us/"><span style="font-weight: 400;"> reach out</span></a><span style="font-weight: 400;"> to us before proceeding.</span></p>
<p>&nbsp;</p>
<h3>4. <b>Implement the methods per API with help from our tools</b></h3>
<p><span style="font-weight: 400;">Next, please implement the methods for your chosen API</span><span style="font-weight: 400;"><br />
</span><span style="font-weight: 400;"><br />
</span><b>To create and manage your first card, implement the applicable methods.</b></p>
<ul>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/">Companion API</a></li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/">Card API</a></li>
</ul>



<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<h2>Companion API (V2)</h2>
<p>Companion API is composed of Local and Remote methods. Local methods &#8211; you send a request to Paymentology&#8217;s Sprint platform. Remote methods &#8211; Paymentology&#8217;s Sprint platform sends a request to you.</p>
<h3><strong>Local API Testing</strong></h3>
<p>So let&#8217;s create and manage your first Card. Below are a list of important Local API calls you need to implement depending on whether you choose Physical Companion API or Virtual Companion API.</p>
<p>&nbsp;</p>



<!-- spacing: desktop=20, mobile=10 -->


<!-- unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"Companion - Local API","table":{"use_header":true,"header":[{"c":"PHYSICAL COMPANION API"},{"c":"VIRTUAL COMPANION API"}],"caption":false,"body":[[{"c":"OrderCard or OrderCardWithPinBlock"},{"c":"CreateLinkedCards\n<br><i>(Please note: Virtual Cards are created active and linked so you don't need to use the Activate and Link API calls.)</i>"}],[{"c":"LinkCard"},{"c":"GetActiveLinkedCards"}],[{"c":"ActivateCard"},{"c":"StopCard"}],[{"c":"ChangePin"},{"c":"UnstopCard"}],[{"c":"GetActiveLinkedCards"},{"c":"UpdateCVV"}],[{"c":"TransferLink"},{"c":"RetireCard"}],[{"c":"StopCard"},{"c":"Status"}],[{"c":"UnstopCard"},{"c":""}],[{"c":"RetireCard"},{"c":""}],[{"c":"Status"},{"c":""}]]}} -->


<!-- spacing: desktop=20, mobile=10 -->


<p>Please note that these need to be successfully passed before we can implement Remote API calls.</p>



<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<h3>Remote API Testing</h3>
<p>All <strong>Remote API</strong> calls are mandatory and your system needs to be able to process these requests. Remote API calls are applicable to both Virtual and Physical APIs.</p>
<p>&nbsp;</p>



<!-- spacing: desktop=20, mobile=10 -->


<!-- unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"PHYSICAL AND VIRTUAL APIs"}],"caption":false,"body":[[{"c":"Deduct\n"}],[{"c":"DeductAdjustment"}],[{"c":"DeductReversal"}],[{"c":"LoadAdjustment"}],[{"c":"LoadReversal"}],[{"c":"AdministartiveMessage3DSecureOTP"}],[{"c":"AdministrativeMessagedigitization.activation"}],[{"c":"Stop"}],[{"c":"ValidatePIN"}],[{"c":"Balance"}],[{"c":"LoadAuth"}],[{"c":"LoadAuthReversal"}]]}} -->


<!-- spacing: desktop=20, mobile=10 -->


<h3><span style="color: #0000ff;"><a style="color: #0000ff;" href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/">Remote API Testing &#8211; Documentation </a></span></h3>



<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<h2>Card API</h2>
<p>For Card API, most of the API calls are applicable to both the Physical and Virtual Card API. Below we have listed the calls applicable for each.</p>



<!-- spacing: desktop=20, mobile=10 -->


<!-- unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"PHYSICAL CARD API ONLY"},{"c":"VIRTUAL CARD API ONLY"}],"caption":false,"body":[[{"c":"LinkCard"},{"c":"CreateVirtualCard"}],[{"c":"ChangePin"},{"c":"AddPocket"}]]}} -->


<!-- spacing: desktop=20, mobile=10 -->


<!-- unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":"PHYSICAL  AND/OR VIRTUAL CARD APIS (These apply to both) "}],"caption":false,"body":[[{"c":"BearerDetail"}],[{"c":"CardDetail"}],[{"c":"DeductFunds"}],[{"c":"DeductFundsReverse"}],[{"c":"Devalue"}],[{"c":"DevalueReverse"}],[{"c":"PocketTransfer"}],[{"c":"PocketTransferReverse"}],[{"c":"InsertTransactionFee"}],[{"c":"ListCards"}],[{"c":"LoadFunds"}],[{"c":"LoadFundsReverse"}],[{"c":"RetireCard"}],[{"c":"Statement"}],[{"c":"StopCard"}],[{"c":"UnStopCard"}],[{"c":"UpdateCardLabel"}],[{"c":"Set3DSecureCode (Static 3DS)"}],[{"c":"SetBearerDetail"}],[{"c":"ToggleVoucherFeature"}],[{"c":"AddCardTag"}]]}} -->


<!-- spacing: desktop=20, mobile=10 -->


<p>Follow for full <a href="https://developer.sprint.paymentology.com/card-api/">Card API Documentation</a></p>



<!-- spacing: desktop=20, mobile=10 -->


<p><span style="font-weight: 400;">Next, use the following tools to help you with the integration. </span><span style="font-weight: 400;"> These will ensure that you have built your Local API requests correctly. <a href="https://developer.sprint.paymentology.com/tools/">Learn more about our tools.</a></span></p>
<ul>
<li><span style="font-weight: 400;">The <span style="color: #0000ff;"><a style="color: #0000ff;" href="https://developer.sprint.paymentology.com/tools/checksum-generator/">Checksum Generator</a></span>​​ allows you to calculate the checksum for a transaction based on a terminal password value and the request data.​It replicates the same process that happens during authentication. You can use the tool to validate that your own calculated checksum is the same as the one the Paymentology Sprint system generates. </span><span style="font-weight: 400;">The hash algorithm is</span><span style="font-weight: 400;"> </span><span style="font-weight: 400;">SHA256</span><span style="font-weight: 400;"> and is configured by Paymentology – please </span><span style="font-weight: 400;">let us know</span><span style="font-weight: 400;"> which one you will be using.</span></li>
<li><span style="font-weight: 400;">The <span style="color: #0000ff;"><a style="color: #0000ff;" href="https://developer.sprint.paymentology.com/tools/xml-generator/">XML Generator</a></span>​​ allows you to generate a valid XML request (including a checksum string) from your request parameters.​To ensure compatibility, you can use the tool to confirm if your own generated XML requests, including the checksum, are the same with those that Paymentology generates.</span></li>
<li><span style="font-weight: 400;">The <span style="color: #0000ff;"><a style="color: #0000ff;" href="https://developer.sprint.paymentology.com/tools/xml-poster/">XML Poster</a></span>​​ allows you to post XML requests directly to the Paymentology Sprint system. ​In case there is no other route, you can use the XML Poster to post requests created with the XML Generator to the Paymentology Sprint systems.​ For example, at the start of your testing, you’ll not have a system in place for calling the Companion Card Local API; therefore, you can use this tool to post requests to the API directly—such as when creating your first test card.</span></li>
<li><span style="color: #0000ff;"><a style="color: #0000ff;" href="https://developer.sprint.paymentology.com/tools/simpos/">SimPOS</a></span> is a transaction simulator tool that allows you to simulate remote API transactions. For example: you can use SimPOS to test that the flow of virtual card transactions within the Companion Card API is working properly.</li>
</ul>
<p>&nbsp;</p>



<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<!-- spacing: desktop=20, mobile=10 -->


<h2>5. Download the test scenarios for your API</h2>
<p><span style="font-weight: 400;">After you’ve implemented all the methods and you think you’re ready, download the testing scenarios for your chosen API:</span></p>
<h2><strong>Companion API Scenarios</strong></h2>
<ul>
<li><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2022/11/Companion-API-Physical-Card-test-script.xlsx">Companion API Physical Card test script</a></li>
<li><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2022/11/Companion-API-Virtual-Card-test-script.xlsx">Companion API Virtual Card test script</a></li>
</ul>
<h2><strong>Card API Scenarios</strong></h2>
<ul>
<li><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2022/11/Card-API-Physical-Card-test-script.xlsx">Card API Physical Card test script</a></li>
<li><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2022/11/Card-API-Virtual-Card-test-script.xlsx">Card API Virtual Card test script</a></li>
</ul>



<!-- spacing: desktop=20, mobile=10 -->


<!-- unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21}},"text":"<p><b>Please remember: </b><span style=\"font-weight: 400;\">you will need to call each method specified in the script &#8211; and log it with a timestamp.</span></p>\n"}]} -->


<!-- spacing: desktop=20, mobile=10 -->


<h2>6. <b>Return the signed testing document to us for verification</b></h2>
<p><span style="font-weight: 400;">Once done and you have received a positive response<span class="xml-highlight"> (200 code)</span> for every method from the script, please sign the document and send it back to us at </span><a href="mailto:implementations@tutuka.com"><span style="font-weight: 400;">implementations@paymentology.com</span></a></p>
<p>&nbsp;</p>
<h2>7. <b>Success! </b><b>Book a meeting with us so we can review the implementation</b></h2>
<p><span style="font-weight: 400;">Lastly, please book a meeting with our implementations team to review the testing together.</span></p>
<p>&nbsp;</p>
<p><b>Note:</b><span style="font-weight: 400;"> Please allow one business day for the review &#8211; testing must be booked at least </span><b>24 hours</b><span style="font-weight: 400;"> in advance to ensure resource availability.</span></p>
