---
title: UpdateBearerExtended
deprecated: false
hidden: false
metadata:
  robots: index
---
<!-- MIGRATION_METADATA
Migrated-From: https://developer.sprint.paymentology.com/profile-api-reference/updatebearerextended/
Source-Slug: updatebearerextended
Migrated-On: 2026-02-12T21:13:24+00:00
Migrated-By: wp-readme-migration
-->

Update the cardholder details.

This is an extended API to update additional details like address and employment details. Use [UpdateBearer](updatebearer-1) in case you only need to update details like name and contact details.


#### Path parameters

| Parameter | type | Limits | required | Description |
| --- | --- | --- | --- | --- |
| terminalID | String | 10 characters | ✓ | The Paymentology issued terminal ID of the terminal requesting the transaction. |
| profileNumber | String | 1-20 characters | ✓ | Profile number linked with this card. |
| cardidentifier | String | 1-20 characters | ✓ | The tracking number of the specified card. |
| Title | String | 1-10 characters | ✓ | The Title of the cardholder. |
| Initials | String | 1-15 characters | ✓ | The Initials of the cardholder. |
| birthdate | Date | 1-20 characters | ✓ | Birthday date of the cardholder, in the format yyyMMdd |
| Gender | String | 1-10 characters | ✓ | The gender of the Cardholder |
| identificationTypeCode | String | 1-20 characters | ✓ | The card number, sequence number or tracking number of the specified card.<br><br>**Permissible Values:**<br><br>South African ID number – 1<br><br>Foreign ID number – 2<br><br>Foreign Passport number – 3<br><br>Enterprise Registration number – 4<br><br>Foreign Enterprise registration number – 5<br><br>ISIN number – 6<br><br>South African trust registration number – 7<br><br>Foreign trust registration number – 8<br><br>Internal identification number – 9<br><br>Temp Res Permit – 10<br><br>Temporary ID number – 11<br><br>RSA Passport – 12<br><br>Other – 13<br><br>Asylum Seeker Permit Number – 14<br><br>Work Permit Number – 15<br><br>Refugee Permit Number – 16<br><br>Birth Certificates – 17<br><br>Drivers License – 18 |
| IdIssuedDate | Date | 1-20 characters | ✓ | Date the ID was issued to the cardholder, in the format yyyyMMdd |
| IdExpiryDate | Date | 1-20 characters | ✓ | Expiry date of the ID, in the format yyyyMMdd |
| IdIssuedCountry | String | 1-3 characters | ✓ | The country the ID was issued in. The three digit country code as specified [here](https://www.iban.com/country-codes). |
| ResidenceIndicator | Integer | 2 digits | ✓ | Indicator value for resident type of cardholder.<br><br>**Permissible Values:**<br><br>Resident –  01<br><br>Temporary Resident – 02<br><br>NON Resident – 03 |
| EmploymentStatus | Integer | 2 digits | ✓ | Numeric mapped value to indicate the type of employment of cardholder.<br><br>**Permissible Values:**<br><br>Not Employed – 01<br><br>Employed – 02<br><br>Self Employed – 03<br><br>Professional – 04<br><br>Retired – 05<br><br>Student – 07<br><br>Others – 08<br><br>Pensioned- 09<br><br>Temporary Employed – 10<br><br>Freelance – 11 |
| HomeLanguage | Integer | 2 digits | ✓ | Numeric mapped value to indicate the home language of cardholder.<br><br>**Permissible Values:**<br><br>Afrikaans – 01<br><br>Ndebele – 02<br><br>North Sotho – 03<br><br>South Sotho – 04<br><br>Swazi – 05<br><br>Tsonga – 06<br><br>Tswana – 07<br><br>Venda – 08<br><br>Xhosa – 09<br><br>Zulu – 10<br><br>English – 11<br><br>Other – 12<br><br>Sepedi – 13 |
| EstimatedMonthlyTurnover | Integer | 2 digits | ✓ | The numeric value mapped against Estimated monthly turnover of the cardholder.<br><br>**Permissible Values:**<br><br>None – 01<br><br>Unknown – 02<br><br>R 0 to R 4,999 – 03<br><br>R 5,000 to R 9,999 – 04<br><br>R 10,000 to R 49,999 – 05<br><br>R 50,000 or more – 06 |
| ExpectedSourceOfFunds | Integer | 2 digits | ✓ | The numeric value mapped against the expected source of funds of the cardholder.<br><br>**Permissible Values:**<br><br>Alimony – 01<br><br>Bonuses – 02<br><br>Child Support – 03<br><br>Commisions – 04<br><br>Dividend/Interest – 05<br><br>Pension – 06<br><br>Rental Income – 07<br><br>Salary – 08<br><br>Unknown – 09<br><br>Loan – 10<br><br>Donations – 11<br><br>None – 12<br><br>Business Activities – 13<br><br>Others – 14 |
| EstimatedCashTransactionValue | Integer | 2 digits | ✓ | The numeric value mapped against the Estimated Cash transaction value of the cardholder.<br><br>**Permissible Values:**<br><br>None – 01<br><br>Unknown – 02<br><br>R 0 to R 4,999 – 03<br><br>R 5,000 to R 9,999 – 04<br><br>R 10,000 to R 49,999 – 05<br><br>R 50,000 or more – 06 |
| ExpectedUseOfChannel | Integer | 2 digits | ✓ | The numeric value mapped against the expected use of channel of the cardholder.<br><br>**Permissible Values:**<br><br>Suite – 01<br><br>ATM – 02<br><br>Cell Phone – 03<br><br>Internet/EFT – 04<br><br>Combination – 05 |
| expectedForeignTransaction | Integer | 2 digits | ✓ | The numeric value mapped against the expected foreign transaction value of the cardholder.<br><br>**Permissible Values:**<br><br>None – 01<br><br>Unknown – 02<br><br>R 0 to R 4,999 – 03<br><br>R 5,000 to R 9,999 – 04<br><br>R 10,000 to R 49,999 – 05<br><br>R 50,000 or more – 06 |
| Nationality | String | 1-10 characters | ✓ | Nationality of the cardholder. The three digit country code as specified [here](https://www.iban.com/country-codes). |
| IndustryId | Integer |  | ✓ | Numeric mapped value for the type of Industry the cardholder is employed in.<br><br>**Industry IDs are present in the downloadable document below:**<br><br>[IndustryID_PermissibleValues](../../assets/IndustryID_PermissibleValues.pdf) |
| IndustryHighLevel | Integer | 2 digits | ✓ | The numeric value mapped against the high-level industry cardholder is involved in.<br><br>**Permissible Values:**<br><br>Agriculture, Hunting, Forestry and Fishing – 01<br><br>Mining and Quarrying – 02<br><br>Manufacturing – 03<br><br>Electricity, Gas and Water Supply – 04<br><br>Construction – 05<br><br>Wholesale and Retail Trade – 06<br><br>Transport, Storage and Communication – 07<br><br>Financial, Insurance, Real Estate and Business – 08<br><br>Community, Social and Personal – 09<br><br>Private Exterritorial Organisations – 10 |
| StreetNumber | String | 1-10 characters | ✓ | Street number of the cardholder. |
| StreetName | String | 1-100 characters | ✓ | Street name of the cardholder. |
| CityTown | String | 1-50 characters | ✓ | City or Town name of the cardholder. |
| Province | String | 1-20 characters | ✓ | Province name of the cardholder. |
| Country | String | 1-50 characters | ✓ | Country name of the cardholder. |
| AddressPostalCode | String | 1-9 characters | ✓ | Postal code of the cardholder. |
| SuburbDistrict | String | 1-50 characters | ✓ | Suburb or Distriict name of the cardholder. |
| ResidentialStatusCode | String | 1-255 characters | ✓ | The numeric value mpped against residential status of the cardholder.<br><br>**Permissible Values:**<br><br>Owner – 01<br><br>Tenant – 02<br><br>Owned by spouse – 03<br><br>Living with parents – 04 |
| TransactionID | String | 1-255 characters | ✓ | Transaction ID number generated by the calling client. |
| TransactionDate | Date |  | ✓ | Transaction date generated by the calling client. |
| Checksum | String |  | ✓ | HMAC-SHA1 hashed signature of the concatenated method name with all argument values using the terminal password as private key. |


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
```


#### Response schema

| Parameter | type | Description |
| --- | --- | --- |
| CardIdentifier | String | Echo of the incoming value.<br><br>(1-12 characters) |
| ProfileNumber | String | Echo of the incoming value.<br><br>(1-12 characters) |
| TerminalID | String | Echo of the incoming value.<br><br>(1-12 characters) |
| transactionDate | Date | Transaction date generated by the calling client. |
| serverTransactionID | String | Transaction ID generated by Paymentology.<br><br>(1-255 characters) |
| resultCode | Integer | Status code indicating transaction result. |
| resultText | String | Text indicating transaction result. |


```xml
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
