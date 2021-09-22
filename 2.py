import sys
import operator

user_input = sys.argv[1:]

if not len(user_input) == 3:
    print("Not enough parameters")

else:
    # copy all parameters except file name to object
    operation_dict = {"add": operator.add,
                      "sub": operator.sub,
                      "mul": operator.mul,
                      "div": operator.truediv}
    # dictionary with all arithmetic operations needed
    try:
        # trying to count the expression with operation from the dictionary
        # printing an answer if everything ok
        # printing an error message if user made mistake
        print(operation_dict[user_input[0]](int(user_input[1]), int(user_input[2])))
    except ValueError:
        print("Input error (Value error)")
    except KeyError:
        print("Incorrect input! The first argument should be: add, div, multi or sub")
    except ZeroDivisionError:
        print("Division by zero")
