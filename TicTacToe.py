# Set up the game board as a list
board = ["-", "-", "-",
		"-", "-", "-",
		"-", "-", "-"]

# Define a function to print the game board
def print_board():
	print(board[0] + " | " + board[1] + " | " + board[2])
	print(board[3] + " | " + board[4] + " | " + board[5])
	print(board[6] + " | " + board[7] + " | " + board[8])

# Define a function to handle a player's turn
def take_turn(player):
	print(player + "'s turn.")
	position = input("Choose a position from 1-9: ")
	while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
		position = input("Invalid input. Choose a position from 1-9: ")
	position = int(position) - 1
	while board[position] != "-":
		position = int(input("Position already taken. Choose a different position: ")) - 1
	board[position] = player
	print_board()

# Define a function to check if the game is over
def check_game_over():
	# Check for a win
	if (board[0] == board[1] == board[2] != "-") or \
	(board[3] == board[4] == board[5] != "-") or \
	(board[6] == board[7] == board[8] != "-") or \
	(board[0] == board[3] == board[6] != "-") or \
	(board[1] == board[4] == board[7] != "-") or \
	(board[2] == board[5] == board[8] != "-") or \
	(board[0] == board[4] == board[8] != "-") or \
	(board[2] == board[4] == board[6] != "-"):
		return "win"
	# Check for a tie
	elif "-" not in board:
		return "tie"
	# Game is not over
	else:
		return "play"

# Define the main game loop
def play_game():
	print_board()
	current_player = "X"
	game_over = False
	while not game_over:
		take_turn(current_player)
		game_result = check_game_over()
		if game_result == "win":
			print(current_player + " wins!")
			game_over = True
		elif game_result == "tie":
			print("It's a tie!")
			game_over = True
		else:
			# Switch to the other player
			current_player = "O" if current_player == "X" else "X"
# Start the game
play_game()

# What is Tic-Tac-Toe?
# Tic-Tac-Toe is among the games played between two players played on a 3 x 3 square grid. 
# Each player inhabits a cell in their respective turns, keeping the objective of placing 
# three similar marks in a vertical, horizontal, or diagonal pattern. 
# The first player utilizes the Cross (X) as the marker, whereas the other utilizes the Naught or Zero (O).

# Rules of the Game

# The game is to be played between two people (in this program between HUMAN and COMPUTER).
# One of the player chooses ‘O’ and the other ‘X’ to mark their respective cells.
# The game starts with one of the players and the game ends when one of the players has one whole row/ column/ diagonal 
# filled with his/her respective character (‘O’ or ‘X’).
# If no one wins, then the game is said to be draw.

# Implementation In our program the moves taken by the computer and the human are chosen randomly. 
# We use rand() function for this. What more can be done in the program? 
# The program is in not played optimally by both sides because the moves are chosen randomly. 
# The program can be easily modified so that both players play optimally (which will fall under the category of Artificial Intelligence). 
# Also the program can be modified such that the user himself gives the input (using scanf() or cin). 
# The above changes are left as an exercise to the readers. 
# Winning Strategy – An Interesting Fact If both the players play optimally then it is destined that 
# you will never lose (“although the match can still be drawn”). 
# It doesn’t matter whether you play first or second.
# In another ways – “ Two expert players will always draw ”. Isn’t this interesting ? 