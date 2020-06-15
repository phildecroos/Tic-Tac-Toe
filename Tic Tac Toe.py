import time

board = [
    "",
    "[ ]", "[ ]", "[ ]",
    "[ ]", "[ ]", "[ ]",
    "[ ]", "[ ]", "[ ]"
]


def show_board():
    print(board[1] + board[2] + board[3])
    print(board[4] + board[5] + board[6])
    print(board[7] + board[8] + board[9])


test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def good_input(possible_input):
    if possible_input in test_list:
        return True
    else:
        return False


def is_available(input_num):
    if board[input_num] == "[ ]":
        return True
    else:
        return False


def ai_square():
    '''
    This isn't the best algorithm, and it definitely could've been shortened with loops and/or recursion, but it will
    at least tie the player unless they are actually good.

    HOW THE ALGORITHM WORKS
    The algorithm starts by looking at each square on the board and picking the first one it comes across that will win
    the game for the computer, if there are none, it does the same thing but with squares that will block the player
    from winning in the next turn.
    If neither of those conditions are met it resets the board_scores list to a score of 0 for each square, and it
    analyzes every possibly combination of moves that is left in the game, allotting 1 point to each square that is the
    winning move for the computer.
    I tried allocating different amounts of points based on who won in that scenario and how many moves it took, but an
    equal amount of points for every scenario seemed to work best.
    From my testing, I have only found three combinations of moves that beat this algorithm.
    '''
    for x in range(1, len(board)):
        if board[x] == "[ ]":
            board[x] = "[O]"
            if won("O"):
                board[x] = "[ ]"
                return int(x)
            board[x] = "[ ]"
    for x in range(1, len(board)):
        if board[x] == "[ ]":
            board[x] = "[X]"
            if won("X"):
                board[x] = "[ ]"
                return int(x)
            board[x] = "[ ]"
    board_scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in range(1, len(board)):
        if board[x] == "[ ]":
            board[x] = "[O]"
            for y in range(1, len(board)):
                if board[y] == "[ ]":
                    board[y] = "[O]"
                    if won("O"):
                        board_scores[x] += 1
                    board[y] = "[X]"
                    for z in range(1, len(board)):
                        if board[z] == "[ ]":
                            board[z] = "[O]"
                            if won("O"):
                                board_scores[x] += 1
                            for a in range(1, len(board)):
                                if board[a] == "[ ]":
                                    board[a] = "[O]"
                                    if won("O"):
                                        board_scores[x] += 1
                                    board[a] = "[X]"
                                    for b in range(1, len(board)):
                                        if board[b] == "[ ]":
                                            board[b] = "[O]"
                                            if won("O"):
                                                board_scores[x] += 1
                                            for c in range(1, len(board)):
                                                if board[c] == "[ ]":
                                                    board[c] = "[O]"
                                                    if won("O"):
                                                        board_scores[x] += 1
                                                    board[c] = "[X]"
                                                    for d in range(1, len(board)):
                                                        if board[d] == "[ ]":
                                                            board[d] = "[O]"
                                                            if won("O"):
                                                                board_scores[x] += 1
                                                            for e in range(1, len(board)):
                                                                if board[e] == "[ ]":
                                                                    board[e] = "[O]"
                                                                    if won("O"):
                                                                        board_scores[x] += 1
                                                                    board[e] = "[ ]"
                                                            board[d] = "[ ]"
                                                    board[c] = "[ ]"
                                            board[b] = "[ ]"
                                    board[a] = "[ ]"
                            board[z] = "[ ]"
                    board[y] = "[ ]"
            board[x] = "[ ]"
    return board_scores.index(max(board_scores))


def claim_square(cell, player):
    board[cell] = "[" + player + "]"


def is_tie():
    empty = 0
    for x in range(1, len(board)):
        if board[x] == "[ ]":
            empty += 1
    if empty == 0:
        return True
    else:
        return False


def won(player):
    if board[1] == ("[" + player + "]") and board[5] == ("[" + player + "]") and board[9] == ("[" + player + "]"):
        return True
    if board[3] == ("[" + player +"]") and board[5] == ("[" + player + "]") and board[7] == ("[" + player + "]"):
        return True
    if board[1] == ("[" + player + "]") and board[4] == ("[" + player + "]") and board[7] == ("[" + player + "]"):
        return True
    if board[2] == ("[" + player + "]") and board[5] == ("[" + player + "]") and board[8] == ("[" + player + "]"):
        return True
    if board[3] == ("[" + player + "]") and board[6] == ("[" + player + "]") and board[9] == ("[" + player + "]"):
        return True
    if board[1] == ("[" + player + "]") and board[2] == ("[" + player + "]") and board[3] == ("[" + player + "]"):
        return True
    if board[4] == ("[" + player + "]") and board[5] == ("[" + player + "]") and board[6] == ("[" + player + "]"):
        return True
    if board[7] == ("[" + player + "]") and board[8] == ("[" + player + "]") and board[9] == ("[" + player + "]"):
        return True


show_board()
print("The squares in the board are numbered from 1 to 9 from top left to bottom right.")
print("To do a move, just type the number of the square you want to put an X on.")
recent_move = 0

while True:
    user_input = int(input("Your move..."))
    if good_input(user_input):
        if is_available(user_input):
            claim_square(user_input, "X")
            recent_move = user_input
            show_board()
            if won("X"):
                print("You win!")
                break
            if is_tie():
                print("It's a tie!")
                break
            print("Computer's move...")
            time.sleep(1)
            claim_square(ai_square(), "O")
            show_board()
            if won("O"):
                print("The computer wins!")
                break
        else:
            print("That square is already taken. Please choose a different one.")
    else:
        print("Invalid input. Please input a 1 digit number that corresponds to a square on the board.")