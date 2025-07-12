import os
import re

# Regex to match files like DayN(M).py
pattern = re.compile(r"Day(\d+)\((\d)\)\.py")

for filename in os.listdir():
    match = pattern.match(filename)
    if match:
        day = int(match.group(1))
        part = match.group(2)
        new_name = f"Day{day:02d}({part}).py"
        if filename != new_name:
            os.rename(filename, new_name)
            print(f"Renamed: {filename} → {new_name}")
