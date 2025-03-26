import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this.amount = amount;
    this.currency = currency;
  }

  get amount() {
    return this._amount;
  }

  set amount(NewAmount) {
    if (typeof NewAmount !== 'number') {
      throw new TypeError('amount must be a number');
    }
    this._amount = NewAmount;
  }

  get currency() {
    return this._currency;
  }

  set currency(NewCurrency) {
    if (NewCurrency instanceof Currency) {
      this._currency = NewCurrency;
    } else {
      throw new TypeError('ta mere la pute');
    }
  }

  displayFullPrice() {
    return `${this.amount} ${this.currency.name} (${this.currency.code})`;
  }

  static convertPrice(amount, conversionRate) {
    return (amount * conversionRate);
  }
}
