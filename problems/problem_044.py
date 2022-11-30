# Complete the translate function which accepts two
# parameters, a list of keys and a dictionary. It returns a
# new list that contains the values of the corresponding
# keys in the dictionary. If the key does not exist, then
# the list should contain a None for that key.
#
# Examples:
#   * keys:       ["name", "age"]
#     dictionary: {"name": "Noor", "age": 29}
#     result:     ["Noor", 29]
#   * keys:       ["eye color", "age"]
#     dictionary: {"name": "Noor", "age": 29}
#     result:     [None, 29]
#   * keys:       ["age", "age", "age"]
#     dictionary: {"name": "Noor", "age": 29}
#     result:     [29, 29, 29]
#
# Remember that a dictionary has the ".get" method on it.

def translate(key_list, dictionary):
    soln = []
    for description in key_list:
        value = dictionary.get(description)
        soln.append(value)
    return soln

keys=      ["eye color", "age"]
dictionary= {"name": "Noor", "age": 29}

print(translate(keys, dictionary))

# loop thru keyes

# get wil reutrn None if key doesn't exist

# simply add .get the value



# output -> list containing corresponding values to corresponding keys. if key does not exist, should return none
# list
# lenght matches length of keys
