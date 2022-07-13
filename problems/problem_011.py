# Complete the is_divisible_by_5 function to return the
# word "buzz" if the value in the number parameter is
# divisible by 5. Otherwise, just return the number.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def is_divisible_by_5(number):
    if number % 5 == 0:
        return "buzz"
    return number

x = 232
y = 235
print(is_divisible_by_5(x))
print(is_divisible_by_5(y))


# function -> testing if num % 5 == 0
# if True return string "buzz"
# if False return number itself

