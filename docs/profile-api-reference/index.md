---
title: Profile API Reference
deprecated: false
hidden: false
metadata:
  robots: index
---
<!-- MIGRATION_METADATA
Migrated-From: https://developer.sprint.paymentology.com/profile-api-reference/
Source-Slug: profile-api-reference
Migrated-On: 2026-02-12T21:14:38+00:00
Migrated-By: wp-readme-migration
-->

## Card Issuance and Management API’s

- [Activate](activate) – Activate a card

- [AllocateCard](allocatecard) – Allocate a card to a bearer

- [AllocateCreateVirtualCard](allocatecreatevirtualcard) – Create a virtual card with specified amount loaded, linked to the specified profile and allocated to a cardholder with specified details

- [Balance](balance-1) – Retrieve the balance of a card

- [CancelScheduledStop](cancelscheduledstop) – Cancels an existing scheduled stop

- [CancelStopCard](cancelstopcard) – Un-stop a card

- [CardDetail](carddetail-1) – Returns details regarding the created virtual card

- [ChangePin](changepin-2) – Change the pin on the card associated with the customer reference and tracking number

- [CheckAuthorisation](checkauthorisation) – Provides a method to check if the specified amount was deducted from a card.

- [CheckLoad](checkload) – Provides a method to check if the specified amount was loaded on a card.

- [CreateScheduledStop](createscheduledstop) – Schedules the stop of the card on the date of the parameter

- [CreateVirtualCard](createvirtualcard-1) – Create a virtual card with specified amount loaded, linked to the specified profile and allocated to the profile owner

- [DeductCardLoadProfile](deductcardloadprofile) – Deduct requested amount from card and load the amount back to the profile

- [DeLinkCard](delinkcard) – Provides a method to unlink a card from a specified profile

- [DevalueProfile](devalueprofile) – Deducts the requested amount from the Profile specified

- [GetScheduleStopDetail](getschedulestopdetail) – Returns the existing scheduled stops for a card

- [InsertTransactionFee](inserttransactionfee-1) – Deduct requested amount from card as a fee using any one of the (integer) fee type IDs

- [LoadCardDeductProfile](loadcarddeductprofile) – Load a card with the requested amount and deduct the amount off the profile

- [LinkCard](linkcard-2) – Link a card to a profile

- [LinkCardsBySequenceRange](linkcardsbysequencerange) – Link multiple cards to a profile using a range of sequence numbers

- [OrderCard](ordercard-2) – Order a card for a specific cardholder

- [Register](register) – Creates and registers a new profile

- [ResetPin](resetpin-1) – Provides a method to reset the PIN of a card

- [ReverseDeductCardLoadProfile](reversedeductcardloadprofile) – Reverse a previous DeductCardLoadProfile request

- [ReverseDevalueProfile](reversedevalueprofile) – Reverse a previous DevalueProfile request

- [ReverseTransactionFee](reversetransactionfee) – Reverse a fee that was charged via the API using [InsertTransactionFee](inserttransactionfee-1)

- [Statement](statement-1) – Retrieve the statement of a card

- [StatementByDateRange](statementbydaterange) – Returns the statement between two dates

- [Status](status-1) – Retrieve the current status of a card

- [StopCard](stopcard-2) – Stop a card with one of the allowed (integer) values for stopReasonID

- [ToggleVoucherFeature](togglevoucherfeature-2) – Toggles a voucher feature on or off

- [TransferFunds](transferfunds-1) – Transfer funds from one card to another

- [TransferFundsBetweenProfiles](transferfundsbetweenprofiles) – Transfer funds from one profile to another

- [UpdateAllocatedCard](updateallocatedcard) – Updates the cellphone or ID number linked to an allocated card

- [UpdateBearer](updatebearer-1) – Updates the firstName, lastName, cellphone and ID number linked to an allocated card

- [UpdateProfile](updateprofile) – Updates a profile owner’s details

- [UpdateScheduledStop](updatescheduledstop) – Updates an existing scheduled stop


## Additional Card Management API’s

**NOTE:** The Additional Card Management API’s listed below are available to specific clients. Please confirm with your Account Manager.

- [TransferLink](transferlink-2) – Transfer a reference to a new card (Visa).

- [AllocateIBAN](allocateiban) – Allocate an IBAN [Account Number] for a card linked to the specified profile.

- [ReverseVasTransferFunds](reversevastransferfunds) – Reverse a VAS transfer on the card.

- [UpdateBearerExtended](updatebearerextended) – Update the cardholder details. This is an extended API to update additional details like address and employment details.

- [UploadFicaDocument](uploadficadocument) – Uploads identification to be FICA compliant.

- [VasTransferFunds](vastransferfunds) – Transfer funds from a card for a VAS transaction.


## Tokenisation Life Cycle Management API’s

**NOTE:** The Tokenisation Life Cycle Management API’s listed below are available to Tokenisation enabled clients. Please contact your Account Manager if you require further information.

- [ActivateToken](activatetoken-2) – Used to activate a token for a digitization that has been approved and provisioned, but requires additional cardholder authentication prior to activation.

- [CalculateTAV](calculatetav-2) – This API is used to create Token Authentication Value (TAV)

- [DeleteToken](deletetoken-1) – Remove a payment token linked to a card

- [GenerateTimeBasedSecret](generatetimebasedsecret-2) – Generates a “secret token” to enable communication with our tokenisation APIs

- [ListAllTokens](listalltokens-2) – Returns all the tokens (active and inactive) linked to a card

- [ListTokens](listtokens-2) – Returns all the tokens linked to a card

- [StopToken](stoptoken-2) – Stops a token reference or all the ones linked to a card

- [TransferToken](transfertoken-1) – Transfer a payment token from one card to another

- [UpdateTokenAccount](updatetokenaccount-2) – Updates the card PAN information associated with a token

- [UnStopToken](unstoptoken-2) – Unstops a token reference or all the ones linked to a card
