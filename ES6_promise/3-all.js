import { uploadPhoto, createUser } from './utils.js';

export default function handleProfileSignup() {
  const prom1 = uploadPhoto();
  const prom2 = createUser();

  Promise.all([prom1, prom2]).then((values) => {
    console.log(values[0].body, values[1].firstName, values[1].lastName);
  })
    .catch(() => {
      console.error('Signup system offline');
    });
}
