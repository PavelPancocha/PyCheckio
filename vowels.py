

def translate(phrase):
    word = ""
    counter = 0  # letters from last addition
    last_was_vowel = False
    for letter in phrase:
        if counter == 0:
            word += letter
            counter = 2
            last_was_vowel = True if letter in VOWELS else False
        elif 1 < counter <= 3:
            if last_was_vowel:
                counter += 1
            else:
                counter = 1
        elif letter == " ":
            word += letter
            counter = 1
        else:
            word += letter
            counter = 2
            last_was_vowel = True if letter in VOWELS else False
    return word


if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
