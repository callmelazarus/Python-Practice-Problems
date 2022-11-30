# Write a function that meets these requirements.
#
# Name:       basic_calculator
# Parameters: left, the left number
#             op, the math operation to perform
#             right, the right number
# Returns:    the result of the math operation
#             between left and right
#
# The op parameter can be one of four values:
#   * "+" for addition
#   * "-" for subtraction
#   * "*" for multiplication
#   * "/" for division
#
# Examples:
#     * inputs:  10, "+", 12
#       result:  22
#     * inputs:  10, "-", 12
#       result:  -2
#     * inputs:  10, "*", 12
#       result:  120
#     * inputs:  10, "/", 12
#       result:  0.8333333333333334
"""
calculator function -> 

inputs -> number, operator, number

challenge is turning the operator to the operation

returns -> result of operation

SOLVED 8/6/2022

"""


def basic_calculator(num1, operator, num2):
    add = lambda num1, num2: num1 + num2
    minus = lambda num1, num2: num1 - num2
    multiply = lambda num1, num2: num1 * num2
    divide = lambda num1, num2: num1 / num2
    if operator == "+":
        return add(num1,num2)
    elif operator == "-":
        return minus(num1,num2)
    elif operator == "*":
        return multiply(num1,num2)
    elif operator == "/":
        return divide(num1,num2)
    else:
        return "I can't deal with that operator"

print(basic_calculator(2,"+",2))