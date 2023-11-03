export default function getListStudentIds(studentsArray) {
  if (!Array.isArray(studentsArray)) {
    return [];
  }
  // Use the map function to extract the 'id' values
  const studentsIds = studentsArray.map(student => student.id);
  return studentsIds;
}
