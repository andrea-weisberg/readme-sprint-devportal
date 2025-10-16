---
title: Remote
deprecated: false
hidden: false
metadata:
  robots: index
original_path: companion-api/api-reference
---
<p>The Remote API is hosted on your platform and allows us to call you to perform actions on your store of value/wallet e.g. Deducting/loading funds, balance inquiries, etc.</p>
<p id="intro"><strong>Note:</strong> you will need to implement the relevant method names corresponding to the different calls in order to perform the necessary actions on your system.</p>



<!-- spacing: desktop=20, mobile=10 -->


<h2>Available Methods</h2>
<ul>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/administrativemessage/">AdministrativeMessage</a> &#8211; Sends a message to a client for MDES digitization activation code OR sends message with 3D Secure OTP</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/balance/">Balance</a> &#8211; Checks the balance on a card</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/brazilianinstallmentsettled/">BrazilianInstallmentSettled</a> &#8211; Notifies that a Brazilian installment transaction is settled</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/deduct/">Deduct</a> &#8211; Deduct the requested amount from a wallet</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/deductadjustment/">DeductAdjustment</a> &#8211; Adjust a previous transaction, deduct the requested amount from a wallet</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/deductreversal/">DeductReversal</a> &#8211; Reverse a deduct that was previously requested on a wallet</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/loadadjustment/">LoadAdjustment</a> &#8211; Adjust a previous transaction, load a wallet</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/loadauth/">LoadAuth</a> &#8211; Request to pre-load in case of refund request or a payment request</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/loadauthreversal/">LoadAuthReversal</a> &#8211; Request to reverse the pre-load requested in LoadAuth</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/loadreversal/">LoadReversal</a> &#8211; Reverse a load that was previously requested on a wallet</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/mexicaninstallmentsettled/">MexicanInstallmentSettled</a> &#8211; Notifies that a Mexican installment transaction has been settled.</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/stop/">Stop</a> &#8211; Notification that a card was stopped</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/validatepin/">ValidatePIN</a> &#8211; Validate the PIN</li>
</ul>
