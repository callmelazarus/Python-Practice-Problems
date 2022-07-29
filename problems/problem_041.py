# Complete the add_csv_lines function which accepts a list
# as its only parameter. Each item in the list is a
# comma-separated string of numbers. The function should
# return a new list with each entry being the corresponding
# sum of the numbers in the comma-separated string.
#
# These kinds of strings are called CSV strings, or comma-
# sepearted values strings.
#
# Examples:
#   * input:  []
#     output: []
#   * input:  ["3", "1,9"]
#     output: [3, 10]
#   * input:  ["8,1,7", "10,10,10", "1,2,3"]
#     output:  [16, 30, 6]
#
# Look up the string split function to find out how to
# split a string into pieces.

# Write out your own pseudocode to help guide you.

def add_csv_lines(csv_lines):
    soln = []
    for item in csv_lines:
        item_into_list = item.split(",")
        rev_list = []
        for item in item_into_list:
            conv_num = int(item)
            rev_list.append(conv_num)
        summed_item = sum(rev_list)
        soln.append(summed_item)
    return soln


string= ["8,1,7", "10,10,10", "1,2,3"]
list = "10,10,10"


print(add_csv_lines(string))

# input -> lists, each item in list is a list of comma, seperated string of numbers

# create empty solution list

# loop thru each item in list

# within an item -> split the item based on "," -> creates a list of numbers

# sum the list and return to the empty solution list

# return solution list


# output -> summation of the items in the list





# solution 1 -> works only for single strings... let's use split!!!
def add_csv_lines_alt(csv_lines):
    soln = []
    for item in csv_lines:
        list_of_string = []
        for char in item:
            if char.isdigit():
                list_of_string.append(int(char))
                summed_list = sum(list_of_string)
        soln.append(summed_list)
    print(soln)





# add_csv_lines(string)


# input -> lists, each item in list is a list of comma, seperated string of numbers
    
# create empty solution list
# loop thru list
# inspect one item of the list
# find a way to add up these numbers
            # lets break this problem up more
# return that sum to the solution list

# output -> summation of the items in the list


