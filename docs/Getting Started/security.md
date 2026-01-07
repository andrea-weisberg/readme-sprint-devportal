---
title: Security
deprecated: false
hidden: false
metadata:
  robots: index
---
**Security is central to everything we do at Paymentology**

These are the measures Paymentology implements to ensure the security of Sprint’s API services:

<br />

## 1. Checksum

To ensure that transactions are secure, Paymentology uses a checksum-based authentication method (

<span title="SHA-256 stands for Secure Hash Algorithm 256-bit and is used for crptographic security" style={{ borderBottom: '1px dotted #E56A5D', cursor: 'help' }}>SHA256</span>
) to ensure the validity of processes. The checksum is generated mostly from the data in the
<span title="The Paymentology issued terminal ID of the terminal requesting the transaction" style={{ borderBottom: '1px dotted #E56A5D', cursor: 'help' }}>TERMINAL ID</span>
and
<span title="HMAC-SHA256 hashed signature of the concatenated method name with all argument values using the terminal password as private key" style={{ borderBottom: '1px dotted #E56A5D', cursor: 'help' }}>CHECKSUM</span>
field, which is included in every single API call.

<br />

You can think of the

<span title="The Paymentology issued terminal ID of the terminal requesting the transaction" style={{ borderBottom: '1px dotted #E56A5D', cursor: 'help' }}>TERMINAL ID</span>
and
<span title="HMAC-SHA256 hashed signature of the concatenated method name with all argument values using the terminal password as private key" style={{ borderBottom: '1px dotted #E56A5D', cursor: 'help' }}>CHECKSUM</span>
fields as the
<span title="ADD TOOLTIP TEXT HERE" style={{ borderBottom: '1px dotted #E56A5D', cursor: 'help' }}>USERNAME</span>
and
<span title="ADD TOOLTIP TEXT HERE" style={{ borderBottom: '1px dotted #E56A5D', cursor: 'help' }}>PASSWORD</span>,
respectively.

<br />

This guarantees **authentication** as well as the **integrity** of every piece of data within the transaction. The

<span title="The Paymentology issued terminal ID of the terminal requesting the transaction" style={{ borderBottom: '1px dotted #E56A5D', cursor: 'help' }}>TERMINAL ID</span>
is specific to you and you only, and only Paymentology will know the
<span title="ADD TOOLTIP TEXT HERE" style={{ borderBottom: '1px dotted #E56A5D', cursor: 'help' }}>PASSWORD</span>
associated with that terminalID.

<br />

For this process to be fully secure, the recipient of the message will have to **recalculate** the <span title="HMAC-SHA256 hashed signature of the concatenated method name with all argument values using the terminal password as private key" style={{ borderBottom: '1px dotted #E56A5D', cursor: 'help' }}>CHECKSUM</span> using all the individual details of the message and then **compare** it to the Paymentology supplied <span title="HMAC-SHA256 hashed signature of the concatenated method name with all argument values using the terminal password as private key" style={{ borderBottom: '1px dotted #E56A5D', cursor: 'help' }}>CHECKSUM</span>. If both are the same, the transaction gets authenticated and verified.

During implementation, you can use our **[Checksum Generator tool](https://developer.sprint.paymentology.com/tools/checksum-generator/)** to compare the results of your checksum calculation to Paymentology’s checksum calculations.

## 2. User-Agent Header

Paymentology’s Sprint platform requires a User-Agent header to be included in every request to its API services. The User-Agent request header is a characteristic string that identifies your application, its version number, and the programming language used.

Paymentology uses this information to effectively isolate problems that might be associated with your applications. It also enables Paymentology to identify you as the authorized caller.

Any request without a User-Agent header shall be denied.

Example (RFC 7231): [http://tools.ietf.org/html/rfc7231#section-5.5.3](http://tools.ietf.org/html/rfc7231#section-5.5.3) (application, version and programming lang)

```txt
User-Agent: <product> / <product-version> <comment>
```

During implementation, you can use our **[Checksum Generator tool](https://developer.sprint.paymentology.com/tools/checksum-generator/)** to compare the results of your checksum calculation to Paymentology’s checksum calculations.

## 2. User-Agent Header

Paymentology’s Sprint platform requires a User-Agent header to be included in every request to its API services. The User-Agent request header is a characteristic string that identifies your application, its version number, and the programming language used.

Paymentology uses this information to effectively isolate problems that might be associated with your applications. It also enables Paymentology to identify you as the authorized caller.

Any request without a User-Agent header shall be denied.

Example:

[http://tools.ietf.org/html/rfc7231#section-5.5.3](http://tools.ietf.org/html/rfc7231#section-5.5.3)  
(application, version and programming lang),

```txt
User-Agent: <product> / <product-version> <comment>
```

## 3. Disclosure of expected traffic

Paymentology requires you to disclose beforehand the amount of traffic you expect per second. Paymentology also requires information on periods when you expect a higher than usual traffic, such as during holidays and promotions.

Paymentology uses this information to identify abnormal or unexpected traffic surges, which may require more keen attention. This information helps Paymentology better plan its services, prevent disruptions, and identify occasions when its services are flooded with tons of useless requests.

You need to communicate this information to Paymentology before setting up your production environment.

## 4. Enforcing IP reputation

Paymentology enforces the AWS IP reputation mechanism as an additional, proactive approach to threat prevention and security management. IP reputation is derived mainly from historical sending patterns and volume. An IP address that sends consistent and predictable volumes of requests over an extended period of time usually has a good reputation.

If your IP address is on the poor reputation list, please contact AWS for resolution.

## 5. Only server-to-server communication allowed

Paymentology permits only server-to-server communication. Mobile/app-to-server traffic is not permitted at all. Paymentology’s Sprint APIs are designed for server-to-server communication and they do not incorporate user tokens that are considered the security standard for mobile/app-to-server communications. Connectivity to Paymentology servers must always come from a server, even if that server is just proxying requests through to use from your mobile app.
