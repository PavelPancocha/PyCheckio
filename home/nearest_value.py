"""
https://py.checkio.org/en/mission/nearest-value/
"""


def nearest_value(values: set[int], value: int) -> int:
    """
    Return the nearest value to value from values.
    If two values are equidistant, return the smaller value.
    """
    if value in values:
        return value
    return min(values, key=lambda x: (abs(x - value), x))
