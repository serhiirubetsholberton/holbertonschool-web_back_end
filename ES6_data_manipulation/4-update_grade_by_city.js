export default function updateStudentGradeByCity(students, city, newGrades) {
  const gradesById = newGrades.reduce((res, grade) => {
    res[grade.studentId] = grade.grade;
    return res;
  }, {});

  console.log(gradesById);

  return students
    .filter(({ location }) => location === city)
    .map((student) => ({
      ...student,
      grade: gradesById[student.id] || 'N/A',
    }));
}
