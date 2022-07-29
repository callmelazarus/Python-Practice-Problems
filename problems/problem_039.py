# Complete the reverse_dictionary function which has a
# single parameter that is a dictionary. Return a new
# dictionary that has the original dictionary's values
# for its keys, and the original dictionary's keys for
# its values.
#
# Examples:
#   * input:  {}
#     output: {}
#   * input:  {"key": "value"}
#     output: {"value", "key"}
#   * input:  {"one": 1, "two": 2, "three": 3}
#     output: {1: "one", 2: "two", 3: "three"}

def reverse_dictionary(dictionary):
    dict_soln = {}
    for key, value in dictionary.items():
        dict_soln[value] = key
    return dict_soln


dict = {"one": 1, "two": 2, "three": 3}

dict2 = {"key": "value"}

print(reverse_dictionary(dict2))


# input -> dictionary

# create an empty dictionary solution

# Loop thru the input dict, and assign the key, to the value of solution dictionary

# same thing but vice versa for the value

# outpu -> swaps the keys and values for these dictionaries
