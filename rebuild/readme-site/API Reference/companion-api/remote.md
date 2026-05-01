# Remote

The Remote API is hosted on your platform and allows us to call you to perform actions on your store of value/wallet e.g. Deducting/loading funds, balance inquiries, etc.

Note: you will need to implement the relevant method names corresponding to the different calls in order to perform the necessary actions on your system.

## Available Methods

- [AdministrativeMessage](/api-reference/companion-api/administrativemessage) - Sends a message to a client for MDES digitization activation code OR sends message with 3D Secure OTP

- [Balance](/api-reference/companion-api/balance) - Checks the balance on a card

- [BrazilianInstallmentSettled](/api-reference/companion-api/brazilianinstallmentsettled) - Notifies that a Brazilian installment transaction is settled

- [Deduct](/api-reference/companion-api/deduct) - Deduct the requested amount from a wallet

- [DeductAdjustment](/api-reference/companion-api/deductadjustment) - Adjust a previous transaction, deduct the requested amount from a wallet

- [DeductReversal](/api-reference/companion-api/deductreversal) - Reverse a deduct that was previously requested on a wallet

- [LoadAdjustment](/api-reference/companion-api/loadadjustment) - Adjust a previous transaction, load a wallet

- [LoadAuth](/api-reference/companion-api/loadauth) - Request to pre-load in case of refund request or a payment request

- [LoadAuthReversal](/api-reference/companion-api/loadauthreversal) - Request to reverse the pre-load requested in LoadAuth

- [LoadReversal](/api-reference/companion-api/loadreversal) - Reverse a load that was previously requested on a wallet

- [MexicanInstallmentSettled](/api-reference/companion-api/mexicaninstallmentsettled) - Notifies that a Mexican installment transaction has been settled.

- [Stop](/api-reference/companion-api/stop) - Notification that a card was stopped

- [ValidatePIN](/api-reference/companion-api/validatepin) - Validate the PIN
