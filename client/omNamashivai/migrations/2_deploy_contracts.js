const HelloEtherlink = artifacts.require("HelloEtherlink");

module.exports = function (deployer) {
  deployer.deploy(HelloEtherlink);
};