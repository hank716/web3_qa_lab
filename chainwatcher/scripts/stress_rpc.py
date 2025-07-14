import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import asyncio
import time
from utils.rpc_client import call_rpc

TOTAL_REQUESTS = 100   # Adjustable: Number of requests for stress testing
CONCURRENCY = 10       # Number of concurrent requests

results = []

async def single_request(i):
    start = time.time()
    try:
        res = await call_rpc("eth_blockNumber")
        block_number = int(res["result"], 16)
        assert block_number > 0
        success = True
    except Exception as e:
        print(f"[{i}] Error: {e}")
        success = False
    end = time.time()
    results.append({
        "id": i,
        "success": success,
        "elapsed": round(end - start, 4)
    })

async def run_stress_test():
    sem = asyncio.Semaphore(CONCURRENCY)

    async def sem_wrapper(i):
        async with sem:
            await single_request(i)

    tasks = [sem_wrapper(i) for i in range(TOTAL_REQUESTS)]
    await asyncio.gather(*tasks)

    # Statistics
    success_count = sum(r["success"] for r in results)
    avg_time = sum(r["elapsed"] for r in results) / len(results)
    max_time = max(r["elapsed"] for r in results)
    min_time = min(r["elapsed"] for r in results)

    print(f"\n✅ Total Requests Sent: {TOTAL_REQUESTS}")
    print(f"🟢 Successful Requests: {success_count}")
    print(f"❌ Failed Requests: {TOTAL_REQUESTS - success_count}")
    print(f"⏱ Average Latency: {avg_time:.4f}s")
    print(f"🚀 Fastest Response: {min_time:.4f}s")
    print(f"🐢 Slowest Response: {max_time:.4f}s")

if __name__ == "__main__":
    asyncio.run(run_stress_test())
