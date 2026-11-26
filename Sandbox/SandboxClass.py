# practice and samples for class constructors, get set, inheritance
Run_Class = True
Run_Next = False
Run_say_goodbye= True





# defining class
# HBreslauer Nov 24, 2026, created and tried to make it look real with indents etc
# overrode the __str__;
# add new class
#define Classes

if Run_Class:

    class Person:
        # you can define the arguments here, or bring them in
        first_name: str="Jim"
        last_name: str="Morrison"

        #this is for constructors
        def __init__(self, first_name: str ="",
                    last_name:str=""):
            self.first_name = first_name
            self.last_name =last_name

        def __str__(self):   #override the python default
            return f"{self.first_name}, {self.last_name}"

            # for the getter
        @property
        def first_name(self):
            return self.first_name.title()

        @first_name.setter
        def first_name(self, value:str):
            if value.isalpha()  or value == "":
                self.__first_name= value
            else:
                raise ValueError("The first name should only contain letters.")
        #Now the property and setter for lastname
        @property
        def last_name(self):
            return self.__last_name.title()

        @last_name.setter
        def last_name(self,value:str):
            if value.isalpha() or value == "":
                self.__last_name = value
            else:
                raise ValueError("The last name should only contain letters.")
        #create a method to override the default __str__()
        def __str__(self):
            return f'{self.first_name},{self.last_name}'
        # syntax ok to here.

    class Student(Person):
        def __init__(
                self, first_name: str ="",
                last_name:str="", gpa : float=(0.00)
        ):
            super().__init__(first_name=first_name, last_name=last_name) #childs gets parent to run this part
            self.gpa = gpa # add the new item
    print("Finished class")

# work on another sectionl
if Run_say_goodbye:
    print("\nGood Job Heidi")

# NEW STUFF
# printing out the object which is a table of rows
# splitting an f string:
for each in student_objects
print(
    f'Student {each.first_name} '
    f'{each.last_name} is enrolled in '
    f'{each.course}.'
)




