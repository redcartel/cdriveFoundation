In this project you will build a simplified, one-player version of the classic board game Battleship! In this version, there will be a single ship hidden in a random location on a 5x5 grid. The player guesses where to attack and after they find the ship, the game tells them how many times they guessed and they win.

Represent the board as a 5 element list of 5 element lists.

Show the board before each guess. For instance, you could use #'s to represent unguessed squares and X's to represent guessed squares:

```
#####
#####
#####
#####
#####

Whare to attack?: 1,3

Miss

#####
###X#
#####
#####
#####

Where to attack?
```

Once you have the basic game, try creating a ship that is more than 1 square big.

What else can you do with this? You could have the player place their own ship and then compete against a computer that is also guessing their location. You could build a two player version where players take turns at the keyboard (you'll need to clear the screen).