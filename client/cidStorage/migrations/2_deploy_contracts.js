const CIDStorage = artifacts.require("CIDStorage");

module.exports = function (deployer) {
  deployer.deploy(CIDStorage);
};
