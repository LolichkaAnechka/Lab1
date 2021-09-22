import sys
#required for argv - list of parameters

def check(string, curr_pos):
    """Checks whether the input string is the correct entry for the 'formula' according EBNF syntax"""
    if not string[curr_pos].isdigit() and (string[curr_pos] not in oper_list or string[curr_pos-1] in oper_list):
        return False
    elif not curr_pos:
        if string[len(string)-1] not in oper_list:
            return True
    else:
        return check(string, curr_pos-1)

user_input = sys.argv[1:]
#parametr list
oper_list = ['+', '-']
#list of operation signs

if not user_input:
#check if there is an input
    print("No parameters")
else:
    user_input_str = "".join(user_input)
    #converting a list of parameters into string
    if check(user_input_str, len(user_input_str)-1):
        #if string is correct, printing the answer
        #else, printing the "False" message
        print("True", eval(user_input_str), sep=", ")
    else:
        print("False, None")