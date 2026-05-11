---
title: Lifecycle Management
category:
  uri: Guides
slug: token-lifecycle-management
position: 25
parent:
  uri: tokenization2
---

Token lifecycle management refers to handling the different states of the token, from creation to expiry. All tokens have a lifecycle; that is, the series of events happening from the date of creation to the expiry date when they’re no longer valid. The expiry date is usually linked to the expiry date of the full PAN that was used for provisioning.

Token lifecycle management involves passing messages between Paymentology and MDES that notify the client of the following token events:

- Token stopped (suspended)

- Token digitized (resumed)

- Token deleted from Device (deleted from a specific digital device only)

- Token deleted (deleted in its entirety)

- Token re-digitized (re-digitized or updated)

The token lifecycle events are managed through the **AdministrativeMessage** method. The **messageName**path parameter, required in the **AdministrativeMessage** method, specifies the name of the administrative messages sent to the client.

![Token lofecycle management flow](https://developer.sprint.paymentology.com/wp-content/uploads/2023/03/Token-life-cycle-management-v2.png)

These are the possible values for the **messageName**data field when managing tokens:

- [Digitization.event.stopped](https://developer.sprint.paymentology.com/administrative-message-values/#stopped) (token suspended)

- [Digitization.event.digitized](https://developer.sprint.paymentology.com/administrative-message-values/#digitized) (token resumed)

- [Digitization.event.Deleted_from_device](https://developer.sprint.paymentology.com/administrative-message-values/#deletedfromdevice) (token deleted from device)

- [Digitization.event.Deleted](https://developer.sprint.paymentology.com/administrative-message-values/#eventdeleted) (token deleted in its entirety)

- [digitization.event.Replacement](https://developer.sprint.paymentology.com/administrative-message-values/#replacement) (token re-digitized or replaced)

Let’s talk about each of the values in detail.

- [Digitization.event.stopped](https://developer.sprint.paymentology.com/administrative-message-values/#stopped)

This is when Paymentology informs a wallet that a token has been stopped or suspended. Paymentology will request the MDES to stop all the token transactions associated with the card’s full PAN.

- [Digitization.event.digitized](https://developer.sprint.paymentology.com/administrative-message-values/#digitized)

This is when Paymentology informs a wallet that a stopped token has been resumed. Paymentology will request MDES to reactivate the token mapped to the card.

- [Digitization.event.Deleted_from_device](https://developer.sprint.paymentology.com/administrative-message-values/#deletedfromdevice)

This is when Paymentology informs a wallet that the account holder has deleted the token from the wallet program on their device.

- [Digitization.event.Deleted](https://developer.sprint.paymentology.com/administrative-message-values/#eventdeleted)

This is when Paymentology informs the wallet that a token has been removed in its entirety.

- **[Digitization.event.Replacement](https://developer.sprint.paymentology.com/administrative-message-values/#replacement)**

This is when Paymentology informs the wallet that a token has been re-digitized or replaced. For example, a token expiry date can be updated based on the new replaced card.

## Tokenization with Digital Wallets

To allow for tokenization, issuers have historically needed to contract and integrate with each service or wallet separately. Every digital wallet has different capabilities for enabling tokenization.

On Paymentology's Sprint platform, these are the IDs associated with the various digital wallet programs:

Note that a 3-digit numeric value represents the IDs.

Notably, the digital wallets handle token provisioning differently. For example, Apple Pay and Google Pay work in the same way. So, for manual provisioning, an OTP will be issued, and they’ll be no OTP for push provisioning.

However, Samsung Pay does not issue an OTP, either for manual provisioning or push provisioning. So, during manual provisioning, Pamentology will just notify the client via **[Digitization.complete](https://developer.sprint.paymentology.com/administrative-message-values/#complete)**of the successful tokenization of the cardholder’s card on Samsung Pay.
