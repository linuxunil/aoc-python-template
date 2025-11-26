#!/bin/bash
set -e

# MISE_TASK_USAGE: arg [day] help="Day to run" default="0"
: ${usage_day:=0}
DAY=${usage_day:-$(date +%d)}
((DAY > 25)) && DAY=25
uv run python solutions/day$(printf "%02d" $DAY).py
