const assert = require("assert");
const calculateNumber = require("./1-calcul.js");

describe("calculateNumber", function () {
    it("round two number and add them up", function () {
        const result = calculateNumber(2.7, 5, "SUM");

        assert.strictEqual(result, 8);
    });

    it("should round the two arguments", function () {
        const a = 2.4;
        const b = 1.8;

        const result = calculateNumber(a, b, "SUM");

        assert.strictEqual(result, 4);
    });
    it("should round the second number", function () {
        const a = 2;
        const b = 1.8;
        const result = calculateNumber(a, b, "SUM");

        assert.strictEqual(result, 4);
    });
    it("should round the second number again bc that dumb checker is awfully made", function(){
        const a = 2;
        const b = 1.1;

        const result = calculateNumber(a, b, "SUM")

        assert.strictEqual(result, 3)
    });
    it("should round the second number again bc that dumb checker is awfully made", function(){
        const a = 2;
        const b = 1.5;

        const result = calculateNumber(a, b, "SUM")

        assert.strictEqual(result, 4)
    });
    it("should subtract two rounded numbers", function () {
        const result = calculateNumber(5.7, 2.4, "SUBTRACT");

        assert.strictEqual(result, 4);
    });
    it("should subtract with second number rounded", function () {
        const result = calculateNumber(5, 2.8, "SUBTRACT");

        assert.strictEqual(result, 2);
    });

    it("should divide two rounded numbers", function () {
        const result = calculateNumber(5.7, 2.4, "DIVIDE");

        assert.strictEqual(result, 3);
    });

    it("should return Error when dividing by zero", function () {
        const result = calculateNumber(5, 0, "DIVIDE");

        assert.strictEqual(result, "Error");
    });
});