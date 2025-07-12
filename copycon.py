import os
import shutil

# Loop over days 3 to 31
for day in range(3, 32):
    for part in range(1, 4):  # For files DayN-1.py to DayN-3.py
        src = f"Day{day}-{part}.py"
        dest = f"Day{day}({part}).py"
        if os.path.exists(src):
            shutil.copyfile(src, dest)
            print(f"Copied {src} → {dest}")
        else:
            print(f"Skipped (not found): {src}")
