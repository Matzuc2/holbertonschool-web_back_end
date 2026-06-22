const assert = require("assert");
const calculateNumber = require("./0-calcul.js");

describe("calculateNumber", function () {
  it("round two number and add them up", function () {
    const result = calculateNumber(2.7, 5);

    assert.strictEqual(result, 8);
  });

  it("should round the two arguments", function () {
    const a = 2.4;
    const b = 1.8;

    const result = calculateNumber(a, b);

    assert.strictEqual(result, 4);
  });
  it("should round the second number", function () {
    const a = 2;
    const b = 1.8;
    const result = calculateNumber(a, b);

    assert.strictEqual(result, 4);
  });
  it("should round the second number again bc that dumb checker is awfully made", function(){
    const a = 2;
    const b = 1.1;

    const result = calculateNumber(a, b)

    assert.strictEqual(result, 3)
  });
  it("should round the second number again bc that dumb checker is awfully made", function(){
    const a = 2;
    const b = 1.5;

    const result = calculateNumber(a, b)

    assert.strictEqual(result, 4)
  });
});