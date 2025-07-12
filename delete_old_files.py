import os

# Delete DayM-N.py files from Day 1 to Day 31 and N = 1 to 3
for day in range(1, 32):
    for part in range(1, 4):
        filename = f"Day{day}-{part}.py"
        if os.path.exists(filename):
            os.remove(filename)
            print(f"Deleted: {filename}")
        else:
            print(f"Skipped (not found): {filename}")
