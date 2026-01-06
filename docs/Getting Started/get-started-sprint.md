---
title: Get Started
excerpt: >-
  Welcome to Paymentology’s Sprint Developer Portal, where you will find
  everything you need to start integrating with our platform. Use our APIs to
  start issuing physical and virtual cards quickly and easily with just a few
  lines of code.
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  description: |2-
      Welcome to Paymentology’s Sprint Developer Portal, where you will find
      everything you need to start integrating with our platform. Use our APIs to
      start issuing physical and virtual cards quickly and easily with just a few
      lines of code.
  robots: index
---
## Our API’s

**We offer three simple and distinct APIs:**

<div style={{display:'flex',gap:'24px',flexWrap:'wrap',margin:'32px 0'}}>
  {/* Companion API */}

  <div style={{flex:1,minWidth:'260px',background:'#F3FBF8',padding:'32px',borderRadius:'16px'}}>
    <div style={{width:'64px',height:'64px',background:'#9ADBC0',borderRadius:'16px',marginBottom:'24px'}} />

    <h3 style={{marginBottom:'12px'}}>Companion API</h3>

    <p>
      Use this API if you would like to store your customers’ card balances
      on your platform.
    </p>
  </div>

  {/* Card API */}

  <div style={{flex:1,minWidth:'260px',background:'#EDF9F5',padding:'32px',borderRadius:'16px'}}>
    <div style={{width:'64px',height:'64px',background:'#9ADBC0',borderRadius:'16px',marginBottom:'24px'}} />

    <h3 style={{marginBottom:'12px'}}>Card API</h3>

    <p>
      Use this API if you want us to store your customers’ card balances
      for you.
    </p>
  </div>

  {/* QR Payments API */}

  <div style={{flex:1,minWidth:'260px',background:'#F3FBF8',padding:'32px',borderRadius:'16px'}}>
    <div style={{width:'64px',height:'64px',background:'#9ADBC0',borderRadius:'16px',marginBottom:'24px'}} />

    <h3 style={{marginBottom:'12px'}}>QR Payments API</h3>

    <p>
      Use this API to enable contactless QR Payments.
    </p>
  </div>
</div>

The Card and Companion API each offer a unique customer journey, so you will need to clearly understand how the two are different and what they do, to choose the one that is right for you. Our QR Payments API can be used as a standalone API or as a plugin to either the Card or Companion API.

[Explore Our API’s](our-apis.md)

## Testing environments

**You’ll get access to our two testing environments:**

[Explore Our Testing Environments](testing.md)

## Helpful tools

**We have a helpful set of tools to support your integration process:**

- **XML Generator**: allows you to generate a valid XML request (including a checksum string) from your request parameters
- **XML Poster**: allows you to post XML requests directly to the Paymentology system
- **Checksum Generator**: allows you to calculate the checksum for a transaction based on a terminal password value and the request data
- **API references**: we have included API references under each of our three API sections

