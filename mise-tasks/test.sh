#!/bin/bash
set -e

# MISE_TASK_USAGE: arg [day] help="Day to test (0 = all)" default="0"
: ${usage_day:=0}
if [ ${usage_day} -eq 0 ]; then
  uv run pytest solutions/ -v
else
  DAY=$(printf "%02d" ${usage_day})
  uv run pytest solutions/day${DAY}.py -v
fi
