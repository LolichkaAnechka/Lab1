import sys
import operator

user_input = sys.argv[1:]
#copy all parameters except file name to object
operation_dict = {"add": operator.add,
    "sub": operator.sub,
    "mul": operator.mul,
    "div": operator.truediv}
#dictionary with all arifmetic oprerations needed
answer = operation_dict[user_input[0]](int(user_input[1]), int(user_input[2]))
#getting the answer
print(answer)