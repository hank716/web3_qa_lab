# contract-tester

A smart contract testing project based on **Foundry**, providing a mainstream structure and report generation workflow.

## Project Structure

- `contracts/`: Solidity smart contracts  
- `test/`: Unit test files (ending in `.t.sol`)  
- `script/`: Deployment and interaction scripts  
- `reports/`: Automatically generated test and gas reports (organized by timestamp)  
- `run_tests.sh`: Shell script to automate testing and output reports  

## Usage

```bash
forge install
forge build
./run_tests.sh
```

## Initial Contract: Voting

A simple voting contract that includes:

- vote tracking (`votes`)
- voter restriction (`hasVoted`)
- event emission (`emit Voted(...)`)

Used to test:
- state changes  
- access control / error handling  
- event verification  
