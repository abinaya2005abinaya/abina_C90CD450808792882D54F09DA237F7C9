class student:
    
  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa
    
  def sort_students(student_list):
   #sort the list of students in descending order of CGPA
   sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=true)
   #syntax -lambda arg:exp
   return sorted_students

#example usage:
students = [student("hari", "A123", 7.8),
            student("srikanth", "A124", 8.9),
            student("saumya", "A125", 9.1),
            student("Mahidhar", "A126", 9.9),]

sorted_students = sort_student(students)

#print the sorted list of students
for students in sorted_students:
    print ("Name: {}, Roll number: {}, CGPA:{}".format(students.name,student.roll_number,student.cgpa))



