export default function getStudentIdsSum(array){
    let initial = 0;
    const map1 = array.map((x) => x["id"]);
    const SumArray = map1.reduce((acc, plus) => acc + plus, initial);
    return SumArray
}