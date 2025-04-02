import { uploadPhoto, createUser } from "./utils.js";

export default function handleProfileSignup(){
    let prom1 = uploadPhoto()
    let prom2 = createUser()

    Promise.all([prom1, prom2]).then((values) => {
        console.log(values[0].body, values[1].firstName, values[1].lastName)
      })
      .catch(() =>{
        console.log("Signup system offline")
      });
}
