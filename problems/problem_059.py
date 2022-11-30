# Write a function that meets these requirements.
#
# Name:       specific_random
# Parameters: none
# Returns:    a random number between 10 and 500, inclusive,
#             that is divisible by 5 and 7
#
# Examples:
#     * returns: 35
#     * returns: 105
#     * returns: 70
#
# Guidance:
#   * Generate all the numbers that are divisible by 5
#     and 7 into a list
#   * Use random.choice to select one

"""
Generate a list of values

SOLVED 8/6/2022
"""

from random import choice, randint, random

def specific_random():
    choice_list = []
    for i in range(10,501):
        if i%5 == 0 and i%7 == 0:
            choice_list.append(i)
    return choice(choice_list)


