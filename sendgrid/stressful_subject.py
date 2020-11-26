import itertools

RED_WORDS = ("help", "asap", "urgent", )

def is_stressful(text):
    if text[-3:] == "!!!":
        return True
    # removed non-text chars
    cleaned_text = "".join(list(filter(lambda x: x.isalpha(), text)))
    # removed duplicates
    cleaned_text = "".join(val for val, g in itertools.groupby(cleaned_text))
    # Check upper
    if all(map(lambda x: x.isupper(), cleaned_text)):
        return True
    # Check red words
    for stress_word in RED_WORDS:
        if stress_word in cleaned_text.lower():
            return True
    return False


if __name__ == '__main__':
    #These "asserts" are only for self-checking and not necessarily for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed") == True, "Second"
    print('Done! Go Check it!')