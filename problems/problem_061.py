# Write a function that meets these requirements.
#
# Name:       remove_duplicates
# Parameters: a list of values
# Returns:    a copy of the list removing all
#             duplicate values and keeping the
#             original order
#
# Examples:
#     * input:   [1, 1, 1, 1]
#       returns: [1]
#     * input:   [1, 2, 2, 1]
#       returns: [1, 2]
#     * input:   [1, 3, 3, 20, 3, 2, 2]
#       returns: [1, 3, 20, 2]

"""
returns copy of list, removind duplicates, but retaining order..
using list comprehensions seems to be the easiest way..

"""


def remove_duplicates(list): # fast solution
    soln = []
    [soln.append(x) for x in list if x not in soln]
    return soln


print(remove_duplicates([1, 3, 3, 20, 3, 2, 2]))


def remove_dup(list): # not as fast solution
    soln = []
    for item in list:
        if item not in soln:
            soln.append(item)
    return soln


print(remove_dup([1, 3, 3, 20, 3, 2, 2]))
