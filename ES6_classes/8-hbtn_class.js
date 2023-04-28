export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  get size() {
    return this._location;
  }

  set size(value) {
    this._location = value;
  }

  get location() {
    return this._size;
  }

  set location(value) {
    this._size = value;
  }

  valueOf() {
    return this.size;
  }

  toString() {
    return this.location;
  }
}
