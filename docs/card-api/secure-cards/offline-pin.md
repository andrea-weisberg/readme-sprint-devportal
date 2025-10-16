---
title: Offline PIN
deprecated: false
hidden: false
metadata:
  robots: index
---
<p>Offline PIN is a card verification method used for EMV chip cards as the PIN is stored on the chip. This means that cardholder verification can occur even if a POS terminal is not connected to a network.</p>

<section id="tutuka-block-5" className="tutuka-block tutuka-block--text-full-width">
<div className="tutuka-block--text-full-width__content">
<p>The way the offline PIN transactions differ from online PIN transactions is with online PIN, the PIN is encrypted and sent to Paymentology in an ISO message however with offline PIN transactions, we use different cardholder verification methods and checks to validate the transaction.</p>
</div>
</section>
<div id="tutuka-block-6" className="tutuka-block tutuka-block--spacing"></div>

<h3>How to update the Offline PIN</h3>
<ol className="ak-ol" data-indent-level="1">
<li>
<p data-renderer-start-pos="4217">The issuer calls the <a href="https:developer.sprint.paymentology.com/card-api/api-reference/changepin/">ChangePIN</a> API</p>
</li>
<li>
<p data-renderer-start-pos="4306">We instantly update the online PIN, and record the fact that the offline PIN needs updating</p>
</li>
<li>
<p data-renderer-start-pos="4401">The next time a card-present transaction arrives, that is not NFC based, we will return the issuer script to the terminal, which should tell the card to update the script</p>
</li>
<li>
<p data-renderer-start-pos="4575">In the following transaction, if it specifies that the previous attempt to update the issuer script fails, we will mark the update as needing reprocessing again</p>
</li>
</ol>
</p></li></p></li></p></li></a></p></li></ol></h3></div></p></div></section></p>
