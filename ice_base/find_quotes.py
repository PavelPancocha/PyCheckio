"""
https://py.checkio.org/en/mission/find-quotes/
"""

from typing import Final, Iterable

QUOTE_CHAR: Final[str] = '"'


def find_quotes(input_string: str) -> list[str]:
    """
    Return a list of strings that are enclosed in double quotes.
    Note: Regular expression not used on purpose.
    """
    quotes_locations: Iterable[int] = (i for i, char in enumerate(input_string) if char == QUOTE_CHAR)
    quote_pairs: list[tuple[int, int]] = list(zip(quotes_locations, quotes_locations))
    quoted_parts: list[str] = [input_string[start + 1 : end] for start, end in quote_pairs]
    return quoted_parts
