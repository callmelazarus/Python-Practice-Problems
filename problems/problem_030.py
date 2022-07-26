# Complete the find_second_largest function which accepts
# a list of numerical values and returns the second largest
# in the list
#
# If the list of values is empty, the function should
# return None
#
# If the list of values has only one value, the function
# should return None
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.



def find_second_largest(values):
    if len(values) <= 1:
        return None
    adj_list = values
    adj_list.sort(reverse = True)
    second_largest = adj_list[1]
    return second_largest

    
#accepts a list
#returns the 2nd largest on the list
#how do you determine the 2nd largest #....



list1 = [12, 43, 123, 12, 192]
# list2 = ['a','d', 'e', 'f', 'z', 'b']


print(find_second_largest(list1))
# print(find_second_largest(list2))

# solved