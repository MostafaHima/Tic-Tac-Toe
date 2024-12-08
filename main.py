import random

# Define the game board
board = [["", "|", "", "|", ""],
         ["", "|", "", "|", ""],
         ["", "|", "", "|", ""]]

player_choices = []
computer_choices = []

def places_process(selected_column, selected_row, symbol):
    # Place the symbol in the correct position based on the column
    if selected_column == 1:
        board[selected_row - 1][0] = symbol
    elif selected_column == 2:
        board[selected_row - 1][2] = symbol
    elif selected_column == 3:
        board[selected_row - 1][4] = symbol

def generate_computer_choice():
    # Generate a random row and column for the computer
    return [random.randint(1, 3), random.randint(1, 3)]

def print_board():
    # Print the game board
    for row in board:
        print("    ".join(row))
        print("-------------------")

def check_winner():
    # Check all possible winning combinations for the player
    if (
            "11" in player_choices and "12" in player_choices and "13" in player_choices or
            "21" in player_choices and "22" in player_choices and "23" in player_choices or
            "31" in player_choices and "32" in player_choices and "33" in player_choices or
            "11" in player_choices and "22" in player_choices and "33" in player_choices or
            "31" in player_choices and "22" in player_choices and "13" in player_choices or
            "11" in player_choices and "21" in player_choices and "31" in player_choices or
            "12" in player_choices and "22" in player_choices and "32" in player_choices or
            "13" in player_choices and "23" in player_choices and "33" in player_choices):
        print("\n     You Win")
        print("     Computer Loss.")
        return True

    # Check all possible winning combinations for the computer
    if\
            "11" in computer_choices and "12" in computer_choices and "13" in computer_choices or\
            "21" in computer_choices and "22" in computer_choices and "23" in computer_choices or\
            "31" in computer_choices and "32" in computer_choices and "33" in computer_choices or\
            "11" in computer_choices and "22" in computer_choices and "33" in computer_choices or\
            "31" in computer_choices and "22" in computer_choices and "13" in computer_choices or\
            "11" in computer_choices and "21" in computer_choices and "31" in computer_choices or\
            "12" in computer_choices and "22" in computer_choices and "32" in computer_choices or\
            "13" in computer_choices and "23" in computer_choices and "33" in computer_choices:
        print("\n     You Loss")
        print("      Computer Win.")
        return True

def play():
    # Let the player choose their symbol
    while True:
        player_symbol = input("Choose a symbol (X or O): ").upper()
        if player_symbol in ["X", "O"]:
            computer_symbol = "O" if player_symbol == "X" else "X"
            break
        print("Invalid symbol. Please choose X or O.")

    # Main game loop
    while True:
        print_board()
        if check_winner():
            break

        # Ask the player to choose a position
        while True:
            user_input = input("Choose a place (row and column, e.g., 11): ")
            if len(user_input) == 2 and user_input.isdigit():
                player_selected_row = int(user_input[0])
                player_selected_column = int(user_input[1])
                if 1 <= player_selected_row <= 3 and 1 <= player_selected_column <= 3:
                    if user_input not in player_choices and user_input not in computer_choices:
                        break
                    else:
                        print("Place already taken. Choose another place.")
                else:
                    print("Invalid position. Please choose values between 1 and 3.")
            else:
                print("Invalid input. Enter two digits (e.g., 11).")

        # Update the board with the player's choice
        player_choices.append(user_input)
        places_process(player_selected_column, player_selected_row, player_symbol)

        print_board()
        if check_winner():
            break

        # Check if the game has ended
        if len(player_choices) + len(computer_choices) == 9:
            print("Game Over!")
            break

        # Let the computer choose a position
        while True:
            computer_selected = generate_computer_choice()
            computer_selected_str = f"{computer_selected[0]}{computer_selected[1]}"
            if computer_selected_str not in player_choices and computer_selected_str not in computer_choices:
                break

        # Update the board with the computer's choice
        computer_choices.append(computer_selected_str)
        computer_selected_row, computer_selected_column = computer_selected
        places_process(computer_selected_column, computer_selected_row, computer_symbol)

        print("Computer's turn:")


play()



