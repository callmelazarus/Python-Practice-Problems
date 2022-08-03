# Complete the check_password function that accepts a
# single parameter, the password to check.
#
# A password is valid if it meets all of these criteria
#   * It must have at least one lowercase letter (a-z)
#   * It must have at least one uppercase letter (A-Z)
#   * It must have at least one digit (0-9)
#   * It must have at least one special character $, !, or @
#   * It must have six or more characters in it
#   * It must have twelve or fewer characters in it
#
# The string object has some methods that you may want to use,
# like ".isalpha", ".isdigit", ".isupper", and ".islower"

def check_password(password):
    digit_limit = 0
    lower_limit = 0
    upper_limit = 0
    spec_character_limit = 0
    if len(password) <= 12 and len(password) >= 6:
        for char in password:
            if char.isdigit():
                digit_limit += 1
            elif char.islower():
                lower_limit += 1
            elif char.isupper():
                upper_limit += 1
            elif char == "$" or char == "!" or char == "@":
                spec_character_limit += 1
        soln_list = [digit_limit, lower_limit, upper_limit, spec_character_limit]
        print(soln_list)
        if soln_list.count(0) >= 1:
            return False # password ng
        return True # password ok
    else:
        return False
    
            


password = "A0z!ac"

print(check_password(password))


# input -> string password to be checked

# have a counter. I would like it such that if the counter is Greater than 0. than something is wrong. This means I need to add to it, if a condition is not met....
# maybe its better if I add to it, if the condition IS met...

# loop to find casing. need at last one lower case

# loop to find digit

# loop to find one character (find char value of signature)

# loop to find length check

# may need to use break/condinue


#output -> True or False if the string meets ALL criteria