# ------------------------------------------------------------------------------------------------------ #
# Title: Demo05 - Converting Json and Student Objects
# Description: This demo shows how the same student data can be stored and converted between:
#   1. A plain string
#   2. A list
#   3. A dictionary
#   4. A custom object (class instance)
#
#   It also demonstrates:
#   - Saving and reading data from JSON files
#   - Converting object data for saving to files

# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# RRoot,1.2.2030,Moved the fields into the constructor
# RRoot,1.3.2030,Added properties and private attributes
# -------------------------------------------------------------------------------------------------------- #
import json

# In this module we learned how to store data in objects made from custom data classes
# instead of using Python pre-made lists and dictionaries data classes.
class Person:  # TODO Create a Person Class and add the first and last name properties from the Student class (Done)

    def __init__(self, first_name: str = "", last_name: str = ""):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self.__first_name.title()

    @first_name.setter
    def first_name(self, value: str):
        if value.isalpha() or value == "":
            self.__first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")

    @property
    def last_name(self):
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value: str):
        if value.isalpha() or value == "":
            self.__last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    # TODO Override the __str__() method (Done)
    def __str__(self):
        return f"{self.first_name},{self.last_name}"


class Student(Person):

    def __init__(self, first_name: str = "", last_name: str = "", gpa: float = 0.0):
        # TODO Replace calls to the first and last name properties with a call to the Person constructor (Done)
        # self.first_name = first_name
        # self.last_name = last_name
        super().__init__(first_name=first_name,last_name=last_name)

        # TODO add one or more attributes unique to students (Done)
        self.gpa = gpa

    # TODO add the getter (Done)
    @property
    def gpa(self):
        return self.__gpa

    # TODO add the setter (Done)
    @gpa.setter
    def gpa(self, value: float):
        try:
            self.__gpa = float(value)
        except ValueError:
            raise ValueError("GPA must be a numeric value.")

    # TODO Override the __str__() method (Done)
    def __str__(self):
        return f"{self.first_name},{self.last_name},{self.gpa}"


# Main body of the demo #
# In module 1 we learned how to store data in memory using variables.
student_first_name: str = 'Vic'
student_last_name: str = 'Vu'
gpa: float = 3.8

# Working with Strings #
# In module 2, we learned how to create a comma-separated string of student data.
student_str = f"{student_first_name},{student_last_name},{gpa}"
print(student_str, type(student_str)) # Storing data as a string in memory

# Working with Lists #
# In module 4, we learned how to create a list of student data.
student_lst = [student_first_name,student_last_name,gpa]
print(student_lst, type(student_lst))  # Same data, but a different way to store the data in memory

# And, learned how to convert the list back into a string in order to save that data to a file.
student_str = f"{student_lst[0]},{student_lst[1]},{student_lst[2]}"
print(student_str, type(student_str))
file = open("Test.csv", "w")
file.write(student_str)
file.close()

# Working with Dictionaries #
# In module 5, we learned how to create a dictionary of student data.
student_dic = {"FirstName": student_first_name,"LastName": student_last_name,"GPA": gpa}
print(student_dic, type(student_dic))

# And, how to convert the dictionary to a string in order to save that data to a file.
student_str = f'{student_dic["FirstName"]},{student_dic["LastName"]},{student_dic["GPA"]}'
print(student_str, type(student_str))
file = open("Test.csv", "w")
file.write(student_str)
file.close()


# In this module we learned how to store the same data in a custom Student object.
student_obj = Student(first_name=student_first_name,last_name=student_last_name, gpa=gpa)

# You can convert the dictionary to a string in order to save that data to a file like this.
student_str = f"{student_obj.first_name},{student_obj.last_name},{student_obj.gpa}"
print(student_str, type(student_str))
file = open("Test.csv", "w")
file.write(student_str)
file.close()

# But, you can also get a string using the __str__() method in an object
print(student_obj, type(student_obj))  # The print function automatically call the __str__() method
print(student_obj.__str__(), type(student_str))  # so this is the same output
file = open("Test.csv", "w")
file.write(student_obj.__str__())  # However, the file.write() method does not automatically call the __str__() function
file.close()


# Working with JSON #
# JSON is a specialize formated string with extra quotation marks so we can create that string like this
student_obj = Student(first_name=student_first_name,last_name=student_last_name, gpa=gpa)
student_json_str = (f'{{"FirstName": "{student_obj.first_name}", '
                    f'"LastName": "{student_obj.last_name}", '
                    f'"GPA": {student_obj.gpa}}}')  # Note: The double {{ and }} are escaping the curly-braces in the string

print(student_json_str, type(student_json_str))

# Or simply use the json module's dumps() method to create the string for us. (Note: dumps has an "s" as in string)
student_json = json.dumps({
    "FirstName": student_obj.first_name,
    "LastName": student_obj.last_name,
    "GPA": student_obj.gpa
})
print(student_json, type(student_json))


# However, we need to convert Student objects back into dictionaries to use the json module's dump() method.
student_dic = {"FirstName": student_obj.first_name, "LastName": student_obj.last_name, "GPA": student_obj.gpa}
print(student_dic, type(student_dic))  # Note there are no quotes around the data values
file = open("Test.json", "w")
json.dump(student_dic, file)  # Open the file and notice that json.dump added quotes around the data values
file.close()

# And when we read the file, the load method will convert it again into a list of dictionary rows.
file = open("Test.json", "r")
student_dic = json.load(file)  # the load function returns a single dictionary row.
file.close()
print(student_dic, type(student_dic))

# Working with multiple rows of data #
# However, if we have multiple rows of data the load method will create a list of dictionary rows
# Let's test this out by creating two rows of data and adding it to a list
student1_obj = Student(first_name="Bob",last_name="Smith", gpa=3.8)
student2_obj = Student(first_name="Sue",last_name="Jones", gpa=4.0)
students_lst = [student1_obj, student2_obj]

# We want to save this data to a json file, but the json.dump method does not automatically work with custom classes.
# So, we have to convert the data into a list of dictionary rows like this:
json_students = []
for student in students_lst:
    student_dict = {"FirstName": student.first_name,
                    "LastName": student.last_name,
                    "GPA": student.gpa}
    json_students.append(student_dict)

# Now, we can use the dump() method to save the data to a json file
file = open("Test.json", "w")
json.dump(json_students, file, indent=2)
file.close()

# And we can use json.load() to create a list of dictionary rows from the files data like this:
file = open("Test.json", "r")
students_list_of_dictionary_rows = json.load(file)  # the load function returns a list of dictionary rows.
file.close()
print(students_list_of_dictionary_rows, type(students_list_of_dictionary_rows))

# However, if we want to use our custom Student class objects we need to convert the data once again!
student_objects = []
for row in students_list_of_dictionary_rows:
    student_obj = Student(first_name=row["FirstName"],
                          last_name=row["LastName"],
                          gpa=row["GPA"])
    student_objects.append(student_obj)


# REMEMBER:
# It's all the same student data, but we’re storing and converting it in different ways:
# - Strings are easy to display.
# - Lists are easy to access by position.
# - Dictionaries are flexible and work well with JSON.
# - Objects group data and behavior together.
# While this is often confusing for beginners, converting between data formats is a key skill in real-world programming.
