# Complete the max_in_list function to find the
# maximum value in a list
#
# If the list is empty, then return None.
#

def max_in_list(values):
    if values == []:
        return None
    return max(values)


test_list = [12, 43, 2]
print(max_in_list(test_list))