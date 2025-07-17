from dotenv import load_dotenv
import os
load_dotenv()

import yaml
import requests
from web3 import Web3
from utils.report_writer import write_json_report
from datetime import datetime

rpc_url = os.getenv("INFURA_RPC")
if not rpc_url:
    raise ValueError("❌ 請設定 INFURA_RPC")

def test_block_hash_match():
    with open("config/settings.yaml", "r") as f:
        config = yaml.safe_load(f)

    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    report = {}
    success = False

    try:
        w3 = Web3(Web3.HTTPProvider(rpc_url))
        block_number = config["block_range"]["start_block"]
        report["block_number"] = block_number

        block = w3.eth.get_block(block_number, full_transactions=False)
        node_hash = block.hash.hex()
        report["node_hash"] = node_hash

        url = f"https://api.etherscan.io/api?module=proxy&action=eth_getBlockByNumber&tag={hex(block_number)}&boolean=true&apikey={os.getenv('ETHERSCAN_API_KEY', config['etherscan_api_key'])}"
        response = requests.get(url)
        etherscan_hash = response.json()["result"]["hash"]
        report["etherscan_hash"] = etherscan_hash

        report["status"] = "match" if node_hash == etherscan_hash else "mismatch"
        success = (node_hash == etherscan_hash)

    except Exception as e:
        report["status"] = "error"
        report["error"] = str(e)

    finally:
        write_json_report(report, f"reports/hash_diff_{timestamp}.json")

    assert success, f"比對失敗或發生錯誤：{report.get('error', 'hash mismatch')}"
