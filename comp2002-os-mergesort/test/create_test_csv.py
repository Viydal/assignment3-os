import os
import re
import itertools
import subprocess
from datetime import datetime
from pathlib import Path
import pandas as pd 

# -----------------------------
# USER-CONFIGURABLE PARAMETERS
# -----------------------------
SIZE_LIST = [pow(10,7), pow(10,8)] #TODO: cannot do more than 1 billion???? too long
CUTOFF_LIST = [0, 1, 2,3,4,5,6,7,8,9,10, 11, 12, 13, 14] #TODO: cannot do 20
RAND_SEED_LIST = [1, 2, 3] 

EXECUTABLE = "./test-mergesort"

# Output folder
TEST_DIR = Path("./test")
RESULTS_DIR = TEST_DIR / "results"

#-----------------------------
# Setup
#----------------------------

# Output of test-mergesort will be in this form: "Sorting 1000000 elements took 0.07 seconds."
# We create regex patterns to extract the size and time taken
LINE_RE = re.compile(r"Sorting\s+(\d+)\s+elements\s+took\s+([0-9]*\.?[0-9]+)\s+seconds\.", re.IGNORECASE)


RESULTS_DIR.mkdir(parents=True, exist_ok=True)
if not Path(EXECUTABLE).exists():
    raise SystemExit(f"Executable not found at '{EXECUTABLE}'. Build it first with `make` in project root.")

#-----------------------------
# Run tests and collect results
#----------------------------
total_combinations = len(SIZE_LIST) * len(CUTOFF_LIST) * len(RAND_SEED_LIST)
print(f"Running {total_combinations} tests...")
rows = []
for size, cutoff, seed in itertools.product(SIZE_LIST, CUTOFF_LIST, RAND_SEED_LIST):
    print(f"- Running test with size={size}, cutoff={cutoff}, seed={seed}", end="", flush=True) #flush=True to ensure print appears immediately
    result = subprocess.run([EXECUTABLE, str(size), str(cutoff), str(seed)],
                            capture_output=True, text=True)
    output = result.stdout.strip()
    print(f"\nDone, output is collected.")
    # If output is empty, raise an error
    if not output:
        raise ValueError(f"Error: No output from executable. Stderr:\n{result.stderr}")
    # Parse output
    match = LINE_RE.search(output)
    if not match:
        raise ValueError(f"Unexpected output format:\n{output}")
    parsed_size = int(match.group(1))
    print(f" Parsed size: {parsed_size}, time: {match.group(2)} seconds.")
    if parsed_size != size:
        #raise error and exit
        raise ValueError(f"Error: Parsed size {parsed_size} does not match expected size {size}.")
    time_taken = float(match.group(2))
    rows.append({
        "size": parsed_size,
        "cutoff": cutoff,
        "seed": seed,
        "time_seconds": time_taken
    })

#-----------------------------
# Save results to CSV
#-----------------------------
# Convert rows to dataframe
df = pd.DataFrame(rows)
# Save to CSV with timestamped filename
out_path = RESULTS_DIR / f"results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
df.to_csv(out_path, index=False)
