const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');

    const rows = data.split('\n').slice(1).filter((row) => row.trim() !== '');
    let namelistCS = [];
    let namelistSWE = [];
    let CountCS = 0;
    let CountSWE = 0;
    const CountAll = rows.length;

    rows.forEach((row) => {
      const columns = row.split(',');
      if (columns[3] === 'CS') {
        namelistCS.push(String(columns[0]));
        CountCS += 1;
      } else if (columns[3] === 'SWE') {
        namelistSWE.push(String(columns[0]));
        CountSWE += 1;
      }
    });

    namelistCS = namelistCS.toString().replace(/,/g, ', ');
    namelistSWE = namelistSWE.toString().replace(/,/g, ', ');

    console.log(`Number of students: ${CountAll}`);
    console.log(`Number of students in CS: ${CountCS}. List: ${namelistCS}`);
    console.log(`Number of students in SWE: ${CountSWE}. List: ${namelistSWE}`);

    // Create a string in the required format
    const output = `Number of students: ${CountAll}
Number of students in CS: ${CountCS}. List: ${namelistCS}
Number of students in SWE: ${CountSWE}. List: ${namelistSWE}`;

    return output;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
