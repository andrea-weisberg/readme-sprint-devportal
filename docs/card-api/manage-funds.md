---
title: Manage funds
deprecated: false
hidden: false
metadata:
  robots: index
---
<p><strong>Once a cardholder has been issued with a card, they can start to manage the funds associated with their card or pockets.</strong><br >
​<br >
These are the supported options for managing funds:​</p>
<ul>
<li>Loading funds onto the card</li>
<li>Reversing the load</li>
<li>Transferring funds between cards</li>
<li>Reversing funds transferred between cards</li>
<li>Transferring funds between pockets</li>
<li>Reversing the pocket transfer</li>
<li>Deducting funds from card or pocket</li>
<li>Reversing the card deduction</li>
<li>Devaluing a card or pocket</li>
<li>Reversing the card’s devalue</li>
</ul>
<p>Let’s look at each of them.</p>

<h2>1. Loading funds onto the card​​</h2>
<p>​You can load funds onto a card balance or a pocket (if you’ve opted for pockets). If you do not have pockets, then the funds will be loaded directly onto the card.​ If you’re loading the funds onto a pocket, then you’ll need to specify the target pocket’s UUID (universally unique identifier) number, which Paymentology provides.​</p>
<p>To carry out the loading of funds, the client manages a separate process that makes a debit from the store of value account and credits it to the card. ​It’s also possible to set limits that predefine the amount that can be loaded on the card.</p>
<p>You’ll need to make a call to the <span className="xml-highlight">LoadFunds</span> method.</p>

<h2>2. Reversing the load​</h2>
<p>​If you want to reverse the loaded funds on the card, for any reason, and the funds have not been used, then you can initiate a reversal process.</p>
<p>You’ll need to make a call to the <span className="xml-highlight">LoadFundsReverse</span> method.</p>

<h2>3. Transferring funds between cards​​</h2>
<p>​If there are cards issued within the same program, funds can be transferred between them easily.​ For example, if two people have cards from the same program, they can send each other funds easily.</p>
<p>You’ll need to make a call to the <span className="xml-highlight">TransferFunds</span> method.</p>

<h2>​4. Reversing funds transferred between cards​​</h2>
<p>If you want to reverse the transferred funds, for any reason, and the funds have not been used, then you can initiate a reversal process.</p>
<p>You’ll need to make a call to the​ <span className="xml-highlight">TransferFundsReverse</span> method.</p>

<h2>5. Transferring funds between pockets​​</h2>
<p>​You can transfer funds between pockets for the easy management of money. For example, you may want to transfer some funds from your expenditure pocket to your savings pocket.</p>
<p>You’ll need to make a call to the​ <span className="xml-highlight">PocketTransfer</span> method.</p>

<h2>6. Reversing the pocket transfer​​</h2>
<p>​<br >
If you want to reverse the funds transferred to a pocket, for any reason, and the funds have not been used, then you can initiate a reversal process.</p>
<p>You’ll need to make a call to the​ <span className="xml-highlight">PocketTransferReverse</span> method.</p>

<h2>7. Deducting funds from card or pocket​​</h2>
<p>​If a cardholder wants to deduct funds from their card or pocket balances, then they can specify the value that needs to be deducted. The amount requested to be deducted must be equal or less than the balance; otherwise, the process will not be successful. After the deduction has been completed successfully, the client then credits the customer’s store of value account.</p>
<p>You’ll need to make a call to the <span className="xml-highlight">DeductFunds</span> method.</p>

<h2 className="block highlight" data-element="bridgehead" data-attr-renderas="sect3" data-attr-xml-id="bridgehead-idm4646117335828831693994440263"><span className="inline translation current" data-element="emphasis" data-attr-role="bold" data-attr-xinfo-text="10463">8. Reversing the card deduction​</span>​</h2>
<p className="placeholder">​If you want to reverse the funds deducted, for any reason, then you can initiate a reversal process. ​Once successful, the balance will change based on the reversed amount.</p>
<p className="placeholder"><span className="inline link linktool link-external" data-element="link" data-attr-xlink-href="https:developer.sprint.paymentology.com/card/documentation/card-api#deductfundsreverse">You’ll need to make a call to the ​<span className="xml-highlight">DeductFundsReverse</span> method.</span></p>

<h2>​9. Devaluing a card or pocket​​</h2>
<p>​You can perform a deduction of the full amount available on the card or pocket. No partial amount will be removed from the card or pocket balances, but only all the funds.</p>
<p>You’ll need to make a call to the <span className="xml-highlight">​Devalue</span> method.</p>

<h2>10. Reversing a devalue​​​</h2>
<p>If you want to reverse the devaluing of funds from a card or pocket balance, for any reason, then you can initiate a reversal process. ​Once successful, the devalued amount will be credited to the card or pocket balance.</p>
<p>You’ll need to make a call to the​ <span className="xml-highlight">DevalueReverse</span> method.</p>
</span></p></p></h2></span></p></p></h2></span></span></p></p></span></h2></span></p></p></h2></span></p></p></h2></span></p></p></h2></span></p></p></h2></span></p></p></h2></span></p></p></h2></span></p></p></p></h2></p></li></li></li></li></li></li></li></li></li></li></ul></strong></p>
