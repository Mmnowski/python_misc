import re


def checkio(phrase):
    phrase = re.sub("[^a-zA-Z]", "", phrase)
    occurences = {}
    for n in phrase.lower():
        if occurences.get(n):
            occurences[n] += 1
        else:
            occurences[n] = 1
    occurences = dict(sorted(occurences.items()))
    max_key = max(occurences.keys(), key=(lambda k: occurences[k]))
    return max_key


print(checkio("Hello World!") == "l")
print(checkio("How do you do?") == "o")
print(checkio("12345,12345,12345 S 12345,12345"))
# checkio("Oops!") == "o"
# checkio("AAaooo!!!!") == "a"
# checkio("abe") == "a"
