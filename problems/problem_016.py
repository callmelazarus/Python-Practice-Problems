# Complete the is_inside_bounds function which takes an x
# coordinate and a y coordinate, and then tests each to
# make sure they're between 0 and 10, inclusive.
# Planning

## Research

# * [ x, y coords] Vocab
# * [ is_inside_bounds] Functions
# * [ ] Methods

# ## Problem decomposition

# * [ x, y] Input
# * [ True or False] Output
# * [ ] Examples
# * [ if 0 => x <= 10 and 0 => y <= 10] Conditions (if)
# * [ ] Iteration (loop)

def is_inside_bounds(x, y):
    if x >= 0 and x <= 10:
        if y >= 0 and y <= 10:
            return True
    return False

x= -1
y=10
print(is_inside_bounds(x,y))