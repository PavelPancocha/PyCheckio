def checkio(first, second):
    first = set(first.split(","))
    second = set(second.split(","))
    result = list(first.intersection(second))
    result.sort()
    return ",".join(result)


# These "asserts" using only for self-checking and not necessary for auto-testing

if __name__ == '__main__':
    print(checkio("one,two,three", "four,five,one,two,six,three"))
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
