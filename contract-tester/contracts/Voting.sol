// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Voting {
    mapping(uint => uint) public votes;
    mapping(address => bool) public hasVoted;

    event Voted(uint indexed option, address indexed voter);

    mapping(address => uint) public voteRecord; 

    function vote(uint option) public {
        require(!hasVoted[msg.sender], "You already voted!");
        voteRecord[msg.sender] = option;
        votes[option]++;
        hasVoted[msg.sender] = true;
        emit Voted(option, msg.sender);
    }
}
