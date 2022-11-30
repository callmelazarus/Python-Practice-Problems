# Write a function that meets these requirements.
#
# Name:       shift_letters
# Parameters: a string containing a single word
# Returns:    a new string with all letters replaced
#             by the next letter in the alphabet
#
# If the letter "Z" or "z" appear in the string, then
# they would get replaced by "A" or "a", respectively.
#
# Examples:
#     * inputs:  "import"
#       result:  "jnqpsu"
#     * inputs:  "ABBA"
#       result:  "BCCB"
#     * inputs:  "Kala"
#       result:  "Lbmb"
#     * inputs:  "zap"
#       result:  "abq"
#
# You may want to look at the built-in Python functions
# "ord" and "chr" for this problem

"""
function that shifts the letter one, next inthe alphabed.

z turns to a -> 

case is retained

consider using ord and chr
change characters to integer -> ord(leter) 
add 1 to value
change integer back to character -> chr(integer)

SOLVED: 8/8/2022

"""

def shift_letters(word):
    soln = ""
    for letter in word:
        if letter == 'z':
            soln += 'a'
        elif letter == 'Z':
            soln += 'A'
        else:
            adj_letter = chr(ord(letter) + 1)
            soln += adj_letter
    return soln


print(shift_letters("zap"))

print(f"z is { ord('z') }")
print(f"Z is { ord('Z') }")

print(f"a is { ord('a') }")
print(f"A is { ord('A') }")
