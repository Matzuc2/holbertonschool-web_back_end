export default function appendToEachArrayValue(array, appendString) {
  let result = [];
  for (let idx of array) {
    result.push(appendString + idx);
  }
  return result;
}
