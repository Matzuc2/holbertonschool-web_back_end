export default function hasValuesFromArray(set, array1) {
  return array1.every((element) => set.has(element));
}
