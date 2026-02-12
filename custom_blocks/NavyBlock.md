---
name: NavyBlock
---
<div
  style={{
    background: "#0F1F3A",
    color: "#FFFFFF",
    padding: "0 16px",
    minHeight: "48px",
    display: "flex",
    alignItems: "center",
    gap: "12px",
    fontSize: "14px",
    fontWeight: 500,
    lineHeight: "20px",
  }}
>
  {/* Info icon (SVG, perfectly centered) */}
  <span
    style={{
      width: "20px",
      height: "20px",
      borderRadius: "50%",
      background: "#3B6EDC",
      display: "inline-flex",
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
      style={{ display: "block" }}
    >
      {/* dot */}
      <circle cx="6" cy="3" r="1" fill="#FFFFFF" />
      {/* stem */}
      <rect x="5.25" y="5" width="1.5" height="5" rx="0.75" fill="#FFFFFF" />
    </svg>
  </span>

  <span style={{ display: "inline-flex", alignItems: "center" }}>
    <span style={{ fontWeight: 800, marginRight: "6px" }}>Note:</span>
    <span>sample file will automatically download upon clicking link</span>
  </span>
</div>


<br />
