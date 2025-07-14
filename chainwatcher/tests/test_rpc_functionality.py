# tests/test_rpc_functionality.py
import pytest
from utils.rpc_client import call_rpc

@pytest.mark.asyncio
async def test_eth_block_number():
    res = await call_rpc("eth_blockNumber")
    assert "result" in res
    block_number = int(res["result"], 16)
    print(f"Current block height：{block_number}")
    assert block_number > 0
