# Complete the calculate_average function which accepts
# a list of numerical values and returns the average of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#
# Pseudocode is available for you

def calculate_average(values):
    if values == []:
        return None
    
    len_list = len(values)
    list_total = 0
    for num in values:
        list_total = list_total + num
    average = list_total/len_list
    
    return average
    


# pc
# accepts list of numbers
# returns average
# if list is empty -> return none

listy = [1,3,5,2,3,5,8,232,12,23,4,24]

list2 = []

list3 = [10,10,10,10]

print(calculate_average(listy))
print(calculate_average(list2))
print(calculate_average(list3))

# solved