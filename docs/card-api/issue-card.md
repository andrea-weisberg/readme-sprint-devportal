---
title: Issue cards
deprecated: false
hidden: false
metadata:
  robots: index
---
<h2><span style="font-size: 20px;">With the Card API you can o</span><span style="font-size: 20px;">ffer your customers two types of cards</span><span style="font-size: 20px;">:</span></h2>

<p>**Card-API-issuing-process-flow-v2.png IMAGE GOES HERE.**</p>

<h2>1. Issuing a virtual card</h2>
<p>You can use the Card API to create a Virtual Card Number (VCN), which you can link to the unique customer reference number.</p>
<p><span style="font-weight: 400;">The VCN  will then act as your customer’s identifier, which is useful if you want to manage or fund the card at a later stage.  This means that you may not need to store the PAN number (Permanent Account Number) at all.</span></p>
<p><span style="font-weight: 400;">Once the API receives the request</span>, it will create a 16-digit PAN number, CVV (Card Verification Value), and an expiry date — which are the constituents of the virtual card. You can then forward this information to your customer.</p>

<p>After the VCN has been linked to the customer’s store of value, they can instantly start transacting on any e-commerce site or application that accepts the chosen card association.</p>
<p>​You can also create and issue multiple virtual cards and label them differently to allow for easier management and identification.</p>

<h2><a name="#physical"></a>2. Issuing a physical card​​</h2>
<p>You can create and issue a physical card and send a request to Paymentology to link it to a unique customer reference number.​</p>
<p>You can decide to have one card linked per customer or multiple cards linked to a single customer.​</p>
<p>Once the card is linked, it is now ready to be funded and used as per the predefined use cases, like making ATM withdrawals, local and international online payments, point of sale transactions, or closed-loop network transactions.</p>
<p>​There are two options for issuing physical cards: Issue on-site and link immediately or issue with courier and link later</p>

<p>Making this call will lead to the following:</p>
<ul>
<li>A PAN number file will be created and sent to the card manufacturer automatically.</li>
<li>The card manufacturer will create the physical card and deliver it to the cardholder.</li>
<li>The cardholder will need to activate and link the card using the ActivateCard and LinkCard API method.</li>
</ul>
<p> </p>

</p></li></li></li></ul></p></p></p></p></p></a></h2></p></p></span></p></span></p></p></h2></p></span></span></span></h2>
