import re


def is_stressful(subj):
    """
        recoognise stressful subject
    """
    triggers = ["help", "asap", "urgent"]
    for letter in subj[-3::-1]:
        if letter != '!':
            break
        return True
    subj = re.sub(r'[^\w\s]', '', subj)
    if subj.strip(' ').isupper():
        return True
    words = subj.lower().split(' ')
    print(words)
    for word in words:
        clean_word = word[0]
        for n in range(1, len(word)):
            if word[n-1] != word[n]:
                clean_word += word[n]
        for trigger in triggers:
            if trigger == clean_word:
                return True
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") is False, "First"
    assert is_stressful("I neeed HELP") is True, "Second"
    assert is_stressful("h!e!l!p") is True, "Third"
    print('Done! Go Check it!')
