import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime
import os

# Input CSV file
TEST_DIR = Path("./test")
RESULTS_DIR = TEST_DIR / "results"

# Input the name of the csv to load here
# FILEPATH = RESULTS_DIR / "results_20251030_155057.csv"
# Or you can load the latest results CSV based on creation time
FILEPATH = max(RESULTS_DIR.glob("results_*.csv"), key=os.path.getctime) # get the most recently created file

#-----------------------------
# Create table figure from CSV
#-----------------------------

# ---- read & prep data ----
df = pd.read_csv(FILEPATH)[["size", "cutoff", "seed", "time_seconds"]]
# Coerce the time to 3dp for ease of reading
df["time_seconds"] = df["time_seconds"].round(3)
# Format size with commas
df["size"] = pd.to_numeric(df["size"], errors="coerce").astype("Int64")
df["size"] = df["size"].map(lambda x: f"{int(x):,}" if pd.notna(x) else "")

#-----------------------------
# Create figure with table
#-----------------------------

n_rows, n_cols = df.shape
fig_w = max(6, n_cols * 1.7)
fig_h = max(2.5, 1.0 + n_rows * 0.27)
fig, ax = plt.subplots(figsize=(fig_w, fig_h), dpi=200)
ax.axis("off")
TITLE = f"Merge Sort Benchmarks — {FILEPATH.name}"

table = ax.table(
    cellText=df.values,
    colLabels=df.columns.tolist(),
    loc="center",
    cellLoc="center",
    colLoc="center"
)

#-----------------------------
# Style the table
#-----------------------------

# basic styling
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.0, 1.2) #can do 1.0, 1.18 if more compact needed

# colors: choose your own!
header_color = "#abd5ea" 
row_a, row_b = "#ffffff", "#fafafa"
border = "#dddddd"

for (r, c), cell in table.get_celld().items():
    if r == 0:
        cell.set_text_props(weight="bold")
        cell.set_facecolor(header_color)
    else:
        cell.set_facecolor(row_a if r % 2 == 1 else row_b)
    cell.set_edgecolor(border)
    cell.set_linewidth(0.5)

plt.tight_layout(pad=0)

# -------------------------------
# Add title above table (relative to table position)
# -------------------------------

fig.canvas.draw()   # needed so the table has a valid bbox
renderer = fig.canvas.get_renderer()
tb = table.get_window_extent(renderer=renderer)
tb_fig = tb.transformed(fig.transFigure.inverted())

x = tb_fig.x0 + tb_fig.width / 2
y = tb_fig.y1 + 0.01  # padding above table (figure coords)
fig.text(x, y, TITLE, ha="center", va="bottom", fontsize=12, fontweight="bold")

#-----------------------------
# Save figure
#-----------------------------
OUT_PNG = FILEPATH.with_name(FILEPATH.stem + "_table.png") # Save as same name with _table suffix
fig.savefig(OUT_PNG, bbox_inches="tight", pad_inches=0) # To increase padding, change pad_inches to higher value
plt.close(fig)
