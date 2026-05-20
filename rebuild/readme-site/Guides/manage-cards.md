# Manage cards

**You can manage the issued Paymentology Sprint cards and make updates to them whenever necessary. You can also use the API methods below to develop a UI that comes with self-help options that allow the cardholders to manage their cards by themselves.**

These are the supported card management options:

- [Stopping](#stop) a card

- [Unstopping](#unstop) a card

- [Retiring](#retire) a card

- [Replacing](#replace) a card

- [Retrieving](#retrieve) card details

- Getting the [status](#status) on a card

Let's look at each of them.

## 1. Stopping a card

To stop a card temporarily, you’ll need to call the [​StopCard](https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/#StopCard) method​​.

## 2. Unstopping a card

To unstop a card that was stopped previously, you’ll need to call the ​[UnStopCard](https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/#UnstopCard) method​​.

## 3. Retiring a card

To cancel (retire) your card permanently, you’ll need to call the ​ [RetireCard](https://developer.sprint.paymentology.com/retirecard/) method​.

## 4. Replacing a card

​To replace an old card with a new card and transfer the link from the old card to the new card, you’ll need to call the ​[TransferLink](https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/#TransferLink) method.

## 5. Retrieving card details

To get the details of a card that was previously linked or created, you’ll need to make a call to the ​[GetActiveLinkedCards](https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/#GetActiveLinkedCards) method. Active card refers to a card that is not stopped, retired or cancelled.

## 6. Getting the status on a card

To retrieve the status of a card that is linked to a unique customer reference number, you’ll need to make a call to the [Status](https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/#Status) method​​.
