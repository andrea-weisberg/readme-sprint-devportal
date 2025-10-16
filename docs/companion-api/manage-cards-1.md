---
title: Manage cards
deprecated: false
hidden: false
metadata:
  robots: index
original_path: companion-api
---
<p><strong>You can manage the issued Paymentology Sprint cards and make updates to them whenever necessary. You can also use the API methods below to develop a UI that comes with self-help options that allow the cardholders to manage their cards by themselves.</strong></p>



<!-- spacing: desktop=20, mobile=10 -->


<p><span style="font-weight: 400;">These are the supported card management options:</span></p>
<ul>
<li><a href="#stop">Stopping</a> a card</li>
<li><a href="#unstop">Unstopping</a> a card</li>
<li><a href="#retire">Retiring</a> a card</li>
<li><a href="#replace">Replacing</a> a card</li>
<li><a href="#retrieve">Retrieving</a> card details</li>
<li>Getting the <a href="#status">status</a> on a card</li>
</ul>
<p><span style="font-weight: 400;">Let&#8217;s look at each of them.</span></p>



<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<h2><a id="stop"></a>1. Stopping a card</h2>
<p>To stop a card temporarily, you’ll need to call the <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/#StopCard"><span class="xml-highlight">​StopCard</span></a> method​​.</p>



<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<h2><a id="unstop"></a>2. Unstopping a card</h2>
<p>To unstop a card that was stopped previously, you’ll need to call the ​<a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/#UnstopCard"><span class="xml-highlight">UnStopCard</span></a> method​​.</p>



<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<h2><a id="retire"></a>3. Retiring a card</h2>
<p>To cancel (retire) your card permanently, you’ll need to call the <span style="color: #0000ff;">​</span><a href="https://developer.sprint.paymentology.com/retirecard/"><span class="xml-highlight">RetireCard</span></a> method​.</p>



<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<h2><a id="replace"></a>4. Replacing a card</h2>
<p>​To replace an old card with a new card and transfer the link from the old card to the new card, you’ll need to call the ​<a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/#TransferLink"><span class="xml-highlight">TransferLink</span></a> method.</p>



<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<h2><a id="retrieve"></a>5. Retrieving card details</h2>
<p>To get the details of a card that was previously linked or created, you’ll need to make a call to the ​<a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/#GetActiveLinkedCards"><span class="xml-highlight">GetActiveLinkedCards</span></a> method. <em>Active card</em> refers to a card that is not stopped, retired or cancelled.</p>



<!-- unsupported_acf_block: line_separator {"acf_fc_layout":"line_separator"} -->


<h2><a id="status"></a>6. Getting the status on a card</h2>
<p>To retrieve the status of a card that is linked to a unique customer reference number, you’ll need to make a call to the <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/#Status"><span class="xml-highlight">Status</span></a> method​​.</p>
