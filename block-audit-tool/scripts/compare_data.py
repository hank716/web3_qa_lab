from dotenv import load_dotenv
import os
import yaml
import requests
from web3 import Web3
from utils.report_writer import write_json_report
from utils.helpers import current_timestamp

load_dotenv()
rpc_url = os.getenv("INFURA_RPC")

with open("config/settings.yaml", "r") as f:
    config = yaml.safe_load(f)

block_number = config["block_range"]["start_block"]
w3 = Web3(Web3.HTTPProvider(rpc_url))
block = w3.eth.get_block(block_number, full_transactions=False)
node_hash = block.hash.hex()

url = f"https://api.etherscan.io/api?module=proxy&action=eth_getBlockByNumber&tag={hex(block_number)}&boolean=true&apikey={os.getenv('ETHERSCAN_API_KEY')}"
response = requests.get(url)
etherscan_hash = response.json()["result"]["hash"]

report = {
    "block_number": block_number,
    "node_hash": node_hash,
    "etherscan_hash": etherscan_hash,
    "status": "match" if node_hash == etherscan_hash else "mismatch"
}
filename = f"reports/hash_diff_{current_timestamp()}.json"
write_json_report(report, filename)

if node_hash == etherscan_hash:
    print("✅ Hash match")
else:
    print("❌ Hash mismatch")
