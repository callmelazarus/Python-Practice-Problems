# Complete the remove_duplicate_letters that takes a string
# parameter "s" and returns a string with all of the
# duplicates removed.
#
# Examples:
#   * For "abc", the result is "abc"
#   * For "abcabc", the result is "abc"
#   * For "abccba", the result is "abc"
#   * For "abccbad", the result is "abcd"
#
# If the list is empty, then return the empty string.

def remove_duplicate_letters(s):
    if s == "":
        return ""
    pruned = ""
    for letter in s:
        if letter in s and letter not in pruned:
            pruned += letter
    return pruned

# def remove_duplicate_letters(s):
#     if s == "":
#         return ""
#     return set(s)

test = "abcabc"

print(remove_duplicate_letters(test))

#solved

#pc
# takes a string parameter
# returns string with all duplicates removed
# may need to use in operator
# plan on looping through string, and seeing if that single letter is in the entire list and in the new list. it can't be in the new list
# if it is in the list -> need to find a way to remove this.... ooo
# create blank string
# add letter to this empy string ONLY if there are no duplicates.