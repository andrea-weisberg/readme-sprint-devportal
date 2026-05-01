# Card API REFERENCE

The Card API contains the API and API methods that we use to call you to send transactions on to the store of value for authorizations. Transactions originate from the merchant and are sent to Paymentology via the financial networks and then are forwarded to the store of value for authorization.

Note: You will need to implement the relevant method names corresponding to the different calls in order to perform the necessary actions on your system.

# Available methods

- [ActivateToken](/api-reference/card-api/activatetoken) - Used to activate a token that has been approved and provisioned

- [AddCardTag](/api-reference/card-api/addcardtag) - Add a Tag Name and Tag Value to a card identified by tracking number

- [AddPocket](/api-reference/card-api/addpocket) - Add a pocket for the type indicated by UUID to a card identified by tracking number

- [BearerDetail](/api-reference/card-api/bearerdetail) - Get the details of the bearer that is identified by the given tracking number

- [CalculateTAV](/api-reference/card-api/calculatetav) - This API is used to create Token Authentication Value (TAV)

- [CardDetail](/api-reference/card-api/carddetail) - Get the details of a card that is identified by the given tracking number

- [ChangePin](/api-reference/card-api/changepin) - Change the pin on the card associated with the customer reference and tracking number

- [CreateVirtualCard](/api-reference/card-api/createvirtualcard) - Create a virtual card in the campaign identified by its UUID and linked to the customer reference given

- [CreateVirtualCardWithLoad](/api-reference/card-api/createvirtualcardwithload) - Create a virtual card in the campaign identified by its UUID and linked to the customer reference given and loads the card

- [DeductFunds](/api-reference/card-api/deductfunds) - Deducts the requested amount from a card, or a pocket if applicable

- [DeductFundsReverse](/api-reference/card-api/deductfundsreverse) - Reverse a deduct that was previously requested but had potentially failed

- [DeleteToken](https://developer.sprint.paymentology.com/deletetoken-2/) - Remove a payment token linked to a card

- [Devalue](/api-reference/card-api/devalue) - Deducts the requested amount from a card, or pocket if specified, with a redemption type of "Devalue"

- [DevalueReverse](/api-reference/card-api/devaluereverse) - Reverse a devalue that was previously requested but had potentially failed

- [GenerateTimeBasedSecret](/guides/generatetimebasedsecret) - Create a one-time based secret

- [InsertTransactionFee](/api-reference/card-api/inserttransactionfee) - Charge a fee to a card (or pocket if applicable)

- [LinkCard](/api-reference/card-api/linkcard) - Link an existing card to a given customer reference

- [ListAllTokens](/api-reference/card-api/listalltokens)- Returns all the tokens (active and inactive) linked to a card

- [ListCards](/api-reference/card-api/listcards) - Return a list of all cards that are linked to the customer reference

- [ListTokens](/api-reference/card-api/listtokens) - Returns all the tokens linked to a card

- [LoadFunds](/api-reference/card-api/loadfunds) - Load a card (or pocket if applicable) with the requested amount

- [LoadFundsReverse](/api-reference/card-api/loadfundsreverse) - Reverse a load that was previously requested but has potentially failed

- [MostRecentTransactions](/api-reference/card-api/mostrecenttransactions) - Provides the latest transactions on a card based on date range and transaction count.

- [OrderCard](/api-reference/card-api/ordercard) - Order a card for a specific cardholder. A card can be printed with cardholder details by the card manufacturer.

- [OrderCardWithPinBlock](/api-reference/card-api/ordercardwithpinblock) - Order a card for a specific cardholder with a pin block. A card can be printed with cardholder details by the card manufacturer.

- [PocketTransfer](/api-reference/card-api/pockettransfer) - Transfer funds between two pockets linked to a card identified by tracking number

- [PocketTransferReverse](/api-reference/card-api/pockettransferreverse) - Reverse an PocketTransfer transaction that was timed out using the details of the failed transaction

- [RetireCard](/api-reference/card-api/retirecard) - Permanently disable a card so that it is no longer returned for the customer reference in the ListCards method

- [Set3DSecureCode](/api-reference/card-api/set3dsecurecode) - Update the 3D Secure Code on the card associated with the customer reference and tracking number

- [SetBearerDetail](/api-reference/card-api/setbearerdetail) - Set the details of the bearer that is identified by the given tracking number

- [Statement](/api-reference/card-api/statement) - Retrieve the statement of a card (or pocket if applicable). NB. Version 1.3 available

- [StopCard](/api-reference/card-api/stopcard) - Stop a card with one of the allowed (integer) values for stopReasonID

- [StopToken](/api-reference/card-api/stoptoken) - Stops a token reference or all the ones linked to a card

- [ThreeDSAuthenticationOutcome](/api-reference/card-api/threedsauthenticationoutcome) - Gives the result of the 3D Secure App Authentication.

- [ToggleVoucherFeature](https://developer.sprint.paymentology.com/card-api/togglevoucherfeature/) - Toggles a voucher feature on or off

- [TokenApproveDeviceBinding](/api-reference/card-api/tokenapprovedevicebinding-2) - Used to Bind the device with the token

- [TokenRemoveDeviceBinding](/api-reference/card-api/tokenremovedevicebinding) - Remove device with the token

- [TransferFunds](/api-reference/card-api/transferfunds)- Transfer funds from one card to another identified by tracking numbers, using pockets if applicable of the same type

- [TransferFundsReverse](/api-reference/card-api/transferfundsreverse) - Reverse a TransferFunds transaction that was timed out using the details of the failed transaction

- [TransferLink](https://developer.sprint.paymentology.com/card-api/transferlink/) - Transfer a reference to a new card. The old card will be stopped and the bearer details transferred to the new card. The new card will be linked and activated

- [TransferToken](https://developer.sprint.paymentology.com/transfertoken-2/) - Transfer a payment token from one card to another

- [UnStopCard](/api-reference/card-api/unstopcard) - Unstop a card

- [UnstopToken](/api-reference/card-api/unstoptoken) - Unstops a token reference or all the ones linked to a card

- [UpdateCardExpiryDate](/api-reference/card-api/updatecardexpirydate) - Updates the expiry date of a virtual card

- [UpdateCardLabel](/api-reference/card-api/updatecardlabel) - Update the card label of a card identified by tracking number

- [UpdateCVV](/api-reference/card-api/updatecvv) - Generate a new CVV2 of the specified card

- [UpdateTokenAccount](/api-reference/card-api/updatetokenaccount) - Updates the card PAN information associated with a token

The Tutuka issued terminal ID of the terminal requesting the transaction

Customer reference to link the card to

Card number or Tracking number of the card to link

Transaction ID number generated by the calling client

Transaction date generated by the calling client

HMAC-SHA1 hashed signature Concatenate the method name with all previous fields and hash it using the HMAC-SHA1 algorithm using the terminal password as key

<methodCall>
<methodName>LinkCard</methodName>
<params>
<param>
<value>
<string>0008866376</string>
</value>
</param>
<param>
<value>
<string>TEST_Tutuka</string>
</value>
</param>
<param>
<value>
<string>156554700000004</string>
</value>
</param>
<param>
<value>
<string>4857467</string>
</value>
</param>
<param>
<value>
<dateTime.iso8601>20161017T00:00:00</dateTime.iso8601>
</value>
</param>
<param>
<value>
<string>4252E91C4890A9BDB7ED04C2673A89ED53F4C6D5</string>
</value>
</param>
</params>
</methodCall>

echo

echo

echo

tracking number of the linked card

echo

Transaction ID number generated by Tutuka

Status code indicating transaction result

Status text indicating transaction result

The Tutuka issued terminal ID of the terminal requesting the transaction

Customer reference to return cards for

Transaction ID number generated by the calling client

Transaction date generated by the calling client

HMAC-SHA1 hashed signature Concatenate the method name with all previous fields and hash it using the HMAC-SHA1 algorithm using the terminal password as key

<methodCall>
<methodName type="xs:string">ListCards</methodName>
<params>
<param>
<value>
<string>0008866376</string>
</value>
</param>
<param>
<value>
<string>TEST_CUSTOMER</string>
</value>
</param>
<param>
<value>
<string>d89d6df6-4e14-45a5-a32c-217c7175dfdb</string>
</value>
</param>
<param>
<value>
<dateTime.iso8601>20160525T00:00:00</dateTime.iso8601>
</value>
</param>
<param>
<value>
<string>862758A93795270DDEE9D8D3398F28E88830BDE8</string>
</value>
</param>
</params>
</methodCall>

The Tutuka issued terminal ID of the terminal requesting the transaction

Customer reference linked with this card

The tracking number of the card to either load or to which the pocket belongs

The UUID of the type of pocket to load, else empty if not applicable

The requested amount to be loaded on the card (or pocket if applicable)

Transaction ID number generated by the calling client

Transaction date generated by the calling client

HMAC-SHA1 hashed signature Concatenate the method name with all previous fields and hash it using the HMAC-SHA1 algorithm using the terminal password as key

<methodCall>
<methodName>LoadFunds</methodName>
<params>
<param>
<value>
<string>0008866376</string>
</value>
</param>
<param>
<value>
<string>999000001</string>
</value>
</param>
<param>
<value>
<string>953860100000030</string>
</value>
</param>
<param>
<value>
<string>NOTUSED</string>
</value>
</param>
<param>
<value>
<int>11100</int>
</value>
</param>
<param>
<value>
<string>43-load</string>
</value>
</param>
<param>
<value>
<dateTime.iso8601>20180731T12:50:11</dateTime.iso8601>
</value>
</param>
<param>
<value>
<string>E52A8FA98B8827CEBD1A552C9747B5D3C7867E4F</string>
</value>
</param>
</params>
</methodCall>

echo

echo

echo

echo

echo

Balances of pockets linked to the card

echo

Transaction ID number generated by Tutuka

Status code indicating transaction result

Status text indicating transaction result

The Tutuka issued terminal ID of the terminal requesting the transaction

Customer reference linked with this card

The tracking number of the card that was either loaded or to which the pocket belongs

The UUID of the type of pocket onto which the funds were originally loaded, else empty if not applicable

The amount that was requested in original LoadFunds call

Transaction ID number generated by the calling client

Transaction date generated by the calling client

The value of transactionID that was used with original LoadFunds call

The value of transactionDate that was used with the original LoadFunds call

HMAC-SHA1 hashed signature Concatenate the method name with all previous fields and hash it using the HMAC-SHA1 algorithm using the terminal password as key

echo

echo

echo

echo

echo

echo

echo

Transaction ID number generated by Tutuka

Status code indicating transaction result

Status text indicating transaction result

The Tutuka issued terminal ID of the terminal requesting the transaction

Customer reference linked with this card

The tracking number of the card to deduct the requested amount from

The tracking number of the card to load the requested amount on

The UUID of the type of pocket to transfer funds between, else empty if not applicable

The requested amount to be loaded on the card and deducted from the profile

Transaction ID number generated by the calling client

Transaction date generated by the calling client

HMAC-SHA1 hashed signature Concatenate the method name with all previous fields and hash it using the HMAC-SHA1 algorithm using the terminal password as key

echo

echo

echo

echo

echo

echo

echo

Transaction ID number generated by Tutuka

Balances of pockets linked to the card

Status code indicating transaction result

Status text indicating transaction result

<methodResponse>
<params>
<param>
<value>
<struct>
<member>
<name>clientTransactionID</name>
<value>
<string>4857467</string>
</value>
</member>
<member>
<name>resultCode</name>
<value>
<int>1</int>
</value>
</member>
<member>
<name>terminalID</name>
<value>
<string>0042128722</string>
</value>
</member>
<member>
<name>requestAmount</name>
<value>
<int>5000</int>
</value>
</member>
<member>
<name>customerReference</name>
<value>
<string>Tutuka Test</string>
</value>
</member>
<member>
<name>resultText</name>
<value>
<string>Approved</string>
</value>
</member>
<member>
<name>pocketUUID</name>
<value>
<string>
</string>
</value>
</member>
<member>
<name>trackingNumberTo</name>
<value>
<string>351453400000961</string>
</value>
</member>
<member>
<name>serverTransactionID</name>
<value>
<string>A3A67D85-155D-00FA-4DCD9DA1DB01532F</string>
</value>
</member>
<member>
<name>trackingNumberFrom</name>
<value>
<string>687653400000962</string>
</value>
</member>
<member>
<name>balance</name>
<value>
<array>
<data>
<value>
<struct>
<member>
<name>currency</name>
<value>
<string>840</string>
</value>
</member>
<member>
<name>amount</name>
<value>
<int>5000</int>
</value>
</member>
<member>
<name>pocketUUID</name>
<value>
<string>CABCCA6F-155D-0028-
9D9D270F6F1C5369</string>
</value>
</member>
</struct>
</value>
</data>
</array>
</value>
</member>
</struct>
</value>
</param>
</params>
</methodResponse>

The Tutuka issued terminal ID of the terminal requesting the transaction

Customer reference linked with this card

The tracking number of the card to reset the pin for

The name of the feature to enable/disable. Possible values: ENABLE_MAGSTRIPE and ENABLE_INTERNATIONAL

# [Remote Messaging API](https://developer.sprint.paymentology.com/remotemessaging/) for Non-Companion clients

The Remote Messaging API is hosted on your platform and allows us to call you to send administrative advice messages.

- [3DSecure.AppAuthentication](https://developer.sprint.paymentology.com/remotemessaging/#appauth)

- [3DSecure.AppFinalisation](https://developer.sprint.paymentology.com/remotemessaging/#appfinal)

- [3DSecure.OTP](https://developer.sprint.paymentology.com/remotemessaging/#3DSecure)

- [3DSecure Cardholder's Contact Detail Collection](https://developer.sprint.paymentology.com/remotemessaging/#3DSecureCCD)

- [digitization.activation](https://developer.sprint.paymentology.com/remotemessaging/#activation)

- [digitization.activationmethods](https://developer.sprint.paymentology.com/remotemessaging/#activationmethods)

- [digitization.event](https://developer.sprint.paymentology.com/remotemessaging/#event)

- [Response Reference](https://developer.sprint.paymentology.com/remotemessaging/#responsereference)
