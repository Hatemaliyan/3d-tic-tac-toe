# 3d-tic-tac-toe
A more challenging and fun variation of regular tic-tac-toe.
# Introduction
This is a Python program for a game called "Ultimate Tic Tac Toe". The game is played on a 3x3 grid of 3x3 grids. The objective of the game is to win three grids in a row. The game can be played by two players or one player against the computer.

# How to Play
Run the program in a Python environment.
Enter the names of the players.
Choose whether to play against the computer or another player.
Choose your symbol from the options provided.
The game will randomly select the first player.
Players take turns placing their symbol on the board.
The first player to win three grids in a row wins the game.
The program will display the winner and the number of wins for each player.

Players can choose to play again or exit the game.
# Functions
The program includes the following functions:

pName(): This function prompts the players to enter their names and returns a list of the player names.
radPlayer(players): This function randomly selects the first player from the list of players.
choose_w(players): This function prompts the players to choose their symbol from a list of options and returns a dictionary of the player names and their chosen symbols.
crUser(cp, players): This function changes the current player to the other player.
create_board(): This function creates the game board.
print_board(tables): This function prints the game board.
move(tables, playerchoice, cp): This function prompts the player to make a move and updates the game board.
is_Win(boards, playerchoice, cp): This function checks if a player has won the game.
win_Display(): This function displays a message when a player wins the game.
winners_B(cp, winnerdic): This function updates the dictionary of winners with the current winner.
main(): This function runs the game.

#Dependencies
This program requires the random and time modules.

#Conclusion
This program is a fun and challenging game that can be played by two players or one player against the computer. The program includes several functions that make the game easy to play and understand.
