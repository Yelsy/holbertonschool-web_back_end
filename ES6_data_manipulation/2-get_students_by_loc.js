export default function getStudentsByLocation(student, city) {
  const studentByLocation = student.filter(
    (student) => student.location === city,
  );
  return studentByLocation;
}
