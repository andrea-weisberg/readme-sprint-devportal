---
title: Profile API Reference
category:
  uri: Shared
slug: profile-api-reference
position: 2
---

## Card Issuance and Management API's

- [Activate](/api-reference/shared/activate) - Activate a card

- [AllocateCard](/api-reference/shared/allocatecard) - Allocate a card to a bearer

- [AllocateCreateVirtualCard](/api-reference/shared/allocatecreatevirtualcard) - Create a virtual card with specified amount loaded, linked to the specified profile and allocated to a cardholder with specified details

- [Balance](/api-reference/shared/balance) - Retrieve the balance of a card

- [CancelScheduledStop](/api-reference/shared/cancelscheduledstop) - Cancels an existing scheduled stop

- [CancelStopCard](/api-reference/shared/cancelstopcard) - Un-stop a card

- [CardDetail](/api-reference/shared/carddetail) - Returns details regarding the created virtual card

- [ChangePin](/api-reference/shared/changepin) - Change the pin on the card associated with the customer reference and tracking number

- [CheckAuthorisation](/api-reference/shared/checkauthorisation) - Provides a method to check if the specified amount was deducted from a card.

- [CheckLoad](/api-reference/shared/checkload) - Provides a method to check if the specified amount was loaded on a card.

- [CreateScheduledStop](/api-reference/shared/createscheduledstop) - Schedules the stop of the card on the date of the parameter

- [CreateVirtualCard](/api-reference/shared/createvirtualcard) - Create a virtual card with specified amount loaded, linked to the specified profile and allocated to the profile owner

- [DeductCardLoadProfile](/api-reference/shared/deductcardloadprofile) - Deduct requested amount from card and load the amount back to the profile

- [DeLinkCard](/api-reference/shared/delinkcard) - Provides a method to unlink a card from a specified profile

- [DevalueProfile](/api-reference/shared/devalueprofile) - Deducts the requested amount from the Profile specified

- [GetScheduleStopDetail](/api-reference/shared/getschedulestopdetail) - Returns the existing scheduled stops for a card

- [InsertTransactionFee](/api-reference/shared/inserttransactionfee) - Deduct requested amount from card as a fee using any one of the (integer) fee type IDs

- [LoadCardDeductProfile](/api-reference/shared/loadcarddeductprofile) - Load a card with the requested amount and deduct the amount off the profile

- [LinkCard](/api-reference/shared/linkcard) - Link a card to a profile

- [LinkCardsBySequenceRange](/api-reference/shared/linkcardsbysequencerange) - Link multiple cards to a profile using a range of sequence numbers

- [OrderCard](/api-reference/shared/ordercard) - Order a card for a specific cardholder

- [Register](/api-reference/shared/register) - Creates and registers a new profile

- [ResetPin](/api-reference/shared/resetpin) - Provides a method to reset the PIN of a card

- [ReverseDeductCardLoadProfile](/api-reference/shared/reversedeductcardloadprofile) - Reverse a previous DeductCardLoadProfile request

- [ReverseDevalueProfile](/api-reference/shared/reversedevalueprofile) - Reverse a previous DevalueProfile request

- [ReverseTransactionFee](/api-reference/shared/reversetransactionfee) - Reverse a fee that was charged via the API using [InsertTransactionFee](/api-reference/shared/inserttransactionfee)

- [Statement](/api-reference/shared/statement) - Retrieve the statement of a card

- [StatementByDateRange](/api-reference/shared/statementbydaterange) - Returns the statement between two dates

- [Status](/api-reference/shared/status) - Retrieve the current status of a card

- [StopCard](/api-reference/shared/stopcard) - Stop a card with one of the allowed (integer) values for stopReasonID

- [ToggleVoucherFeature](/api-reference/shared/togglevoucherfeature) - Toggles a voucher feature on or off

- [TransferFunds](/api-reference/shared/transferfunds) - Transfer funds from one card to another

- [TransferFundsBetweenProfiles](/api-reference/shared/transferfundsbetweenprofiles) - Transfer funds from one profile to another

- [UpdateAllocatedCard](/api-reference/shared/updateallocatedcard) - Updates the cellphone or ID number linked to an allocated card

- [UpdateBearer](/api-reference/shared/updatebearer) - Updates the firstName, lastName, cellphone and ID number linked to an allocated card

- [UpdateProfile](/api-reference/shared/updateprofile) - Updates a profile owner's details

- [UpdateScheduledStop](/api-reference/shared/updatescheduledstop) - Updates an existing scheduled stop

## Additional Card Management API's

**NOTE:** The Additional Card Management API's listed below are available to specific clients. Please confirm with your Account Manager.

- [TransferLink](/api-reference/shared/transferlink) - Transfer a reference to a new card (Visa).

- [AllocateIBAN](/api-reference/shared/allocateiban) - Allocate an IBAN [Account Number] for a card linked to the specified profile.

- [ReverseVasTransferFunds](/api-reference/shared/reversevastransferfunds) - Reverse a VAS transfer on the card.

- [UpdateBearerExtended](/api-reference/shared/updatebearerextended) - Update the cardholder details. This is an extended API to update additional details like address and employment details.

- [UploadFicaDocument](/api-reference/shared/uploadficadocument) - Uploads identification to be FICA compliant.

- [VasTransferFunds](/api-reference/shared/vastransferfunds) - Transfer funds from a card for a VAS transaction.

## Tokenisation Life Cycle Management API's

**NOTE:** The Tokenisation Life Cycle Management API's listed below are available to Tokenisation enabled clients. Please contact your Account Manager if you require further information.

- [ActivateToken](/api-reference/shared/activatetoken) - Used to activate a token for a digitization that has been approved and provisioned, but requires additional cardholder authentication prior to activation.

- [CalculateTAV](/api-reference/shared/calculatetav-2) - This API is used to create Token Authentication Value (TAV)

- [DeleteToken](/api-reference/shared/deletetoken) - Remove a payment token linked to a card

- [GenerateTimeBasedSecret](/api-reference/shared/generatetimebasedsecret) - Generates a “secret token” to enable communication with our tokenisation APIs

- [ListAllTokens](/api-reference/shared/listalltokens) - Returns all the tokens (active and inactive) linked to a card

- [ListTokens](/api-reference/shared/listtokens) - Returns all the tokens linked to a card

- [StopToken](/api-reference/shared/stoptoken) - Stops a token reference or all the ones linked to a card

- [TransferToken](/api-reference/shared/transfertoken) - Transfer a payment token from one card to another

- [UpdateTokenAccount](/api-reference/shared/updatetokenaccount) - Updates the card PAN information associated with a token

- [UnStopToken](/api-reference/shared/unstoptoken) - Unstops a token reference or all the ones linked to a card
