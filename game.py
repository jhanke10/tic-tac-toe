from board import *

turns = ['x', 'o']

#Plays the game
def playGame(board, turn):
	print board

	row = input("Which row do you want to place it in? ")
	col = input("Which col do you want to place it in? ")

	position = board.placePiece(turns[turn], row, col)

	if position != None:
		if board.hasWon(turns[turn], position):
			print turns[turn] + " has won!"
		elif board.gameOver():
			print "Tie game"
		else:
			playGame(board, 1 - turn)

def main():
	board = Board()
	print "Game Start"
	playGame(board, 0)

if __name__ == "__main__":main()