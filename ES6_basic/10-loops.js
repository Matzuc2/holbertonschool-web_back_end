export default function appendToEachArrayValue(array, appendString) {
    let result = [];
    for (let idx of array) { 
      result.push(appendString + array[idx])
    }
    return result;
  }