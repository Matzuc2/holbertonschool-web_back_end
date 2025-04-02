export default function cleanSet(set1, string) {
  if (!(set1 instanceof Set) || typeof string !== 'string') {
    return '';
  }
  const len = string.length;
  if (len === 0) {
    return '';
  }
  let str = '';
  set1.forEach((element) => {
    if (String(element).startsWith(string)) {
      str += `${String(element).slice(len)}-`;
    }
  });
  str = str.slice(0, -1);
  return str;
}
