export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const gradeObj = newGrades.filter((grade) => grade.studentId === student.id);

      if (gradeObj.length > 0) {
        return { ...student, grade: gradeObj[0].grade };
      } else {
        return { ...student, grade: 'N/A' };
      }
    });
}
