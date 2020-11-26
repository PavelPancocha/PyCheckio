def double_substring(line):
    """
        length of the longest substring that non-overlapping repeats more than once.
    """
    lenghts = []
    for x in range(len(line)):
        for y in range(x+1,len(line)+1):
            if line[x:y] in line[y:]:
                lenghts.append(len(line[x:y]))
    return max(lenghts) if len(lenghts) > 0 else 0

#  https://github.com/txytju/checkio/blob/master/double-substring.py
#  https://py.checkio.org/mission/double-substring/solve/


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert double_substring('aaaa') == 2, "First"
    assert double_substring('abc') == 0, "Second"
    assert double_substring('aghtfghkofgh') == 3, "Third"
    print('"Run" is good. How is "Check"?')