---
title: Administrative message values
deprecated: false
hidden: false
metadata:
  robots: index
---

Values for the messageName field
- [digitization.activationmethods](#activationmethods)
- [digitization.activation](#activation)
- [digitization.complete](#complete)
- [digitization.event.Deleted](#eventdeleted)
- [digitization.event.Deleted_from_device](#deletedfromdevice)
- [digitization.event.Stopped](#stopped)
- [digitization.event.Digitized](#digitized)
- [digitization.event.Digitization_Exception](#exception)
- [digitization.event.Replacement](#replacement)

---

## **digitization.activationmethods**

This event occurs at the beginning of the token provisioning process. This message signals that a token provision has been made and requires verification method in order to push the OTP. The type of method will need to be passed as well as the data for the method.

KLV data – ‘digitized device id’ = 910, ‘digitized token requestor id’ = 915′, digitization path’ = 929, ‘wallet recommendation’ = 930,’tokenization pan source’ = 931.

**For more information on KLV data, click [here](../../../klv-lookup)**

*Activation methods*
| Value | Method |
| --- | --- |
| 1 | Masked mobile phone number |
| 2 | Masked email address |
| 3 | Call to automated call center initiated by cardholder |
| 4 | Call to staffed call center initiated by cardholder |
| 5 | Website |
| 6 | Mobile application |
| 7 | Issuer voice call to cardholder phone |

#### Request

```xml
<?xml version="1.0"?>
<methodCall>
    <methodName>AdministrativeMessage</methodName>
    <params>
        <param>
            <value>
                <string>0009555048</string>
            </value>
        </param>
        <param>
            <value>
                <string>a97af597-5a61-4683-be18-0f9910031743</string>
            </value>
        </param>
        <param>
            <value>
                <string>digitization.activationmethods</string>
            </value>
        </param>
        <param>
            <value>
                <string>90106497953</string>
            </value>
        </param>
        <param>
            <value>
                <string>822190</string>
            </value>
        </param>
        <param>
            <value>
                <dateTime.iso8601>20200717T03:38:53</dateTime.iso8601>
            </value>
        </param>
    </params>
    <param>
        <value>
            <string>DE6AFB51241B7F9D443BC719299B06432C706DC47D76CE10D6C32401135D2D49</string>
        </value>
    </param>
</methodCall>
```

#### Response

```xml
<methodresponse>
    <params>
        <param>
            <value>
                <struct>
                    <member>
                        <name>resultCode</name>
                        <value>
                            <int>1</int>
                        </value>
                    </member>
                    <member>
                        <name>activationMethods</name>
                        <value>
                            <array>
                                <data>
                                    <value>
                                        <struct>
                                            <member>
                                                <name>type</name>
                                                <value>1</value>
                                            </member>
                                            <member>
                                                <name>value</name>
                                                <value>555-444-2222</value>
                                            </member>
                                        </struct>
                                    </value>
                                    <value>
                                        <struct>
                                            <member>
                                                <name>type</name>
                                                <value>2</value>
                                            </member>
                                            <member>
                                                <name>value</name>
                                                <value>email@address.com</value>
                                            </member>
                                        </struct>
                                    </value>
                                </data>
                            </array>
                        </value>
                    </member>
                </struct>
            </value>
    </params>
</methodresponse>
```

---

## **digitization.activation**

The activation code that Paymentology will receive from MDES. Paymentology will send this code in the AdministrativeMessage to the client so that the client can pass on the activation code to the cardholder to input in app.

KLV data – ‘digitization activation’ (activation code) = 901, ‘digitization activation method type’ = 902, ‘digitization activation method value’ = 903, ‘digitization activation expiry’ = 904, ‘digitized token requestor id’ = 915. 

**For more information on KLV data, click [here](../../../klv-lookup)**

#### Request

```xml
<?xml version="1.0"?>
<methodCall>
    <methodName>AdministrativeMessage</methodName>
    <params>
        <param>
            <value>
                <string>0054239023</string>
            </value>
        </param>
        <param>
            <value>
                <string>mdestesting</string>
            </value>
        </param>
        <param>
            <value>
                <string>digitization.activation</string>
            </value>
        </param>
        <param>
            <value>
                <string>90106325541</string>
            </value>
        </param>
        <param>
            <value>
                <string>924089</string>
            </value>
        </param>
        <param>
            <value>
                <dateTime.iso8601>20201008T12:29:11</dateTime.iso8601>
            </value>
        </param>
        <param>
            <value>
                <string>85CC180D34893D1EF4E234DD48B8382630D055A1CCD868BCACD8C1938CA7B390</string>
            </value>
        </param>
    </params>
</methodCall>
```

#### Response

```xml
<methodResponse>
    <params>
        <param>
            <value>
                <struct>
                    <member>
                        <name>resultCode</name>
                            <value>
                                <int>1</int>
                            </value>
                    </member>
                </struct>
            </value>
        </param>
    </params>
</methodResponse>
```

---

## **digitization.complete**

 MDES sends a notification to the Issuer confirming that the token creation is completed.

KLV data – ‘digitized pan’ = 254, ‘digitized wallet id’ = 255, ‘digitized device id’ = 910, ‘digitized pan expiry’ = 911, ‘digitized fpan masked’ = 912, ‘Token Unique Reference’ = 913, ‘Digitized Token Requestor ID’ = 915, ‘Digitization event type’ = 923 , ‘Digitization event reason code’ = 924.

**For more information on KLV data, click [here](../../../klv-lookup)**

#### Request

```xml
<?xml version="1.0"?>
<methodCall>
    <methodName>AdministrativeMessage</methodName>
    <params>
        <param>
            <value>
                <string>0054239023</string>
            </value>
        </param>
        <param>
            <value>
                <string>mdestesting</string>
            </value>
        </param>
        <param>
            <value>
                <string>digitization.complete</string>
            </value>
        </param>
        <param>
            <value>
                <string>254165308426600000116255031039100221911042311912165190XXXXXXXX953891348DAPLMC00002584413e8419ef209a4257a24cfc68ce45d378</string>
            </value>
        </param>
        <param>
            <value>
                <string>663851</string>
            </value>
        </param>
        <param>
            <value>
                <dateTime.iso8601>20201008T12:29:55</dateTime.iso8601>
            </value>
        </param>
        <param>
            <value>
                <string>6E4103865CAD4496FCA1EC15181449A64D128AA7BE8E8FF8FF0FBB9E2766341D</string>
            </value>
        </param>
    </params>
</methodCall>
```

#### Response

```xml
<methodResponse>
    <params>
        <param>
            <value>
                <struct>
                    <member>
                        <name>resultCode</name>
                            <value>
                                <int>1</int>
                            </value>
                    </member>
                </struct>
            </value>
        </param>
    </params>
</methodResponse>
```

---

## **digitization.event.Deleted**

Informs the wallet about the removal of a token.

KLV data – ‘digitized pan’ = 254, ‘digitized wallet id’ = 255, ‘digitized device id’ = 910, ‘digitized pan expiry’ = 911, ‘digitized fpan masked’ = 912, ‘Token Unique Reference’ = 913, ‘Digitized Token Requestor ID’ = 915, ‘Digitization event type’ = 923 , ‘Digitization event reason code’ = 924.

**For more information on KLV data, click [here](../../../klv-lookup)**

*NB. Token deactivation for any other wallet program will result in the deactivation message being sent to the client and the token being deactivated, preventing further transactions being processed.*

#### Request

```xml
<?xml version="1.0"?>
<methodCall>
    <methodName>AdministrativeMessage</methodName>
    <params>
        <param>
            <value>
                <string>0054239023</string>
            </value>
        </param>
        <param>
            <value>
                <string>mdestesting</string>
            </value>
        </param>
        <param>
            <value>
                <string>digitization.event.Deleted</string>
            </value>
        </param>
        <param>
            <value>
                <string>254165265072400005904255032169100221911042311912165313XXXXXXXX494891300</string>
            </value>
        </param>
        <param>
            <value>
                <string>833456</string>
            </value>
        </param>
        <param>
            <value>
                <dateTime.iso8601>20201014T07:01:22</dateTime.iso8601>
            </value>
        </param>
        <param>
            <value>
                <string>3547639602EE35BE21D3DA2513183620E8EB1105</string>
            </value>
        </param>
    </params>
</methodCall>
```

#### Response

```xml
<methodResponse>
    <params>
        <param>
            <value>
                <struct>
                    <member>
                        <name>resultCode</name>
                            <value>
                                <int>1</int>
                            </value>
                    </member>
                </struct>
            </value>
        </param>
    </params>
</methodResponse>
```

---

## **digitization.event.Deleted_from_device**

The account holder deletes their token from the wallet program on their device.

KLV data – ‘digitized pan’ = 254, ‘digitized wallet id’ = 255, ‘digitized device id’ = 910, ‘digitized pan expiry’ = 911, ‘digitized fpan masked’ = 912, ‘Token Unique Reference’ = 913, ‘Digitized Token Requestor ID’ = 915, ‘Digitization event type’ = 923 , ‘Digitization event reason code’ = 924.

**For more information on KLV data, click [here](../../../klv-lookup)**

#### Request

```xml
<?xml version="1.0"?>
<methodCall>
    <methodName>AdministrativeMessage</methodName>
    <params>
        <param>
            <value>
                <string>0054239023</string>
            </value>
        </param>
        <param>
            <value>
                <string>mdestesting</string>
            </value>
        </param>
        <param>
            <value>
                <string>digitization.event.Deleted_from_Device</string>
            </value>
        </param>
        <param>
            <value>
                <string>254165308426600000116255031039100221911042311912165190XXXXXXXX953891300</string>
            </value>
        </param>
        <param>
            <value>
                <string>559069</string>
            </value>
        </param>
        <param>
            <value>
                <dateTime.iso8601>20201008T12:32:27</dateTime.iso8601>
            </value>
        </param>
        <param>
            <value>
                <string>BF8A989DB976A4E8A9830C1D32DC0388F94257192FE964B5508D15FCBCBE20CD</string>
            </value>
        </param>
    </params>
</methodCall>
```

#### Response

```xml
<methodResponse>
    <params>
        <param>
            <value>
                <struct>
                    <member>
                        <name>resultCode</name>
                            <value>
                                <int>1</int>
                            </value>
                    </member>
                </struct>
            </value>
        </param>
    </params>
</methodResponse>
```

---

## **digitization.event.Stopped**

When a token has been stopped.

KLV data – ‘digitized pan’ = 254, ‘digitized wallet id’ = 255, ‘digitized device id’ = 910, ‘digitized pan expiry’ = 911, ‘digitized fpan masked’ = 912, ‘Token Unique Reference’ = 913, ‘Digitized Token Requestor ID’ = 915, ‘Digitization event type’ = 923 , ‘Digitization event reason code’ = 924.

**For more information on KLV data, click [here](../../../klv-lookup)**

#### Request

```xml
<?xml version="1.0"?>
<methodCall>
    <methodName>AdministrativeMessage</methodName>
    <params>
        <param>
            <value>
                <string>0054239023</string>
            </value>
        </param>
        <param>
            <value>
                <string>mdestesting</string>
            </value>
        </param>
        <param>
            <value>
                <string>digitization.event.Stopped</string>
            </value>
        </param>
        <param>
            <value>
                <string>2541652650724000966222550332791000911042310912165313XXXXXXXX494891300</string>
            </value>
        </param>
        <param>
            <value>
                <string>25999</string>
            </value>
        </param>
        <param>
            <value>
                <dateTime.iso8601>20201014T06:31:27</dateTime.iso8601>
            </value>
        </param>
        <param>
            <value>
                <string>7C8476C5F9800A78243414CE5F4062FB48F6A1ED</string>
            </value>
        </param>
    </params>
</methodCall>
```

#### Response

```xml
<methodResponse>
    <params>
        <param>
            <value>
                <struct>
                    <member>
                        <name>resultCode</name>
                            <value>
                                <int>1</int>
                            </value>
                    </member>
                </struct>
            </value>
        </param>
    </params>
</methodResponse>
```

---

## **digitization.event.Digitized**

When a stopped token is reactivated.

KLV data – ‘digitized pan’ = 254, ‘digitized wallet id’ = 255, ‘digitized device id’ = 910, ‘digitized pan expiry’ = 911, ‘digitized fpan masked’ = 912, ‘Token Unique Reference’ = 913, ‘Digitized Token Requestor ID’ = 915, ‘Digitization event type’ = 923 , ‘Digitization event reason code’ = 924.

**For more information on KLV data, click [here](../../../klv-lookup)**

#### Request

```xml
<?xml version="1.0"?>
<methodCall>
    <methodName>AdministrativeMessage</methodName>
    <params>
        <param>
            <value>
                <string>0054239023</string>
            </value>
        </param>
        <param>
            <value>
                <string>mdestesting</string>
            </value>
        </param>
        <param>
            <value>
                <string>digitization.event.Digitized</string>
            </value>
        </param>
        <param>
            <value>
                <string>2541652650724000966222550332791000911042310912165313XXXXXXXX4948913000</string>
            </value>
        </param>
        <param>
            <value>
                <string>286071</string>
            </value>
        </param>
        <param>
            <value>
                <dateTime.iso8601>20201014T06:29:16</dateTime.iso8601>
            </value>
        </param>
        <param>
            <value>
                <string>78CC973C9D48947793D2AAA667314D7B3E829374</string>
            </value>
        </param>
    </params>
</methodCall>
```

#### Response

```xml
<methodResponse>
    <params>
        <param>
            <value>
                <struct>
                    <member>
                        <name>resultCode</name>
                            <value>
                                <int>1</int>
                            </value>
                    </member>
                </struct>
            </value>
        </param>
    </params>
</methodResponse>
```

---

## **digitization.event.Digitization_Exception**

When the activation code retries have been exceeded, an expired activation code was used, an invalid activation code was used, or an incorrect activation code has been entered

KLV data – ‘digitized pan’ = 254, ‘digitized wallet id’ = 255, ‘digitized device id’ = 910, ‘digitized pan expiry’ = 911, ‘digitized fpan masked’ = 912, ‘Token Unique Reference’ = 913, ‘Digitized Token Requestor ID’ = 915, ‘Digitization event type’ = 923 , ‘Digitization event reason code’ = 924.

**For more information on KLV data, click [here](../../../klv-lookup)**

#### Request

```xml
<?xml version="1.0"?>
<methodCall>
    <methodName>AdministrativeMessage</methodName>
    <params>
        <param>
            <value>
                <string>0054239023</string>
            </value>
        </param>
        <param>
            <value>
                <string>mdestesting</string>
            </value>
        </param>
        <param>
            <value>
                <string>digitization.event.Digitization_Exception</string>
            </value>
        </param>
        <param>
            <value>
                <string>254165265072400109086255032169100221911042311912165313XXXXXXXX494891300</string>
            </value>
        </param>
        <param>
            <value>
                <string>268282</string>
            </value>
        </param>
        <param>
            <value>
                <dateTime.iso8601>20201014T06:42:35</dateTime.iso8601>
            </value>
        </param>
        <param>
            <value>
                <string>191C9B39123EFBA55445AE38A53344A9A3F10747</string>
            </value>
        </param>
    </params>
</methodCall>
```

#### Response

```xml
<methodResponse>
    <params>
        <param>
            <value>
                <struct>
                    <member>
                        <name>resultCode</name>
                            <value>
                                <int>1</int>
                            </value>
                    </member>
                </struct>
            </value>
        </param>
    </params>
</methodResponse>
```

---

## **digitization.event.Replacement**

Token is re-digitized or replaced (e.g. token expiry date update) and can only be done via the device.

KLV data – ‘digitized pan’ = 254, ‘digitized wallet id’ = 255, ‘digitized device id’ = 910, ‘digitized pan expiry’ = 911, ‘digitized fpan masked’ = 912, ‘Token Unique Reference’ = 913, ‘Digitized Token Requestor ID’ = 915, ‘Digitization event type’ = 923 , ‘Digitization event reason code’ = 924.

**For more information on KLV data, click [here](../../../klv-lookup)**

#### Request

```xml
<?xml version="1.0"?>
<methodCall>
  <methodName>AdministrativeMessage</methodName>
  <params>
    <param>
      <value>
        <string>0009555048</string>
      </value>
    </param>
    <param>
      <value>
        <string>65432115</string>
      </value>
    </param>
    <param>
      <value>
        <string>digitization.event.Replacement</string>
      </value>
    </param>
    <param>
      <value>
        <string>042323DF.COMc4a92491c88162e9493933cc7915115011442868492317event.Replacement92400</string>
      </value>
    </param>
    <param>
      <value>
        <string>111111</string>
      </value>
    </param>
    <param>
      <value>
        <dateTime.iso8601>20250506T12:21:45</dateTime.iso8601>
      </value>
    </param>
    <param>
      <value>
        <string>DE6AFB51241B7F9D443BC719299B06432C706DC47D76CE10D6C32401135D2D49</string>
      </value>
    </param>
  </params>
</methodCall>
```

#### Response

```xml
<?xml version="1.0" encoding="UTF-8"?>
<methodResponse>
  <params>
    <param>
      <value>
        <struct>
          <member>
            <name>resultText</name>
            <value>Approved</value>
          </member>
          <member>
            <name>resultCode</name>
            <value>
              <i4>1</i4>
            </value>
          </member>
        </struct>
      </value>
    </param>
  </params>
</methodResponse>
```

---

# How to Test

The Wallet side is expected to respond to the messages above with approval, meaning response code 1.

***Note:*** During the testing session, the tester from Paymentology will manually post mock messages to your wallet and expect approval response in return.
| Test Case | Description | Expected Result |
| --- | --- | --- |
| Digitization activation methods | Paymentology informs wallet there is provisioning activity | Approval - Code 1 |
| Digitization activation  | Paymentology sends OTP to wallet | Approval - Code 1 |
| Digitization complete | Paymentology informs wallet about the completion of provisioning process | Approval - Code 1 |
| Digitization event (Deleted from device) | Paymentology informs wallet a card has been removed from a device | Approval - Code 1 |
| Digitization event (Stopped) | Paymentology informs wallet that a token has been suspended | Approval - Code 1 |
| Digitization event (Digitized) | Paymentology informs wallet that a suspended token has been resumed | Approval - Code 1 |
| Digitization event (Digitization Exception) | Paymentology informs the wallet that there is an error during the provisioning process | Approval - Code 1 |
| Digitization event (Deleted) | Paymentology informs the wallet that a token has been removed | Approval - Code 1 |
