from typing import Final, Iterable

DONUT: Final = 0


def duplicate_zeros(donuts: list[int]) -> Iterable[int]:
    # your code here
    return [result for something in donuts for result in ([DONUT, DONUT] if something == DONUT else [something])]


assert list(duplicate_zeros([100, 10, 0, 101, 1000])) == [100, 10, 0, 0, 101, 1000]
