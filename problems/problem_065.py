# Write a function that meets these requirements.
#
# Name:       biggest_gap
# Parameters: a list of numbers that has at least
#             two numbers in it
# Returns:    the largest gap between any two
#             consecutive numbers in the list
#             (this will always be a positive number)
#
# Examples:
#     * input:  [1, 3, 5, 7]
#       result: 2 because they all have the same gap
#     * input:  [1, 11, 9, 20, 0]
#       result: 20 because from 20 to 0 is the biggest gap
#     * input:  [1, 3, 100, 103, 106]
#       result: 97 because from 3 to 100 is the biggest gap
#
# You may want to look at the built-in "abs" function

"""
input -> list with at least two numbers

output -> largest gap between any two consecutive numbers in that same list

challenge - need to be able to compare one list item, and take the difference with the previous number. 
save that difference in a particular variable
replace that number if the new difference is bigger than the previous solution

"""

def biggest_gap_with_range(list):
    gap = 0
    for item in range(len(list)):
        gap_iteration = list[item] - list[item+1]
        if gap_iteration > gap:
            gap = gap_iteration
    return gap



def biggest_gap(list):
    prev_number = list[0]
    gap = 0
    for number in list:
        new_gap = abs(number-prev_number)
        if new_gap > gap:
            gap = new_gap
        prev_number=number
    return gap


print(biggest_gap([1, 3, 100, 103, 106]))

