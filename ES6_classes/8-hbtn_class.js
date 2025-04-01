class MathUtils {
  static add(a, b) {
      return a + b;
  }

  static multiply(a, b) {
      return a * b;
  }
}

// Calling static methods on the class
// console.log(MathUtils.add(5, 3));
// console.log(MathUtils.multiply(4, 6));
const math = new MathUtils;
console.log(math.add(1, 1));