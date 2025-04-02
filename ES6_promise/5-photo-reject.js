export default function uploadPhoto(filename) {
    let prom1 = new Promise((resolve, reject) =>{
        reject(new Error(`${filename} cannot be processed`))
    })
    return prom1
}