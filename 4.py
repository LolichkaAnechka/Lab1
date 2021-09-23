bars = [16, 13, 12]
capacity = 25
# start data


def knapsack(knap_cap, weight):
    """Function to count the maximum weight you can fit in knapsack"""
    numb_of_bars = len(weight)
    subp_list = [[0 for x in range(knap_cap + 1)] for x in range(numb_of_bars + 1)]
    # list that contains all subproblems exist filled with zeros
    for index in range(1, numb_of_bars + 1):
        for value in range(knap_cap + 1):
            if weight[index - 1] <= value:
                subp_list[index][value] = max(weight[index - 1] + subp_list[index - 1][value - weight[index - 1]],
                                                                                subp_list[index - 1][value])
            # filling the row with the biggest value possible with the considered bars

            else:
                subp_list[index][value] = subp_list[index - 1][value]
            # taking the value from the previous row if the weight of a bar is higher than the value we consider now
    return subp_list[numb_of_bars][knap_cap]
    # returning the value in the very end of subproblem list that will be the solution


print(knapsack(capacity, bars))
