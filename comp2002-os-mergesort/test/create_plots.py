import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from pathlib import Path
from datetime import datetime
import os
import sys

# -----------------------------
# File paths
# -----------------------------
TEST_DIR = Path("./test")
RESULTS_DIR = TEST_DIR / "results"

# Choose control column and value:
#CONTROL must be one of: "size", "cutoff", "seed"
CONTROL = "seed" #"size" #"size"
CONTROL_VALUE = 1 #100000000  #change this to a value that exists in the chosen CONTROL column

# -----------------------------
# Load your desired CSV or use the latest CSV
# -----------------------------
FILEPATH = max(RESULTS_DIR.glob("results_*.csv"), key=os.path.getctime)  # most recently created file
# or: # FILEPATH = RESULTS_DIR / "results_20251030_155057.csv"
df = pd.read_csv(FILEPATH)[["size", "cutoff", "seed", "time_seconds"]]
df["time_seconds"] = df["time_seconds"].round(3)

# -----------------------------
# Determine axes & grouping by CONTROL
# -----------------------------
if CONTROL not in {"size", "cutoff", "seed"}:
    print(f"CONTROL must be one of 'size', 'cutoff', or 'seed'. Got: {CONTROL}")
    sys.exit(1)

if CONTROL == "size":
    x_col = "cutoff"
    group_col = "seed"
elif CONTROL == "cutoff":
    x_col = "size"
    group_col = "seed"
else:  # CONTROL == "seed"
    x_col = "cutoff"
    group_col = "size"

# -----------------------------
# Filter by CONTROL_VALUE
# -----------------------------
df_filt = df[df[CONTROL] == CONTROL_VALUE].copy()
if df_filt.empty:
    print(f"No rows found where {CONTROL} == {CONTROL_VALUE} in {FILEPATH.name}")
    sys.exit(0)

# -----------------------------
# Prepare plotting
# -----------------------------
# Pastel palette (I just create a simple hardcoded list here, feel free to change colors)
pastels = [
    "#aec7e8", "#ffbb78", "#98df8a", "#c5b0d5", "#f7b6d2",
    "#c49c94", "#dbdb8d", "#9edae5", "#c7c7c7", "#ff9896",
    "#bcbd22", "#17becf"
]

fig, ax = plt.subplots(figsize=(8, 5))

# Put grid behind the points
ax.set_axisbelow(True)
# Light transparent gray grid
ax.minorticks_on()  # enables minor ticks for a finer grid
ax.grid(True, which="major", axis="both", linestyle="-", linewidth=0.6, color="gray", alpha=0.35)
ax.grid(True, which="minor", axis="both", linestyle="-", linewidth=0.3, color="gray", alpha=0.18)


# Scatter per group
for i, (key, sub) in enumerate(df_filt.groupby(group_col)):
    color = pastels[i % len(pastels)]
    ax.scatter(
        sub[x_col],
        sub["time_seconds"],
        s=18, marker="o",
        label=f"{group_col}={key}",
        color=color
    )

# Y-axis scaling (scale together with padding)
ymin = df_filt["time_seconds"].min()
ymax = df_filt["time_seconds"].max()
pad = 0.05 * (ymax - ymin if ymax > ymin else max(ymax, 1.0))
ax.set_ylim(ymin - pad, ymax + pad)

# Labels
ax.set_xlabel(x_col)
ax.set_ylabel("time_seconds")

# Title
# Create a title with description of y-axis, x-axis, labels, and control
# However, in the title, reformat the CONTROL_VALUE to be commas for thousands
CONTROL_VALUE_FMT = f"{CONTROL_VALUE:,}"
TITLE=f"Merge Sort Benchmark Scatter Plot\nX-axis: {x_col}, Y-axis: time_seconds, grouped by label: {group_col}\nFiltered where Control {CONTROL}={CONTROL_VALUE_FMT}"
ax.set_title(TITLE, pad=15)

# Legend
# if group_col is "size", we can format group_col with commas using the same as f"{CONTROL_VALUE:,}"
if group_col == "size":
    ax.legend(title=group_col, fontsize=8, labels=[f"{int(x):,}" for x in df_filt[group_col].unique()])
else:
    ax.legend(title=group_col, fontsize=8)

# Tight layout and save PNG
OUT_PNG = FILEPATH.with_name(f"{FILEPATH.stem}_{CONTROL}_{CONTROL_VALUE}_scatter.png")
fig.savefig(OUT_PNG, bbox_inches="tight", pad_inches=0.1)
