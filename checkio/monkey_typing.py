import re


def count_words(text, word_list):
    wordcount = 0
    words = text.lower().split(' ')
    for n in range(len(words)):
        words[n] = re.sub("[^a-zA-Z]", "", words[n])
    print(words)
    for n in range(len(words)):
        for word in word_list:
            if words[n].find(word) != -1:
                wordcount += 1
                print(words[n])
                words[n] = words[n].split(word, 1)[1]
                print(words[n])
    print(wordcount)
    return wordcount


print(count_words("Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.",
                  {"far", "word", "vokal", "count", "tries"}) == 5)


# dziala poprawnie dla kazdego przypadku poza nazwami wlasnymi (chyba, zadanie nie tlumaczylo wystarczajaco zeby stwierdzic czy to w tym lezy problem
