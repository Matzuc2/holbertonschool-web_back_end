export default function appendToEachArrayValue(array, appendString) {
  const result = [];
  for (let idx of array) {
    result.push(appendString + array[idx]);
  }
  return result;
}
