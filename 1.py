import sys
#required for argv - list of parameters

user_input = sys.argv[1:]
#copy all parameters except file name to object
user_input_str = " ".join(user_input)
#turning list of parameters to string with space separator
answer = eval(user_input_str)
#counting the expression with eval()
print(answer)
#printing out an answer
