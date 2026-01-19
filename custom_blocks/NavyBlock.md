---
name: NavyBlock
---
<div
  style={{
    background: "#0F1F3A",
    color: "#FFFFFF",
    padding: "0 16px",
    minHeight: "56px",              // ensures vertical centering in the box
    display: "flex",
    alignItems: "center",
    gap: "12px",
    fontSize: "14px",
    fontWeight: 500,
    lineHeight: "20px",             // keep icon + text aligned
  }}
>
  {/* Info icon */}
  <div
    style={{
      width: "20px",
      height: "20px",
      borderRadius: "50%",
      background: "#3B6EDC",
      display: "grid",
      placeItems: "center",
      flexShrink: 0,
    }}
    aria-hidden="true"
  >
    <span
      style={{
        display: "block",
        fontSize: "12px",
        fontWeight: 800,
        lineHeight: "12px",
        transform: "translateY(-0.5px)",
      }}
    >
      i
    </span>
  </div>

  {/* Text */}
  <span style={{ display: "inline-flex", alignItems: "center" }}>
    <span style={{ fontWeight: 800, marginRight: "6px" }}>Note:</span>
    <span>sample file will automatically download upon clicking link</span>
  </span>
</div>


<br />
