const axios = require('axios');
const FormData = require('form-data');
const fs = require('fs');
require('dotenv').config();  // Load API keys from .env

const pinataApiKey = process.env.PINATA_API_KEY;
const pinataSecretApiKey = process.env.PINATA_SECRET_API_KEY;

async function uploadToPinata(filePath) {
    const url = `https://api.pinata.cloud/pinning/pinFileToIPFS`;

    // Read the file from the provided path
    const data = new FormData();
    data.append('file', fs.createReadStream(filePath));

    const headers = {
        'Content-Type': `multipart/form-data; boundary=${data._boundary}`,
        'pinata_api_key': pinataApiKey,
        'pinata_secret_api_key': pinataSecretApiKey,
    };

    try {
        const response = await axios.post(url, data, { headers });
        console.log('File uploaded to Pinata successfully.');
        console.log('CID:', response.data.IpfsHash); 
        return response.data.IpfsHash;
    } catch (error) {
        console.error('Error uploading file to Pinata:', error);
    }
}

// Example usage
const filePath = './test.txt';
uploadToPinata(filePath);