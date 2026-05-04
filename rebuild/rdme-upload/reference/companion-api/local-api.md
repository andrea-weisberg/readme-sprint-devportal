---
title: Local API
category:
  uri: Companion API
slug: local-api
position: 27
parent:
  uri: api-reference
---

The Local API contains all the methods available for you to call Paymentology in order to perform the necessary actions on your cards. It includes methods that allow the SVA to create a virtual card, stop a card, or link a physical card. Local API calls are initiated by you.

The Local API is used for administration purposes.

## Available Methods

- [ActivateCard](/api-reference/companion-api/activatecard) - Activate the specified card if the card was initially created as inactive

- [ActivateToken](/api-reference/companion-api/activatetoken) - Used to activate a token for a digitization that has been approved and provisioned, but requires additional cardholder authentication prior to activation

- [CalculateTAV](/api-reference/companion-api/calculatetav) - Return the TAV (Token Authentication Value) of the specified card. The Token Authentication Value will be returned in Base64 format.

- [ChangePin](/api-reference/companion-api/changepin) - Change the specified card's PIN

- [CreateLinkedCard](/api-reference/companion-api/createlinkedcard) - Create a new, active virtual card and link it to a reference with the given bearer details

- [DeleteToken](https://developer.sprint.paymentology.com/deletetoken/) - Remove a payment token linked to a card

- [GenerateTimeBasedSecret](https://developer.sprint.paymentology.com/generatetimebasedsecret-2/) - Create a one-time based secret

- [GetActiveLinkedCards](/api-reference/companion-api/getactivelinkedcards) - Get an array of card details of activated cards linked to the reference

- [GetCardDetails](/api-reference/companion-api/getcarddetails) - Get card details of a specific card

- [GetLinkedCards](https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/getalllinkedcards/) - Get an array of card details of all cards (active, stopped and retired) linked to the reference

- [LinkCard](/api-reference/companion-api/linkcard) - Link a card to a reference with the given bearer details. Linking a card will not activate it

- [ListAllTokens](/api-reference/companion-api/listalltokens) - Returns all the tokens (active and inactive) linked to a card

- [ListTokens](https://developer.sprint.paymentology.com/listtokens/) - Returns all the active tokens linked to a card

- [OrderCard](/api-reference/companion-api/ordercard) - Order a card for a specific cardholder. A card can be printed with cardholder details by the card manufacturer

- [OrderCardWithPinBlock](/api-reference/companion-api/ordercardwithpinblock) - Order a card for a specific cardholder. A card can be printed with cardholder details by the card manufacturer

- [PrintLinkedCard](/api-reference/companion-api/printlinkedcard) - Print the specified card if the card was initially created as virtual

- [PrintLinkedCardWithPINBlock](/api-reference/companion-api/printlinkedcardwithpinblock) - Print the specified card if the card was initially created as virtual with PIN block

- [ResetPin](/api-reference/companion-api/resetpin) - Reset the specified card's PIN. The random pin will be sent to the card bearer's cell via text message

- [RetireCard](https://developer.sprint.paymentology.com/retirecard/) - Retires the specified card

- [Status](/api-reference/companion-api/status) - Return the status of the specified card

- [Set3dSecureCode](/api-reference/companion-api/set3dsecurecode) - Set 3D Secure Code of the specified card

- [StopCard](/api-reference/companion-api/stopcard) - Stop the specified card

- [StopToken](https://developer.sprint.paymentology.com/stoptoken/) – Stops a token reference or all the ones linked to a card. The token or tokens can be unstopped using UnStopToken

- [ThreeDSAuthenticationOutcome](/api-reference/companion-api/threedsauthenticationoutcome) – Gives the result of the 3D Secure App Authentication

- [ToggleVoucherFeature](/api-reference/companion-api/togglevoucherfeature) - Toggles a voucher feature on or off

- [TokenApproveDeviceBinding](/api-reference/companion-api/tokenapprovedevicebinding) - Bind the device with token

- [TokenRemoveDeviceBinding](/api-reference/companion-api/tokenremovedevicebinding) - Remove device with the token

- [TransferLink](/api-reference/companion-api/transferlink) - Transfer a reference to a new card

- [TransferToken](https://developer.sprint.paymentology.com/transfertoken/) - Transfer a payment token from one card to another

- [UnstopCard](/api-reference/companion-api/unstopcard) - Unstop the specified card

- [UnStopToken](https://developer.sprint.paymentology.com/unstoptoken/) – Unstops a token reference or all the ones linked to a card

- [UpdateBearer](/api-reference/companion-api/updatebearer) - Update the specified card's bearer details

- [UpdateCVV](/api-reference/companion-api/updatecvv) - Generate a new CVV2 of the specified card

- [UpdateTokenAccount](/api-reference/companion-api/updatetokenaccount) - Updates the card PAN information associated with a token

## Response Codes

To access the Response Codes for the Local API, please click [here](/guides/response-codes).
