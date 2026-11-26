load in json data and convert to my object: need the json keys

def load_students(filename):
    with open(filename, "r") as file:
        student_data = json.load(file)

    students = []

    for student_dict in student_data:
        students.append(Student(**student_dict))

    return students

#another sample using Student class
students = []

for student_dict in student_list:
    student = Student(
        first_name=student_dict["first_name"],
        last_name=student_dict["last_name"],
        gpa=student_dict["gpa"]
    )
    students.append(student)