board = list(range(1, 10))


def draw_board(board):
    for i in range(3):
        print(board[i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3])
        if i != 2:
            print("---------")


def inp(player):
    while True:
        player_resp = input(f"Choose number, clown, {player} ")
        try:
            player_resp = int(player_resp)
        except:
            print("Incorrect number")
            continue
        if player_resp >= 1 and player_resp <= 9:
            if (str(board[player_resp - 1])) not in "XO":
                board[player_resp - 1] = player
                break
            else:
                print("Cell is already busy")
        else:
            print("Choose number from 1 to 9")


def if_win(board):
    win_condition = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    for j in win_condition:
        if board[j[0]] == board[j[1]] == board[j[2]]:
            print(board[j[0]], board[j[1]], board[j[2]])
            return f"Win of {board[j[0]]}"
    return False


def main(board):
    count = 0
    while True:
        draw_board(board)
        if count % 2 == 0:
            inp("X")
        else:
            inp("O")
        count += 1
        if count > 4:
            tmp = if_win(board)
            if tmp:
                print(tmp, "win")
                break
        if count == 9:
            print("draw")
            break
    draw_board(board)


if __name__ == "__main__":
    main(board)