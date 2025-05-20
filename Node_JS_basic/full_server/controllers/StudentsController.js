const readDatabase = require('../utils');

class StudentsController {
  static getAllStudents(request, response) {
    const dbPath = process.argv[2];
    const data = readDatabase(dbPath);
    data.then((output) => {
      let responseText = 'This is the list of our students\n';
      const csLength = output.CS.length;
      const csList = output.CS.join(', ');
      responseText += `Number of students in CS: ${csLength}. List: ${csList}\n`;

      const sweLength = output.SWE.length;
      const sweList = output.SWE.join(', ');
      responseText += `Number of students in SWE: ${sweLength}. List: ${sweList}`;

      response
        .status(200)
        .send(responseText);
    })
      .catch(() => {
        response
          .status(500)
          .send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(request, response) {
    const { major } = request.params;
    if (major !== 'CS' && major !== 'SWE') {
      response
        .status(500)
        .send('Major parameter must be CS or SWE');
    } else {
      const dbPath = process.argv[2];
      const data = readDatabase(dbPath);
      data
        .then((output) => {
          const ListMajor = output[major].join(', ');
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
}

module.exports = StudentsController;
