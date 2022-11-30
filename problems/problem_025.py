# Complete the calculate_sum function which accepts
# a list of numerical values and returns the sum of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#

def calculate_sum(values):
    if values == []:
        return None
    list_total = 0
    for num in values:
        list_total = list_total + num
    
    return list_total
    


# pc
# accepts list of numbers
# returns average
# if list is empty -> return none

listy = [1,3,5,2,3,5,8,232,12,23,4,24]

list2 = []

list3 = [10,10,10,10]

print(calculate_sum(listy))
print(calculate_sum(list2))
print(calculate_sum(list3))

#solved