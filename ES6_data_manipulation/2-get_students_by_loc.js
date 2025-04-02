export default function getStudentsByLocation(array, city) {
  if (typeof city === 'string'){
  const filterList = array.filter((x) => x.location === city);
  return filterList;
  }
}
