---
title: Manage funds
deprecated: false
hidden: false
metadata:
  robots: index
---
<p><strong>When the cardholder has either a virtual or a physical companion card (or both), they can start transacting against their store of value. These transactions originate from the merchant and are then sent to Paymentology via the card schemes, before being forwarded to the store of value for validation and authorization.</strong></p>

<p><span style={{fontWeight: "400"}}>These are the supported transaction management options:</span></p>
<ul>
<li style={{fontWeight: "400"}}><span style={{fontWeight: "400"}}>Getting a balance on a card</span></li>
<li style={{fontWeight: "400"}}><span style={{fontWeight: "400"}}>Doing a deduct transaction on a card</span></li>
<li style={{fontWeight: "400"}}><span style={{fontWeight: "400"}}>A reversal for a deduct transaction </span></li>
<li style={{fontWeight: "400"}}><span style={{fontWeight: "400"}}>Adjustments on a card</span></li>
</ul>

<h2>1. Getting a balance on a card</h2>
<div className="block translation current highlight" data-element="para" data-attr-xinfo-text="10671">
<p><span style={{fontWeight: "400"}}>If a card is enabled for ATM transactions, then the cardholder can make balance inquiries at an ATM machine. </span><span style={{fontWeight: "400"}}>The balance that is sent back is the amount remaining in the stored value.</span></p>
<p>You’ll need to make a call to the <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/balance/"><span className="xml-highlight">Balance</span></a> method.</p>
</div>

<h2>2. Doing a deduct transaction on a card​</h2>
<p><span style={{fontWeight: "400"}}>When a cardholder makes an ATM, point of sale (POS), or e-commerce transaction, Paymentology will send a Deduct request for the funds to be deducted from the store of value. </span></p>
<p>You’ll need to respond with Approved for the transaction to be concluded successfully.</p>
<p> </p>
<p>**Companion-transaction-processing-3-v2.png IMAGE GOES HERE.**</p>

<h2>3. A <a id="reversal"></a>reversal for a deduct transaction</h2>
<div className="block translation current highlight" data-element="para" data-attr-xinfo-text="10678">
<p><span style={{fontWeight: "400"}}>A reversal is essentially a request for a transaction that was not completed and could have failed at a particular step of the transaction process. </span><span style={{fontWeight: "400"}}>It is an advisement message to all parties of the transaction and ensures that the card and store of value are put back into their original state if a failed to deduct transaction had been initiated.</span></p>
<p><span style={{fontWeight: "400"}}>If you sent a transaction and did not receive a confirmation that the transaction was successful, it could imply that the transaction did not reach the intended destination.</span></p>
<p>Reversals are triggered by merchants for three reasons:</p>
<h4>1. The merchant did not receive any response back from the card scheme for the authorization request. In this case, the merchant would timeout the transaction</h4>
<p>Scenario: In this scenario, a <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/deduct/"><span className="xml-highlight">Deduct</span> </a>request was sent to the store of value system but there was no response received. This will cause a time out, as no response will be sent back to the merchant.</p>
<p><strong><em>A full cycle of an authorization must be concluded within 5 seconds meaning a response from the store of value system needs to be received with 2 seconds maximum.</em></strong></p>
<p>Due to no response, a <span className="xml-highlight"><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/deductreversal/">DeductReversal</a> </span>will be triggered and the store of value system will match the <strong>TransactionID </strong>of the initial <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/deduct/"><span className="xml-highlight">Deduct</span> </a>and match it with the <strong>ReferenceID</strong> in the <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/deductreversal/"><span className="xml-highlight">DeductReversal</span> </a>and <strong>Approves</strong> the <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/deductreversal/"><span className="xml-highlight">DeductReversal</span> </a>by responding with <strong>1 – Success</strong> and reverse the funds the funds back.</p>
<p>The store of value system does not have the option to respond with a -9 Crashed or disapproved response.</p>
<h4>2. The merchant receives a timeout request from the card scheme due to connectivity issues</h4>
<p>Scenario: In the scenario, due to connectivity issues the <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/deduct/"><span className="xml-highlight">Deduct</span> </a>request is not sent to the store of value system. This results in a timeout in the transaction. The merchant will timeout the transaction and trigger a <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/deductreversal/"><span className="xml-highlight">DeductReversal</span> </a>which will be sent to the store of value system. At this point, the store of value system has no record of the initial <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/deduct/"><span className="xml-highlight">Deduct</span></a>.</p>
<p>The store of value system will attempt to match the <strong>ReferenceID</strong> in the <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/deductreversal/"><span className="xml-highlight">DeductReversal</span></a>, which they will not find as the initial <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/deduct/"><span className="xml-highlight">Deduct</span> </a>did not reach the store of value system. The store of value system will send an acknowledgement = <strong>1 – Success </strong>but no funds will be moved on the store of value system</p>
<p>The store of value system may not respond with a -9 Crashed or disapproved response.</p>
<p> </p>
<h4>3. The merchant voided the transaction</h4>
<p>Scenario: In this scenario, the authorization is cancelled/ voided immediately after a successful transaction has been concluded. The store of value system will have received the initial <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/deduct/"><span className="xml-highlight">Deduct</span> </a>request.</p>
<p>The store of value system will match the <strong>ReferenceID</strong> of the <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/deductreversal/"><span className="xml-highlight">DeductReversal</span> </a>to the <strong>Transaction id</strong> of the initial <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/deduct/"><span className="xml-highlight">Deduct</span> </a>request. They will reverse the funds and respond with <strong>1 – Success.</strong></p>
<p>The store of value system may not respond with a -9 Crashed or disapproved response.</p>
</div>
<p> </p>
<p>Also, the transaction could have reached the destination and was processed correctly, but the confirmation response was “lost” along the way.</p>
<div className="block translation current highlight" data-element="para" data-attr-xinfo-text="10678">
<p style={{margin: "12.0pt 0cm 12.0pt 0cm"}}><span style={{fontSize: "11.0pt", fontFamily: "'Arial',sans-serif", color: "black", background: "white"}}>Paymentology will link the deduct reversal to the original authorization, we do this by including a <span className="xml-highlight">ReferenceID</span> in the <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/deductreversal/"><span className="xml-highlight">DeductReversal</span> </a>API request. The <span className="xml-highlight">ReferenceID</span> field is the transaction id of the original authorization (Deduct).</span></p>
<p><span style={{fontWeight: "400"}}>Here is a table that shows the only acceptable response codes that can be sent to Paymentology:</span></p>
</div>

<p>**Reversal-v2.png IMAGE GOES HERE.**</p>

<h2>4. Adjustments on a card</h2>
<div className="block translation current highlight" data-element="para" data-attr-xinfo-text="10694">
<p><span style={{fontWeight: "400"}}>Just like in any other account, there may be times when your funds need to be adjusted to reflect some changes that have occurred. </span></p>
<p><span style={{fontWeight: "400"}}>For example, a refund could have been issued to your card, and it needs to be adjusted on the store of value as this is where the balance will be managed eventually.</span></p>
<p><span style={{fontWeight: "400"}}>These are the common types of adjustment transactions on companion cards:</span></p>
<ul>
<li style={{fontWeight: "400"}}><span style={{fontWeight: "400"}}>Load adjustment transactions</span></li>
<li style={{fontWeight: "400"}}><span style={{fontWeight: "400"}}>Load reversal transactions</span></li>
<li style={{fontWeight: "400"}}><span style={{fontWeight: "400"}}>Deduct adjustment transactions</span></li>
</ul>
<p><span style={{fontWeight: "400"}}>Let’s look at each of them.</span></p>
</div>

<h3><b>i) <a id="Loadadjustment"></a>Load adjustment transactions</b></h3>
<p><span style={{fontWeight: "400"}}>If there is a need to load money back into a store of value, Paymentology will send a load adjustment request so that the store of value makes the adjustment. </span></p>
<p><strong><a id="LoadAuth"></a>LoadAuth</strong></p>
<p><span style={{fontWeight: "400"}}>LoadAuth is an authorisation, but for a load, rather than a deduct. This would most commonly be the result of a <strong>refund</strong> from a merchant. But it could also be a load from a “money send” type transaction, where cardholders can transfer funds over the MC network, if your program allows this. </span><span style={{fontWeight: "400"}}>This method is most similar to the </span><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/deduct/"><span style={{fontWeight: "400"}}><span className="xml-highlight">Deduct</span></span></a><span style={{fontWeight: "400"}}> method, which is an authorisation for a redemption.</span></p>
<p>You can decline this transaction i.e. <em>choose not to approve it</em>. If you decline, the refund will not be completed at the merchant. There are 3 important things to note:</p>
<ul>
<li>If you approve this transaction, <em><strong>do not</strong></em> immediately load the card</li>
<li>Unlike <span className="xml-highlight"><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/deduct/">Deduct</a> </span>, the card should <em><strong>only</strong></em> be loaded when the funds are cleared because then you know you have received them (for most systems, after evaluating and approving this transaction, there would be nothing further for you to do). You may choose to reflect a <em>pending</em> amount on cardholder statements but this should not be included in their available balance</li>
<li>If you decline this transaction, you should expect cardholder frustration because cardholders are not familiar with refunds being declined because it does not depend on their available balance. Therefore, it is recommended that you approve these transactions unless there are strong reasons not to. <em>NB. If a refund is fraudulent for some reason, the liability sits with the Merchant. </em></li>
</ul>
<p>Mastercard has mandated that refunds should be authorised but merchants do not follow this. Therefore, you will find very few <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/loadauth/"><span className="xml-highlight">LoadAuth</span> </a>requests as most as just sent immediately as settlement (which you will receive as <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/loadadjustment/"><span className="xml-highlight">LoadAdjustments</span></a>)</p>
<p><span style={{fontWeight: "400"}}>Once the request has been approved, the amounts on both the card and the store of value will be balanced. </span></p>
<p><span style={{fontWeight: "400"}}>However, if the request is not accepted by the store of value, Paymentology will continue sending it ten times at regular intervals. If unsuccessful, the adjustment request will be retired as not processed.</span></p>
<p><span style={{fontWeight: "400"}}>Here is a table that shows the only acceptable response codes that can be sent to Paymentology: </span></p>

<p>You’ll need to respond to the <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/loadadjustment/"><span className="xml-highlight">LoadAdjustment</span> </a>method.</p>

<h3>LoadAdjustment</h3>
<p>As for a <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/loadauth/"><span className="xml-highlight">LoadAuth</span></a>, this is the result of a refund or a money transfer request that loads funds to a cardholder but this is an advice message confirming that the funds have moved.</p>
<p>When a <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/loadauth/"><span className="xml-highlight">LoadAuth</span> </a>is settled, it will result in a <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/loadadjustment/"><span className="xml-highlight">LoadAdjustment</span> </a>(this assumes no <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/loadauthreversal/"><span className="xml-highlight">LoadAuthReversal</span> </a>occurred). As with all advice messages, it is <strong>required</strong> that the message is approved. There is no other option except for a system failure/crash. Your response of “1” is not “approving” the adjustment, it is confirming that you have been notified of the adjustment. All adjustments have already occurred and declining such a message will not change that. If you respond with anything besides approval, it results in a process of manual intervention to investigate why the failure occurred and to work with you to take steps to correct it.</p>
<p> </p>
<p>Many clients wish to link any refunds back to the original transaction. MasterCard has implemented some fields to allow this, but merchants  do not use these fields. From their perspective, they do not see any reason necessary to complete the development necessary for this to work. This is similar to merchants being mandated to obtain authorisation for refunds, which they also tend not to do. To a significant degree, you would want to be cautious about how much energy you invest in trying to do this. As an Issuer, if you receive a refund settlement, you must process and if there is fraud taking place at the Merchant, it is at the Merchant’s cost – not yours.</p>
<p>If you really don’t want to refund a wallet unless you can reconcile the refund, our recommended course of action is:</p>
<ul>
<li>Acknowledgement of he adjustment API (you have to do this)</li>
<li>But then, do not load the wallet</li>
</ul>
<p>In other words, once you have acknowledged the API call with a valid APO response, Paymentology does not concern itself with how you handle those funds. so, you could choose to reflect the funds in some holding account and the you work through some administrative process to approve the refund and then you transfer to the wallet when you are satisfied it is legitimate. This way:</p>
<ul>
<li>You are still responding correctly to the API calls</li>
<li>You still have control of the funds and when and where to load them without having caused a failure by rejecting the API call</li>
</ul>

<h3>​ii) <a id="Reversal"></a>Load reversal transactions</h3>
<div className="block translation current highlight" data-element="para" data-attr-xinfo-text="10714">
<p><span style={{fontWeight: "400"}}>If there is a need to load money back into a store of value, and the client is not accepting the adjustment request, Paymentology will send a load reversal request to ensure that no action is undertaken. </span></p>
<p><strong>LoadAuthReversal</strong></p>
<p>This is a reversal message for <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/loadauth/"><span className="xml-highlight">LoadAuth</span> </a>. It is the equivalent of <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/deductreversal/"><span className="xml-highlight">DeductReversal</span> </a>. This will be sent if we do not receive any response to the <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/loadauth/"><span className="xml-highlight">LoadAuth</span> </a>. As with all adjustments and reversals, they are “advice” messages, they are “telling” you to do something. They are not asking you to approve something. Your response should therefore be an acknowledgement that you have received the message not that you “approve” the message. For all reversals, we will keep resending if we do not receive positive acknowledgement. Failure to respond repeatedly results in manual intervention which should only happen if your system is down.</p>
<p>Our recommendation for reversals is:</p>
<ul>
<li style={{fontWeight: "400"}} aria-level="1"><span style={{fontWeight: "400"}}>You should add the reversal to an internal queue (a low intensity operation)</span></li>
<li style={{fontWeight: "400"}} aria-level="1"><span style={{fontWeight: "400"}}>You should then immediately respond positively to our API call</span></li>
<li style={{fontWeight: "400"}} aria-level="1"><span style={{fontWeight: "400"}}>And only then, attempt to process the reversal (a high intensity operation)</span></li>
<li style={{fontWeight: "400"}} aria-level="1"><span style={{fontWeight: "400"}}>This is because very often, reversals only happen during problems s</span><span style={{fontWeight: "400"}}>o you don’t want to exacerbate the problem, by performing complex tasks as you receive the reversal</span></li>
<li style={{fontWeight: "400"}} aria-level="1"><span style={{fontWeight: "400"}}>It’s therefore best to queue the complex tasks for processing only after you have responded</span></li>
<li style={{fontWeight: "400"}} aria-level="1"><span style={{fontWeight: "400"}}>This way we stop messaging you with repeats of reversals, which will only add to your load</span></li>
</ul>
<p><span style={{fontWeight: "400"}}>After that, Paymentology will resend a <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/loadadjustment/"><span className="xml-highlight">LoadAdjustment</span> </a>request so that an OK response can be returned. This pattern will continue ten times until the adjustment is processed adequately against the stored value.</span></p>
<p>You’ll need to make a call to the <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/loadreversal/"><span className="xml-highlight">LoadReversal</span> </a>method.</p>
</div>

<p>Remember, the transaction and reversal failures may be the result of a network interruption that is happening <em>after</em> you have responded each time. You may receive multiple reversals for a reversal which you have already processed so you must be able to identify that you have already processed the reversal to prevent “duplication”.</p>
<p> </p>
<p>What you do on your system for a <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/loadauthreversal/"><span className="xml-highlight">LoadAuthReversal</span> </a>will depend on what you do for a <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/loadauth/"><span className="xml-highlight">LoadAuth</span> </a>. If you approve and did nothing else (see <a href="#LoadAuth">LoadAuth</a> above for more information), then there isn’t anything for you to do when reversing. If your system records and reflects the “pending” load, you’d need to remove this pending load.</p>
<p> </p>

<h3>LoadReversal</h3>
<p>This is sent if we do not receive any response to the <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/loadadjustment/"><span className="xml-highlight">LoadAdjustment</span></a>. All the other rules mentioned in <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/loadauthreversal/"><span className="xml-highlight">LoadAuthReversal</span> </a>still apply.</p>
<ul>
<li>It is an advice message which you must “approve” (i.e. send a response acknowledging the advice message)</li>
<li>It will be repeated if you not respond to it</li>
<li>After 10 repeats, it will be logged for manual intervention</li>
<li>You should add to an internal queue and respond immediately and then process from your queue</li>
</ul>
<p> </p>
<p>One big difference is that, almost without exception, a <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/loadadjustment/"><span className="xml-highlight">LoadAdjustment</span> </a>will result in actual funds having been loaded to a cardholder balance, and so reversing this means you will need to “undo” that load. Again, undoing a load might practically be done through a deduct but you are  not deducting, you are putting the wallet back to it’s previous state. The difference becomes important when ensuring that  you are able to handle repeats. Do not keep deducting every reversal you receive as you may already have done the deduction. Remember that the connection failure we are experiencing with you, might only be for messages after you have processed them.</p>
<p> </p>
<p>Some important points to note about reversals:</p>
<ul>
<li>It <strong>is</strong> possible to receive a reversal for which you cannot find the original reference.<br  />
– You might not find it because you never received the original transaction (this is normal, and part of the design of reversals)<br  />
– You might not find it because, even though you received it, you already reversed it<br  />
In both cases, you would effectively <em>do nothing</em>, because there is nothing to reverse.</li>
<li>Do <strong>not</strong> debit/credit (whichever is applicable) just because you received a reversal. You have to find the original transaction, confirm it has not been reversed, and reverse it. If you cannot find it, or it has already been reversed, there is nothing further to do. You must also still respond positively to the Reversal API call confirming you received it</li>
<li>You do not need to tell us (since it is not relevant) whether you found the original transaction to reverse or not</li>
</ul>

<h3>iii) Deduct adjustment transactions</h3>
<div className="block translation current highlight" data-element="para" data-attr-xinfo-text="10718">
<p><span style={{fontWeight: "400"}}>In some cases, there may be a discrepancy between the funds that were authorized on a transaction and what was actually settled. </span><span style={{fontWeight: "400"}}>When a user makes a purchase at a point of sale, it takes a two-step process for the transaction to be completed. </span></p>
<p><span style={{fontWeight: "400"}}>First, an authorization request is made and the funds for the transaction are taken from the card and kept in reserve. </span></p>
<p><span style={{fontWeight: "400"}}>Then, the second half of the transaction takes place when the bank that processes the merchant’s payments generates a clearing request to the given card association for this authorization to be settled. </span><span style={{fontWeight: "400"}}>Just like the authorization request, the card associations also forward this settlement request to Paymentology.</span></p>
<p><span style={{fontWeight: "400"}}>So, whenever the clearing request amount is higher than the authorization request amount for any reason, such as due to rising exchange rates, the store of value will be debited for this differing amount.  </span><span style={{fontWeight: "400"}}>The store of value must acknowledge this request for it to be handled appropriately. </span><span style={{fontWeight: "400"}}>Although the cardholder has the right to dispute this transaction, the debit should happen first before the dispute can be filed. </span></p>
<p><span style={{fontWeight: "400"}}>If the store of value does not send an OK response to Paymentology, then the card will remain in a state of having a pending adjustment, and no transaction would be processed until the adjustment has been rectified.</span></p>
<p>You’ll need to make a call to the <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/deductadjustment/"><span className="xml-highlight">DeductAdjustment</span> </a>method.</p>
</div>

