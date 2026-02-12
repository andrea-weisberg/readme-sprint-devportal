---
title: Get connected
deprecated: false
hidden: false
metadata:
  robots: index
---
**To facilitate easier API integrations, Paymentology provides two integration environments: test environment and live environment.**

## i) Test integration environment

The test environment is publicly accessible. You must send a request to a “named” URL, such as vexdev.tutuka.com or apidev.tutuka.com. If you send a request to an IP address, it will not work.

Here are more requirements for the test environment:

* An incorrect XML in a request can cause the Paymentology Sprint system not to respond. If you are not getting a reply from Paymentology, and have confirmed the point above, please make full use of the available tools to verify the XML is indeed properly constructed and valid, and that your details (**TerminalID** and **checksum**, most notably) are correct.
* If the client is using a site-to-site VPN, there is a possibility that the client’s remote network is also using the same IP numbering scheme as Paymentology’s. This will cause an IP numbering conflict. Therefore, it is the client’s responsibility to NAT the incoming ranges to an IP that won’t conflict with Paymentology’s Sprint test network.
* If the IP is changed from what is used publicly (Internet) or on the private range when using a VPN, a host entry is required to map the IP to the correct FQDN (fully qualified domain name).

### Paymentology’s Test IP ranges

* 34.254.134.65
* 52.16.61.250
* 54.154.40.211

### URL’s to post test requests to:

* Local Companion API calls: [https://companion.uat.tutuka.cloud/v2_0/XmlRpc.cfm](https://companion.uat.tutuka.cloud/v2_0/XmlRpc.cfm)
* Card API calls: [https://apidev.tutuka.com/card/v1/XmlRpc.cfm](https://apidev.tutuka.com/card/v1/XmlRpc.cfm)
* QR API calls: [https://apidev.tutuka.com/mpqr/v1_0/consumer/xmlrpc.cfm](https://apidev.tutuka.com/mpqr/v1_0/consumer/xmlrpc.cfm)

## ii) Live integration environment

In addition to the test environment requirements above – which are also applicable to the live environment – there are a few additional requirements that apply to the live environment:

* **Integration method**​​—the preferred method for integration with Paymentology’s live environment is over the Internet using SSL (as opposed to a VPN connection).
* **System support​**—your system has to support TLS 1.2 as per requirements set by PCI. TLS 1.0 and TLS 1.1 cannot be supported.
* **[SimPOS](simpos.md)** —this is a transaction simulator tool that allows you to simulate remote API transactions. For example, you can use SimPOS to test that the flow of virtual card transactions over Paymentology’s Sprint Companion Card API is working properly.

# VPN

A VPN is a **Virtual Private Network** that allows a user to establish a private and protected network connection when using public networks to send and receive data. Paymentology Sprint platform does not offer VPNs to clients because messages are secured at an application and network level.

## **HMAC-SHA256 checksum at the application level**

* Message security is incorporated into each API call at the application level
* Paymentology will provide one or more (depending on your configuration requirements) unique terminal IDs and shared secrets (“keys”)
* This key is used in an algorithm to generate a secure message checksum
* The checksum is used by both parties to validate sender **identity** and message **integrity**
* This ensures that the sender is known and that the message has not been tampered with in any way

## **TLS 1.3 at the network level**

* Protecting each message at the network level as it travels between Paymentology’s Sprint platform and your system is TLS 1.3
* TLS 1.3 is the most advanced and secure implementation of the familiar “SSL” protocol
* It uses a combination of asymmetric and symmetric encryption with certificate-based authentication
* This ensures **complete end-to-end protection** of every message from the point of origin to its destination

## Need help?

In case you’re experiencing any integration issues, do not hesitate to [get in touch](contact-us.md)
