"""Apple HIG Inspired PeopleOps Executive & Funnel Intelligence Suite.
Combines Liquid Glass functional layer, Apple typography, custom SVG tapered funnel,
and interactive data exploration.
"""

from pathlib import Path

OUT_FILE = Path(__file__).resolve().parent / "dashboard.html"

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>Indus Weave Textiles — PeopleOps Executive Intelligence</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    :root {
      --system-bg: #000000;
      --secondary-bg: #0d1117;
      --card-bg: rgba(22, 27, 34, 0.72);
      --card-border: rgba(255, 255, 255, 0.08);
      --card-hover-border: rgba(255, 255, 255, 0.18);
      
      --system-blue: #0A84FF;
      --system-indigo: #5E5CE6;
      --system-purple: #BF5AF2;
      --system-pink: #FF375F;
      --system-red: #FF453A;
      --system-orange: #FF9F0A;
      --system-yellow: #FFD60A;
      --system-green: #30D158;
      --system-mint: #63E6E2;
      --system-teal: #40C8E0;
      --system-cyan: #64D2FF;
      
      --label-primary: #FFFFFF;
      --label-secondary: #86868B;
      --label-tertiary: #6E6E73;
      --separator: rgba(255, 255, 255, 0.08);
      
      --font-stack: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Plus Jakarta Sans", system-ui, sans-serif;
      --font-mono: "SF Mono", "JetBrains Mono", Menlo, monospace;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; -webkit-font-smoothing: antialiased; }

    body {
      font-family: var(--font-stack);
      background-color: var(--system-bg);
      color: var(--label-primary);
      line-height: 1.47059;
      letter-spacing: -0.022em;
      min-height: 100vh;
      background-image: 
        radial-gradient(at 0% 0%, rgba(10, 132, 255, 0.12) 0px, transparent 50%),
        radial-gradient(at 100% 10%, rgba(94, 92, 230, 0.10) 0px, transparent 50%),
        radial-gradient(at 50% 100%, rgba(48, 209, 88, 0.06) 0px, transparent 50%);
      background-attachment: fixed;
    }

    /* Apple Liquid Glass Floating Header */
    header {
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(13, 17, 23, 0.75);
      backdrop-filter: blur(28px) saturate(190%);
      -webkit-backdrop-filter: blur(28px) saturate(190%);
      border-bottom: 1px solid var(--separator);
      padding: 16px 36px;
    }

    .header-inner {
      max-width: 1400px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 20px;
      flex-wrap: wrap;
    }

    .brand-section {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .brand-icon {
      width: 40px;
      height: 40px;
      border-radius: 10px;
      background: linear-gradient(135deg, #2c3e50, #000000);
      border: 1px solid rgba(255, 255, 255, 0.12);
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.5);
    }

    .brand-icon svg { width: 22px; height: 22px; fill: none; stroke: var(--system-cyan); stroke-width: 2; }

    .brand-text h1 {
      font-size: 19px;
      font-weight: 700;
      letter-spacing: -0.015em;
      color: #fff;
    }

    .brand-text p {
      font-size: 12.5px;
      color: var(--label-secondary);
    }

    /* Apple Segmented Control Bar */
    .segmented-nav {
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 9999px;
      padding: 3px;
      display: inline-flex;
      align-items: center;
      gap: 2px;
    }

    .segmented-item {
      background: transparent;
      border: none;
      color: var(--label-secondary);
      font-family: inherit;
      font-size: 13px;
      font-weight: 600;
      padding: 7px 16px;
      border-radius: 9999px;
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      align-items: center;
      gap: 7px;
      white-space: nowrap;
    }

    .segmented-item svg { width: 15px; height: 15px; stroke: currentColor; fill: none; stroke-width: 2; }

    .segmented-item:hover {
      color: var(--label-primary);
    }

    .segmented-item.active {
      background: rgba(255, 255, 255, 0.16);
      color: #ffffff;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.35);
    }

    .status-badge {
      display: inline-flex;
      align-items: center;
      gap: 7px;
      padding: 6px 12px;
      border-radius: 9999px;
      font-size: 12px;
      font-weight: 600;
      background: rgba(48, 209, 88, 0.12);
      color: var(--system-green);
      border: 1px solid rgba(48, 209, 88, 0.25);
    }

    .status-dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--system-green);
      box-shadow: 0 0 8px var(--system-green);
    }

    /* Main Container */
    main {
      max-width: 1400px;
      margin: 0 auto;
      padding: 32px 36px 80px;
    }

    /* Apple-Style Widget Cards */
    .widget-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 16px;
      margin-bottom: 28px;
    }

    .widget-card {
      background: var(--card-bg);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid var(--card-border);
      border-radius: 18px;
      padding: 22px;
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.25s ease, box-shadow 0.25s ease;
      position: relative;
      overflow: hidden;
    }

    .widget-card:hover {
      transform: translateY(-2px);
      border-color: var(--card-hover-border);
      box-shadow: 0 12px 32px rgba(0, 0, 0, 0.5);
    }

    .widget-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
    }

    .widget-title {
      font-size: 13px;
      font-weight: 600;
      color: var(--label-secondary);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .widget-pill {
      font-size: 11.5px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 6px;
    }

    .pill-cyan { background: rgba(100, 210, 255, 0.12); color: var(--system-cyan); }
    .pill-green { background: rgba(48, 209, 88, 0.12); color: var(--system-green); }
    .pill-orange { background: rgba(255, 159, 10, 0.12); color: var(--system-orange); }
    .pill-red { background: rgba(255, 69, 58, 0.15); color: var(--system-red); }

    .widget-value {
      font-size: 34px;
      font-weight: 800;
      letter-spacing: -0.03em;
      color: #fff;
      margin-bottom: 4px;
    }

    .widget-subtitle {
      font-size: 13px;
      color: var(--label-tertiary);
    }

    /* Content Panels */
    .apple-panel {
      background: var(--card-bg);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid var(--card-border);
      border-radius: 20px;
      padding: 26px;
      margin-bottom: 26px;
    }

    .panel-headline {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
      flex-wrap: wrap;
      gap: 12px;
    }

    .panel-headline h2 {
      font-size: 18px;
      font-weight: 700;
      letter-spacing: -0.015em;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .panel-headline p {
      font-size: 13px;
      color: var(--label-secondary);
    }

    /* Apple Callout */
    .apple-callout {
      border-radius: 14px;
      padding: 18px 20px;
      margin-bottom: 24px;
      display: flex;
      gap: 14px;
      align-items: flex-start;
      border: 1px solid transparent;
    }

    .callout-blue { background: rgba(10, 132, 255, 0.08); border-color: rgba(10, 132, 255, 0.2); }
    .callout-red { background: rgba(255, 69, 58, 0.08); border-color: rgba(255, 69, 58, 0.2); }
    .callout-orange { background: rgba(255, 159, 10, 0.08); border-color: rgba(255, 159, 10, 0.2); }

    .callout-icon {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      margin-top: 1px;
    }

    .callout-blue .callout-icon { background: rgba(10, 132, 255, 0.2); color: var(--system-blue); }
    .callout-red .callout-icon { background: rgba(255, 69, 58, 0.2); color: var(--system-red); }
    .callout-orange .callout-icon { background: rgba(255, 159, 10, 0.2); color: var(--system-orange); }

    .callout-body h3 {
      font-size: 14.5px;
      font-weight: 700;
      color: #fff;
      margin-bottom: 4px;
    }

    .callout-body p {
      font-size: 13.5px;
      color: var(--label-secondary);
      line-height: 1.5;
    }

    /* Interactive SVG Funnel Diagram */
    .funnel-hero-container {
      background: #090d16;
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 24px 20px;
      margin-bottom: 24px;
      text-align: center;
    }

    .funnel-stages-row {
      display: flex;
      justify-content: space-between;
      align-items: stretch;
      gap: 12px;
      margin-top: 18px;
      flex-wrap: wrap;
    }

    .funnel-stage-tile {
      flex: 1;
      min-width: 190px;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      padding: 16px;
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      text-align: left;
      position: relative;
    }

    .funnel-stage-tile:hover, .funnel-stage-tile.active-stage {
      background: rgba(255, 255, 255, 0.07);
      border-color: var(--system-blue);
      transform: translateY(-2px);
    }

    .stage-step-tag {
      font-size: 11px;
      font-weight: 700;
      color: var(--system-cyan);
      letter-spacing: 0.04em;
      text-transform: uppercase;
      margin-bottom: 6px;
    }

    .stage-tile-name {
      font-size: 15px;
      font-weight: 700;
      color: #fff;
    }

    .stage-tile-num {
      font-size: 26px;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: #fff;
      margin: 4px 0 6px;
    }

    .stage-tile-rate {
      font-size: 12px;
      color: var(--label-secondary);
    }

    .stage-drop-badge {
      display: inline-flex;
      align-items: center;
      gap: 3px;
      font-size: 11px;
      font-weight: 700;
      color: var(--system-red);
      background: rgba(255, 69, 58, 0.1);
      padding: 2px 6px;
      border-radius: 4px;
      margin-top: 8px;
    }

    /* Stage Detail Spotlight Box */
    .spotlight-box {
      background: linear-gradient(135deg, rgba(10, 132, 255, 0.08), rgba(94, 92, 230, 0.08));
      border: 1px solid rgba(10, 132, 255, 0.25);
      border-radius: 14px;
      padding: 18px 22px;
      margin-top: 18px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
      text-align: left;
    }

    .spotlight-left h4 {
      font-size: 15px;
      font-weight: 700;
      color: #fff;
      margin-bottom: 4px;
    }

    .spotlight-left p {
      font-size: 13px;
      color: var(--label-secondary);
    }

    /* Apple-Style Slider Controls */
    .slider-group {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 18px;
      margin-top: 16px;
    }

    .apple-control-card {
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      padding: 18px;
    }

    .control-label-row {
      display: flex;
      justify-content: space-between;
      font-size: 13px;
      font-weight: 600;
      color: var(--label-secondary);
      margin-bottom: 10px;
    }

    .control-val {
      font-weight: 700;
      color: var(--system-cyan);
      font-family: var(--font-mono);
    }

    input[type="range"] {
      -webkit-appearance: none;
      width: 100%;
      height: 6px;
      border-radius: 3px;
      background: rgba(255, 255, 255, 0.12);
      outline: none;
    }

    input[type="range"]::-webkit-slider-thumb {
      -webkit-appearance: none;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: #FFFFFF;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.5);
      cursor: pointer;
      transition: transform 0.1s ease;
    }

    input[type="range"]::-webkit-slider-thumb:hover {
      transform: scale(1.15);
    }

    .calc-hero {
      background: linear-gradient(135deg, rgba(94, 92, 230, 0.15), rgba(10, 132, 255, 0.15));
      border: 1px solid rgba(94, 92, 230, 0.3);
      border-radius: 16px;
      padding: 24px;
      text-align: center;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }

    .calc-num {
      font-size: 48px;
      font-weight: 800;
      letter-spacing: -0.03em;
      color: #fff;
    }

    /* Apple Modern Table */
    .search-bar {
      width: 100%;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--card-border);
      border-radius: 10px;
      padding: 11px 16px;
      color: #fff;
      font-size: 13.5px;
      font-family: inherit;
      outline: none;
      margin-bottom: 16px;
      transition: all 0.2s ease;
    }

    .search-bar:focus {
      border-color: var(--system-blue);
      background: rgba(255, 255, 255, 0.08);
      box-shadow: 0 0 0 3px rgba(10, 132, 255, 0.2);
    }

    .table-responsive {
      overflow-x: auto;
      border-radius: 12px;
    }

    table {
      width: 100%;
      border-collapse: separate;
      border-spacing: 0;
      font-size: 13.5px;
      text-align: left;
    }

    th {
      background: rgba(255, 255, 255, 0.03);
      color: var(--label-secondary);
      font-weight: 600;
      padding: 12px 14px;
      border-bottom: 1px solid var(--separator);
      font-size: 11.5px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    td {
      padding: 13px 14px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.04);
      color: var(--label-primary);
    }

    tr:last-child td { border-bottom: none; }
    tr:hover td { background: rgba(255, 255, 255, 0.025); }

    .mono-code {
      font-family: var(--font-mono);
      color: var(--system-cyan);
      font-size: 12px;
    }

    /* Progress meters */
    .meter-track {
      width: 100%;
      background: rgba(255, 255, 255, 0.06);
      height: 22px;
      border-radius: 6px;
      overflow: hidden;
      position: relative;
    }

    .meter-fill {
      height: 100%;
      display: flex;
      align-items: center;
      padding-left: 8px;
      font-size: 11.5px;
      font-weight: 700;
      color: #fff;
      border-radius: 6px;
    }

    .fill-blue { background: linear-gradient(90deg, #0A84FF, #5E5CE6); }
    .fill-cyan { background: linear-gradient(90deg, #64D2FF, #40C8E0); }
    .fill-orange { background: linear-gradient(90deg, #FF9F0A, #FF453A); }
    .fill-green { background: linear-gradient(90deg, #30D158, #63E6E2); }
    .fill-red { background: linear-gradient(90deg, #FF453A, #FF375F); }

    /* Code Snippet */
    pre code {
      display: block;
      background: #040711;
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 18px;
      font-family: var(--font-mono);
      font-size: 12px;
      color: #d1d5db;
      line-height: 1.6;
      overflow-x: auto;
    }

    footer {
      text-align: center;
      color: var(--label-tertiary);
      font-size: 12.5px;
      padding: 36px 0 20px;
    }

    /* Responsive */
    @media (max-width: 820px) {
      header { padding: 14px 20px; }
      main { padding: 20px 20px 60px; }
      .funnel-stages-row { flex-direction: column; }
    }
  </style>
</head>
<body>

  <!-- Floating Liquid Glass Header -->
  <header>
    <div class="header-inner">
      <div class="brand-section">
        <div class="brand-icon">
          <svg viewBox="0 0 24 24"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>
        </div>
        <div class="brand-text">
          <h1>Indus Weave Textiles</h1>
          <p>PeopleOps Executive &amp; Data Warehouse Intelligence</p>
        </div>
      </div>

      <!-- Segmented Navigation -->
      <nav class="segmented-nav">
        <button class="segmented-item active" onclick="activateTab('funnel')">
          <svg viewBox="0 0 24 24"><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"></polygon></svg>
          Talent Funnel
        </button>
        <button class="segmented-item" onclick="activateTab('cfo')">
          <svg viewBox="0 0 24 24"><line x1="12" y1="1" x2="12" y2="23"></line><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>
          CFO Overtime Audit
        </button>
        <button class="segmented-item" onclick="activateTab('warehouse')">
          <svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="9" y1="21" x2="9" y2="9"></line></svg>
          Workforce Analytics
        </button>
        <button class="segmented-item" onclick="activateTab('dq')">
          <svg viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
          Data Quality (22/22)
        </button>
      </nav>

      <div class="status-badge">
        <span class="status-dot"></span>
        Verified Star Schema
      </div>
    </div>
  </header>

  <main>
    <!-- =========================================================
         TAB 1: RECRUITMENT FUNNEL & CONVERSION (BONUS TASK 3)
         ========================================================= -->
    <div id="tab-funnel" class="tab-pane">
      <div class="widget-grid">
        <div class="widget-card">
          <div class="widget-header">
            <span class="widget-title">Talent Pool</span>
            <span class="widget-pill pill-cyan">100% Inflow</span>
          </div>
          <div class="widget-value">1,400</div>
          <div class="widget-subtitle">Unique candidates across 14 divisions</div>
        </div>

        <div class="widget-card">
          <div class="widget-header">
            <span class="widget-title">Onboarded Hires</span>
            <span class="widget-pill pill-green">5.3% Net Conversion</span>
          </div>
          <div class="widget-value">74</div>
          <div class="widget-subtitle">Accepted offers verified into Core HR</div>
        </div>

        <div class="widget-card">
          <div class="widget-header">
            <span class="widget-title">Median Dwell Time</span>
            <span class="widget-pill pill-cyan">33 Days</span>
          </div>
          <div class="widget-value">33 <span style="font-size:20px; font-weight:600; color:var(--label-secondary);">days</span></div>
          <div class="widget-subtitle">Balanced ~8.5 days per stage progression</div>
        </div>

        <div class="widget-card">
          <div class="widget-header">
            <span class="widget-title">Critical Bottleneck</span>
            <span class="widget-pill pill-red">34.2% Pass</span>
          </div>
          <div class="widget-value" style="font-size:26px; padding-top:6px;">Interview ➔ Offer</div>
          <div class="widget-subtitle">173 candidates disqualified after panel round</div>
        </div>
      </div>

      <!-- Interactive Tapered Funnel Architecture -->
      <div class="apple-panel">
        <div class="panel-headline">
          <h2>Interactive 5-Stage Conversion Funnel</h2>
          <p>Click any stage card below to inspect cohort velocity and drop-off diagnostics</p>
        </div>

        <!-- SVG Funnel Graphic -->
        <div class="funnel-hero-container">
          <svg viewBox="0 0 1000 220" style="width: 100%; max-height: 220px; overflow: visible;">
            <defs>
              <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#0A84FF" stop-opacity="0.8"/>
                <stop offset="100%" stop-color="#5E5CE6" stop-opacity="0.8"/>
              </linearGradient>
              <linearGradient id="grad2" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#5E5CE6" stop-opacity="0.8"/>
                <stop offset="100%" stop-color="#64D2FF" stop-opacity="0.8"/>
              </linearGradient>
              <linearGradient id="grad3" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#64D2FF" stop-opacity="0.8"/>
                <stop offset="100%" stop-color="#FF9F0A" stop-opacity="0.8"/>
              </linearGradient>
              <linearGradient id="grad4" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#FF9F0A" stop-opacity="0.8"/>
                <stop offset="100%" stop-color="#30D158" stop-opacity="0.9"/>
              </linearGradient>
            </defs>

            <!-- Tapered Segments -->
            <!-- Stage 1 to 2 -->
            <polygon points="40,20 220,50 220,170 40,200" fill="url(#grad1)" opacity="0.85"/>
            <!-- Stage 2 to 3 -->
            <polygon points="230,52 420,72 420,148 230,168" fill="url(#grad2)" opacity="0.85"/>
            <!-- Stage 3 to 4 -->
            <polygon points="430,74 660,86 660,134 430,146" fill="url(#grad3)" opacity="0.85"/>
            <!-- Stage 4 to 5 -->
            <polygon points="670,87 940,93 940,127 670,133" fill="url(#grad4)" opacity="0.95"/>

            <!-- Stage Labels inside SVG -->
            <text x="130" y="115" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-weight="800" font-size="15" text-anchor="middle">APPLIED (1,400)</text>
            <text x="325" y="115" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-weight="800" font-size="14" text-anchor="middle">SCREENED (682)</text>
            <text x="545" y="115" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-weight="800" font-size="13" text-anchor="middle">INTERVIEW (263)</text>
            <text x="730" y="115" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-weight="800" font-size="12" text-anchor="middle">OFFER (90)</text>
            <text x="900" y="115" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-weight="800" font-size="13" text-anchor="middle">HIRE (74)</text>

            <!-- Drop connectors -->
            <path d="M 225 170 L 225 205" stroke="#FF453A" stroke-width="2" stroke-dasharray="3,3"/>
            <text x="225" y="218" fill="#FF453A" font-size="11" font-weight="700" text-anchor="middle">-718 (51.3%)</text>

            <path d="M 425 150 L 425 205" stroke="#FF453A" stroke-width="2" stroke-dasharray="3,3"/>
            <text x="425" y="218" fill="#FF453A" font-size="11" font-weight="700" text-anchor="middle">-419 (61.4%)</text>

            <path d="M 665 135 L 665 205" stroke="#FF453A" stroke-width="2" stroke-dasharray="3,3"/>
            <text x="665" y="218" fill="#FF453A" font-size="11" font-weight="700" text-anchor="middle">-173 (65.8%)</text>

            <path d="M 940 128 L 940 205" stroke="#FF9F0A" stroke-width="2" stroke-dasharray="3,3"/>
            <text x="940" y="218" fill="#FF9F0A" font-size="11" font-weight="700" text-anchor="middle">-16 declined</text>
          </svg>

          <!-- Stage Selection Row -->
          <div class="funnel-stages-row">
            <div class="funnel-stage-tile active-stage" onclick="selectStage(1, 'Applied', 1400, 100.0, 0, 'Initial pool of applicants received across 14 divisions.')">
              <div class="stage-step-tag">Step 01</div>
              <div class="stage-tile-name">Applied</div>
              <div class="stage-tile-num">1,400</div>
              <div class="stage-tile-rate">100% Top-Funnel</div>
            </div>

            <div class="funnel-stage-tile" onclick="selectStage(2, 'Screened', 682, 48.7, 718, 'Passed initial qualification & automated credential filter.')">
              <div class="stage-step-tag">Step 02</div>
              <div class="stage-tile-name">Screened</div>
              <div class="stage-tile-num">682</div>
              <div class="stage-tile-rate">48.7% conversion</div>
              <div class="stage-drop-badge">▼ 718 dropped</div>
            </div>

            <div class="funnel-stage-tile" onclick="selectStage(3, 'Interviewed', 263, 18.8, 419, 'Underwent technical & plant manager interviews.')">
              <div class="stage-step-tag">Step 03</div>
              <div class="stage-tile-name">Interviewed</div>
              <div class="stage-tile-num">263</div>
              <div class="stage-tile-rate">38.6% from screen</div>
              <div class="stage-drop-badge">▼ 419 dropped</div>
            </div>

            <div class="funnel-stage-tile" onclick="selectStage(4, 'Offered', 90, 6.4, 173, 'Formal written employment contract extended.')">
              <div class="stage-step-tag">Step 04</div>
              <div class="stage-tile-name">Offered</div>
              <div class="stage-tile-num">90</div>
              <div class="stage-tile-rate">34.2% from interview</div>
              <div class="stage-drop-badge">▼ 173 dropped</div>
            </div>

            <div class="funnel-stage-tile" onclick="selectStage(5, 'Hired', 74, 5.3, 16, 'Offer accepted; biometric ID enrolled and onboarded.')">
              <div class="stage-step-tag" style="color:var(--system-green);">Step 05</div>
              <div class="stage-tile-name" style="color:var(--system-green);">Hired</div>
              <div class="stage-tile-num" style="color:var(--system-green);">74</div>
              <div class="stage-tile-rate">82.2% acceptance</div>
              <div class="stage-drop-badge" style="background:rgba(255,159,10,0.1); color:var(--system-orange);">▼ 16 declined</div>
            </div>
          </div>

          <!-- Dynamic Spotlight Box -->
          <div class="spotlight-box" id="stageSpotlight">
            <div class="spotlight-left">
              <h4 id="spotlightTitle">Stage 1: Applied (1,400 Candidates)</h4>
              <p id="spotlightDesc">Initial candidate pool from April to September 2026 across 14 divisions. Median dwell time 8 days.</p>
            </div>
            <div style="text-align: right;">
              <span class="status-badge" id="spotlightBadge" style="background:rgba(10,132,255,0.12); color:var(--system-blue); border-color:rgba(10,132,255,0.3);">
                Baseline Pool (100%)
              </span>
            </div>
          </div>
        </div>

        <!-- Apple Callout Insights -->
        <div class="apple-callout callout-blue">
          <div class="callout-icon">
            <svg viewBox="0 0 24 24" style="width:16px; height:16px; fill:none; stroke:currentColor; stroke-width:2;"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
          </div>
          <div class="callout-body">
            <h3>Talent Acquisition Diagnostic Verdict</h3>
            <p>
              Candidate sourcing volume is exceptionally healthy (1,400 applicants), but <strong>51.3% are eliminated at resume screening</strong> and <strong>65.8% fail the interview stage</strong>.
              Meanwhile, candidate offer acceptance is remarkably high at <strong>82.2%</strong>. The hiring yield is constrained not by market appetite, but by interview evaluation calibration.
            </p>
          </div>
        </div>
      </div>

      <!-- Interactive What-If Scenario Modeler -->
      <div class="apple-panel">
        <div class="panel-headline">
          <h2>Interactive Pipeline &quot;What-If&quot; Simulator</h2>
          <p>Model the hiring outcome by dynamically tuning milestone conversion rates</p>
        </div>

        <div class="slider-group">
          <div class="apple-control-card">
            <div class="control-label-row">
              <span>Screening Pass Rate</span>
              <span class="control-val" id="lbl-screen">48.7%</span>
            </div>
            <input type="range" id="rng-screen" min="20" max="80" step="0.5" value="48.7" oninput="recalcModel()">
          </div>

          <div class="apple-control-card">
            <div class="control-label-row">
              <span>Screened ➔ Interview</span>
              <span class="control-val" id="lbl-interview">38.6%</span>
            </div>
            <input type="range" id="rng-interview" min="15" max="70" step="0.5" value="38.6" oninput="recalcModel()">
          </div>

          <div class="apple-control-card">
            <div class="control-label-row">
              <span>Interview ➔ Offer</span>
              <span class="control-val" id="lbl-offer">34.2%</span>
            </div>
            <input type="range" id="rng-offer" min="15" max="65" step="0.5" value="34.2" oninput="recalcModel()">
          </div>

          <div class="apple-control-card">
            <div class="control-label-row">
              <span>Offer Acceptance</span>
              <span class="control-val" id="lbl-accept">82.2%</span>
            </div>
            <input type="range" id="rng-accept" min="50" max="100" step="0.5" value="82.2" oninput="recalcModel()">
          </div>

          <div class="calc-hero">
            <span style="font-size:12px; font-weight:700; color:var(--label-secondary); text-transform:uppercase; letter-spacing:0.06em;">Simulated Hires</span>
            <div class="calc-num" id="calc-result">74</div>
            <span id="calc-delta" style="font-size:12.5px; font-weight:600; color:var(--label-secondary); margin-top:4px;">Matches Case Study Baseline</span>
          </div>
        </div>
      </div>

      <!-- Department Table -->
      <div class="apple-panel">
        <div class="panel-headline">
          <h2>Departmental Talent Inflow &amp; Hire Rates</h2>
          <p>Filter across 14 operating divisions</p>
        </div>

        <input type="text" id="deptSearch" class="search-bar" placeholder="Search department name or code (e.g. Cutting, Spinning, D21)..." oninput="filterDepts()">

        <div class="table-responsive">
          <table id="tblDepts">
            <thead>
              <tr>
                <th>Code</th>
                <th>Division</th>
                <th>Applications</th>
                <th>Hired</th>
                <th>Rejected</th>
                <th>Declined</th>
                <th>Hire Rate</th>
                <th>Conversion Share</th>
              </tr>
            </thead>
            <tbody>
              <tr><td class="mono-code">D21</td><td style="font-weight:600;">Cutting</td><td>180</td><td style="color:var(--system-green); font-weight:700;">12</td><td>167</td><td>1</td><td><span class="widget-pill pill-green">6.7%</span></td><td><div class="meter-track" style="width:110px;"><div class="meter-fill fill-green" style="width:78%;">16%</div></div></td></tr>
              <tr><td class="mono-code">D08</td><td style="font-weight:600;">Spinning</td><td>162</td><td style="color:var(--system-green); font-weight:700;">14</td><td>144</td><td>4</td><td><span class="widget-pill pill-green">8.6%</span></td><td><div class="meter-track" style="width:110px;"><div class="meter-fill fill-green" style="width:95%;">19%</div></div></td></tr>
              <tr><td class="mono-code">D23</td><td style="font-weight:600;">Maintenance</td><td>156</td><td style="color:var(--system-green); font-weight:700;">6</td><td>148</td><td>2</td><td><span class="widget-pill pill-cyan">3.8%</span></td><td><div class="meter-track" style="width:110px;"><div class="meter-fill fill-blue" style="width:42%;">8%</div></div></td></tr>
              <tr><td class="mono-code">D15</td><td style="font-weight:600;">Finishing</td><td>143</td><td style="color:var(--system-green); font-weight:700;">4</td><td>136</td><td>3</td><td><span class="widget-pill pill-cyan">2.8%</span></td><td><div class="meter-track" style="width:110px;"><div class="meter-fill fill-blue" style="width:28%;">5%</div></div></td></tr>
              <tr><td class="mono-code">D14</td><td style="font-weight:600;">Dyeing</td><td>121</td><td style="color:var(--system-green); font-weight:700;">6</td><td>114</td><td>1</td><td><span class="widget-pill pill-cyan">5.0%</span></td><td><div class="meter-track" style="width:110px;"><div class="meter-fill fill-blue" style="width:42%;">8%</div></div></td></tr>
              <tr><td class="mono-code">D22</td><td style="font-weight:600;">Packing</td><td>105</td><td style="color:var(--system-green); font-weight:700;">8</td><td>96</td><td>1</td><td><span class="widget-pill pill-green">7.6%</span></td><td><div class="meter-track" style="width:110px;"><div class="meter-fill fill-green" style="width:55%;">11%</div></div></td></tr>
              <tr><td class="mono-code">D02</td><td style="font-weight:600;">Finance</td><td>96</td><td style="color:var(--system-green); font-weight:700;">6</td><td>90</td><td>0</td><td><span class="widget-pill pill-green">6.2%</span></td><td><div class="meter-track" style="width:110px;"><div class="meter-fill fill-green" style="width:42%;">8%</div></div></td></tr>
              <tr><td class="mono-code">D25</td><td style="font-weight:600;">Warehouse</td><td>91</td><td style="color:var(--system-green); font-weight:700;">3</td><td>87</td><td>1</td><td><span class="widget-pill pill-cyan">3.3%</span></td><td><div class="meter-track" style="width:110px;"><div class="meter-fill fill-blue" style="width:21%;">4%</div></div></td></tr>
              <tr><td class="mono-code">D18</td><td style="font-weight:600;">Warehouse</td><td>89</td><td style="color:var(--system-green); font-weight:700;">3</td><td>84</td><td>2</td><td><span class="widget-pill pill-cyan">3.4%</span></td><td><div class="meter-track" style="width:110px;"><div class="meter-fill fill-blue" style="width:21%;">4%</div></div></td></tr>
              <tr><td class="mono-code">D05</td><td style="font-weight:600;">Sales &amp; Marketing</td><td>85</td><td style="color:var(--system-green); font-weight:700;">4</td><td>80</td><td>1</td><td><span class="widget-pill pill-cyan">4.7%</span></td><td><div class="meter-track" style="width:110px;"><div class="meter-fill fill-blue" style="width:28%;">5%</div></div></td></tr>
              <tr><td class="mono-code">D20</td><td style="font-weight:600;">Stitching</td><td>50</td><td style="color:var(--system-green); font-weight:700;">3</td><td>47</td><td>0</td><td><span class="widget-pill pill-green">6.0%</span></td><td><div class="meter-track" style="width:110px;"><div class="meter-fill fill-green" style="width:21%;">4%</div></div></td></tr>
              <tr><td class="mono-code">D11</td><td style="font-weight:600;">Quality Control</td><td>42</td><td style="color:var(--system-green); font-weight:700;">2</td><td>40</td><td>0</td><td><span class="widget-pill pill-cyan">4.8%</span></td><td><div class="meter-track" style="width:110px;"><div class="meter-fill fill-blue" style="width:14%;">3%</div></div></td></tr>
              <tr><td class="mono-code">D16</td><td style="font-weight:600;">Maintenance</td><td>42</td><td style="color:var(--system-green); font-weight:700;">3</td><td>39</td><td>0</td><td><span class="widget-pill pill-green">7.1%</span></td><td><div class="meter-track" style="width:110px;"><div class="meter-fill fill-green" style="width:21%;">4%</div></div></td></tr>
              <tr><td class="mono-code">D06</td><td style="font-weight:600;">Administration</td><td>38</td><td style="color:var(--system-red); font-weight:700;">0</td><td>38</td><td>0</td><td><span class="widget-pill pill-red">0.0%</span></td><td><div class="meter-track" style="width:110px;"><div class="meter-fill fill-red" style="width:0%;">0%</div></div></td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- =========================================================
         TAB 2: CFO OVERTIME LEAKAGE AUDIT (CASE CORE)
         ========================================================= -->
    <div id="tab-cfo" class="tab-pane" style="display:none;">
      <div class="apple-callout callout-red">
        <div class="callout-icon">
          <svg viewBox="0 0 24 24" style="width:16px; height:16px; fill:none; stroke:currentColor; stroke-width:2;"><polygon points="7.86 2 16.14 2 22 7.86 22 16.14 16.14 22 7.86 22 2 16.14 2 7.86 7.86 2"></polygon><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
        </div>
        <div class="callout-body">
          <h3>The CFO&apos;s Core Question Answered: Why is Overtime Escalating?</h3>
          <p>
            The company&apos;s overtime bill rose by <strong>+23.5% (PKR 2.81M to 3.48M)</strong> over six months while headcount actually declined from 1,199 to 1,176.
            The audit reveals that <strong>payroll disburses overtime from manager-signed OT slips rather than biometric clock punches</strong>.
            Over the six months, <strong>36,402 hours were paid against only 29,116 hours physically worked</strong> — an unearned leakage of <strong>7,286 overtime hours</strong> and PKR 3.78M in ghost payroll.
          </p>
        </div>
      </div>

      <div class="widget-grid">
        <div class="widget-card">
          <div class="widget-header">
            <span class="widget-title">Overtime Gap</span>
            <span class="widget-pill pill-red">+7,286 hrs</span>
          </div>
          <div class="widget-value">36,402 vs 29,116</div>
          <div class="widget-subtitle">Paid Overtime vs Biometrically Clocked OT</div>
        </div>

        <div class="widget-card">
          <div class="widget-header">
            <span class="widget-title">Monthly Spend Surge</span>
            <span class="widget-pill pill-red">+23.5%</span>
          </div>
          <div class="widget-value">PKR 3.48M</div>
          <div class="widget-subtitle">Climbed from PKR 2.81M (Apr) to 3.48M (Sep)</div>
        </div>

        <div class="widget-card">
          <div class="widget-header">
            <span class="widget-title">Unearned Approvals</span>
            <span class="widget-pill pill-orange">3,687 cases</span>
          </div>
          <div class="widget-value">18.7%</div>
          <div class="widget-subtitle">Approved OT with 0 computed biometric hours</div>
        </div>

        <div class="widget-card">
          <div class="widget-header">
            <span class="widget-title">Post-Separation Pay</span>
            <span class="widget-pill pill-red">15 Staff</span>
          </div>
          <div class="widget-value">PKR 3.78M</div>
          <div class="widget-subtitle">52 paychecks issued after separation date</div>
        </div>
      </div>

      <!-- Findings Breakdown -->
      <div class="apple-panel">
        <div class="panel-headline">
          <h2>Top 3 Strategic Findings for CFO 5-Minute Demo</h2>
          <span class="status-badge" style="background:rgba(10,132,255,0.12); color:var(--system-blue); border-color:rgba(10,132,255,0.25);">
            Executive Summary
          </span>
        </div>

        <div style="display:grid; gap:16px;">
          <div style="background:rgba(255,255,255,0.03); border:1px solid var(--card-border); border-radius:14px; padding:20px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <h3 style="font-size:15px; color:#fff; font-weight:700;">1. Paid Overtime Decoupled From Worked Overtime</h3>
              <span class="widget-pill pill-red">Gap Doubled</span>
            </div>
            <p style="font-size:13.5px; color:var(--label-secondary); line-height:1.6;">
              In April, the monthly discrepancy was 856 hours. By September, it widened to 1,782 hours. Physical biometric overtime remained flat (~4,800 hrs/mo), yet managers authorized ever-increasing overtime payouts.
              <strong>Faisalabad Plant generates 4,588.5 excess hours alone (63% of the company total).</strong>
              <br><strong style="color:var(--system-cyan);">Action:</strong> Make biometric punch reconciliation mandatory before overtime payroll release.
            </p>
          </div>

          <div style="background:rgba(255,255,255,0.03); border:1px solid var(--card-border); border-radius:14px; padding:20px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <h3 style="font-size:15px; color:#fff; font-weight:700;">2. Overtime Authorized on Zero-Work Days</h3>
              <span class="widget-pill pill-orange">18.7% of Approvals</span>
            </div>
            <p style="font-size:13.5px; color:var(--label-secondary); line-height:1.6;">
              Out of 19,666 approved overtime requests, 3,687 occurred on days where the employee worked zero overtime hours (581 Present shifts leaving on time, plus &gt;3,000 on Absent, Leave, or Weekly Off days).
              <br><strong style="color:var(--system-cyan);">Action:</strong> Enforce ERP rule blocking overtime requests on non-qualifying biometric punch records.
            </p>
          </div>

          <div style="background:rgba(255,255,255,0.03); border:1px solid var(--card-border); border-radius:14px; padding:20px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <h3 style="font-size:15px; color:#fff; font-weight:700;">3. Ghost Payroll: Payments Continued Post-Separation</h3>
              <span class="widget-pill pill-red">PKR 3.78M Leakage</span>
            </div>
            <p style="font-size:13.5px; color:var(--label-secondary); line-height:1.6;">
              15 employees continued receiving monthly payroll after their official separation date (52 paychecks).
              <strong>Umair Baloch (E10471)</strong> separated on 23 April 2026, yet received monthly paychecks throughout May, June, July, August, and September totaling PKR 682,100 with zero days worked.
              <br><strong style="color:var(--system-cyan);">Action:</strong> Integrate HR separation dates with automated payroll termination.
            </p>
          </div>
        </div>
      </div>

      <!-- Monthly Trend -->
      <div class="apple-panel">
        <div class="panel-headline">
          <h2>Monthly Trajectory: Physical Hours vs Paid Overtime</h2>
          <p>Evidence from Q5 &amp; fact_payroll_line</p>
        </div>
        <div class="table-responsive">
          <table>
            <thead>
              <tr>
                <th>Month</th>
                <th>Physical Worked</th>
                <th>Approved Slips</th>
                <th>Paid Units</th>
                <th>Monthly Leakage</th>
                <th>Gross OT Spend</th>
                <th>Variance %</th>
              </tr>
            </thead>
            <tbody>
              <tr><td style="font-weight:600;">2026-04</td><td>4,622.0 hrs</td><td>5,525.5 hrs</td><td style="font-weight:700; color:#fff;">5,525.5 hrs</td><td style="color:var(--system-red); font-weight:700;">+856.0 hrs</td><td>PKR 2.81M</td><td><span class="widget-pill pill-orange">+18.5%</span></td></tr>
              <tr><td style="font-weight:600;">2026-05</td><td>4,972.0 hrs</td><td>5,806.5 hrs</td><td style="font-weight:700; color:#fff;">5,806.5 hrs</td><td style="color:var(--system-red); font-weight:700;">+834.5 hrs</td><td>PKR 2.86M</td><td><span class="widget-pill pill-orange">+16.8%</span></td></tr>
              <tr><td style="font-weight:600;">2026-06</td><td>4,795.5 hrs</td><td>5,889.0 hrs</td><td style="font-weight:700; color:#fff;">5,889.0 hrs</td><td style="color:var(--system-red); font-weight:700;">+1,093.5 hrs</td><td>PKR 2.93M</td><td><span class="widget-pill pill-orange">+22.8%</span></td></tr>
              <tr><td style="font-weight:600;">2026-07</td><td>4,794.5 hrs</td><td>6,249.0 hrs</td><td style="font-weight:700; color:#fff;">6,249.0 hrs</td><td style="color:var(--system-red); font-weight:700;">+1,454.5 hrs</td><td>PKR 3.37M</td><td><span class="widget-pill pill-red">+30.3%</span></td></tr>
              <tr><td style="font-weight:600;">2026-08</td><td>5,014.0 hrs</td><td>6,513.0 hrs</td><td style="font-weight:700; color:#fff;">6,513.0 hrs</td><td style="color:var(--system-red); font-weight:700;">+1,499.0 hrs</td><td>PKR 3.57M</td><td><span class="widget-pill pill-red">+29.9%</span></td></tr>
              <tr><td style="font-weight:600;">2026-09</td><td>4,636.5 hrs</td><td>6,418.5 hrs</td><td style="font-weight:700; color:#fff;">6,418.5 hrs</td><td style="color:var(--system-red); font-weight:700;">+1,782.0 hrs</td><td>PKR 3.48M</td><td><span class="widget-pill pill-red">+38.4%</span></td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- =========================================================
         TAB 3: WORKFORCE & ATTENDANCE ANALYTICS (Q1-Q10)
         ========================================================= -->
    <div id="tab-warehouse" class="tab-pane" style="display:none;">
      <div class="widget-grid">
        <div class="widget-card">
          <div class="widget-header">
            <span class="widget-title">Active Roster</span>
            <span class="widget-pill pill-cyan">Sep Snapshot</span>
          </div>
          <div class="widget-value">1,172</div>
          <div class="widget-subtitle">Falling from 1,189 in April (-1.4%)</div>
        </div>

        <div class="widget-card">
          <div class="widget-header">
            <span class="widget-title">Peak Plant Absence</span>
            <span class="widget-pill pill-red">5.12% Rate</span>
          </div>
          <div class="widget-value">Faisalabad</div>
          <div class="widget-subtitle">2,801 unexcused absence days</div>
        </div>

        <div class="widget-card">
          <div class="widget-header">
            <span class="widget-title">Chronic Late Arrivals</span>
            <span class="widget-pill pill-orange">Top: 53 shifts</span>
          </div>
          <div class="widget-value">Usman Gill</div>
          <div class="widget-subtitle">D21 Cutting, Faisalabad (2,420 min late)</div>
        </div>

        <div class="widget-card">
          <div class="widget-header">
            <span class="widget-title">Leave Exhaustion</span>
            <span class="widget-pill pill-red">20 Employees</span>
          </div>
          <div class="widget-value">20 Staff</div>
          <div class="widget-subtitle">Exceeded 12-month annual quota in 6 mo</div>
        </div>
      </div>

      <!-- Absenteeism & Headcount Grid -->
      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:20px; margin-bottom:26px;">
        <div class="apple-panel" style="margin:0;">
          <div class="panel-headline">
            <h2>Plant Absenteeism Comparison (Q3)</h2>
          </div>
          <div class="table-responsive">
            <table>
              <thead><tr><th>Plant</th><th>Absences</th><th>Scheduled</th><th>Absence Rate</th></tr></thead>
              <tbody>
                <tr><td style="font-weight:600;">Faisalabad Plant</td><td>2,801</td><td>54,720</td><td><span class="widget-pill pill-red">5.12%</span></td></tr>
                <tr><td style="font-weight:600;">SITE Plant</td><td>1,768</td><td>49,024</td><td><span class="widget-pill pill-orange">3.61%</span></td></tr>
                <tr><td style="font-weight:600;">Korangi Plant</td><td>1,863</td><td>54,792</td><td><span class="widget-pill pill-orange">3.40%</span></td></tr>
                <tr><td style="font-weight:600;">Head Office</td><td>435</td><td>17,212</td><td><span class="widget-pill pill-cyan">2.53%</span></td></tr>
              </tbody>
            </table>
          </div>
        </div>

        <div class="apple-panel" style="margin:0;">
          <div class="panel-headline">
            <h2>Headcount Stability Trend (Q1)</h2>
          </div>
          <div class="table-responsive">
            <table>
              <thead><tr><th>Month</th><th>Count</th><th>Progressive Trajectory</th></tr></thead>
              <tbody>
                <tr><td style="font-weight:600;">2026-04</td><td style="font-weight:700;">1,189</td><td><div class="meter-track" style="width:130px;"><div class="meter-fill fill-blue" style="width:100%;"></div></div></td></tr>
                <tr><td style="font-weight:600;">2026-05</td><td style="font-weight:700;">1,186</td><td><div class="meter-track" style="width:130px;"><div class="meter-fill fill-blue" style="width:99.7%;"></div></div></td></tr>
                <tr><td style="font-weight:600;">2026-06</td><td style="font-weight:700;">1,183</td><td><div class="meter-track" style="width:130px;"><div class="meter-fill fill-blue" style="width:99.4%;"></div></div></td></tr>
                <tr><td style="font-weight:600;">2026-07</td><td style="font-weight:700;">1,172</td><td><div class="meter-track" style="width:130px;"><div class="meter-fill fill-blue" style="width:98.5%;"></div></div></td></tr>
                <tr><td style="font-weight:600;">2026-08</td><td style="font-weight:700;">1,176</td><td><div class="meter-track" style="width:130px;"><div class="meter-fill fill-blue" style="width:98.9%;"></div></div></td></tr>
                <tr><td style="font-weight:600;">2026-09</td><td style="font-weight:700;">1,172</td><td><div class="meter-track" style="width:130px;"><div class="meter-fill fill-blue" style="width:98.5%;"></div></div></td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- =========================================================
         TAB 4: STAR SCHEMA & DATA QUALITY (STAGE 4 & 6)
         ========================================================= -->
    <div id="tab-dq" class="tab-pane" style="display:none;">
      <div class="widget-grid">
        <div class="widget-card">
          <div class="widget-header">
            <span class="widget-title">Automated Checks</span>
            <span class="widget-pill pill-green">22 / 22 PASS</span>
          </div>
          <div class="widget-value" style="color:var(--system-green);">100% Valid</div>
          <div class="widget-subtitle">Stored and checked in dq_results table</div>
        </div>

        <div class="widget-card">
          <div class="widget-header">
            <span class="widget-title">Raw Records Ingested</span>
            <span class="widget-pill pill-cyan">Exact Match</span>
          </div>
          <div class="widget-value">472,907</div>
          <div class="widget-subtitle">12 source files untouched with row hashes</div>
        </div>

        <div class="widget-card">
          <div class="widget-header">
            <span class="widget-title">Reconciliation Accuracy</span>
            <span class="widget-pill pill-green">Zero Loss</span>
          </div>
          <div class="widget-value">100.0%</div>
          <div class="widget-subtitle">Raw = Staged (449,770) + Rejected (23,137)</div>
        </div>

        <div class="widget-card">
          <div class="widget-header">
            <span class="widget-title">Hardware Defect Fix</span>
            <span class="widget-pill pill-orange">Rule 11</span>
          </div>
          <div class="widget-value">48,146 rows</div>
          <div class="widget-subtitle">DEV-SITE-01 60 min fast clock corrected</div>
        </div>
      </div>

      <!-- DDL Star Schema Architecture -->
      <div class="apple-panel">
        <div class="panel-headline">
          <h2>Production Star Schema Schema (Stage 4)</h2>
          <p>Enforced PK/FK dimensional model in SQLite (indus_weave.db)</p>
        </div>
        <pre><code>-- DIMENSIONS
dim_employee (employee_key [PK], emp_id, full_name, hire_date, separation_date, dept_id, designation, grade, basic_salary, valid_from, valid_to, is_current) [SCD Type 2]
dim_department (dept_id [PK], dept_name, plant, cost_center)
dim_shift (shift_code [PK], name, start_time, end_time, crosses_midnight, grace_minutes)
dim_date (date_key [PK], date, year, month, day, day_of_week, is_weekend, is_holiday)

-- FACTS
fact_attendance_daily (attendance_key [PK], emp_id, work_date, employee_key [FK], dept_id [FK], shift_code [FK], first_punch, last_punch, worked_hours, overtime_hours, late_minutes, early_minutes, status)
fact_leave_day (leave_day_key [PK], request_id, emp_id, leave_date, leave_type)
fact_overtime_approved (ot_key [PK], request_id, emp_id, ot_date, requested_hours, approved_hours, approver_id)
fact_payroll_line (line_id [PK], payroll_month, emp_id, employee_key [FK], dept_id [FK], component, component_type, units, amount)</code></pre>
      </div>
    </div>

    <footer>
      Indus Weave Textiles • PeopleOps Data Hackathon 2026 • Apple Human Interface Guidelines Design
    </footer>
  </main>

  <script>
    // Tab Switching
    function activateTab(tabId) {
      document.querySelectorAll('.tab-pane').forEach(el => el.style.display = 'none');
      document.querySelectorAll('.segmented-item').forEach(btn => btn.classList.remove('active'));
      
      const target = document.getElementById('tab-' + tabId);
      if (target) target.style.display = 'block';

      const clickedBtn = Array.from(document.querySelectorAll('.segmented-item')).find(b => b.getAttribute('onclick').includes(tabId));
      if (clickedBtn) clickedBtn.classList.add('active');
    }

    // Dynamic Funnel Stage Selector
    function selectStage(num, name, count, pct, drop, desc) {
      document.querySelectorAll('.funnel-stage-tile').forEach(t => t.classList.remove('active-stage'));
      event.currentTarget.classList.add('active-stage');

      document.getElementById('spotlightTitle').textContent = `Stage ${num}: ${name} (${count.toLocaleString()} Candidates)`;
      document.getElementById('spotlightDesc').textContent = `${desc} Conversion rate: ${pct}% of total inflow.`;

      const badge = document.getElementById('spotlightBadge');
      if (drop > 0) {
        badge.textContent = `Drop-off: -${drop.toLocaleString()} candidates`;
        badge.style.background = 'rgba(255,69,58,0.12)';
        badge.style.color = '#FF453A';
        badge.style.borderColor = 'rgba(255,69,58,0.3)';
      } else {
        badge.textContent = 'Baseline Inflow (100%)';
        badge.style.background = 'rgba(10,132,255,0.12)';
        badge.style.color = '#0A84FF';
        badge.style.borderColor = 'rgba(10,132,255,0.3)';
      }
    }

    // Interactive Recalculation Model
    function recalcModel() {
      const scr = parseFloat(document.getElementById('rng-screen').value);
      const intv = parseFloat(document.getElementById('rng-interview').value);
      const off = parseFloat(document.getElementById('rng-offer').value);
      const acc = parseFloat(document.getElementById('rng-accept').value);

      document.getElementById('lbl-screen').textContent = scr.toFixed(1) + '%';
      document.getElementById('lbl-interview').textContent = intv.toFixed(1) + '%';
      document.getElementById('lbl-offer').textContent = off.toFixed(1) + '%';
      document.getElementById('lbl-accept').textContent = acc.toFixed(1) + '%';

      const applied = 1400;
      const screened = applied * (scr / 100);
      const interviewed = screened * (intv / 100);
      const offered = interviewed * (off / 100);
      const hires = Math.round(offered * (acc / 100));

      document.getElementById('calc-result').textContent = hires;
      const delta = hires - 74;
      const deltaEl = document.getElementById('calc-delta');
      if (delta > 0) {
        deltaEl.textContent = `+${delta} Hires vs Baseline (+${((delta/74)*100).toFixed(0)}%)`;
        deltaEl.style.color = 'var(--system-green)';
      } else if (delta < 0) {
        deltaEl.textContent = `${delta} Hires vs Baseline (${((delta/74)*100).toFixed(0)}%)`;
        deltaEl.style.color = 'var(--system-red)';
      } else {
        deltaEl.textContent = 'Matches Case Study Baseline';
        deltaEl.style.color = 'var(--label-secondary)';
      }
    }

    // Department Filter
    function filterDepts() {
      const q = document.getElementById('deptSearch').value.toLowerCase();
      document.querySelectorAll('#tblDepts tbody tr').forEach(tr => {
        tr.style.display = tr.textContent.toLowerCase().includes(q) ? '' : 'none';
      });
    }
  </script>
</body>
</html>
"""

def main():
    OUT_FILE.write_text(HTML, encoding="utf-8")
    print(f"Generated Apple-styled {OUT_FILE} ({len(HTML)} bytes)")

if __name__ == "__main__":
    main()
