#  https://py.checkio.org/cs/mission/pawn-brotherhood/
#  https://py.checkio.org/mission/pawn-brotherhood/solve/


def safe_pawns(pawns: set) -> int:
    pawns_index = set()
    for p in pawns:
        col, row = ord(p[0]) - 96, int(p[1])
        pawns_index.add((row, col))

    safe_pawns_count = 0
    for row, col in pawns_index:
        is_safe = True if ((row - 1, col - 1) in pawns_index) or ((row - 1, col + 1) in pawns_index) else False
        if is_safe:
            safe_pawns_count += 1
    return safe_pawns_count


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")