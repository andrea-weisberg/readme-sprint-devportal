---
title: UpdateBearerExtended
deprecated: false
hidden: false
metadata:
  robots: index
---
<p>Update the cardholder details.</p>
<p>This is an extended API to update additional details like address and employment details. Use <a href="https://developer.sprint.paymentology.com/profile-api-reference/updatebearer/">UpdateBearer</a> in case you only need to update details like name and contact details.</p>

#### Path parameters

| Parameter | Type | Limits | Required | Description |
|---|---|---|:--:|---|
| terminalID | String | 10 characters | ✓ | <p>The Paymentology issued terminal ID of the terminal requesting the transaction.</p> |
| profileNumber | String | 1-20 characters | ✓ | <p>Profile number linked with this card.</p> |
| cardidentifier | String | 1-20 characters | ✓ | <p>The tracking number of the specified card.</p> |
| Title | String | 1-10 characters | ✓ | <p>The Title of the cardholder.</p> |
| Initials | String | 1-15 characters | ✓ | <p>The Initials of the cardholder.</p> |
| birthdate | Date | 1-20 characters | ✓ | <p>Birthday date of the cardholder, in the format yyyMMdd</p> |
| Gender | String | 1-10 characters | ✓ | <p>The gender of the Cardholder</p> |
| identificationTypeCode | String | 1-20 characters | ✓ | <p>The card number, sequence number or tracking number of the specified card.</p> <p><strong>Permissible Values:</strong></p> <p>South African ID number – 1<br /> Foreign ID number – 2<br /> Foreign Passport number – 3<br /> Enterprise Registration number – 4<br /> Foreign Enterprise registration number – 5<br /> ISIN number – 6<br /> South African trust registration number – 7<br /> Foreign trust registration number – 8<br /> Internal identification number – 9<br /> Temp Res Permit – 10<br /> Temporary ID number – 11<br /> RSA Passport – 12<br /> Other – 13<br /> Asylum Seeker Permit Number – 14<br /> Work Permit Number – 15<br /> Refugee Permit Number – 16<br /> Birth Certificates – 17<br /> Drivers License – 18</p> |
| IdIssuedDate | Date | 1-20 characters | ✓ | <p>Date the ID was issued to the cardholder, in the format yyyyMMdd</p> |
| IdExpiryDate | Date | 1-20 characters | ✓ | <p>Expiry date of the ID, in the format yyyyMMdd</p> |
| IdIssuedCountry | String | 1-3 characters | ✓ | <p>The country the ID was issued in. The three digit country code as specified <a href="https://www.iban.com/country-codes">here</a>.</p> |
| ResidenceIndicator | Integer | 2 digits | ✓ | <p>Indicator value for resident type of cardholder.</p> <p><strong>Permissible Values:</strong></p> <p>Resident –  01<br /> Temporary Resident – 02<br /> NON Resident – 03</p> |
| EmploymentStatus | Integer | 2 digits | ✓ | <p>Numeric mapped value to indicate the type of employment of cardholder.</p> <p><strong>Permissible Values:</strong></p> <p>Not Employed – 01<br /> Employed – 02<br /> Self Employed – 03<br /> Professional – 04<br /> Retired – 05<br /> Student – 07<br /> Others – 08<br /> Pensioned- 09<br /> Temporary Employed – 10<br /> Freelance – 11</p> |
| HomeLanguage | Integer | 2 digits | ✓ | <p>Numeric mapped value to indicate the home language of cardholder.</p> <p><strong>Permissible Values:</strong></p> <p>Afrikaans – 01<br /> Ndebele – 02<br /> North Sotho – 03<br /> South Sotho – 04<br /> Swazi – 05<br /> Tsonga – 06<br /> Tswana – 07<br /> Venda – 08<br /> Xhosa – 09<br /> Zulu – 10<br /> English – 11<br /> Other – 12<br /> Sepedi – 13</p> |
| EstimatedMonthlyTurnover | Integer | 2 digits | ✓ | <p>The numeric value mapped against Estimated monthly turnover of the cardholder.</p> <p><strong>Permissible Values:</strong></p> <p>None – 01<br /> Unknown – 02<br /> R 0 to R 4,999 – 03<br /> R 5,000 to R 9,999 – 04<br /> R 10,000 to R 49,999 – 05<br /> R 50,000 or more – 06</p> |
| ExpectedSourceOfFunds | Integer | 2 digits | ✓ | <p>The numeric value mapped against the expected source of funds of the cardholder.</p> <p><strong>Permissible Values:</strong></p> <p>Alimony – 01<br /> Bonuses – 02<br /> Child Support – 03<br /> Commisions – 04<br /> Dividend/Interest – 05<br /> Pension – 06<br /> Rental Income – 07<br /> Salary – 08<br /> Unknown – 09<br /> Loan – 10<br /> Donations – 11<br /> None – 12<br /> Business Activities – 13<br /> Others – 14</p> |
| EstimatedCashTransactionValue | Integer | 2 digits | ✓ | <p>The numeric value mapped against the Estimated Cash transaction value of the cardholder.</p> <p><strong>Permissible Values:</strong></p> <p>None – 01<br /> Unknown – 02<br /> R 0 to R 4,999 – 03<br /> R 5,000 to R 9,999 – 04<br /> R 10,000 to R 49,999 – 05<br /> R 50,000 or more – 06</p> |
| ExpectedUseOfChannel | Integer | 2 digits | ✓ | <p>The numeric value mapped against the expected use of channel of the cardholder.</p> <p><strong>Permissible Values:</strong></p> <p>Suite – 01<br /> ATM – 02<br /> Cell Phone – 03<br /> Internet/EFT – 04<br /> Combination – 05</p> |
| expectedForeignTransaction | Integer | 2 digits | ✓ | <p>The numeric value mapped against the expected foreign transaction value of the cardholder.</p> <p><strong>Permissible Values:</strong></p> <p>None – 01<br /> Unknown – 02<br /> R 0 to R 4,999 – 03<br /> R 5,000 to R 9,999 – 04<br /> R 10,000 to R 49,999 – 05<br /> R 50,000 or more – 06</p> |
| Nationality | String | 1-10 characters | ✓ | <p>Nationality of the cardholder. The three digit country code as specified <a href="https://www.iban.com/country-codes">here</a>.</p> |
| IndustryId | Integer |  | ✓ | <p>Numeric mapped value for the type of Industry the cardholder is employed in.</p> <p><strong>Industry IDs are present in the downloadable document below:</strong></p> <p><a href="https://developer.sprint.paymentology.com/wp-content/uploads/2024/07/IndustryID_PermissibleValues.pdf">IndustryID_PermissibleValues</a></p> |
| IndustryHighLevel | Integer | 2 digits | ✓ | <p>The numeric value mapped against the high-level industry cardholder is involved in.</p> <p><strong>Permissible Values:</strong></p> <p>Agriculture, Hunting, Forestry and Fishing – 01<br /> Mining and Quarrying – 02<br /> Manufacturing – 03<br /> Electricity, Gas and Water Supply – 04<br /> Construction – 05<br /> Wholesale and Retail Trade – 06<br /> Transport, Storage and Communication – 07<br /> Financial, Insurance, Real Estate and Business – 08<br /> Community, Social and Personal – 09<br /> Private Exterritorial Organisations – 10</p> |
| StreetNumber | String | 1-10 characters | ✓ | <p>Street number of the cardholder.</p> |
| StreetName | String | 1-100 characters | ✓ | <p>Street name of the cardholder.</p> |
| CityTown | String | 1-50 characters | ✓ | <p>City or Town name of the cardholder.</p> |
| Province | String | 1-20 characters | ✓ | <p>Province name of the cardholder.</p> |
| Country | String | 1-50 characters | ✓ | <p>Country name of the cardholder.</p> |
| AddressPostalCode | String | 1-9 characters | ✓ | <p>Postal code of the cardholder.</p> |
| SuburbDistrict | String | 1-50 characters | ✓ | <p>Suburb or Distriict name of the cardholder.</p> |
| ResidentialStatusCode | String | 1-255 characters | ✓ | <p>The numeric value mpped against residential status of the cardholder.</p> <p><strong>Permissible Values:</strong></p> <p>Owner – 01<br /> Tenant – 02<br /> Owned by spouse – 03<br /> Living with parents – 04</p> |
| TransactionID | String | 1-255 characters | ✓ | <p>Transaction ID number generated by the calling client.</p> |
| TransactionDate | Date |  | ✓ | <p>Transaction date generated by the calling client.</p> |
| Checksum | String |  | ✓ | <p>HMAC-SHA1 hashed signature of the concatenated method name with all argument values using the terminal password as private key.</p> |

```xml
<?xml version="1.0"?>
<methodCall>
  <methodName>UpdateBearerExtended</methodName>
  <params>
    <param>
      <value>
        <string>0988963840</string>
      </value>
    </param>
    <param>
      <value>
        <string>5790094121</string>
      </value>
    </param>
    <param>
      <value>
        <string>75163739087896</string>
      </value>
    </param>
    <param>
      <value>
        <string>uTitle</string>
      </value>
    </param>
    <param>
      <value>
        <string>uInitials</string>
      </value>
    </param>
    <param>
      <value>
        <dateTime.iso8601>19991227T03:25:54</dateTime.iso8601>
      </value>
    </param>
    <param>
      <value>
        <string>uGender</string>
      </value>
    </param>
    <param>
      <value>
        <int>01</int>
      </value>
    </param>
    <param>
      <value>
        <dateTime.iso8601>19991227T03:25:54</dateTime.iso8601>
      </value>
    </param>
    <param>
      <value>
        <dateTime.iso8601>20351227T03:25:54</dateTime.iso8601>
      </value>
    </param>
    <param>
      <value>
        <string>uty</string>
      </value>
    </param>
    <param>
      <value>
        <int>22</int>
      </value>
    </param>
    <param>
      <value>
        <int>00</int>
      </value>
    </param>
    <param>
      <value>
        <int>01</int>
      </value>
    </param>
    <param>
      <value>
        <int>02</int>
      </value>
    </param>
    <param>
      <value>
        <int>03</int>
      </value>
    </param>
    <param>
      <value>
        <int>04</int>
      </value>
    </param>
    <param>
      <value>
        <int>05</int>
      </value>
    </param>
    <param>
      <value>
        <int>06</int>
      </value>
    </param>
    <param>
      <value>
        <string>uat</string>
      </value>
    </param>
    <param>
      <value>
        <int>07</int>
      </value>
    </param>
    <param>
      <value>
        <int>08</int>
      </value>
    </param>
    <param>
      <value>
        <string>uStno</string>
      </value>
    </param>
    <param>
      <value>
        <string>uStnam</string>
      </value>
    </param>
    <param>
      <value>
        <string>uot</string>
      </value>
    </param>
    <param>
      <value>
        <string>uProvince</string>
      </value>
    </param>
    <param>
      <value>
        <string>uty</string>
      </value>
    </param>
    <param>
      <value>
        <string>uCode</string>
      </value>
    </param>
    <param>
      <value>
        <string>uSod</string>
      </value>
    </param>
    <param>
      <value>
        <int>09</int>
      </value>
    </param>
    <param>
      <value>
        <string>txnId</string>
      </value>
    </param>
    <param>
      <value>
        <dateTime.iso8601>20240418T03:25:54</dateTime.iso8601>
      </value>
    </param>
    <param>
      <value>
        <string>4A2EEAC72EC2BD539CADCA72E37044A899D16037AA91A9A12CCF315DBDB2DAE5</string>
      </value>
    </param>
  </params>
</methodCall>

```,```xml
<?xml version="1.0" encoding="UTF-8"?>
<methodResponse>
  <params>
    <param>
      <value>
        <struct>
          <member>
            <name>cardIdentifier</name>
            <value>
              <string>751622200000006</string>
            </value>
          </member>
          <member>
            <name>resultCode</name>
            <value>
              <int>1</int>
            </value>
          </member>
          <member>
            <name>terminalID</name>
            <value>
              <string>0058263840</string>
            </value>
          </member>
          <member>
            <name>profileNumber</name>
            <value>
              <string>5792074121</string>
            </value>
          </member>
          <member>
            <name>resultText</name>
            <value>
              <string>Approved</string>
            </value>
          </member>
          <member>
            <name>transactionDate</name>
            <value>
              <dateTime.iso8601>20240418T03:25:54</dateTime.iso8601>
            </value>
          </member>
          <member>
            <name>serverTransactionID</name>
            <value>
              <string>5792074121-4A2EEAC72EC2BD539CADCA72E37044A899D16037AA91A9A12CCF315DBDB2DAE5</string>
            </value>
          </member>
          <member>
            <name>transactionID</name>
            <value>
              <string>txnId</string>
            </value>
          </member>
        </struct>
      </value>
    </param>
  </params>
</methodResponse>

```

<p> </p>

#### Response schema

| Field | Type | Description |
|---|---|---|
| CardIdentifier | String | <p>Echo of the incoming value.<br /> (1-12 characters)</p> |
| ProfileNumber | String | <p>Echo of the incoming value.<br /> (1-12 characters)</p> |
| TerminalID | String | <p>Echo of the incoming value.<br /> (1-12 characters)</p> |
| transactionDate | Date | <p>Transaction date generated by the calling client.</p> |
| serverTransactionID | String | <p>Transaction ID generated by Paymentology.<br /> (1-255 characters)</p> |
| resultCode | Integer | <p>Status code indicating transaction result.</p> |
| resultText | String | <p>Text indicating transaction result.</p> |

```xml
<?xml version="1.0"?>
<methodCall>
  <methodName>UpdateBearerExtended</methodName>
  <params>
    <param>
      <value>
        <string>0988963840</string>
      </value>
    </param>
    <param>
      <value>
        <string>5790094121</string>
      </value>
    </param>
    <param>
      <value>
        <string>75163739087896</string>
      </value>
    </param>
    <param>
      <value>
        <string>uTitle</string>
      </value>
    </param>
    <param>
      <value>
        <string>uInitials</string>
      </value>
    </param>
    <param>
      <value>
        <dateTime.iso8601>19991227T03:25:54</dateTime.iso8601>
      </value>
    </param>
    <param>
      <value>
        <string>uGender</string>
      </value>
    </param>
    <param>
      <value>
        <int>01</int>
      </value>
    </param>
    <param>
      <value>
        <dateTime.iso8601>19991227T03:25:54</dateTime.iso8601>
      </value>
    </param>
    <param>
      <value>
        <dateTime.iso8601>20351227T03:25:54</dateTime.iso8601>
      </value>
    </param>
    <param>
      <value>
        <string>uty</string>
      </value>
    </param>
    <param>
      <value>
        <int>22</int>
      </value>
    </param>
    <param>
      <value>
        <int>00</int>
      </value>
    </param>
    <param>
      <value>
        <int>01</int>
      </value>
    </param>
    <param>
      <value>
        <int>02</int>
      </value>
    </param>
    <param>
      <value>
        <int>03</int>
      </value>
    </param>
    <param>
      <value>
        <int>04</int>
      </value>
    </param>
    <param>
      <value>
        <int>05</int>
      </value>
    </param>
    <param>
      <value>
        <int>06</int>
      </value>
    </param>
    <param>
      <value>
        <string>uat</string>
      </value>
    </param>
    <param>
      <value>
        <int>07</int>
      </value>
    </param>
    <param>
      <value>
        <int>08</int>
      </value>
    </param>
    <param>
      <value>
        <string>uStno</string>
      </value>
    </param>
    <param>
      <value>
        <string>uStnam</string>
      </value>
    </param>
    <param>
      <value>
        <string>uot</string>
      </value>
    </param>
    <param>
      <value>
        <string>uProvince</string>
      </value>
    </param>
    <param>
      <value>
        <string>uty</string>
      </value>
    </param>
    <param>
      <value>
        <string>uCode</string>
      </value>
    </param>
    <param>
      <value>
        <string>uSod</string>
      </value>
    </param>
    <param>
      <value>
        <int>09</int>
      </value>
    </param>
    <param>
      <value>
        <string>txnId</string>
      </value>
    </param>
    <param>
      <value>
        <dateTime.iso8601>20240418T03:25:54</dateTime.iso8601>
      </value>
    </param>
    <param>
      <value>
        <string>4A2EEAC72EC2BD539CADCA72E37044A899D16037AA91A9A12CCF315DBDB2DAE5</string>
      </value>
    </param>
  </params>
</methodCall>

```,```xml
<?xml version="1.0" encoding="UTF-8"?>
<methodResponse>
  <params>
    <param>
      <value>
        <struct>
          <member>
            <name>cardIdentifier</name>
            <value>
              <string>751622200000006</string>
            </value>
          </member>
          <member>
            <name>resultCode</name>
            <value>
              <int>1</int>
            </value>
          </member>
          <member>
            <name>terminalID</name>
            <value>
              <string>0058263840</string>
            </value>
          </member>
          <member>
            <name>profileNumber</name>
            <value>
              <string>5792074121</string>
            </value>
          </member>
          <member>
            <name>resultText</name>
            <value>
              <string>Approved</string>
            </value>
          </member>
          <member>
            <name>transactionDate</name>
            <value>
              <dateTime.iso8601>20240418T03:25:54</dateTime.iso8601>
            </value>
          </member>
          <member>
            <name>serverTransactionID</name>
            <value>
              <string>5792074121-4A2EEAC72EC2BD539CADCA72E37044A899D16037AA91A9A12CCF315DBDB2DAE5</string>
            </value>
          </member>
          <member>
            <name>transactionID</name>
            <value>
              <string>txnId</string>
            </value>
          </member>
        </struct>
      </value>
    </param>
  </params>
</methodResponse>

```

<p> </p>

