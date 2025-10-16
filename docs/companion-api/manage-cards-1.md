---
title: Manage cards
deprecated: false
hidden: false
metadata:
  robots: index
---
<p><strong>You can manage the issued Paymentology Sprint cards and make updates to them whenever necessary. You can also use the API methods below to develop a UI that comes with self-help options that allow the cardholders to manage their cards by themselves.</strong></p>

<p><span style={{fontWeight: "400"}}>These are the supported card management options:</span></p>
<ul>
<li><a href="#stop">Stopping</a> a card</li>
<li><a href="#unstop">Unstopping</a> a card</li>
<li><a href="#retire">Retiring</a> a card</li>
<li><a href="#replace">Replacing</a> a card</li>
<li><a href="#retrieve">Retrieving</a> card details</li>
<li>Getting the <a href="#status">status</a> on a card</li>
</ul>
<p><span style={{fontWeight: "400"}}>Let’s look at each of them.</span></p>

<h2><a id="stop"></a>1. Stopping a card</h2>
<p>To stop a card temporarily, you’ll need to call the <a href="https:developer.sprint.paymentology.com/companion-api/api-reference/local-api/#StopCard"><span className="xml-highlight">​StopCard</span></a> method​​.</p>

<h2><a id="unstop"></a>2. Unstopping a card</h2>
<p>To unstop a card that was stopped previously, you’ll need to call the ​<a href="https:developer.sprint.paymentology.com/companion-api/api-reference/local-api/#UnstopCard"><span className="xml-highlight">UnStopCard</span></a> method​​.</p>

<h2><a id="retire"></a>3. Retiring a card</h2>
<p>To cancel (retire) your card permanently, you’ll need to call the <span style={{color: "#0000ff"}}>​</span><a href="https:developer.sprint.paymentology.com/retirecard/"><span className="xml-highlight">RetireCard</span></a> method​.</p>

<h2><a id="replace"></a>4. Replacing a card</h2>
<p>​To replace an old card with a new card and transfer the link from the old card to the new card, you’ll need to call the ​<a href="https:developer.sprint.paymentology.com/companion-api/api-reference/local-api/#TransferLink"><span className="xml-highlight">TransferLink</span></a> method.</p>

<h2><a id="retrieve"></a>5. Retrieving card details</h2>
<p>To get the details of a card that was previously linked or created, you’ll need to make a call to the ​<a href="https:developer.sprint.paymentology.com/companion-api/api-reference/local-api/#GetActiveLinkedCards"><span className="xml-highlight">GetActiveLinkedCards</span></a> method. <em>Active card</em> refers to a card that is not stopped, retired or cancelled.</p>

<h2><a id="status"></a>6. Getting the status on a card</h2>
<p>To retrieve the status of a card that is linked to a unique customer reference number, you’ll need to make a call to the <a href="https:developer.sprint.paymentology.com/companion-api/api-reference/local-api/#Status"><span className="xml-highlight">Status</span></a> method​​.</p>
</span></a></p></a></h2></em></span></a></p></a></h2></span></a></p></a></h2></span></a></span></p></a></h2></span></a></p></a></h2></span></a></p></a></h2></span></p></a></li></a></li></a></li></a></li></a></li></a></li></ul></span></p></strong></p>
