---
name: DeclinedNavyBox
---
<div
  style={{
    background: "#0F1F3A",
    color: "#FFFFFF",
    height: "48px",                 // 👈 fixed height = true centering
    display: "flex",
    alignItems: "center",
    gap: "12px",
    padding: "0 16px",              // 👈 horizontal only
    fontSize: "14px",
    fontWeight: 500,
    lineHeight: "20px",
  }}
>
  {/* Info icon */}
  <div
    style={{
      width: "20px",
      height: "20px",
      borderRadius: "50%",
      background: "#3B6EDC",
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      flexShrink: 0,
    }}
    aria-hidden="true"
  >
    <svg
      width="12"
      height="12"
      viewBox="0 0 12 12"
      xmlns="http://www.w3.org/2000/svg"
    >
      <circle cx="6" cy="3" r="1" fill="#FFFFFF" />
      <rect x="5.25" y="5" width="1.5" height="5" rx="0.75" fill="#FFFFFF" />
    </svg>
  </div>

  {/* Text */}
  <div style={{ display: "flex", alignItems: "center" }}>
    If the transaction did not reach Paymentology and was declined, this would
    not appear on the report.
  </div>
</div>
