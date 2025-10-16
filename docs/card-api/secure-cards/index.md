---
title: Secure cards
deprecated: false
hidden: false
metadata:
  robots: index
---
<p><strong>The Sprint Card API allows you to access a wide range of features to ensure the security of card transactions.</strong></p>
<p>Here are the main features to use to ensure the security of your cards:</p>
<ul>
<li>Dynamic secure code on virtual cards</li>
<li>Dynamic CVV on virtual cards</li>
<li>PIN on physical cards</li>
<li>Adding pockets to your card</li>
</ul>
<p> </p>
<p>Let’s look at each of them.</p>

<h2 class="block highlight" data-element="bridgehead" data-attr-renderas="sect3" data-attr-xml-id="bridgehead-idm4580796441427231693872562228"><span class="inline translation current" data-element="emphasis" data-attr-role="bold" data-attr-xinfo-text="10337">1. Using a dynamic secure code on virtual cards​</span>​</h2>
<div class="placeholder">​A dynamic secure code allows you to increase the security of your virtual cards. If you add a dynamic secure code, it will be required at the time of making any transaction, enhancing payments security and safeguarding against fraud.</div>
<div class="placeholder">​</div>
<div class="block translation" data-element="para" data-attr-xinfo-text="10340">The secure code is what Mastercard refers to as 3D Secure, and Visa refers to it as Visa Secure (formerly Verified by Visa (VbV)).</div>
<div data-element="para" data-attr-xinfo-text="10340"></div>
<div data-element="para" data-attr-xinfo-text="10340">
<div class="block translation current highlight" data-element="para" data-attr-xinfo-text="10341">To secure your virtual card with a dynamic secure code, you’ll need to make a call to the <span class="inline link linktool link-external" data-element="link" data-attr-xlink-href="https://developer.sprint.paymentology.com/companion/documentation/remote#administrativemessage"><span class="xml-highlight">AdministrativeMessage</span> method.</span></div>
<div data-element="para" data-attr-xinfo-text="10341"></div>
<div class="placeholder">​</div>
<div class="block translation current highlight" data-element="para" data-attr-xinfo-text="10341">Then, a One Time PIN (OTP), which is triggered by the <span class="inline link linktool link-external" data-element="link" data-attr-xlink-href="https://developer.sprint.paymentology.com/remote-messaging/documentation#otprequest"><span class="xml-highlight">OTPRequest</span> method, will be delivered to the cardholder to enable them to complete the secure code process and finalize the transaction.</span></div>
</div>

<h2 class="block highlight" data-element="bridgehead" data-attr-renderas="sect3" data-attr-xml-id="bridgehead-idm4646117344587231693882666982"><span class="inline translation current" data-element="emphasis" data-attr-role="bold" data-attr-xinfo-text="10343">2. Using a dynamic CVV on virtual cards​</span>​</h2>
<div class="placeholder">​The Card Verification Value (CVV), which comes with every virtual card, is an essential feature for improving security. This static number helps in validating the identity of the cardholder, ensuring the card cannot be used for making fraudulent transactions.</div>
<div class="placeholder">​</div>
<div class="block translation" data-element="para" data-attr-xinfo-text="10346">And if you intend to revamp the security of a virtual card, or if a cardholder suspects their CVV has been compromised, you can simply update the CVV.</div>
<div data-element="para" data-attr-xinfo-text="10346"></div>
<div class="placeholder">​</div>
<div class="block translation" data-element="para" data-attr-xinfo-text="10346">To update the CVV, you’ll need to make a call to the <span class="xml-highlight">UpdateCVV</span> method. Paymentology will then create a new CVV that you can send to your cardholder.</div>

<h2 class="block highlight" data-element="bridgehead" data-attr-renderas="sect3" data-attr-xml-id="bridgehead-idm4575661939452831693886418008"><span class="inline translation current" data-element="emphasis" data-attr-role="bold" data-attr-xinfo-text="10348">3. Using a PIN on physical cards​</span>​</h2>
<div class="placeholder">​A PIN (personal identification number) is required to perform all ATM transactions. A secret PIN verifies a user’s identity and allows them to perform secure transactions. Apart from managing the transactions on the card, Paymentology will also manage its PIN. The PIN can either be pre-printed in a tamper-proof package containing the card or it can be set when the card is linked/issued.</div>
<div></div>
<div class="placeholder">​</div>
<div class="placeholder">If the card PIN needs to be set for the first time or changed at a later time, or if the customer forgets it or requests it to be changed, you’ll need to make a call to the <span class="inline link linktool link-external" data-element="link" data-attr-xlink-href="https://developer.sprint.paymentology.com/card/documentation/card-api#changepin">​<span class="xml-highlight">ChangePIN</span> method. After the API request has been completed, Paymentology will issue a new PIN.</span></div>

<h2 class="block highlight" data-element="bridgehead" data-attr-renderas="sect3" data-attr-xml-id="bridgehead-idm4511158928099231693890860727"><span class="inline translation current" data-element="emphasis" data-attr-role="bold" data-attr-xinfo-text="10353">4. Adding pockets to your card​</span>​</h2>
<div class="placeholder">​Although the ability to add multiple pockets may not be suitable for everyone, this feature allows you to enhance the versatility and security of your card. You will have your main Permanent Account Number (PAN) as your “control” card and multiple pockets that sit under this with different balances.</div>
<div class="placeholder">​</div>
<div class="block translation" data-element="para" data-attr-xinfo-text="10356"><span style="font-weight: 400;">Pockets are a useful feature to help customers manage their money.  Different pockets can be set up, like for example multiple currency pockets, savings pockets, expenditure pockets, or lifestyle pockets. </span>Each pocket comes with its own balance management system, which also enhances its security.</div>
<div data-element="para" data-attr-xinfo-text="10356"></div>
<div class="placeholder">​</div>
<div class="block translation" data-element="para" data-attr-xinfo-text="10356">To add multiple pockets to your card, you’ll need to make a call to the <span class="inline link linktool link-external" data-element="link" data-attr-xlink-href="https://developer.sprint.paymentology.com/card/documentation/card-api#addpocket"><em><span style="color: #0000ff;">​</span></em><span class="xml-highlight">AddPocket</span> method​.</span></div>
</span></span></em></span></div></div></div></span></div></div></div></span></h2></span></span></div></div></div></div></span></h2></span></div></div></div></div></div></div></span></h2></span></span></div></div></div></span></span></div></div></div></div></div></div></span></h2></p></p></li></li></li></li></ul></p></strong></p>
