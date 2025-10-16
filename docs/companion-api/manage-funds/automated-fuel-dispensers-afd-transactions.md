---
title: AFD Transactions
deprecated: false
hidden: false
metadata:
  robots: index
---
<p><span style="font-weight: 400;">Automated Fuel Dispensers (AFD) are unattended terminals at fuel stations that allow cardholders to purchase fuel without requiring an attendant. The emergence of AFD transactions has revolutionized the fuel purchase industry and greatly benefitted both merchants and customers.</span></p>
<p><span style="font-weight: 400;">In the past, fueling was a tedious process—an attendant had to manually pump the requested amount of fuel, usually resulting in lines and customer queues. However, AFDs has turned this around—no more direct engagements with staff and other time-consuming hassles.</span></p>
<p><span style="font-weight: 400;">With Paymentology Sprint’s support for AFD transactions, you can make payments</span><span style="font-weight: 400;"> for your cardholders </span><span style="font-weight: 400;">at the pump painless, fast, and secure.</span></p>

<h2><b>Benefits of AFD Transactions</b></h2>
<ul>
<li aria-level="1"><b>Speeds up fueling for customers</b></li>
</ul>
<p><span style="font-weight: 400;">At unattended terminals, a customer can quickly and conveniently obtain fuel without the time-consuming hassle of having to wait to be served. A customer can simply tap, dip, or swipe their card without the manual process of engaging an attendant. </span></p>
<ul>
<li aria-level="1"><b>Enhances customer experience</b></li>
</ul>
<p><span style="font-weight: 400;">AFDs offer a convenient way for drivers to gas up and get back on the road without the usual fueling hassles. This streamlined experience results in customer loyalty and more business to merchants. </span></p>
<ul>
<li aria-level="1"><b>Reduces costs</b></li>
</ul>
<p><span style="font-weight: 400;">Although AFDs require an initial capital cost to install and set up, they can reduce operational costs in the long run. Their automated nature implies that personnel costs are minimal.</span></p>
<p><span style="font-weight: 400;">The convenience of AFDs also enables customers not to waste time and fuel—which equals money—when fueling their vehicles.</span></p>
<ul>
<li aria-level="1"><b>Increases purchase sizes</b></li>
</ul>
<p><span style="font-weight: 400;">Since AFDs allow customers to use their payment cards, which could be directly connected to their deposit and line-of-credit accounts, they reduce the chances of abandoning payments. Merchants do not need to worry about customers not having enough cash in their wallets.</span></p>
<ul>
<li aria-level="1"><b>Lowers theft possibilities</b></li>
</ul>
<p><span style="font-weight: 400;">The traditional way of using cash at fuel outlets is prone to employee theft, robbery, or unintentional miscounting. By eliminating cash, this risk is drastically reduced.</span></p>

<h2><b>Best Practices For AFD Transactions</b></h2>
<ul>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">Ensure all purchase transactions are properly authorized. Remember that the available authorization methods vary based on the merchant type and region.</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">Ensure that any approved amount that was not settled is promptly reversed. This would avert any cardholder account holds and/or unnecessary potential fees.</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">Ensure estimated transactions are handled appropriately. If the final amount surpasses the estimated amount, you should obtain additional authorization. Remember that the confirmation advice or the settlement should never be higher than the initial authorization amount sent from the AFD POS.</span></li>
</ul>

<h2>AFD Transactions Flow</h2>
<p>**AFD-Transaction-processing-v2.png IMAGE GOES HERE.**</p>

<ol>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">Cardholder makes a transaction at an AFD POS</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">POS sends an authorization request to a card scheme</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">Card scheme sends an authorization to Paymentology</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">Paymentology sends payment authorization to a wallet provider</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">Wallet provider accepts or rejects the transaction based on the availability of funds</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">If the wallet accepts successfully, confirmation advice is passed from AFD POS to the card scheme. If the wallet declines, the decline reason response will be sent</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">AFD POS device passes confirmation to the card scheme. Card scheme sends confirmation advice to Paymentology </span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">Paymentology processes the confirmation advice and checks if there is a pending balance from the original authorization</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">Paymentology sends a reversal to the wallet provider for the balance of the original pre-authorization amount. </span></li>
</ol>
</span></li></span></li></span></li></span></li></span></li></span></li></span></li></span></li></span></li></ol></p></h2></span></li></span></li></span></li></ul></b></h2></span></p></b></li></ul></span></p></b></li></ul></span></p></span></p></b></li></ul></span></p></b></li></ul></span></p></b></li></ul></b></h2></span></span></span></p></span></p></span></p>
