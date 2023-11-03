export default function getStudentIdsSum(studentsArray) {
  const studentsSumIds = studentsArray.reduce((accum, student) => accum + student.id, 0);
  return studentsSumIds;
}
