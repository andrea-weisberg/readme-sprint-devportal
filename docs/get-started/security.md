---
title: Security
deprecated: false
hidden: false
metadata:
  robots: index
---
<p><b>Security is central to everything we do at Paymentology</b></p>
<p><span style={{fontWeight: "400"}}>These are the measures Paymentology implements to ensure the <span style={{color: "#79dbbf"}}>security</span> of  Sprint’s API services:</span></p>
<p> </p>
<h2>1. Checksum</h2>
<p>To ensure that transactions are secure, Paymentology uses a checksum-based authentication method (<span className="tutuka-custom-tooltip" data-content="SHA-256 stands for Secure Hash Algorithm 256-bit and is used for cryptographic security">SHA256</span>) to ensure the validity of processes. The checksum is generated mostly from the data in the <span className="tutuka-custom-tooltip" data-content="The Paymentology issued terminal id of the terminal requesting the transaction">terminalID</span> and <span className="tutuka-custom-tooltip" data-content="HMAC-SHA256 hashed signature of the concatenated method name with all argument values using the terminal password as private key">checksum</span> field, which is included in every single API call.</p>
<p>You can think of the <span className="tutuka-custom-tooltip" data-content="The Paymentology issued terminal id of the terminal requesting the transaction">terminalID</span> and <span className="tutuka-custom-tooltip" data-content="HMAC-SHA256 hashed signature of the concatenated method name with all argument values using the terminal password as private key">checksum</span> fields as the <span className="tutuka-custom-tooltip" data-content="A sequence of characters/string value that is used to identify a user on a digital platform">username</span> and <span className="tutuka-custom-tooltip" data-content="A sequence of characters/string value that allows a user access to a system or platform">password</span>, respectively. But the <span className="tutuka-custom-tooltip" data-content="The Paymentology issued terminal id of the terminal requesting the transaction">terminalID</span> value in the request).</p>
<p>This guarantees <b>authentication</b> as well as the <b>integrity</b> of every piece of data within the transaction. The <span className="tutuka-custom-tooltip" data-content="The Paymentology issued terminal id of the terminal requesting the transaction">terminalID</span> is specific to you and you only, and only Paymentology will know the password associated with that <span className="tutuka-custom-tooltip" data-content="The Paymentology issued terminal id of the terminal requesting the transaction">terminalID</span>.</p>
<p>For this process to be fully secure, the recipient of the message will have to <b>recalculate</b> the <span className="tutuka-custom-tooltip" data-content="HMAC-SHA256 hashed signature of the concatenated method name with all argument values using the terminal password as private key">checksum</span> using all the individual details of the message and then <b>compare</b> it to the Paymentology supplied <span className="tutuka-custom-tooltip" data-content="HMAC-SHA256 hashed signature of the concatenated method name with all argument values using the terminal password as private key">checksum</span>. If both are the same, the transaction gets authenticated and verified.</p>
<p>During implementation, you can use our <a href="https://developer.sprint.paymentology.com/tools/checksum-generator/"><b>Checksum Generator tool</b></a> to compare the results of your checksum calculation to Paymentology’s checksum calculations.</p>
<p> </p>
<h2>2. User-Agent Header</h2>
<p><span style={{fontWeight: "400"}}>Paymentology’s Sprint platform requires a User-Agent header to be included in every request to its API services. The User-Agent request header is a characteristic string that identifies your application, its version number, and the programming language used. </span></p>
<p><span style={{fontWeight: "400"}}>Paymentology uses this information to effectively isolate problems that might be associated with your applications. It also enables Paymentology to identify you as the authorized caller. </span></p>
<p><span style={{fontWeight: "400"}}>Any request without a User-Agent header shall be denied.</span></p>
<p>Example:</p>
<div className="p-rich_text_section"><a className="c-link" href="http://tools.ietf.org/html/rfc7231#section-5.5.3" target="_blank" rel="noopener noreferrer" data-stringify-link="http://tools.ietf.org/html/rfc7231#section-5.5.3" data-sk="tooltip_parent">http://tools.ietf.org/html/rfc7231#section-5.5.3</a><br  />
(application, version and programming lang),</div>
<pre className="c-mrkdwn__pre" data-stringify-type="pre"><span className="xml-highlight">User-Agent: <product> / <product-version> <comment></span></pre>
<h2></h2>
<p> </p>
<h2>3. Disclosure of expected traffic</h2>
<p><span style={{fontWeight: "400"}}>Paymentology requires you to disclose beforehand the amount of traffic you expect per second. Paymentology also requires information on periods when you expect a higher than usual traffic, such as during holidays and promotions.</span></p>
<p><span style={{fontWeight: "400"}}>Paymentology uses this information to identify abnormal or unexpected traffic surges, which may require more keen attention. This information helps Paymentology better plan its services, prevent disruptions, and identify occasions when its services are flooded with tons of useless requests. </span></p>
<p><span style={{fontWeight: "400"}}>You need to communicate this information to Paymentology before setting up your production environment.</span></p>
<p> </p>
<h2>4. Enforcing IP reputation</h2>
<p><span style={{fontWeight: "400"}}>Paymentology enforces the AWS IP reputation mechanism as an additional, proactive approach to threat prevention and security management. IP reputation is derived mainly from historical sending patterns and volume. An IP address that sends consistent and predictable volumes of requests over an extended period of time usually has a good reputation.</span></p>
<p><span style={{fontWeight: "400"}}>If your IP address is on the poor reputation list, please contact AWS for resolution. </span></p>
<h2>5. Only server-to-server communication allowed</h2>
<p>Paymentology permits only server-to-server communication. Mobile/app-to-server traffic is not permitted at all. Paymentology’s Sprint APIs are designed for server-to-server communication and they do not incorporate user tokens that are considered the security standard for mobile/app-to-server communications. Connectivity to Paymentology servers must always come from a server, even if that server is just proxying requests through to use from your mobile app.</p>
