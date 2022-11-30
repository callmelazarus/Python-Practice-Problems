# Write a function that meets these requirements.
#
# Name:       sum_fraction_sequence
# Parameters: a number
# Returns:    the sum of the fractions of the
#             form 1/2+2/3+3/4+...+number/number+1
#
# Examples:
#     * input:   1
#       returns: 1/2
#     * input:   2
#       returns: 1/2 + 2/3
#     * input:   3
#       returns: 1/2 + 2/3 + 3/4

"""
return the sum of the fractions in the form number/number+1

could use a for / range situation.... and add to empty list

SOLVED 8/7/2022
"""

def sum_fraction_sequence(num):
    soln = []
    for i in range(num):
        fractioned = str(i+1) + "/" + str(i+2)
        soln.append(fractioned)
    return soln

print(sum_fraction_sequence(1))