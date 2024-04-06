def print_board(board):
    print(f" {board['T1']} | {board['T2']} | {board['T3']} ")
    print("-----------")
    print(f" {board['M1']} | {board['M2']} | {board['M3']} ")
    print("-----------")
    print(f" {board['B1']} | {board['B2']} | {board['B3']} ")


def game_status(board, token):
    global game_in_play

    # Check if any row, column or diagonal has all values set to last token played
    if (board['T1'] == token and board['T1'] == board['T2'] and board['T2'] == board['T3']
            or (board['M1'] == token and board['M1'] == board['M2'] and board['M2'] == board['M3'])
            or (board['B1'] == token and board['B1'] == board['B2'] and board['B2'] == board['B3'])
            or (board['T1'] == token and board['T1'] == board['M1'] and board['M1'] == board['B1'])
            or (board['T2'] == token and board['T2'] == board['M2'] and board['M2'] == board['B2'])
            or (board['T3'] == token and board['T3'] == board['M3'] and board['M3'] == board['B3'])
            or (board['T1'] == token and board['T1'] == board['M2'] and board['M2'] == board['B3'])
            or (board['T3'] == token and board['T3'] == board['M2'] and board['M2'] == board['B1'])):
        print(f"{token} wins the game!!!")
        game_in_play = False


def play_game():
    global game_in_play

    # Create a dictionary to represent a 3x3 board with a space in each tile
    board_full = {
        "T1": " ",
        "T2": " ",
        "T3": " ",
        "M1": " ",
        "M2": " ",
        "M3": " ",
        "B1": " ",
        "B2": " ",
        "B3": " ",
    }

    token = 'X'
    turns = 1

    while game_in_play:

        # search the dictionary for blank values, the corresponding key is an available tile
        valid_moves = ""
        for tile, placement in board_full.items():
            if placement == " ":
                if valid_moves != "":
                    valid_moves = valid_moves + "/"
                valid_moves = valid_moves + tile

        print_board(board_full)
        print(f'Available moves are {valid_moves}')
        move = input(f'Input your move ({token} to play): ').upper()

        # Validate the input before calling the game play
        if move[:1] not in ['T', 'M', 'B'] or move[1:2] not in ['1', '2', '3']:
            print(f"Tile {move} is invalid")
        elif board_full[move] != " ":
            print(f"Tile {move} is already populated")
        else:
            board_full[move] = token
            game_status(board_full, token)

            # the token changes on each turn
            if token == 'X':
                token = 'O'
            else:
                token = 'X'

            # When 9 turns have occurred, there are no more tiles available and the game is over
            if turns == 9:
                print("Game has ended in a draw")
                game_in_play = False

            turns += 1

    # Print the final board at the end of the game
    print_board(board_full)


# Ask if the user wants to play - this is the main control loop
while input("Do you want to play a game of Tic Tac Toe? Type 'y' or 'n': ").upper() == "Y":
    game_in_play = True
    play_game()
