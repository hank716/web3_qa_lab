# ⛓️ ChainWatcher

**ChainWatcher** is a lightweight RPC performance and health monitoring tool for Ethereum nodes.  
It tracks latest block heights, response latency, and generates CSV + visual reports for performance analysis.

---

## 📌 Project Purpose

In decentralized environments like Ethereum, ensuring your node's RPC endpoint is responsive and up-to-date is critical for:

- Running validators
- Powering DApps or indexers
- Load balancing across providers (e.g. Infura, Alchemy, custom nodes)
- Debugging blockchain sync issues

**ChainWatcher** helps you monitor and compare node performance through automated tracking and historical reporting.

---

## 🧱 Architecture Overview

```
[start.sh]
   │
   ├── fetch_blocks.py  → Periodically fetches latest block + latency
   │                         ↳ stores to SQLite
   │
   ├── report_blocks.py → Generates:
   │                         - block_data.csv
   │                         - block_trend.png
   │                         - latency_trend.png
   │
   └── reports/YYYYMMDD_HHMMSS/
         ├── .db file (per run)
         ├── block_data.csv
         ├── block_trend.png
         └── latency_trend.png
```

---

## 🔧 Features

- ⛓ Periodically call `eth_blockNumber` via JSON-RPC
- 🕒 Record and monitor response latency
- 💾 Store all results in lightweight per-run `.db` (SQLite)
- 📊 Export results to CSV and visual `.png` reports
- 🧪 Includes Pytest-based test to verify RPC endpoint health
- 💼 Organized into per-run timestamped folders for easy comparison

---

## 🚀 Getting Started

```bash
git clone https://github.com/YOUR_NAME/chainwatcher.git
cd chainwatcher

# Create Python environment
conda create -n chainwatcher python=3.10
conda activate chainwatcher

# Install dependencies
pip install -r requirements.txt

# Add your RPC URL
cp config/node_config.yaml.example config/node_config.yaml
# Edit config/node_config.yaml:
# rpc_url: "https://mainnet.infura.io/v3/YOUR_PROJECT_ID"

# Start data collection
bash start.sh
```

---

## ⚙️ Custom Run Options

By default, `start.sh` runs 1 block fetch and generates reports.

You can customize:

```bash
# Fetch 10 times, 3 seconds apart
python3 scripts/fetch_blocks.py --count 10 --interval 3
```

All data is stored into a timestamped folder like:

```
reports/20250713_193217/
├── block_data.csv
├── block_trend.png
├── latency_trend.png
└── chainwatcher_20250713_193217.db
```

---

## 🧪 Running Tests

Includes a simple async RPC test via `pytest`:

```bash
pytest -s tests/
```

Test script: `tests/test_rpc_functionality.py`

---

## 📈 Example Visualizations

- **Block Trend** (x: time, y: block height)
- **Latency Trend** (x: time, y: seconds)

These can help you detect issues like:
- Slow response times
- Flat block height (stuck node)
- Performance spikes

---

## 🔮 Future Ideas

| Idea                          | Description |
|-------------------------------|-------------|
| Multi-RPC comparison          | Compare latency across Infura / Alchemy / local node |
| Alerts                        | Notify if latency > 2s or block stuck |
| Live dashboard                | Use Streamlit or Dash for interactive report |
| TheGraph integration          | Compare on-chain data vs. indexed view |
| GitHub Actions integration    | Run fetch & report on schedule |

---

## 📜 License

MIT — free for personal or commercial use. Contributions welcome!
