---
title: Reporting API (companion)
deprecated: false
hidden: false
metadata:
  robots: index
---
**The Reporting API is a local API which can be called to obtain files produced by Tutuka, foe example, reports.**

**In order to call this API, a token must be obtained from the Tutuka Token Service. This token is validated by the API and allows access to resources based on certain values contained within the token.**

### *The Reporting API is only available to clients on our AWS UAT environment and will become available to all clients in September 2021*

# Authentication (Obtaining a token)

The token will remain valid for 24 hours, after which a fresh token should be obtained.

To obtain a token from the Token service, you will require a *ClientID* and *Client secret* which can be obtained from your Client Executive. These values are highly sensitive and should be treated as such. Storing these values in browsers, local disk and source control is not recommended. Should these values be compromised, contact your Client executive urgently.

In order to obtain a token, an http request to: `https://auth.uat.tutuka.cloud/oauth/token` using Basic Authentication and providing the BASE64 encoded ClientID and Secret in the Authorization Header specifying the `client_credentials` grant type in the body. e.g.

```null
async function getAccessToken() {
  const authToken = `${process.env.CLIENT_ID}:${process.env.SECRET}`;
  const buffer = Buffer.from(authToken);
  var options = {
    'method': 'POST',
    'hostname': 'auth.uat.tutuka.cloud',
    'path': '/oauth/token',
    'headers': {
      'Authorization': `Basic ${buffer.toString('base64')}`,
      'Content-type': 'text/html'
    }
  };

  var body = qs.stringify({
    'grant_type': 'client_credentials',
  });
  const resp = await httpCall(options, body)
    .catch(error => { console.log(error); })
  return JSON.parse(resp.body).access_token;
}
```

```null
async function getCampaignReports(token) {
  const options = {
    'method': 'GET',
    'hostname': envContext[process.env.ENV].ReportsApiEndpoint,
    'path': `/v1/clients/insert_client_id/campaigns/insert_campaign_uuid/reports`,
    'protocol': 'https:',  
    'headers': {
      'Authorization': 'Bearer ' + token,
      'Content-type': 'application/json'
    }
  };
  let GetCampaignReportsResp = await httpCall(options, "");
  console.log(`GetCampaignReports: statusCode: ${GetCampaignReportsResp.statusCode ?? ""}, statusMessage: ${GetCampaignReportsResp.statusMessage ?? ""}`);
  console.log(GetCampaignReportsResp.body);
}

(async () => {
  const tokenPromise = getAccessToken();
  tokenPromise.then(getCampaignReports);
})();
```

```null
[
  {
    "reportId":4,
    "reportName":"Companion Daily Statement"
  },
  {
    "reportId":5,
    "reportName":"Daily Settlement summary"
  },
  {
    "reportId":12,
    "reportName":"Daily Authorisation Failure Report"
  },
  {
    "reportId":13,
    "reportName":"Daily Created Cards Report"
  }
]
```

```null
{
  "campaignUUID": "72021503-C427-1A07-XXXXXXXXXXXXXXX",
  "reportId": 4,
  "dates": [
    "20100510",
    "20200510",
    "20200515",
    "20210510"
  ]
}
```

```null
{
  "campaignUUID": "72021503-C427-1A07-ED8968880BC391FC",
  "reportId": 4,
  "date": "20210510",
  "reportUrl": "https://coldfusion-test.s3.eu-west-1.amazonaws.com/WebShare/VoucherEngine/downloads/72021503-C427-1A07-ED8968880BC391FC/RapydCorporateCompanionPhysicalSG_CompanionStatement_20210510.csv?X-Amz-Security-Token\u003dIQoJb3J..."
}
```

The token obtained can then be used as a Bearer token in calls to the Reporting API, for example:
```null
async function getAccessToken() {
  const authToken = `${process.env.CLIENT_ID}:${process.env.SECRET}`;
  const buffer = Buffer.from(authToken);
  var options = {
    'method': 'POST',
    'hostname': 'auth.uat.tutuka.cloud',
    'path': '/oauth/token',
    'headers': {
      'Authorization': `Basic ${buffer.toString('base64')}`,
      'Content-type': 'text/html'
    }
  };

  var body = qs.stringify({
    'grant_type': 'client_credentials',
  });
  const resp = await httpCall(options, body)
    .catch(error => { console.log(error); })
  return JSON.parse(resp.body).access_token;
}
```

```null
async function getCampaignReports(token) {
  const options = {
    'method': 'GET',
    'hostname': envContext[process.env.ENV].ReportsApiEndpoint,
    'path': `/v1/clients/insert_client_id/campaigns/insert_campaign_uuid/reports`,
    'protocol': 'https:',  
    'headers': {
      'Authorization': 'Bearer ' + token,
      'Content-type': 'application/json'
    }
  };
  let GetCampaignReportsResp = await httpCall(options, "");
  console.log(`GetCampaignReports: statusCode: ${GetCampaignReportsResp.statusCode ?? ""}, statusMessage: ${GetCampaignReportsResp.statusMessage ?? ""}`);
  console.log(GetCampaignReportsResp.body);
}

(async () => {
  const tokenPromise = getAccessToken();
  tokenPromise.then(getCampaignReports);
})();
```

```null
[
  {
    "reportId":4,
    "reportName":"Companion Daily Statement"
  },
  {
    "reportId":5,
    "reportName":"Daily Settlement summary"
  },
  {
    "reportId":12,
    "reportName":"Daily Authorisation Failure Report"
  },
  {
    "reportId":13,
    "reportName":"Daily Created Cards Report"
  }
]
```

```null
{
  "campaignUUID": "72021503-C427-1A07-XXXXXXXXXXXXXXX",
  "reportId": 4,
  "dates": [
    "20100510",
    "20200510",
    "20200515",
    "20210510"
  ]
}
```

```null
{
  "campaignUUID": "72021503-C427-1A07-ED8968880BC391FC",
  "reportId": 4,
  "date": "20210510",
  "reportUrl": "https://coldfusion-test.s3.eu-west-1.amazonaws.com/WebShare/VoucherEngine/downloads/72021503-C427-1A07-ED8968880BC391FC/RapydCorporateCompanionPhysicalSG_CompanionStatement_20210510.csv?X-Amz-Security-Token\u003dIQoJb3JpZ2luX2VjEBcaCWV1LXdlc3QtMSJHMEUCIQCNAWtEsDGdLZ5WeOrjvpeK94hjT0Zrb%2FLnHnjlNCYJzwIgR5xKw8ZqrH%2F46a3%2FaMvva0NANSpRYIm%2FuCZC9M1Ovj8q9AEIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARACGgw3MjU0MDY2Nzg2MjgiDCgkP2b3CNM1OCnxdCrIAYK6ZBCoZ%2BbPODGAzDbm2YIkIsfxGdNiVjd2PpqMMFvsu%2Fui1JrTluiu3USmLcwDNG2f3OURO798%2FeZSYka%2Fi%2Bo79kCcHLs2GFaU0vKvSoMzZAlHxTExJhaO6zLcidAdQREY4%2BfZOBh7z5OAu1RJRcDVjL4ALrHhW5LCA1U9wXyDY2qTjA6TWDt3LyYogHaxLJZR89X5ZuUJD4qPSL0By%2BU6ZgHGvQL8gfs%2FFWQSF5qWz7U9rc2YOykY87iqI%2F1bYqxEuNlw9aBRMKWX2YUGOuABu19V5D1iHBnnulfEQXIefc%2BZunfirz2HGU3IJlOstzeOa11qQaC3Wfbc2%2BWsR8WkD%2BdjT7nXuGCDBDNN73JljSWXN1Vg%2BTNrHY%2FcuqqEMFWUwLBCpbp4PDwwRrAcGA%2FHhD4fxMojMFlPFdIRg6tXVFI%2FtA9jUbnyNpZ63ef%2FI1%2FY9K3RXKBt%2FfJttHWDgmQEQNB3VT1zrP9S06uzk%2FC195UNHmXNfFTX0ryfn0RN2XSBVn6ZptaF5lW9lVDH1VooTjfqTCnUsvBslXvczYw2QO2rj6YDiqB%2FConF3HXC56g%3D\u0026X-Amz-Algorithm\u003dAWS4-HMAC-SHA256\u0026X-Amz-Date\u003d20210601T150106Z\u0026X-Amz-SignedHeaders\u003dhost\u0026X-Amz-Expires\u003d299\u0026X-Amz-Credential\u003dASIA2RZM3PZSNZWQHSW5%2F20210601%2Feu-west-1%2Fs3%2Faws4_request\u0026X-Amz-Signature\u003df1b3844473df87d97c6333d21da220b217af60ec281414481bd9029e7f778a3c"
}
```

---

# Reports

During the onboarding process, clients are issued with a Client UUID, which will include one or more campaigns which are identified by the campaign UUIDs.

Reports are produced for campaigns based on product type and opt in / out configuration values.

## Report Types for Campaign


#### Path parameters

| Parameter    | type   | Limits | required | Description                                                            |
| ------------ | ------ | ------ | :------: | ---------------------------------------------------------------------- |
| ClientUUID   | String |        |     ✓    | Your client UUID                                                       |
| CampaignUUID | String |        |     ✓    | The campaignUUID for which you want to obtain a list of report types.  |

```null
async function getAccessToken() {
  const authToken = `${process.env.CLIENT_ID}:${process.env.SECRET}`;
  const buffer = Buffer.from(authToken);
  var options = {
    'method': 'POST',
    'hostname': 'auth.uat.tutuka.cloud',
    'path': '/oauth/token',
    'headers': {
      'Authorization': `Basic ${buffer.toString('base64')}`,
      'Content-type': 'text/html'
    }
  };

  var body = qs.stringify({
    'grant_type': 'client_credentials',
  });
  const resp = await httpCall(options, body)
    .catch(error => { console.log(error); })
  return JSON.parse(resp.body).access_token;
}


## Get List of Reports of a particular type

#### Path parameters

| Parameter    | type   | Limits | required | Description                                                            |
| ------------ | ------ | ------ | :------: | ---------------------------------------------------------------------- |
| ClientUUID   | String |        |     ✓    | Your client UUID                                                       |
| CampaignUUID | String |        |     ✓    | The campaignUUID for which you want to obtain a list of report types. |
| ReportId     | String |        |     ✓    | The numeric id identifying the report type                             |

```null
async function getAccessToken() {
  const authToken = `${process.env.CLIENT_ID}:${process.env.SECRET}`;
  const buffer = Buffer.from(authToken);
  var options = {
    'method': 'POST',
    'hostname': 'auth.uat.tutuka.cloud',
    'path': '/oauth/token',
    'headers': {
      'Authorization': `Basic ${buffer.toString('base64')}`,
      'Content-type': 'text/html'
    }
  };

  var body = qs.stringify({
    'grant_type': 'client_credentials',
  });
  const resp = await httpCall(options, body)
    .catch(error => { console.log(error); })
  return JSON.parse(resp.body).access_token;
}
````

```null
async function getCampaignReports(token) {
  const options = {
    'method': 'GET',
    'hostname': envContext[process.env.ENV].ReportsApiEndpoint,
    'path': `/v1/clients/insert_client_id/campaigns/insert_campaign_uuid/reports`,
    'protocol': 'https:',  
    'headers': {
      'Authorization': 'Bearer ' + token,
      'Content-type': 'application/json'
    }
  };
  let GetCampaignReportsResp = await httpCall(options, "");
  console.log(`GetCampaignReports: statusCode: ${GetCampaignReportsResp.statusCode ?? ""}, statusMessage: ${GetCampaignReportsResp.statusMessage ?? ""}`);
  console.log(GetCampaignReportsResp.body);
}

(async () => {
  const tokenPromise = getAccessToken();
  tokenPromise.then(getCampaignReports);
})();
```

```null
[
  {
    "reportId":4,
    "reportName":"Companion Daily Statement"
  },
  {
    "reportId":5,
    "reportName":"Daily Settlement summary"
  },
  {
    "reportId":12,
    "reportName":"Daily Authorisation Failure Report"
  },
  {
    "reportId":13,
    "reportName":"Daily Created Cards Report"
  }
]
```

```null
{
  "campaignUUID": "72021503-C427-1A07-XXXXXXXXXXXXXXX",
  "reportId": 4,
  "dates": [
    "20100510",
    "20200510",
    "20200515",
    "20210510"
  ]
}
```


```null
{
  "campaignUUID": "72021503-C427-1A07-ED8968880BC391FC",
  "reportId": 4,
  "date": "20210510",
  "reportUrl": "https://coldfusion-test.s3.eu-west-1.amazonaws.com/WebShare/VoucherEngine/downloads/72021503-C427-1A07-ED8968880BC391FC/RapydCorporateCompanionPhysicalSG_CompanionStatement_20210510.csv?X-Amz-Security-Token\u003dIQoJb3JpZ2luX2VjEBcaCWV1LXdlc3QtMSJHMEUCIQCNAWtEsDGdLZ5WeOrjvpeK94hjT0Zrb%2FLnHnjlNCYJzwIgR5xKw8ZqrH%2F46a3%2FaMvva0NANSpRYIm%2FuCZC9M1Ovj8q9AEIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARACGgw3MjU0MDY2Nzg2MjgiDCgkP2b3CNM1OCnxdCrIAYK6ZBCoZ%2BbPODGAzDbm2YIkIsfxGdNiVjd2PpqMMFvsu%2Fui1JrTluiu3USmLcwDNG2f3OURO798%2FeZSYka%2Fi%2Bo79kCcHLs2GFaU0vKvSoMzZAlHxTExJhaO6zLcidAdQREY4%2BfZOBh7z5OAu1RJRcDVjL4ALrHhW5LCA1U9wXyDY2qTjA6TWDt3LyYogHaxLJZR89X5ZuUJD4qPSL0By%2BU6ZgHGvQL8gfs%2FFWQSF5qWz7U9rc2YOykY87iqI%2F1bYqxEuNlw9aBRMKWX2YUGOuABu19V5D1iHBnnulfEQXIefc%2BZunfirz2HGU3IJlOstzeOa11qQaC3Wfbc2%2BWsR8WkD%2BdjT7nXuGCDBDNN73JljSWXN1Vg%2BTNrHY%2FcuqqEMFWUwLBCpbp4PDwwRrAcGA%2FHhD4fxMojMFlPFdIRg6tXVFI%2FtA9jUbnyNpZ63ef%2FI1%2FY9K3RXKBt%2FfJttHWDgmQEQNB3VT1zrP9S06uzk%2FC195UNHmXNfFTX0ryfn0RN2XSBVn6ZptaF5lW9lVDH1VooTjfqTCnUsvBslXvczYw2QO2rj6YDiqB%2FConF3HXC56g%3D\u0026X-Amz-Algorithm\u003dAWS4-HMAC-SHA256\u0026X-Amz-Date\u003d20210601T150106Z\u0026X-Amz-SignedHeaders\u003dhost\u0026X-Amz-Expires\u003d299\u0026X-Amz-Credential\u003dASIA2RZM3PZSNZWQHSW5%2F20210601%2Feu-west-1%2Fs3%2Faws4_request\u0026X-Amz-Signature\u003df1b3844473df87d97c6333d21da220b217af60ec281414481bd9029e7f778a3c"
}
```
