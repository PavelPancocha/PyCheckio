def goes_after(word: str, first: str, second: str) -> bool:
    first_occurrence_index = word.find(first)
    second_occurrence_index = word.find(second)
    if first_occurrence_index == -1 or second_occurrence_index == -1:
        return False
    if first_occurrence_index == second_occurrence_index:
        return False
    if first_occurrence_index > second_occurrence_index:
        return False
    if first_occurrence_index + 1 != second_occurrence_index:
        return False
    return True
