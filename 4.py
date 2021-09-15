from typing import ValuesView


weight = [16, 13, 11]
Cap = 25
#start data


def knapSack(Cap, weight):
    numb_of_bars = len(weight)
    subp_list = [[0 for x in range(Cap + 1)] for x in range(numb_of_bars + 1)]
    #list that contains all subproblems exist
    for i in range(numb_of_bars + 1):
    #by incrementing, increments the number of bars can be used
        for value in range(Cap + 1):
        #value is used as the weight, so by incrementing it we can see what bars can fit in in a particular moment
            if i == 0 or value == 0:
                subp_list[i][value] = 0
            #filling the first row with zeros to fill next rows if the value we consider is lower then the weight of any bar we consider

            elif weight[i-1] <= value:
                subp_list[i][value] = max(weight[i-1] + subp_list[i-1][value-weight[i-1]],  subp_list[i-1][value])
            #filling the row considering the weight in previous ones

            else:
                subp_list[i][value] = subp_list[i-1][value]
            #taking the value from the previous row if the weight of a bar is higher than the value we consider now

    return subp_list[numb_of_bars][Cap]
    #returning the value in the very end of subproblem list that will be the solution 

print(knapSack(Cap, weight))
