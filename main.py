##Tic Tac Toe
#Name: Lucas Quinn
#Date: Feb 12, 2021

#1. (Var) Setup the empty board as a list
testBoard = ['no','X','O','X','X','O','O','X','X','X'] #for testing checkWin and checkFull

theBoard = ['no','','','','','','','','','']
             #0  #1 #2 #3 #4 #5 #6 #7 #8 #9

import time       #For any timers
import random     #For RNG

#2. (fun) Print the board.
#in: a 10 item list (either x, o or ' ')
#do: print a graphic for the board
#out: none

def printBoard():
    print(theBoard[7] + " | " + theBoard[8] + " | " + theBoard[9])
    print("---------")
    print(theBoard[4] + " | " + theBoard[5] + " | " + theBoard[6])
    print("---------")
    print(theBoard[1] + " | " + theBoard[2] + " | " + theBoard[3])

#3a. (fun) Determine if player is X or O

player1 = ''
player2 = ''
  

#in: None
#do: get user choice, assign X/O to player1 and 2
#out: None

def chooseLetter(): 
    p1 = str(input("Player 1, what letter do you want? X or O : ")) #Asks for letter
    global player1
    player1 = p1 
    global player2
    if player1 == "X":
      player2 = "O"
      print("")
      print("Player 1 is X, Player 2 is O") #Print who is what letter
    else:
      player2 = "X"
      print("")
      print("Player 1 is O, Player 2 is X")
    

firstplayer = '' #the player who goes first
seondplayer = ''

#3b. (fun) Choose starting player 1 or 2
def chooseStart():
  global firstplayer
  global secondplayer

  randstart = random.randrange(1,3) #Randomly select who goes first
  if randstart == 1:
    print("Player 1 will take the first move")
    firstplayer = 1
    secondplayer = 2
  if randstart == 2:
    print("Player 2 will take the first move")
    firstplayer = 2
    secondplayer = 1

#4. (fun) Get player move
#in: board as list, player as X or O
#do: get user choice (1-9),
#    check if the space is empty,
#    update the board with the X or O at the user location
#out: none


def playerMove(board, player): 
  global theBoard
  if player == 1:
    move1 = int(input("Player 1, What position? "))
    if theBoard[move1] == '':
      theBoard.pop(move1)
      theBoard.insert(move1, player1)
      printBoard()
    else:
      print("Space already taken")
      time.sleep(0.5)
      playerMove(theBoard,firstplayer)

  elif player == 2:
    move2 = int(input("Player 2, What position? "))
    if theBoard[move2] == '':
      theBoard.pop(move2)
      theBoard.insert(move2, player2)
      printBoard()
    else:
      print("Space already taken")
      time.sleep(0.5)
      playerMove(theBoard,firstplayer)
  

#5. (fun) Check Winner
#in: board as list, player as X or O
#do: check all possible win scenarios
#out: True for win, False otherwise
    
def checkWin(board, player):

  if theBoard[7] == theBoard[8] == theBoard[9] != ' ':
    return True

  elif theBoard[4] == theBoard[5] == theBoard[6] != ' ':
    return True

  elif theBoard[1] == theBoard[2] == theBoard[3] != ' ':
    return True

  elif theBoard[1] == theBoard[5] == theBoard[9] != ' ':
    return True

  elif theBoard[3] == theBoard[5] == theBoard[7] != ' ':
    return True

  elif theBoard[1] == theBoard[4] == theBoard[7] != ' ':
    return True

  elif theBoard[2] == theBoard[5] == theBoard[8] != ' ':
    return True

  elif theBoard[3] == theBoard[6] == theBoard[9] != ' ':
    return True

  else:
    return False

#6. (fun) Check if board is full
#Because there are 10 list items for 9 spots,
#the first item theBoard[0] will always be ' '
#in: board as list
#do: count number of empty spaces, if there is no more spaces
#out: return True if board is full, False otherwise


def checkFull(board):
  if '' in board:
    return False
  else:
    return True


#7. Main function


def main():
  
  #print Welcome
  #print instructions

  print("Welcome to python Tic Tac Toe")
  print("----------------------------------------------------------")
  time.sleep(1.5)
  print("The board has 9 spots, this is the layout")
  print("")
  print("7" + " | " + "8" + " | " + "9")
  print("---------")
  print("4" + " | " + "5" + " | " + "6")
  print("---------")
  print("1" + " | " + "2" + " | " + "3")
  print("")
  print("To win, you need to get 3 of your letter in a line, vertically, horizontally, or diagonally")
  print("----------------------------------------------------------")

  #game play
  #get player letter choice

  time.sleep(0.5)
  chooseLetter()
  print("----------------------------------------------------------")
  time.sleep(0.5)
  chooseStart()

  checkFull(theBoard)

  turn = firstplayer

  while checkFull == False:
    playerMove(theBoard,firstplayer)
    ###first player move
        #player chooses move
        #print board
        #check win
        #check board full

    ###second player move
        #player chooses move
        #print baord
        #check win
    
main()


