const assert = require('assert');
const sinon = require('sinon');
const getPaymentTokenFromAPI = require('./6-payment_token')
const { beforeEach, afterEach } = require('mocha');
const { AssertionError } = require('chai');


describe('getPaymentTokenFromAPI', function(){
    it("should return a resolved promise", function(){
        return getPaymentTokenFromAPI(true).then((result) => {
        assert.deepStrictEqual(result, { data: 'Successful response from the API' });
        });
    })
})