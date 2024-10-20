// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CIDStorage {
    // Mapping to store CID against an address
    mapping(address => string) private cids;

    // Event to emit when a CID is stored
    event CIDStored(address indexed user, string cid);

    // Function to store the CID
    function storeCID(string memory _cid) public {
        cids[msg.sender] = _cid;
        emit CIDStored(msg.sender, _cid);
    }

    // Function to retrieve the CID
    function retrieveCID() public view returns (string memory) {
        return cids[msg.sender];
    }
}
