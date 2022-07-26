# Complete the sum_of_squares function which accepts
# a list of numerical values and returns the sum of
# each item squared
#
# If the list of values is empty, the function should
# return None
#
# Examples:
#   * [] returns None
#   * [1, 2, 3] returns 1*1+2*2+3*3=14
#   * [-1, 0, 1] returns (-1)*(-1)+0*0+1*1=2
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.


def sum_of_squares(values):
    if values == []:
        return None
    final = 0
    for num in values:
        final += num*num
    return final



        # returns the numbers squared in a list
        # how do you square a number?
        # will need to loop, taking each value and squaring it

list1 = [1, 2, 3] # returns 1*1+2*2+3*3=14
list2 = [-1, 0, 1] #returns (-1)*(-1)+0*0+1*1=2

print(sum_of_squares(list1))
print(sum_of_squares(list2))