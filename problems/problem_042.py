# Complete the pairwise_add function which accepts two lists
# of the same size. It creates a new list and populates it
# with the sum of corresponding entries in the two lists.
#
# Examples:
#   * list1:  [1, 2, 3, 4]
#     list2:  [4, 5, 6, 7]
#     result: [5, 7, 9, 11]
#   * list1:  [100, 200, 300]
#     list2:  [ 10,   1, 180]
#     result: [110, 201, 480]
#
# Look up the zip function to help you with this problem.

def pairwise_add(list1, list2):
    soln = []
    for index in range(0,len(list1)):
        soln.append(list1[index]+list2[index])
    return soln


list1 = [1, 2, 3, 4]
list2=[4, 5, 6, 7]

print(pairwise_add(list1, list2))



# input -> two lists of same size

# potential solutions
# try to avoid looping right away
# what kind of legwork could I take care of beforehand?

# use range? to figure out how many loops I will actually go thru

# 1. make a dictionary???? is this the way to go?
# 2. group the entries, and then sum them?



# output -> new list, with the sum of the corresponding entries