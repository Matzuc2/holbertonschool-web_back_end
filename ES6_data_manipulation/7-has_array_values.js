export default function hasValuesFromArray(set, array1){
    let bool1 = false;
    array1.forEach(element => {
        if (set.has(element)){
            bool1 = true;
        }
        else{
            bool1 = false;
            return false
        }
    });
    return bool1;
}
