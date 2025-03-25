export default function appendToEachArrayValue(array, appendString) {
  const result = [];
  for (const idx of array) {
    result.push(appendString + array[idx]);
  }
  return result;
}
