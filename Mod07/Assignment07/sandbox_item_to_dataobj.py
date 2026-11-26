#json load result is a list of dict
student_json: list = []
student_json = [{"FirstName": "Vic", "LastName": "Vu", "CourseName": "Python 100"}, {"FirstName": "Sue", "LastName": "Jones", "CourseName": "Python 100"}]

# Working with Dictionaries #
# In module 5, we learned how to create a dictionary of student data.
student_dic = {"FirstName": student_first_name,"LastName": student_last_name,"GPA": gpa}
print(student_dic, type(student_dic))

# In this module7 we learned how to store the same data in a custom Student object.
student_obj = Student(first_name=student_first_name,last_name=student_last_name, gpa=gpa)