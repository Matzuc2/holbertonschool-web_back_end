export default function createInt8TypedArray(length, position, value){
    let int8 = new ArrayBuffer(length)
    const viewOfArray = new Int8Array(int8) 
    if (position > (length - 1)){
        throw new Error("Position outside range");
    }
    viewOfArray[position] = value
    let dt = new DataView(int8)
    return dt
}