---
title: Local API
deprecated: false
hidden: false
metadata:
  robots: index
original_path: companion-api/api-reference
---
<p>The Local API contains all the methods available for you to call Paymentology in order to perform the necessary actions on your cards. It includes methods that allow the SVA to create a virtual card, stop a card, or link a physical card. Local API calls are initiated by you.</p>
<p>The Local API is used for administration purposes.</p>



<!-- spacing: desktop=20, mobile=10 -->


<h2>Available Methods</h2>
<ul>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/activatecard/">ActivateCard</a> &#8211; Activate the specified card if the card was initially created as inactive</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/activatetoken/">ActivateToken</a> &#8211; Used to activate a token for a digitization that has been approved and provisioned, but requires additional cardholder authentication prior to activation</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/calculatetav/">CalculateTAV</a> &#8211; Return the TAV (Token Authentication Value) of the specified card. The Token Authentication Value will be returned in Base64 format.</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/changepin/">ChangePin</a> &#8211; Change the specified card&#8217;s PIN</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/createlinkedcard/">CreateLinkedCard</a> &#8211; Create a new, active virtual card and link it to a reference with the given bearer details</li>
<li><a href="https://developer.sprint.paymentology.com/deletetoken/">DeleteToken</a> &#8211; Remove a payment token linked to a card</li>
<li><a href="https://developer.sprint.paymentology.com/generatetimebasedsecret-2/">GenerateTimeBasedSecret</a> &#8211; Create a one-time based secret</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/getactivelinkedcards/">GetActiveLinkedCards</a> &#8211; Get an array of card details of activated cards linked to the reference</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/getcarddetails/">GetCardDetails</a> &#8211; Get card details of a specific card</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/getalllinkedcards/">GetLinkedCards</a> &#8211; Get an array of card details of all cards (active, stopped and retired) linked to the reference</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/linkcard/">LinkCard</a> &#8211; Link a card to a reference with the given bearer details. Linking a card will not activate it</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/listalltokens/">ListAllTokens</a> &#8211; Returns all the tokens (active and inactive) linked to a card</li>
<li><a href="https://developer.sprint.paymentology.com/listtokens/">ListTokens</a> &#8211; Returns all the active tokens linked to a card</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/ordercard/">OrderCard</a> &#8211; Order a card for a specific cardholder. A card can be printed with cardholder details by the card manufacturer</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/ordercardwithpinblock/">OrderCardWithPinBlock</a> &#8211; Order a card for a specific cardholder. A card can be printed with cardholder details by the card manufacturer</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/printlinkedcard/">PrintLinkedCard</a> &#8211; Print the specified card if the card was initially created as virtual</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/printlinkedcardwithpinblock/">PrintLinkedCardWithPINBlock</a> &#8211; Print the specified card if the card was initially created as virtual with PIN block</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/resetpin/">ResetPin</a> &#8211; Reset the specified card&#8217;s PIN. The random pin will be sent to the card bearer&#8217;s cell via text message</li>
<li><a href="https://developer.sprint.paymentology.com/retirecard/">RetireCard</a> &#8211; Retires the specified card</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/status/">Status</a> &#8211; Return the status of the specified card</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/set3dsecurecode/">Set3dSecureCode</a> &#8211; Set 3D Secure Code of the specified card</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/stopcard/">StopCard</a> &#8211; Stop the specified card</li>
<li><a href="https://developer.sprint.paymentology.com/stoptoken/">StopToken</a> – Stops a token reference or all the ones linked to a card. The token or tokens can be unstopped using UnStopToken</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/threedsauthenticationoutcome/">ThreeDSAuthenticationOutcome</a> – Gives the result of the 3D Secure App Authentication</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/togglevoucherfeature/">ToggleVoucherFeature</a> &#8211; Toggles a voucher feature on or off</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/tokenapprovedevicebinding/">TokenApproveDeviceBinding</a> &#8211; Bind the device with token</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/tokenremovedevicebinding/">TokenRemoveDeviceBinding</a> &#8211; Remove device with the token</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/transferlink/">TransferLink</a> &#8211; Transfer a reference to a new card</li>
<li><a href="https://developer.sprint.paymentology.com/transfertoken/">TransferToken</a> &#8211; Transfer a payment token from one card to another</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/unstopcard/">UnstopCard</a> &#8211; Unstop the specified card</li>
<li><a href="https://developer.sprint.paymentology.com/unstoptoken/">UnStopToken</a> – Unstops a token reference or all the ones linked to a card</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/updatebearer/">UpdateBearer</a> &#8211; Update the specified card&#8217;s bearer details</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/updatecvv/">UpdateCVV</a> &#8211; Generate a new CVV2 of the specified card</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/updatetokenaccount/">UpdateTokenAccount</a> &#8211; Updates the card PAN information associated with a token</li>
</ul>



<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<h2>Response Codes</h2>
<p>To access the Response Codes for the Local API, please click <a href="https://developer.sprint.paymentology.com/response-codes/">here</a>.</p>
<p> </p>
<p> </p>
<p> </p>
