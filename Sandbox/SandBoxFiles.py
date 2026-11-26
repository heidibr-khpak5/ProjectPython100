# working with files
# Heidi Breslauer, Nov 25, 2026
FILE_NAME=("sandboxFileTest.txt")  # note the type: csv, json, txt
file = None   # no file handle yet

#sample data dictionary rows
table: list =[]
row1: dict={}
row2: dict={}

row1={"ID": 1, "Name":"BJ", "Email":"BJ@notmail.com","Age": str(42)}
row2={"ID": 2, "Name":"TJ", "Email":"TJ@notmail.com", "Age": str(38)}
table=[row1, row2]

print(table)
for each in table:
    print(each)

# file stuff
file=open(FILE_NAME, "w")
for each_row in table:
    file.write(f'{each_row["ID"]}, {each_row["Name"]}, {each_row["Email"]},'
               f'{each_row["Age"]}\n')
file.close()
print("txt file is written.")

# using json files write to json file dump
import json

FILE_NAMEJ="sandboxFileJson.json"   # constants are supposed to be constants!

file=open(FILE_NAMEJ, "w")
json.dump(table, file, indent=2) # table is a list of dictionary rows.
file.close()

print("Json file is written.")

# read the json file with structured error handling
try:
    file=open(FILE_NAMEJ, "r")
    data = json.load(file) #data is a list of dictionaries
    file.close()
# other except items first if using
except Exception as e:  # had a bug, adding except seems to have made me fix indents
    print(type(e))
    print(e)
    print(e.__doc__)
    print(e.__str__())

print("json file is read.")
print(data)

# convert json_table of dict to object
for each in json_students:

    student_object = Student(
        first_name=each["FirstName"],
        last_name=each["LastName"],
        course_name=each["CourseName"]
    )

    student_objects.append(student_object)

