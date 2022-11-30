# Write a class that meets these requirements.
#
# Name:       Student
#
# Required state:
#    * name, a string
#
# Behavior:
#    * add_score(score)   # Adds a score to their list of scores
#    * get_average()      # Gets the average of the student's scores
#
# Example:
#    student = Student("Malik")
#
#    print(student.get_average())    # Prints None
#    student.add_score(80)
#    print(student.get_average())    # Prints 80
#    student.add_score(90)
#    student.add_score(82)
#    print(student.get_average())    # Prints 84
#
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.

"""
An attribute/state is not required to be an argument. You can use this attribute in other
parts of the class

SOLVED - 8/13/2022

LESSON:
(same as above) An attribute/state is not required to be an argument. You can use this attribute in other
parts of the class
"""


class Student:
    def __init__(self, name):
        self.name = name
        self.scores = [] # you can create this attribute without receiving an argument

    def add_score(self, score):
        # adds a score to their list of scores
        self.scores.append(score)

    def get_average(self):
        # average is the total scores / number of scores
        # summation of items in list / len(scores)
        # how do I bring in a variable from another funciton?
        if self.scores == []:
            return None
        average = sum(self.scores)/len(self.scores)
        return average


Joe = Student("Joe")

Joe.add_score(80)
Joe.add_score(90)
Joe.add_score(75)
Joe.add_score(100)
Joe.add_score(95)

print(Joe.get_average()) # returns 88
