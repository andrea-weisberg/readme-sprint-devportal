---
title: Card API REFERENCE
deprecated: false
hidden: false
metadata:
  robots: index
original_path: card-api
---
<p>The Card API contains the API and API methods that we use to call you to send transactions on to the store of value for authorizations. Transactions originate from the merchant and are sent to Paymentology via the financial networks and then are forwarded to the store of value for authorization.</p>
<p id="intro"><strong>Note:</strong> You will need to implement the relevant method names corresponding to the different calls in order to perform the necessary actions on your system.</p>



<!-- unsupported_acf_block: api_endpoint_example {"acf_fc_layout":"api_endpoint_example","endpoint":"https://apidev.voucherengine.com/card/v1/xmlrpc.cfm"} -->


<!-- spacing: desktop=20, mobile=10 -->


<h1>Available methods</h1>
<ul>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/activatetoken/">ActivateToken</a> &#8211; Used to activate a token that has been approved and provisioned</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/addcardtag/">AddCardTag</a> &#8211; Add a Tag Name and Tag Value to a card identified by tracking number</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/addpocket/">AddPocket</a> &#8211; Add a pocket for the type indicated by UUID to a card identified by tracking number</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/bearerdetail/">BearerDetail</a> &#8211; Get the details of the bearer that is identified by the given tracking number</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/calculatetav/">CalculateTAV</a> &#8211; This API is used to create Token Authentication Value (TAV)</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/carddetail/">CardDetail</a> &#8211; Get the details of a card that is identified by the given tracking number</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/changepin/">ChangePin</a> &#8211; Change the pin on the card associated with the customer reference and tracking number</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/createvirtualcard/">CreateVirtualCard</a> &#8211; Create a virtual card in the campaign identified by its UUID and linked to the customer reference given</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/createvirtualcardwithload/">CreateVirtualCardWithLoad</a> &#8211; Create a virtual card in the campaign identified by its UUID and linked to the customer reference given and loads the card</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/deductfunds/">DeductFunds</a> &#8211; Deducts the requested amount from a card, or a pocket if applicable</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/deductfundsreverse/">DeductFundsReverse</a> &#8211; Reverse a deduct that was previously requested but had potentially failed</li>
<li><a href="https://developer.sprint.paymentology.com/deletetoken-2/">DeleteToken</a> &#8211; Remove a payment token linked to a card</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/devalue/">Devalue</a> &#8211; Deducts the requested amount from a card, or pocket if specified, with a redemption type of &#8220;Devalue&#8221;</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/devaluereverse/">DevalueReverse</a> &#8211; Reverse a devalue that was previously requested but had potentially failed</li>
<li><a href="https://developer.sprint.paymentology.com/generatetimebasedsecret/">GenerateTimeBasedSecret</a> &#8211; Create a one-time based secret</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/inserttransactionfee/">InsertTransactionFee</a> &#8211; Charge a fee to a card (or pocket if applicable)</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/linkcard/">LinkCard</a> &#8211; Link an existing card to a given customer reference</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/listalltokens/">ListAllTokens </a>&#8211; Returns all the tokens (active and inactive) linked to a card</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/listcards/">ListCards</a> &#8211; Return a list of all cards that are linked to the customer reference</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/listtokens/">ListTokens</a> &#8211; Returns all the tokens linked to a card</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/loadfunds/">LoadFunds</a> &#8211; Load a card (or pocket if applicable) with the requested amount</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/loadfundsreverse/">LoadFundsReverse</a> &#8211; Reverse a load that was previously requested but has potentially failed</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/mostrecenttransactions/">MostRecentTransactions</a> &#8211; Provides the latest transactions on a card based on date range and transaction count.</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/ordercard/">OrderCard</a> &#8211; Order a card for a specific cardholder. A card can be printed with cardholder details by the card manufacturer.</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/ordercardwithpinblock/">OrderCardWithPinBlock</a> &#8211; Order a card for a specific cardholder with a pin block. A card can be printed with cardholder details by the card manufacturer.</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/pockettransfer/">PocketTransfer</a> &#8211; Transfer funds between two pockets linked to a card identified by tracking number</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/pockettransferreverse/">PocketTransferReverse</a> &#8211; Reverse an PocketTransfer transaction that was timed out using the details of the failed transaction</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/retirecard/">RetireCard</a> &#8211; Permanently disable a card so that it is no longer returned for the customer reference in the ListCards method</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/set3dsecurecode/">Set3DSecureCode</a> &#8211; Update the 3D Secure Code on the card associated with the customer reference and tracking number</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/setbearerdetail/">SetBearerDetail</a> &#8211; Set the details of the bearer that is identified by the given tracking number</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/statement/">Statement</a> &#8211; Retrieve the statement of a card (or pocket if applicable). <em>NB. Version 1.3 available</em></li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/stopcard/">StopCard</a> &#8211; Stop a card with one of the allowed (integer) values for stopReasonID</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/stoptoken/">StopToken</a> &#8211; Stops a token reference or all the ones linked to a card</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/threedsauthenticationoutcome/">ThreeDSAuthenticationOutcome</a> &#8211; Gives the result of the 3D Secure App Authentication.</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/togglevoucherfeature/">ToggleVoucherFeature</a> &#8211; Toggles a voucher feature on or off</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/tokenapprovedevicebinding-2/">TokenApproveDeviceBinding</a> &#8211; Used to Bind the device with the token</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/tokenremovedevicebinding/">TokenRemoveDeviceBinding</a> &#8211; Remove device with the token</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/transferfunds/">TransferFunds</a>&#8211; Transfer funds from one card to another identified by tracking numbers, using pockets if applicable of the same type</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/transferfundsreverse/">TransferFundsReverse</a> &#8211; Reverse a TransferFunds transaction that was timed out using the details of the failed transaction</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/transferlink/">TransferLink</a> &#8211; Transfer a reference to a new card. The old card will be stopped and the bearer details transferred to the new card. The new card will be linked and activated</li>
<li><a href="https://developer.sprint.paymentology.com/transfertoken-2/">TransferToken</a> &#8211; Transfer a payment token from one card to another</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/unstopcard/">UnStopCard</a> &#8211; Unstop a card</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/unstoptoken/">UnstopToken</a> &#8211; Unstops a token reference or all the ones linked to a card</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/updatecardexpirydate/">UpdateCardExpiryDate</a> &#8211; Updates the expiry date of a virtual card</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/updatecardlabel/">UpdateCardLabel</a> &#8211; Update the card label of a card identified by tracking number</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/updatecvv/">UpdateCVV</a> &#8211; Generate a new CVV2 of the specified card</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/updatetokenaccount/">UpdateTokenAccount</a> &#8211; Updates the card PAN information associated with a token</li>
</ul>



<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<h1><a href="https://developer.sprint.paymentology.com/remotemessaging/">Remote Messaging API</a> for Non-Companion clients</h1>
<p>The Remote Messaging API is hosted on your platform and allows us to call you to send administrative advice messages.</p>
<ul>
<li><a href="https://developer.sprint.paymentology.com/remotemessaging/#appauth">3DSecure.AppAuthentication</a></li>
<li><a href="https://developer.sprint.paymentology.com/remotemessaging/#appfinal">3DSecure.AppFinalisation</a></li>
<li><a href="https://developer.sprint.paymentology.com/remotemessaging/#3DSecure">3DSecure.OTP</a></li>
<li><a href="https://developer.sprint.paymentology.com/remotemessaging/#3DSecureCCD">3DSecure Cardholder&#8217;s Contact Detail Collection</a></li>
<li><a href="https://developer.sprint.paymentology.com/remotemessaging/#activation">digitization.activation</a></li>
<li><a href="https://developer.sprint.paymentology.com/remotemessaging/#activationmethods">digitization.activationmethods</a></li>
<li><a href="https://developer.sprint.paymentology.com/remotemessaging/#event">digitization.event</a></li>
<li><a href="https://developer.sprint.paymentology.com/remotemessaging/#responsereference">Response Reference</a></li>
</ul>
