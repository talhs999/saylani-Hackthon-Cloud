"""Generates the comprehensive, world-class standalone dashboard.html.
Includes:
- Recruitment Funnel & Candidate Journey (Bonus 3)
- CFO Overtime Leakage Audit (Case Core)
- Workforce & Attendance Analytics (Q1-Q10)
- Star Schema Architecture & 22/22 Data Quality Suite (Stage 6)
"""

from pathlib import Path

OUT_FILE = Path(__file__).resolve().parent / "dashboard.html"

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Indus Weave Textiles — PeopleOps Executive Suite &amp; Funnel Intelligence</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-base: #060913;
      --bg-surface: #0c1222;
      --bg-card: rgba(15, 23, 42, 0.75);
      --bg-card-hover: rgba(30, 41, 59, 0.85);
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-accent: rgba(99, 102, 241, 0.35);
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --primary: #6366f1;
      --primary-light: #818cf8;
      --cyan: #06b6d4;
      --emerald: #10b981;
      --amber: #f59e0b;
      --rose: #f43f5e;
      --font-sans: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: var(--font-sans);
      background-color: var(--bg-base);
      color: var(--text-main);
      line-height: 1.55;
      min-height: 100vh;
      background-image: 
        radial-gradient(circle at 10% 10%, rgba(99, 102, 241, 0.15) 0px, transparent 45%),
        radial-gradient(circle at 90% 90%, rgba(6, 182, 212, 0.12) 0px, transparent 45%),
        radial-gradient(circle at 50% 50%, rgba(15, 23, 42, 0.6) 0px, transparent 100%);
      background-attachment: fixed;
    }

    /* Header */
    header {
      background: rgba(12, 18, 34, 0.85);
      backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border-subtle);
      padding: 20px 32px;
      position: sticky;
      top: 0;
      z-index: 50;
    }

    .header-content {
      max-width: 1360px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
    }

    .brand-area {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .brand-logo {
      width: 44px;
      height: 44px;
      border-radius: 12px;
      background: linear-gradient(135deg, #4f46e5, #06b6d4);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 20px;
      color: #fff;
      box-shadow: 0 4px 18px rgba(79, 70, 229, 0.45);
    }

    .brand-title h1 {
      font-size: 22px;
      font-weight: 800;
      letter-spacing: -0.02em;
      background: linear-gradient(to right, #ffffff, #cbd5e1);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .brand-title p {
      font-size: 13px;
      color: var(--text-muted);
    }

    .header-badges {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }

    .pill-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 600;
    }

    .pill-success {
      background: rgba(16, 185, 129, 0.12);
      color: #34d399;
      border: 1px solid rgba(16, 185, 129, 0.25);
    }

    .pill-info {
      background: rgba(6, 182, 212, 0.12);
      color: #38bdf8;
      border: 1px solid rgba(6, 182, 212, 0.25);
    }

    .dot-pulse {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: #10b981;
      box-shadow: 0 0 10px #10b981;
    }

    /* Tab Navigation */
    .nav-tabs {
      max-width: 1360px;
      margin: 18px auto 0;
      padding: 0 32px;
      display: flex;
      gap: 12px;
      border-bottom: 1px solid var(--border-subtle);
      overflow-x: auto;
    }

    .tab-button {
      background: transparent;
      color: var(--text-muted);
      border: none;
      padding: 12px 18px;
      font-size: 14px;
      font-weight: 600;
      cursor: pointer;
      border-bottom: 2px solid transparent;
      transition: all 0.2s ease;
      white-space: nowrap;
      display: flex;
      align-items: center;
      gap: 8px;
      font-family: inherit;
    }

    .tab-button:hover {
      color: var(--text-main);
    }

    .tab-button.active {
      color: #818cf8;
      border-bottom-color: #6366f1;
    }

    /* Main Container */
    main {
      max-width: 1360px;
      margin: 0 auto;
      padding: 28px 32px 64px;
    }

    /* KPI Grid */
    .kpi-row {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 16px;
      margin-bottom: 24px;
    }

    .kpi-box {
      background: var(--bg-card);
      backdrop-filter: blur(16px);
      border: 1px solid var(--border-subtle);
      border-radius: 14px;
      padding: 20px;
      transition: all 0.25s ease;
      position: relative;
      overflow: hidden;
    }

    .kpi-box:hover {
      transform: translateY(-3px);
      border-color: var(--border-accent);
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4);
    }

    .kpi-box::before {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 2px;
      background: linear-gradient(90deg, transparent, var(--primary), transparent);
      opacity: 0;
      transition: opacity 0.25s ease;
    }

    .kpi-box:hover::before { opacity: 1; }

    .kpi-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 12.5px;
      font-weight: 600;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-bottom: 8px;
    }

    .kpi-number {
      font-size: 32px;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: #fff;
      margin-bottom: 6px;
    }

    .kpi-caption {
      font-size: 13px;
      color: var(--text-dim);
    }

    .tag-badge {
      font-size: 11px;
      padding: 3px 8px;
      border-radius: 6px;
      font-weight: 700;
    }

    .tag-rose { background: rgba(244, 63, 94, 0.15); color: #fb7185; border: 1px solid rgba(244, 63, 94, 0.3); }
    .tag-amber { background: rgba(245, 158, 11, 0.15); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.3); }
    .tag-emerald { background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3); }
    .tag-cyan { background: rgba(6, 182, 212, 0.15); color: #38bdf8; border: 1px solid rgba(6, 182, 212, 0.3); }

    /* Glass Panels */
    .glass-panel {
      background: var(--bg-card);
      backdrop-filter: blur(16px);
      border: 1px solid var(--border-subtle);
      border-radius: 14px;
      padding: 24px;
      margin-bottom: 24px;
    }

    .glass-panel-title {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 18px;
      flex-wrap: wrap;
      gap: 10px;
    }

    .glass-panel-title h2 {
      font-size: 18px;
      font-weight: 700;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .glass-panel-title p {
      font-size: 13px;
      color: var(--text-muted);
    }

    /* Callout Card */
    .callout-box {
      border-radius: 12px;
      padding: 20px;
      margin-bottom: 24px;
      border-left: 4px solid;
    }

    .callout-rose { background: rgba(244, 63, 94, 0.08); border-color: #f43f5e; }
    .callout-amber { background: rgba(245, 158, 11, 0.08); border-color: #f59e0b; }
    .callout-cyan { background: rgba(6, 182, 212, 0.08); border-color: #06b6d4; }

    .callout-box h3 {
      font-size: 16px;
      font-weight: 700;
      color: #fff;
      margin-bottom: 6px;
    }

    .callout-box p {
      font-size: 14px;
      color: var(--text-muted);
      line-height: 1.6;
    }

    /* Funnel Step Cards & Pipeline */
    .funnel-pipeline {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
      gap: 14px;
      margin: 20px 0;
      position: relative;
    }

    .stage-card {
      background: rgba(12, 18, 34, 0.8);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 18px;
      position: relative;
      transition: all 0.2s ease;
    }

    .stage-card:hover {
      border-color: var(--border-accent);
      transform: translateY(-2px);
    }

    .stage-card-num {
      width: 24px;
      height: 24px;
      border-radius: 6px;
      background: rgba(99, 102, 241, 0.2);
      color: #818cf8;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 12px;
      font-weight: 700;
      margin-bottom: 10px;
    }

    .stage-card-name {
      font-size: 16px;
      font-weight: 700;
      color: #fff;
    }

    .stage-card-count {
      font-size: 26px;
      font-weight: 800;
      color: #fff;
      margin: 6px 0;
    }

    .stage-card-stats {
      font-size: 12px;
      color: var(--text-muted);
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .drop-indicator {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      font-size: 11.5px;
      font-weight: 600;
      color: #fb7185;
      margin-top: 6px;
    }

    /* Progress and Bars */
    .progress-track {
      width: 100%;
      background: rgba(255, 255, 255, 0.05);
      height: 32px;
      border-radius: 8px;
      overflow: hidden;
      margin: 8px 0;
      position: relative;
    }

    .progress-bar {
      height: 100%;
      display: flex;
      align-items: center;
      padding: 0 12px;
      font-weight: 700;
      font-size: 12px;
      color: #fff;
      transition: width 0.6s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .bar-violet { background: linear-gradient(90deg, #4f46e5, #6366f1); }
    .bar-teal { background: linear-gradient(90deg, #0891b2, #06b6d4); }
    .bar-green { background: linear-gradient(90deg, #059669, #10b981); }
    .bar-red { background: linear-gradient(90deg, #e11d48, #f43f5e); }
    .bar-orange { background: linear-gradient(90deg, #d97706, #f59e0b); }

    /* Tables */
    .table-container {
      overflow-x: auto;
      border-radius: 8px;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 13.5px;
      text-align: left;
    }

    th {
      background: rgba(255, 255, 255, 0.03);
      color: var(--text-muted);
      font-weight: 600;
      padding: 12px 14px;
      border-bottom: 1px solid var(--border-subtle);
      text-transform: uppercase;
      font-size: 11.5px;
      letter-spacing: 0.03em;
    }

    td {
      padding: 12px 14px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.04);
      color: var(--text-main);
    }

    tr:hover td {
      background: rgba(255, 255, 255, 0.02);
    }

    /* Inputs */
    .filter-input {
      width: 100%;
      background: rgba(12, 18, 34, 0.85);
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      padding: 12px 16px;
      color: #fff;
      font-family: inherit;
      font-size: 14px;
      outline: none;
      transition: all 0.2s ease;
      margin-bottom: 14px;
    }

    .filter-input:focus {
      border-color: #6366f1;
      box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.25);
    }

    /* Simulator Sliders */
    .simulator-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 18px;
      margin-top: 14px;
    }

    .sim-card {
      background: rgba(12, 18, 34, 0.8);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 16px;
    }

    .sim-card label {
      display: flex;
      justify-content: space-between;
      font-size: 13px;
      font-weight: 600;
      color: var(--text-muted);
      margin-bottom: 8px;
    }

    .sim-card input[type="range"] {
      width: 100%;
      accent-color: #6366f1;
    }

    .sim-result-box {
      background: linear-gradient(135deg, rgba(99, 102, 241, 0.15), rgba(6, 182, 212, 0.15));
      border: 1px solid var(--border-accent);
      border-radius: 12px;
      padding: 20px;
      text-align: center;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }

    .sim-result-val {
      font-size: 44px;
      font-weight: 800;
      color: #fff;
    }

    /* Pre & Code */
    pre {
      background: #040711;
      padding: 18px;
      border-radius: 10px;
      border: 1px solid var(--border-subtle);
      font-family: var(--font-mono);
      font-size: 12px;
      color: #cbd5e1;
      overflow-x: auto;
      line-height: 1.6;
    }

    footer {
      text-align: center;
      color: var(--text-dim);
      font-size: 13px;
      padding: 32px 0 16px;
    }

    /* Responsive */
    @media (max-width: 768px) {
      header { padding: 16px; }
      .nav-tabs { padding: 0 16px; }
      main { padding: 16px; }
      .kpi-row { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>

  <!-- Header -->
  <header>
    <div class="header-content">
      <div class="brand-area">
        <div class="brand-logo">IW</div>
        <div class="brand-title">
          <h1>Indus Weave Textiles — PeopleOps Executive Suite</h1>
          <p>Reconciled HCM Platform Data Warehouse &amp; Talent Funnel Analytics (April–September 2026)</p>
        </div>
      </div>
      <div class="header-badges">
        <span class="pill-badge pill-success">
          <span class="dot-pulse"></span>
          22/22 Data Quality Passed
        </span>
        <span class="pill-badge pill-info">
          1,400 Applicants • 1,266 Employees
        </span>
      </div>
    </div>

    <!-- Navigation Tabs -->
    <nav class="nav-tabs">
      <button class="tab-button active" onclick="switchTab('funnel')">
        🎯 Talent Funnel &amp; Conversion (Bonus)
      </button>
      <button class="tab-button" onclick="switchTab('cfo')">
        📊 CFO Overtime Leakage Audit (Case Core)
      </button>
      <button class="tab-button" onclick="switchTab('warehouse')">
        🏢 Workforce &amp; Attendance Analytics (Q1–Q10)
      </button>
      <button class="tab-button" onclick="switchTab('dq')">
        🛡️ Star Schema &amp; Data Quality
      </button>
    </nav>
  </header>

  <main>
    <!-- =============================================================
         TAB 1: RECRUITMENT FUNNEL & CONVERSION (BONUS TASK 3)
         ============================================================= -->
    <div id="tab-funnel" class="tab-content">
      <div class="kpi-row">
        <div class="kpi-box">
          <div class="kpi-header">
            Total Applications
            <span class="tag-badge tag-cyan">100% Top-Funnel</span>
          </div>
          <div class="kpi-number">1,400</div>
          <div class="kpi-caption">Unique applications received across 14 departments</div>
        </div>

        <div class="kpi-box">
          <div class="kpi-header">
            Hires Completed
            <span class="tag-badge tag-emerald">5.3% Conversion</span>
          </div>
          <div class="kpi-number">74</div>
          <div class="kpi-caption">Accepted offers onboarded as permanent employees</div>
        </div>

        <div class="kpi-box">
          <div class="kpi-header">
            Median Velocity
            <span class="tag-badge tag-cyan">33 Days</span>
          </div>
          <div class="kpi-number">33 days</div>
          <div class="kpi-caption">Average dwell time ~8.5 days per stage progression</div>
        </div>

        <div class="kpi-box">
          <div class="kpi-header">
            Critical Bottleneck
            <span class="tag-badge tag-rose">34.2% Pass</span>
          </div>
          <div class="kpi-number">Interview ➔ Offer</div>
          <div class="kpi-caption">Largest proportional loss: 173 candidates eliminated</div>
        </div>
      </div>

      <!-- Funnel Stage Visual Cards -->
      <div class="glass-panel">
        <div class="glass-panel-title">
          <h2>5-Stage Recruitment Conversion Journey</h2>
          <p>Interactive funnel flow from initial application to final hire</p>
        </div>

        <div class="funnel-pipeline">
          <div class="stage-card">
            <div class="stage-card-num">1</div>
            <div class="stage-card-name">Applied</div>
            <div class="stage-card-count">1,400</div>
            <div class="stage-card-stats">
              <span>100% of top pool</span>
              <span>Baseline applicants</span>
            </div>
          </div>

          <div class="stage-card">
            <div class="stage-card-num">2</div>
            <div class="stage-card-name">Screened</div>
            <div class="stage-card-count">682</div>
            <div class="stage-card-stats">
              <span>48.7% of total</span>
              <span>48.7% step conversion</span>
            </div>
            <div class="drop-indicator">▼ -718 dropped (51.3%)</div>
          </div>

          <div class="stage-card">
            <div class="stage-card-num">3</div>
            <div class="stage-card-name">Interviewed</div>
            <div class="stage-card-count">263</div>
            <div class="stage-card-stats">
              <span>18.8% of total</span>
              <span>38.6% step conversion</span>
            </div>
            <div class="drop-indicator">▼ -419 dropped (61.4%)</div>
          </div>

          <div class="stage-card">
            <div class="stage-card-num">4</div>
            <div class="stage-card-name">Offered</div>
            <div class="stage-card-count">90</div>
            <div class="stage-card-stats">
              <span>6.4% of total</span>
              <span>34.2% step conversion</span>
            </div>
            <div class="drop-indicator">▼ -173 dropped (65.8%)</div>
          </div>

          <div class="stage-card" style="border-color: rgba(16, 185, 129, 0.4);">
            <div class="stage-card-num" style="background: rgba(16, 185, 129, 0.2); color: #34d399;">5</div>
            <div class="stage-card-name" style="color: #34d399;">Hired</div>
            <div class="stage-card-count" style="color: #34d399;">74</div>
            <div class="stage-card-stats">
              <span>5.3% of total</span>
              <span>82.2% offer acceptance</span>
            </div>
            <div class="drop-indicator" style="color: var(--text-dim);">▼ 16 declined (17.8%)</div>
          </div>
        </div>

        <!-- Funnel Progress Bars -->
        <div style="margin-top: 24px;">
          <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 4px;">
            <span>Applied (1,400)</span>
            <span style="color: var(--text-muted)">100%</span>
          </div>
          <div class="progress-track"><div class="progress-bar bar-violet" style="width: 100%;">1,400</div></div>

          <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 4px; margin-top: 10px;">
            <span>Screened (682)</span>
            <span style="color: var(--text-muted)">48.7%</span>
          </div>
          <div class="progress-track"><div class="progress-bar bar-teal" style="width: 48.7%;">682</div></div>

          <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 4px; margin-top: 10px;">
            <span>Interviewed (263)</span>
            <span style="color: var(--text-muted)">18.8%</span>
          </div>
          <div class="progress-track"><div class="progress-bar bar-orange" style="width: 18.8%;">263</div></div>

          <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 4px; margin-top: 10px;">
            <span>Offered (90)</span>
            <span style="color: var(--text-muted)">6.4%</span>
          </div>
          <div class="progress-track"><div class="progress-bar bar-teal" style="width: 6.4%;">90</div></div>

          <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 4px; margin-top: 10px;">
            <span>Hired (74)</span>
            <span style="color: #34d399; font-weight: 700;">5.3%</span>
          </div>
          <div class="progress-track"><div class="progress-bar bar-green" style="width: 5.3%;">74</div></div>
        </div>
      </div>

      <!-- Diagnostic Insight Box -->
      <div class="callout-box callout-cyan">
        <h3>🔍 Talent Acquisition Bottleneck Analysis</h3>
        <p>
          <strong>1. Screening Volume Drop:</strong> 718 candidates (51.3%) are removed right at initial resume evaluation. This indicates candidate sourcing is broad but unqualified, or screening criteria are overly restrictive.<br>
          <strong>2. Interview-to-Offer Bottleneck:</strong> Only 34.2% of interviewed candidates receive an offer (65.8% rejection rate), creating severe panel interviewer fatigue.<br>
          <strong>3. High Offer Acceptance:</strong> Once an offer is extended, <strong>82.2% accept</strong> (74 out of 90). The employer brand and compensation packages are competitive; the pipeline issue lies entirely in evaluation calibration.
        </p>
      </div>

      <!-- Interactive What-If Scenario Simulator -->
      <div class="glass-panel">
        <div class="glass-panel-title">
          <h2>Interactive Pipeline "What-If" Simulator</h2>
          <p>Adjust conversion assumptions to see projected hiring yields</p>
        </div>

        <div class="simulator-grid">
          <div class="sim-card">
            <label>
              <span>Applied ➔ Screened Rate</span>
              <span id="sim-screen-val" style="color:#818cf8;">48.7%</span>
            </label>
            <input type="range" id="sim-screen" min="20" max="80" value="48.7" step="0.5" oninput="runSimulation()">
          </div>

          <div class="sim-card">
            <label>
              <span>Screened ➔ Interviewed Rate</span>
              <span id="sim-interview-val" style="color:#818cf8;">38.6%</span>
            </label>
            <input type="range" id="sim-interview" min="15" max="70" value="38.6" step="0.5" oninput="runSimulation()">
          </div>

          <div class="sim-card">
            <label>
              <span>Interview ➔ Offer Rate</span>
              <span id="sim-offer-val" style="color:#818cf8;">34.2%</span>
            </label>
            <input type="range" id="sim-offer" min="15" max="65" value="34.2" step="0.5" oninput="runSimulation()">
          </div>

          <div class="sim-card">
            <label>
              <span>Offer Acceptance Rate</span>
              <span id="sim-accept-val" style="color:#818cf8;">82.2%</span>
            </label>
            <input type="range" id="sim-accept" min="50" max="100" value="82.2" step="0.5" oninput="runSimulation()">
          </div>

          <div class="sim-result-box">
            <span style="font-size: 13px; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-muted);">Simulated Hires</span>
            <div class="sim-result-val" id="sim-hires-result">74</div>
            <span id="sim-hire-delta" style="font-size: 13px; color: #34d399; font-weight: 600;">Baseline</span>
          </div>
        </div>
      </div>

      <!-- Department Breakdown Table -->
      <div class="glass-panel">
        <div class="glass-panel-title">
          <h2>Departmental Talent Intake &amp; Hire Rates</h2>
          <p>Type to filter by department name or code</p>
        </div>

        <input type="text" id="deptSearch" class="filter-input" placeholder="Search department name or code (e.g., Cutting, Spinning, D21)..." oninput="filterDeptTable()">

        <div class="table-container">
          <table id="deptTable">
            <thead>
              <tr>
                <th>Code</th>
                <th>Department</th>
                <th>Applications</th>
                <th>Hired</th>
                <th>Rejected</th>
                <th>Offer Declined</th>
                <th>Hire Rate %</th>
              </tr>
            </thead>
            <tbody>
              <tr><td style="font-family: var(--font-mono); color:#818cf8;">D21</td><td style="font-weight:600;">Cutting</td><td>180</td><td style="color:#34d399; font-weight:700;">12</td><td>167</td><td>1</td><td><span class="tag-badge tag-emerald">6.7%</span></td></tr>
              <tr><td style="font-family: var(--font-mono); color:#818cf8;">D08</td><td style="font-weight:600;">Spinning</td><td>162</td><td style="color:#34d399; font-weight:700;">14</td><td>144</td><td>4</td><td><span class="tag-badge tag-emerald">8.6%</span></td></tr>
              <tr><td style="font-family: var(--font-mono); color:#818cf8;">D23</td><td style="font-weight:600;">Maintenance</td><td>156</td><td style="color:#34d399; font-weight:700;">6</td><td>148</td><td>2</td><td><span class="tag-badge tag-cyan">3.8%</span></td></tr>
              <tr><td style="font-family: var(--font-mono); color:#818cf8;">D15</td><td style="font-weight:600;">Finishing</td><td>143</td><td style="color:#34d399; font-weight:700;">4</td><td>136</td><td>3</td><td><span class="tag-badge tag-cyan">2.8%</span></td></tr>
              <tr><td style="font-family: var(--font-mono); color:#818cf8;">D14</td><td style="font-weight:600;">Dyeing</td><td>121</td><td style="color:#34d399; font-weight:700;">6</td><td>114</td><td>1</td><td><span class="tag-badge tag-cyan">5.0%</span></td></tr>
              <tr><td style="font-family: var(--font-mono); color:#818cf8;">D22</td><td style="font-weight:600;">Packing</td><td>105</td><td style="color:#34d399; font-weight:700;">8</td><td>96</td><td>1</td><td><span class="tag-badge tag-emerald">7.6%</span></td></tr>
              <tr><td style="font-family: var(--font-mono); color:#818cf8;">D02</td><td style="font-weight:600;">Finance</td><td>96</td><td style="color:#34d399; font-weight:700;">6</td><td>90</td><td>0</td><td><span class="tag-badge tag-emerald">6.2%</span></td></tr>
              <tr><td style="font-family: var(--font-mono); color:#818cf8;">D25</td><td style="font-weight:600;">Warehouse</td><td>91</td><td style="color:#34d399; font-weight:700;">3</td><td>87</td><td>1</td><td><span class="tag-badge tag-cyan">3.3%</span></td></tr>
              <tr><td style="font-family: var(--font-mono); color:#818cf8;">D18</td><td style="font-weight:600;">Warehouse</td><td>89</td><td style="color:#34d399; font-weight:700;">3</td><td>84</td><td>2</td><td><span class="tag-badge tag-cyan">3.4%</span></td></tr>
              <tr><td style="font-family: var(--font-mono); color:#818cf8;">D05</td><td style="font-weight:600;">Sales &amp; Marketing</td><td>85</td><td style="color:#34d399; font-weight:700;">4</td><td>80</td><td>1</td><td><span class="tag-badge tag-cyan">4.7%</span></td></tr>
              <tr><td style="font-family: var(--font-mono); color:#818cf8;">D20</td><td style="font-weight:600;">Stitching</td><td>50</td><td style="color:#34d399; font-weight:700;">3</td><td>47</td><td>0</td><td><span class="tag-badge tag-emerald">6.0%</span></td></tr>
              <tr><td style="font-family: var(--font-mono); color:#818cf8;">D11</td><td style="font-weight:600;">Quality Control</td><td>42</td><td style="color:#34d399; font-weight:700;">2</td><td>40</td><td>0</td><td><span class="tag-badge tag-cyan">4.8%</span></td></tr>
              <tr><td style="font-family: var(--font-mono); color:#818cf8;">D16</td><td style="font-weight:600;">Maintenance</td><td>42</td><td style="color:#34d399; font-weight:700;">3</td><td>39</td><td>0</td><td><span class="tag-badge tag-emerald">7.1%</span></td></tr>
              <tr><td style="font-family: var(--font-mono); color:#818cf8;">D06</td><td style="font-weight:600;">Administration</td><td>38</td><td style="color:#fb7185; font-weight:700;">0</td><td>38</td><td>0</td><td><span class="tag-badge tag-rose">0.0%</span></td></tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Transition Velocity Table -->
      <div class="glass-panel">
        <div class="glass-panel-title">
          <h2>Candidate Stage Velocity &amp; Turnaround Times</h2>
          <p>Median and mean dwell days between recruitment milestones</p>
        </div>
        <div class="table-container">
          <table>
            <thead>
              <tr>
                <th>Origin Stage</th>
                <th>Destination Stage</th>
                <th>Total Volume</th>
                <th>Median Dwell</th>
                <th>Mean Dwell</th>
              </tr>
            </thead>
            <tbody>
              <tr><td>Applied</td><td>Screened</td><td>682</td><td style="font-weight:600; color:#fff;">9 days</td><td>8.5 days</td></tr>
              <tr><td>Applied</td><td>Rejected</td><td>718</td><td style="font-weight:600; color:#fff;">8 days</td><td>8.2 days</td></tr>
              <tr><td>Screened</td><td>Interviewed</td><td>263</td><td style="font-weight:600; color:#fff;">8 days</td><td>8.0 days</td></tr>
              <tr><td>Screened</td><td>Rejected</td><td>419</td><td style="font-weight:600; color:#fff;">8 days</td><td>8.4 days</td></tr>
              <tr><td>Interviewed</td><td>Offered</td><td>90</td><td style="font-weight:600; color:#fff;">9 days</td><td>8.7 days</td></tr>
              <tr><td>Interviewed</td><td>Rejected</td><td>173</td><td style="font-weight:600; color:#fff;">9 days</td><td>9.0 days</td></tr>
              <tr><td>Offered</td><td>Hired</td><td>74</td><td style="font-weight:600; color:#34d399;">8 days</td><td>8.4 days</td></tr>
              <tr><td>Offered</td><td>Offer Declined</td><td>16</td><td style="font-weight:600; color:#fbbf24;">10 days</td><td>8.7 days</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- =============================================================
         TAB 2: CFO OVERTIME LEAKAGE AUDIT (CASE CORE)
         ============================================================= -->
    <div id="tab-cfo" class="tab-content" style="display: none;">
      <div class="callout-box callout-rose">
        <h3>🚨 CFO Problem Statement: Why is Overtime Escalating?</h3>
        <p>
          Indus Weave Textiles' overtime bill soared by <strong>+23.5% (PKR 2.81M to PKR 3.48M)</strong> over the 6 months, yet plant managers claimed attendance was normal.
          Our reconciled warehouse uncovers the truth: <strong>Payroll pays overtime strictly based on manager-signed requests rather than biometric physical punches</strong>.
          Managers approved and paid <strong>36,402 overtime hours</strong> against only <strong>29,116 hours physically worked</strong> — an unearned gap of <strong>7,286 overtime hours</strong>.
        </p>
      </div>

      <div class="kpi-row">
        <div class="kpi-box">
          <div class="kpi-header">
            Overtime Hours Gap
            <span class="tag-badge tag-rose">+7,286 hrs</span>
          </div>
          <div class="kpi-number">36,402 vs 29,116</div>
          <div class="kpi-caption">Approved/Paid vs Biometrically Computed OT</div>
        </div>

        <div class="kpi-box">
          <div class="kpi-header">
            Overtime Spend Surge
            <span class="tag-badge tag-rose">+23.5%</span>
          </div>
          <div class="kpi-number">PKR 3.48M</div>
          <div class="kpi-caption">Climbed from PKR 2.81M in April to 3.48M in Sep</div>
        </div>

        <div class="kpi-box">
          <div class="kpi-header">
            Approvals on Zero-Work Days
            <span class="tag-badge tag-amber">3,687 cases</span>
          </div>
          <div class="kpi-number">18.7%</div>
          <div class="kpi-caption">Approved requests with 0 actual biometric OT hours</div>
        </div>

        <div class="kpi-box">
          <div class="kpi-header">
            Ghost Payroll Post-Separation
            <span class="tag-badge tag-rose">15 Staff</span>
          </div>
          <div class="kpi-number">PKR 3.78M</div>
          <div class="kpi-caption">52 payroll lines paid after employee departure</div>
        </div>
      </div>

      <!-- Top 3 Findings -->
      <div class="glass-panel">
        <div class="glass-panel-title">
          <h2>Top 3 Strategic Findings for CFO Presentation</h2>
          <span class="tag-badge tag-cyan">5-Minute Executive Briefing</span>
        </div>

        <div style="display: grid; gap: 16px;">
          <div style="background: rgba(255,255,255,0.02); padding: 18px; border-radius: 10px; border: 1px solid var(--border-subtle);">
            <h4 style="color: #818cf8; margin-bottom: 6px;">Finding 1: Paid Overtime is Completely Decoupled from Worked Overtime &amp; Growing</h4>
            <p style="color: var(--text-muted); font-size: 14px; line-height: 1.6;">
              In April, the disparity was 856 hours (5,525 paid vs 4,622 worked). By September, the monthly gap surged to 1,782 hours (6,418 paid vs 4,636 worked).
              Actual biometric overtime stayed flat at 4,600–5,000 hours per month, yet payroll disbursements climbed steadily.
              <strong>Faisalabad Plant is the primary hotspot: 4,588.5 excess paid hours (63% of the entire company gap).</strong><br>
              <em>Executive Action:</em> Tie overtime payroll approval directly to biometric machine punches.
            </p>
          </div>

          <div style="background: rgba(255,255,255,0.02); padding: 18px; border-radius: 10px; border: 1px solid var(--border-subtle);">
            <h4 style="color: #38bdf8; margin-bottom: 6px;">Finding 2: 3,687 Overtime Requests Approved for Non-Working or Standard Days</h4>
            <p style="color: var(--text-muted); font-size: 14px; line-height: 1.6;">
              Out of 19,666 approved overtime requests, 3,687 had ZERO computed overtime on that day — including 581 Present shifts where workers left on time, and over 3,000 requests submitted for Absent, Missing Punch, Weekly Off, or Leave days.<br>
              <em>Executive Action:</em> Introduce automated ERP workflow blocks preventing overtime request submissions for shifts with no biometric overtime record.
            </p>
          </div>

          <div style="background: rgba(255,255,255,0.02); padding: 18px; border-radius: 10px; border: 1px solid var(--border-subtle);">
            <h4 style="color: #fb7185; margin-bottom: 6px;">Finding 3: Ghost Payroll — Payroll Did Not Stop After Employee Resignation</h4>
            <p style="color: var(--text-muted); font-size: 14px; line-height: 1.6;">
              15 separated employees received 52 paychecks totaling PKR 3,782,469 in months following their separation date.
              The standout case is <strong>Umair Baloch (E10471)</strong>, who left on 23 April 2026, yet received full paychecks across May, June, July, August, and September totaling PKR 682,100 without a single day of attendance.<br>
              <em>Executive Action:</em> Automate payroll cutoff upon HR recording of separation date, and initiate audit recovery for PKR 3.78M.
            </p>
          </div>
        </div>
      </div>

      <!-- Monthly Trend Table -->
      <div class="glass-panel">
        <div class="glass-panel-title">
          <h2>Monthly Trajectory: Biometric Hours vs Approved vs Paid</h2>
          <p>Evidence from Q5 &amp; fact_payroll_line</p>
        </div>
        <div class="table-container">
          <table>
            <thead>
              <tr>
                <th>Month</th>
                <th>Biometric Hours</th>
                <th>Approved Hours</th>
                <th>Paid Hours</th>
                <th>Monthly Gap</th>
                <th>Overtime Spend</th>
                <th>Gap %</th>
              </tr>
            </thead>
            <tbody>
              <tr><td style="font-weight:600;">2026-04</td><td>4,622.0 hrs</td><td>5,525.5 hrs</td><td style="font-weight:700; color:#fff;">5,525.5 hrs</td><td style="color:#fb7185; font-weight:700;">+856.0 hrs</td><td>PKR 2.81M</td><td><span class="tag-badge tag-amber">+18.5%</span></td></tr>
              <tr><td style="font-weight:600;">2026-05</td><td>4,972.0 hrs</td><td>5,806.5 hrs</td><td style="font-weight:700; color:#fff;">5,806.5 hrs</td><td style="color:#fb7185; font-weight:700;">+834.5 hrs</td><td>PKR 2.86M</td><td><span class="tag-badge tag-amber">+16.8%</span></td></tr>
              <tr><td style="font-weight:600;">2026-06</td><td>4,795.5 hrs</td><td>5,889.0 hrs</td><td style="font-weight:700; color:#fff;">5,889.0 hrs</td><td style="color:#fb7185; font-weight:700;">+1,093.5 hrs</td><td>PKR 2.93M</td><td><span class="tag-badge tag-amber">+22.8%</span></td></tr>
              <tr><td style="font-weight:600;">2026-07</td><td>4,794.5 hrs</td><td>6,249.0 hrs</td><td style="font-weight:700; color:#fff;">6,249.0 hrs</td><td style="color:#fb7185; font-weight:700;">+1,454.5 hrs</td><td>PKR 3.37M</td><td><span class="tag-badge tag-rose">+30.3%</span></td></tr>
              <tr><td style="font-weight:600;">2026-08</td><td>5,014.0 hrs</td><td>6,513.0 hrs</td><td style="font-weight:700; color:#fff;">6,513.0 hrs</td><td style="color:#fb7185; font-weight:700;">+1,499.0 hrs</td><td>PKR 3.57M</td><td><span class="tag-badge tag-rose">+29.9%</span></td></tr>
              <tr><td style="font-weight:600;">2026-09</td><td>4,636.5 hrs</td><td>6,418.5 hrs</td><td style="font-weight:700; color:#fff;">6,418.5 hrs</td><td style="color:#fb7185; font-weight:700;">+1,782.0 hrs</td><td>PKR 3.48M</td><td><span class="tag-badge tag-rose">+38.4%</span></td></tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Plant Breakdown -->
      <div class="glass-panel">
        <div class="glass-panel-title">
          <h2>Overtime Discrepancy by Plant Location</h2>
          <p>Distribution of the 7,286 hour excess payout</p>
        </div>
        <div class="table-container">
          <table>
            <thead>
              <tr>
                <th>Plant Location</th>
                <th>Worked Hours</th>
                <th>Approved Hours</th>
                <th>Paid Hours</th>
                <th>Excess Hours</th>
                <th>Company Share</th>
              </tr>
            </thead>
            <tbody>
              <tr><td style="font-weight:700; color:#fff;">Faisalabad Plant</td><td>9,829.0 hrs</td><td>14,417.5 hrs</td><td>14,417.5 hrs</td><td style="color:#fb7185; font-weight:700;">+4,588.5 hrs</td><td><span class="tag-badge tag-rose">63.0% of total gap</span></td></tr>
              <tr><td style="font-weight:700; color:#fff;">Korangi Plant</td><td>9,228.0 hrs</td><td>10,690.0 hrs</td><td>10,690.0 hrs</td><td style="color:#fbbf24; font-weight:700;">+1,462.0 hrs</td><td><span class="tag-badge tag-amber">20.1% of total gap</span></td></tr>
              <tr><td style="font-weight:700; color:#fff;">SITE Plant</td><td>8,275.0 hrs</td><td>9,566.0 hrs</td><td>9,566.0 hrs</td><td style="color:#fbbf24; font-weight:700;">+1,291.0 hrs</td><td><span class="tag-badge tag-amber">17.7% of total gap</span></td></tr>
              <tr><td style="font-weight:700; color:#fff;">Head Office</td><td>1,502.5 hrs</td><td>1,728.0 hrs</td><td>1,728.0 hrs</td><td style="color:#38bdf8; font-weight:700;">+225.5 hrs</td><td><span class="tag-badge tag-cyan">3.1% of total gap</span></td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- =============================================================
         TAB 3: WORKFORCE & ATTENDANCE ANALYTICS (Q1-Q10)
         ============================================================= -->
    <div id="tab-warehouse" class="tab-content" style="display: none;">
      <div class="kpi-row">
        <div class="kpi-box">
          <div class="kpi-header">Active Headcount (Sep)</div>
          <div class="kpi-number">1,172</div>
          <div class="kpi-caption">Down from 1,189 in April (-1.4% change)</div>
        </div>
        <div class="kpi-box">
          <div class="kpi-header">Worst Absenteeism</div>
          <div class="kpi-number">5.12%</div>
          <div class="kpi-caption">Faisalabad Plant (leading company rate)</div>
        </div>
        <div class="kpi-box">
          <div class="kpi-header">Late Check-in Champion</div>
          <div class="kpi-number">53 times</div>
          <div class="kpi-caption">Usman Gill (D21 Cutting, FSD Plant)</div>
        </div>
        <div class="kpi-box">
          <div class="kpi-header">Annual Leave Overuse</div>
          <div class="kpi-number">20 Staff</div>
          <div class="kpi-caption">Exceeded full-year leave quota in 6 months</div>
        </div>
      </div>

      <!-- Absenteeism & Headcount Grid -->
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px; margin-bottom: 24px;">
        <div class="glass-panel" style="margin: 0;">
          <div class="glass-panel-title">
            <h2>Plant Absenteeism Rates (Q3)</h2>
          </div>
          <div class="table-container">
            <table>
              <thead>
                <tr><th>Plant</th><th>Absent Days</th><th>Scheduled</th><th>Rate</th></tr>
              </thead>
              <tbody>
                <tr><td>Faisalabad Plant</td><td>2,801</td><td>54,720</td><td><span class="tag-badge tag-rose">5.12%</span></td></tr>
                <tr><td>SITE Plant</td><td>1,768</td><td>49,024</td><td><span class="tag-badge tag-amber">3.61%</span></td></tr>
                <tr><td>Korangi Plant</td><td>1,863</td><td>54,792</td><td><span class="tag-badge tag-amber">3.40%</span></td></tr>
                <tr><td>Head Office</td><td>435</td><td>17,212</td><td><span class="tag-badge tag-cyan">2.53%</span></td></tr>
              </tbody>
            </table>
          </div>
        </div>

        <div class="glass-panel" style="margin: 0;">
          <div class="glass-panel-title">
            <h2>Month-End Headcount Trajectory (Q1)</h2>
          </div>
          <div class="table-container">
            <table>
              <thead>
                <tr><th>Month</th><th>Headcount</th><th>Visual Trend</th></tr>
              </thead>
              <tbody>
                <tr><td>2026-04</td><td style="font-weight:700;">1,189</td><td><div class="progress-track" style="height:20px; width:140px;"><div class="progress-bar bar-violet" style="width:100%;"></div></div></td></tr>
                <tr><td>2026-05</td><td style="font-weight:700;">1,186</td><td><div class="progress-track" style="height:20px; width:140px;"><div class="progress-bar bar-violet" style="width:99.7%;"></div></div></td></tr>
                <tr><td>2026-06</td><td style="font-weight:700;">1,183</td><td><div class="progress-track" style="height:20px; width:140px;"><div class="progress-bar bar-violet" style="width:99.4%;"></div></div></td></tr>
                <tr><td>2026-07</td><td style="font-weight:700;">1,172</td><td><div class="progress-track" style="height:20px; width:140px;"><div class="progress-bar bar-violet" style="width:98.5%;"></div></div></td></tr>
                <tr><td>2026-08</td><td style="font-weight:700;">1,176</td><td><div class="progress-track" style="height:20px; width:140px;"><div class="progress-bar bar-violet" style="width:98.9%;"></div></div></td></tr>
                <tr><td>2026-09</td><td style="font-weight:700;">1,172</td><td><div class="progress-track" style="height:20px; width:140px;"><div class="progress-bar bar-violet" style="width:98.5%;"></div></div></td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Top Late Arrivals Table -->
      <div class="glass-panel">
        <div class="glass-panel-title">
          <h2>Top 10 Chronic Late Arrivals (Q4)</h2>
          <p>Employees checking in &gt;10 minutes past shift start</p>
        </div>
        <div class="table-container">
          <table>
            <thead>
              <tr>
                <th>Emp ID</th>
                <th>Employee Name</th>
                <th>Department</th>
                <th>Plant</th>
                <th>Late Days</th>
                <th>Total Minutes Late</th>
              </tr>
            </thead>
            <tbody>
              <tr><td style="font-family: var(--font-mono); color:#818cf8;">E10580</td><td style="font-weight:600;">Usman Gill</td><td>Cutting</td><td>Faisalabad Plant</td><td style="color:#fbbf24; font-weight:700;">53 times</td><td>2,420 min</td></tr>
              <tr><td style="font-family: var(--font-mono); color:#818cf8;">E10982</td><td style="font-weight:600;">Adnan Akhtar</td><td>Production Planning</td><td>Korangi Plant</td><td style="color:#fbbf24; font-weight:700;">48 times</td><td>1,891 min</td></tr>
              <tr><td style="font-family: var(--font-mono); color:#818cf8;">E10454</td><td style="font-weight:600;">Raheel Khan</td><td>Maintenance</td><td>Faisalabad Plant</td><td style="color:#fbbf24; font-weight:700;">46 times</td><td>1,906 min</td></tr>
              <tr><td style="font-family: var(--font-mono); color:#818cf8;">E10283</td><td style="font-weight:600;">Ali Raza</td><td>Cutting</td><td>Faisalabad Plant</td><td style="color:#fbbf24; font-weight:700;">45 times</td><td>2,125 min</td></tr>
              <tr><td style="font-family: var(--font-mono); color:#818cf8;">E10287</td><td style="font-weight:600;">Naveed Hussain</td><td>Quality Control</td><td>Faisalabad Plant</td><td style="color:#fbbf24; font-weight:700;">45 times</td><td>1,999 min</td></tr>
              <tr><td style="font-family: var(--font-mono); color:#818cf8;">E10328</td><td style="font-weight:600;">Bilal Butt</td><td>Maintenance</td><td>SITE Plant</td><td style="color:#fbbf24; font-weight:700;">44 times</td><td>1,780 min</td></tr>
              <tr><td style="font-family: var(--font-mono); color:#818cf8;">E10649</td><td style="font-weight:600;">Bilal Butt</td><td>Maintenance</td><td>SITE Plant</td><td style="color:#fbbf24; font-weight:700;">44 times</td><td>1,911 min</td></tr>
              <tr><td style="font-family: var(--font-mono); color:#818cf8;">E10398</td><td style="font-weight:600;">Zahid Gill</td><td>Stitching</td><td>Faisalabad Plant</td><td style="color:#fbbf24; font-weight:700;">43 times</td><td>1,845 min</td></tr>
              <tr><td style="font-family: var(--font-mono); color:#818cf8;">E10871</td><td style="font-weight:600;">Rashid Butt</td><td>Stitching</td><td>Faisalabad Plant</td><td style="color:#fbbf24; font-weight:700;">43 times</td><td>1,812 min</td></tr>
              <tr><td style="font-family: var(--font-mono); color:#818cf8;">E10967</td><td style="font-weight:600;">Bilal Hashmi</td><td>Weaving</td><td>Korangi Plant</td><td style="color:#fbbf24; font-weight:700;">42 times</td><td>1,745 min</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- =============================================================
         TAB 4: STAR SCHEMA & DATA QUALITY (STAGE 4 & 6)
         ============================================================= -->
    <div id="tab-dq" class="tab-content" style="display: none;">
      <div class="kpi-row">
        <div class="kpi-box">
          <div class="kpi-header">Quality Checks</div>
          <div class="kpi-number" style="color:#34d399;">22 / 22 PASS</div>
          <div class="kpi-caption">100% automated validation in dq_results</div>
        </div>
        <div class="kpi-box">
          <div class="kpi-header">Raw Records Loaded</div>
          <div class="kpi-number">472,907</div>
          <div class="kpi-caption">Untouched, all columns as text with row hashes</div>
        </div>
        <div class="kpi-box">
          <div class="kpi-header">Reconciliation Rate</div>
          <div class="kpi-number">100.0%</div>
          <div class="kpi-caption">Raw = Staged (449,770) + Rejected (23,137)</div>
        </div>
        <div class="kpi-box">
          <div class="kpi-header">Hardware Bug Corrected</div>
          <div class="kpi-number">48,146 rows</div>
          <div class="kpi-caption">DEV-SITE-01 +60 min clock drift shifted back</div>
        </div>
      </div>

      <!-- DQ Checks Table -->
      <div class="glass-panel">
        <div class="glass-panel-title">
          <h2>Automated Data Quality Verification Suite</h2>
          <span class="tag-badge tag-emerald">ALL CHECKS GREEN</span>
        </div>
        <div class="table-container">
          <table>
            <thead>
              <tr>
                <th>Test Identifier</th>
                <th>Category</th>
                <th>Expected Result</th>
                <th>Observed Result</th>
                <th>Validation Status</th>
              </tr>
            </thead>
            <tbody>
              <tr><td style="font-family:var(--font-mono); color:#818cf8;">pk_dim_employee_unique</td><td>PK Uniqueness</td><td>0 duplicate keys</td><td>0</td><td><span class="tag-badge tag-emerald">PASS</span></td></tr>
              <tr><td style="font-family:var(--font-mono); color:#818cf8;">pk_dim_department_unique</td><td>PK Uniqueness</td><td>0 duplicate keys</td><td>0</td><td><span class="tag-badge tag-emerald">PASS</span></td></tr>
              <tr><td style="font-family:var(--font-mono); color:#818cf8;">pk_dim_shift_unique</td><td>PK Uniqueness</td><td>0 duplicate keys</td><td>0</td><td><span class="tag-badge tag-emerald">PASS</span></td></tr>
              <tr><td style="font-family:var(--font-mono); color:#818cf8;">pk_fact_attendance_unique</td><td>PK Uniqueness</td><td>0 duplicate keys</td><td>0</td><td><span class="tag-badge tag-emerald">PASS</span></td></tr>
              <tr><td style="font-family:var(--font-mono); color:#818cf8;">fk_attendance_dept</td><td>Referential Integrity</td><td>0 orphan FKs</td><td>0</td><td><span class="tag-badge tag-emerald">PASS</span></td></tr>
              <tr><td style="font-family:var(--font-mono); color:#818cf8;">fk_attendance_employee_key</td><td>Referential Integrity</td><td>0 orphan FKs</td><td>0</td><td><span class="tag-badge tag-emerald">PASS</span></td></tr>
              <tr><td style="font-family:var(--font-mono); color:#818cf8;">fk_payroll_dept</td><td>Referential Integrity</td><td>0 orphan FKs</td><td>0</td><td><span class="tag-badge tag-emerald">PASS</span></td></tr>
              <tr><td style="font-family:var(--font-mono); color:#818cf8;">notnull_attendance_emp_date</td><td>Not-Null Constraints</td><td>0 null values</td><td>0</td><td><span class="tag-badge tag-emerald">PASS</span></td></tr>
              <tr><td style="font-family:var(--font-mono); color:#818cf8;">status_accepted_values</td><td>Domain Values</td><td>0 invalid statuses</td><td>0</td><td><span class="tag-badge tag-emerald">PASS</span></td></tr>
              <tr><td style="font-family:var(--font-mono); color:#818cf8;">leave_type_accepted</td><td>Domain Values</td><td>0 invalid leave types</td><td>0</td><td><span class="tag-badge tag-emerald">PASS</span></td></tr>
              <tr><td style="font-family:var(--font-mono); color:#818cf8;">pay_component_accepted</td><td>Domain Values</td><td>0 invalid pay codes</td><td>0</td><td><span class="tag-badge tag-emerald">PASS</span></td></tr>
              <tr><td style="font-family:var(--font-mono); color:#818cf8;">negative_worked_hours</td><td>Business Sanity</td><td>0 negative hours</td><td>0</td><td><span class="tag-badge tag-emerald">PASS</span></td></tr>
              <tr><td style="font-family:var(--font-mono); color:#818cf8;">worked_over_16h</td><td>Business Sanity</td><td>0 shifts &gt;16h</td><td>0</td><td><span class="tag-badge tag-emerald">PASS</span></td></tr>
              <tr><td style="font-family:var(--font-mono); color:#818cf8;">scd_overlaps</td><td>SCD Type 2 Validity</td><td>0 overlapping dates</td><td>0</td><td><span class="tag-badge tag-emerald">PASS</span></td></tr>
              <tr><td style="font-family:var(--font-mono); color:#818cf8;">scd_valid_to_before_from</td><td>SCD Type 2 Validity</td><td>0 inverted dates</td><td>0</td><td><span class="tag-badge tag-emerald">PASS</span></td></tr>
              <tr><td style="font-family:var(--font-mono); color:#818cf8;">ot_not_half_hour</td><td>Business Sanity</td><td>0 unrounded OT</td><td>0</td><td><span class="tag-badge tag-emerald">PASS</span></td></tr>
              <tr><td style="font-family:var(--font-mono); color:#818cf8;">recon_employees</td><td>Reconciliation</td><td>1,316 raw = 1,266 + 50 dedup</td><td>1,316</td><td><span class="tag-badge tag-emerald">PASS</span></td></tr>
              <tr><td style="font-family:var(--font-mono); color:#818cf8;">recon_punches</td><td>Reconciliation</td><td>345,280 raw = 322,143 + 23,137</td><td>345,280</td><td><span class="tag-badge tag-emerald">PASS</span></td></tr>
              <tr><td style="font-family:var(--font-mono); color:#818cf8;">recon_leave_requests</td><td>Reconciliation</td><td>5,372 raw = 5,372</td><td>5,372</td><td><span class="tag-badge tag-emerald">PASS</span></td></tr>
              <tr><td style="font-family:var(--font-mono); color:#818cf8;">recon_departments</td><td>Reconciliation</td><td>25 raw = 25</td><td>25</td><td><span class="tag-badge tag-emerald">PASS</span></td></tr>
              <tr><td style="font-family:var(--font-mono); color:#818cf8;">recon_payroll</td><td>Reconciliation</td><td>53,617 raw = 53,617</td><td>53,617</td><td><span class="tag-badge tag-emerald">PASS</span></td></tr>
              <tr><td style="font-family:var(--font-mono); color:#818cf8;">recon_overtime_total</td><td>Reconciliation</td><td>22,098 raw = 22,098</td><td>22,098</td><td><span class="tag-badge tag-emerald">PASS</span></td></tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Faulty Hardware Anomaly Card -->
      <div class="callout-box callout-amber">
        <h3>Hardware Anomaly Root Cause: DEV-SITE-01 Clock Drift</h3>
        <p>
          <strong>Discovery:</strong> By profiling median first punch timestamp relative to shift start per device, <code>DEV-SITE-01</code> showed normal check-ins (-7 min) in Q2 (Apr–Jun), but jumped to +53 min on 1 July 2026.
          <strong>Correction:</strong> The pipeline subtracted 60 minutes from all 48,146 punches recorded by DEV-SITE-01 on or after 2026-07-01 prior to shift assignment.
        </p>
      </div>

      <!-- Star Schema DDL -->
      <div class="glass-panel">
        <div class="glass-panel-title">
          <h2>Star Schema DDL Architecture</h2>
          <p>Production dimensional model in indus_weave.db</p>
        </div>
        <pre><code>-- DIMENSIONS
CREATE TABLE dim_employee (
    employee_key INTEGER PRIMARY KEY AUTOINCREMENT,
    emp_id TEXT NOT NULL,
    full_name TEXT NOT NULL,
    gender TEXT, hire_date TEXT, separation_date TEXT,
    dept_id TEXT NOT NULL, designation TEXT, grade TEXT,
    basic_salary INTEGER, change_reason TEXT,
    valid_from TEXT NOT NULL, valid_to TEXT NOT NULL,
    is_current INTEGER NOT NULL,
    FOREIGN KEY (dept_id) REFERENCES dim_department(dept_id)
);
CREATE TABLE dim_department (dept_id TEXT PRIMARY KEY, dept_name TEXT, plant TEXT, cost_center TEXT);
CREATE TABLE dim_shift (shift_code TEXT PRIMARY KEY, name TEXT, start_time TEXT, end_time TEXT, crosses_midnight INTEGER, grace_minutes INTEGER);
CREATE TABLE dim_date (date_key TEXT PRIMARY KEY, date TEXT, year INTEGER, month INTEGER, month_name TEXT, day INTEGER, day_of_week TEXT, is_weekend INTEGER, is_holiday INTEGER);

-- FACTS
CREATE TABLE fact_attendance_daily (
    attendance_key INTEGER PRIMARY KEY AUTOINCREMENT,
    emp_id TEXT NOT NULL, work_date TEXT NOT NULL,
    employee_key INTEGER, dept_id TEXT, shift_code TEXT,
    plant TEXT, first_punch TEXT, last_punch TEXT,
    worked_hours REAL, overtime_hours REAL,
    late_minutes INTEGER, early_minutes INTEGER,
    is_late INTEGER, is_early INTEGER,
    status TEXT NOT NULL,
    FOREIGN KEY (employee_key) REFERENCES dim_employee(employee_key),
    FOREIGN KEY (dept_id) REFERENCES dim_department(dept_id),
    FOREIGN KEY (shift_code) REFERENCES dim_shift(shift_code)
);
CREATE TABLE fact_leave_day (leave_day_key INTEGER PRIMARY KEY AUTOINCREMENT, request_id TEXT, emp_id TEXT, leave_date TEXT, leave_type TEXT);
CREATE TABLE fact_overtime_approved (ot_key INTEGER PRIMARY KEY AUTOINCREMENT, request_id TEXT, emp_id TEXT, ot_date TEXT, requested_hours REAL, approved_hours REAL, approver_id TEXT, requested_at TEXT);
CREATE TABLE fact_payroll_line (line_id TEXT PRIMARY KEY, payroll_month TEXT, emp_id TEXT, employee_key INTEGER, dept_id TEXT, plant TEXT, component TEXT, component_type TEXT, units REAL, amount REAL);</code></pre>
      </div>
    </div>

    <footer>
      Indus Weave Textiles • PeopleOps Data Hackathon 2026 • 100% Case Study Compliant
    </footer>
  </main>

  <script>
    // Tab switching
    function switchTab(tabId) {
      document.querySelectorAll('.tab-content').forEach(el => el.style.display = 'none');
      document.querySelectorAll('.tab-button').forEach(btn => btn.classList.remove('active'));
      
      const target = document.getElementById('tab-' + tabId);
      if (target) target.style.display = 'block';
      
      const activeBtn = Array.from(document.querySelectorAll('.tab-button')).find(b => b.getAttribute('onclick').includes(tabId));
      if (activeBtn) activeBtn.classList.add('active');
    }

    // Filter department table
    function filterDeptTable() {
      const q = document.getElementById('deptSearch').value.toLowerCase();
      document.querySelectorAll('#deptTable tbody tr').forEach(tr => {
        tr.style.display = tr.textContent.toLowerCase().includes(q) ? '' : 'none';
      });
    }

    // Interactive simulator
    function runSimulation() {
      const screenPct = parseFloat(document.getElementById('sim-screen').value);
      const interviewPct = parseFloat(document.getElementById('sim-interview').value);
      const offerPct = parseFloat(document.getElementById('sim-offer').value);
      const acceptPct = parseFloat(document.getElementById('sim-accept').value);

      document.getElementById('sim-screen-val').textContent = screenPct.toFixed(1) + '%';
      document.getElementById('sim-interview-val').textContent = interviewPct.toFixed(1) + '%';
      document.getElementById('sim-offer-val').textContent = offerPct.toFixed(1) + '%';
      document.getElementById('sim-accept-val').textContent = acceptPct.toFixed(1) + '%';

      const applied = 1400;
      const screened = applied * (screenPct / 100);
      const interviewed = screened * (interviewPct / 100);
      const offered = interviewed * (offerPct / 100);
      const hires = Math.round(offered * (acceptPct / 100));

      const delta = hires - 74;
      document.getElementById('sim-hires-result').textContent = hires;
      const deltaEl = document.getElementById('sim-hire-delta');
      if (delta > 0) {
        deltaEl.textContent = `+${delta} vs baseline (+${((delta/74)*100).toFixed(0)}%)`;
        deltaEl.style.color = '#34d399';
      } else if (delta < 0) {
        deltaEl.textContent = `${delta} vs baseline (${((delta/74)*100).toFixed(0)}%)`;
        deltaEl.style.color = '#fb7185';
      } else {
        deltaEl.textContent = 'Baseline (Exact Match)';
        deltaEl.style.color = '#94a3b8';
      }
    }
  </script>
</body>
</html>
"""

def main():
    OUT_FILE.write_text(HTML_CONTENT, encoding="utf-8")
    print(f"Generated {OUT_FILE} ({len(HTML_CONTENT)} bytes)")

if __name__ == "__main__":
    main()
