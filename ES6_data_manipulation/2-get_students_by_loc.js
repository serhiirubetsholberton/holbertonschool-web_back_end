export default function getStudentsByLocation(students, studentLocation) {
  return students.filter(({ location }) => location === studentLocation);
}
