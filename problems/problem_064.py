# Write a function that meets these requirements.
#
# Name:       temperature_differences
# Parameters: highs: a list of daily high temperatures
#             lows: a list of daily low temperatures
# Returns:    a new list containing the difference
#             between each high and low temperature
#
# The two lists will be the same length
#
# Example:
#     * inputs:  highs: [80, 81, 75, 80]
#                lows:  [72, 78, 70, 70]
#       result:         [ 8,  3,  5, 10]


"""
highs - list of daily high temps
lows - list of daily low temps

returns -> new list containing the differences between the highs and lows

Lesson: 
like to use the loop with range, to be able to loop thru the same index each time
This can be adjusted to loop thru similar index's

SOLVED: 8/8/2022
"""

def temperature_differences(highs, lows):
    soln = []
    for i in range(len(highs)):
        soln.append(highs[i]-lows[i])
    return soln