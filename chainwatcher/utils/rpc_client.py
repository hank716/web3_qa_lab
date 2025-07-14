import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import requests
import logging
import yaml

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load config using absolute path
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config", "node_config.yaml")
CONFIG_PATH = os.path.abspath(CONFIG_PATH)

with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f)
    RPC_URL = config.get("rpc_url")

def call_rpc(method, params=None):
    try:
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params or [],
            "id": 1
        }
        response = requests.post(RPC_URL, json=payload, timeout=10)
        return response.json()
    except Exception as e:
        logging.exception("RPC call failed")
        return None
