export default class HolbertonCourse {
  constructor(name, length, students) {

    if (typeof name !== 'string') {
      throw new Error('Name must be a string');
    }

    if (typeof name !== 'number') {
      throw new Error('Length must be a number');
    }

    if (!Array.isArray(students)) {
      throw new Error('Students must be an array');
    }

    this._length = length;
    this._name = name;
    this._sudents = students;
  }

  get name() {
    return this._name;
  }

  set name(value) {
    this._name = value;
  }

  get length() {
    return this._length;
  }

  set length(value) {
    this._length = value;
  }

  get sudents() {
    return this._sudents;
  }

  set sudents(value) {
    this._sudents = value;
  }
}
