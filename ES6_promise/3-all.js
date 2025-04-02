import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const prom1 = uploadPhoto();
  const prom2 = createUser();

  Promise.all([prom1, prom2]).then(([photo, user]) => {
    console.log(photo.body, user.firstName, user.lastName);
  })
    .catch(() => {
      console.log('Signup system offline');
    });
}
