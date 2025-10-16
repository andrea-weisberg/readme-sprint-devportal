---
title: Card API REFERENCE
deprecated: false
hidden: false
metadata:
  robots: index
---
<p>The Card API contains the API and API methods that we use to call you to send transactions on to the store of value for authorizations. Transactions originate from the merchant and are sent to Paymentology via the financial networks and then are forwarded to the store of value for authorization.</p>
<p id="intro"><strong>Note:</strong> You will need to implement the relevant method names corresponding to the different calls in order to perform the necessary actions on your system.</p>



\{/* unsupported_acf_block: api_endpoint_example {"acf_fc_layout":"api_endpoint_example","endpoint":"https://apidev.voucherengine.com/card/v1/xmlrpc.cfm"\} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h1>Available methods</h1>
<ul>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/activatetoken/">ActivateToken</a> – Used to activate a token that has been approved and provisioned</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/addcardtag/">AddCardTag</a> – Add a Tag Name and Tag Value to a card identified by tracking number</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/addpocket/">AddPocket</a> – Add a pocket for the type indicated by UUID to a card identified by tracking number</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/bearerdetail/">BearerDetail</a> – Get the details of the bearer that is identified by the given tracking number</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/calculatetav/">CalculateTAV</a> – This API is used to create Token Authentication Value (TAV)</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/carddetail/">CardDetail</a> – Get the details of a card that is identified by the given tracking number</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/changepin/">ChangePin</a> – Change the pin on the card associated with the customer reference and tracking number</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/createvirtualcard/">CreateVirtualCard</a> – Create a virtual card in the campaign identified by its UUID and linked to the customer reference given</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/createvirtualcardwithload/">CreateVirtualCardWithLoad</a> – Create a virtual card in the campaign identified by its UUID and linked to the customer reference given and loads the card</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/deductfunds/">DeductFunds</a> – Deducts the requested amount from a card, or a pocket if applicable</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/deductfundsreverse/">DeductFundsReverse</a> – Reverse a deduct that was previously requested but had potentially failed</li>
<li><a href="https://developer.sprint.paymentology.com/deletetoken-2/">DeleteToken</a> – Remove a payment token linked to a card</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/devalue/">Devalue</a> – Deducts the requested amount from a card, or pocket if specified, with a redemption type of “Devalue”</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/devaluereverse/">DevalueReverse</a> – Reverse a devalue that was previously requested but had potentially failed</li>
<li><a href="https://developer.sprint.paymentology.com/generatetimebasedsecret/">GenerateTimeBasedSecret</a> – Create a one-time based secret</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/inserttransactionfee/">InsertTransactionFee</a> – Charge a fee to a card (or pocket if applicable)</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/linkcard/">LinkCard</a> – Link an existing card to a given customer reference</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/listalltokens/">ListAllTokens </a>– Returns all the tokens (active and inactive) linked to a card</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/listcards/">ListCards</a> – Return a list of all cards that are linked to the customer reference</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/listtokens/">ListTokens</a> – Returns all the tokens linked to a card</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/loadfunds/">LoadFunds</a> – Load a card (or pocket if applicable) with the requested amount</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/loadfundsreverse/">LoadFundsReverse</a> – Reverse a load that was previously requested but has potentially failed</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/mostrecenttransactions/">MostRecentTransactions</a> – Provides the latest transactions on a card based on date range and transaction count.</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/ordercard/">OrderCard</a> – Order a card for a specific cardholder. A card can be printed with cardholder details by the card manufacturer.</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/ordercardwithpinblock/">OrderCardWithPinBlock</a> – Order a card for a specific cardholder with a pin block. A card can be printed with cardholder details by the card manufacturer.</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/pockettransfer/">PocketTransfer</a> – Transfer funds between two pockets linked to a card identified by tracking number</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/pockettransferreverse/">PocketTransferReverse</a> – Reverse an PocketTransfer transaction that was timed out using the details of the failed transaction</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/retirecard/">RetireCard</a> – Permanently disable a card so that it is no longer returned for the customer reference in the ListCards method</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/set3dsecurecode/">Set3DSecureCode</a> – Update the 3D Secure Code on the card associated with the customer reference and tracking number</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/setbearerdetail/">SetBearerDetail</a> – Set the details of the bearer that is identified by the given tracking number</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/statement/">Statement</a> – Retrieve the statement of a card (or pocket if applicable). <em>NB. Version 1.3 available</em></li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/stopcard/">StopCard</a> – Stop a card with one of the allowed (integer) values for stopReasonID</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/stoptoken/">StopToken</a> – Stops a token reference or all the ones linked to a card</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/threedsauthenticationoutcome/">ThreeDSAuthenticationOutcome</a> – Gives the result of the 3D Secure App Authentication.</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/togglevoucherfeature/">ToggleVoucherFeature</a> – Toggles a voucher feature on or off</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/tokenapprovedevicebinding-2/">TokenApproveDeviceBinding</a> – Used to Bind the device with the token</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/tokenremovedevicebinding/">TokenRemoveDeviceBinding</a> – Remove device with the token</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/transferfunds/">TransferFunds</a>– Transfer funds from one card to another identified by tracking numbers, using pockets if applicable of the same type</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/transferfundsreverse/">TransferFundsReverse</a> – Reverse a TransferFunds transaction that was timed out using the details of the failed transaction</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/transferlink/">TransferLink</a> – Transfer a reference to a new card. The old card will be stopped and the bearer details transferred to the new card. The new card will be linked and activated</li>
<li><a href="https://developer.sprint.paymentology.com/transfertoken-2/">TransferToken</a> – Transfer a payment token from one card to another</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/unstopcard/">UnStopCard</a> – Unstop a card</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/unstoptoken/">UnstopToken</a> – Unstops a token reference or all the ones linked to a card</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/updatecardexpirydate/">UpdateCardExpiryDate</a> – Updates the expiry date of a virtual card</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/updatecardlabel/">UpdateCardLabel</a> – Update the card label of a card identified by tracking number</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/updatecvv/">UpdateCVV</a> – Generate a new CVV2 of the specified card</li>
<li><a href="https://developer.sprint.paymentology.com/card-api/api-reference/updatetokenaccount/">UpdateTokenAccount</a> – Updates the card PAN information associated with a token</li>
</ul>



\{/* unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"\} */}


<h1><a href="https://developer.sprint.paymentology.com/remotemessaging/">Remote Messaging API</a> for Non-Companion clients</h1>
<p>The Remote Messaging API is hosted on your platform and allows us to call you to send administrative advice messages.</p>
<ul>
<li><a href="https://developer.sprint.paymentology.com/remotemessaging/#appauth">3DSecure.AppAuthentication</a></li>
<li><a href="https://developer.sprint.paymentology.com/remotemessaging/#appfinal">3DSecure.AppFinalisation</a></li>
<li><a href="https://developer.sprint.paymentology.com/remotemessaging/#3DSecure">3DSecure.OTP</a></li>
<li><a href="https://developer.sprint.paymentology.com/remotemessaging/#3DSecureCCD">3DSecure Cardholder’s Contact Detail Collection</a></li>
<li><a href="https://developer.sprint.paymentology.com/remotemessaging/#activation">digitization.activation</a></li>
<li><a href="https://developer.sprint.paymentology.com/remotemessaging/#activationmethods">digitization.activationmethods</a></li>
<li><a href="https://developer.sprint.paymentology.com/remotemessaging/#event">digitization.event</a></li>
<li><a href="https://developer.sprint.paymentology.com/remotemessaging/#responsereference">Response Reference</a></li>
</ul>
