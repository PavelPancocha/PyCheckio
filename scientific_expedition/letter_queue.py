from collections import deque
from enum import Enum
from typing import List


class Actions(Enum):
    PUSH = 'PUSH'
    POP = 'POP'


def letter_queue(commands: List[str]) -> str:
    # your code here
    queue: deque = deque()
    for action, *letters in (command.split() for command in commands):
        if Actions(action) is Actions.PUSH:
            queue.extend(letters)
        elif queue:
            queue.popleft()
    return ''.join(queue)


if __name__ == '__main__':
    print("Example:")
    print(
        letter_queue(
            ['PUSH A',
             'POP',
             'POP',
             'PUSH Z',
             'PUSH D',
             'PUSH O',
             'POP',
             'PUSH T']
            )
        )

    # These "asserts" are used for self-checking and not for an auto-testing
    assert letter_queue(
        ['PUSH A',
         'POP',
         'POP',
         'PUSH Z',
         'PUSH D',
         'PUSH O',
         'POP',
         'PUSH T']
        ) == 'DOT'
    assert letter_queue(['POP', 'POP']) == ''
    assert letter_queue(['PUSH H', 'PUSH I']) == 'HI'
    assert letter_queue([]) == ''
    print("Coding complete? Click 'Check' to earn cool rewards!")
