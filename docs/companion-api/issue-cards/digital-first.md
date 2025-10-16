---
title: Digital First
deprecated: false
hidden: false
metadata:
  robots: index
---
<p><strong>Today’s consumers do everything on their mobile phones or online. The Paymentology Sprint Digital First card program allows you to design a simple, secure and flexible financial experience that emulates the digital lifestyle of today’s generation.</strong></p>

<h2>What is Digital First?</h2>
<p><span style={{fontWeight: "400"}}>Digital First is a payment card that stores all the card information electronically in a digital wallet. It’s a revolutionary program that lets cardholders manage their accounts, check their balances, keep track of their transactions and undertake other tasks—all within a digital environment.</span></p>

<h2>How Does it Work?</h2>
<p><span style={{fontWeight: "400"}}>The Digital First card works just like a normal card—but it can do a lot more. It modernizes the process of issuing cards by eliminating the need for plastic cards. This type of card is virtual, only existing in digital wallets.</span></p>
<p><span style={{fontWeight: "400"}}>The card’s credentials, such as account number (PAN), cardholder’s name, CVC2, expiration date and customer service information, are securely stored electronically, and not on plastic. Digital First cards can be issued for credit cards, debit cards and prepaid cards. </span></p>
<p><span style={{fontWeight: "400"}}>Although the Digital First cards are primarily used virtually for digital payments, customers can request plastic cards. However, the plastic version looks different from what we’re used to. They are designed to reinforce a digital-first relationship with consumers. </span></p>
<p><span style={{fontWeight: "400"}}>The Digital First plastic cards do not have the customer’s account number, CVC2, expiration date and customer service information. The cardholder’s name is required, but it can be replaced with its shorter version. Those missing details are stored on the cardholder’s digital wallet apps. The general term for a card like this is a numberless card.</span></p>
<p><span style={{fontWeight: "400"}}>Numberless cards improve security. They lower the risk of personal information loss when cards fall into the wrong hands.</span></p>

<h2>Capabilities of Paymentology Sprint’s Digital First Card</h2>
<p><span style={{fontWeight: "400"}}>Paymentology Sprint’s Digital First card program is built to provide an optimal, convenient and secure consumer experience. </span></p>
<p><span style={{fontWeight: "400"}}>These are the capabilities of the program. </span></p>
<p> </p>
<h3>1. Instant issuance</h3>
<p><span style={{fontWeight: "400"}}>Once consumers apply online, and their application is approved, they’ll be instantly issued with a digital PAN. They can then immediately access their account credentials and start making purchases online, in-app or at POS terminals via digital wallet offerings. The cardholder may also request a physical-optional card with no numbers printed on it.</span></p>
<p> </p>
<h3>2. Intuitive card management</h3>
<p><span style={{fontWeight: "400"}}>The Digital First card provides a simple and easy way for cardholders to manage their payment credentials digitally. Cardholders can complete various card management tasks directly on the UI. For example, they can quickly access card details, update PIN, check balances, set alerts, report an urgent issue, review transaction history and more.</span></p>
<p> </p>
<h3>3. Tokenization</h3>
<p><span style={{fontWeight: "400"}}><a href="https://developer.sprint.paymentology.com/companion-api/tokenization2/">Tokenization</a> is the process of substituting the card’s sensitive data, such as an account number, with non-sensitive, surrogate data, called a token. The PAN is usually replaced with a unique string of numbers that acts as a secure reference to the card.</span></p>
<p><span style={{fontWeight: "400"}}>Paymentology Sprint’s existing integration with MDES (Mastercard Digital Enablement Service) and <a href="https://developer.sprint.paymentology.com/companion-api/tokenization2/visa-token-provisioning/">VTS</a> (Visa Token Service), both of which offer the infrastructure for generating and managing tokens, allows for instant tokenization of the Digital First cards once enrolment is complete.</span></p>
<p><span style={{fontWeight: "400"}}>Paymentology has also partnered with Upaid Systems Ltd, a provider of centralized mobile payment processing platforms, to provide an MCBP (Mastercard Cloud-Based Payments) SDK for markets with no XPay presence. This allows customers to make the most of Paymentology Sprint’s tokenization technology. Customers can also manage tokens using Paymentology Sprint’s flexible APIs.</span></p>
<p> </p>
<h3>4. Speed and flexibility</h3>
<p><span style={{fontWeight: "400"}}>Paymentology Sprint’s Digital First card program offers the following benefits:</span></p>
<ul>
<li style={{fontWeight: "400"}} aria-level="1"><span style={{fontWeight: "400"}}>6 to 8 weeks to get a VCN BIN live </span></li>
<li style={{fontWeight: "400"}} aria-level="1"><span style={{fontWeight: "400"}}>4 weeks to put MDES/VTS live </span></li>
<li style={{fontWeight: "400"}} aria-level="1"><span style={{fontWeight: "400"}}>6 weeks for the physical production of a Digital First plastic card</span></li>
</ul>

<h2>How to Issue a Digital First Card</h2>
<p><span style={{fontWeight: "400"}}>Digital First cards are issued just like virtual cards. You can use the Companion API to create a Virtual Card Number (VCN), which you can link to the unique customer reference number, as described </span><a href="https://developer.sprint.paymentology.com/companion-api/issue-cards/"><span style={{fontWeight: "400"}}>here</span></a><span style={{fontWeight: "400"}}>. </span></p>
<p><span style={{fontWeight: "400"}}>To print it later, you can follow the steps below:</span></p>
<ul>
<li style={{fontWeight: "400"}} aria-level="1"><b>step 1:</b>
<ul>
<li style={{fontWeight: "400"}} aria-level="1"><strong>Option 1:</strong> <a href="https://developer.sprint.paymentology.com/printlinkedcard/"><span style={{fontWeight: "400"}}>PrintLinkedCard</span></a><span style={{fontWeight: "400"}}>— Use this option if you want the existing Digital First cards to be printed.</span> <strong>OR</strong></li>
<li style={{fontWeight: "400"}} aria-level="1"><strong>Option 2:</strong> <a href="https://developer.sprint.paymentology.com/companion-api/api-reference/local-api/printlinkedcardwithpinblock/"><span style={{fontWeight: "400"}}>PrintLinkedCardWithPINBlock</span></a><span style={{fontWeight: "400"}}>—Use this option if you want the existing Digital First cards to be printed with PIN block.</span></li>
</ul>
</li>
<li style={{fontWeight: "400"}} aria-level="1"><b>step 2:</b> <a href="https://developer.sprint.paymentology.com/togglevoucherfeature/"><span style={{fontWeight: "400"}}>ToggleVoucherFeature</span></a><span style={{fontWeight: "400"}}>— Use this when you want the printed Digital First cards to be used at POS terminals.</span></li>
</ul>

<p><strong>This is an example of a Digital First card powered by Paymentology Sprint for our client Grab in Asia</strong></p>
<p>**Grab-numberless-card.jpeg IMAGE GOES HERE.**</p>
<p><em>Image credit: Grab</em></p>
