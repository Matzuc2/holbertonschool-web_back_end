export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
  }

  get name() {
    return this._name;
  }

  set name(NewName) {
    if (typeof NewName !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = NewName;
  }

  get length() {
    return this._length;
  }

  set length(NewLength) {
    if (typeof NewLength !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this._length = NewLength;
  }

  get students() {
    return this._students;
  }

  set students(NewStudents) {
    for (const student in NewStudents) {
      if (typeof (student) !== 'string') {
        throw new TypeError('Each elements of array must be a string');
      }
    }
    if (!Array.isArray(NewStudents) && typeof (NewStudents) !== 'object') {
      TypeError('Students must be an array');
    }
    this._students = NewStudents;
  }
}
