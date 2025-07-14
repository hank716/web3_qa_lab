# contract-tester

一個基於 Foundry 的智能合約測試專案，提供主流測試結構與報告流程，適合區塊鏈測試工程師學習與求職使用。

## 結構說明

- `contracts/`：Solidity 智能合約
- `test/`：單元測試檔案（`.t.sol`）
- `script/`：部署與模擬腳本
- `reports/`：每次執行產生的測試與 gas 報告（以 timestamp 區分）
- `run_tests.sh`：自動化測試與報告輸出腳本

## 使用方式

```bash
forge install
forge build
./run_tests.sh
```

## 初始合約：Voting

一個簡單的投票合約，具備事件發送與投票限制，可用來測試狀態變化、錯誤處理與事件驗證。
