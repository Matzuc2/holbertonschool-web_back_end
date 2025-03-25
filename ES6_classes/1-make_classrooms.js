import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const array1 = [];
  const a = new ClassRoom(19);
  const b = new ClassRoom(20);
  const c = new ClassRoom(34);
  return array1.concat(a, b, c);
}
