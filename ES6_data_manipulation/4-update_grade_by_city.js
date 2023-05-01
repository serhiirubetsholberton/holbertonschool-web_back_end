export default function updateStudentGradeByCity(students, city, newGrades) {
  // const studentsById = students.reduce((res, student) => {
  //   res[student.id] = student;
  //   return res;
  // }, {});

  const gradesById = newGrades.reduce((res, grade) => {
    res[grade.studentId] = grade.grade;
    return res;
  }, {});

  console.log(gradesById)

  return students
    .filter(({ location }) => location === city)
    .map((student) => {
      return {
        ...student,
        grade: gradesById[student.id] ?? 'N/A'
      }
    })
}
