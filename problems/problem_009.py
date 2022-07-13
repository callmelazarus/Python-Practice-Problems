# Complete the is_palindrome function to check if the value in
# the word parameter is the same backward and forward.
#
# For example, the word "racecar" is a palindrome because, if
# you write it backwards, it's the same word.

# It uses the built-in function reversed and the join method
# for string objects.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.


def is_palindrome(strings): # function name
    new_word = "".join(strings)   #
    print(new_word)
    if new_word == new_word[::-1]:
        return True
    return False


x = "whatever"
y = "racecar"
z = ('evil', 'olive')



# print(is_palindrome(z))
# print(is_palindrome(y))

#convert string to list
#reverse list
#check if each letter is the same



fruit1 = ['a','p','p','l','e']

fruit1.reverse()

print(fruit1


# use if statement to check if og work == reverse word
# return True/False

#built in function -> reversed and join method


# print(x[::-1])   #prints word backwords -> using slicing

