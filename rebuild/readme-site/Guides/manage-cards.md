# Manage cards

You can manage the issued Paymentology cards and make updates to them whenever necessary. You can also use the API methods below to develop a UI that comes with self-help options that allow the cardholders to manage their cards by themselves.

These are the supported card management options:

- Getting card balances and other details

- Getting a card's transactions statement

- Adding cardholder details to a card

- Retrieving cardholder details

- Getting a list of cards linked to a customer

- Enabling and disabling a card's features

- Updating a card label

- Stopping a card

- Unstopping a card

- Retiring a card

Let's look at each of them.

## 1. Getting card balances and other details

To get the balance on a card, get the card details, or get the status of a card, you'll need to make a call to the CardDetail method.

## 2. Getting a card's transaction statement

To get a statement of the list of transactions on a card, you'll need to make a call to the Statement method.

## 3. Adding cardholder details to a card

To add the cardholder's details to a card, store KYC (Know Your Customer) information, or perform the sanctions screening, you'll need to make a call to the SetBearerDetail method.

You can also choose to opt-out of some parameter options. For example, if you only want to set the cardholder's details, then this is the only information you can send, and the rest of the parameter options will remain as null.

## 4. Retrieving cardholder details

To retrieve the set details of the cardholder, you'll need to make a call to the BearerDetail method.

## 5. Getting a list of cards linked to a customer

To get a list of all cards linked to a customer reference number, you'll need to make a call to the ListCards method.

## 6. Enabling and disabling a card's features

To enable and disable features on specific cards, such as the ability to make international transactions or magstripe transactions, you'll need to make a call to the ToggleVoucherFeature method.

## 7. Updating a card label

To update a label for a card that has already been issued, you'll need to make a call to the UpdateCardLabel method.

## 8. Stopping a card

To stop a card temporarily, you'll need to make a call to the StopCard method.

## 9. Unstopping a card

To unstop a card that was stopped previously, you'll need to make a call to the UnstopCard method.

## 10. Retiring a card

To cancel (retire) your card permanently, you'll need to make a call to the RetireCard method. You should ensure the funds are removed from the card before it is retired. Once retired, the card will not be able to be used again.
