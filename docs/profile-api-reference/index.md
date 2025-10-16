---
title: Profile API Reference
deprecated: false
hidden: false
metadata:
  robots: index
---
<h2>Card Issuance and Management API’s</h2>
<ul>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/activate/">Activate</a> – Activate a card</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/allocatecard/">AllocateCard</a> – Allocate a card to a bearer</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/allocatecreatevirtualcard/">AllocateCreateVirtualCard</a> – Create a virtual card with specified amount loaded, linked to the specified profile and allocated to a cardholder with specified details</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/balance/">Balance</a> – Retrieve the balance of a card</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/cancelscheduledstop/">CancelScheduledStop</a> – Cancels an existing scheduled stop</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/cancelstopcard/">CancelStopCard</a> – Un-stop a card</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/carddetail/">CardDetail</a> – Returns details regarding the created virtual card</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/changepin/">ChangePin</a> – Change the pin on the card associated with the customer reference and tracking number</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/checkauthorisation/">CheckAuthorisation</a> – Provides a method to check if the specified amount was deducted from a card.</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/checkload/">CheckLoad</a> – Provides a method to check if the specified amount was loaded on a card.</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/createscheduledstop/">CreateScheduledStop</a> – Schedules the stop of the card on the date of the parameter</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/createvirtualcard/">CreateVirtualCard</a> – Create a virtual card with specified amount loaded, linked to the specified profile and allocated to the profile owner</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/deductcardloadprofile/">DeductCardLoadProfile</a> – Deduct requested amount from card and load the amount back to the profile</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/delinkcard/">DeLinkCard</a> – Provides a method to unlink a card from a specified profile</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/devalueprofile/">DevalueProfile</a> – Deducts the requested amount from the Profile specified</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/getschedulestopdetail/">GetScheduleStopDetail</a> – Returns the existing scheduled stops for a card</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/inserttransactionfee/">InsertTransactionFee</a> – Deduct requested amount from card as a fee using any one of the (integer) fee type IDs</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/loadcarddeductprofile/">LoadCardDeductProfile</a> – Load a card with the requested amount and deduct the amount off the profile</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/linkcard/">LinkCard</a> – Link a card to a profile</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/linkcardsbysequencerange/">LinkCardsBySequenceRange</a> – Link multiple cards to a profile using a range of sequence numbers</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/ordercard/">OrderCard</a> – Order a card for a specific cardholder</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/register/">Register</a> – Creates and registers a new profile</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/resetpin/">ResetPin</a> – Provides a method to reset the PIN of a card</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/reversedeductcardloadprofile/">ReverseDeductCardLoadProfile</a> – Reverse a previous DeductCardLoadProfile request</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/reversedevalueprofile/">ReverseDevalueProfile</a> – Reverse a previous DevalueProfile request</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/reversetransactionfee/">ReverseTransactionFee</a> – Reverse a fee that was charged via the API using <a href="https://developer.sprint.paymentology.com/profile-api-reference/inserttransactionfee/">InsertTransactionFee</a></li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/statement/">Statement</a> – Retrieve the statement of a card</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/statementbydaterange/">StatementByDateRange</a> – Returns the statement between two dates</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/status/">Status</a> – Retrieve the current status of a card</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/stopcard/">StopCard</a> – Stop a card with one of the allowed (integer) values for <span className="xml-highlight">stopReasonID</span></li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/togglevoucherfeature/">ToggleVoucherFeature</a> – Toggles a voucher feature on or off</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/transferfunds/">TransferFunds</a> – Transfer funds from one card to another</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/transferfundsbetweenprofiles/">TransferFundsBetweenProfiles</a> – Transfer funds from one profile to another</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/updateallocatedcard/">UpdateAllocatedCard</a> – Updates the cellphone or id number linked to an allocated card</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/updatebearer/">UpdateBearer</a> – Updates the firstName, lastName, cellphone and id number linked to an allocated card</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/updateprofile/">UpdateProfile</a> – Updates a profile owner’s details</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/updatescheduledstop/">UpdateScheduledStop</a> – Updates an existing scheduled stop</li>
</ul>

<h2>Additional Card Management API’s</h2>
<p><strong>NOTE:</strong> The Additional Card Management API’s listed below are available to specific clients. Please confirm with your Account Manager.</p>
<ul>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/transferlink/">TransferLink</a> – Transfer a reference to a new card (Visa).</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/allocateiban/">AllocateIBAN</a> – Allocate an IBAN [Account Number] for a card linked to the specified profile.</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/reversevastransferfunds/">ReverseVasTransferFunds</a> – Reverse a VAS transfer on the card.</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/updatebearerextended/">UpdateBearerExtended</a> – Update the cardholder details. This is an extended API to update additional details like address and employment details.</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/uploadficadocument/">UploadFicaDocument</a> – Uploads identification to be FICA compliant.</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/vastransferfunds/">VasTransferFunds</a> – Transfer funds from a card for a VAS transaction.</li>
</ul>

<h2>Tokenisation Life Cycle Management API’s</h2>
<p><strong>NOTE:</strong> The Tokenisation Life Cycle Management API’s listed below are available to Tokenisation enabled clients. Please contact your Account Manager if you require further information.</p>
<ul>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/activatetoken/">ActivateToken</a> – Used to activate a token for a digitization that has been approved and provisioned, but requires additional cardholder authentication prior to activation.</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/calculatetav-2/">CalculateTAV</a> – This API is used to create Token Authentication value (TAV)</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/deletetoken/">DeleteToken</a> – Remove a payment token linked to a card</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/generatetimebasedsecret/">GenerateTimeBasedSecret</a> – Generates a “secret token” to enable communication with our tokenisation APIs</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/listalltokens/">ListAllTokens</a> – Returns all the tokens (active and inactive) linked to a card</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/listtokens/">ListTokens</a> – Returns all the tokens linked to a card</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/stoptoken/">StopToken</a> – Stops a token reference or all the ones linked to a card</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/transfertoken/">TransferToken</a> – Transfer a payment token from one card to another</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/updatetokenaccount/">UpdateTokenAccount</a> – Updates the card PAN information associated with a token</li>
<li><a href="https://developer.sprint.paymentology.com/profile-api-reference/unstoptoken/">UnStopToken</a> – Unstops a token reference or all the ones linked to a card</li>
</ul>

