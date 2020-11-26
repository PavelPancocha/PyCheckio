SEPARATORS = (".", ",", " ")


def first_word(text: str, seps=SEPARATORS) -> str:
    """
        returns the first word in a given text.
    """
    for sep in seps:
        text = text.replace(sep, " ")
    text = [txt.strip() for txt in text.split()]

    return text[0]


