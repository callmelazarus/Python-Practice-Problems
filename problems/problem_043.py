# Complete the find_indexes function which accepts two
# parameters, a list and a search term. It returns a new
# list that contains the indexes of the search term in
# the search list.
#
# Remember that indexes in Python are zero-based. That
# means the first element in the list is index 0.
#
# Examples:
#   * search_list:  [1, 2, 3, 4, 5]
#     search_term:  4
#     result:       [3]
#   * search_list:  [1, 2, 3, 4, 5]
#     search_term:  6
#     result:       []
#   * search_list:  [1, 2, 1, 2, 1]
#     search_term:  1
#     result:       [0, 2, 4]
#
# Look up the enumerate function to help you with this problem.

def find_indexes(search_list, search_term):
    dictionary = dict(enumerate(search_list))
    soln = []
    for key, value in dictionary.items():
        if search_term == value:
            soln.append(key)
        continue
    return soln

search_list =  [1, 2, 3, 4, 5]
search_term =  4

print(find_indexes(search_list, search_term))


# input -> list, and searched for number

# use enumerate function -> can convert to a dictionary or list

# using that dictionary -> the key, would be the iteration/index, and the value would be the serached item

# need to return the key, associated with the value

# returns list -> index of search term
