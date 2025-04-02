export default function getStudentsByLocation(array, city) {
  const filterList = array.filter((x) => x.location === city);
  return filterList;
}
