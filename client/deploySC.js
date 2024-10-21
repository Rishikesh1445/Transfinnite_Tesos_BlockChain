const { exec } = require('child_process');
const path = require('path');

// Function to run a command in a specific folder
function runCommandInFolder(command, folderPath) {
    exec(command, { cwd: folderPath }, (error, stdout, stderr) => {
        if (error) {
            console.error(`Error executing command: ${error.message}`);
            return;
        }
        if (stderr) {
            console.error(`Standard error: ${stderr}`);
            return;
        }
        console.log(`Output: ${stdout}`);
    });
}

const folderPath = path.join(__dirname, 'rishi'); // Replace 'your-folder' with your folder name
const command = 'truffle migration --network development'; // Replace with the command you want to run, e.g., 'ls' or 'dir'

// Run the command
runCommandInFolder(command, folderPath);

