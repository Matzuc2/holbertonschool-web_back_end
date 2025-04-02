export default function handleResponseFromAPI(promise){
        promise.then(() =>{
            return {'status': 200, 'body': "success"}
        })
        promise.catch(() =>{
            throw new Error
        })
        promise.finally(() =>{
            console.log("Got a response from the API")
        })
}