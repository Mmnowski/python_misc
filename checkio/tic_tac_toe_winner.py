from typing import List


def checkio(game_result: List[str]) -> str:
    board_list = []
    for n in game_result:
        board_list += list(n)
    if board_list[0] == board_list[1] == board_list[2] and board_list[0] != '.':
        return board_list[0]
    elif board_list[3] == board_list[4] == board_list[5] and board_list[3] != '.':
        return board_list[3]
    elif board_list[6] == board_list[7] == board_list[8] and board_list[6] != '.':
        return board_list[6]
    elif board_list[0] == board_list[3] == board_list[6] and board_list[0] != '.':
        return board_list[0]
    elif board_list[1] == board_list[4] == board_list[7] and board_list[1] != '.':
        return board_list[1]
    elif board_list[2] == board_list[5] == board_list[8] and board_list[2] != '.':
        return board_list[2]
    elif board_list[0] == board_list[4] == board_list[8] and board_list[0] != '.':
        return board_list[0]
    elif board_list[2] == board_list[4] == board_list[6] and board_list[2] != '.':
        return board_list[2]
    else:
        return 'D'


if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "...",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
