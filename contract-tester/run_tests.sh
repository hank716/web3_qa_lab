#!/bin/bash

timestamp=$(date "+%Y-%m-%d_%H%M")
report_dir="reports/$timestamp"
mkdir -p "$report_dir"

echo "🔧 Running forge tests..."
forge test > "$report_dir/forge_output.txt"

echo "⛽ Snapshotting gas usage..."
forge snapshot > "$report_dir/gas_report.txt"

echo "✅ Reports saved to $report_dir"
