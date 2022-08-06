# Write a function that meets these requirements.
#
# Name:       username_from_email
# Parameters: a valid email address as a string
# Returns:    the username portion of the email address
#
# The username portion of an email is the substring
# of the email address that appears before the @
#
# Examples
#    * input:   "basia@yahoo.com"
#      returns: "basia"
#    * input:   "basia.farid@yahoo.com"
#      returns: "basia.farid"
#    * input:   "basia_farid+test@yahoo.com"
#      returns: "basia_farid+test

"""
input -> valid email address as string

output -> address before the @ symbol....

Find what index the @ is?

even better - split list at the @ symbol...

Return the string values using slicing before the at



"""

def username_from_email(email):
    test = email.split("@")
    return test[0]



print(username_from_email("jay@gmail.com"))
