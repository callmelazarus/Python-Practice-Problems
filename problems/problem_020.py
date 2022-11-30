# Complete the has_quorum function to test to see if the number
# of the people in the attendees list is greater than or equal
# to 50% of the number of people in the members list.

def has_quorum(attendees_list, members_list):
    if len(attendees_list) >= len(members_list)/2: 
        return True
    return False


## Research

# * [comparing lists] Vocab
# * [ as_quorum, len()] Functions
# * [ ] Methods

# ## Problem decomposition

# * [attendees_list, members_list ] Input
# * [ True or False] Output
# * [ ] Examples
# * [ if the length of attendees >= legnth of members list / 2] Conditions (if)
# * [ ] Iteration (loop)


list1 = ["bob", "jay", "joy"]
list2 = ["mark", "fred", "joey"]

print(has_quorum(list1, list2))

# solved