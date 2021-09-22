import sys
#required for argv - list of parameters
user_input = sys.argv[1:]
#copy all parameters except file name to object
if not user_input:
    print("No parameters")
else:
    user_input_str = "".join(user_input)
#turning list of parameters to string with space separator
    try:
        print(eval(user_input_str))
        #trying to count the expression with eval()
        #printing an answer if everything ok
        #printing an error message if user made mistake
    except NameError:
        print("Input error (Name error)")
    except ZeroDivisionError:
        print("Divinition by zero")
    except SyntaxError:
        print("Input error (Syntax error)")