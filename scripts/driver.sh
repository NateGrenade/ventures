#!/usr/bin/env bash
# Batch driver. Run from cron, NOT as a daemon — cron gives you a stop condition and an audit trail.
set -euo pipefail
cd "$(dirname "$0")/.."

CELL_COUNT="${CELL_COUNT:-8}"
MAX_TURNS="${MAX_TURNS:-30}"
COST_CEILING="${COST_CEILING:-15.00}"

git pull --rebase --autostash

i=0
for cell in $(python scripts/next_cells.py --count "$CELL_COUNT"); do
  i=$((i+1))
  claude -p "Sweep frontier cell ${cell} using the niche-sweep skill. Agent id: sweep-${i}." \
    --max-turns "$MAX_TURNS" > "logs/sweep-${cell}.log" 2>&1 &
done
wait

# deterministic passes, in order
python scripts/dedup.py --sweep
python scripts/verify_sources.py --unverified-only

# scrutiny over whatever the sweep produced
if [ -n "$(python scripts/list_ideas.py --status sandbox --paths)" ]; then
  claude -p "Run the niche-scrutiny skill over all ideas at status sandbox." --max-turns 60 \
    > "logs/scrutiny-$(date -I).log" 2>&1
fi

python scripts/build_index.py
python scripts/cost_report.py | tee "logs/cost-$(date -I).txt"

git add -A && git commit -m "batch: $(date -I)" && git push

echo "Batch complete. Ceiling was \$${COST_CEILING} — check the cost report."
