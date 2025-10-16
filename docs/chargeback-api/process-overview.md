---
title: Process overview
deprecated: false
hidden: false
metadata:
  robots: index
original_path: chargeback-api
---
<h2>Breakdown of the chargebacks process with Chargeback API</h2>
<p>The Paymentology dispute resolution cycle facilitates the whole process of reversing payments to cardholders. Card transaction disputes usually start when a cardholder or an issuer identifies suspicious, fraudulent, or erroneous charges on accounts.<br />
Issuers and acquirers then follow a process to attempt to resolve the dispute. In the case of Mastercard, the two parties use the Mastercom platform to create and manage disputes throughout their lifecycle, expedite the dispute resolution process, and ensure satisfactory handling of the claims.</p>



\{/* spacing: desktop=20, mobile=10 */\}


\{/* unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21\}},"text":"<p>All chargebacks initiated will be processed using Mastercom Version 6.</p>\n"}]} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h2>Typical dispute resolution cycle steps:</h2>



{/* unsupported_acf_block: columns_with_icons_and_text {"acf_fc_layout":"columns_with_icons_and_text","title":"","block_variant":"Variant 1","columns":[{"column_width":"1/3","icon":false,"title":"","text":"<h1><a href=\"#step 1\">Step 1: First chargeback</a></h1>\n","link":""},{"column_width":"1/3","icon":false,"title":"","text":"<h1><a href=\"#step 2\">Step 2: Collaboration phase</a></h1>\n","link":""},{"column_width":"1/3","icon":false,"title":"","text":"<h1><a href=\"#step 3\">Step 3: Second presentment</a></h1>\n","link":""},{"column_width":"1/3","icon":false,"title":"","text":"<h1><a href=\"#step 4\">Step 4: Pre-arbitration case</a></h1>\n","link":""},{"column_width":"1/3","icon":false,"title":"","text":"<h1><a href=\"#step 5\">Step 5: Arbitration case</a></h1>\n","link":""}]} */}


<p><img loading="lazy" decoding="async" src="https://developer.sprint.paymentology.com/wp-content/uploads/2024/02/Diagram-for-Sprint-Developer-Porta_Lightmode-2.png" alt="Chargeback process flow" width="7245" height="4076" class="alignleft size-full wp-image-4320" srcset="https://developer.sprint.paymentology.com/wp-content/uploads/2024/02/Diagram-for-Sprint-Developer-Porta_Lightmode-2.png 7245w, https://developer.sprint.paymentology.com/wp-content/uploads/2024/02/Diagram-for-Sprint-Developer-Porta_Lightmode-2-300x169.png 300w, https://developer.sprint.paymentology.com/wp-content/uploads/2024/02/Diagram-for-Sprint-Developer-Porta_Lightmode-2-1024x576.png 1024w, https://developer.sprint.paymentology.com/wp-content/uploads/2024/02/Diagram-for-Sprint-Developer-Porta_Lightmode-2-768x432.png 768w, https://developer.sprint.paymentology.com/wp-content/uploads/2024/02/Diagram-for-Sprint-Developer-Porta_Lightmode-2-1536x864.png 1536w, https://developer.sprint.paymentology.com/wp-content/uploads/2024/02/Diagram-for-Sprint-Developer-Porta_Lightmode-2-2048x1152.png 2048w" sizes="auto, (max-width: 7245px) 100vw, 7245px" /></p>



<p>As part of the claim resolution process:</p>
<ul>
<li>Paymentology provides a Chargeback API that allows clients to submit the required data for making the first chargeback.</li>
<li>Paymentology handles all chargebacks that move into second presentment, pre-arbitration, and arbitration stages.</li>
<li>Paymentology provides an API that allows clients to submit the required data for pre-arbitration case filings.</li>
<li>Paymentology allows clients to track the status of each phase of the dispute resolution cycle. We also provide up-to-date reports about the outcome of each step.</li>
</ul>



\{/* spacing: desktop=20, mobile=10 */\}


<h2>Let’s take a look at the steps in more detail</h2>



\{/* unsupported_acf_block: info_block {"acf_fc_layout":"info_block","layout":"Icon","info_repeater":[{"tag_text":"","icon":{"ID":213,"id":213,"title":"icon-secure-card3","filename":"icon-secure-card3.png","filesize":303,"url":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","link":"https://developer.sprint.paymentology.com/card-api/issue-card/icon-secure-card3/","alt":"","author":"1","description":"","caption":"","name":"icon-secure-card3","status":"inherit","uploaded_to":204,"date":"2020-04-02 16:39:05","modified":"2020-04-02 16:39:05","menu_order":0,"mime_type":"image/png","type":"image","subtype":"png","icon":"https://developer.sprint.paymentology.com/wp-includes/images/media/default.png","width":21,"height":21,"sizes":{"thumbnail":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","thumbnail-width":21,"thumbnail-height":21,"medium":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium-width":21,"medium-height":21,"medium_large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","medium_large-width":21,"medium_large-height":21,"large":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","large-width":21,"large-height":21,"1536x1536":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","1536x1536-width":21,"1536x1536-height":21,"2048x2048":"https://developer.sprint.paymentology.com/wp-content/uploads/2020/04/icon-secure-card3.png","2048x2048-width":21,"2048x2048-height":21\}},"text":"<p>After every step, the issuer or acquirer can opt to close the dispute. If not, the matter will eventually be escalated to Mastercard to issue a ruling.</p>\n"}]} */}


\{/* spacing: desktop=20, mobile=10 */\}


<h3><a id="step 1"></a>Step 1: First chargeback</h3>
<p>If we deem the claim to be valid, we can make the first chargeback, transferring the disputed funds from the acquirer to us.<br />
We then communicate to the acquirer about the chargeback by giving a chargeback reason code as well as supportive data.<br />
The chargeback must be for a lesser transaction amount or the entire transaction amount—it cannot be higher than the entire amount.<br />
To successfully complete this step, we provide a Chargeback API that allows you to send us the following information:</p>



\{/* unsupported_acf_block: table_block {"acf_fc_layout":"table_block","table_caption":"","table":{"use_header":true,"header":[{"c":""\},\{"c":""\}],"caption":false,"body":[[\{"c":"Tracking number"\},\{"c":"trackingNumber"\}],[\{"c":"Transaction ID"\},\{"c":"transactionId"\}],[\{"c":"Auth number (optional)"\},\{"c":"authnumber"\}],[\{"c":"System date"\},\{"c":"systemDate"\}],[\{"c":"Settlement amount"\},\{"c":"settlementAmount"\}],[\{"c":"Chargeback amount"\},\{"c":"chargebackAmount"\}],[\{"c":"Reason code"\},\{"c":"reasonCode"\}],[\{"c":"Supporting document"\},\{"c":"supportingDocument"\}]]}} */}


<h4>Payload example</h4>

```json
{
    "trackingNumber": "tRaCkInGnUmBeR",
    "transactionId": "tRaNsAcTiOnId",
    "authnumber": "AuthNumber",
    "systemDate": "2021-08-24 00:00:00",
    "settlementAmount": 402.76,
    "chargebackAmount": 5.74,
    "reasonCode": "4834",
    "supportingDocument": "BASE64_ENCODED_FILE_HERE"
}

```




{/* spacing: desktop=20, mobile=10 */}


<h3><a id="step 2"></a>Step 2: Collaboration phase</h3>
<p>Issuer-initiated chargebacks remain in a pending status (no more than 72 hours) on issuers’ behalf to allow merchants to respond and resolve the inquiry.<br />
In this phase, the acquirer can reject the first chargeback and refund the disputed amount. This closes the dispute and prevents them from going through the chargeback process.<br />
If the acquirer rejects the first chargeback, we will get a notification of rejection and a refund should be processed by the acquirer. If they don’t reject it, the chargeback is then processed as normal to which the acquirer can then dispute if they disagree by making a second presentment.</p>



{/* spacing: desktop=20, mobile=10 */}


<h3><a id="step 3"></a>Step 3: Second presentment</h3>
<p>If the acquirer is dissatisfied with the chargeback reason, they can create a second presentment that gives their side of the story.<br />
This step transfers the money from the issuer to the acquirer. The second presentment must be for a lesser chargeback amount or the entire chargeback amount. It cannot be higher than the entire amount.<br />
After receiving the second presentment, Paymentology will notify the client and present the documents for the case.<br />
The client will then decide the next course of action – either to accept the second presentment and close the dispute or continue with the dispute.</p>



{/* spacing: desktop=20, mobile=10 */}


<h3><a id="step 4"></a>Step 4: Pre-arbitration case</h3>
<p>If we are dissatisfied with the second presentment reason, we can make a second chargeback, which is referred to as an pre-arbitration case.<br />
Paymentology provides an API that allows clients to submit the required data for pre-arbitration case filings.<br />
The pre-arbitration case must be for a lesser second presentment amount or the entire amount—it cannot be higher than the entire amount.</p>



{/* spacing: desktop=20, mobile=10 */}


<h3><a id="step 5"></a>Step 5: Arbitration case</h3>
<p>The arbitration case filing step escalates the issue to Mastercard. Mastercard will then examine the evidence provided by both the issuer and the acquirer to determine the party that carries the day.</p>
