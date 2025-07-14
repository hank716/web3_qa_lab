// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

import "forge-std/Test.sol";
import "../contracts/Voting.sol";

contract VotingTest is Test {
    Voting public voting;
    address user1 = address(0x123);
    address user2 = address(0x456);

    event Voted(uint indexed option, address indexed voter);

    function setUp() public {
        voting = new Voting();
    }

    function testVoteIncreasesCount() public {
        voting.vote(1);
        assertEq(voting.votes(1), 1);
    }

    function testMultipleVotesDifferentUsers() public {
        vm.prank(user1);
        voting.vote(1);

        vm.prank(user2);
        voting.vote(1);

        assertEq(voting.votes(1), 2);
    }

    function testRejectDoubleVoteSameUser() public {
        voting.vote(1);
        vm.expectRevert("You already voted!");
        voting.vote(2);
    }

    function testVoteEmitsEvent() public {
        vm.expectEmit(true, true, false, true);
        emit Voted(1, address(this));
        voting.vote(1);
    }
}
