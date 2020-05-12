from nltk import FreqDist

# Given string of text, return a list of tuples like
# [('text', 2), ('Here', 1), ('is', 1), ('some', 1)...]
def distfreq(s):
    return list(FreqDist(s.split()).most_common())

