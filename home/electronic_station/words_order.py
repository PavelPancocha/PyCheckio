def words_order(text: str, words: list) -> bool:
    if len(words) != len(set(words)):
        # There are duplicate words in the list, so return False
        return False
    search_position = 0
    split_text = text.split()
    for word in words:
        # Check if the word is in the text starting from search_pos
        remaining_text = split_text[search_position:]
        if word not in remaining_text:
            # The word was not found in the text, so return False
            return False
        search_position = split_text.index(word, search_position)

    return True
