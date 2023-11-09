def stutterFFormat(word):
    stutter_string = "%s...%s...%s." % (word[0:2], word[0:2], word)
    return stutter_string

def stutterStrFormat(word):
    stutter_string_two = "{}...{}...{}.".format(word[0:2], word[0:2], word)
    return stutter_string_two

word = input("Type a word:\n")
print(stutterFFormat(word))
print(stutterStrFormat(word))
