
const assert = require('assert');
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');
const calculateNumber = require('./2-calcul_chai');
const { beforeEach, afterEach } = require('mocha');

let spy; 

describe('sendPaymentRequestToApi', function() {
    beforeEach(() =>{
        spy = sinon.spy(console, 'log');
    })
    it('should call sendRequestToAPI with 100, 20', function() {
        sendPaymentRequestToApi(100, 20);
        assert(spy.calledWith('The total is: 120'));
        assert(spy.calledOnce)
    });
    it('should call sendRequestToAPI with 10, 20', function() {
        sendPaymentRequestToApi(10, 10);
        assert(spy.calledWith('The total is: 20'));
        assert(spy.calledOnce)
    });
    afterEach(() => {
        spy.restore();
    })
});