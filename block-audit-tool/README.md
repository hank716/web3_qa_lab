# block-audit-tool

Verify whether the blockchain node data is consistent with the block browser, and support automatic generation of JSON reports.

## Installation and startup

```bash
conda env create -f environment.yml
conda activate block-audit-env
```

## Execution function

- Fetch block data:
```bash
python scripts/fetch_block.py
```

- Compare nodes with Etherscan:
```bash
python scripts/compare_data.py
```

- Execute automatic scheduled monitoring (every 10 minutes):
```bash
python monitor/monitor_runner.py
```

- Execute pytest and output report:
```bash
python -m pytest tests/
```