from nltk import FreqDist

# Given string of text, return frequency distributions of all the words,
# with the most common first 
# Returns a list of dicts like
# [{'text': 2}, {'Here': 1}, {'is': 1}, {'some': 1}...]
def distfreq(s):
    mcommon = FreqDist(s.split()).most_common()
    return list(map(lambda x : {x[0]: x[1]}, mcommon))

