export default class Currency {
  constructor(code, name) {
    this.code = code;
    this.name = name;
  }

  get code() {
    return this._code;
  }

  set code(NewCode) {
    if (typeof NewCode !== 'string') {
      throw new TypeError('Code must be a string');
    }
    this._code = NewCode;
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

  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}
