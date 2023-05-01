export default function getStudentIdsSum(students) {
  return students.reduce((res, { id }) => res + id, 0);
}
