# Complete the sum_of_first_n_numbers function which accepts
# a numerical limit and returns the sum of the numbers from
# 0 up to and including limit.
#
# If the value of the limit is less than 0, then it should
# return None
#
# Examples:
#   * -1 returns None
#   * 0 returns 0
#   * 1 returns 0+1=1
#   * 2 returns 0+1+2=3
#   * 5 returns 0+1+2+3+4+5=15
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def sum_of_first_n_numbers(limit):
    sum = 0
    if limit < 0:
        return None
    elif limit == 0:
        return 0
    else:
        for num in range(1, limit+1):
            sum += num
    return sum

num = 5

print(range(num+1))

print(sum_of_first_n_numbers(num))

# returns sum of numbers from 0 to the limit
# seems like I will need to find a way to count integers from 0 to that number, and add them all up