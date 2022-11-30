# Complete the count_letters_and_digits function which
# accepts a parameter s that contains a string and returns
# two values, the number of letters in the string and the
# number of digits in the string
#
# Examples:
#   * "" returns 0, 0
#   * "a" returns 1, 0
#   * "1" returns 0, 1
#   * "1a" returns 1, 1
#
# To test if a character c is a digit, you can use the
# c.isdigit() method to return True of False
#
# To test if a character c is a letter, you can use the
# c.isalpha() method to return True of False
#
# Remember that functions can return more than one value
# in Python. You just use a comma with the return, like
# this:
#      return value1, value2 (as a tuple)


def count_letters_and_digits(s):
    count_letter = 0
    count_number = 0
    for digit in s:
        if digit.isdigit()== True:
            count_number += 1
        elif digit.isalpha()== True:
            count_letter += 1
        else:
            print("please resubmit string to include letter or number")
    return count_letter, count_number


print(count_letters_and_digits("123456789abc"))

#solved

#this will count the number of letters, and digits in a string that is input
# seems like you are going to need to loop thru the string and inspect if that is letter or number...
# first return is the letter
# second return is the number