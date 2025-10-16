---
title: QR payments
deprecated: false
hidden: false
metadata:
  robots: index
---
<p><span style={{fontWeight: "400"}}>The QR payments API allows you to create a contactless merchant payment system where customers can make electronic payments by scanning a QR code from a smartphone application. It’s a simple and secure way for consumers to push payments to merchants using their mobile money wallets or bank account balances. </span></p>
<p><span style={{fontWeight: "400"}}>Tutuka allows integration into </span><b>Mastercard QR</b><b> </b><span style={{fontWeight: "400"}}>for the issuing and acceptance of QR payments, offering a safe, innovative way for consumers to scan and pay. Since it works as a plug-in to virtual or physical cards, having an existing virtual or physical PAN number allows for quicker and easier implementation of QR payments.</span></p>

<h2>Benefits of QR payments</h2>

<h2>How QR payments work</h2>
<p><span style={{fontWeight: "400"}}>QR payments involve a four-party model where transactions occur between an Originating Institution (OI), the cardholder’s bank, a Receiving Institution (RI), and the merchant’s bank.</span></p>
<p><span style={{fontWeight: "400"}}>This is a typical QR transaction process:</span></p>
<ol>
<li style={{fontWeight: "400"}}><span style={{fontWeight: "400"}}>The cardholder initiates a QR payment transaction in which they pay by scanning the QR code the merchant displays at the point of sale. </span></li>
<li style={{fontWeight: "400"}}><span style={{fontWeight: "400"}}>The merchant sends the transaction to the OI.</span></li>
<li style={{fontWeight: "400"}}><span style={{fontWeight: "400"}}>The OI verifies the available funds and debits the cardholder’s bank account. </span></li>
<li><span style={{fontWeight: "400"}}>The OI sends the payment to the RI.</span></li>
<li style={{fontWeight: "400"}}><span style={{fontWeight: "400"}}>The RI credits the merchant’s bank account and sends a notification that the payment has been received successfully.</span></li>
</ol>

<p>**QR-Payments-End-to-end-v2.png IMAGE GOES HERE.**</p>

<h2>About the Originating Institution (OI)</h2>
<p><span style={{fontWeight: "400"}}>The Originating Institution (OI) is the store of value provider that issues the customer’s card or account. </span>When the consumer initiates a QR Payment transaction by scanning the merchants static QR code, the OI verifies the available funds on the consumer’s account and debits it. To transfer a QR payment to a merchant, you’ll need to make a call to the <span className="xml-highlight">​TransferPaymentToMerchant</span> method.</p>

<p>**QR-Payments-send-bank-v2-1.png IMAGE GOES HERE.**</p>

<h2>OI reports</h2>
<p><span style={{fontWeight: "400"}}>A report will be generated daily for all transactions that come from the OI. In an ideal situation, the payments pulled from the Originating Institution should match those pushed to the Receiving Institution.</span></p>

<h2>About the Receiving Institution (RI)</h2>
<p><span style={{fontWeight: "400"}}>The Receiving Institution (RI) is the bank that holds the merchant’s account. The RI credits the merchant’s bank account and sends a notification that the payment has been received successfully.</span></p>
<p><span style={{fontWeight: "400"}}>The RI can make the following API requests:</span></p>
<ul>
<li>Make a call to the <span className="xml-highlight">Load method</span> to load funds onto the merchant’s wallet. If making the API request does not return any response, a timeout occurs, or an incorrect response code is returned, then a reversal will be triggered.</li>
<li>Make a call to the <span className="xml-highlight">LoadReversal method</span> to reverse the loaded funds from a merchant’s wallet. If there is no response returned, a timeout occurs, or an incorrect response code is returned, then a reversal will be triggered.</li>
</ul>

<p>**QR-Payments-receive-bank-v2.png IMAGE GOES HERE.**</p>

<h2>Using the SimPOS tool</h2>
<p>The <a href="https:developer.sprint.paymentology.com/tools/simpos/">SimPOS tool</a> can be used to facilitate a load to a merchant or a card, as well as an OI load.</p>

<h2>Onboarding merchants</h2>
<p><span style={{fontWeight: "400"}}>Before a merchant can accept QR payments, you’ll need to onboard them first and create their QR data in the required format, as stipulated by the card scheme.</span></p>
<h3>Onboarding with Mastercard</h3>
<p>To create the QR code, you’ll use the Mastercard QR generator. You should ensure that the correct data is imported into the generator.</p>

<p>**QR-Payments-Merchant-onboarding-v2.png IMAGE GOES HERE.**</p>

<p>To onboard your merchants, you’ll need to make a call to the Tutuka’s <span className="xml-highlight">CreateQRData method</span>. This method allows you to create a QR code that your merchant can display to enable them to receive payments.</p>

<p>The <span className="xml-highlight">CreateQRData method</span> accepts the following arguments:</p>
<ul>
<li style={{fontWeight: "400"}}><span style={{fontWeight: "400"}}><span className="xml-highlight">terminalID</span></span></li>
<li style={{fontWeight: "400"}}><span style={{fontWeight: "400"}}><span className="xml-highlight">merchantCategoryCode</span></span></li>
<li style={{fontWeight: "400"}}><span style={{fontWeight: "400"}}><span className="xml-highlight">merchantName</span></span></li>
<li style={{fontWeight: "400"}}><span style={{fontWeight: "400"}}><span className="xml-highlight">merchantCity</span></span></li>
<li style={{fontWeight: "400"}}><span style={{fontWeight: "400"}}><span className="xml-highlight">countryCode</span></span></li>
<li style={{fontWeight: "400"}}><span style={{fontWeight: "400"}}><span className="xml-highlight">reference</span></span></li>
<li style={{fontWeight: "400"}}><span style={{fontWeight: "400"}}><span className="xml-highlight">transactionID</span></span></li>
<li style={{fontWeight: "400"}}><span style={{fontWeight: "400"}}><span className="xml-highlight">transactionDate</span></span></li>
<li style={{fontWeight: "400"}}><span style={{fontWeight: "400"}}><span className="xml-highlight">optionalData</span></span></li>
<li style={{fontWeight: "400"}}><span style={{fontWeight: "400"}}><span className="xml-highlight">checksum</span></span></li>
</ul>
<p> </p>

<p><span style={{fontWeight: "400"}}>Broadly speaking, the above arguments can be categorized into two types of data: </span><b>authentication data </b><span style={{fontWeight: "400"}}>and </span><b>merchant QR data</b><span style={{fontWeight: "400"}}>.</span></p>
<h3>a) Authentication data</h3>
<p><span style={{fontWeight: "400"}}>The </span><span className="xml-highlight">terminalID</span><span style={{fontWeight: "400"}}> and </span><span className="xml-highlight">checksum</span><span style={{fontWeight: "400"}}> fields are used to ensure the validity of transactions. These fields authenticate that the same data returned by Tutuka is received by you and sent back securely. You can think of the </span><span className="xml-highlight">terminalID</span><span style={{fontWeight: "400"}}> field and </span><span className="xml-highlight">checksum</span><span style={{fontWeight: "400"}}> field as a username and a password. </span></p>
<p><span style={{fontWeight: "400"}}>The </span><span className="xml-highlight">terminalID</span> <span style={{fontWeight: "400"}}>is</span> <span style={{fontWeight: "400"}}>specific to you, and you only. Only Tutuka will know the password associated with that </span><span className="xml-highlight">terminalID</span><span style={{fontWeight: "400"}}>.</span><b> </b></p>
<p><span style={{fontWeight: "400"}}>The </span><span className="xml-highlight">checksum</span> <span style={{fontWeight: "400"}}>is more than just a simple password—it is a string generated from the actual method name and the text content of every field in the transaction encrypted against your private key (or actual password). It guarantees the authentication as well as the integrity of every piece of data within the transaction.</span></p>
<p><b>Note:</b><span style={{fontWeight: "400"}}> You will be required to generate your own checksum and send it to Tutuka. We will then recalculate the checksum to ensure that no field has been tampered with. Only if both checksums are the same will the transaction be authenticated and verified.</span></p>
<p><span style={{fontWeight: "400"}}>You can use </span>Tutuka’s <a href="https:developer.sprint.paymentology.com/tools/checksum-generator/">Checksum Generator tool</a><span style={{fontWeight: "400"}}> to test the checksum generation and implementation process manually.</span></p>

<h3>b) Merchant QR data</h3>
<p><span style={{fontWeight: "400"}}>The </span><span className="xml-highlight">merchantCategoryCode</span><span style={{fontWeight: "400"}}>, </span><span className="xml-highlight">merchantName</span><span style={{fontWeight: "400"}}>, </span><span className="xml-highlight">merchantCity</span><span style={{fontWeight: "400"}}> and </span><span className="xml-highlight">countryCode</span><span style={{fontWeight: "400"}}> fields provide more details about the merchant.</span></p>
<p><span style={{fontWeight: "400"}}>The </span><span className="xml-highlight">reference</span><span style={{fontWeight: "400"}}> field is the unique customer reference or identifier number on your system. This reference will be linked to the unique PAN, which payments will be loaded to before it is passed to the wallet.</span></p>
<p><span style={{fontWeight: "400"}}>After making a call to the <span className="xml-highlight">CreateQRData method</span>, the following data elements will be returned:</span></p>
<ul>
<li style={{fontWeight: "400"}}><span style={{fontWeight: "400"}}><span className="xml-highlight">resultCode</span></span></li>
<li style={{fontWeight: "400"}}><span style={{fontWeight: "400"}}><span className="xml-highlight">cardnumber</span></span></li>
<li style={{fontWeight: "400"}}><span style={{fontWeight: "400"}}><span className="xml-highlight">resulttext</span></span></li>
<li style={{fontWeight: "400"}}><span style={{fontWeight: "400"}}><span className="xml-highlight">qrCodeImage</span></span></li>
<li style={{fontWeight: "400"}}><span style={{fontWeight: "400"}}><span className="xml-highlight">qrCodeString</span></span></li>
</ul>
</span></span></li></span></span></li></span></span></li></span></span></li></span></span></li></ul></span></span></p></span></span></span></p></span></span></span></span></span></span></span></span></span></p></h3></span></a></span></p></span></b></p></span></span></span></p></b></span></span></span></span></span></span></p></span></span></span></span></span></span></span></span></span></p></h3></span></b></span></b></span></p></p></span></span></li></span></span></li></span></span></li></span></span></li></span></span></li></span></span></li></span></span></li></span></span></li></span></span></li></span></span></li></ul></span></p></span></p></p></p></h3></span></p></h2></a></p></h2></p></span></li></span></li></ul></span></p></span></p></h2></span></p></h2></p></span></span></p></h2></p></span></li></span></li></span></li></span></li></span></li></ol></span></p></span></p></h2></h2></span></b></b></span></p></span></p>
