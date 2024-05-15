import os
import math
import random


# Function to draw the Tic Tac Toe board
def draw_board(spots):
    # Construct the string representation of the board using f-strings
    board = (
        f"|{spots[1]}|{spots[2]}|{spots[3]}|{' '*5}|1|2|3|\n"  # First row
        f"|{spots[4]}|{spots[5]}|{spots[6]}|{' '*5}|4|5|6|\n"  # Second row
        f"|{spots[7]}|{spots[8]}|{spots[9]}|{' '*5}|7|8|9|"  # Third row
    )
    # Print the board
    print(board)


# Function to check for a win condition
def check_win(spots, player):
    # Define all possible winning combinations
    win_combinations = [
        # Horizontal
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        # Vertical
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        # Diagonal
        [1, 5, 9],
        [3, 5, 7],
    ]
    # Check if any winning combination is found
    for combo in win_combinations:
        if all(spots[pos] == player for pos in combo):
            return True
    return False


# Function to check if the board is full
def is_board_full(spots):
    return all(spot in {"X", "O"} for spot in spots.values())


# Function to evaluate the score of the board for the AI player ('X')
def evaluate(spots):
    if check_win(spots, "X"):
        return 1
    elif check_win(spots, "O"):
        return -1
    else:
        return 0


# Minimax algorithm
def minimax(spots, depth, is_maximizing):
    if is_board_full(spots) or depth == 0:
        return evaluate(spots)

    if is_maximizing:
        max_eval = -math.inf
        for spot in spots:
            if spots[spot] not in {"X", "O"}:
                spots[spot] = "X"
                eval = minimax(spots, depth - 1, False)
                spots[spot] = ""
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for spot in spots:
            if spots[spot] not in {"X", "O"}:
                spots[spot] = "O"
                eval = minimax(spots, depth - 1, True)
                spots[spot] = ""
                min_eval = min(min_eval, eval)
        return min_eval


# Function to get the AI's move
def get_ai_move(spots):
    best_score = -math.inf
    best_move = None
    for spot in spots:
        if spots[spot] not in {"X", "O"}:
            spots[spot] = "X"
            score = minimax(
                spots, 5, False
            )  # Adjust the depth for desired AI difficulty
            spots[spot] = ""
            if score > best_score:
                best_score = score
                best_move = spot
    return best_move


# Dictionary representing the initial state of the Tic Tac Toe board
spots = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}

# Call the draw_board function to print the initial state of the board
draw_board(spots)

playing = True
turn = 0

while playing:
    # Reset the screen
    os.system("cls" if os.name == "nt" else "clear")
    # Check whose turn it is
    if turn % 2 == 0:
        # Player's turn
        draw_board(spots)
        choice = input("Enter a number from 1-9 to place your mark (or 'q' to quit): ")
        if choice == "q":
            playing = False
        elif (
            str.isdigit(choice)
            and int(choice) in spots
            and spots[int(choice)] not in {"X", "O"}
        ):
            spots[int(choice)] = "O"
            turn += 1
    else:
        # AI's turn
        ai_move = get_ai_move(spots)
        spots[ai_move] = "X"
        turn += 1

    # Check for win or draw
    if check_win(spots, "X"):
        os.system("cls" if os.name == "nt" else "clear")
        draw_board(spots)
        print("AI wins!")
        playing = False
    elif check_win(spots, "O"):
        os.system("cls" if os.name == "nt" else "clear")
        draw_board(spots)
        print("Player wins!")
        playing = False
    elif is_board_full(spots):
        os.system("cls" if os.name == "nt" else "clear")
        draw_board(spots)
        print("It's a draw!")
        playing = False
