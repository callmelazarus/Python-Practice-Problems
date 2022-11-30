# Complete the calculate_grade function which accepts
# a list of numerical scores each between 0 and 100.
#
# Based on the average of the scores, the function
# returns
#   * An "A" for an average greater than or equal to 90
#   * A "B" for an average greater than or equal to 80
#     and less than 90
#   * A "C" for an average greater than or equal to 70
#     and less than 80
#   * A "D" for an average greater than or equal to 60
#     and less than 70
#   * An "F" for any other average

def calculate_grade(values):
    len_list = len(values)
    list_total = 0
    for num in values:
        list_total = list_total + num
    average = list_total/len_list
    if average >=90:
        return "A"
    elif average >= 80 and average < 90:
        return "B"
    elif average >= 70 and average < 80:
        return "C"
    elif average >= 60 and average < 70:
        return "D"
    else:
        return "F"


listy = [1,3,5,2,3,5,8,232,12,23,4,24]

list2 = [80, 90, 82]

list3 = [92, 82, 92,99]

print(calculate_grade(listy))
print(calculate_grade(list2))
print(calculate_grade(list3))

#solved


#pc
# accepts list of numerical scores
# functions a letter based on the average of the scores