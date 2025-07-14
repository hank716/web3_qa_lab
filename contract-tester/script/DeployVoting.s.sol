// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

import "forge-std/Script.sol";
import "../contracts/Voting.sol";

contract DeployVoting is Script {
    function run() external {
        vm.startBroadcast();
        new Voting();
        vm.stopBroadcast();
    }
}
