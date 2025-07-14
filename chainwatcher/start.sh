#!/bin/bash
cd "$(dirname "$0")"

# Create a unique report folder and database
TS=$(date +%Y%m%d_%H%M%S)
REPORT_DIR="reports/$TS"
mkdir -p "$REPORT_DIR"

DB_FILE="$REPORT_DIR/chainwatcher_$TS.db"
export PYTHONPATH=$(pwd)
export DB_PATH="$DB_FILE"

touch "$DB_FILE"

echo "📡 Fetching block data..." 
python3 scripts/fetch_blocks.py --count 10 --interval 3

echo "📊 Generating block report..."
python3 scripts/report_blocks.py --output-dir "$REPORT_DIR" --db "$DB_FILE"

echo "✅ Done! Reports saved to $REPORT_DIR, DB: $DB_FILE"
