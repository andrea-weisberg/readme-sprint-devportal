---
title: Profile API Reference
deprecated: false
hidden: false
metadata:
  robots: index
---
<h2>Card Issuance and Management API&#8217;s</h2>
<ul>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/activate/">Activate</a> &#8211; Activate a card</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/allocatecard/">AllocateCard</a> &#8211; Allocate a card to a bearer</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/allocatecreatevirtualcard/">AllocateCreateVirtualCard</a> &#8211; Create a virtual card with specified amount loaded, linked to the specified profile and allocated to a cardholder with specified details</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/balance/">Balance</a> &#8211; Retrieve the balance of a card</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/cancelscheduledstop/">CancelScheduledStop</a> &#8211; Cancels an existing scheduled stop</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/cancelstopcard/">CancelStopCard</a> &#8211; Un-stop a card</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/carddetail/">CardDetail</a> &#8211; Returns details regarding the created virtual card</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/changepin/">ChangePin</a> &#8211; Change the pin on the card associated with the customer reference and tracking number</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/checkload/">CheckAuthorisation</a> &#8211; Provides a method to check if the specified amount was deducted from a card.</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/checkload/">CheckLoad</a> &#8211; Provides a method to check if the specified amount was loaded on a card.</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/createscheduledstop/">CreateScheduledStop</a> &#8211; Schedules the stop of the card on the date of the parameter</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/createvirtualcard/">CreateVirtualCard</a> &#8211; Create a virtual card with specified amount loaded, linked to the specified profile and allocated to the profile owner</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/deductcardloadprofile/">DeductCardLoadProfile</a> &#8211; Deduct requested amount from card and load the amount back to the profile</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/delinkcard/">DeLinkCard</a> &#8211; Provides a method to unlink a card from a specified profile</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/devalueprofile/">DevalueProfile</a> &#8211; Deducts the requested amount from the Profile specified</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/getschedulestopdetail/">GetScheduleStopDetail</a> &#8211; Returns the existing scheduled stops for a card</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/inserttransactionfee/">InsertTransactionFee</a> &#8211; Deduct requested amount from card as a fee using any one of the (integer) fee type IDs</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/loadcarddeductprofile/">LoadCardDeductProfile</a> &#8211; Load a card with the requested amount and deduct the amount off the profile</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/linkcard/">LinkCard</a> &#8211; Link a card to a profile</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/linkcardsbysequencerange/">LinkCardsBySequenceRange</a> &#8211; Link multiple cards to a profile using a range of sequence numbers</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/ordercard/">OrderCard</a> &#8211; Order a card for a specific cardholder</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/register/">Register</a> &#8211; Creates and registers a new profile</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/resetpin/">ResetPin</a> &#8211; Provides a method to reset the PIN of a card</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/reversedeductcardloadprofile/">ReverseDeductCardLoadProfile</a> &#8211; Reverse a previous DeductCardLoadProfile request</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/reversedevalueprofile/">ReverseDevalueProfile</a> &#8211; Reverse a previous DevalueProfile request</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/reversetransactionfee/">ReverseTransactionFee</a> &#8211; Reverse a fee that was charged via the API using <a href="https://developer.sprint.paymentology.com/profile-api-reference/inserttransactionfee/">InsertTransactionFee</a></li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/statement/">Statement</a> &#8211; Retrieve the statement of a card</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/statementbydaterange/">StatementByDateRange</a> &#8211; Returns the statement between two dates</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/status/">Status</a> &#8211; Retrieve the current status of a card</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/stopcard/">StopCard</a> &#8211; Stop a card with one of the allowed (integer) values for <span class="xml-highlight">stopReasonID</span></li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/togglevoucherfeature/">ToggleVoucherFeature</a> &#8211; Toggles a voucher feature on or off</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/transferfunds/">TransferFunds</a> &#8211; Transfer funds from one card to another</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/transferfundsbetweenprofiles/">TransferFundsBetweenProfiles</a> &#8211; Transfer funds from one profile to another</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/updateallocatedcard/">UpdateAllocatedCard</a> &#8211; Updates the cellphone or ID number linked to an allocated card</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/updatebearer/">UpdateBearer</a> &#8211; Updates the firstName, lastName, cellphone and ID number linked to an allocated card</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/updateprofile/">UpdateProfile</a> &#8211; Updates a profile owner&#8217;s details</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/updatescheduledstop/">UpdateScheduledStop</a> &#8211; Updates an existing scheduled stop</li>
</ul>



<!-- spacing: desktop=20, mobile=10 -->


<h2>Additional Card Management API&#8217;s</h2>
<p><strong>NOTE:</strong> The Additional Card Management API&#8217;s listed below are available to specific clients. Please confirm with your Account Manager.</p>
<ul>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/transferlink/">TransferLink</a> &#8211; Transfer a reference to a new card (Visa).</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/allocateiban/">AllocateIBAN</a> &#8211; Allocate an IBAN [Account Number] for a card linked to the specified profile.</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/reversevastransferfunds/">ReverseVasTransferFunds</a> &#8211; Reverse a VAS transfer on the card.</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/updatebearerextended/">UpdateBearerExtended</a> &#8211; Update the cardholder details. This is an extended API to update additional details like address and employment details.</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/uploadficadocument/">UploadFicaDocument</a> &#8211; Uploads identification to be FICA compliant.</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/vastransferfunds/">VasTransferFunds</a> &#8211; Transfer funds from a card for a VAS transaction.</li>
</ul>



<!-- spacing: desktop=20, mobile=10 -->


<h2>Tokenisation Life Cycle Management API&#8217;s</h2>
<p><strong>NOTE:</strong> The Tokenisation Life Cycle Management API&#8217;s listed below are available to Tokenisation enabled clients. Please contact your Account Manager if you require further information.</p>
<ul>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/activatetoken/">ActivateToken</a> &#8211; Used to activate a token for a digitization that has been approved and provisioned, but requires additional cardholder authentication prior to activation.</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/calculatetav-2/">CalculateTAV</a> &#8211; This API is used to create Token Authentication Value (TAV)</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/deletetoken/">DeleteToken</a> &#8211; Remove a payment token linked to a card</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/generatetimebasedsecret/">GenerateTimeBasedSecret</a> &#8211; Generates a “secret token” to enable communication with our tokenisation APIs</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/listalltokens/">ListAllTokens</a> &#8211; Returns all the tokens (active and inactive) linked to a card</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/listtokens/">ListTokens</a> &#8211; Returns all the tokens linked to a card</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/stoptoken/">StopToken</a> &#8211; Stops a token reference or all the ones linked to a card</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/transfertoken/">TransferToken</a> &#8211; Transfer a payment token from one card to another</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/updatetokenaccount/">UpdateTokenAccount</a> &#8211; Updates the card PAN information associated with a token</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/unstoptoken/">UnStopToken</a> &#8211; Unstops a token reference or all the ones linked to a card</li>
</ul>



<!-- spacing: desktop=20, mobile=10 -->
