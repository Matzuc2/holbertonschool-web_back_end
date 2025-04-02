export default function signUpUser(firstName, lastName) {
    let prom1 = new Promise((resolve, reject) => {
        resolve({'firstName': firstName, 'lastName': lastName})
    });
    return prom1
}