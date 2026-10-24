from PIL import Image, ImageDraw, ImageFont
import pathlib

W, H = 2200, 1550
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def font(size, bold=False):
    p = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    return ImageFont.truetype(p, size)

TITLE = font(44, True)
SUB = font(24)
HDR = font(24, True)
COL = font(20)
COLB = font(20, True)
SMALL = font(20)
NOTE = font(20)

# Banner, like the example
d.rounded_rectangle([20, 20, W-20, 130], radius=18, fill=(18, 53, 91))
d.text((60, 48), "Indus Weave - Star Schema ERD", font=TITLE, fill="white", anchor="lt")
d.text((60, 98), "Attendance belongs to Workforce; Payroll consumes attendance results.", font=SUB, fill=(205, 216, 228), anchor="lt")

ROW_H = 32
HDR_H = 52
tables = {}

def add_table(key, x, y, w, color, title, cols):
    h = HDR_H + len(cols) * ROW_H
    tables[key] = {"x": x, "y": y, "w": w, "h": h, "title": title, "cols": cols, "color": color,
                   "row_y": {c[0]: y + HDR_H + i*ROW_H + ROW_H//2 for i, c in enumerate(cols)}}
    return tables[key]

BLUE = (31, 111, 178)
GREEN = (14, 159, 110)
PURPLE = (123, 94, 167)
ORANGE = (230, 126, 34)
NAVY = (18, 53, 91)
TEAL = (15, 118, 110)
RED = (214, 69, 69)
VIOLET = (108, 92, 231)

add_table("dim_employee", 60, 160, 560, BLUE, "dim_employee  (SCD2)", [
    ("employee_key", "INT", "PK"), ("emp_id", "TEXT", ""), ("dept_id", "TEXT", ""),
    ("grade", "TEXT", ""), ("valid_from", "TEXT", ""), ("valid_to", "TEXT", ""), ("is_current", "INT", ""),
])
add_table("dim_department", 820, 160, 560, GREEN, "dim_department", [
    ("dept_id", "TEXT", "PK"), ("dept_name", "TEXT", ""), ("plant", "TEXT", ""), ("cost_center", "TEXT", ""),
])
add_table("dim_shift", 1580, 160, 560, PURPLE, "dim_shift", [
    ("shift_code", "TEXT", "PK"), ("start_time", "TEXT", ""), ("end_time", "TEXT", ""),
])
add_table("fact_attendance", 820, 540, 560, NAVY, "fact_attendance_daily", [
    ("emp_id, work_date", "TEXT", "PK"), ("employee_key", "INT", "FK"), ("dept_id", "TEXT", "FK"),
    ("shift_code", "TEXT", "FK"), ("status", "TEXT", ""), ("worked_hours", "REAL", ""), ("overtime_hours", "REAL", ""),
])
add_table("dim_date", 1580, 540, 560, ORANGE, "dim_date", [
    ("date", "TEXT", "PK"), ("year", "INT", ""), ("month", "INT", ""), ("day_of_week", "TEXT", ""),
])
add_table("fact_leave", 60, 960, 560, TEAL, "fact_leave_day", [
    ("emp_id, leave_date", "TEXT", "PK"), ("leave_type", "TEXT", "PK"), ("request_id", "TEXT", ""),
])
add_table("fact_overtime", 820, 960, 560, RED, "fact_overtime_approved", [
    ("request_id", "TEXT", "PK"), ("emp_id", "TEXT", ""), ("ot_date", "TEXT", ""), ("approved_hours", "REAL", ""),
])
add_table("fact_payroll", 1580, 960, 560, VIOLET, "fact_payroll_line", [
    ("line_id", "TEXT", "PK"), ("payroll_month", "TEXT", ""), ("emp_id", "TEXT", ""),
    ("component", "TEXT", ""), ("amount", "REAL", ""), ("units", "REAL", ""),
])

def label_1n(x, y, txt):
    d.ellipse([x-12, y-12, x+12, y+12], fill="white", outline=(30,30,30), width=2)
    d.text((x, y), txt, font=font(18, True), fill=(20,20,20), anchor="mm")

ENDPOINTS = []
def line_1n(x1, y1, x2, y2):
    d.line([(x1, y1), (x2, y2)], fill=(30, 53, 91), width=3)
    ENDPOINTS.append((x1, y1, "1"))
    ENDPOINTS.append((x2, y2, "N"))
    label_1n(x1, y1, "1")
    label_1n(x2, y2, "N")

# Main star: dims to attendance
line_1n(620, 280, 820, 600)  # employee to attendance, top-left corner area
line_1n(1100, 360, 1100, 540)  # department down to attendance
line_1n(1580, 260, 1380, 540)  # shift to attendance
line_1n(1580, 640, 1380, 640)  # date to attendance, horizontal
# Shared employee/date: attendance to other facts, as in the example
line_1n(820, 800, 620, 960)  # attendance to leave
line_1n(1100, 820, 1100, 960)  # attendance to overtime
line_1n(1380, 800, 1580, 960)  # attendance to payroll

# Tables on top of lines
for key, t in tables.items():
    x, y, w, h = t["x"], t["y"], t["w"], t["h"]
    d.rounded_rectangle([x, y, x+w, y+h], radius=14, fill="white", outline=t["color"], width=3)
    # header, clip by drawing a rounded top only via rectangle + cover bottom corners
    d.rounded_rectangle([x, y, x+w, y+HDR_H], radius=14, fill=t["color"])
    d.rectangle([x, y+HDR_H-14, x+w, y+HDR_H], fill=t["color"])
    d.text((x+w//2, y+HDR_H//2), t["title"], font=HDR, fill="white", anchor="mm")
    for i, (name, typ, kind) in enumerate(t["cols"]):
        ry = y + HDR_H + i*ROW_H
        if i % 2 == 1:
            d.rectangle([x+2, ry, x+w-2, ry+ROW_H], fill=(242, 247, 251))
        label = f"{kind}  {name}" if kind else f"      {name}"
        f = COLB if kind else COL
        d.text((x+16, ry+ROW_H//2), label, font=f, fill=(20,20,20), anchor="lm")
        d.text((x+w-16, ry+ROW_H//2), typ, font=COL, fill=(70,90,110), anchor="rm")

# Redraw 1/N labels on top of tables, so they are fully visible
for (lx, ly, lt) in ENDPOINTS:
    label_1n(lx, ly, lt)

# Bottom legend + notes
d.rounded_rectangle([20, 1260, W-20, 1520], radius=14, fill=(240, 247, 251), outline=(200,210,220), width=2)
d.text((50, 1285), "PK  Primary Key", font=COLB, fill=(20,20,20), anchor="lt")
d.text((50, 1325), "FK  Foreign Key", font=COLB, fill=(20,20,20), anchor="lt")
d.text((50, 1365), "INT  Integer", font=COL, fill=(20,20,20), anchor="lt")
d.text((50, 1405), "TEXT  Variable Character", font=COL, fill=(20,20,20), anchor="lt")
d.text((50, 1445), "REAL  Decimal", font=COL, fill=(20,20,20), anchor="lt")
d.text((450, 1285), "Schema Notes:", font=COLB, fill=(20,20,20), anchor="lt")
d.text((450, 1325), "- fact_attendance_daily is the central fact table (star schema).", font=NOTE, fill=(40,40,40), anchor="lt")
d.text((450, 1365), "- Dimensions (employee, department, shift, date) give descriptive context.", font=NOTE, fill=(40,40,40), anchor="lt")
d.text((450, 1405), "- Fact-to-fact lines show shared employee and date, not a direct FK.", font=NOTE, fill=(40,40,40), anchor="lt")
d.text((450, 1445), "- Full columns and FKs are in warehouse/ddl/warehouse.sql.", font=NOTE, fill=(40,40,40), anchor="lt")

out = pathlib.Path("/home/hatch/workspace/indus-weave-hr-pipeline/warehouse/erd.png")
img.save(out, dpi=(200, 200))
print(f"saved {out} {img.size}")
