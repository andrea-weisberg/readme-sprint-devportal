---
title: Overview
deprecated: false
hidden: false
metadata:
  robots: index
---
<h1 style={{ margin: '0 0 12px 0', fontSize: '40px', lineHeight: 1.15 }}>
  Companion API is a simple API that allows you to issue cards and hold your customers’ card balances on your platform
</h1>

<p style={{ margin: '0 0 16px 0', fontSize: '16px', lineHeight: 1.6, color: '#243646' }}>
  A Companion card is a card that is linked to a store of value (SVA) like a wallet or a bank account. What makes this API different from the others we offer, is that the customer's card balance sits within the SVA and not on the card. Choose the Companion API if you want to issue cards and hold your customers’ card balances on your own platform.
</p>

<p style={{ margin: '0 0 16px 0', fontSize: '16px', lineHeight: 1.6, color: '#243646' }}>
  **Note**: You’ll be responsible for authorising transactions with this API.
</p>

<div
  style={{
    background: '#0B1B33',
    color: '#FFFFFF',
    borderRadius: '12px',
    padding: '18px 20px',
    margin: '0 0 32px 0',
    display: 'flex',
    alignItems: 'flex-start',
    gap: '14px',
  }}
>
  {/* Info icon */}

  <div
    style={{
      width: '28px',
      height: '28px',
      borderRadius: '999px',
      background: '#1E3A66',
      color: '#FFFFFF',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      fontWeight: 700,
      fontSize: '16px',
      lineHeight: '28px',
      flexShrink: 0,
    }}
  >
    i
  </div>

  {/* Text content */}

  <p
    style={{
      margin: 0,
      fontSize: '16px',
      lineHeight: 1.6,
    }}
  >
    If you want Paymentology to hold your customer’s balance for you, use the **Card API** instead. If you’re not sure which API to choose, read about{' '} <a href="https://developer.sprint.paymentology.com/get-started/our-apis/" style={{color: '#FFFFFF',textDecoration: 'underline',fontWeight: 600,}}> our APIs</a> {' '} first or{' '} <a href="#" style={{color: '#FFFFFF',textDecoration: 'underline',fontWeight: 600,}}> get in touch </a>.
  </p>
</div>

<div style={{ width: '100%', margin: '20px 0 8px 0' }}>
  {/* Row 1: 3 tiles */}

  <div
    style={{
      display: 'grid',
      gridTemplateColumns: 'repeat(3, 1fr)',
      gap: '20px',
      marginBottom: '20px',
    }}
  >
    <div style={{ background: '#F3FBF8', borderRadius: '16px', padding: '22px', minHeight: '190px' }}>
      <img src="ICON_URL_1" alt="" style={{ width: '56px', height: '56px', marginBottom: '40px' }} />

      <p style={{ margin: 0, fontSize: '16px', lineHeight: 1.55, fontWeight: 700, color: '#0F2233' }}>
        Store your customers’ account balances on your platform and be responsible for authorising transactions
      </p>
    </div>

    <div style={{ background: '#F3FBF8', borderRadius: '16px', padding: '22px', minHeight: '190px' }}>
      <img src="ICON_URL_2" alt="" style={{ width: '56px', height: '56px', marginBottom: '40px' }} />

      <p style={{ margin: 0, fontSize: '16px', lineHeight: 1.55, fontWeight: 700, color: '#0F2233' }}>
        Issue your own virtual and physical cards instantly
      </p>
    </div>

    <div style={{ background: '#F3FBF8', borderRadius: '16px', padding: '22px', minHeight: '190px' }}>
      <img src="ICON_URL_3" alt="" style={{ width: '56px', height: '56px', marginBottom: '40px' }} />

      <p style={{ margin: 0, fontSize: '16px', lineHeight: 1.55, fontWeight: 700, color: '#0F2233' }}>
        Connect your customers to an open-loop environment with just one integration
      </p>
    </div>
  </div>

  {/* Row 2: 2 tiles */}

  <div
    style={{
      display: 'grid',
      gridTemplateColumns: 'repeat(2, 1fr)',
      gap: '20px',
    }}
  >
    <div style={{ background: '#F3FBF8', borderRadius: '16px', padding: '22px', minHeight: '190px' }}>
      <img src="ICON_URL_4" alt="" style={{ width: '56px', height: '56px', marginBottom: '40px' }} />

      <p style={{ margin: 0, fontSize: '16px', lineHeight: 1.55, fontWeight: 700, color: '#0F2233' }}>
        Give your cardholders access to the global open-loop world of payments so that they can transact securely anywhere 24/7
      </p>
    </div>

    <div style={{ background: '#F3FBF8', borderRadius: '16px', padding: '22px', minHeight: '190px' }}>
      <img src="ICON_URL_5" alt="" style={{ width: '56px', height: '56px', marginBottom: '40px' }} />

      <p style={{ margin: 0, fontSize: '16px', lineHeight: 1.55, fontWeight: 700, color: '#0F2233' }}>
        Empower customers who don’t qualify for a credit card or bank account with a virtual or physical card that they can use to shop online
      </p>
    </div>
  </div>
</div>

The Companion API is split into two separate APIs based on whether we are calling you (we call it **Remote API**), or you’re calling us (**Local API**):

|:--------:|:--------:|
| **Local API - you call us**   |    **Remote API - we call you**       |
| This API allows you to call us to perform necessary actions on your cards It contains all the API methods you will need e.g. linking a card to the SVA or updating cardholder details It is hosted by Paymentology |  This API allows us to call you to perform actions on your SVA/wallet e.g. Deducting/loading funds, balance inquiries, etc. It is hosted by you         |
