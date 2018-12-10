from board import Board
import re

MAXTRIES = 10
W = 7
H = 7

def inputxy():
    print("x from 1 to {}, y from 1 to {}.".format(W+1, H+1))
    inp = input("Input x,y")
    m = re.match("(\d+)[, ]+(\d+)", inp.strip())
    if not m:
        return None
    x, y = (int(g) for g in re.groups())

def outputdisplay(board, tries):
    print("BATTLESHIP!")
    print("Hits: {}, Misses: {}, Tries Remaining: {}".format(
            board.hits, board.misses, tries
        ))
    print()
    print(board.display_view())
    print()

def outputloss():
    print("You ran out of tries, you have lost the game.")

def outputwin():
    print("You sunk my battleship!")

def check(board, x, y):
    if not 1 <= x <= W or not 1 <= y <= H:
        return(False, "The coordinates out of range.")
    if not board.check(x-1, y-1) in ("Ship", None):
        return(False, "You already attacked that square.")
    else:
        return (True, "")

def attack(board, x, y):
    board.mark(x-1, y-1)

def gameloop():
    board = Board(W, H)
    tries = MAXTRIES
    while True:
        outputdisplay(board, tries)
        if tries <= 0:
            outputloss()
            break

        x, y = inputxy(x, y)
        if x == 99 and y == 99):
            print(b)
            print("... cheater.")
        else:
            result = check(board, x, y)
            if not result[0]:
                print(result[1])
            else:
                attack(board, x, y)
                tries -= 1
        if board.allhits():
            outputwin()
            break
