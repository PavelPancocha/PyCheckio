from enum import Enum
from itertools import pairwise


class Direction(Enum):
    UP = 1
    DOWN = 2

def changing_direction(elements: list[int]) -> int:
    changes: int = 0
    direction: Direction | None = None

    for prev_element, current_element in pairwise(elements):
        if current_element == prev_element:
            continue

        current_direction: Direction = Direction.UP if current_element > prev_element else Direction.DOWN

        if direction and direction is not current_direction:
            changes += 1

        direction = current_direction

    return changes
