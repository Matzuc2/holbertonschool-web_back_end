export default function getFullResponseFromAPI(success){
    let prom = new Promise((resolve, reject) =>{
        if (success === true){
            resolve({'status': 200, 'body': "Success"})
        }
        else{
            reject(new Error("The fake API is not working currently"))
        }
    })
    return prom
}