---
title: Local API
deprecated: false
hidden: false
metadata:
  robots: index
---
<p>The Local API contains all the methods available for you to call Paymentology in order to perform the necessary actions on your cards. It includes methods that allow the SVA to create a virtual card, stop a card, or link a physical card. Local API calls are initiated by you.</p>
<p>The Local API is used for administration purposes.</p>

<h2>Available Methods</h2>
<ul>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/activatecard/">ActivateCard</a> – Activate the specified card if the card was initially created as inactive</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/activatetoken/">ActivateToken</a> – Used to activate a token for a digitization that has been approved and provisioned, but requires additional cardholder authentication prior to activation</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/calculatetav/">CalculateTAV</a> – Return the TAV (Token Authentication Value) of the specified card. The Token Authentication Value will be returned in Base64 format.</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/changepin/">ChangePin</a> – Change the specified card’s PIN</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/createlinkedcard/">CreateLinkedCard</a> – Create a new, active virtual card and link it to a reference with the given bearer details</li>
<li><a href="https://developer.sprint.paymentology.com/deletetoken/">DeleteToken</a> – Remove a payment token linked to a card</li>
<li><a href="https://developer.sprint.paymentology.com/generatetimebasedsecret-2/">GenerateTimeBasedSecret</a> – Create a one-time based secret</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/getactivelinkedcards/">GetActiveLinkedCards</a> – Get an array of card details of activated cards linked to the reference</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/getcarddetails/">GetCardDetails</a> – Get card details of a specific card</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/getalllinkedcards/">GetLinkedCards</a> – Get an array of card details of all cards (active, stopped and retired) linked to the reference</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/linkcard/">LinkCard</a> – Link a card to a reference with the given bearer details. Linking a card will not activate it</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/listalltokens/">ListAllTokens</a> – Returns all the tokens (active and inactive) linked to a card</li>
<li><a href="https://developer.sprint.paymentology.com/listtokens/">ListTokens</a> – Returns all the active tokens linked to a card</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/ordercard/">OrderCard</a> – Order a card for a specific cardholder. A card can be printed with cardholder details by the card manufacturer</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/ordercardwithpinblock/">OrderCardWithPinBlock</a> – Order a card for a specific cardholder. A card can be printed with cardholder details by the card manufacturer</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/printlinkedcard/">PrintLinkedCard</a> – Print the specified card if the card was initially created as virtual</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/printlinkedcardwithpinblock/">PrintLinkedCardWithPINBlock</a> – Print the specified card if the card was initially created as virtual with PIN block</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/resetpin/">ResetPin</a> – Reset the specified card’s PIN. The random pin will be sent to the card bearer’s cell via text message</li>
<li><a href="https://developer.sprint.paymentology.com/retirecard/">RetireCard</a> – Retires the specified card</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/status/">Status</a> – Return the status of the specified card</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/set3dsecurecode/">Set3dSecureCode</a> – Set 3D Secure Code of the specified card</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/stopcard/">StopCard</a> – Stop the specified card</li>
<li><a href="https://developer.sprint.paymentology.com/stoptoken/">StopToken</a> – Stops a token reference or all the ones linked to a card. The token or tokens can be unstopped using UnStopToken</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/threedsauthenticationoutcome/">ThreeDSAuthenticationOutcome</a> – Gives the result of the 3D Secure App Authentication</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/togglevoucherfeature/">ToggleVoucherFeature</a> – Toggles a voucher feature on or off</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/tokenapprovedevicebinding/">TokenApproveDeviceBinding</a> – Bind the device with token</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/tokenremovedevicebinding/">TokenRemoveDeviceBinding</a> – Remove device with the token</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/transferlink/">TransferLink</a> – Transfer a reference to a new card</li>
<li><a href="https://developer.sprint.paymentology.com/transfertoken/">TransferToken</a> – Transfer a payment token from one card to another</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/unstopcard/">UnstopCard</a> – Unstop the specified card</li>
<li><a href="https://developer.sprint.paymentology.com/unstoptoken/">UnStopToken</a> – Unstops a token reference or all the ones linked to a card</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/updatebearer/">UpdateBearer</a> – Update the specified card’s bearer details</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/updatecvv/">UpdateCVV</a> – Generate a new CVV2 of the specified card</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/updatetokenaccount/">UpdateTokenAccount</a> – Updates the card PAN information associated with a token</li>
</ul>

<h2>Response Codes</h2>
<p>To access the Response Codes for the Local API, please click <a href="https://developer.sprint.paymentology.com/response-codes/">here</a>.</p>
<p> </p>
<p> </p>
<p> </p>
</p></p></p></a></p></h2></a></li></a></li></a></li></a></li></a></li></a></li></a></li></a></li></a></li></a></li></a></li></a></li></a></li></a></li></a></li></a></li></a></li></a></li></a></li></a></li></a></li></a></li></a></li></a></li></a></li></a></li></a></li></a></li></a></li></a></li></a></li></a></li></a></li></a></li></ul></h2></p></p>
