import sys

status = True
user_input = sys.argv[1]
#copy all parameters except file name to object
input_len= len(user_input)
#getting lenght of user input 
print(user_input)
if user_input:
    #checking if there is a string 
    for x in range(input_len):
        if(user_input[x].isalpha() or not (user_input[x].isnumeric()) and not (user_input[x]==('+' or '-'))):
            #cheking if there is an alphabetic symbol, or any other except the numbers and arifmetic operators
            status = False
            break
        elif((user_input[x]==('+' or '-')) and x==input_len-1):
            #cheking if there is an operation symbol in the end of the string
            status = False
            break
        elif((x==0 or user_input[x-1]==('+' or '-')) and user_input[x]=='0'):
            #checking if there is a number starting with 0
            status = False
            break
        elif((user_input[x] == ('+' or '-')) and (user_input[x+1] == ('+' or '-'))):
            #checking if there is an operation number near another one
            status = False
            break
        
else:
    status = False

if(status):
    #forming the result
    result = (status, eval(user_input))
else:
    result = (status, None)

print(result)
