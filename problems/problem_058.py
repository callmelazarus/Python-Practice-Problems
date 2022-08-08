# Write a function that meets these requirements.
#
# Name:       group_cities_by_state
# Parameters: a list of cities in the format "«name», «st»"
#             where «name» is the name of the city, followed
#             by a comma and a space, then the two-letter
#             abbreviation of the state
# Returns:    a dictionary whose keys are the two letter
#             abbreviations of the states in the list and
#             whose values are a list of the cities appearing
#             in that list for that state
#
# In the items in the input, there will only be one comma.
#
# Examples:
#     * input:   ["San Antonio, TX"]
#       returns: {"TX": ["San Antonio"]}
#     * input:   ["Springfield, MA", "Boston, MA"]
#       returns: {"MA": ["Springfield", "Boston"]}
#     * input:   ["Cleveland, OH", "Columbus, OH", "Chicago, IL"]
#       returns: {"OH": ["Cleveland", "Columbus"], "IL": ["Chicago"]}
#
# You may want to look up the ".strip()" method for the string.

"""
converts string list, into dictionary:

strip method for strings - may be used to just cleanup the whitespace before the abbrev

key:value -> abbreviation as key. Value: list of the cities associated with list

will likely need to loop thru list, and work with each element in that list

break string part at the ',', then .split the abbreviation

fill dictionary with key's associated with abbreviation.
fill value with the city

problem" I am overwriting the existing values....

NOT SOLVED---------------------------------------------------------------------------------
"""

def group_cities_by_state(cities):
    soln = {}
    large = []
    for city in cities:
        city_abv = city.split(",")
        abv = city_abv[1].strip() # generates abbreviation
        city_name = city_abv[0] # generates city
        entry = [abv, city_name]
        large.append(entry) # creates a large list with the first entry being the state
    # create key/value pairs of the same state
    # loop thru list -> and group the same first entries


# time to create key:value pairs -> to be later infilled with values
    unique_states = {} # dictionary of all the cities
    for state in large:
        unique_states[state[0]] = None
    
    
    
    print(large)
    print(unique_states)    

group_cities_by_state(["Cleveland, OH", "Columbus, OH", "Chicago, IL"])