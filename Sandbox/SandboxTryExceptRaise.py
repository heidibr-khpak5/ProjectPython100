#
# Heidi Testing and practicing try except;
# HB Nov. 11, 2026 start
# declare variables
# HB  Nov 23, 2026 add some bools tell what to run
Run_Except=False
Run_dict_to_json = False

Run_File_except = True
Run_File_write_except = False
Run_say_goodbye= False
if Run_Except:
    try:
        first_name:list =["John", "Henr5y", "Axl"]
        print(type(first_name))
        print(first_name)
        # do some checking
        for each in first_name:
            if not each.isalpha():
                raise ValueError(f"'{each}' contains non-letter characters")
        if first_name[1]=="Hans":
            print(first_name[1]," Hello, how are you?" )
        else:
            print("I expected Hans")
    except ValueError as e:
        print(e)


    except Exception as e:
        print("error!")
        print("Technical Error Message:")
        print(e)
        print(e.__doc__)
        print(e.__str__())
# another test goodbye
if Run_say_goodbye:
    print("\nGood Job Heidi")



if Run_File_except: # look for file not found and make sure it is closed

    import json

    # Data --------------------------------------------- #
    FILE_NAME: str = 'sandboxFilejson.json'
    student_table: list = []
    file = None

    # Processing --------------------------------------- #
    # Read from the JSON file
    try:
        file = open(FILE_NAME, "r")
        student_table = json.load(file)
        print(student_table)
        for item in student_table:
            print(
                f" ID: {item['ID']}, Name: {item['Name']}"
                f" email:{item["Email"]}, age:{item['Age']}")

        file.close()
    except FileNotFoundError as e:
        print("Text file must exist before running this script!\n")
        print("-- Technical Error Message -- ")
        print(e, e.__doc__, type(e), sep='\n')
    except Exception as e:
        print("There was a non-specific error!\n")
        print("-- Technical Error Message -- ")
        print(e, e.__doc__, type(e), sep='\n')
    finally:
        if file is not None and file.closed == False:
            file.close()

if Run_File_write_except:
    import json
    FILE_NAME= "file_namej.json"
    file = None
    student_table:list=[]

    try:
        file = open(FILE_NAME, "w")
        json.dump(student_table, file)
    except FileNotFoundError as e:
        print("Text file must exist before running this script!\n")
        print("-- Technical Error Message -- ")
        print(e, e.__doc__, type(e), sep='\n')
    except Exception as e:
        print("There was a non-specific error!\n")
        print("-- Technical Error Message -- ")
        print(e, e.__doc__, type(e), sep='\n')
    finally:
        if file is not None and file.closed == False:
            file.close()

