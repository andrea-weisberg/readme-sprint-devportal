---
title: Card API REFERENCE
deprecated: false
hidden: false
metadata:
  robots: index
---
The Card API contains the API and API methods that we use to call you to send transactions on to the store of value for authorizations. Transactions originate from the merchant and are sent to Paymentology via the financial networks and then are forwarded to the store of value for authorization.

**Note:** You will need to implement the relevant method names corresponding to the different calls in order to perform the necessary actions on your system.

# Available methods

- [ActivateToken](https://developer.sprint.paymentology.com/card-api/api-reference/activatetoken/) – Used to activate a token that has been approved and provisioned
- [AddCardTag](https://developer.sprint.paymentology.com/card-api/api-reference/addcardtag/) – Add a Tag name and Tag value to a card identified by tracking number
- [AddPocket](https://developer.sprint.paymentology.com/card-api/api-reference/addpocket/) – Add a pocket for the type indicated by UUID to a card identified by tracking number
- [BearerDetail](https://developer.sprint.paymentology.com/card-api/api-reference/bearerdetail/) – Get the details of the bearer that is identified by the given tracking number
- [CalculateTAV](https://developer.sprint.paymentology.com/card-api/api-reference/calculatetav/) – This API is used to create Token Authentication value (TAV)
- [CardDetail](https://developer.sprint.paymentology.com/card-api/api-reference/carddetail/) – Get the details of a card that is identified by the given tracking number
- [ChangePin](https://developer.sprint.paymentology.com/card-api/api-reference/changepin/) – Change the pin on the card associated with the customer reference and tracking number
- [CreateVirtualCard](https://developer.sprint.paymentology.com/card-api/api-reference/createvirtualcard/) – Create a virtual card in the campaign identified by its UUID and linked to the customer reference given
- [CreateVirtualCardWithLoad](https://developer.sprint.paymentology.com/card-api/api-reference/createvirtualcardwithload/) – Create a virtual card in the campaign identified by its UUID and linked to the customer reference given and loads the card
- [DeductFunds](https://developer.sprint.paymentology.com/card-api/api-reference/deductfunds/) – Deducts the requested amount from a card, or a pocket if applicable
- [DeductFundsReverse](https://developer.sprint.paymentology.com/card-api/api-reference/deductfundsreverse/) – Reverse a deduct that was previously requested but had potentially failed
- [DeleteToken](https://developer.sprint.paymentology.com/deletetoken-2/) – Remove a payment token linked to a card
- [Devalue](https://developer.sprint.paymentology.com/card-api/api-reference/devalue/) – Deducts the requested amount from a card, or pocket if specified, with a redemption type of “Devalue”
- [DevalueReverse](https://developer.sprint.paymentology.com/card-api/api-reference/devaluereverse/) – Reverse a devalue that was previously requested but had potentially failed
- [GenerateTimeBasedSecret](https://developer.sprint.paymentology.com/generatetimebasedsecret/) – Create a one-time based secret
- [InsertTransactionFee](https://developer.sprint.paymentology.com/card-api/api-reference/inserttransactionfee/) – Charge a fee to a card (or pocket if applicable)
- [LinkCard](https://developer.sprint.paymentology.com/card-api/api-reference/linkcard/) – Link an existing card to a given customer reference
- [ListAllTokens](https://developer.sprint.paymentology.com/card-api/api-reference/listalltokens/) – Returns all the tokens (active and inactive) linked to a card
- [ListCards](https://developer.sprint.paymentology.com/card-api/api-reference/listcards/) – Return a list of all cards that are linked to the customer reference
- [ListTokens](https://developer.sprint.paymentology.com/card-api/api-reference/listtokens/) – Returns all the tokens linked to a card
- [LoadFunds](https://developer.sprint.paymentology.com/card-api/api-reference/loadfunds/) – Load a card (or pocket if applicable) with the requested amount
- [LoadFundsReverse](https://developer.sprint.paymentology.com/card-api/api-reference/loadfundsreverse/) – Reverse a load that was previously requested but has potentially failed
- [MostRecentTransactions](https://developer.sprint.paymentology.com/card-api/api-reference/mostrecenttransactions/) – Provides the latest transactions on a card based on date range and transaction count.
- [OrderCard](https://developer.sprint.paymentology.com/card-api/api-reference/ordercard/) – Order a card for a specific cardholder. A card can be printed with cardholder details by the card manufacturer.
- [OrderCardWithPinBlock](https://developer.sprint.paymentology.com/card-api/api-reference/ordercardwithpinblock/) – Order a card for a specific cardholder with a pin block. A card can be printed with cardholder details by the card manufacturer.
- [PocketTransfer](https://developer.sprint.paymentology.com/card-api/api-reference/pockettransfer/) – Transfer funds between two pockets linked to a card identified by tracking number
- [PocketTransferReverse](https://developer.sprint.paymentology.com/card-api/api-reference/pockettransferreverse/) – Reverse an PocketTransfer transaction that was timed out using the details of the failed transaction
- [RetireCard](https://developer.sprint.paymentology.com/card-api/api-reference/retirecard/) – Permanently disable a card so that it is no longer returned for the customer reference in the ListCards method
- [Set3DSecureCode](https://developer.sprint.paymentology.com/card-api/api-reference/set3dsecurecode/) – Update the 3D Secure Code on the card associated with the customer reference and tracking number
- [SetBearerDetail](https://developer.sprint.paymentology.com/card-api/api-reference/setbearerdetail/) – Set the details of the bearer that is identified by the given tracking number
- [Statement](https://developer.sprint.paymentology.com/card-api/api-reference/statement/) – Retrieve the statement of a card (or pocket if applicable). *NB. Version 1.3 available*
- [StopCard](https://developer.sprint.paymentology.com/card-api/api-reference/stopcard/) – Stop a card with one of the allowed (integer) values for stopReasonID
- [StopToken](https://developer.sprint.paymentology.com/card-api/api-reference/stoptoken/) – Stops a token reference or all the ones linked to a card
- [ThreeDSAuthenticationOutcome](https://developer.sprint.paymentology.com/card-api/api-reference/threedsauthenticationoutcome/) – Gives the result of the 3D Secure App Authentication.
- [ToggleVoucherFeature](https://developer.sprint.paymentology.com/card-api/togglevoucherfeature/) – Toggles a voucher feature on or off
- [TokenApproveDeviceBinding](https://developer.sprint.paymentology.com/card-api/api-reference/tokenapprovedevicebinding-2/) – Used to Bind the device with the token
- [TokenRemoveDeviceBinding](https://developer.sprint.paymentology.com/card-api/api-reference/tokenremovedevicebinding/) – Remove device with the token
- [TransferFunds](https://developer.sprint.paymentology.com/card-api/api-reference/transferfunds/) – Transfer funds from one card to another identified by tracking numbers, using pockets if applicable of the same type
- [TransferFundsReverse](https://developer.sprint.paymentology.com/card-api/api-reference/transferfundsreverse/) – Reverse a TransferFunds transaction that was timed out using the details of the failed transaction
- [TransferLink](https://developer.sprint.paymentology.com/card-api/transferlink/) – Transfer a reference to a new card. The old card will be stopped and the bearer details transferred to the new card. The new card will be linked and activated
- [TransferToken](https://developer.sprint.paymentology.com/transfertoken-2/) – Transfer a payment token from one card to another
- [UnStopCard](https://developer.sprint.paymentology.com/card-api/api-reference/unstopcard/) – Unstop a card
- [UnstopToken](https://developer.sprint.paymentology.com/card-api/api-reference/unstoptoken/) – Unstops a token reference or all the ones linked to a card
- [UpdateCardExpiryDate](https://developer.sprint.paymentology.com/card-api/api-reference/updatecardexpirydate/) – Updates the expiry date of a virtual card
- [UpdateCardLabel](https://developer.sprint.paymentology.com/card-api/api-reference/updatecardlabel/) – Update the card label of a card identified by tracking number
- [UpdateCVV](https://developer.sprint.paymentology.com/card-api/api-reference/updatecvv/) – Generate a new CVV2 of the specified card
- [UpdateTokenAccount](https://developer.sprint.paymentology.com/card-api/api-reference/updatetokenaccount/) – Updates the card PAN information associated with a token

# [Remote Messaging API](https://developer.sprint.paymentology.com/remotemessaging/) for Non-Companion clients

The Remote Messaging API is hosted on your platform and allows us to call you to send administrative advice messages.

- [3DSecure.AppAuthentication](https://developer.sprint.paymentology.com/remotemessaging/#appauth)
- [3DSecure.AppFinalisation](https://developer.sprint.paymentology.com/remotemessaging/#appfinal)
- [3DSecure.OTP](https://developer.sprint.paymentology.com/remotemessaging/#3DSecure)
- [3DSecure Cardholder’s Contact Detail Collection](https://developer.sprint.paymentology.com/remotemessaging/#3DSecureCCD)
- [digitization.activation](https://developer.sprint.paymentology.com/remotemessaging/#activation)
- [digitization.activationmethods](https://developer.sprint.paymentology.com/remotemessaging/#activationmethods)
- [digitization.event](https://developer.sprint.paymentology.com/remotemessaging/#event)
- [Response Reference](https://developer.sprint.paymentology.com/remotemessaging/#responsereference)
