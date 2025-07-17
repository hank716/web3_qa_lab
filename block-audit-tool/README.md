# block-audit-tool

驗證區塊鏈節點資料與區塊瀏覽器是否一致，並支援自動產生 JSON 報告。

## 安裝與啟動

```bash
conda env create -f environment.yml
conda activate block-audit-env
```

## 執行功能

- 抓取區塊資料：
```bash
python scripts/fetch_block.py
```

- 比對節點與 Etherscan：
```bash
python scripts/compare_data.py
```

- 執行自動排程監控（每 10 分鐘）：
```bash
python monitor/monitor_runner.py
```

- 執行 pytest 並輸出報告：
```bash
python -m pytest tests/
```
