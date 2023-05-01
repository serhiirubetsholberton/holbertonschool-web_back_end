export default function updateStudentGradeByCity(students, city, newGrades) {
  const studentsById = students.reduce((res, student) => {
    res[student.id] = student;
    return res;
  }, {});

  const gradesById = newGrades.reduce((res, grade) => {
    res[grade.id] = grade.grade;
    return res;
  }, {});

  return students
    .filter(({ location }) => location === city)
    .map((student) => {
      return {
        ...student,
        grade: gradesById[student.id].grade
      }
    })
}
