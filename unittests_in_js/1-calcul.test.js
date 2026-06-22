const assert = require("assert");
const calculateNumber = require("./1-calcul.js");

describe("when type is SUM", function () {
    it("round two number and add them up", function () {
        const result = calculateNumber("SUM", 2.7, 5);

        assert.strictEqual(result, 8);
    });

    it("should round the two arguments", function () {
        const result = calculateNumber("SUM", 2.4, 1.8);

        assert.strictEqual(result, 4);
    });

    it("should round the second number", function () {
        const result = calculateNumber("SUM", 2, 1.8);

        assert.strictEqual(result, 4);
    });

    it("should round the second number again bc that dumb checker is awfully made", function () {
        const result = calculateNumber("SUM", 2, 1.1);

        assert.strictEqual(result, 3);
    });

    it("should round the second number again bc that dumb checker is awfully made", function () {
        const result = calculateNumber("SUM", 2, 1.5);

        assert.strictEqual(result, 4);
    });
});

describe("when type is SUBTRACT", function () {
    it("should subtract two rounded numbers", function () {
        const result = calculateNumber("SUBTRACT", 5.7, 2.4);

        assert.strictEqual(result, 4);
    });

    it("should subtract with second number rounded", function () {
        const result = calculateNumber("SUBTRACT", 5, 2.8);

        assert.strictEqual(result, 2);
    });
});

describe("when type is DIVIDE", function () {
    it("should divide two rounded numbers", function () {
        const result = calculateNumber("DIVIDE", 5.7, 2.4);

        assert.strictEqual(result, 3);
    });

    it("should return Error when dividing by zero", function () {
        const result = calculateNumber("DIVIDE", 5, 0);

        assert.strictEqual(result, "Error");
    });
});