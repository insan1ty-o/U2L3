from random import random, choice

class TicTacToe:
  def __init__(self):
    self.__board = [[" "]*3 for i in range(0,3)]
    self.__turn = choice(["X","O"]) #next player token (X or O) - initially randomly generated

#ACTIONS
  def __switch_turns(self):
    if self.__turn == "X":
      self.__turn = "O"
    else:
      self.__turn = "X"

  def __check_win(self):
    #determine if a given player has won the game
    win = False

    #check across
    row = 0
    while row != 3:
      if self.__board[row][0] == self.__board[row][1] == self.__board[row][2] == "X" or self.__board[row][0] == self.__board[row][1] == self.__board[row][2] == "O":
        win = True
      row += 1
    
    #check vertically
    row = 0
    while row != 3:
      if self.__board[0][row] ==  self.__board[1][row] == self.__board[2][row] == "X" or self.__board[0][row] ==  self.__board[1][row] == self.__board[2][row] == "O":
        win = True
      row += 1

    #check diagonally
    if self.__board[0][0] == self.__board[1][1] == self.__board[2][2] == "X" or self.__board[0][0] == self.__board[1][1] == self.__board[2][2] == "O":
      win = True

    if self.__board[2][0] == self.__board[1][1] == self.__board[0][2] == "X" or self.__board[2][0] == self.__board[1][1] == self.__board[0][2] == "O":
      win = True

    self.__switch_turns()
    return win, self.__turn

  def place_token(self, rowSelect, slotSelect):
    #accepts board position, updates __board
    #print(f">{self.__board[rowSelect][slotSelect]}< ; {len(self.__board[rowSelect][slotSelect])}")
    if self.__board[rowSelect][slotSelect] == " ":
      self.__board[rowSelect][slotSelect] = self.__turn
      return True
    else:
      return False

  def is_winner(self):
    #returns if a player (X or O) has won
    winner = self.__check_win()
    return winner, self.__turn
#ETC
  def __str__(self):
    return f"""                 1   2   3
                ___________
             1 | {self.__board[0][0]} | {self.__board[0][1]} | {self.__board[0][2]} |
               |-----------|
             2 | {self.__board[1][0]} | {self.__board[1][1]} | {self.__board[1][2]} |
               |-----------|
             3 | {self.__board[2][0]} | {self.__board[2][1]} | {self.__board[2][2]} |
                -----------""" 