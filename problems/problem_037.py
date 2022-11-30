# Complete the pad_left function which takes three parameters
#   * a number
#   * the number of characters in the result
#   * a padding character
# and turns the number into a string of the desired length
# by adding the padding character to the left of it
#
# Examples:
#   * number: 10
#     length: 4
#     pad:    "*"
#     result: "**10"
#   * number: 10
#     length: 5
#     pad:    "0"
#     result: "00010"
#   * number: 1000
#     length: 3
#     pad:    "0"
#     result: "1000"
#   * number: 19
#     length: 5
#     pad:    " "
#     result: "   19"

def pad_left(number, length, pad):
    if length < len(str(number)):
        return "update your length, it is too short. It needs to be equal or greater than the length of your number"
    else:
        num_pad = length - len(str(number))
        pad_string = num_pad*pad
        final_string = pad_string + str(number)
    return final_string


number = 10

length = 1

pad = " "

# print(len(str(number)))

print(pad_left(number, length, pad))

# input -> number, how long the end string will be (must be greater than number before I suppose), the type of padding on the left

# number of pad = total length - length of number

# add pads * number of pad

# add trailing number

# output -> string with padding, the number -> with a total length specified
