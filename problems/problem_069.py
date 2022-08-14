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
# There is pseudocode for you to guide you.


# class Student
    # method initializer with required state "name"
        # self.name = name
        # self.scores = [] because its an internal state

    # method add_score(self, score)
        # appends the score value to self.scores

    # method get_average(self)
        # if there are no scores in self.scores
            # return None
        # returns the sum of the scores divided by
        # the number of scores

"""
class methods practice 
SOLVED 8/8/2022

LESSON: 
attritbutes don't need to be taken in from the argument....
these attributes can then be used as parameters for methods within a lass
"""

class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)
    
    def get_average(self): 
        if self.scores == []:
            return None
        else:
            return sum(self.scores)/len(self.scores)

Joe = Student("Joe")

Joe.add_score(80)
Joe.add_score(90)
Joe.add_score(75)
Joe.add_score(100)
Joe.add_score(95)

print(Joe.get_average()) # returns 88

Ray = Student("Ray")

Ray.add_score(90)

print(Ray.get_average()) # returns 90


    # student.add_score(90)
#    student.add_score(82)
#    print(student.get_average())    # Prints 84
#