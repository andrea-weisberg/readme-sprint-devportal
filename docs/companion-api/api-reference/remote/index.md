---
title: Remote
deprecated: false
hidden: false
metadata:
  robots: index
---
<p>The Remote API is hosted on your platform and allows us to call you to perform actions on your store of value/wallet e.g. Deducting/loading funds, balance inquiries, etc.</p>
<p id="intro"><strong>Note:</strong> you will need to implement the relevant method names corresponding to the different calls in order to perform the necessary actions on your system.</p>

<h2>Available Methods</h2>
<ul>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/administrativemessage/">AdministrativeMessage</a> – Sends a message to a client for MDES digitization activation code OR sends message with 3D Secure OTP</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/balance/">Balance</a> – Checks the balance on a card</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/brazilianinstallmentsettled/">BrazilianInstallmentSettled</a> – Notifies that a Brazilian installment transaction is settled</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/deduct/">Deduct</a> – Deduct the requested amount from a wallet</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/deductadjustment/">DeductAdjustment</a> – Adjust a previous transaction, deduct the requested amount from a wallet</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/deductreversal/">DeductReversal</a> – Reverse a deduct that was previously requested on a wallet</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/loadadjustment/">LoadAdjustment</a> – Adjust a previous transaction, load a wallet</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/loadauth/">LoadAuth</a> – Request to pre-load in case of refund request or a payment request</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/loadauthreversal/">LoadAuthReversal</a> – Request to reverse the pre-load requested in LoadAuth</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/loadreversal/">LoadReversal</a> – Reverse a load that was previously requested on a wallet</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/mexicaninstallmentsettled/">MexicanInstallmentSettled</a> – Notifies that a Mexican installment transaction has been settled.</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/stop/">Stop</a> – Notification that a card was stopped</li>
<li><a href="https://developer.sprint.paymentology.com/companion-api/api-reference/remote/validatepin/">ValidatePIN</a> – Validate the PIN</li>
</ul>
