---
title: Client Card Program
deprecated: false
hidden: false
metadata:
  robots: index
original_path: get-started
---
<p><span style="font-weight: 400;">On the Paymentology Sprint platform, we use an internal Client Management System to manage the various settings associated with clients’ card programs. This software allows Client Executives, who are responsible for clients’ accounts, to set up configurations that relate to the products we sell to our clients. </span></p>
<p><span style="font-weight: 400;">It’s how we track the various settings pertaining to how the stated card program works so that we can provide a seamless client experience.</span></p>
<p><span style="font-weight: 400;">The Client Executives use the information that clients provide on the Client Product Checklist form to select their appropriate card schemes, products and card program features. </span></p>
<p><span style="font-weight: 400;">These are some possible card settings:</span></p>
<ul>
<li><b>The BIN</b><span style="font-weight: 400;"><br />
</span><span style="font-weight: 400;"><span style="font-weight: 400;">This is the Bank Identification Number, which is the initial four to six digits that appear on a card number. BIN is used to identify the institution issuing the card.</span></span></li>
<li aria-level="1"><b>The currency</b><b><br />
</b><span style="font-weight: 400;">This is the currency that transactions will be processed in. </span></li>
</ul>
<ul>
<li aria-level="1"><b>The product</b><b><br />
</b><span style="font-weight: 400;">This is the Paymentology Sprint product that is being used, such as Companion API or Card API.</span></li>
</ul>
<ul>
<li aria-level="1"><b>PIN configuration</b><b><br />
</b><span style="font-weight: 400;">This configures cards to be created with a PIN and provides PIN management functions. </span></li>
</ul>
<ul>
<li aria-level="1"><b>Countries where the card can be used</b><b><br />
</b><span style="font-weight: 400;">This is a list of countries where the card can be used to make transactions. </span></li>
</ul>
<ul>
<li aria-level="1"><b>Expiry settings</b><b><br />
</b><span style="font-weight: 400;">This is the card expiry date and other expiry configurations, such as re-issuing of an expired card. </span></li>
</ul>
<ul>
<li aria-level="1"><b>Reports</b><b><br />
</b><span style="font-weight: 400;">This enables the Paymentology Sprint reports that a client can download. For example, a mark-off file can include all the settings under that client. </span></li>
</ul>
<ul>
<li aria-level="1"><b>Limits</b><b><br />
</b><span style="font-weight: 400;">This defines the maximum load allowed on a card as well as other velocity checks. </span></li>
</ul>
<ul>
<li aria-level="1"><b>KLV Fields</b><b><br />
</b><span style="font-weight: 400;">This selects the KLV data that can be sent to the client. Read more about </span><a href="https://developer.sprint.paymentology.com/companion-api/klv-lookup/"><span style="font-weight: 400;">KLV data here</span></a><span style="font-weight: 400;"><span style="font-weight: 400;">.</span></span></li>
<li aria-level="1"><b>Security permissions<br />
</b>This allows for blacklisting and setting merchant group permissions.</li>
</ul>



\{/* spacing: desktop=20, mobile=10 */\}


<p><span style="font-weight: 400;">Whenever a transaction is undertaken for a card, all its associated settings are run through the Client Management System to determine their efficacy. For example, the system establishes whether it’s a Card or Companion model, if it’s 3DS or tokenization enabled, or its fees setup. </span></p>
<p> </p>
<p><span style="font-weight: 400;">Here is an illustration that shows how Paymentology manages clients’ cards programs on the Sprint platform:</span></p>
<p> </p>
<p><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-2346" src="https://developer.sprint.paymentology.com/wp-content/uploads/2021/09/Campaigns.png" alt="Card program management" width="1280" height="720" srcset="https://developer.sprint.paymentology.com/wp-content/uploads/2021/09/Campaigns.png 1280w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/09/Campaigns-300x169.png 300w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/09/Campaigns-1024x576.png 1024w, https://developer.sprint.paymentology.com/wp-content/uploads/2021/09/Campaigns-768x432.png 768w" sizes="auto, (max-width: 1280px) 100vw, 1280px" /></p>
<p> </p>
<p> </p>
<p><span style="font-weight: 400;">Let’s explain how it works:</span></p>
<ul>
<li><b>Client</b><span style="font-weight: 400;"><br />
</span><span style="font-weight: 400;">This is the entity that signs a contract with Paymentology to use its services and issue cards to customers. A Client Executive creates a client on the Client Management System. A client can have multiple settings linked to it. </span></li>
<li aria-level="1"><b>Program</b><b><br />
</b><span style="font-weight: 400;">These are records that define the parameters of the product that Paymentology has sold to the client. </span></li>
</ul>
<p> </p>
<p><span style="font-weight: 400;">A client can have more than 1 program linked to them and these will be managed accordingly:</span></p>
<ul>
<li><b>Multiple settings—</b><span style="font-weight: 400;">these are used for tracking different product types, such as virtual cards, physical cards and Digital First cards. They can be set up with different merchants (or partners), multiple VISA SREs’ and multiple BINs (one BIN per setting). The settings can also vary from one card to another, such as different spend limits, different MCCs and multiple reports per setting. They are applied for medium to large clients. These settings are billed individually per setting. </span></li>
<li aria-level="1"><b>Single settings—</b><span style="font-weight: 400;">these are used to manage single card programs, such as one BIN, one VISA SRE, for small to medium clients. They are also billed individually per setting. </span></li>
</ul>
<p> </p>
