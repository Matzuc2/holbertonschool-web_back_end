export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;
  if (trueOrFalse) {
    /* eslint-disable */
    const task = true;
    const task2 = false;
  }
  console.log(task2)
  return [task, task2];
}
