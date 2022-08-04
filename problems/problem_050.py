# Write a function that meets these requirements.
#
# Name:       halve_the_list
# Parameters: a single list
# Returns:    two lists, each containing half of the original list
#             if the original list has an odd number of items, then
#             the extra item is in the first list
#
# Examples:
#    * input: [1, 2, 3, 4]
#      result: [1, 2], [3, 4]
#    * input: [1, 2, 3]
#      result: [1, 2], [3]

def halve_the_list(list1):
    list_half1 = []
    list_half2 = []
    for item in range(len(list1)):
        if item < len(list1)/2:
            list_half1.append(list1[item])
        else:
            list_half2.append(list1[item])
    return list_half1, list_half2


list1 = [1, 2,3, 4, 5, 6, 7]
list2 = [1, 2,3]
print(halve_the_list(list1))