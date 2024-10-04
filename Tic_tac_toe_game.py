import random

dashboard = [" "] * 9  # Simplify initialization of the dashboard
game_on = True
winner = None
player = "X"

# Emoji for players
PLAYER_X_EMOJI = "❌"
PLAYER_O_EMOJI = "⭕"


# function for display dashboard with emojis....
def display_dashboard():
    board = [PLAYER_X_EMOJI if cell == 'X' else PLAYER_O_EMOJI if cell == 'O' else ' ' for cell in dashboard]
    print("\n")
    print(f"\t {board[0]} | {board[1]} | {board[2]}")
    print("\t-----------")
    print(f"\t {board[3]} | {board[4]} | {board[5]}")
    print("\t-----------")
    print(f"\t {board[6]} | {board[7]} | {board[8]}")
    print("\n")


# Input validation
def get_valid_position(player):
    while True:
        pos = input(f"{player} ➡️  Choose a position from 1 to 9: ")
        if pos.isdigit() and 1 <= int(pos) <= 9:
            pos = int(pos) - 1
            if dashboard[pos] == " ":
                return pos
            else:
                print("❗ This position is already taken. Try another one.")
        else:
            print("❗ Invalid input. Please enter a number between 1 and 9.")


# function for players' turn
def players_turn(player, player1, player2):
    if player == "X":
        print(f"{player1} {PLAYER_X_EMOJI} now it's your turn.")
    else:
        print(f"{player2} {PLAYER_O_EMOJI} now it's your turn.")
    pos = get_valid_position(player)
    dashboard[pos] = player
    display_dashboard()


# function for normal computer turn
def normal_computer_turn(player, player1, player2):
    if player == "X":
        pos = gen_random_index()
        print(f"\n{PLAYER_X_EMOJI} {player1} chose position {pos + 1}.")
    else:
        print(f"{player2} {PLAYER_O_EMOJI} now it's your turn.")
        pos = get_valid_position(player)
    dashboard[pos] = player
    display_dashboard()


# function for generating random index of computer turn
def gen_random_index():
    pos = random.randint(0, 8)
    while dashboard[pos] != " ":
        pos = random.randint(0, 8)
    return pos


# Combined function to check rows, columns, and diagonals
def check_for_winner():
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)  # Diagonals
    ]
    for a, b, c in win_conditions:
        if dashboard[a] == dashboard[b] == dashboard[c] != " ":
            return dashboard[a]  # Return the winner ('X' or 'O')
    return None


def check_game_status():
    global game_on, winner
    winner = check_for_winner()
    if winner:
        game_on = False
    elif " " not in dashboard:
        game_on = False  # It's a tie


def switch_player():
    global player
    player = "O" if player == "X" else "X"


def reset_game():
    global dashboard, game_on, winner, player
    dashboard = [" "] * 9
    game_on = True
    winner = None
    player = "X"
    display_dashboard()


# function to handle play with players
def play_with_players():
    player1 = input("\nEnter Player1's Name: ")
    player2 = input("Enter Player2's Name: ")

    if player1.isalpha() and player2.isalpha():
        reset_game()
        while game_on:
            players_turn(player, player1, player2)
            check_game_status()
            if not game_on:
                break
            switch_player()

        if winner == "X":
            print(f"🎉 Congrats {player1} {PLAYER_X_EMOJI}, you won the game!")
        elif winner == "O":
            print(f"🎉 Congrats {player2} {PLAYER_O_EMOJI}, you won the game!")
        else:
            print("🤝 It's a tie! Better luck next time!")
    else:
        print("❗ Please enter valid alphabetic names.")
        play_with_players()


# function to handle play with normal computer
def play_with_normal_computer():
    player1 = "Normal_Computer"
    player2 = input("\nEnter Player2's Name: ")

    if player2.isalpha():
        reset_game()
        while game_on:
            if player == "X":
                normal_computer_turn(player, player1, player2)
            else:
                players_turn(player, player1, player2)
            check_game_status()
            if not game_on:
                break
            switch_player()

        if winner == "X":
            print(f"🎉 {player1} {PLAYER_X_EMOJI} won the game!")
        elif winner == "O":
            print(f"🎉 Congrats {player2} {PLAYER_O_EMOJI}, you won the game!")
        else:
            print("🤝 It's a tie!")
    else:
        print("❗ Please enter valid alphabetic names.")
        play_with_normal_computer()


# Smart Computer using Minimax Algorithm
def minimax(board, is_maximizing):
    scores = {'X': 1, 'O': -1, 'tie': 0}
    result = check_for_winner()

    if result == "X":
        return scores['X']
    elif result == "O":
        return scores['O']
    elif " " not in board:
        return scores['tie']  # It's a tie

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, False)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score


def smart_computer_turn():
    best_score = -float('inf')
    best_move = None
    for i in range(9):
        if dashboard[i] == " ":
            dashboard[i] = "X"
            score = minimax(dashboard, False)
            dashboard[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    dashboard[best_move] = "X"
    print(f"Smart Computer {PLAYER_X_EMOJI} chose position {best_move + 1}.")
    display_dashboard()


# function to handle play with smart computer
def play_with_smart_computer():
    reset_game()
    while True:
        player2 = input("Enter Player name: ")
        if player2.isalpha():
            break
        else:
            print("Player name must be alphabet only!")

    choice = input(
        "\nWho goes first? Smart Computer or Player\nEnter 'C' for Smart Computer and 'P' for Player: ").upper()
    if choice == 'C':
        while game_on:
            smart_computer_turn()
            check_game_status()
            if not game_on:
                break
            players_turn("O", "Smart Computer", player2)
            check_game_status()
    elif choice == 'P':
        while game_on:
            players_turn("O", "Smart Computer", player2)
            check_game_status()
            if not game_on:
                break
            smart_computer_turn()
            check_game_status()
    else:
        print("❗ Invalid choice. Please enter 'C' or 'P'.")
        play_with_smart_computer()

    if winner == "X":
        print(f"🎉 Smart Computer {PLAYER_X_EMOJI} won the game!")
    elif winner == "O":
        print(f"🎉 Congrats {player2} {PLAYER_O_EMOJI}, you won the game!")
    else:
        print("🤝 It's a tie! Well played!")


# Option menu with emoji and clear choices
def option_menu():
    while True:
        print("\n{0:-^75}".format(" 🎮 WELCOME TO TIC TAC TOE 🎮 "))
        print(
            "\n1️⃣  Play with another Player\n2️⃣  Play with Normal Computer\n3️⃣  Play with Smart Computer\n4️⃣  Exit")
        choice = input("\nEnter Your Choice: ")
        if choice == '1':
            play_with_players()
        elif choice == '2':
            play_with_normal_computer()
        elif choice == '3':
            play_with_smart_computer()
        elif choice == '4':
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please select 1, 2, 3, or 4.")


# Start the game by calling option_menu
option_menu()
