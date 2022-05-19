import random
dashboard = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]
game_on = True
winner = None
player="X"

#function for display dashboard....
def display_dashboard():
  print("\n")
  print("\t"+ dashboard[0] + " | " + dashboard[1] + " | " + dashboard[2])
  print("\t---------")
  print("\t"+ dashboard[3] + " | " + dashboard[4] + " | " + dashboard[5])
  print("\t---------")
  print("\t"+ dashboard[6] + " | " + dashboard[7] + " | " + dashboard[8])
  print("\n")

#function for play_with_players trun
def players_turn(player,player1,player2):
  
  if player=="X":
    print(f"{player1} {[player]} now yours turn.")
    pos= input("Choose a pos from (1-9): ")
    valid = False
  if player=="O":
    print(f"{player2} {[player]} now yours turn.")
    pos= input("Choose a position from (1-9): ")
    valid = False
    
  while not valid:
    while pos not in ['1','2','3','4','5','6','7','8','9']:
        pos = input("Choose a position from (1-9): ")
    pos=int(pos)-1
    if dashboard[pos] == " ":
      valid = True
    else:
      print("This pos is not vacant can't go there. Go again.")
    
  dashboard[pos] = player
  display_dashboard()
  
#function for play_with_normal_computers trun  
def normal_computer_turn(player,player1,player2):
  
  if player=="X":
    pos= str(gen_random_index())
    print(f"\n{[player]} {player1} entered on {pos}th pos .")
    valid = False
    
  if player=="O":
    print(f"{player2} {[player]} now yours turn.")
    pos= input("Choose a pos from (1-9),,,: ")
    valid = False
      
  while not valid:
    while pos not in ['1','2','3','4','5','6','7','8','9']:
        pos = input("Choose a position from (1-9)...: ")
    pos=int(pos)-1
    if dashboard[pos] == " ":
      valid = True
    else:
      print("This pos is not vacant can't go there. Go again.")
    
  dashboard[pos] = player
  display_dashboard()
  
#function for generating random index of play_with_normal_compute.....  
def gen_random_index():
  pos=random.randint(1,9)
  if dashboard[int(pos)-1] == " ":
      return pos
  else:
      return gen_random_index()


#.......rows,coumns,diaginals checking................
def rows_check():
  global game_on
  if dashboard[0] == dashboard[1] == dashboard[2] != " ":
    game_on= False
    return dashboard[0]
  
  if dashboard[3] == dashboard[4] == dashboard[5] != " ":
    game_on= False
    return dashboard[3]
  
  if dashboard[6] == dashboard[7] == dashboard[8] != " ":
    game_on= False
    return dashboard[6] 
  else:
    return None
  
def columns_check():
  global game_on
  if dashboard[0] == dashboard[3] == dashboard[6] != " ":
    game_on = False
    return dashboard[0]

  if dashboard[1] == dashboard[4] == dashboard[7] != " ":
    
    game_on= False
    return dashboard[1] 

  if dashboard[2] == dashboard[5] == dashboard[8] != " ":
    game_on= False
    return dashboard[2] 
  else:
    return None

def diagonals_check():
  global game_on
  if dashboard[0] == dashboard[4] == dashboard[8] != " ":
    game_on= False
    return dashboard[0] 

  if dashboard[2] == dashboard[4] == dashboard[6] != " ":
    game_on= False
    return dashboard[2]
  else:
    return None

def check_game_status():
  global winner
  global game_on
  #checking for winner...
  if rows_check():
    winner = rows_check()
  elif columns_check():
    winner = columns_check()
  elif diagonals_check():
    winner = diagonals_check()
  else:
    winner = None
    
  #checking for tie
  if ' ' not in dashboard:
    game_on = False
    return True
  else:
    return False
  
def switch_player():
  global player
  if player == "X":
    player = "O"
  elif player == "O":
    player = "X"
    
def play_again():
  for i in range(len(dashboard)):
    dashboard.insert(i," ")
  global game_on,winner,player
  game_on = True
  winner = None
  player="X"
  option_menu(player)


#function for play with users
def play_with_players():
  player1=input("\nEnter Player1's Name: ")
  player2=input("Enter Player2's Name: ")

  if player1.isalpha() and player2.isalpha():
    display_dashboard()
    # Loop until the game stops (winner or tie)
    while game_on:
      players_turn(player,player1,player2)
      check_game_status()
      switch_player()
    #printing the winner or tie
    if winner == "X":
      print(f"Congrats! Mr/Mrs {player1} You won the game.\n")
    if winner == "O":
      print(f"Congrats! Mr/Mrs {player2} You won the game.\n")
    elif winner == None:
      print("Game Tie..Better luck next time for both of you..\n")
  else:
      print("Please enter name as alphabet characters only")
      return play_with_players()
    
#function for play with normal computer
def play_with_normal_computer():
  player1="Normal_Computer"
  player2=input("\nEnter Player2's Name: ")
  if player2.isalpha():
  # Loop until the game stops (winner or tie)
    while game_on:
      normal_computer_turn(player,player1,player2)
      check_game_status()
      switch_player()
    #printing the winner or tie
    if winner == "X":
      print(f"Congrats! {player1} You won the game.\n")
    if winner == "O":
      print(f"Congrats! {player2} You won the game.\n")
    elif winner == None:
      print("Game Tie..Better luck next time for both of you..\n")
  else:
    print("Please enter name as alphabet characters only")
    return play_with_normal_computer()

#Play with Smart Computer.......................

def print_board(board):
  print("\n")
  print("\t"+ board[1] + " | " + board[2] + " | " + board[3])
  print("\t---------")
  print("\t"+ board[4] + " | " + board[5] + " | " + board[6])
  print("\t---------")
  print("\t"+ board[7] + " | " + board[8] + " | " + board[9])
  print("\n")

def checking_space(pos):
    if board[pos] == ' ':
        return True
    else:
        return False
    
def insert_letter(letter,pos):
    if checking_space(pos):
        if letter=='X':
            print(f"\n{play1} {[letter]} entered on position {pos}\n")
        else:
            print(f"\n{play2} {[letter]} entered on position {pos}\n")
        
        board[pos] = letter
        print_board(board)
        if (checking_draw()):
            print("Game Tie..Better luck next time for both of you..\n")
            play_again2()
        if checking_for_win():
            if letter == 'X':
                print(f"Congrats! {play1} You won the game.\n")
                play_again2()
            else:
                print(f"Congrats! {play2} You won the game.\n")
                play_again2()
        return
    else:
        print("Can't insert there!")
        pos = int(input("Please enter new position:  "))
        insert_letter(letter, pos)
        return


def checking_for_win():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False


def checking_marks(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False

def checking_draw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True

def play_turn(play):
    print(f"{play2} {['O']} now yours turn.")
    pos= input("\nChoose a position from (1-9): ")
    valid= False
    while not valid:
        while pos not in ['1','2','3','4','5','6','7','8','9']:
            pos = input("\nChoose a position from (1-9): ")
        valid=True
    pos=int(pos)
    insert_letter(play, pos)
    return


def smart_computer_turn(comp,play):
    best_score = -1000
    bestMove = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = comp
            score = best_move(comp,board, 0, False)
            board[key] = ' '
            if (score > best_score):
                best_score = score
                bestMove = key

    insert_letter(comp, bestMove)
    return

def best_move(comp,board, depth, isMaximizing):
    if (checking_marks(comp)):
        return 1
    elif (checking_marks(play)):
        return -1
    elif (checking_draw()):
        return 0

    if (isMaximizing):
        best_score = -1000
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = comp
                score = best_move(comp,board, depth + 1, False)
                board[key] = ' '
                if (score > best_score):
                    best_score = score
        return best_score

    else:
        best_score = 1000
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = play
                score = best_move(comp,board, depth + 1, True)
                board[key] = ' '
                if (score < best_score):
                    best_score = score
        return best_score

board = {1:' ', 2:' ', 3:' ',
         4:' ', 5:' ', 6:' ',
         7:' ', 8:' ', 9:' '}

def play_with_smart_computer():
    global play1,play2,play,comp
    play1="Smart Computer"
    play = 'O'
    comp = 'X'
    while True:
        person=input("Enter Player name: ")
        if person.isalpha():
            play2=person
            break
        else:
            print("Player name must be alphabet only!")

    choice=input("\nWho goes first Smart Computer or Player\n\nEnter 'C' for Smart Computer and 'P' for Player: ")
    if choice.upper()=='C' or choice.upper()=='P':
        print_board(board)
        while not checking_for_win():
            if choice=='p':
                play_turn(play)
                smart_computer_turn(comp,play)
            else:
                smart_computer_turn(comp,play)
                play_turn(play)
    else:
        print("Choice must be alphabet only!")
            
def play_again2():
  for i in range(len(board)+1):
    board[i]=(" ")
  global game_on,winner,player,play,comp
  game_on = True
  winner = None
  player="X"
  play='O'
  comp='X'
  option_menu(player)
  
#function for play with smart computer
def option_menu(player):
  cmd=True
  while cmd:
    print("\n{0:-^75s}".format(" WELCOME TO TIC TAC TOE GAME "))
    print("\n1.Play with Users\t2.Play with Computer(Normal)\t3.Play with Computer(AI)\n\n4.Exit")
    choice=input("\nEnter Your Choice: ")
    if choice.isdigit():
      if choice=='1':
        play_with_players()
        while True:
          print("\nDou You want to play again? If yes then enter 'Y' or Enter 'q' for quit. ")
          ch=input("\nEnter Your Choice: ")
          if (ch.upper())=='Y':
            play_again()
          elif (ch.upper())=='Q':
            cmd=False
            break
          else:
            print("\nYou have entered Invalid characters!")
            
      elif choice=='2':
        play_with_normal_computer()
        while True:
          print("\nDou You want to play again? If yes then enter 'Y' or Enter 'q' for quit. ") 
          ch=input("\nEnter Your Choice: ")
          if (ch.upper()=='Y'):
            play_again()
          elif (ch.upper()=='Q'):
            cmd=False
            break
          else:
            print("\nYou have entered Invalid characters!")

      elif choice=='3':
        play_with_smart_computer()
        
      elif choice=='4':
        break

      else:
        print("You have entered Invalid options, please select from (1-4) only")
    else:
      print("\nChoice must be digit only! Try again")

#game will start from here...
option_menu(player)
