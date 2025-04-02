export default function updateStudentGradeByCity(array, city, newGrades) {
  const filterList = array.filter((x) => x.location === city);
  const mapList = filterList.map((x) => Object.assign(x, { grade: 'N/A' }));
  mapList.forEach((element) => {
    newGrades.forEach((i) => {
      if (i.studentId === element.id) {
        // eslint-disable-next-line no-param-reassign
        element.grade = i.grade;
      }
    });
  });
  return mapList;
}
