# Profile API Reference

## Card Issuance and Management API's

- [Activate](/api-reference/profile-api-reference/activate) - Activate a card

- [AllocateCard](/api-reference/profile-api-reference/allocatecard) - Allocate a card to a bearer

- [AllocateCreateVirtualCard](/api-reference/profile-api-reference/allocatecreatevirtualcard) - Create a virtual card with specified amount loaded, linked to the specified profile and allocated to a cardholder with specified details

- [Balance](/api-reference/profile-api-reference/balance) - Retrieve the balance of a card

- [CancelScheduledStop](/api-reference/profile-api-reference/cancelscheduledstop) - Cancels an existing scheduled stop

- [CancelStopCard](/api-reference/profile-api-reference/cancelstopcard) - Un-stop a card

- [CardDetail](/api-reference/profile-api-reference/carddetail) - Returns details regarding the created virtual card

- [ChangePin](/api-reference/profile-api-reference/changepin) - Change the pin on the card associated with the customer reference and tracking number

- [CheckAuthorisation](/api-reference/profile-api-reference/checkauthorisation) - Provides a method to check if the specified amount was deducted from a card.

- [CheckLoad](/api-reference/profile-api-reference/checkload) - Provides a method to check if the specified amount was loaded on a card.

- [CreateScheduledStop](/api-reference/profile-api-reference/createscheduledstop) - Schedules the stop of the card on the date of the parameter

- [CreateVirtualCard](/api-reference/profile-api-reference/createvirtualcard) - Create a virtual card with specified amount loaded, linked to the specified profile and allocated to the profile owner

- [DeductCardLoadProfile](/api-reference/profile-api-reference/deductcardloadprofile) - Deduct requested amount from card and load the amount back to the profile

- [DeLinkCard](/api-reference/profile-api-reference/delinkcard) - Provides a method to unlink a card from a specified profile

- [DevalueProfile](/api-reference/profile-api-reference/devalueprofile) - Deducts the requested amount from the Profile specified

- [GetScheduleStopDetail](/api-reference/profile-api-reference/getschedulestopdetail) - Returns the existing scheduled stops for a card

- [InsertTransactionFee](/api-reference/profile-api-reference/inserttransactionfee) - Deduct requested amount from card as a fee using any one of the (integer) fee type IDs

- [LoadCardDeductProfile](/api-reference/profile-api-reference/loadcarddeductprofile) - Load a card with the requested amount and deduct the amount off the profile

- [LinkCard](/api-reference/profile-api-reference/linkcard) - Link a card to a profile

- [LinkCardsBySequenceRange](/api-reference/profile-api-reference/linkcardsbysequencerange) - Link multiple cards to a profile using a range of sequence numbers

- [OrderCard](/api-reference/profile-api-reference/ordercard) - Order a card for a specific cardholder

- [Register](/api-reference/profile-api-reference/register) - Creates and registers a new profile

- [ResetPin](/api-reference/profile-api-reference/resetpin) - Provides a method to reset the PIN of a card

- [ReverseDeductCardLoadProfile](/api-reference/profile-api-reference/reversedeductcardloadprofile) - Reverse a previous DeductCardLoadProfile request

- [ReverseDevalueProfile](/api-reference/profile-api-reference/reversedevalueprofile) - Reverse a previous DevalueProfile request

- [ReverseTransactionFee](/api-reference/profile-api-reference/reversetransactionfee) - Reverse a fee that was charged via the API using [InsertTransactionFee](/api-reference/profile-api-reference/inserttransactionfee)

- [Statement](/api-reference/profile-api-reference/statement) - Retrieve the statement of a card

- [StatementByDateRange](/api-reference/profile-api-reference/statementbydaterange) - Returns the statement between two dates

- [Status](/api-reference/profile-api-reference/status) - Retrieve the current status of a card

- [StopCard](/api-reference/profile-api-reference/stopcard) - Stop a card with one of the allowed (integer) values for stopReasonID

- [ToggleVoucherFeature](/api-reference/profile-api-reference/togglevoucherfeature) - Toggles a voucher feature on or off

- [TransferFunds](/api-reference/profile-api-reference/transferfunds) - Transfer funds from one card to another

- [TransferFundsBetweenProfiles](/api-reference/profile-api-reference/transferfundsbetweenprofiles) - Transfer funds from one profile to another

- [UpdateAllocatedCard](/api-reference/profile-api-reference/updateallocatedcard) - Updates the cellphone or ID number linked to an allocated card

- [UpdateBearer](/api-reference/profile-api-reference/updatebearer) - Updates the firstName, lastName, cellphone and ID number linked to an allocated card

- [UpdateProfile](/api-reference/profile-api-reference/updateprofile) - Updates a profile owner's details

- [UpdateScheduledStop](/api-reference/profile-api-reference/updatescheduledstop) - Updates an existing scheduled stop

## Additional Card Management API's

**NOTE:** The Additional Card Management API's listed below are available to specific clients. Please confirm with your Account Manager.

- [TransferLink](/api-reference/profile-api-reference/transferlink) - Transfer a reference to a new card (Visa).

- [AllocateIBAN](/api-reference/profile-api-reference/allocateiban) - Allocate an IBAN [Account Number] for a card linked to the specified profile.

- [ReverseVasTransferFunds](/api-reference/profile-api-reference/reversevastransferfunds) - Reverse a VAS transfer on the card.

- [UpdateBearerExtended](/api-reference/profile-api-reference/updatebearerextended) - Update the cardholder details. This is an extended API to update additional details like address and employment details.

- [UploadFicaDocument](/api-reference/profile-api-reference/uploadficadocument) - Uploads identification to be FICA compliant.

- [VasTransferFunds](/api-reference/profile-api-reference/vastransferfunds) - Transfer funds from a card for a VAS transaction.

## Tokenisation Life Cycle Management API's

**NOTE:** The Tokenisation Life Cycle Management API's listed below are available to Tokenisation enabled clients. Please contact your Account Manager if you require further information.

- [ActivateToken](/api-reference/profile-api-reference/activatetoken) - Used to activate a token for a digitization that has been approved and provisioned, but requires additional cardholder authentication prior to activation.

- [CalculateTAV](/api-reference/profile-api-reference/calculatetav-2) - This API is used to create Token Authentication Value (TAV)

- [DeleteToken](/api-reference/profile-api-reference/deletetoken) - Remove a payment token linked to a card

- [GenerateTimeBasedSecret](/api-reference/profile-api-reference/generatetimebasedsecret) - Generates a “secret token” to enable communication with our tokenisation APIs

- [ListAllTokens](/api-reference/profile-api-reference/listalltokens) - Returns all the tokens (active and inactive) linked to a card

- [ListTokens](/api-reference/profile-api-reference/listtokens) - Returns all the tokens linked to a card

- [StopToken](/api-reference/profile-api-reference/stoptoken) - Stops a token reference or all the ones linked to a card

- [TransferToken](/api-reference/profile-api-reference/transfertoken) - Transfer a payment token from one card to another

- [UpdateTokenAccount](/api-reference/profile-api-reference/updatetokenaccount) - Updates the card PAN information associated with a token

- [UnStopToken](/api-reference/profile-api-reference/unstoptoken) - Unstops a token reference or all the ones linked to a card
