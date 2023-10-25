export default class Airport {
  constructor(name, code) {
    if (typeof name !== 'string') throw TypeError('name must be a string');
    if (typeof code !== 'string') throw TypeError('code must be a string');
    this._name = name;
    this._code = code;
  }

  get name() { return this._name; }

  set name(value) { this._code = value; }

  get code() { return this._code; }

  set code(value) { this._code = value; }

  toString() {
    return `[object ${this._code}]`;
  }
}
