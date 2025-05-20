const readDatabase = require('../utils.js');
const path = require('path');

class StudentsController {
  static getAllStudents(request, response) {
    const dbPath = process.argv[2];
    const data = readDatabase(dbPath);
    data.then((output) => {
      // Start building the response string
      let responseText = 'This is the list of our students\n';
      
      // Format CS students data
      const csLength = output['CS'].length;
      const csList = output['CS'].join(', ');
      responseText += `Number of students in CS: ${csLength}. List: ${csList}\n`;
      
      // Format SWE students data
      const sweLength = output['SWE'].length;
      const sweList = output['SWE'].join(', ');
      responseText += `Number of students in SWE: ${sweLength}. List: ${sweList}`;
      
      // Send the formatted response
      response
        .status(200)
        .send(responseText);
    })
    .catch((error) => {
      response
        .status(500)
        .send('Cannot load the database');
    });
  }

  static getAllStudentsByMajor(request, response) {
    const major = request.params.major;
    if (major !== "CS" && major !== "SWE") {
      return response
        .status(500)
        .send('Major parameter must be CS or SWE');
    }
    const dbPath = path.resolve(__dirname, '..', process.argv[2]);
    const data = readDatabase(dbPath);
    data
      .then((output) => {
        let ListMajor = output[major];
        response
          .status(200)
          .send(`List: ${ListMajor}`);
      })
      .catch(() => {
        response
          .status(500)
          .send('Cannot load the database');
      });
  }
}

module.exports = StudentsController;