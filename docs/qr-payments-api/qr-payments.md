---
title: QR payments
deprecated: false
hidden: false
metadata:
  robots: index
---
<p><span style="font-weight: 400;">The QR payments API allows you to create a contactless merchant payment system where customers can make electronic payments by scanning a QR code from a smartphone application. It’s a simple and secure way for consumers to push payments to merchants using their mobile money wallets or bank account balances. </span></p>
<p><span style="font-weight: 400;">Tutuka allows integration into </span><b>Mastercard QR</b><b> </b><span style="font-weight: 400;">for the issuing and acceptance of QR payments, offering a safe, innovative way for consumers to scan and pay. Since it works as a plug-in to virtual or physical cards, having an existing virtual or physical PAN number allows for quicker and easier implementation of QR payments.</span></p>



\{/* spacing: desktop=20, mobile=10 */\}


<h2>Benefits of QR payments</h2>



\{/* spacing: desktop=20, mobile=10 */\}


\{/* unsupported_acf_block: columns_with_icons_and_text {"acf_fc_layout":"columns_with_icons_and_text","title":"","block_variant":"Variant 1","columns":[{"column_width":"1/3","icon":{"ID":215,"id":215,"title":"icon-secure-card5","filename":"icon-secure-card5.png","filesize":862,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card5.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card5/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card5","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:06","modified":"2020-04-02 16:39:06","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":52,"height":38,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card5.png","thumbnail-width":52,"thumbnail-height":38,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card5.png","medium-width":52,"medium-height":38,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card5.png","medium_large-width":52,"medium_large-height":38,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card5.png","large-width":52,"large-height":38,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card5.png","1536x1536-width":52,"1536x1536-height":38,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card5.png","2048x2048-width":52,"2048x2048-height":38\}},"title":"","text":"<p><span style=\"font-weight: 400;\">Customers can make cashless payments using their smartphones without needing bank accounts or physical plastic cards.</span></p>\n","link":""},\{"column_width":"1/3","icon":{"ID":41,"id":41,"title":"home-icon-digital","filename":"home-icon-digital.png","filesize":613,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/home-icon-digital.png","link":"https://developer.sprint.paymentology.com/home/home-icon-digital/","alt":"Digital Icon","author":"1","description":"","caption":"","name":"home-icon-digital","status":"inherit","uploaded_to":8,"date":"2020-04-01 13:39:21","modified":"2020-04-01 13:39:26","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":51,"height":67,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/home-icon-digital.png","thumbnail-width":51,"thumbnail-height":67,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/home-icon-digital.png","medium-width":51,"medium-height":67,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/home-icon-digital.png","medium_large-width":51,"medium_large-height":67,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/home-icon-digital.png","large-width":51,"large-height":67,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/home-icon-digital.png","1536x1536-width":51,"1536x1536-height":67,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/home-icon-digital.png","2048x2048-width":51,"2048x2048-height":67\}},"title":"","text":"<p><span style=\"font-weight: 400;\">Low cost to issue digital products.</span></p>\n","link":""},\{"column_width":"1/3","icon":{"ID":165,"id":165,"title":"issue-card-icon1","filename":"issue-card-icon1.png","filesize":1016,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/issue-card-icon1.png","link":"https://developer.sprint.paymentology.com/companion-api/secure-cards/issue-card-icon1/","alt":"","author":"1","description":"","caption":"","name":"issue-card-icon1","status":"inherit","uploaded_to":157,"date":"2020-04-02 13:35:39","modified":"2020-04-02 13:35:39","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":49,"height":48,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/issue-card-icon1.png","thumbnail-width":49,"thumbnail-height":48,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/issue-card-icon1.png","medium-width":49,"medium-height":48,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/issue-card-icon1.png","medium_large-width":49,"medium_large-height":48,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/issue-card-icon1.png","large-width":49,"large-height":48,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/issue-card-icon1.png","1536x1536-width":49,"1536x1536-height":48,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/issue-card-icon1.png","2048x2048-width":49,"2048x2048-height":48\}},"title":"","text":"<p><span style=\"font-weight: 400;\">QR payments are instant, safe, and secure.</span></p>\n","link":""}]} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>How QR payments work</h2>
<p><span style="font-weight: 400;">QR payments involve a four-party model where transactions occur between an Originating Institution (OI), the cardholder’s bank, a Receiving Institution (RI), and the merchant’s bank.</span></p>
<p><span style="font-weight: 400;">This is a typical QR transaction process:</span></p>
<ol>
<li style="font-weight: 400;"><span style="font-weight: 400;">The cardholder initiates a QR payment transaction in which they pay by scanning the QR code the merchant displays at the point of sale. </span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">The merchant sends the transaction to the OI.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">The OI verifies the available funds and debits the cardholder’s bank account. </span></li>
<li><span style="font-weight: 400;">The OI sends the payment to the RI.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">The RI credits the merchant’s bank account and sends a notification that the payment has been received successfully.</span></li>
</ol>



<p><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-1655" src="https://developer.sprint.paymentology.com/wp-content/uploads/2023/03/QR-Payments-End-to-end-v2.png" alt="End to end - how QR payments work" width="8000" height="4500" /></p>



\{/* spacing: desktop=20, mobile=10 */\}


<h2>About the Originating Institution (OI)</h2>
<p><span style="font-weight: 400;">The Originating Institution (OI) is the store of value provider that issues the customer’s card or account. </span>When the consumer initiates a QR Payment transaction by scanning the merchants static QR code, the OI verifies the available funds on the consumer’s account and debits it. To transfer a QR payment to a merchant, you’ll need to make a call to the <span class="xml-highlight">​TransferPaymentToMerchant</span> method.</p>



<p><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-1656" src="https://developer.sprint.paymentology.com/wp-content/uploads/2023/03/QR-Payments-send-bank-v2-1.png" alt="" width="7982" height="4482" /></p>



\{/* unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21\}},"text":"<p>To transfer a QR payment to a merchant, you’ll need to make a call to the <span class=\"xml-highlight\">TransferPaymentToMerchant method</span>.</p>\n"}]} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>OI reports</h2>
<p><span style="font-weight: 400;">A report will be generated daily for all transactions that come from the OI. In an ideal situation, the payments pulled from the Originating Institution should match those pushed to the Receiving Institution.</span></p>



\{/* unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21\}},"text":"<p><span style=\"font-weight: 400;\">You can access the report by making an HTTP GET request and downloading it as a CSV file. </span></p>\n"}]} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>About the Receiving Institution (RI)</h2>
<p><span style="font-weight: 400;">The Receiving Institution (RI) is the bank that holds the merchant’s account. The RI credits the merchant’s bank account and sends a notification that the payment has been received successfully.</span></p>
<p><span style="font-weight: 400;">The RI can make the following API requests:</span></p>
<ul>
<li>Make a call to the <span class="xml-highlight">Load method</span> to load funds onto the merchant’s wallet. If making the API request does not return any response, a timeout occurs, or an incorrect response code is returned, then a reversal will be triggered.</li>
<li>Make a call to the <span class="xml-highlight">LoadReversal method</span> to reverse the loaded funds from a merchant’s wallet. If there is no response returned, a timeout occurs, or an incorrect response code is returned, then a reversal will be triggered.</li>
</ul>



<p><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-1657" src="https://developer.sprint.paymentology.com/wp-content/uploads/2023/03/QR-Payments-receive-bank-v2.png" alt="" width="7999" height="4499" /></p>



\{/* unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21\}},"text":"<p><span style=\"font-weight: 400;\">It will be triggered ten times at 5-minute intervals until a valid response code is returned; thereafter, it results in a fail that Tutuka flags.</span></p>\n"}]} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Using the SimPOS tool</h2>
<p>The <a href="https://developer.sprint.paymentology.com/tools/simpos/">SimPOS tool</a> can be used to facilitate a load to a merchant or a card, as well as an OI load.</p>



\{/* spacing: desktop=20, mobile=10 */\}


<h2>Onboarding merchants</h2>
<p><span style="font-weight: 400;">Before a merchant can accept QR payments, you’ll need to onboard them first and create their QR data in the required format, as stipulated by the card scheme.</span></p>
<h3>Onboarding with Mastercard</h3>
<p>To create the QR code, you’ll use the Mastercard QR generator. You should ensure that the correct data is imported into the generator.</p>



<p><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-1658" src="https://developer.sprint.paymentology.com/wp-content/uploads/2023/03/QR-Payments-Merchant-onboarding-v2.png" alt="" width="7999" height="4499" /></p>



\{/* unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21\}},"text":"<p>To produce the correct image, be mindful of any spaces at the beginning and end of the data inputs. Lastly, you can download the MasterPass QR Tester App to test that the QR code is correct and meets all Mastercard’s specifications.</p>\n"}]} */}


\{/* spacing: desktop=20, mobile=10 */\}


<p>To onboard your merchants, you’ll need to make a call to the Tutuka’s <span class="xml-highlight">CreateQRData method</span>. This method allows you to create a QR code that your merchant can display to enable them to receive payments.</p>



\{/* spacing: desktop=20, mobile=10 */\}


<p>The <span class="xml-highlight">CreateQRData method</span> accepts the following arguments:</p>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;"><span class="xml-highlight">terminalID</span></span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;"><span class="xml-highlight">merchantCategoryCode</span></span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;"><span class="xml-highlight">merchantName</span></span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;"><span class="xml-highlight">merchantCity</span></span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;"><span class="xml-highlight">countryCode</span></span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;"><span class="xml-highlight">reference</span></span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;"><span class="xml-highlight">transactionID</span></span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;"><span class="xml-highlight">transactionDate</span></span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;"><span class="xml-highlight">optionalData</span></span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;"><span class="xml-highlight">checksum</span></span></li>
</ul>
<p> </p>



\{/* spacing: desktop=20, mobile=10 */\}


<p><span style="font-weight: 400;">Broadly speaking, the above arguments can be categorized into two types of data: </span><b>authentication data </b><span style="font-weight: 400;">and </span><b>merchant QR data</b><span style="font-weight: 400;">.</span></p>
<h3>a) Authentication data</h3>
<p><span style="font-weight: 400;">The </span><span class="xml-highlight">terminalID</span><span style="font-weight: 400;"> and </span><span class="xml-highlight">checksum</span><span style="font-weight: 400;"> fields are used to ensure the validity of transactions. These fields authenticate that the same data returned by Tutuka is received by you and sent back securely. You can think of the </span><span class="xml-highlight">terminalID</span><span style="font-weight: 400;"> field and </span><span class="xml-highlight">checksum</span><span style="font-weight: 400;"> field as a username and a password. </span></p>
<p><span style="font-weight: 400;">The </span><span class="xml-highlight">terminalID</span> <span style="font-weight: 400;">is</span> <span style="font-weight: 400;">specific to you, and you only. Only Tutuka will know the password associated with that </span><span class="xml-highlight">terminalID</span><span style="font-weight: 400;">.</span><b> </b></p>
<p><span style="font-weight: 400;">The </span><span class="xml-highlight">checksum</span> <span style="font-weight: 400;">is more than just a simple password—it is a string generated from the actual method name and the text content of every field in the transaction encrypted against your private key (or actual password). It guarantees the authentication as well as the integrity of every piece of data within the transaction.</span></p>
<p><b>Note:</b><span style="font-weight: 400;"> You will be required to generate your own checksum and send it to Tutuka. We will then recalculate the checksum to ensure that no field has been tampered with. Only if both checksums are the same will the transaction be authenticated and verified.</span></p>
<p><span style="font-weight: 400;">You can use </span>Tutuka’s <a href="https://developer.sprint.paymentology.com/tools/checksum-generator/">Checksum Generator tool</a><span style="font-weight: 400;"> to test the checksum generation and implementation process manually.</span></p>



\{/* spacing: desktop=20, mobile=10 */\}


<h3>b) Merchant QR data</h3>
<p><span style="font-weight: 400;">The </span><span class="xml-highlight">merchantCategoryCode</span><span style="font-weight: 400;">, </span><span class="xml-highlight">merchantName</span><span style="font-weight: 400;">, </span><span class="xml-highlight">merchantCity</span><span style="font-weight: 400;"> and </span><span class="xml-highlight">countryCode</span><span style="font-weight: 400;"> fields provide more details about the merchant.</span></p>
<p><span style="font-weight: 400;">The </span><span class="xml-highlight">reference</span><span style="font-weight: 400;"> field is the unique customer reference or identifier number on your system. This reference will be linked to the unique PAN, which payments will be loaded to before it is passed to the wallet.</span></p>
<p><span style="font-weight: 400;">After making a call to the <span class="xml-highlight">CreateQRData method</span>, the following data elements will be returned:</span></p>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;"><span class="xml-highlight">resultCode</span></span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;"><span class="xml-highlight">cardnumber</span></span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;"><span class="xml-highlight">resulttext</span></span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;"><span class="xml-highlight">qrCodeImage</span></span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;"><span class="xml-highlight">qrCodeString</span></span></li>
</ul>
