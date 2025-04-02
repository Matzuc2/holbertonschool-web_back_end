export default function signUpUser(firstName, lastName) {
  const prom1 = new Promise((resolve) => {
    resolve({ firstName, lastName });
  });
  return prom1;
}
