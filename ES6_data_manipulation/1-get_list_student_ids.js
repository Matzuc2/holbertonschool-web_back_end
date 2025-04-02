export default function getListStudentIds(array) {
  if (array instanceof Array) {
    const map1 = array.map((x) => x.id);
    return map1;
  }

  return [];
}
