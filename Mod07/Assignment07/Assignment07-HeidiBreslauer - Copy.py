# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   HeidiBreslauer, Nov 24, 2026, start
#   HeidiBreslauer, Nov 25, 2026, start over
#   HeidiBreslauer,Nov 25. Got through the classes, check on what I left out
#   HeidiBreslauer,Nov 26, 2026 worked on get user input into objects
#   Heidi Breslauer, Nov 26, 2026, - created dictionary and list for student_json
#                                   -debugged file read, file write
# ------------------------------------------------------------------------------------------ #
import json # to read and write json files

# from Sandbox.SandboxTryExceptRaise import first_name

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.
student_objects: object = []


# TODO Create a Person Class2
# TODO Add first_name and last_name properties to the constructor
# TODO Create a getter and setter for the first_name property
# TODO Create a getter and setter for the last_name property
# TODO Override the __str__() method to return Person data

# defining class
# HBreslauer Nov 25, 2026, created and tried to make it look real with indents etc
# overrode the __str__;
class Person:
    # you can define the arguments here, or bring them in

    # this is for constructors
    def __init__(self, first_name: str = "",
                 last_name: str = ""):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):  # override the python default
        return f"{self.first_name}, {self.last_name}"

        # for the getter

    @property
    def first_name(self):
        return self.__first_name.title()

    @first_name.setter
    def first_name(self, value: str):
        if value.isalpha() or value == "":
            self.__first_name = value
        else:
            raise ValueError(
                "The first name should only contain letters.")

    # Now the property and setter for lastname
    @property
    def last_name(self):
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value: str):
        if value.isalpha() or value == "":
            self.__last_name = value
        else:
            raise ValueError(
                "The last name should only contain letters.")

    # create a method to override the default __str__()
    def __str__(self):
        return f'{self.first_name},{self.last_name}'



# TODO Create a Student class the inherits from the Person class
# TODO call to the Person constructor and pass it the first_name and last_name data
# TODO add a assignment to the course_name property using the course_name parameter
# TODO add the getter for course_name
# TODO add the setter for course_name
# TODO Override the __str__() method to return the Student data



class Student(Person):
    def __init__(
        self, first_name: str ="",
        last_name:str="", course_name: str=""
        ):
        super().__init__(first_name=first_name, last_name=last_name) #childs gets parent to run this part
        self.course_name = course_name # add the new item

    @property
    def course_name(self):
        return self.__course_name.upper()


    @course_name.setter
    def course_name(self, value:str): # we would want to check for valid course name here
        self.__course_name = value

    def __str__(self):  # create a method to override the default __str__()
        return f'{self.first_name},{self.last_name},{self.course_name}'

# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    H Breslauer, Nov 25, 2026, coded  read from json
    """
    @staticmethod
    def read_data_from_file(file_name: str):
        """ This function reads data from a json file and loads it into a list of dictionary rows
        then returns the list filled with student data.

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        H Breslauer, Nov 25, 2026, coded  read from json

        :param file_name: string data with name of file to read from

        :return: list
        """
        #print("did I get to theis line")
        file = None
        #I commented out a bunch of stuff
        try:
            # Get a list of dictionary rows from the data file
            file = open(file_name, "r")
            json_students = json.load(file)
            file.close()
            print(json_students)

            # Convert the list of dictionary rows into a list of Student objects

            #  convert dictionary data to student object
            for each in json_students:
                student_object = Student(
                    first_name=each["FirstName"],
                    last_name= each["LastName"],
                    course_name= each["CourseName"]
                )
                student_objects.append(student_object)
            print("try to print the objects read from json and changed to object")
            print(student_objects)
        except FileNotFoundError as e:
            IO.output_error_messages(message = "Error: File not found.")
            print(e)
            print(e.__doc__)
            print(e.__str__())
            print(type(e))
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)
            print(e)

        finally:
            if file is not None and file.closed == False:
                file.close()
        # print(student_objects) by row aka each
        for each in student_objects:
            print(each)
            #print(f'Student {each.first_name} {each.last_name}'
            #      f' is enrolled in {each.course_name}.')
        #using the IO method
        #IO.output_student_and_course_names(student_objects)

        return student_objects


    @staticmethod
    def write_data_to_file(file_name, student_objects: list):
        """ This function writes data to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        HeidiBreslauer, Nov 26, 2026

        :param file_name: string data with name of file to write to
        :param student_data: list of dictionary rows to be writen to the file

        :return: None
        """
        file = None
        student_json: list =[]

        try:#convert Student objects into dictionaries
            for each in student_objects: # create a dictionary
                student_json_row = {
                    "FirstName": each.first_name,
                    "LastName": each.last_name,
                    "CourseName": each.course_name
                }
                student_json.append(student_json_row)


                #print(student_json)
                file = open(file_name, "w")
                json.dump(student_json, file)

        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message,error=e)
        finally:
            if file is not None and file.closed == False:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    RRoot,1.2.2030,Added menu output and input functions
    RRoot,1.3.2030,Added a function to display the data
    RRoot,1.4.2030,Added a function to display custom error messages
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function


        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_and_course_names(student_objects: list):
        """ This function displays the student and course names to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        Heidi Breslauer, Nov 26, 2026, modified to use objects

        :param student_objects list of student_object rows to be displayed

        :return: None
        """

        print("-" * 50)
        for each in student_objects:
            print(
                f' Student {each.first_name} '
                f' {each.last_name} is enrolled in '
                f' {each.course_name}.'
            )
        print("-" * 50)

    @staticmethod
    def input_student_data(student_objects: list):
        """ This function gets the student's first name and last name, with a course name from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :param student_data: list of dictionary rows to be filled with input data

        :return: list
        """

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should be letters.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should be letters.")
            course_name = input("Please enter the name of the course: ")

            #create student_object and append to student_objects
            student_object=Student( first_name= student_first_name,
                       last_name= student_last_name,
                       course_name = course_name)
            print(type(student_objects))
            print(student_objects)
            student_objects.append(student_object)




            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the values was the correct type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_objects


# Start of main body

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
student_objects = FileProcessor.read_data_from_file(file_name=FILE_NAME)

# Present and Process the data
while True:

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        student_objects = IO.input_student_data(student_objects=student_objects)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_names(student_objects)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_objects=student_objects)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
