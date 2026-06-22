const { expect } = require("chai");
const calculateNumber = require("./1-calcul.js");

describe("type=SUM", function () {
    it("round two number and add them up", function () {
        expect(calculateNumber("SUM", 2.7, 5)).to.equal(8);
    });

    it("should round the two arguments", function () {
        expect(calculateNumber("SUM", 2.4, 1.8)).to.equal(4);
    });

    it("should round the second number", function () {
        expect(calculateNumber("SUM", 2, 1.8)).to.equal(4);
    });

    it("should round the second number again bc", function () {
        expect(calculateNumber("SUM", 2, 1.1)).to.equal(3);
    });

    it("should round the second number again", function () {
        expect(calculateNumber("SUM", 2, 1.5)).to.equal(4);
    });
});

describe("type=SUBTRACT", function () {
    it("should subtract two rounded numbers", function () {
        expect(calculateNumber("SUBTRACT", 5.7, 2.4)).to.equal(4);
    });

    it("should subtract with second number rounded", function () {
        expect(calculateNumber("SUBTRACT", 5, 2.8)).to.equal(2);
    });
});

describe("type=DIVIDE", function () {
    it("should divide two rounded numbers", function () {
        expect(calculateNumber("DIVIDE", 5.7, 2.4)).to.equal(3);
    });

    it("should return Error when dividing by zero", function () {
        expect(calculateNumber("DIVIDE", 5, 0)).to.equal("Error");
    });
});