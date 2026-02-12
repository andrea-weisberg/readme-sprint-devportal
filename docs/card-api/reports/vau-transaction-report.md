---
title: VAU transaction report
deprecated: false
hidden: false
metadata:
  robots: index
---
<p>The purpose of this report is to send to the client the transactions that are still being made to a certain card that was already sent to VISA via the VAU file.</p>
<p data-renderer-start-pos="241">So for example if a card was sent to VISA in a VAU file on the date <span className="date-lozenger-container"><span className="date-node" data-node-type="date" data-timestamp="1694995200000">Sep 18, 2023</span></span> and transactions are still happening after the file was generated the card will be on the report.</p>
<p>The VAU Transaction Report has the following fields:</p>

<ul>
  <li><strong>Wallet Reference</strong> – this is the unique identifier of the wallet (12 character string).</li>
  <li><strong>Merchant name</strong> – this is the name of the merchant where the transaction took place (string).</li>
  <li><strong>Pre Authorisation Date</strong> – date of the pre-authorisation (MM/DD/YYYY HH:MM:SS).</li>
  <li><strong>Vau File System Date</strong> – VAU file generation date (MM/DD/YYYY HH:MM:SS).</li>
  <li><strong>Voucher id</strong> – corresponds to the transaction id associated with the voucher (integer).</li>
  <li><strong>TrackingNumber</strong> – this is the unique identifier linked to the voucher number (15 character string).</li>
  <li><strong>Voucher Number</strong> – the voucher number sent to VISA in the VAU file (16 character string).</li>
  <li><strong>Expiry Date</strong> – the old expiry date sent to VISA in the VAU file (YYMM).</li>
  <li><strong>Service Identifier</strong> – this identifies the type of change that occurred on the card (string).</li>
</ul>

<h2>Report format</h2>

<br />

<table>
  <thead>
    <tr>
      <th align="center">FORMAT</th>
      <th align="center">FILE NAME</th>
      <th align="center">FREQUENCY</th>
      <th align="center">ACCESSIBILITY</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td align="center">CSV</td>

      <td align="center">
        VAUTransactionsReport\[ClientName]\_\[report generation date YYYY-MM-DD].csv
      </td>

      <td align="center">Monthly</td>
      <td align="center">Sent via email</td>
    </tr>
  </tbody>
</table>

<h2>Report time frame</h2>

<br />

<table>
  <thead>
    <tr>
      <th align="center">UTC +2</th>
      <th align="center">UTC +7</th>
      <th align="center">REMARKS</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td align="center">10:00</td>
      <td align="center">15:00</td>

      <td align="center">
        The report is generated at the provided times on the 1st of every month
        and issued to Visa clients via email.
      </td>
    </tr>
  </tbody>
</table>

<h2>Report sample</h2>

<NavyBlock />

<p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2024/02/VAUtransactionsReportClientName_YYYY-MM-DD.csv">VAUtransactionsReportClientName_YYYY-MM-DD.csv</a></p>
