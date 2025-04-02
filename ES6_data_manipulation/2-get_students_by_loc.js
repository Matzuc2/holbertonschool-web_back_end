export default function getStudentsByLocation(array, city) {
  if (Array.isArray(array) && typeof city === 'string') {
    const filterList = array.filter((x) => x.location === city);
    return filterList;
  }
  return filterList;
}
