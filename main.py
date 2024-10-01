# Matthew Fahnestock
# U2 L3
# Creating a game of Tic Tac Toe

from tic_tac_toe import TicTacToe
from random import choice
from time import sleep
import os

def validate(game, row, slot):
  condition = game.place_token(row, slot)
  return condition

def rowSelection():
  rowSelect = input("Select a row (1,2,3): ")
  while rowSelect != int():
    try:
      rowSelect = int(rowSelect)
      if rowSelect <= 3:
        return rowSelect - 1
      else:
        rowSelect = input("Select a row (1,2,3):  ")
    except:
      rowSelect = input("Select a row (1,2,3):  ")
  
def slotSelection():
  slotSelect = input("Select a slot (1,2,3): ")
  while slotSelect != int():
    try:
      slotSelect = int(slotSelect)
      if slotSelect <= 3:
        return slotSelect - 1
      else:
        slotSelect = input("Select a row (1,2,3):  ")
    except:
      slotSelect = input("Select a slot (1,2,3):  ")

def main():
  ttt = TicTacToe()
  winCondition = False
  while winCondition == False:
    print(ttt)
    #PLAYER
    playervalid = False
    row = rowSelection()
    slot = slotSelection()
    while playervalid == False:
      selection = validate(ttt, row, slot)
      if selection == True:
        playervalid = True
        winner, player = ttt.is_winner()
      else:
        row = rowSelection()
        slot = slotSelection()
    os.system("clear")
    print(ttt)

    #COMPUTER
    print("The computer is thinking...")
    cpuvalid = False
    compRow = int(choice([0,1,2]))
    compSlot = int(choice([0,1,2]))
    sleep(1.8)

    while cpuvalid == False:
      selection = validate(ttt, compRow, compSlot)
      if selection == True:
        cpuvalid = True
        winner, player = ttt.is_winner()
      else:
        compRow = int(choice([0,1,2]))
        compSlot = int(choice([0,1,2]))
    os.system("clear")
    if winner[0] == True:
      winCondition = True

  print(f"\t   Player '{player}' wins!")
  print("""             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
              `````````""")
if __name__ == "__main__":
  os.system("clear")
  main()
