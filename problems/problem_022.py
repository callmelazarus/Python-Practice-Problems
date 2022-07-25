# Complete the gear_for_day function which returns a list of
# gear needed for the day given certain criteria.
#   * If the day is not sunny and it is a workday, the list
#     needs to contain "umbrella"
#   * If it is a workday, the list needs to contain "laptop"
#   * If it is not a workday, the list needs to contain
#     "surfboard"

# if day is workday and it is NOT sunny -> list needs umbrella
# if day is workday -> need laptop
# if day is nonworkday -> need surfboard
# returns a LIST of gear needed for the day
def gear_for_day(is_workday, is_sunny):
    if is_workday == True and is_sunny == True:
        return ['laptop']
    elif is_workday == True and is_sunny == False:
        return ['laptop', 'umbrella']
    elif is_workday == False:
        return ['surfboard']

    
print(gear_for_day(True,False))


#solved



# * [ ] Vocab
# * [ ] Functions
# * [ ] Methods

# ## Problem decomposition

# * [ ] Input
# * [ ] Output
# * [ ] Examples
# * [ ] Conditions (if)
# * [ ] Iteration (loop)