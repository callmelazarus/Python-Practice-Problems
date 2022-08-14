# Write a class that meets these requirements.
#
# Name:       Person
#
# Required state:
#    * name, a string
#    * hated foods list, a list of names of food they don't like
#    * loved foods list, a list of names of food they really do like
#
# Behavior:
#    * taste(food name)  * returns None if the food name is not in their
#                                  hated or loved food lists
#                        * returns True if the food name is in their
#                                  loved food list
#                        * returns False if the food name is in their
#                                  hated food list
#
# Example:
#    person = Person("Malik",
#                    ["cottage cheese", "sauerkraut"],
#                    ["pizza", "schnitzel"])
#
#    print(person.taste("lasagna"))     # Prints None, not in either list
#    print(person.taste("sauerkraut"))  # Prints False, in the hated list
#    print(person.taste("pizza"))       # Prints True, in the loved list


# class Person
    # method initializer with name, hated foods list, and loved foods list
        # self.name = name
        # self.hated_foods = hated_foods
        # self.loved_foods = loved_foods
    # method taste(self, food)
        # if food is in self.hated_foods
            # return False
        # otherwise, if food is in self.loved_foods
            # return True
        # otherwise
            # return None
"""
class methods practice
SOLVED - 8/13/2022

LESSON:
class methods - take in self (if you use the attributes, which you likely will....)
and another argument
"""
class Person:
    def __init__(self, name, hated_foods_list, loved_foods_list):
        self.name = name
        self.hated_foods_list = hated_foods_list
        self.loved_foods_list = loved_foods_list

    def taste(self, food):
        if food in self.hated_foods_list:
            return False
        elif food in self.loved_foods_list:
            return True
        else:
            return None

person = Person("Malik",
                ["cottage cheese", "sauerkraut"],
                ["pizza", "schnitzel"])

print(person.taste(food = "lasagna"))     # Prints None, not in either list
print(person.taste("sauerkraut"))  # Prints False, in the hated list
print(person.taste("pizza"))       # Prints True, in the loved list