export default function getStudentIdsSum(array) {
  const initial = 0;
  const map1 = array.map((x) => x.id);
  const SumArray = map1.reduce((x, y) => x + y, initial);
  return SumArray;
}
