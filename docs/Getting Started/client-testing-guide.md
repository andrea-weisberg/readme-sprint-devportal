---
title: Client Testing Guide
excerpt: >-
  Complete guide for testing with Paymentology's Sprint platform, including
  setup steps, API selection, implementation, and testing scenarios.
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  robots: index
---
## How to start testing

Testing with Paymentology's Sprint platform is easy. By following the steps below you can safely try out our API functionality:

1. Sign up
2. Get your testing credentials
3. Select the correct API
4. Implement API methods with help from our tools
5. Download the test scenarios for your API
6. Return the signed testing document to us for verification
7. Book an implementation review meeting with us

Read on to find out exactly how to complete these steps to get your API testing started. If you would like assistance along the way, email [implementations@paymentology.com](mailto:implementations@paymentology.com) to book a short call with our Implementations Team.

### 1. Sign up for a testing account

As a first step, you will need to sign up for a testing account. You should receive your test credentials within 24 hours.

### 2. Get your testing credentials

Signed up and have an account? Great! You should now have received your testing credentials. Make sure to take note of these and keep them safe as this information is confidential and is used to identify you.

### 3. Select the right API

Select [the type](https://developer.sprint.paymentology.com/get-started/our-apis/) of API that works best for you. We have three distinct APIs. **It is important that you test the right API**. Depending on the API you choose, the testing credentials will vary as follows:

## Testing Credentials

1. **Companion and QR API**
   * Terminal id
   * Password/Private Key

2. **Card API**
   * Terminal id
   * Password/Private Key
   * Campaign UUID

If you have not yet received any of these details, please [reach out](https://developer.sprint.paymentology.com/contact-us/) to us before proceeding.

### 4. Implement the methods per API with help from our tools

Next, please implement the methods for your chosen API.

**To create and manage your first card, implement the applicable methods.**

* [Companion API](https://developer.sprint.paymentology.com/companion-api/api-reference/)
* [Card API](https://developer.sprint.paymentology.com/card-api/api-reference/)

## Companion API (V2)

Companion API is composed of Local and Remote methods. Local methods – you send a request to Paymentology's Sprint platform. Remote methods – Paymentology's Sprint platform sends a request to you.

### **Local API Testing**

So let's create and manage your first Card. Below are a list of important Local API calls you need to implement depending on whether you choose Physical Companion API or Virtual Companion API.

<div align="center">

<Table align={["center","center"]}>
  <thead>
    <tr>
      <th>
        PHYSICAL COMPANION API
      </th>

      <th>
        VIRTUAL COMPANION API
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        OrderCard or OrderCardWithPinBlock
      </td>

      <td>
        CreateLinkedCards
        (Please note: Virtual Cards are created active and linked so you don't need to use the Activate and Link API calls.)
      </td>
    </tr>

    <tr>
      <td>
        LinkCard
      </td>

      <td>
        GetActiveLinkedCards
      </td>
    </tr>

    <tr>
      <td>
        ActivateCard
      </td>

      <td>
        StopCard
      </td>
    </tr>

    <tr>
      <td>
        ChangePin
      </td>

      <td>
        UnstopCard
      </td>
    </tr>

    <tr>
      <td>
        GetActiveLinkedCards
      </td>

      <td>
        UpdateCVV
      </td>
    </tr>

    <tr>
      <td>
        TransferLink
      </td>

      <td>
        RetireCard
      </td>
    </tr>

    <tr>
      <td>
        StopCard
      </td>

      <td>
        Status
      </td>
    </tr>

    <tr>
      <td>
        UnstopCard
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        RetireCard
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Status
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

</div>

Please note that these need to be successfully passed before we can implement Remote API calls.

### Remote API Testing

All **Remote API** calls are mandatory and your system needs to be able to process these requests. Remote API calls are applicable to both Virtual and Physical APIs.

|           PHYSICAL AND VIRTUAL APIs          |
| :------------------------------------------: |
|                    Deduct                    |
|               DeductAdjustment               |
|                DeductReversal                |
|                LoadAdjustment                |
|                 LoadReversal                 |
|       AdministrativeMessage3DSecureOTP       |
| AdministrativeMessagedigitization.activation |
|                     Stop                     |
|                  ValidatePin                 |
|                    Balance                   |
|                   LoadAuth                   |
|               LoadAuthReversal               |

<br />

### [Remote API Testing – Documentation](https://developer.sprint.paymentology.com/companion-api/api-reference/remote/)

## Card API

For Card API, most of the API calls are applicable to both the Physical and Virtual Card API. Below we have listed the calls applicable for each.

Follow for full [Card API Documentation](https://developer.sprint.paymentology.com/card-api/)

Next, use the following tools to help you with the integration. These will ensure that you have built your Local API requests correctly. [Learn more about our tools.](https://developer.sprint.paymentology.com/tools/)

* The [Checksum Generator](https://developer.sprint.paymentology.com/tools/checksum-generator/) allows you to calculate the checksum for a transaction based on a terminal password value and the request data. It replicates the same process that happens during authentication. You can use the tool to validate that your own calculated checksum is the same as the one the Paymentology Sprint system generates. The hash algorithm is SHA256 and is configured by Paymentology – please let us know which one you will be using.

* The [XML Generator](https://developer.sprint.paymentology.com/tools/xml-generator/) allows you to generate a valid XML request (including a checksum string) from your request parameters. To ensure compatibility, you can use the tool to confirm if your own generated XML requests, including the checksum, are the same with those that Paymentology generates.

* The [XML Poster](https://developer.sprint.paymentology.com/tools/xml-poster/) allows you to post XML requests directly to the Paymentology Sprint system. In case there is no other route, you can use the XML Poster to post requests created with the XML Generator to the Paymentology Sprint systems. For example, at the start of your testing, you'll not have a system in place for calling the Companion Card Local API; therefore, you can use this tool to post requests to the API directly—such as when creating your first test card.

* [SimPOS](https://developer.sprint.paymentology.com/tools/simpos/) is a transaction simulator tool that allows you to simulate remote API transactions. For example: you can use SimPOS to test that the flow of virtual card transactions within the Companion Card API is working properly.

## 5. Download the test scenarios for your API

After you've implemented all the methods and you think you're ready, download the testing scenarios for your chosen API:

## **Companion API Scenarios**

* [Companion API Physical Card test script](https://developer.sprint.paymentology.com/wp-content/uploads/2022/11/Companion-API-Physical-Card-test-script.xlsx)
* [Companion API Virtual Card test script](https://developer.sprint.paymentology.com/wp-content/uploads/2022/11/Companion-API-Virtual-Card-test-script.xlsx)

## **Card API Scenarios**

* [Card API Physical Card test script](https://developer.sprint.paymentology.com/wp-content/uploads/2022/11/Card-API-Physical-Card-test-script.xlsx)
* [Card API Virtual Card test script](https://developer.sprint.paymentology.com/wp-content/uploads/2022/11/Card-API-Virtual-Card-test-script.xlsx)

## 6. Return the signed testing document to us for verification

Once done and you have received a positive response **(200 code)** for every method from the script, please sign the document and send it back to us at [implementations@paymentology.com](mailto:implementations@tutuka.com)

## 7. Success! Book a meeting with us so we can review the implementation

Lastly, please book a meeting with our implementations team to review the testing together.

**Note:** Please allow one business day for the review – testing must be booked at least **24 hours** in advance to ensure resource availability.
