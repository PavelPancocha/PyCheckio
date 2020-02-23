
def checkio(game_result) -> str:
    def check_if_win(line):
        return True if (line[0] == line[1] == line[2] and "." not in line) else False
    for line in game_result:  # check lines
        if check_if_win(line):
            return line[0]
    for column in zip(*game_result):  # check columns - just rotated
        if check_if_win(column):
            return column[0]
    if check_if_win([game_result[0][0], game_result[1][1], game_result[2][2]]) or check_if_win([game_result[0][2], game_result[1][1], game_result[2][0]]):
        return game_result[1][1]
    return "D"


print(checkio(["OO.",
         "XOX",
         "XOX"]))