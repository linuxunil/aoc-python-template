#!/usr/bin/env -S uv run --script
# /// script
# dependencies = ["aocd<2"]
# ///
"""Download Advent of Code input(s). With no arg or 0, downloads all missing up to today."""

import os
import sys
from datetime import datetime
from pathlib import Path
from aocd import get_data

# Get day from argument or default to 0 (all missing)
day_arg = int(sys.argv[1]) if len(sys.argv) > 1 else 0

# Determine year
now = datetime.now()
if now.month == 12:
    year = now.year
else:
    year = int(os.getenv("AOC_YEAR", now.year))

# Create inputs directory
inputs_dir = Path("inputs")
inputs_dir.mkdir(exist_ok=True)

if day_arg == 0:
    # Download all missing inputs up to current day
    current_day = min(now.day, 25) if now.month == 12 else 25
    
    # Find existing inputs
    existing = set()
    for txt_file in inputs_dir.glob("*.txt"):
        try:
            day_num = int(txt_file.stem)
            existing.add(day_num)
        except ValueError:
            continue
    
    # Download missing days
    downloaded = []
    for day in range(1, current_day + 1):
        if day in existing:
            continue
        
        try:
            data = get_data(day=day, year=year)
            filename = inputs_dir / f"{day:02d}.txt"
            filename.write_text(data)
            url = f"https://adventofcode.com/{year}/day/{day}"
            print(f"✓ Day {day:2d}: {filename}")
            print(f"  Challenge: {url}")
            downloaded.append(day)
        except Exception as e:
            print(f"✗ Day {day:2d}: {e}")
    
    if not downloaded:
        print(f"All inputs up to day {current_day} already downloaded!")
    else:
        print(f"\nDownloaded {len(downloaded)} input(s)")
else:
    # Download specific day
    day = min(day_arg, 25)  # Cap at day 25
    day_str = f"{day:02d}"
    filename = inputs_dir / f"{day_str}.txt"
    
    if filename.exists():
        print(f"Input already exists: {filename}")
    else:
        try:
            data = get_data(day=day, year=year)
            filename.write_text(data)
            url = f"https://adventofcode.com/{year}/day/{day}"
            print(f"✓ Downloaded input to {filename}")
            print(f"  Challenge: {url}")
        except Exception as e:
            print(f"✗ Failed to download day {day}: {e}")
