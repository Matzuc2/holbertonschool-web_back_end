export default function appendToEachArrayValue(array, appendString) {
  const result = [];
  for (let idx of array) {
    result.push(appendString + idx);
  }
  return result;
}
