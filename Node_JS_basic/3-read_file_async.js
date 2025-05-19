const fs = require('fs');
const csv = require('csv-parser');
const getStream = require('get-stream');

async function countStudents(path) {
readCSVData = async (path) => {
  const parseStream = csv({delimiter: ','});
  const data = await getStream.array(fs.createReadStream(path).pipe(parseStream))
  return data
};
    data = await readCSVData(path)
    //continue tomorrow..
}
module.exports = countStudents;