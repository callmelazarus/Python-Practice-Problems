# Complete the is_inside_bounds function which has the
# following parameters:
#   x: the x coordinate to check
#   y: the y coordinate to check
#   rect_x: The left of a rectangle
#   rect_y: The top of a rectangle
#   rect_width: The width of the rectangle
#   rect_height: The height of the rectangle
#
# The is_inside_bounds function returns true if all of
# the following are true
#   * x is greater than or equal to rect_x
#   * y is greater than or equal to rect_y
#   * x is less than or equal to rect_x + rect_width
#   * y is less than or equal to rect_y + rect_height

def is_inside_bounds(x, y, rect_x, rect_y, rect_width, rect_height):
    if x >= rect_x and y >= rect_y:
        if x <= rect_x + rect_width and y <= rect_y + rect_height:
            return True
    return False

print(is_inside_bounds(1, 1, 1, 1, 1, 1))

# * [ operators ] Vocab
# * [ is_inside_bounds] Functions
# * [ ] Methods

# ## Problem decomposition

# * [ x, y, rect_x, rect_y, rect_width, rect_height] Input
# * [ True / False  -> if 4 things are checked as True] Output
# * [ ] Examples
# * [ yes ] Conditions (if)
# * [ probably not ] Iteration (loop)


