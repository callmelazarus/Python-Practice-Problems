# Complete the can_skydive function so that determines if
# someone can go skydiving based on these criteria
#
# * The person must be greater than or equal to 18 years old, or
# * The person must have a signed consent form

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def can_skydive(age, has_consent_form):
    if has_consent_form == 'yes':
        return True



# two arguments to pass

# def function - takes two parameters

# if persons_form == b -> consent form
# elif persons_age > = 18
# else ->

# return message True/False and/or "You can skydive", "you can't skydive" -> covering specific conditions

skydiver_age_check = input("Are you older than 17? (yes/no) ")  # yes / no
consent_form = input("Do you have a consent form? (yes/no) ")  # yes / no

# call the function and test it
print(can_skydive(skydiver_age_check, consent_form))
