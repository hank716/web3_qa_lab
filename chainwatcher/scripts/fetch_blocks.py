import os
import sys
import yaml
import time
import requests
import logging
import argparse

import os
import utils.db as db_module
db_module.DB_PATH = os.environ.get("DB_PATH", "chainwatcher.db")

from utils.db import init_db, save_block_data

# load config/node_config.yaml
CONFIG_PATH = os.path.join(os.path.dirname(__file__), '..', 'config', 'node_config.yaml')
with open(CONFIG_PATH, 'r') as f:
    config = yaml.safe_load(f)

RPC_URL = config.get('rpc_url')
print(f"Loaded RPC_URL: {RPC_URL}")

# Ensure it can be executed from anywhere
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def fetch_latest_block():
    try:
        payload = {
            "jsonrpc": "2.0",
            "method": "eth_blockNumber",
            "params": [],
            "id": 1
        }
        start = time.time()
        response = requests.post(RPC_URL, json=payload, timeout=10)
        latency = time.time() - start

        result = response.json().get("result")
        if result:
            block_number = int(result, 16)
            save_block_data(block_number, latency)
            logging.info(f"✔ get block number {block_number}，latency {latency:.2f}s")
        else:
            logging.warning("⚠️ The returned result is empty")
    except Exception as e:
        logging.exception("❌ An error occurred")

def main():
    init_db()
    parser = argparse.ArgumentParser(description="Fetch latest Ethereum block.")
    parser.add_argument("--count", type=int, default=1, help="Number of times to fetch block data")
    parser.add_argument("--interval", type=float, default=5, help="Interval between fetches (seconds)")
    args = parser.parse_args()

    for _ in range(args.count):
        fetch_latest_block()
        time.sleep(args.interval)

if __name__ == "__main__":
    main()
