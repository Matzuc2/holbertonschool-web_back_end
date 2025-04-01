export default function updateStudentGradeByCity(array, city, newGrades){
    let filterList = array.filter((x) => x["location"] == city)
    let mapList = filterList.map((x) => Object.assign(x, {grade: "N/A"}))
    mapList.forEach(element => {
        newGrades.forEach(i => {
            if (i["studentId"] == element["id"]){
                element["grade"] = i["grade"];
            }
        })
    });
    return mapList
}