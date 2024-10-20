// const pinataSDK = require('@pinata/sdk');
// const pinata = pinataSDK(process.env.PINATA_API_KEY, process.env.PINATA_SECRET_API_KEY);

async function downloadfromPinata(cid){
    // IPFS gateway URL to fetch data
    const url = `https://gateway.pinata.cloud/ipfs/${cid}`;

    fetch(url)
        .then(response => response.text())
        .then(data => console.log(data))
        .catch(err => console.error(err));
}

downloadfromPinata('QmWJJvQTqCBLucActTq7HHv2FzmsqbXLBhALaQSP7mHYcE')