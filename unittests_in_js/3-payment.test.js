
const assert = require('assert');
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', function() {
  it('should call Utils.calculateNumber with SUM, 100, 20', function() {
    const spy = sinon.spy(Utils, 'calculateNumber');

    sendPaymentRequestToApi(100, 20);
    assert(spy.calledWith('SUM', 100, 20));
    
    spy.restore();
  });
});