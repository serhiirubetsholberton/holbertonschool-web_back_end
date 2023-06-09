export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  get location() {
    return this._location;
  }

  set location(value) {
    this._location = value;
  }

  get size() {
    return this._size;
  }

  set size(value) {
    this._size = value;
  }

  valueOf() {
    return this.size;
  }

  toString() {
    return this.location;
  }
}
