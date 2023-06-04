from collections import deque
from itertools import permutations
from typing import Final

MORSE_MAP: Final[dict[str]] = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
}


def count_morse(morse_message: str, letters: str) -> int:
    # Convert the letters into Morse code
    letters_morse = [MORSE_MAP[letter] for letter in letters.lower()]

    # Initialize a queue with the Morse message and letters Morse
    queue = deque([(morse_message, letters_morse)])

    # Initialize the permutation count as 0
    count = 0

    while queue:
        message, codes = queue.popleft()
        # If message becomes empty and all Morse codes are used, increment the permutation count
        if not message and not codes:
            count += 1
        else:
            # Iterate over each Morse code in codes
            for i, code in enumerate(codes):
                # If message starts with code, remove the matched part from message and add the new state to the queue
                if message.startswith(code):
                    queue.append((message[len(code):], codes[:i] + codes[i+1:]))

    return count
