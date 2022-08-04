# Write a function that meets these requirements.
#
# Name:       count_word_frequencies
# Parameters: sentence, a string
# Returns:    a dictionary whose keys are the words in the
#             sentence and their values are the number of
#             times that word has appeared in the sentence
#
# The sentence will contain now punctuation.
#
# This is "case sensitive". That means the word "Table" and "table"
# are considered different words.
#
# Examples:
#    * sentence: "I came I saw I learned"
#      result:   {"I": 3, "came": 1, "saw": 1, "learned": 1}
#    * sentence: "Hello Hello Hello"
#      result:   {"Hello": 3}

## FUNCTION PSEUDOCODE
# function count_word_frequencies(sentence):
    # words = split the sentence
    # counts = new empty dictionary
    # for each word in words
        # if the word is not in counts
            # counts[word] = 0
        # add one to counts[word]
    # return counts

def count_word_frequencies(sentence):
    words = sentence.split() # turns sentence into list, of individual words
    counts = {}
    for word in words:
        if counts.get(word) == None: # if the word doesn't existin the dictionary....
            counts[word] = 0 # adds that key to teh dictionary, and sets value to 0
        counts[word] += 1 # how do I add to the value, of k/v pair
    return counts

sentence="I came I saw I learned"

print(count_word_frequencies(sentence))


emptdic = {
    "test":"value1",
 "test": "value2"
 }

# print(emptdic.get("test"))

print(emptdic)