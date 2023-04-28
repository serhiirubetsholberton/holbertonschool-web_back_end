export default class Currency {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  get code() {
    return this._code;
  }

  set code(value) {
    this._code = value;
  }

  get name() {
    return this._name;
  }

  set name(value) {
    this._name = value;
  }

  get [Symbol.toStringTag]() {
    return this._code;
  }
}
