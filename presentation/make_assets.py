import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import FancyBboxPatch
from pathlib import Path
BASE = Path(__file__).resolve().parents[1]

# ---------- ERD (Pillow, Workbench style) ----------
# The Pillow generator in make_erd.py draws real table grids with
# column types, PK/FK markers and orthogonal coloured joins. It is
# used instead of the old matplotlib box diagram, which looked poor.
import subprocess, sys
subprocess.run([sys.executable, str(BASE / "presentation" / "make_erd.py")], check=True)

# ---------- Slides (6 pages) ----------
slides = [
    ("Indus Weave Textiles\nWhy overtime cost keeps rising", "PeopleOps Data Hackathon  •  Solo  •  Python + SQL + SQLite\n6 months: 1 Apr – 30 Sep 2026  •  ~1,200 employees  •  Headcount fell, OT bill rose\n\nThe question: is this more work, or more paid-but-not-worked overtime?"),
    ("1  •  Paid OT is not worked OT", "Computed OT from biometric punches: 29,116 hours in 6 months\nApproved / paid OT: 36,402 hours\nGap: 7,286 hours\n\nApr gap: 856 hours  →  Sep gap: 1,748 hours\nOT bill: PKR 2.81m (Apr) → PKR 3.48m (Sep), +23.5%\nWorked OT was flat: 4,670 – 5,051 hours per month.\n\nAction: pay OT only from computed OT. No computed OT, no payment."),
    ("2  •  Approvals pay for days with no OT worked", "3,518 of 19,666 approved OT requests (17.9%)\nhad zero computed OT on that day.\n\n584 were Present days with zero OT after shift end.\nThe rest were Absent, Missing Punch, On Leave, Holiday or Weekly Off days.\n\nFaisalabad Plant is the worst: 14,418 paid vs 9,895 computed hours.\n\nAction: block approval when computed OT = 0, and audit Faisalabad first."),
    ("3  •  Pay did not stop on separation", "5 employees were paid after separation.\nTotal: PKR 1,983,188 across 21 employee-months.\n\nExample: Umair Baloch, separated 23 Apr 2026,\npaid May–Sep: PKR 682,100.\n\nOnly 1 employee-month had pay with zero Present days in that month —\nthe same control failure, not a workload story.\n\nAction: payroll must stop automatically on separation_date, with a monthly Q8 check."),
    ("How we proved it — and what to fix next", "• Raw loaded untouched, all TEXT, with _row_hash — 472,907 rows\n• DEV-SITE-01 clock was 60 min fast from 1 Jul 2026 — corrected, documented\n• 20,465 Missing Punch days (9.4%) — fix biometric check-out discipline\n• 20 employees already exceed full-year Annual leave in 6 months\n• DQ: 22/22 checks pass, raw = staging + rejected\n\nNext: computed-OT approval gate, separation payroll stop, SITE device audit."),
    ("Demo  •  What to look at", "Run:  python run_pipeline.py\nThen:  python analytics/run_queries.py\n\nQ1–Q10: analytics/q01..q10.sql  →  analytics/results/*.csv\nWarehouse: indus_weave.db  •  dim_employee (SCD2), dim_department, dim_shift, dim_date\nFacts: fact_attendance_daily, fact_leave_day, fact_overtime_approved, fact_payroll_line\n\nQuestions? I can explain every line — start with Q5, Q6, Q8."),
]
with PdfPages(BASE / "presentation" / "slides.pdf") as pdf:
    for title, body in slides:
        fig, ax = plt.subplots(figsize=(13.33, 7.5))
        ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
        ax.set_facecolor("#f8fafc")
        ax.text(0.5, 9.2, title, ha="left", va="top", fontsize=22, weight="bold", wrap=True)
        ax.text(0.5, 7.2, body, ha="left", va="top", fontsize=15, linespacing=1.6)
        ax.text(0.5, 0.4, "Indus Weave  •  PeopleOps Data Hackathon  •  5-minute demo", ha="left", fontsize=10, color="#555555")
        pdf.savefig(fig, bbox_inches="tight")
        plt.close()
print("slides.pdf written")
