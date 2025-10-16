---
title: Get connected
deprecated: false
hidden: false
metadata:
  robots: index
original_path: get-started
---
<p><strong>To facilitate easier API integrations, Paymentology provides two integration environments: test environment and live environment.</strong></p>



<!-- spacing: desktop=40, mobile=20 -->


<h2>​i) Test integration environment</h2>
<div class="block translation current highlight" data-element="para" data-attr-xinfo-text="10944">The test environment is publicly accessible. You must send a request to a “named” URL, such as vexdev.tutuka.com or apidev.tutuka.com. If you send a request to an IP address, it will not work.</div>
<div class="placeholder">​</div>
<div class="block translation" data-element="para" data-attr-xinfo-text="10947">Here are more requirements for the test environment:</div>
<div data-element="para" data-attr-xinfo-text="10947"></div>
<div data-element="para" data-attr-xinfo-text="10947">
<ul>
<li>An incorrect XML in a request can cause the Paymentology Sprint system not to respond. If you are not getting a reply from Paymentology, and have confirmed the point above, please make full use of the available tools to verify the XML is indeed properly constructed and valid, and that your details (​<span class="inline" data-element="emphasis" data-attr-role="bold">​<span class="xml-highlight">TerminalID</span>​</span>​and <span class="inline" data-element="emphasis" data-attr-role="bold">​<strong><span class="xml-highlight">checksum</span></strong>​</span>​, most notably) are correct.</li>
<li>If the client is using a site-to-site VPN, there is a possibility that the client’s remote network is also using the same IP numbering scheme as Paymentology&#8217;s. This will cause an IP numbering conflict. Therefore, it is the client’s responsibility to NAT the incoming ranges to an IP that won&#8217;t conflict with Paymentology&#8217;s Sprint test network.</li>
<li>If the IP is changed from what is used publicly (Internet) or on the private range when using a VPN, a host entry is required to map the IP to the correct FQDN (fully qualified domain name).</li>
</ul>
<h3>Paymentology&#8217;s Test IP ranges</h2>
<ul>
<li>34.254.134.65</li>
<li>52.16.61.250</li>
<li>54.154.40.211</li>
</ul>
<p>&nbsp;</p>
<h3>URL&#8217;s to post test requests to:</h3>
<ul>
<li>Local Companion API calls: <a href="https://companion.uat.tutuka.cloud/v2_0/XmlRpc.cfm">https://companion.uat.tutuka.cloud/v2_0/XmlRpc.cfm</a></li>
<li>Card API calls: <a href="https://apidev.tutuka.com/card/v1/XmlRpc.cfm">https://apidev.tutuka.com/card/v1/XmlRpc.cfm</a></li>
<li>QR API calls: <a href="https://apidev.tutuka.com/mpqr/v1_0/consumer/xmlrpc.cfm">https://apidev.tutuka.com/mpqr/v1_0/consumer/xmlrpc.cfm</a></li>
</ul>
</div>



<!-- unsupported_acf_block: sign_up_block {"acf_fc_layout":"sign_up_block","main_text":"Only registered developers can use testing environment","button_text":"Create an account"} -->


<h2>ii) Live integration environment</h2>
<p>In addition to the test environment requirements above – which are also applicable to the live environment – there are a few additional requirements that apply to the live environment:</p>
<ul>
<li><strong>Integration method</strong>​​—the preferred method for integration with Paymentology&#8217;s live environment is over the Internet using SSL (as opposed to a VPN connection).</li>
<li><strong>System support​</strong>—your system has to support TLS 1.2 as per requirements set by PCI. TLS 1.0 and TLS 1.1 cannot be supported.</li>
<li><strong><a href="https://developer.sprint.paymentology.com/tools/simpos/">SimPOS</a>​</strong> —this is a transaction simulator tool that allows you to simulate remote API transactions. For example, you can use SimPOS to test that the flow of virtual card transactions over Paymentology&#8217;s Sprint Companion Card API is working properly.</li>
</ul>



<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<h1>VPN</h1>
<p>A VPN is a <strong>Virtual Private Network</strong> that allows a user to establish a private and protected network connection when using public networks to send and receive data. Paymentology Sprint platform does not offer VPNs to clients because messages are secured at an application and network level.</p>
<p>&nbsp;</p>
<h2 class="fs-h3" data-renderer-start-pos="534"><strong data-renderer-mark="true">HMAC-SHA256 checksum at the application level</strong></h3>
<ul class="ak-ul" data-indent-level="1">
<li>
<p data-renderer-start-pos="583">Message security is incorporated into each API call at the application level</p>
</li>
<li>
<p data-renderer-start-pos="663">Paymentology will provide one or more (depending on your configuration requirements) unique terminal IDs and shared secrets (“keys”)</p>
</li>
<li>
<p data-renderer-start-pos="793">This key is used in an algorithm to generate a secure message checksum</p>
</li>
<li>
<p data-renderer-start-pos="867">The checksum is used by both parties to validate sender <strong data-renderer-mark="true">identity</strong> and message <strong data-renderer-mark="true">integrity</strong></p>
</li>
<li>
<p data-renderer-start-pos="957">This ensures that the sender is known and that the message has not been tampered with in any way</p>
</li>
</ul>
<p>&nbsp;</p>
<h2 class="fs-h3" data-renderer-start-pos="1060"><strong data-renderer-mark="true">TLS 1.3 at the network level</strong></h3>
<ul class="ak-ul" data-indent-level="1">
<li>
<p data-renderer-start-pos="1092">Protecting each message at the network level as it travels between Paymentology&#8217;s Sprint platform and your system is TLS 1.3</p>
</li>
<li>
<p data-renderer-start-pos="1196">TLS 1.3 is the most advanced and secure implementation of the familiar “SSL” protocol</p>
</li>
<li>
<p data-renderer-start-pos="1285">It uses a combination of asymmetric and symmetric encryption with certificate-based authentication</p>
</li>
<li>
<p data-renderer-start-pos="1387">This ensures <strong data-renderer-mark="true">complete end-to-end protection</strong> of every message from the point of origin to its destination</p>
</li>
</ul>



<!-- spacing: desktop=20, mobile=10 -->


<h2>Need help?</h2>
<p>In case you’re experiencing any integration issues, do not hesitate to <a href="https://developer.sprint.paymentology.com/contact-us/">get in touch</a></p>
