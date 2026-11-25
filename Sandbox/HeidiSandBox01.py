#
# Heidi Testing and practicing try except;
# HB Nov. 11, 2026 start
# declare variables
# HB  Nov 23, 2026 add some bools tell what to run
Run_Except=False
Run_dict_to_json = False

Run_ File_jsonIO= True
Run_say_goodbye= True
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

if Run_File_jsonIO
