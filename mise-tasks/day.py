#!/usr/bin/env -S uv run --script
# /// script
# dependencies = ["aocd<2"]
# ///
"""Setup a new Advent of Code day: download input and create solution file."""

import os
import sys
from datetime import datetime
from pathlib import Path
from aocd import get_data

# Get day from argument or default to current day
day = int(sys.argv[1]) if len(sys.argv) > 1 else 0

# If day is 0, use current day
if day == 0:
    day = min(datetime.now().day, 25)

# Cap at day 25
if day > 25:
    day = 25
day_str = f"{day:02d}"

# Determine year
now = datetime.now()
year = now.year if now.month == 12 else int(os.getenv("AOC_YEAR", now.year))

# Download input
inputs_dir = Path("inputs")
inputs_dir.mkdir(exist_ok=True)

input_file = inputs_dir / f"{day_str}.txt"
if not input_file.exists():
    data = get_data(day=day, year=year)
    input_file.write_text(data)
    url = f"https://adventofcode.com/{year}/day/{day}"
    print(f"✓ Downloaded input to {input_file}")
    print(f"  Challenge: {url}")
else:
    print(f"Input already exists: {input_file}")

# Create solution file
solution_file = Path(f"solutions/day{day_str}.py")
if not solution_file.exists():
    template = Path("template_day.py").read_text()
    # Update day number in get_input call
    solution = template.replace("get_input(1)", f"get_input({day})")
    solution_file.write_text(solution)
    print(f"✓ Created solution file: {solution_file}")
else:
    print(f"Solution file already exists: {solution_file}")
