const fs = require('fs').promises;

async function readDatabase(path) {
    try {
    const data = await fs.readFile(path, 'utf8');

    const rows = data.split('\n').slice(1).filter((row) => row.trim() !== '');
    let namelistCS = [];
    let namelistSWE = [];

    rows.forEach((row) => {
      const columns = row.split(',');
      if (columns[3] === 'CS') {
        namelistCS.push(String(columns[0]));
      } else if (columns[3] === 'SWE') {
        namelistSWE.push(String(columns[0]));
      }
    });

    // Create a string in the required format
    const output = {CS: namelistCS, SWE: namelistSWE}

    return output;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = readDatabase;