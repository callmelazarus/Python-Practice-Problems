# Write a function that meets these requirements.
#
# Name:       generate_lottery_numbers
# Parameters: none
# Returns:    a list of six random unique numbers
#             between 1 and 40, inclusive
#
# Example bad results:
#    [4, 2, 3, 3, 1, 5] duplicate numbers
#    [1, 2, 3, 4, 5] not six numbers
#
# You can use randint from random, here, or any of
# the other applicable functions from the random
# package.
#
# https://docs.python.org/3/library/random.html


from random import randint
def generate_lottery_numbers():
    soln = []
    while len(soln) < 6:
        new_num = randint(1,40)
        if new_num not in soln:
            soln.append(new_num)
    print(soln)


generate_lottery_numbers()

"""
=return -> 6 unique numbers, between 1 and 40

create empty list

fill in list with random variable if it is NOT in list



"""