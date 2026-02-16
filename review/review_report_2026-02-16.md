# Review Report (v1.0_codex)

**Total completed:** 105

**High risk:** 85 | **Medium:** 20 | **Low:** 0

## Automated Check Findings

### Broken/Missing Links
- `docs/companion-api/api-reference-companion/remote/administrativemessage/administrative-message-values.md`
  - Missing anchor #activationmethods in docs/companion-api/api-reference-companion/remote/administrativemessage/index.md
  - Missing anchor #activation in docs/companion-api/api-reference-companion/remote/administrativemessage/index.md
  - Missing anchor #complete in docs/companion-api/api-reference-companion/remote/administrativemessage/index.md
  - Missing anchor #eventdeleted in docs/companion-api/api-reference-companion/remote/administrativemessage/index.md
  - Missing anchor #deletedfromdevice in docs/companion-api/api-reference-companion/remote/administrativemessage/index.md
  - Missing anchor #stopped in docs/companion-api/api-reference-companion/remote/administrativemessage/index.md
  - Missing anchor #digitized in docs/companion-api/api-reference-companion/remote/administrativemessage/index.md
  - Missing anchor #exception in docs/companion-api/api-reference-companion/remote/administrativemessage/index.md
  - Missing anchor #replacement in docs/companion-api/api-reference-companion/remote/administrativemessage/index.md
- `docs/card-api/api-reference-card/ordercardwithpinblock.md`
  - Missing anchor #pinencryption in docs/card-api/api-reference-card/index.md
- `docs/companion-api/klv-lookup.md`
  - Missing anchor #Deduct in docs/companion-api/api-reference-companion/remote/index.md
  - Missing anchor #DeductAdjustment in docs/companion-api/api-reference-companion/remote/index.md
  - Missing anchor #LoadAuth in docs/companion-api/api-reference-companion/remote/index.md
  - Missing anchor #LoadAdjustment in docs/companion-api/api-reference-companion/remote/index.md
  - Missing anchor #Stop in docs/companion-api/api-reference-companion/remote/index.md
  - Missing anchor #AdministrativeMessage in docs/companion-api/api-reference-companion/remote/index.md
  - Missing anchor #AdministrativeMessage in docs/companion-api/api-reference-companion/remote/index.md
  - Broken link: ../get-started/whats-new
  - Broken link: ../get-started/whats-new
- `docs/documentation/how_payments_work.md`
  - Missing anchor #authorization in docs/companion-api/settlement-and-reconciliation.md
- `docs/card-api/disputes.md`
  - Broken link: ../../assets/Dispute-Resolution-Form-Fraud.docx
  - Broken link: ../../assets/Dispute-Resolution-Form.docx
  - Broken link: ../../assets/Visa-Generic-Dispute-Form.docx
- `docs/profile-api-reference/listalltokens-2.md`
  - Broken link: /
- `docs/card-api/manage-funds-1.md`
  - Broken link: #LoadAuth
- `docs/card-api/reconciliation.md`
  - Broken link: #authorization
  - Broken link: #Settlements
  - Broken link: #Revenue
  - Broken link: #Fraud
- `docs/chargeback-api/process-overview.md`
  - Broken link: #step 1
  - Broken link: #step 2
  - Broken link: #step 3
  - Broken link: #step 4
  - Broken link: #step 5
- `docs/response-codes-2/response-and-action-code-mapping.md`
  - Broken link: /

### Missing Assets
- `docs/card-api/disputes.md`
  - Missing asset: ../../assets/Dispute-Resolution-Form-Fraud.docx
  - Missing asset: ../../assets/Dispute-Resolution-Form.docx
  - Missing asset: ../../assets/Visa-Generic-Dispute-Form.docx
- `docs/profile-api-reference/updatebearerextended.md`
  - Missing asset: ../../assets/IndustryID_PermissibleValues.pdf
- `docs/card-api/reports/daily-negative-balance-report.md`
  - Missing asset: ../../../assets/DailyNegativeBalanceReportOnChargebackQueue_CampaignName_YYYYMMDD.csv
- `docs/card-api/reports/mark-off-file.md`
  - Missing asset: ../../../assets/CampaignName_MarkOffFile_YYYYMMDD.csv
- `docs/card-api/reports/google-pay-monthly-report.md`
  - Missing asset: ../../../assets/CampaignNamegooglepaymonthlyreportMMM-YYYY.csv
- `docs/card-api/reports/blocked-transactions-report.md`
  - Missing asset: ../../../assets/CampaignName-Blocked-Transactions-231015-231022.xls
- `docs/card-api/reports/authorisation-income-report.md`
  - Missing asset: ../../../assets/CampaignName_authorisationincomereport_YYYY_MM_DD.csv
- `docs/card-api/reports/summary-settlement-report-2.md`
  - Missing asset: ../../../assets/Daily_Settlement_Report_ICA_YYYY_MM_DD-1.xls
- `docs/card-api/reports/card-order-report-2.md`
  - Missing asset: ../../../assets/CampaignName_PanDetails_YYYYMMDD-card.csv

## Manual Review Set

### High Risk (85)
- `docs/companion-api/api-reference-companion/remote/administrativemessage/administrative-message-values.md` (source: `administrative-message-values (anchor fix)`)
- `docs/companion-api/api-reference-companion/remote/administrativemessage/index.md` (source: `administrativemessage`)
- `docs/card-api/api-reference-card/ordercardwithpinblock.md` (source: `ordercardwithpinblock`)
- `docs/companion-api/klv-lookup.md` (source: `klv-lookup`)
- `docs/Getting Started/glossary.md` (source: `glossary`)
- `docs/Getting Started/fraud.md` (source: `fraud`)
- `docs/chargeback-api/remote-messaging-api/remote-messaging-api-chargeback-notification.md` (source: `remote-messaging-api-chargeback-notification`)
- `docs/card-api/tokenization/index.md` (source: `tokenization`)
- `docs/documentation/reporting-api-2.md` (source: `reporting-api-2`)
- `docs/documentation/reversedevalueprofile-1.md` (source: `reversedevalueprofile-1`)
- `docs/documentation/how_payments_work.md` (source: `how_payments_work`)
- `docs/card-api/disputes.md` (source: `disputes`)
- `docs/profile-api-reference/ordercard-2.md` (source: `ordercard-2`)
- `docs/profile-api-reference/listalltokens-2.md` (source: `listalltokens-2`)
- `docs/profile-api-reference/checkauthorisation.md` (source: `checkauthorisation`)
- `docs/profile-api-reference/togglevoucherfeature-2.md` (source: `togglevoucherfeature-2`)
- `docs/profile-api-reference/reversevastransferfunds.md` (source: `reversevastransferfunds`)
- `docs/profile-api-reference/updatescheduledstop.md` (source: `updatescheduledstop`)
- `docs/profile-api-reference/statementbydaterange.md` (source: `statementbydaterange`)
- `docs/profile-api-reference/stoptoken-2.md` (source: `stoptoken-2`)
- `docs/profile-api-reference/allocatecard.md` (source: `allocatecard`)
- `docs/profile-api-reference/vastransferfunds.md` (source: `vastransferfunds`)
- `docs/profile-api-reference/cancelscheduledstop.md` (source: `cancelscheduledstop`)
- `docs/card-api/manage-funds-1.md` (source: `manage-funds-1`)
- `docs/profile-api-reference/statement-1.md` (source: `statement-1`)
- `docs/profile-api-reference/calculatetav-2.md` (source: `calculatetav-2`)
- `docs/profile-api-reference/createscheduledstop.md` (source: `createscheduledstop`)
- `docs/profile-api-reference/reversedevalueprofile.md` (source: `reversedevalueprofile`)
- `docs/profile-api-reference/activate.md` (source: `activate`)
- `docs/profile-api-reference/checkload.md` (source: `checkload`)
- `docs/profile-api-reference/changepin-2.md` (source: `changepin-2`)
- `docs/profile-api-reference/transferfunds-1.md` (source: `transferfunds-1`)
- `docs/profile-api-reference/allocateiban.md` (source: `allocateiban`)
- `docs/profile-api-reference/updateallocatedcard.md` (source: `updateallocatedcard`)
- `docs/profile-api-reference/transferlink-2.md` (source: `transferlink-2`)
- `docs/profile-api-reference/status-1.md` (source: `status-1`)
- `docs/profile-api-reference/deletetoken-1.md` (source: `deletetoken-1`)
- `docs/profile-api-reference/resetpin-1.md` (source: `resetpin-1`)
- `docs/profile-api-reference/linkcard-2.md` (source: `linkcard-2`)
- `docs/card-api/reconciliation.md` (source: `reconciliation`)
- `docs/profile-api-reference/unstoptoken-2.md` (source: `unstoptoken-2`)
- `docs/profile-api-reference/updatebearerextended.md` (source: `updatebearerextended`)
- `docs/profile-api-reference/transfertoken-1.md` (source: `transfertoken-1`)
- `docs/profile-api-reference/activatetoken-2.md` (source: `activatetoken-2`)
- `docs/profile-api-reference/register.md` (source: `register`)
- `docs/profile-api-reference/loadcarddeductprofile.md` (source: `loadcarddeductprofile`)
- `docs/profile-api-reference/listtokens-2.md` (source: `listtokens-2`)
- `docs/profile-api-reference/createvirtualcard-1.md` (source: `createvirtualcard-1`)
- `docs/profile-api-reference/generatetimebasedsecret-2.md` (source: `generatetimebasedsecret-2`)
- `docs/profile-api-reference/inserttransactionfee-1.md` (source: `inserttransactionfee-1`)
- `docs/profile-api-reference/delinkcard.md` (source: `delinkcard`)
- `docs/profile-api-reference/balance-1.md` (source: `balance-1`)
- `docs/profile-api-reference/updateprofile.md` (source: `updateprofile`)
- `docs/profile-api-reference/transferfundsbetweenprofiles.md` (source: `transferfundsbetweenprofiles`)
- `docs/profile-api-reference/cancelstopcard.md` (source: `cancelstopcard`)
- `docs/profile-api-reference/linkcardsbysequencerange.md` (source: `linkcardsbysequencerange`)
- `docs/profile-api-reference/deductcardloadprofile.md` (source: `deductcardloadprofile`)
- `docs/profile-api-reference/stopcard-2.md` (source: `stopcard-2`)
- `docs/profile-api-reference/getschedulestopdetail.md` (source: `getschedulestopdetail`)
- `docs/profile-api-reference/reversetransactionfee.md` (source: `reversetransactionfee`)
- `docs/profile-api-reference/carddetail-1.md` (source: `carddetail-1`)
- `docs/profile-api-reference/devalueprofile.md` (source: `devalueprofile`)
- `docs/profile-api-reference/updatetokenaccount-2.md` (source: `updatetokenaccount-2`)
- `docs/profile-api-reference/reversedeductcardloadprofile.md` (source: `reversedeductcardloadprofile`)
- `docs/profile-api-reference/updatebearer-1.md` (source: `updatebearer-1`)
- `docs/profile-api-reference/allocatecreatevirtualcard.md` (source: `allocatecreatevirtualcard`)
- `docs/profile-api-reference/uploadficadocument.md` (source: `uploadficadocument`)
- `docs/chargeback-api/response-codes.md` (source: `response-codes`)
- `docs/chargeback-api/process-overview.md` (source: `process-overview`)
- `docs/chargeback-api/connectivity.md` (source: `connectivity`)
- `docs/chargeback-api/chargeback-reason-codes.md` (source: `chargeback-reason-codes`)
- `docs/response-codes-2/index.md` (source: `response-codes-2`)
- `docs/chargeback-api/chargeback-api-reference/document-status.md` (source: `document-status`)
- `docs/chargeback-api/chargeback-api-reference/query-chargeback.md` (source: `query-chargeback`)
- `docs/chargeback-api/chargeback-api-reference/first-chargeback.md` (source: `first-chargeback`)
- `docs/chargeback-api/chargeback-api-reference/pre-arbitration.md` (source: `pre-arbitration`)
- `docs/response-codes-2/response-and-action-code-mapping.md` (source: `response-and-action-code-mapping`)
- `docs/chargeback-api/chargeback-api-reference/upload-supporting-document.md` (source: `upload-supporting-document`)
- `docs/card-api/reports/daily-negative-balance-report.md` (source: `daily-negative-balance-report`)
- `docs/card-api/reports/mark-off-file.md` (source: `mark-off-file`)
- `docs/card-api/reports/google-pay-monthly-report.md` (source: `google-pay-monthly-report`)
- `docs/card-api/reports/blocked-transactions-report.md` (source: `blocked-transactions-report`)
- `docs/card-api/reports/authorisation-income-report.md` (source: `authorisation-income-report`)
- `docs/card-api/reports/summary-settlement-report-2.md` (source: `summary-settlement-report-2`)
- `docs/card-api/reports/card-order-report-2.md` (source: `card-order-report-2`)

### Medium Risk (10)
- `docs/Getting Started/security.md` (source: `security`)
- `docs/card-api/secure-cards-1/offline-pin-2.md` (source: `offline-pin-2`)
- `docs/card-api/manage-cards.md` (source: `manage-cards`)
- `docs/chargeback-api/remote-messaging-api/index.md` (source: `remote-messaging-api`)
- `docs/documentation/3d-secure-out-of-band.md` (source: `3d-secure-out-of-band`)
- `docs/documentation/register-thank-you.md` (source: `register-thank-you`)
- `docs/chargeback-api/chargeback-api-reference/index.md` (source: `chargeback-api-reference`)
- `docs/report-generator-offline/report-generator-help.md` (source: `report-generator-help`)
- `docs/qr-payments-api/qr-payments.md` (source: `qr-payments`)
- `docs/documentation/contact-us.md` (source: `contact-us`)

### Low Risk (0)
- None

## Manual Review Notes

Fill in Approved / Needs Fix with notes for each reviewed page.

### docs/companion-api/api-reference-companion/remote/administrativemessage/administrative-message-values.md
- Status: TBD
- Notes: 

### docs/companion-api/api-reference-companion/remote/administrativemessage/index.md
- Status: TBD
- Notes: 

### docs/card-api/api-reference-card/ordercardwithpinblock.md
- Status: TBD
- Notes: 

### docs/companion-api/klv-lookup.md
- Status: TBD
- Notes: 

### docs/Getting Started/glossary.md
- Status: TBD
- Notes: 

### docs/Getting Started/fraud.md
- Status: TBD
- Notes: 

### docs/chargeback-api/remote-messaging-api/remote-messaging-api-chargeback-notification.md
- Status: TBD
- Notes: 

### docs/card-api/tokenization/index.md
- Status: TBD
- Notes: 

### docs/documentation/reporting-api-2.md
- Status: TBD
- Notes: 

### docs/documentation/reversedevalueprofile-1.md
- Status: TBD
- Notes: 

### docs/documentation/how_payments_work.md
- Status: TBD
- Notes: 

### docs/card-api/disputes.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/ordercard-2.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/listalltokens-2.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/checkauthorisation.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/togglevoucherfeature-2.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/reversevastransferfunds.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/updatescheduledstop.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/statementbydaterange.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/stoptoken-2.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/allocatecard.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/vastransferfunds.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/cancelscheduledstop.md
- Status: TBD
- Notes: 

### docs/card-api/manage-funds-1.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/statement-1.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/calculatetav-2.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/createscheduledstop.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/reversedevalueprofile.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/activate.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/checkload.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/changepin-2.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/transferfunds-1.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/allocateiban.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/updateallocatedcard.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/transferlink-2.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/status-1.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/deletetoken-1.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/resetpin-1.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/linkcard-2.md
- Status: TBD
- Notes: 

### docs/card-api/reconciliation.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/unstoptoken-2.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/updatebearerextended.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/transfertoken-1.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/activatetoken-2.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/register.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/loadcarddeductprofile.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/listtokens-2.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/createvirtualcard-1.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/generatetimebasedsecret-2.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/inserttransactionfee-1.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/delinkcard.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/balance-1.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/updateprofile.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/transferfundsbetweenprofiles.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/cancelstopcard.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/linkcardsbysequencerange.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/deductcardloadprofile.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/stopcard-2.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/getschedulestopdetail.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/reversetransactionfee.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/carddetail-1.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/devalueprofile.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/updatetokenaccount-2.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/reversedeductcardloadprofile.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/updatebearer-1.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/allocatecreatevirtualcard.md
- Status: TBD
- Notes: 

### docs/profile-api-reference/uploadficadocument.md
- Status: TBD
- Notes: 

### docs/chargeback-api/response-codes.md
- Status: TBD
- Notes: 

### docs/chargeback-api/process-overview.md
- Status: TBD
- Notes: 

### docs/chargeback-api/connectivity.md
- Status: TBD
- Notes: 

### docs/chargeback-api/chargeback-reason-codes.md
- Status: TBD
- Notes: 

### docs/response-codes-2/index.md
- Status: TBD
- Notes: 

### docs/chargeback-api/chargeback-api-reference/document-status.md
- Status: TBD
- Notes: 

### docs/chargeback-api/chargeback-api-reference/query-chargeback.md
- Status: TBD
- Notes: 

### docs/chargeback-api/chargeback-api-reference/first-chargeback.md
- Status: TBD
- Notes: 

### docs/chargeback-api/chargeback-api-reference/pre-arbitration.md
- Status: TBD
- Notes: 

### docs/response-codes-2/response-and-action-code-mapping.md
- Status: TBD
- Notes: 

### docs/chargeback-api/chargeback-api-reference/upload-supporting-document.md
- Status: TBD
- Notes: 

### docs/card-api/reports/daily-negative-balance-report.md
- Status: TBD
- Notes: 

### docs/card-api/reports/mark-off-file.md
- Status: TBD
- Notes: 

### docs/card-api/reports/google-pay-monthly-report.md
- Status: TBD
- Notes: 

### docs/card-api/reports/blocked-transactions-report.md
- Status: TBD
- Notes: 

### docs/card-api/reports/authorisation-income-report.md
- Status: TBD
- Notes: 

### docs/card-api/reports/summary-settlement-report-2.md
- Status: TBD
- Notes: 

### docs/card-api/reports/card-order-report-2.md
- Status: TBD
- Notes: 

### docs/Getting Started/security.md
- Status: TBD
- Notes: 

### docs/card-api/secure-cards-1/offline-pin-2.md
- Status: TBD
- Notes: 

### docs/card-api/manage-cards.md
- Status: TBD
- Notes: 

### docs/chargeback-api/remote-messaging-api/index.md
- Status: TBD
- Notes: 

### docs/documentation/3d-secure-out-of-band.md
- Status: TBD
- Notes: 

### docs/documentation/register-thank-you.md
- Status: TBD
- Notes: 

### docs/chargeback-api/chargeback-api-reference/index.md
- Status: TBD
- Notes: 

### docs/report-generator-offline/report-generator-help.md
- Status: TBD
- Notes: 

### docs/qr-payments-api/qr-payments.md
- Status: TBD
- Notes: 

### docs/documentation/contact-us.md
- Status: TBD
- Notes: 

