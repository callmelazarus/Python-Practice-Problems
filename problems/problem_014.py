# Complete the can_make_pasta function to
# * Return true if the ingredients list contains
#   "flour", "eggs", and "oil"
# * Otherwise, return false
#
# The ingredients list will always contain three items.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def can_make_pasta(ingredients):
    if "flour" in ingredients:
        if "eggs" in ingredients:
            if "oil" in ingredients:
                return True
    return False

list1 = ["flour", "eggs", "oil"] #true
list2 = ["flour", "eggs", "oil", "bacon"] # long
list3 = ["flour", "watermellon"] #too short
list4 = ["flour", "eggs", "fish"] #false
list5 = ["flour", "croissont", "coffee"] #false

print(can_make_pasta(list1))
print(can_make_pasta(list2))
print(can_make_pasta(list3))
print(can_make_pasta(list4))
print(can_make_pasta(list5))

# for item in ingredients:

# soln1. if we had list containing flour.egg.oil. -> compare with ingredients 
# comparing two lists -> research methods that 
# loop thru list -> 
# using a counter - > which counts if the 

# soln2. new list -> loop ingredients and seeing if it matches with flour, eggs, oil
# loop through each element
# if statements OR multiple ands

# * [flower, egg, oil] Vocab
# * [can_make_pasta] Functions
# * [ ] Methods

# ## Problem decomposition

# * [ingredients - list] Input
# * [True/False] Output
# * [ ] Examples
# * [ yes ] Conditions (if) - > if list contains flour, egg, and oil -> needs all three
# * [ yes ] Iteration (loop) -> loop thru each ingred. in list