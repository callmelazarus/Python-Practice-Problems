# Complete the make_sentences function that accepts three
# lists.
#   * subjects contains a list of subjects for three-word sentences
#   * verbs contains a list of verbs for three-word sentences
#   * objects contains a list of objects for three-word sentences
# The make_sentences function should return all possible sentences
# that can be made from the words in each list
#
# Examples:
#   * subjects: ["I"]
#     verbs:    ["play"]
#     objects:  ["Portal"]
#     returns:  ["I play Portal"]
#   * subjects: ["I", "You"]
#     verbs:    ["play"]
#     objects:  ["Portal", "Sable"]
#     returns:  ["I play Portal", "I play Sable",
#                "You play Portal", "You play Sable"]
#   * subjects: ["I", "You"]
#     verbs:    ["play", "watch"]
#     objects:  ["Portal", "Sable"]
#     returns:  ["I play Portal", "I play Sable",
#                "I watch Portal", "I watch Sable",
#                "You play Portal", "You play Sable"
#                "You watch Portal", "You watch Sable"]
#
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.

def make_sentences(subjects, verbs, objects):
    total_string = []
    for subject in subjects:
        for verb in verbs:
            for thing in objects:
                string = subject + " " + verb + " " + thing
                total_string.append(string)
    return total_string

subjects= ["I", "You"]
verbs=    ["play", "watch"]
objects=  ["Portal", "Sable"]

print(make_sentences(subjects, verbs, objects))

# input - 3 lists

# need to be systemeatic about this

# solution list -> holds all the string cobminations

# stay fixed on the first two indexes, and than loop thru third

# fix the first index, step the 2nd index, and loop thru third

# step the first index, start with the first index, loop thru third

# keep the stepped first index, step the 2nd index, loop the third


# output - lists that combine all iterations of three lists