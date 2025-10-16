---
title: Manage cards
deprecated: false
hidden: false
metadata:
  robots: index
---
<p><strong>You can manage the issued Paymentology cards and make updates to them whenever necessary. You can also use the API methods below to develop a UI that comes with self-help options that allow the cardholders to manage their cards by themselves.</strong></p>
<p>These are the supported card management options:</p>
<ul>
<li>Getting card balances and other details</li>
<li>Getting a card’s transactions statement</li>
<li>Adding cardholder details to a card</li>
<li>Retrieving cardholder details</li>
<li>Getting a list of cards linked to a customer</li>
<li>Enabling and disabling a card’s features</li>
<li>Updating a card label</li>
<li>Stopping a card</li>
<li>Unstopping a card</li>
<li>Retiring a card</li>
</ul>
<p>Let’s look at each of them.</p>

<h2>1. Getting card balances and other details</h2>
<p>To get the balance on a card, get the card details, or get the status of a card, you’ll need to make a call to the <span className="xml-highlight">CardDetail</span> method.</p>

<h2>2. Getting a card’s transaction statement</h2>
<p>To get a statement of the list of transactions on a card, you’ll need to make a call to the <span className="xml-highlight">Statement</span> method.</p>

<h2>3. Adding cardholder details to a card</h2>
<p>To add the cardholder’s details to a card, store KYC (Know Your Customer) information, or perform the sanctions screening, you’ll need to make a call to the <span className="xml-highlight">SetBearerDetail</span> method.</p>
<p>You can also choose to opt-out of some parameter options. For example, if you only want to set the cardholder’s details, then this is the only information you can send, and the rest of the parameter options will remain as null.</p>

<h2>4. Retrieving cardholder details</h2>
<p>To retrieve the set details of the cardholder, you’ll need to make a call to the <span className="xml-highlight">BearerDetail</span> method.</p>

<h2>5. Getting a list of cards linked to a customer</h2>
<p>To get a list of all cards linked to a customer reference number, you’ll need to make a call to the <span className="xml-highlight">ListCards</span> method.</p>

<h2>6. Enabling and disabling a card’s features</h2>
<p>To enable and disable features on specific cards, such as the ability to make international transactions or magstripe transactions, you’ll need to make a call to the<span className="xml-highlight"> ToggleVoucherFeature </span>method.</p>

<h2>7. Updating a card label</h2>
<p>To update a label for a card that has already been issued, you’ll need to make a call to the <span className="xml-highlight">UpdateCardLabel</span> method.</p>

<h2>8. Stopping a card</h2>
<p>To stop a card temporarily, you’ll need to make a call to the <span className="xml-highlight">StopCard</span> method.</p>

<h2>9. Unstopping a card</h2>
<p>To unstop a card that was stopped previously, you’ll need to make a call to the <span className="xml-highlight">UnstopCard</span> method.</p>

<h2>10. Retiring a card</h2>
<p>To cancel (retire) your card permanently, you’ll need to make a call to the <span className="xml-highlight">RetireCard</span> method. You should ensure the funds are removed from the card before it is retired. Once retired, the card will not be able to be used again.</p>
</span></p></h2></span></p></h2></span></p></h2></span></p></h2></span></p></h2></span></p></h2></span></p></h2></p></span></p></h2></span></p></h2></span></p></h2></p></li></li></li></li></li></li></li></li></li></li></ul></p></strong></p>
