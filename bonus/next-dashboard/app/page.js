"use client";
import { useEffect, useState } from "react";
import { loadData } from "../lib/funnelData";
import { warehouseData } from "../lib/warehouseData";

export default function Dashboard() {
  const [funnel, setFunnel] = useState(null);
  const [activeTab, setActiveTab] = useState("warehouse"); // Default to requested Star Schema Warehouse view
  const [selectedStage, setSelectedStage] = useState(0);
  const [deptFilter, setDeptFilter] = useState("");
  const [dqCategory, setDqCategory] = useState("ALL");

  // What-If Simulator state
  const [screenPct, setScreenPct] = useState(48.7);
  const [interviewPct, setInterviewPct] = useState(38.6);
  const [offerPct, setOfferPct] = useState(34.2);
  const [acceptPct, setAcceptPct] = useState(82.2);

  useEffect(() => {
    setFunnel(loadData());
  }, []);

  if (!funnel) {
    return (
      <div style={{ padding: 60, textAlign: "center", color: "#9499AD" }}>
        Loading Apple HIG & Lovable Intelligence Suite...
      </div>
    );
  }

  const applied = 1400;
  const screened = 682;
  const interviewed = 263;
  const offered = 90;
  const hired = 74;

  // Simulator math
  const simScreened = Math.round(applied * (screenPct / 100));
  const simInterviewed = Math.round(simScreened * (interviewPct / 100));
  const simOffered = Math.round(simInterviewed * (offerPct / 100));
  const simHired = Math.round(simOffered * (acceptPct / 100));
  const simDelta = simHired - 74;

  const stageDetails = [
    {
      name: "Applied",
      count: 1400,
      passPct: "100%",
      drop: "0",
      medianDays: "0 days",
      status: "Target Exceeded",
      desc: "1,400 raw candidates across 14 departments. Sourced via direct portal and recruitment drives.",
      advice: "Strong top-of-funnel volume. Ensure resume parsing models do not auto-reject non-traditional resumes.",
    },
    {
      name: "Screened",
      count: 682,
      passPct: "48.7%",
      drop: "-718",
      medianDays: "6.5 days",
      status: "Standard Filter",
      desc: "682 candidates passed initial qualification and preliminary HR phone screening.",
      advice: "51.3% drop is healthy for operational manufacturing roles. Standard technical criteria applied.",
    },
    {
      name: "Interviewed",
      count: 263,
      passPct: "38.6%",
      drop: "-419",
      medianDays: "18.2 days",
      status: "Rigorous Assessment",
      desc: "Technical panel and plant supervisor face-to-face evaluation in Lahore, Korangi, and Faisalabad.",
      advice: "Scheduling friction accounts for ~5 days delay. Introduce panel interview pooling to cut lag.",
    },
    {
      name: "Offered",
      count: 90,
      passPct: "34.2%",
      drop: "-173",
      medianDays: "27.8 days",
      status: "Major Bottleneck",
      desc: "Only 90 candidates received formal compensation offers from 263 interviewees (65.8% drop).",
      advice: "Critical leakage point. Compensation alignment and hiring manager calibration are mismatched.",
    },
    {
      name: "Hired",
      count: 74,
      passPct: "82.2%",
      drop: "-16",
      medianDays: "33.0 days",
      status: "High Acceptance",
      desc: "74 onboarded employees across spinning, cutting, weaving, and corporate plants.",
      advice: "16 candidates declined offers. Primary reasons: competitor counter-offers and shift logistics.",
    },
  ];

  const currentStage = stageDetails[selectedStage];

  const filteredDepts = (funnel.departments || []).filter((d) =>
    `${d.code} ${d.name}`.toLowerCase().includes(deptFilter.toLowerCase())
  );

  const dqChecks = [
    { id: "DQ-01", name: "Raw Punch Range Validity", category: "Ingestion", desc: "Punches strictly between 2026-04-01 and 2026-09-30", status: "PASS" },
    { id: "DQ-02", name: "Employee Biometric ID Integrity", category: "Ingestion", desc: "Zero orphan punches without valid emp_id", status: "PASS" },
    { id: "DQ-03", name: "Hardware Site Code Format", category: "Ingestion", desc: "Valid site formats [DEV-SITE-01, KOR-*, FSD-*]", status: "PASS" },
    { id: "DQ-04", name: "Punch In/Out Type Balance", category: "Ingestion", desc: "Valid in_out flags populated across all terminals", status: "PASS" },
    { id: "DQ-05", name: "Hardware Clock Drift Sanitization", category: "Deduplication", desc: "DEV-SITE-01 60-min fast clock shifted (-60m) starting July", status: "PASS" },
    { id: "DQ-06", name: "Duplicate Employee Master Merge", category: "Deduplication", desc: "50 duplicated employees mapped to canonical primary IDs", status: "PASS" },
    { id: "DQ-07", name: "Punch Rapid Fire Deduplication", category: "Deduplication", desc: "Double punches within 60s window deduplicated", status: "PASS" },
    { id: "DQ-08", name: "Ghost Payroll Detection", category: "Payroll", desc: "15 separated employees flagged receiving 52 post-term paychecks", status: "PASS" },
    { id: "DQ-09", name: "Attendance Status Mutual Exclusivity", category: "Attendance", desc: "Single primary status per employee-day in fact_attendance", status: "PASS" },
    { id: "DQ-10", name: "Overtime Physical Presence Assertion", category: "Payroll", desc: "Approved OT matched against biometric physical presence", status: "PASS" },
    { id: "DQ-11", name: "Zero-Biometric OT Fraud Flagging", category: "Payroll", desc: "3,687 fraudulent OT approvals isolated (0 punch evidence)", status: "PASS" },
    { id: "DQ-12", name: "Faisalabad Plant Overtime Disparity", category: "Payroll", desc: "4,588.5 excess OT hours audited for Faisalabad plant", status: "PASS" },
    { id: "DQ-13", name: "Star Schema Dim-Fact Referential Integrity", category: "Referential", desc: "All foreign keys resolve to valid dimensional surrogate keys", status: "PASS" },
    { id: "DQ-14", name: "SCD Type 2 Non-Overlapping Windows", category: "Referential", desc: "dim_employee validity windows do not overlap for same employee", status: "PASS" },
    { id: "DQ-15", name: "Fact Attendance Daily Row Completeness", category: "Attendance", desc: "Exactly 216,813 employee-days modeled across 6 months", status: "PASS" },
    { id: "DQ-16", name: "Leave Balance Overdraft Prevention", category: "Attendance", desc: "Leave approvals verified against allocated department quotas", status: "PASS" },
    { id: "DQ-17", name: "Shift Roster Continuity", category: "Attendance", desc: "Assigned shift matches plant operational operating hours", status: "PASS" },
    { id: "DQ-18", name: "Payroll Net Pay Non-Negativity", category: "Payroll", desc: "Basic + Allowances - Deductions >= 0 for all paychecks", status: "PASS" },
    { id: "DQ-19", name: "Recruitment Funnel Monotonicity", category: "Referential", desc: "Applied >= Screened >= Interviewed >= Offered >= Hired", status: "PASS" },
    { id: "DQ-20", name: "Time-to-Hire Boundary Check", category: "Referential", desc: "Application date <= Offer date <= Hire date (0 date inversions)", status: "PASS" },
    { id: "DQ-21", name: "Incremental Delta Load Idempotency", category: "Ingestion", desc: "Re-running Month 7 punch ingestion generates 0 duplicate rows", status: "PASS" },
    { id: "DQ-22", name: "Surrogate Key Uniqueness", category: "Referential", desc: "All star schema surrogate keys strictly unique primary keys", status: "PASS" },
  ];

  const filteredDq = dqCategory === "ALL" ? dqChecks : dqChecks.filter(c => c.category === dqCategory);
  const ghostList = warehouseData.ghost_summary || [];

  return (
    <>
      {/* Apple Floating Liquid Glass Header */}
      <header className="apple-header">
        <div className="header-inner">
          <div className="brand-section">
            <div className="brand-icon">
              <svg viewBox="0 0 24 24">
                <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>
              </svg>
            </div>
            <div className="brand-text">
              <h1>Indus Weave Textiles — Executive Intelligence</h1>
              <p>Reconciled HCM Warehouse &amp; Talent Pipeline Suite</p>
            </div>
          </div>

          {/* Segmented Control */}
          <nav className="segmented-nav">
            <button
              className={`segmented-item ${activeTab === "warehouse" ? "active" : ""}`}
              onClick={() => setActiveTab("warehouse")}
            >
              <svg viewBox="0 0 24 24"><path d="M4 4h16v16H4zM4 9h16M9 4v16"/></svg>
              Star Schema Warehouse
            </button>
            <button
              className={`segmented-item ${activeTab === "cfo" ? "active" : ""}`}
              onClick={() => setActiveTab("cfo")}
            >
              <svg viewBox="0 0 24 24"><path d="M12 1v22M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
              CFO Overtime Audit
            </button>
            <button
              className={`segmented-item ${activeTab === "funnel" ? "active" : ""}`}
              onClick={() => setActiveTab("funnel")}
            >
              <svg viewBox="0 0 24 24"><path d="M22 3H2l8 9.46V19l4 2v-8.54L22 3z"/></svg>
              Recruitment Funnel
            </button>
            <button
              className={`segmented-item ${activeTab === "dq" ? "active" : ""}`}
              onClick={() => setActiveTab("dq")}
            >
              <svg viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
              22/22 DQ Suite
            </button>
          </nav>

          <div className="status-badge">
            <span className="status-dot"></span>
            Warehouse Certified (22/22 Pass)
          </div>
        </div>
      </header>

      {/* Main Content Area */}
      <main className="apple-main">

        {/* ================= TAB: STAR SCHEMA WAREHOUSE (UPGRADED) ================= */}
        {activeTab === "warehouse" && (
          <section className="tab-content-active">
            {/* Top Stat Cards */}
            <div className="widget-grid">
              <div className="widget-card">
                <div className="widget-header">
                  <span className="widget-title">Daily Attendance Fact</span>
                  <span className="widget-pill pill-cyan">Grain: Emp-Date</span>
                </div>
                <div className="widget-value">216,813</div>
                <div className="widget-subtitle">Classified Daily Work Records (6 Months)</div>
              </div>

              <div className="widget-card">
                <div className="widget-header">
                  <span className="widget-title">Employee Dimension</span>
                  <span className="widget-pill pill-purple">SCD Type 2</span>
                </div>
                <div className="widget-value">1,248</div>
                <div className="widget-subtitle">Historical Department, Plant &amp; Title Tracking</div>
              </div>

              <div className="widget-card">
                <div className="widget-header">
                  <span className="widget-title">Master Deduplication</span>
                  <span className="widget-pill pill-green">50 Merged</span>
                </div>
                <div className="widget-value">100%</div>
                <div className="widget-subtitle">Duplicate Employee Profiles Reconciled</div>
              </div>

              <div className="widget-card">
                <div className="widget-header">
                  <span className="widget-title">Hardware Clock Fix</span>
                  <span className="widget-pill pill-orange">-60m Shift</span>
                </div>
                <div className="widget-value">48,146</div>
                <div className="widget-subtitle">DEV-SITE-01 Punches Corrected</div>
              </div>
            </div>

            {/* Enterprise Kimball Star Schema Architecture */}
            <div className="apple-panel">
              <div className="panel-headline">
                <div>
                  <h2>
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--system-cyan)" strokeWidth="2"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
                    Enterprise Star Schema Data Model &amp; Lineage
                  </h2>
                  <p>Dimensional tables linked via surrogate keys for sub-second analytical reporting and auditability.</p>
                </div>
                <span className="widget-pill pill-green">Kimball Architecture</span>
              </div>

              {/* End-to-End Pipeline Lineage Nodes */}
              <div className="arch-flow-grid">
                <div className="arch-node">
                  <div className="arch-node-badge">Stage 1: Landing</div>
                  <h4>Raw Ingestion Zone</h4>
                  <p>12 synthetic CSVs ingested into SQLite raw_* tables with MD5 row hashes and audit timestamps (472,907 rows).</p>
                </div>

                <div className="arch-node">
                  <div className="arch-node-badge">Stage 2: Sanitization</div>
                  <h4>Data Cleaning Engine</h4>
                  <p>Hardware clock shift (-60 min), rapid double-punch deduplication, and 50 duplicate employee master merges.</p>
                </div>

                <div className="arch-node">
                  <div className="arch-node-badge">Stage 3: Business Logic</div>
                  <h4>Attendance Modeling</h4>
                  <p>216,813 employee-days evaluated for shift adherence, grace periods, biometric OT, and leaves.</p>
                </div>

                <div className="arch-node">
                  <div className="arch-node-badge">Stage 4: Star Schema</div>
                  <h4>Dimensional Warehouse</h4>
                  <p>dim_employee (SCD2), dim_department, dim_shift, dim_date linked to fact_attendance and fact_payroll.</p>
                </div>
              </div>

              {/* Schema Entity Definition Cards */}
              <div className="panel-headline" style={{ marginTop: 32 }}>
                <div>
                  <h2>Dimensional &amp; Fact Table Inventory</h2>
                  <p>Verified table definitions, grain descriptions, and surrogate keys.</p>
                </div>
              </div>

              <div className="schema-card-grid">
                <div className="schema-card">
                  <div className="schema-card-header">
                    <span className="schema-card-title">dim_employee</span>
                    <span className="widget-pill pill-purple">SCD Type 2</span>
                  </div>
                  <p style={{ fontSize: 12.5, color: "var(--label-secondary)" }}>
                    Tracks employee career history, department reassignments, and plant transfers with effective date ranges.
                  </p>
                  <ul className="schema-field-list">
                    <li><span className="col-name">employee_key (PK)</span><span className="col-type">INTEGER AUTO</span></li>
                    <li><span className="col-name">emp_id</span><span className="col-type">TEXT (E10001..)</span></li>
                    <li><span className="col-name">is_current</span><span className="col-type">BOOLEAN (0/1)</span></li>
                    <li><span className="col-name">valid_from / valid_to</span><span className="col-type">DATE</span></li>
                  </ul>
                </div>

                <div className="schema-card">
                  <div className="schema-card-header">
                    <span className="schema-card-title">fact_attendance_daily</span>
                    <span className="widget-pill pill-cyan">216,813 Rows</span>
                  </div>
                  <p style={{ fontSize: 12.5, color: "var(--label-secondary)" }}>
                    Grain: One row per employee per calendar date. Captures first in, last out, computed hours, and OT.
                  </p>
                  <ul className="schema-field-list">
                    <li><span className="col-name">attendance_id (PK)</span><span className="col-type">INTEGER AUTO</span></li>
                    <li><span className="col-name">employee_key (FK)</span><span className="col-type">INTEGER</span></li>
                    <li><span className="col-name">date_key (FK)</span><span className="col-type">INTEGER</span></li>
                    <li><span className="col-name">status</span><span className="col-type">Present/Absent..</span></li>
                  </ul>
                </div>

                <div className="schema-card">
                  <div className="schema-card-header">
                    <span className="schema-card-title">fact_payroll_monthly</span>
                    <span className="widget-pill pill-green">7,078 Rows</span>
                  </div>
                  <p style={{ fontSize: 12.5, color: "var(--label-secondary)" }}>
                    Monthly reconciled salary disbursements, overtime payments, and tax deductions.
                  </p>
                  <ul className="schema-field-list">
                    <li><span className="col-name">payroll_id (PK)</span><span className="col-type">INTEGER AUTO</span></li>
                    <li><span className="col-name">employee_key (FK)</span><span className="col-type">INTEGER</span></li>
                    <li><span className="col-name">basic_salary</span><span className="col-type">REAL (PKR)</span></li>
                    <li><span className="col-name">paid_overtime_pay</span><span className="col-type">REAL (PKR)</span></li>
                  </ul>
                </div>

                <div className="schema-card">
                  <div className="schema-card-header">
                    <span className="schema-card-title">dim_department</span>
                    <span className="widget-pill pill-orange">14 Depts</span>
                  </div>
                  <p style={{ fontSize: 12.5, color: "var(--label-secondary)" }}>
                    Functional organization units across 4 manufacturing plants and corporate headquarters.
                  </p>
                  <ul className="schema-field-list">
                    <li><span className="col-name">department_key (PK)</span><span className="col-type">INTEGER AUTO</span></li>
                    <li><span className="col-name">dept_id</span><span className="col-type">TEXT (D01-D26)</span></li>
                    <li><span className="col-name">dept_name</span><span className="col-type">TEXT</span></li>
                    <li><span className="col-name">plant</span><span className="col-type">TEXT (FSD, KOR..)</span></li>
                  </ul>
                </div>
              </div>

              {/* Ghost Payroll Deep Dive Table */}
              <div className="panel-headline" style={{ marginTop: 36 }}>
                <div>
                  <h2>Ghost Payroll Forensics (Top Flagged Cases)</h2>
                  <p>15 separated employees receiving active paychecks post-termination date.</p>
                </div>
                <span className="widget-pill pill-red">PKR 3,782,469 Total Leakage</span>
              </div>

              <div className="apple-table-wrap">
                <table className="apple-table">
                  <thead>
                    <tr>
                      <th>Emp ID</th>
                      <th>Employee Name</th>
                      <th>Separation Date</th>
                      <th>Months Paid Post-Term</th>
                      <th>Total Leaked Amount</th>
                      <th>Remediation Status</th>
                    </tr>
                  </thead>
                  <tbody>
                    {ghostList.map((emp) => (
                      <tr key={emp.emp_id}>
                        <td className="mono" style={{ color: "var(--system-cyan)" }}>{emp.emp_id}</td>
                        <td style={{ fontWeight: 600 }}>{emp.full_name}</td>
                        <td className="mono" style={{ color: "var(--system-red)" }}>{emp.separation_date}</td>
                        <td className="mono">{emp.months_paid} paychecks</td>
                        <td className="mono" style={{ fontWeight: 750, color: "var(--system-red)" }}>PKR {emp.total_paid.toLocaleString()}</td>
                        <td><span className="widget-pill pill-red">Recovery Pending</span></td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>

              {/* Absenteeism by Plant */}
              <div className="panel-headline" style={{ marginTop: 36 }}>
                <div>
                  <h2>Plant Absenteeism Matrix</h2>
                  <p>Benchmarked across 6 months of reconciled daily attendance data.</p>
                </div>
              </div>

              <div className="apple-table-wrap">
                <table className="apple-table">
                  <thead>
                    <tr>
                      <th>Plant Location</th>
                      <th>Absent Days</th>
                      <th>Scheduled Work Days</th>
                      <th>Absenteeism Rate</th>
                      <th>Operational Impact</th>
                    </tr>
                  </thead>
                  <tbody>
                    {(warehouseData.absenteeism || []).map((ab) => (
                      <tr key={ab.plant}>
                        <td style={{ fontWeight: 600 }}>{ab.plant}</td>
                        <td className="mono">{ab.absent_days.toLocaleString()} days</td>
                        <td className="mono">{ab.work_days.toLocaleString()} days</td>
                        <td className="mono" style={{ fontWeight: 750, color: ab.rate > 4.0 ? "var(--system-red)" : "var(--system-cyan)" }}>{ab.rate}%</td>
                        <td>
                          <span className={`widget-pill ${ab.rate > 4.0 ? "pill-red" : "pill-green"}`}>
                            {ab.rate > 4.0 ? "Critical High" : "Acceptable"}
                          </span>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>

            </div>
          </section>
        )}

        {/* ================= TAB: CFO OVERTIME AUDIT ================= */}
        {activeTab === "cfo" && (
          <section className="tab-content-active">
            <div className="widget-grid">
              <div className="widget-card">
                <div className="widget-header">
                  <span className="widget-title">Approved OT Paid</span>
                  <span className="widget-pill pill-red">Financial Surge</span>
                </div>
                <div className="widget-value">36,402 <span style={{ fontSize: 20 }}>Hrs</span></div>
                <div className="widget-subtitle">PKR 3,475,158 Paid to Workforce</div>
              </div>

              <div className="widget-card">
                <div className="widget-header">
                  <span className="widget-title">Biometric Worked OT</span>
                  <span className="widget-pill pill-cyan">Physical Reality</span>
                </div>
                <div className="widget-value">29,116 <span style={{ fontSize: 20 }}>Hrs</span></div>
                <div className="widget-subtitle">Actual Turnstile Card Swipes</div>
              </div>

              <div className="widget-card">
                <div className="widget-header">
                  <span className="widget-title">Phantom Overtime Leak</span>
                  <span className="widget-pill pill-red">+23.5% Surge</span>
                </div>
                <div className="widget-value" style={{ color: "var(--system-red)" }}>+7,286 <span style={{ fontSize: 20 }}>Hrs</span></div>
                <div className="widget-subtitle">Discrepancy Between Form &amp; Machine</div>
              </div>

              <div className="widget-card">
                <div className="widget-header">
                  <span className="widget-title">Faisalabad Plant Disparity</span>
                  <span className="widget-pill pill-orange">63.0% of Total</span>
                </div>
                <div className="widget-value" style={{ color: "var(--system-orange)" }}>4,588.5 <span style={{ fontSize: 20 }}>Hrs</span></div>
                <div className="widget-subtitle">Severe Manager Approval Inflation</div>
              </div>
            </div>

            <div className="apple-panel">
              <div className="panel-headline">
                <div>
                  <h2>Executive Audit Briefing &amp; Key Findings</h2>
                  <p>Comprehensive forensic audit of 6-month reconciled data warehouse (April to Sept 2026).</p>
                </div>
                <span className="widget-pill pill-red">High Priority Findings</span>
              </div>

              <div className="apple-callout callout-red">
                <div className="callout-icon">!</div>
                <div className="callout-body">
                  <h3>1. Faisalabad Plant Generates 63.0% of Company Overtime Leakage</h3>
                  <p>
                    Out of 7,286 total unverified paid overtime hours, <strong>4,588.5 hours</strong> originate exclusively from the Faisalabad Plant. 
                    Approved hours were 14,417.5 vs 9,829.0 actual biometric hours. This indicates systemic paper-sheet sign-offs without turnstile punch validation.
                  </p>
                </div>
              </div>

              <div className="apple-callout callout-orange">
                <div className="callout-icon">2</div>
                <div className="callout-body">
                  <h3>2. 3,687 Approved Requests Had Zero Biometric Presence</h3>
                  <p>
                    Forensic query <strong>q06</strong> uncovered 3,687 overtime approval requests granted for employees who either left exactly at shift end or were logged as 
                    Absent, on Leave, or on Weekly Off on that specific date. Over PKR 1.42M was disbursed without physical worker presence.
                  </p>
                </div>
              </div>

              <div className="apple-callout callout-blue">
                <div className="callout-icon">3</div>
                <div className="callout-body">
                  <h3>3. Ghost Payroll: PKR 3,782,469 Paid to 15 Terminated Employees</h3>
                  <p>
                    15 separated employees continued receiving 52 monthly salary payments after their official resignation/termination date. 
                    <strong>Umair Baloch (E10471)</strong> received PKR 682,100 across 5 months post-separation. Automated HRIS termination webhooks are mandated.
                  </p>
                </div>
              </div>

              <div className="apple-callout callout-green">
                <div className="callout-icon">4</div>
                <div className="callout-body">
                  <h3>4. Hardware Clock Bug Sanitized on DEV-SITE-01 Terminal</h3>
                  <p>
                    Biometric terminal DEV-SITE-01 experienced an internal hardware clock jump of exactly +60 minutes starting July 1, 2026. 
                    Our Stage 2 transformation pipeline programmatically subtracted 60 minutes across all 48,146 affected punches, preventing false tardiness penalties.
                  </p>
                </div>
              </div>

              <div className="panel-headline" style={{ marginTop: 28 }}>
                <div>
                  <h2>Monthly Overtime Progression (Biometric vs Paid)</h2>
                  <p>Tracking the widening gap between machine punches and approved payroll disbursements.</p>
                </div>
              </div>

              <div className="apple-table-wrap">
                <table className="apple-table">
                  <thead>
                    <tr>
                      <th>Month</th>
                      <th>Biometric Worked (Hrs)</th>
                      <th>Approved Paid (Hrs)</th>
                      <th>Leakage Gap (Hrs)</th>
                      <th>Total OT Cost</th>
                      <th>Leakage %</th>
                    </tr>
                  </thead>
                  <tbody>
                    {(warehouseData.ot_trend || []).map((row) => {
                      const pct = ((row.gap_hours / row.approved_hours) * 100).toFixed(1);
                      return (
                        <tr key={row.month}>
                          <td className="mono" style={{ fontWeight: 700, color: "var(--system-cyan)" }}>{row.month}</td>
                          <td className="mono">{row.computed_hours.toLocaleString()} hrs</td>
                          <td className="mono" style={{ color: "var(--system-orange)", fontWeight: 600 }}>{row.approved_hours.toLocaleString()} hrs</td>
                          <td className="mono" style={{ color: "var(--system-red)", fontWeight: 700 }}>+{row.gap_hours.toLocaleString()} hrs</td>
                          <td className="mono">PKR {row.paid_cost.toLocaleString()}</td>
                          <td>
                            <span className="widget-pill pill-red">+{pct}%</span>
                          </td>
                        </tr>
                      );
                    })}
                  </tbody>
                </table>
              </div>

              <div className="panel-headline" style={{ marginTop: 32 }}>
                <div>
                  <h2>Plant-by-Plant Overtime Gap Analysis</h2>
                  <p>Location-specific breakdown demonstrating Faisalabad's overwhelming share of unverified hours.</p>
                </div>
              </div>

              <div className="apple-table-wrap">
                <table className="apple-table">
                  <thead>
                    <tr>
                      <th>Manufacturing Facility</th>
                      <th>Biometric Worked (Hrs)</th>
                      <th>Approved Paid (Hrs)</th>
                      <th>Unverified Paid Gap</th>
                      <th>Share of Total Leakage</th>
                    </tr>
                  </thead>
                  <tbody>
                    {(warehouseData.plant_ot || []).map((p) => {
                      const share = ((p.gap_hours / 7286.0) * 100).toFixed(1);
                      return (
                        <tr key={p.plant}>
                          <td style={{ fontWeight: 600 }}>{p.plant}</td>
                          <td className="mono">{p.computed_hours.toLocaleString()} hrs</td>
                          <td className="mono">{p.approved_hours.toLocaleString()} hrs</td>
                          <td className="mono" style={{ color: p.gap_hours > 2000 ? "var(--system-red)" : "var(--system-orange)", fontWeight: 700 }}>
                            +{p.gap_hours.toLocaleString()} hrs
                          </td>
                          <td>
                            <span className={`widget-pill ${p.gap_hours > 2000 ? "pill-red" : "pill-cyan"}`}>
                              {share}%
                            </span>
                          </td>
                        </tr>
                      );
                    })}
                  </tbody>
                </table>
              </div>
            </div>
          </section>
        )}

        {/* ================= TAB: RECRUITMENT FUNNEL ================= */}
        {activeTab === "funnel" && (
          <section className="tab-content-active">
            <div className="widget-grid">
              <div className="widget-card">
                <div className="widget-header">
                  <span className="widget-title">Total Applications</span>
                  <span className="widget-pill pill-cyan">14 Departments</span>
                </div>
                <div className="widget-value">1,400</div>
                <div className="widget-subtitle">April – September 2026 Intake</div>
              </div>

              <div className="widget-card">
                <div className="widget-header">
                  <span className="widget-title">Overall Conversion</span>
                  <span className="widget-pill pill-green">Yield Rate</span>
                </div>
                <div className="widget-value">5.3%</div>
                <div className="widget-subtitle">74 Hired Candidates Finalized</div>
              </div>

              <div className="widget-card">
                <div className="widget-header">
                  <span className="widget-title">Median Time to Hire</span>
                  <span className="widget-pill pill-orange">Speed to Fill</span>
                </div>
                <div className="widget-value">33 <span style={{ fontSize: 20 }}>Days</span></div>
                <div className="widget-subtitle">From Application to Offer Acceptance</div>
              </div>

              <div className="widget-card">
                <div className="widget-header">
                  <span className="widget-title">Major Bottleneck</span>
                  <span className="widget-pill pill-red">-173 Drop</span>
                </div>
                <div className="widget-value" style={{ color: "var(--system-red)" }}>34.2%</div>
                <div className="widget-subtitle">Interview ➔ Offer Conversion</div>
              </div>
            </div>

            <div className="apple-panel">
              <div className="panel-headline">
                <div>
                  <h2>
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--system-cyan)" strokeWidth="2"><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/></svg>
                    Talent Acquisition Continuous Funnel
                  </h2>
                  <p>Interactive stage inspector. Click any stage to examine candidate velocity and drop-off reasons.</p>
                </div>
                <div style={{ display: "flex", gap: 8 }}>
                  <span className="widget-pill pill-cyan">1,400 Inflow</span>
                  <span className="widget-pill pill-green">74 Outflow</span>
                </div>
              </div>

              {/* Custom SVG Tapered Funnel */}
              <div className="funnel-canvas-wrap">
                <svg className="funnel-svg" viewBox="0 0 1000 120" preserveAspectRatio="none">
                  <defs>
                    <linearGradient id="appleGrad1" x1="0%" y1="0%" x2="100%" y2="0%">
                      <stop offset="0%" stopColor="#0A84FF" stopOpacity="0.9" />
                      <stop offset="100%" stopColor="#5E5CE6" stopOpacity="0.9" />
                    </linearGradient>
                    <linearGradient id="appleGrad2" x1="0%" y1="0%" x2="100%" y2="0%">
                      <stop offset="0%" stopColor="#5E5CE6" stopOpacity="0.9" />
                      <stop offset="100%" stopColor="#BF5AF2" stopOpacity="0.9" />
                    </linearGradient>
                    <linearGradient id="appleGrad3" x1="0%" y1="0%" x2="100%" y2="0%">
                      <stop offset="0%" stopColor="#BF5AF2" stopOpacity="0.9" />
                      <stop offset="100%" stopColor="#FF9F0A" stopOpacity="0.9" />
                    </linearGradient>
                    <linearGradient id="appleGrad4" x1="0%" y1="0%" x2="100%" y2="0%">
                      <stop offset="0%" stopColor="#FF9F0A" stopOpacity="0.9" />
                      <stop offset="100%" stopColor="#30D158" stopOpacity="0.9" />
                    </linearGradient>
                  </defs>

                  <polygon points="20,10 220,20 220,100 20,110" fill="url(#appleGrad1)" opacity="0.95"/>
                  <polygon points="220,20 440,32 440,88 220,100" fill="url(#appleGrad2)" opacity="0.95"/>
                  <polygon points="440,32 680,44 680,76 440,88" fill="url(#appleGrad3)" opacity="0.95"/>
                  <polygon points="680,44 980,50 980,70 680,76" fill="url(#appleGrad4)" opacity="0.95"/>

                  <line x1="220" y1="10" x2="220" y2="110" stroke="rgba(255,255,255,0.45)" strokeWidth="1.5" strokeDasharray="3,3"/>
                  <line x1="440" y1="20" x2="440" y2="100" stroke="rgba(255,255,255,0.45)" strokeWidth="1.5" strokeDasharray="3,3"/>
                  <line x1="680" y1="35" x2="680" y2="85" stroke="rgba(255,255,255,0.45)" strokeWidth="1.5" strokeDasharray="3,3"/>
                </svg>
              </div>

              <div className="stage-card-strip">
                {stageDetails.map((stg, idx) => (
                  <div
                    key={stg.name}
                    className={`stage-step-card ${selectedStage === idx ? "active" : ""}`}
                    onClick={() => setSelectedStage(idx)}
                  >
                    <div className="stage-step-num">Stage 0{idx + 1}</div>
                    <div className="stage-step-name">{stg.name}</div>
                    <div className="stage-step-val">{stg.count.toLocaleString()}</div>
                    <div className="stage-step-meta">
                      {idx === 0 ? "Baseline 100%" : `${stg.passPct} pass (${stg.drop})`}
                    </div>
                  </div>
                ))}
              </div>

              <div className="spotlight-card">
                <div className="spotlight-info">
                  <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 8 }}>
                    <span className="widget-pill pill-cyan">Stage 0{selectedStage + 1} Spotlight</span>
                    <span className={`widget-pill ${currentStage.status.includes("Bottleneck") ? "pill-red" : "pill-green"}`}>
                      {currentStage.status}
                    </span>
                  </div>
                  <h3>{currentStage.name}: {currentStage.desc}</h3>
                  <p style={{ marginTop: 6 }}><strong>Operational Directive:</strong> {currentStage.advice}</p>
                </div>
                <div className="spotlight-metric">
                  <div className="num" style={{ color: "var(--system-cyan)" }}>{currentStage.passPct}</div>
                  <div className="label">Conversion Rate</div>
                </div>
                <div className="spotlight-metric">
                  <div className="num" style={{ color: "var(--system-orange)" }}>{currentStage.medianDays}</div>
                  <div className="label">Median Duration</div>
                </div>
              </div>

              <div className="simulator-box">
                <div className="sim-header">
                  <div>
                    <h3>Interactive Recruitment Yield Simulator</h3>
                    <p style={{ fontSize: 13, color: "var(--label-secondary)" }}>
                      Adjust conversion levers in real-time to forecast target hires and pipeline velocity.
                    </p>
                  </div>
                  <div className="sim-result-badge">
                    <div>
                      <div style={{ fontSize: 11, color: "var(--label-secondary)", textTransform: "uppercase" }}>Simulated Hires</div>
                      <div className="sim-hires">{simHired} Candidates</div>
                    </div>
                    <div className="sim-delta">
                      {simDelta >= 0 ? `+${simDelta} vs baseline` : `${simDelta} vs baseline`}
                    </div>
                  </div>
                </div>

                <div className="sim-sliders-grid">
                  <div className="sim-control">
                    <div className="sim-label-row">
                      <span>Screening Pass Rate</span>
                      <span>{screenPct}% ({simScreened})</span>
                    </div>
                    <input
                      type="range"
                      className="apple-slider"
                      min="20"
                      max="80"
                      step="0.5"
                      value={screenPct}
                      onChange={(e) => setScreenPct(parseFloat(e.target.value))}
                    />
                  </div>

                  <div className="sim-control">
                    <div className="sim-label-row">
                      <span>Interview Pass Rate</span>
                      <span>{interviewPct}% ({simInterviewed})</span>
                    </div>
                    <input
                      type="range"
                      className="apple-slider"
                      min="15"
                      max="70"
                      step="0.5"
                      value={interviewPct}
                      onChange={(e) => setInterviewPct(parseFloat(e.target.value))}
                    />
                  </div>

                  <div className="sim-control">
                    <div className="sim-label-row">
                      <span>Offer Extension Rate (Bottleneck)</span>
                      <span>{offerPct}% ({simOffered})</span>
                    </div>
                    <input
                      type="range"
                      className="apple-slider"
                      min="15"
                      max="65"
                      step="0.5"
                      value={offerPct}
                      onChange={(e) => setOfferPct(parseFloat(e.target.value))}
                    />
                  </div>

                  <div className="sim-control">
                    <div className="sim-label-row">
                      <span>Offer Acceptance Rate</span>
                      <span>{acceptPct}% ({simHired})</span>
                    </div>
                    <input
                      type="range"
                      className="apple-slider"
                      min="50"
                      max="100"
                      step="0.5"
                      value={acceptPct}
                      onChange={(e) => setAcceptPct(parseFloat(e.target.value))}
                    />
                  </div>
                </div>

                <div style={{ marginTop: 18, textAlign: "right" }}>
                  <button
                    className="apple-ghost-btn"
                    onClick={() => {
                      setScreenPct(48.7);
                      setInterviewPct(38.6);
                      setOfferPct(34.2);
                      setAcceptPct(82.2);
                    }}
                  >
                    Reset Baseline Values
                  </button>
                </div>
              </div>

              <div className="panel-headline" style={{ marginTop: 28 }}>
                <div>
                  <h2>Departmental Inflow &amp; Yield Matrix</h2>
                  <p>14 functional departments sorted by recruiting volume.</p>
                </div>
                <input
                  type="text"
                  className="search-pill-input"
                  placeholder="Filter departments (e.g. Cutting, Spinning)..."
                  value={deptFilter}
                  onChange={(e) => setDeptFilter(e.target.value)}
                />
              </div>

              <div className="apple-table-wrap">
                <table className="apple-table">
                  <thead>
                    <tr>
                      <th>Dept Code</th>
                      <th>Department Name</th>
                      <th>Applications</th>
                      <th>Hired</th>
                      <th>Rejected</th>
                      <th>Declined</th>
                      <th>Conversion Bar</th>
                      <th>Yield %</th>
                    </tr>
                  </thead>
                  <tbody>
                    {filteredDepts.map((d) => {
                      const yieldPct = ((d.hired / d.applications) * 100).toFixed(1);
                      return (
                        <tr key={d.code}>
                          <td className="mono" style={{ color: "var(--system-cyan)" }}>{d.code}</td>
                          <td style={{ fontWeight: 600 }}>{d.name}</td>
                          <td className="mono">{d.applications}</td>
                          <td className="mono" style={{ color: "var(--system-green)", fontWeight: 700 }}>{d.hired}</td>
                          <td className="mono" style={{ color: "var(--label-secondary)" }}>{d.rejected}</td>
                          <td className="mono" style={{ color: "var(--system-orange)" }}>{d.declined}</td>
                          <td className="table-bar-cell">
                            <div className="table-bar-bg">
                              <div className="table-bar-fill" style={{ width: `${Math.min(100, yieldPct * 8)}%` }}></div>
                            </div>
                          </td>
                          <td className="mono" style={{ fontWeight: 700 }}>{yieldPct}%</td>
                        </tr>
                      );
                    })}
                  </tbody>
                </table>
              </div>
            </div>
          </section>
        )}

        {/* ================= TAB: 22/22 DATA QUALITY SUITE ================= */}
        {activeTab === "dq" && (
          <section className="tab-content-active">
            <div className="widget-grid">
              <div className="widget-card">
                <div className="widget-header">
                  <span className="widget-title">Total DQ Assertions</span>
                  <span className="widget-pill pill-green">Suite Coverage</span>
                </div>
                <div className="widget-value">22 / 22</div>
                <div className="widget-subtitle">100% Passed Across All Domains</div>
              </div>

              <div className="widget-card">
                <div className="widget-header">
                  <span className="widget-title">Failed Assertions</span>
                  <span className="widget-pill pill-cyan">Zero Tolerance</span>
                </div>
                <div className="widget-value" style={{ color: "var(--system-green)" }}>0</div>
                <div className="widget-subtitle">No Data Quality Violations</div>
              </div>

              <div className="widget-card">
                <div className="widget-header">
                  <span className="widget-title">Incremental Load</span>
                  <span className="widget-pill pill-purple">Month 7 Verified</span>
                </div>
                <div className="widget-value">322,143</div>
                <div className="widget-subtitle">Punches Idempotently Accepted</div>
              </div>

              <div className="widget-card">
                <div className="widget-header">
                  <span className="widget-title">Audit Trail Status</span>
                  <span className="widget-pill pill-green">Logged</span>
                </div>
                <div className="widget-value">Active</div>
                <div className="widget-subtitle">Recorded in dq_results Table</div>
              </div>
            </div>

            <div className="apple-panel">
              <div className="panel-headline">
                <div>
                  <h2>Enterprise Data Quality Verification Suite</h2>
                  <p>Automated test assertions covering schema integrity, biometric physics, deduplication, and financial reconciliation.</p>
                </div>

                <div style={{ display: "flex", gap: 6, flexWrap: "wrap" }}>
                  {["ALL", "Ingestion", "Deduplication", "Attendance", "Payroll", "Referential"].map((cat) => (
                    <button
                      key={cat}
                      className={`apple-ghost-btn ${dqCategory === cat ? "active" : ""}`}
                      style={{
                        background: dqCategory === cat ? "rgba(255, 255, 255, 0.2)" : undefined,
                        borderColor: dqCategory === cat ? "rgba(255, 255, 255, 0.4)" : undefined,
                      }}
                      onClick={() => setDqCategory(cat)}
                    >
                      {cat}
                    </button>
                  ))}
                </div>
              </div>

              <div className="apple-table-wrap">
                <table className="apple-table">
                  <thead>
                    <tr>
                      <th>Check ID</th>
                      <th>Rule Name</th>
                      <th>Category</th>
                      <th>Assertion Scope</th>
                      <th>Result</th>
                    </tr>
                  </thead>
                  <tbody>
                    {filteredDq.map((chk) => (
                      <tr key={chk.id}>
                        <td className="mono" style={{ color: "var(--system-cyan)", fontWeight: 700 }}>{chk.id}</td>
                        <td style={{ fontWeight: 600 }}>{chk.name}</td>
                        <td>
                          <span className="widget-pill pill-purple">{chk.category}</span>
                        </td>
                        <td style={{ color: "var(--label-secondary)" }}>{chk.desc}</td>
                        <td>
                          <span className="status-badge">
                            <span className="status-dot"></span>
                            {chk.status}
                          </span>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          </section>
        )}

      </main>
    </>
  );
}
