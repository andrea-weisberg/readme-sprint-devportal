---
title: Issue cards
deprecated: false
hidden: false
metadata:
  robots: index
---
<h2>With the Paymentology Sprint Companion API, you can offer your customers different types of cards:</h2>

<h2 class="block highlight" data-element="bridgehead" data-attr-renderas="sect3" data-attr-xml-id="bridgehead-idm4580791643568031694088487013"><span class="inline translation current" data-element="emphasis" data-attr-role="bold" data-attr-xinfo-text="10578">1. Issuing a virtual card​</span>​​</h2>
<div class="block translation" data-element="para" data-attr-xinfo-text="10579">
<p><span style="font-weight: 400;">You can use the Companion API to create a Virtual Card Number (VCN), which you can link to the unique customer reference number. </span></p>
<p><span style="font-weight: 400;">If the API receives the request, it will create a 16-digit PAN (Permanent Account Number), CVV (Card Verification Value), and expiry date. You can then deliver this information to your customer. </span></p>
<p>**How-to-issue-a-virtual-card-v2.png IMAGE GOES HERE.**</p>
</div>

<p><span style="font-weight: 400;">The VCN will be linked to your customer’s store of value. Customers can then start making transactions instantly on any e-commerce site or application that accepts the chosen card association. </span></p>

<p>You’ll need to make a call to the <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/createlinkedcard/"><span class="xml-highlight">CreateLinkedCard</span></a> method to create a VCN.</p>

<h2 class="block highlight" data-element="bridgehead" data-attr-renderas="sect3" data-attr-xml-id="bridgehead-idm4580796471563231694092126034"><span class="inline translation current" data-element="emphasis" data-attr-role="bold" data-attr-xinfo-text="10585">2. Issuing a physical card​</span>​</h2>
<p><span style="font-weight: 400;">You can choose either of the following options for issuing a physical companion card: Issue on-site and link immediately or issue with courier and link later.</span></p>
<p>**Physical-card-fulfilment-flow-v2.png IMAGE GOES HERE.**</p>

<p>**Companion-card-issuing-flow-1-v2.png IMAGE GOES HERE.**</p>

<p>Making this call will lead to three results:</p>
<ul>
<li>Creates a PAN number file to send to the card manufacturer automatically</li>
<li>Making the OrderCard call, a new PAN file will be created and automatically sent to the card manufacturer.</li>
<li>Making the OrderCardWithPINBlock call, a new PAN file will be created and also sent to the card manufacturer, with the PIN of the card printed on the card carrier.</li>
</ul>
<p>After the new card is created, you need to make the corresponding calls to <strong>Link</strong> that card to your customer´s reference number and <strong>Activate</strong> it to get it ready to use.</p>

<p>Once the card is activated and linked, it is now ready to be funded and used as per the predefined use cases, such as making ATM withdrawals, local and international online payments, point of sale transactions, or closed loop network transactions.</p>

<h2>3. Issuing a <a href="https://developer.sprint.paymentology.com/companion-api/issue-cards/digital-first/">digital-first</a> card</h2>
<p>Digital-first cards are available with Mastercard or Visa and currently available in select regions. The cards are issued similarly as a virtual card where you can use Companion API to create a Virtual Card Number (VCN) as described in the section Issuing a Virtual Card. To print it later, you can follow the steps below:</p>
<h3>Step 1: PrintLinkedCard</h3>
<p>You can use this option if you want the existing digital first cards to be printed.</p>

<p><strong>Note: </strong>Since it would take a few days for the card manufacturer to fulfill the order, using this option does not allow the cards to be issued instantly.</p>
<p> </p>

<h3>Step 2: ToggleVoucherFeature</h3>
<p>You can use this option if you want the printed digital-first cards to be used at POS terminals.</p>

<p><strong>Note: </strong>Since it would take a few days for the card manufacturer to fulfill the order, using step 2 should be done one day after step 1.</p>
<p> </p>
</p></strong></p></p></h3></p></strong></p></p></h3></p></a></h2></p></strong></strong></p></li></li></li></ul></p></p></p></span></p></span></h2></span></a></p></span></p></p></span></p></span></p></div></span></h2></h2>
