# Complete the sum_of_first_n_even_numbers function which
# accepts a numerical count n and returns the sum of the
# first n even numbers
#
# If the value of the limit is less than 0, then it should
# return None
#
# Examples:
#   * -1 returns None
#   * 0 returns 0
#   * 1 returns 0+2=2
#   * 2 returns 0+2+4=6
#   * 5 returns 0+2+4+6+8+10=30
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.


# LOL  .... this function will return the sum of the even numbers less than the limit n.... not the intention of function 
def sum_of_first_n_even_numbers2(n):
    sum = 0
    if n < 0:
        return None
    for num in range(1,n):
        if num%2 == 0:
            sum += num
    return sum


def sum_of_first_n_even_numbers(n):
    sum = 0
    limit = n*2
    if n < 0:
        return None
    for num in range(1,limit+1):
        if num%2 == 0:
            sum += num
    return sum
    

num = 7

print(sum_of_first_n_even_numbers(num))




# returns the sum of the first n even numbers
# find a way to create an ascending list of even numbers based on the number listed.......
# 