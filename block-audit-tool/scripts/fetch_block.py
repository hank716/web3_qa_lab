from dotenv import load_dotenv
import os
import yaml
from web3 import Web3

load_dotenv()
rpc_url = os.getenv("INFURA_RPC")

with open("config/settings.yaml", "r") as f:
    config = yaml.safe_load(f)

w3 = Web3(Web3.HTTPProvider(rpc_url))
block = w3.eth.get_block(config["block_range"]["start_block"], full_transactions=False)
print(f"Block Number: {block.number}")
print(f"Hash: {block.hash.hex()}")
print(f"Tx count: {len(block.transactions)}")
